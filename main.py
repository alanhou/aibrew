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

def save_to_markdown(summaries, processed_urls):
    """Saves to _posts/ folder with Jekyll Frontmatter. Appends if file exists."""

    today = datetime.datetime.now()
    date_filename = today.strftime("%Y-%m-%d") # Format: 2026-02-04
    display_date = today.strftime("%B %d, %Y")

    # Jekyll requires posts to be in a specific folder structure
    output_dir = "_posts"
    os.makedirs(output_dir, exist_ok=True)
    filename = f"{output_dir}/{date_filename}-daily-ai-digest.md"

    # Check if file already exists (for appending)
    if os.path.exists(filename):
        # Append new content to existing file
        with open(filename, "a", encoding="utf-8") as f:
            for summary in summaries:
                f.write(summary + "\n\n---\n\n")
        print(f"✅ Appended {len(summaries)} new articles to: {filename}")
    else:
        # Create new file with frontmatter
        frontmatter = f"""---
layout: post
title: "Daily Tech Digest: {display_date}"
date: {date_filename}
categories: [AI, News]
tags: [HackerNews, Bilingual]
author: "AI Editor"
---

## 📅 Daily Trends / 每日动态
*Generated by AI, Curated for Developers.*

---
"""
        with open(filename, "w", encoding="utf-8") as f:
            f.write(frontmatter)
            for summary in summaries:
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
        # Extract URLs from "Read Original" links
        urls = re.findall(r'\[Read Original / 阅读原文\]\((https?://[^\)]+)\)', content)
        processed.update(urls)
    return processed

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # Get already processed URLs to avoid duplicates
    processed_urls = get_processed_urls()
    print(f"📋 Already processed {len(processed_urls)} URLs today")

    stories = get_hn_top_stories(limit=10)  # Fetch more to account for skips
    blog_content = []
    new_urls = []

    for story in stories:
        url = story['url']
        if url in processed_urls:
            print(f"⏭️ Skipping (already processed): {story['title']}")
            continue

        print(f"Processing: {story['title']}")
        html_content, title = fetch_article_content(url)

        if html_content:
            summary = summarize_bilingual(title, html_content)
            if summary:
                formatted = f"{summary}\n\n**[Read Original / 阅读原文]({url})**"
                blog_content.append(formatted)
                new_urls.append(url)

        # Stop after getting 5 new articles
        if len(blog_content) >= 5:
            break

    if blog_content:
        save_to_markdown(blog_content, new_urls)
    else:
        print("ℹ️ No new content to add")