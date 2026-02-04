# AIBrew - Daily AI & Tech Digest

An automated bilingual blog that curates and summarizes the latest in AI, programming, and tech from multiple sources.

一个自动化的双语博客，从多个来源整理和总结最新的 AI、编程和技术内容。

## Features / 功能特点

- **Hacker News** - Top stories with AI-generated bilingual summaries
- **GitHub Trending** - Popular repositories and fast-moving new projects
- **Hugging Face** - Trending ML models and interactive Spaces
- **YouTube** - Tech videos from subscribed channels with transcript-based summaries

---

- **Hacker News** - 热门文章，配有 AI 生成的双语摘要
- **GitHub 热门** - 流行仓库和快速崛起的新项目
- **Hugging Face** - 热门机器学习模型和交互式 Spaces
- **YouTube** - 订阅频道的技术视频，基于字幕生成摘要

## How It Works / 工作原理

The blog runs automatically every 4 hours via GitHub Actions:

1. Fetches content from Hacker News, GitHub, Hugging Face, and YouTube APIs
2. Retrieves full article content, READMEs, and video transcripts when available
3. Generates bilingual (English/Chinese) summaries using an LLM
4. Publishes to a Jekyll-based GitHub Pages site

---

博客通过 GitHub Actions 每 4 小时自动运行：

1. 从 Hacker News、GitHub、Hugging Face 和 YouTube API 获取内容
2. 获取完整文章内容、README 和视频字幕（如有）
3. 使用 LLM 生成双语（英文/中文）摘要
4. 发布到基于 Jekyll 的 GitHub Pages 网站

## Setup / 配置

### Required Secrets / 必需的密钥

Add these to your GitHub repository secrets:

| Secret | Description |
|--------|-------------|
| `LLM_API_KEY` | API key for your LLM provider |
| `LLM_BASE_URL` | Base URL for the LLM API |
| `LLM_MODEL_NAME` | Model name to use |
| `YOUTUBE_API_KEY` | YouTube Data API v3 key (optional) |

### YouTube API Key / YouTube API 密钥

1. Go to [Google Cloud Console](https://console.cloud.google.com/)
2. Create a new project or select existing
3. Enable "YouTube Data API v3"
4. Create credentials > API Key
5. Add to GitHub Secrets as `YOUTUBE_API_KEY`

---

1. 访问 [Google Cloud Console](https://console.cloud.google.com/)
2. 创建新项目或选择现有项目
3. 启用 "YouTube Data API v3"
4. 创建凭据 > API 密钥
5. 添加到 GitHub Secrets，命名为 `YOUTUBE_API_KEY`

### Customization / 自定义

Edit `main.py` to customize:

```python
# YouTube channels to follow (handles or channel IDs)
YOUTUBE_CHANNELS = [
    "@Fireship",
    "@freecodecamp",
    # Add your own channels here
]
```

## Content Sources / 内容来源

| Source | Content | Limit |
|--------|---------|-------|
| Hacker News | Top stories | 3 articles |
| GitHub Trending | Daily trending repos | 3 repos |
| GitHub Fast-Moving | New repos gaining stars | 2 repos |
| Hugging Face Models | Trending ML models | 3 models |
| Hugging Face Spaces | Trending interactive demos | 2 spaces |
| YouTube Channels | Videos from subscribed channels | 3 videos |
| YouTube Trending | Popular tech videos | 2 videos |

## Local Development / 本地开发

```bash
# Install dependencies / 安装依赖
pip install requests openai beautifulsoup4 readability-lxml youtube-transcript-api

# Set environment variables / 设置环境变量
export LLM_API_KEY="your-api-key"
export LLM_BASE_URL="your-base-url"
export LLM_MODEL_NAME="your-model"
export YOUTUBE_API_KEY="your-youtube-key"  # Optional

# Run the script / 运行脚本
python main.py
```

## License / 许可证

MIT License
