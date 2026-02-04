import requests
import os
import datetime
import re
from openai import OpenAI
from readability import Document

# --- CONFIGURATION ---
API_KEY = os.environ.get("LLM_API_KEY")
BASE_URL = os.environ.get("LLM_BASE_URL") # Change if using a different provider
MODEL_NAME = os.environ.get("LLM_MODEL_NAME")
YOUTUBE_API_KEY = os.environ.get("YOUTUBE_API_KEY")

# YouTube channels to fetch videos from (handles like @fireship or channel IDs)
YOUTUBE_CHANNELS = [
    "@Fireship",
    "@freecodecamp",
    "@AndrejKarpathy",
    "@LennysPodcast",
    "@lexfridman",
    "@baoyu_",
    "@AI-qb8eh",
    "@ycombinator",
    "@DwarkeshPatel"
]

if not API_KEY:
    raise ValueError("API Key not found! Set LLM_API_KEY in GitHub Secrets.")

client = OpenAI(api_key=API_KEY, base_url=BASE_URL)

def get_hn_top_stories(limit=5):
    """Fetches top story IDs and then their details from Hacker News."""
    print(f"📡 Fetching top {limit} stories from Hacker News...")
    try:
        top_ids = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json").json()[:limit]
        stories = []
        for item_id in top_ids:
            item = requests.get(f"https://hacker-news.firebaseio.com/v0/item/{item_id}.json").json()
            if item.get('url'):
                stories.append(item)
        return stories
    except Exception as e:
        print(f"Error fetching HN stories: {e}")
        return []

def get_github_trending(limit=5):
    """Fetches trending repositories from GitHub."""
    print(f"📡 Fetching top {limit} trending repos from GitHub...")
    from bs4 import BeautifulSoup

    repos = []
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}

    try:
        # Fetch daily trending
        response = requests.get("https://github.com/trending", headers=headers, timeout=15)
        soup = BeautifulSoup(response.text, 'html.parser')

        for article in soup.select('article.Box-row')[:limit]:
            # Extract repo name
            h2 = article.select_one('h2 a')
            if not h2:
                continue
            repo_path = h2.get('href', '').strip('/')
            if not repo_path:
                continue

            # Extract description
            desc_elem = article.select_one('p')
            description = desc_elem.get_text(strip=True) if desc_elem else ""

            # Extract stars today
            stars_today = ""
            stars_elem = article.select_one('span.d-inline-block.float-sm-right')
            if stars_elem:
                stars_today = stars_elem.get_text(strip=True)

            # Extract language
            lang_elem = article.select_one('span[itemprop="programmingLanguage"]')
            language = lang_elem.get_text(strip=True) if lang_elem else "Unknown"

            repos.append({
                'title': repo_path,
                'url': f"https://github.com/{repo_path}",
                'description': description,
                'language': language,
                'stars_today': stars_today,
                'source': 'github_trending'
            })

        print(f"✅ Found {len(repos)} trending repos")
        return repos
    except Exception as e:
        print(f"Error fetching GitHub trending: {e}")
        return []

def get_github_fast_moving(limit=5):
    """Fetches fast-moving repos using GitHub Search API (most stars in last 7 days)."""
    print(f"📡 Fetching top {limit} fast-moving repos from GitHub...")
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)',
        'Accept': 'application/vnd.github.v3+json'
    }

    # Search for repos created in last 7 days, sorted by stars
    week_ago = (datetime.datetime.now() - datetime.timedelta(days=7)).strftime('%Y-%m-%d')

    try:
        response = requests.get(
            f"https://api.github.com/search/repositories?q=created:>{week_ago}&sort=stars&order=desc&per_page={limit}",
            headers=headers,
            timeout=15
        )
        data = response.json()

        repos = []
        for item in data.get('items', [])[:limit]:
            repos.append({
                'title': item['full_name'],
                'url': item['html_url'],
                'description': item.get('description', '') or '',
                'language': item.get('language', 'Unknown') or 'Unknown',
                'stars': item.get('stargazers_count', 0),
                'source': 'github_fast_moving'
            })

        print(f"✅ Found {len(repos)} fast-moving repos")
        return repos
    except Exception as e:
        print(f"Error fetching GitHub fast-moving repos: {e}")
        return []

def get_youtube_channel_videos(channels, limit=3):
    """Fetches latest videos from specified YouTube channels (handles or IDs)."""
    if not YOUTUBE_API_KEY:
        print("⚠️ YOUTUBE_API_KEY not set, skipping YouTube channel videos")
        return []

    print(f"📡 Fetching videos from {len(channels)} YouTube channels...")
    videos = []

    # Get videos published in last 48 hours
    published_after = (datetime.datetime.utcnow() - datetime.timedelta(hours=48)).strftime('%Y-%m-%dT%H:%M:%SZ')

    for channel in channels:
        # Resolve handle to channel ID if needed
        if channel.startswith('@'):
            channel_id = resolve_youtube_handle(channel)
            if not channel_id:
                print(f"⚠️ Could not resolve handle {channel}")
                continue
        else:
            channel_id = channel

        try:
            response = requests.get(
                "https://www.googleapis.com/youtube/v3/search",
                params={
                    'key': YOUTUBE_API_KEY,
                    'channelId': channel_id,
                    'part': 'snippet',
                    'order': 'date',
                    'type': 'video',
                    'publishedAfter': published_after,
                    'maxResults': 3
                },
                timeout=15
            )
            data = response.json()

            for item in data.get('items', []):
                snippet = item['snippet']
                video_id = item['id']['videoId']
                videos.append({
                    'title': snippet['title'],
                    'url': f"https://www.youtube.com/watch?v={video_id}",
                    'channel': snippet['channelTitle'],
                    'description': snippet['description'],
                    'published_at': snippet['publishedAt'],
                    'source': 'youtube_channel'
                })
        except Exception as e:
            print(f"Error fetching videos from channel {channel}: {e}")

    # Sort by published date and limit
    videos.sort(key=lambda x: x['published_at'], reverse=True)
    print(f"✅ Found {len(videos[:limit])} recent channel videos")
    return videos[:limit]

def resolve_youtube_handle(handle):
    """Resolves a YouTube handle (@username) to a channel ID."""
    if not YOUTUBE_API_KEY:
        return None

    # Remove @ if present
    handle = handle.lstrip('@')

    try:
        response = requests.get(
            "https://www.googleapis.com/youtube/v3/channels",
            params={
                'key': YOUTUBE_API_KEY,
                'forHandle': handle,
                'part': 'id'
            },
            timeout=15
        )
        data = response.json()
        items = data.get('items', [])
        if items:
            return items[0]['id']
    except Exception as e:
        print(f"Error resolving handle {handle}: {e}")
    return None

def get_youtube_trending_tech(limit=3):
    """Fetches trending tech/programming videos from YouTube."""
    if not YOUTUBE_API_KEY:
        print("⚠️ YOUTUBE_API_KEY not set, skipping YouTube trending")
        return []

    print(f"📡 Fetching top {limit} trending tech videos from YouTube...")

    # Search for videos from last 7 days
    published_after = (datetime.datetime.utcnow() - datetime.timedelta(days=7)).strftime('%Y-%m-%dT%H:%M:%SZ')

    keywords = ["programming tutorial", "tech news", "coding", "AI machine learning"]
    videos = []

    for keyword in keywords:
        try:
            response = requests.get(
                "https://www.googleapis.com/youtube/v3/search",
                params={
                    'key': YOUTUBE_API_KEY,
                    'q': keyword,
                    'part': 'snippet',
                    'order': 'viewCount',
                    'type': 'video',
                    'publishedAfter': published_after,
                    'maxResults': 5,
                    'relevanceLanguage': 'en'
                },
                timeout=15
            )
            data = response.json()

            for item in data.get('items', []):
                snippet = item['snippet']
                video_id = item['id']['videoId']
                video_url = f"https://www.youtube.com/watch?v={video_id}"

                # Avoid duplicates
                if any(v['url'] == video_url for v in videos):
                    continue

                videos.append({
                    'title': snippet['title'],
                    'url': video_url,
                    'channel': snippet['channelTitle'],
                    'description': snippet['description'],
                    'published_at': snippet['publishedAt'],
                    'source': 'youtube_trending'
                })
        except Exception as e:
            print(f"Error searching YouTube for '{keyword}': {e}")

    print(f"✅ Found {len(videos[:limit])} trending tech videos")
    return videos[:limit]

def summarize_youtube_video(video_info):
    """Summarizes a YouTube video based on title and description."""
    system_prompt = """
    You are an expert tech editor for a bilingual blog covering YouTube tech videos.
    1. Analyze the video information.
    2. Output a concise summary in English and Chinese.
    3. STRICTLY use Markdown formatting.
    4. Highlight: what the video covers, key topics, why it's worth watching.
    5. Structure:
       ### 🎬 [Video Title]
       **Channel:** [Channel Name]
       * What the video covers
       * Key topics discussed
       * Why it's worth watching

       ### 🎬 [Video Title in Chinese or keep original]
       **频道:** [Channel Name]
       * 视频内容概述
       * 主要话题
       * 为何值得观看
    """

    user_prompt = f"""
Video Title: {video_info['title']}
Channel: {video_info['channel']}
Description: {video_info['description']}
Published: {video_info['published_at']}
"""

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"AI Generation Error: {e}")
        return None

def fetch_github_readme(url):
    """Fetches README content from GitHub repository using raw API."""
    match = re.match(r'https?://github\.com/([^/]+)/([^/]+)/?', url)
    if not match:
        return None, None
    owner, repo = match.groups()
    repo = repo.split('#')[0].split('?')[0]  # Remove fragments/query params

    # Try common README filenames via raw.githubusercontent.com
    readme_names = ['README.md', 'readme.md', 'README.rst', 'README.txt', 'README']
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}

    for readme in readme_names:
        raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/main/{readme}"
        try:
            response = requests.get(raw_url, headers=headers, timeout=10)
            if response.status_code == 200 and len(response.text) > 100:
                return response.text, f"{owner}/{repo}"
        except:
            pass
        # Try master branch as fallback
        raw_url = f"https://raw.githubusercontent.com/{owner}/{repo}/master/{readme}"
        try:
            response = requests.get(raw_url, headers=headers, timeout=10)
            if response.status_code == 200 and len(response.text) > 100:
                return response.text, f"{owner}/{repo}"
        except:
            pass
    return None, None

def fetch_article_content(url):
    """Downloads the article and extracts the main text body."""
    # Handle GitHub URLs specially - fetch README directly
    if 'github.com' in url:
        content, title = fetch_github_readme(url)
        if content:
            return content, title

    try:
        headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)'}
        response = requests.get(url, headers=headers, timeout=10)
        doc = Document(response.text)
        summary = doc.summary()
        # Check if content is too short or looks like an error page
        if len(summary) < 500:
            print(f"⚠️ Content too short for {url}, skipping")
            return None, None
        return summary, doc.title()
    except Exception as e:
        print(f"⚠️ Failed to fetch {url}: {e}")
        return None, None

def summarize_bilingual(title, content):
    """Asks Claude to summarize the content."""
    content_snippet = content[:12000] # Truncate to save tokens

    system_prompt = """
    You are an expert tech editor for a bilingual blog.
    1. Analyze the content.
    2. Output a summary in English and Chinese.
    3. STRICTLY use Markdown formatting.
    4. Structure:
       ### [English Title]
       * Bullet point 1
       * Bullet point 2

       ### [Chinese Title]
       * Chinese Bullet point 1
       * Chinese Bullet point 2
    """

    user_prompt = f"Title: {title}\n\nContent HTML: {content_snippet}"

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"AI Generation Error: {e}")
        return None

def summarize_from_title(title, url):
    """Creates a brief summary based only on the article title when content is unavailable."""
    system_prompt = """
    You are an expert tech editor for a bilingual blog.
    The article content could not be fetched, but you have the title from Hacker News.
    Based on the title alone, provide a brief introduction about what this article likely covers.
    Be honest that this is based on the title only.

    1. Output in English and Chinese.
    2. STRICTLY use Markdown formatting.
    3. Structure:
       ### [Title]
       * Brief description of what this article likely covers based on the title
       * Why it might be interesting to readers

       ### [Chinese Title or Translation]
       * 根据标题推测的文章内容简介
       * 为何值得关注
    """

    user_prompt = f"Article Title: {title}\nURL: {url}"

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"AI Generation Error: {e}")
        return None

def summarize_github_repo(repo_info, readme_content):
    """Summarizes a GitHub repository with its metadata."""
    content_snippet = readme_content[:10000] if readme_content else ""

    system_prompt = """
    You are an expert tech editor for a bilingual blog covering GitHub repositories.
    1. Analyze the repository information and README.
    2. Output a concise summary in English and Chinese.
    3. STRICTLY use Markdown formatting.
    4. Highlight: what it does, key features, why it's trending/notable.
    5. Structure:
       ### [Repo Name] - [Brief English Description]
       * What it does
       * Key features
       * Why it's notable

       ### [Repo Name] - [Brief Chinese Description]
       * 功能介绍
       * 主要特点
       * 为何值得关注
    """

    metadata = f"""
Repository: {repo_info['title']}
Language: {repo_info.get('language', 'Unknown')}
Description: {repo_info.get('description', 'No description')}
"""
    if repo_info.get('stars_today'):
        metadata += f"Stars Today: {repo_info['stars_today']}\n"
    if repo_info.get('stars'):
        metadata += f"Total Stars: {repo_info['stars']}\n"

    user_prompt = f"{metadata}\n\nREADME Content:\n{content_snippet}"

    try:
        response = client.chat.completions.create(
            model=MODEL_NAME,
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            temperature=0.3
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"AI Generation Error: {e}")
        return None

def save_to_markdown(hn_summaries, github_trending_summaries, github_fast_summaries, youtube_summaries=None):
    """Saves to _posts/ folder with Jekyll Frontmatter. Appends if file exists."""
    if youtube_summaries is None:
        youtube_summaries = []

    today = datetime.datetime.now()
    date_filename = today.strftime("%Y-%m-%d")
    display_date = today.strftime("%B %d, %Y")

    output_dir = "_posts"
    os.makedirs(output_dir, exist_ok=True)
    filename = f"{output_dir}/{date_filename}-daily-ai-digest.md"

    # Generate description for frontmatter
    total_hn = len(hn_summaries)
    total_trending = len(github_trending_summaries)
    total_fast = len(github_fast_summaries)
    total_youtube = len(youtube_summaries)
    description = f"Today's digest: {total_hn} Hacker News articles, {total_trending} GitHub trending repos, {total_fast} fast-moving projects, {total_youtube} YouTube videos. 今日精选：{total_hn}篇黑客新闻，{total_trending}个热门项目，{total_fast}个快速崛起项目，{total_youtube}个YouTube视频。"

    if os.path.exists(filename):
        # Append new content to existing file
        with open(filename, "a", encoding="utf-8") as f:
            if hn_summaries:
                for summary in hn_summaries:
                    f.write(summary + "\n\n---\n\n")
            if github_trending_summaries:
                f.write("\n## 🔥 GitHub Trending / GitHub 热门项目\n\n---\n\n")
                for summary in github_trending_summaries:
                    f.write(summary + "\n\n---\n\n")
            if github_fast_summaries:
                f.write("\n## 🚀 Fast-Moving Repos / 快速崛起项目\n\n---\n\n")
                for summary in github_fast_summaries:
                    f.write(summary + "\n\n---\n\n")
            if youtube_summaries:
                f.write("\n## 🎬 YouTube Tech Videos / YouTube 技术视频\n\n---\n\n")
                for summary in youtube_summaries:
                    f.write(summary + "\n\n---\n\n")
        total = len(hn_summaries) + len(github_trending_summaries) + len(github_fast_summaries) + len(youtube_summaries)
        print(f"✅ Appended {total} new articles to: {filename}")
    else:
        frontmatter = f"""---
layout: post
title: "Daily Tech Digest: {display_date}"
date: {date_filename}
description: "{description}"
categories: [AI, News, GitHub, YouTube]
tags: [HackerNews, GitHub, Trending, YouTube, Bilingual]
author: "AI Editor"
---

## 📅 Daily Trends / 每日动态
*Generated by AI, Curated for Developers.*

Today's highlights include top stories from Hacker News, trending GitHub repositories, fast-moving new projects, and tech videos from YouTube.

今日精选包括黑客新闻热门文章、GitHub 热门仓库、快速崛起的新项目以及 YouTube 技术视频。

---

## 📰 Hacker News Highlights / 黑客新闻精选

---
"""
        with open(filename, "w", encoding="utf-8") as f:
            f.write(frontmatter)
            for summary in hn_summaries:
                f.write(summary + "\n\n---\n\n")
            if github_trending_summaries:
                f.write("\n## 🔥 GitHub Trending / GitHub 热门项目\n\n---\n\n")
                for summary in github_trending_summaries:
                    f.write(summary + "\n\n---\n\n")
            if github_fast_summaries:
                f.write("\n## 🚀 Fast-Moving Repos / 快速崛起项目\n\n---\n\n")
                for summary in github_fast_summaries:
                    f.write(summary + "\n\n---\n\n")
            if youtube_summaries:
                f.write("\n## 🎬 YouTube Tech Videos / YouTube 技术视频\n\n---\n\n")
                for summary in youtube_summaries:
                    f.write(summary + "\n\n---\n\n")
        print(f"✅ Created new post: {filename}")

def get_processed_urls():
    """Returns set of URLs already processed today."""
    today = datetime.datetime.now()
    date_filename = today.strftime("%Y-%m-%d")
    filename = f"_posts/{date_filename}-daily-ai-digest.md"

    if not os.path.exists(filename):
        return set()

    processed = set()
    with open(filename, "r", encoding="utf-8") as f:
        content = f.read()
        # Extract URLs from "Read Original", "View Repository", and "Watch Video" links
        urls = re.findall(r'\[Read Original / 阅读原文\]\((https?://[^\)]+)\)', content)
        urls += re.findall(r'\[View Repository / 查看仓库\]\((https?://[^\)]+)\)', content)
        urls += re.findall(r'\[Watch Video / 观看视频\]\((https?://[^\)]+)\)', content)
        processed.update(urls)
    return processed

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # Get already processed URLs to avoid duplicates
    processed_urls = get_processed_urls()
    print(f"📋 Already processed {len(processed_urls)} URLs today")

    # --- Hacker News ---
    stories = get_hn_top_stories(limit=10)
    hn_content = []

    for story in stories:
        url = story['url']
        if url in processed_urls:
            print(f"⏭️ Skipping (already processed): {story['title']}")
            continue

        print(f"Processing HN: {story['title']}")
        html_content, title = fetch_article_content(url)

        if html_content:
            summary = summarize_bilingual(title, html_content)
        else:
            # Fallback: use HN title when content fetch fails
            print(f"📝 Using title-only summary for: {story['title']}")
            summary = summarize_from_title(story['title'], url)

        if summary:
            formatted = f"{summary}\n\n**[Read Original / 阅读原文]({url})**"
            hn_content.append(formatted)
            processed_urls.add(url)

        if len(hn_content) >= 3:
            break

    # --- GitHub Trending ---
    trending_repos = get_github_trending(limit=5)
    github_trending_content = []

    for repo in trending_repos:
        url = repo['url']
        if url in processed_urls:
            print(f"⏭️ Skipping (already processed): {repo['title']}")
            continue

        print(f"Processing Trending: {repo['title']}")
        readme_content, _ = fetch_github_readme(url)
        summary = summarize_github_repo(repo, readme_content)

        if summary:
            formatted = f"{summary}\n\n**[View Repository / 查看仓库]({url})**"
            github_trending_content.append(formatted)
            processed_urls.add(url)

        if len(github_trending_content) >= 3:
            break

    # --- GitHub Fast-Moving ---
    fast_repos = get_github_fast_moving(limit=5)
    github_fast_content = []

    for repo in fast_repos:
        url = repo['url']
        if url in processed_urls:
            print(f"⏭️ Skipping (already processed): {repo['title']}")
            continue

        print(f"Processing Fast-Moving: {repo['title']}")
        readme_content, _ = fetch_github_readme(url)
        summary = summarize_github_repo(repo, readme_content)

        if summary:
            formatted = f"{summary}\n\n**[View Repository / 查看仓库]({url})**"
            github_fast_content.append(formatted)
            processed_urls.add(url)

        if len(github_fast_content) >= 2:
            break

    # --- YouTube Channel Videos ---
    youtube_content = []
    channel_videos = get_youtube_channel_videos(YOUTUBE_CHANNELS, limit=3)

    for video in channel_videos:
        url = video['url']
        if url in processed_urls:
            print(f"⏭️ Skipping (already processed): {video['title']}")
            continue

        print(f"Processing YouTube Channel: {video['title']}")
        summary = summarize_youtube_video(video)

        if summary:
            formatted = f"{summary}\n\n**[Watch Video / 观看视频]({url})**"
            youtube_content.append(formatted)
            processed_urls.add(url)

        if len(youtube_content) >= 3:
            break

    # --- YouTube Trending Tech ---
    trending_videos = get_youtube_trending_tech(limit=5)

    for video in trending_videos:
        url = video['url']
        if url in processed_urls:
            print(f"⏭️ Skipping (already processed): {video['title']}")
            continue

        print(f"Processing YouTube Trending: {video['title']}")
        summary = summarize_youtube_video(video)

        if summary:
            formatted = f"{summary}\n\n**[Watch Video / 观看视频]({url})**"
            youtube_content.append(formatted)
            processed_urls.add(url)

        if len(youtube_content) >= 5:  # 3 channel + 2 trending = 5 total
            break

    # --- Save Results ---
    if hn_content or github_trending_content or github_fast_content or youtube_content:
        save_to_markdown(hn_content, github_trending_content, github_fast_content, youtube_content)
    else:
        print("ℹ️ No new content to add")