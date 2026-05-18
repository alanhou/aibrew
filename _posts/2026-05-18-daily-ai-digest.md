---
title: "Daily Tech Digest: May 18, 2026"
date: 2026-05-18
description: "Today's digest: 12 Hacker News articles, 3 GitHub trending repos, 11 fast-moving projects, 11 YouTube videos, 0 Hugging Face models. 今日精选：12篇黑客新闻，3个热门项目，11个快速崛起项目，11个YouTube视频，0个Hugging Face模型。"
categories: [Daily Digest]
tags: [HackerNews, GitHub, YouTube, HuggingFace]
pin: false
---

### 安全研究人员称微软在 BitLocker 中植入后门，并发布漏洞利用程序

* 根据标题推测，本文可能报道了一位安全研究人员声称微软在 Windows 磁盘加密功能 BitLocker 中故意创建了后门。该研究人员似乎已发布了一个漏洞利用程序来演示这个安全漏洞，可能允许未经授权访问加密驱动器。
* 这对读者很重要，因为 BitLocker 被企业和个人广泛用于保护敏感数据。如果确实存在后门——无论是故意还是意外——都可能对数据安全、隐私以及对微软加密解决方案的信任产生严重影响。漏洞利用程序的发布使这成为一个紧迫且关键的安全问题。

**注意：** 此摘要仅基于文章标题。实际文章可能包含更多背景信息、技术细节、微软的回应，或关于所谓后门性质的澄清。

**[Read Original / 阅读原文](https://www.techspot.com/news/112410-security-researcher-microsoft-secretly-built-backdoor-bitlocker-releases.html)**


## 🔥 GitHub Trending / GitHub 热门项目

### OpenHuman - Your Private Personal AI Super Intelligence

* **What it does**: OpenHuman is an open-source agentic AI assistant that integrates deeply into your daily workflow, connecting to 118+ services (Gmail, Notion, GitHub, Slack, etc.) via one-click OAuth and automatically building a comprehensive knowledge base from your data.

* **Key features**: Features a desktop mascot that speaks and joins Google Meets as a real participant; Memory Tree system that compresses all your documents, emails, and chats into an Obsidian-compatible wiki stored locally in SQLite; TokenJuice compression reduces LLM costs by up to 80%; auto-fetch pulls fresh data every 20 minutes; batteries-included tools for web search, coding, voice (STT/TTS), and model routing across reasoning/fast/vision LLMs.

* **Why it's notable**: Unlike other AI agents that take weeks to learn your context, OpenHuman gets to know you in minutes through automatic data syncing and intelligent compression. Built in Rust with privacy-first architecture (local-first, encrypted), it eliminates vendor sprawl with a single subscription model and provides a clean UI-first experience requiring no terminal setup—making powerful agentic AI accessible without the typical configuration overhead.

---

### OpenHuman - 私密的个人 AI 超级智能助手

* **功能介绍**: OpenHuman 是一个开源的智能 AI 助手,通过一键 OAuth 深度集成 118+ 个服务(Gmail、Notion、GitHub、Slack 等),自动从你的数据中构建全面的知识库,深度融入日常工作流程。

* **主要特点**: 配备会说话的桌面吉祥物,可作为真实参与者加入 Google Meet 会议;Memory Tree 系统将所有文档、邮件和聊天记录压缩为本地 SQLite 存储的 Obsidian 兼容 wiki;TokenJuice 压缩技术可降低 LLM 成本达 80%;每 20 分钟自动获取最新数据;内置网页搜索、编码工具、语音(STT/TTS)和模型路由等全套功能。

* **为何值得关注**: 与其他需要数周才能学习上下文的 AI 智能体不同,OpenHuman 通过自动数据同步和智能压缩在几分钟内就能了解你。采用 Rust 构建,隐私优先架构(本地优先、加密存储),单一订阅模式消除供应商依赖,提供简洁的 UI 优先体验,无需终端配置——让强大的智能体 AI 变得触手可及,没有传统的配置负担。

**[View Repository / 查看仓库](https://github.com/tinyhumansai/openhuman)**

### CLI-Anything - Making ALL Software Agent-Native

* **What it does**: CLI-Anything transforms any software into agent-ready command-line interfaces, enabling AI agents (like Pi, OpenClaw, Claude Code, Cursor) to directly control applications through standardized CLIs. It bridges the gap between AI agents and the world's software by generating harnesses that wrap existing tools.

* **Key features**: 
  - **CLI-Hub package manager** (`pip install cli-anything-hub`) for browsing, installing, and managing community-built CLIs
  - **18+ production harnesses** covering CAD (FreeCAD, Blender), creative tools (Inkscape, Krita, MuseScore), game engines (Godot, Unreal), browsers, workflow automation (n8n, Dify), and more
  - **2,269 passing tests** with comprehensive unit and E2E coverage
  - **Progressive disclosure documentation** with SKILL.md files that guide agents through capabilities
  - **Unified skills directory** with `npx skills add` installation flow
  - **Real-world demos** showing agents producing CAD builds, 3D scenes, diagrams, gameplay, and subtitles

* **Why it's notable**: With 306 stars today, CLI-Anything addresses a critical infrastructure gap as software transitions from human-centric UIs to agent-native interfaces. It's actively maintained with daily updates, has a thriving contributor community (open PR process), and provides production-ready harnesses that let AI agents interact with professional software tools. The project's vision—"Today's Software Serves Humans. Tomorrow's Users will be Agents"—positions it at the forefront of the agentic computing shift.

---

### CLI-Anything - 让所有软件都能被 AI 智能体调用

* **功能介绍**: CLI-Anything 将任何软件转换为智能体就绪的命令行接口,使 AI 智能体(如 Pi、OpenClaw、Claude Code、Cursor)能够通过标准化 CLI 直接控制应用程序。它通过生成包装现有工具的适配器,在 AI 智能体与全球软件之间架起桥梁。

* **主要特点**:
  - **CLI-Hub 包管理器**(`pip install cli-anything-hub`)用于浏览、安装和管理社区构建的 CLI
  - **18+ 个生产级适配器**,涵盖 CAD(FreeCAD、Blender)、创意工具(Inkscape、Krita、MuseScore)、游戏引擎(Godot、Unreal)、浏览器、工作流自动化(n8n、Dify)等
  - **2,269 个通过测试**,具有全面的单元测试和端到端测试覆盖
  - **渐进式文档披露**,通过 SKILL.md 文件引导智能体了解功能
  - **统一技能目录**,支持 `npx skills add` 安装流程
  - **真实世界演示**,展示智能体生成 CAD 构建、3D 场景、图表、游戏玩法和字幕

* **为何值得关注**: CLI-Anything 今日获得 306 星标,解决了软件从以人为中心的 UI 向智能体原生接口转型过程中的关键基础设施缺口。项目保持活跃,每日更新,拥有蓬勃发展的贡献者社区(开放 PR 流程),并提供生产就绪的适配器,让 AI 智能体能够与专业软件工具交互。该项目的愿景——"今天的软件服务人类,明天的用户将是智能体"——使其处于智能体计算变革的最前沿。

**[View Repository / 查看仓库](https://github.com/HKUDS/CLI-Anything)**

### Cal.diy - Community-Driven Open Source Scheduling Platform

* **What it does**: Cal.diy is a fully self-hosted scheduling infrastructure that lets you manage appointments, bookings, and calendar integrations without any commercial dependencies. It's a 100% MIT-licensed fork of Cal.com with all enterprise features removed.

* **Key features**: Built with Next.js, tRPC, and Prisma; supports PostgreSQL databases; includes Docker setup for quick local development; provides complete calendar scheduling functionality including integrations with various calendar providers; no license keys or commercial accounts required.

* **Why it's notable**: Gaining 425 stars today because it offers a truly open-source alternative to commercial scheduling platforms. Unlike "open core" models, Cal.diy removes all proprietary enterprise code, giving self-hosters full control over their scheduling infrastructure. It's ideal for developers and organizations who want scheduling capabilities without vendor lock-in, though it requires technical expertise to deploy and maintain.

---

### Cal.diy - 社区驱动的开源日程安排平台

* **功能介绍**: Cal.diy 是一个完全自托管的日程安排基础设施，可以管理预约、预订和日历集成，无需任何商业依赖。这是 Cal.com 的 100% MIT 许可分支版本，移除了所有企业功能。

* **主要特点**: 使用 Next.js、tRPC 和 Prisma 构建；支持 PostgreSQL 数据库；提供 Docker 快速本地开发环境；包含完整的日历调度功能和多种日历服务集成；无需许可证密钥或商业账户。

* **为何值得关注**: 今日获得 425 星标，因为它提供了真正开源的商业日程安排平台替代方案。与"开放核心"模式不同，Cal.diy 移除了所有专有企业代码，让自托管用户完全掌控其日程安排基础设施。适合希望拥有日程安排功能但不想被供应商锁定的开发者和组织，但需要具备服务器管理和数据库配置的技术能力。

**[View Repository / 查看仓库](https://github.com/calcom/cal.diy)**


## 🚀 Fast-Moving Repos / 快速崛起项目

### YellowKey - BitLocker Bypass Vulnerability Exploit

* **What it does**: Demonstrates a critical vulnerability that allows bypassing Windows BitLocker disk encryption protection through Windows Recovery Environment manipulation
* **Key features**: 
  - Requires only a USB stick with specific FsTx folder structure
  - Works by exploiting Windows Recovery Environment (WinRE) components
  - Grants unrestricted access to BitLocker-protected volumes without requiring the encryption key
  - Affects Windows 11, Server 2022, and Server 2025 (Windows 10 not affected)
* **Why it's notable**: The researcher suggests this may be an intentional backdoor rather than an accidental bug, as the vulnerable component exists only in WinRE with unique functionality not found in standard Windows installations. This represents a severe security flaw in Microsoft's flagship disk encryption technology, disclosed publicly with Microsoft's security teams' involvement.

---

### YellowKey - BitLocker 加密绕过漏洞利用工具

* **功能介绍**: 展示了一个严重的安全漏洞,可通过 Windows 恢复环境操作绕过 Windows BitLocker 磁盘加密保护
* **主要特点**:
  - 仅需一个包含特定 FsTx 文件夹结构的 U 盘
  - 利用 Windows 恢复环境(WinRE)组件中的漏洞
  - 无需加密密钥即可获得对 BitLocker 保护卷的完全访问权限
  - 影响 Windows 11、Server 2022 和 Server 2025(Windows 10 不受影响)
* **为何值得关注**: 研究者认为这可能是一个故意留下的后门而非意外漏洞,因为该漏洞组件仅存在于 WinRE 中,且具有标准 Windows 安装中不存在的独特功能。这代表了微软旗舰磁盘加密技术中的严重安全缺陷,已在微软安全团队参与下公开披露。

**[View Repository / 查看仓库](https://github.com/Nightmare-Eclipse/YellowKey)**

### Zero - A Systems Programming Language Designed for AI Agents

* **What it does**: Zero is a systems language specifically designed for building small native tools that AI agents can use. It compiles to native executables with explicit effect handling, predictable memory management, and structured compiler output that agents can understand.

* **Key features**: 
  - Systems-level performance with C-like efficiency
  - Explicit effects system for predictable behavior
  - Structured compiler output designed for agent consumption
  - Native compilation to small executables
  - Built-in tooling for checking, building, and analyzing code
  - Commands like `zero routes`, `zero skills`, and `zero graph` for agent-oriented workflows

* **Why it's notable**: Zero represents a novel approach to programming language design—optimizing not just for human developers, but for AI agents that need to write, understand, and execute code. As AI coding assistants become more prevalent, a language with explicit semantics and agent-friendly tooling could become increasingly relevant. With 1,482 stars and backing from Vercel Labs, it's an experimental but serious exploration of what programming languages might look like in an AI-first future.

---

### Zero - 为 AI 智能体设计的系统编程语言

* **功能介绍**: Zero 是一门专为构建小型原生工具而设计的系统级编程语言,特别针对 AI 智能体的使用场景。它可以编译为原生可执行文件,具有显式的副作用处理、可预测的内存管理,以及智能体可以理解的结构化编译器输出。

* **主要特点**:
  - 系统级性能,具有类似 C 语言的执行效率
  - 显式副作用系统,确保行为可预测
  - 专为智能体设计的结构化编译器输出
  - 编译为小型原生可执行文件
  - 内置代码检查、构建和分析工具
  - 提供 `zero routes`、`zero skills`、`zero graph` 等面向智能体的工作流命令

* **为何值得关注**: Zero 代表了编程语言设计的新方向——不仅为人类开发者优化,更为需要编写、理解和执行代码的 AI 智能体而设计。随着 AI 编程助手日益普及,一门具有明确语义和智能体友好工具链的语言可能变得越来越重要。该项目获得 1,482 个星标,并由 Vercel Labs 支持,是对 AI 优先时代编程语言形态的严肃探索。

**[View Repository / 查看仓库](https://github.com/vercel-labs/zero)**


## 🎬 YouTube Tech Videos / YouTube 技术视频

### 🎬 Netflix was created because of a late fee - thanks, Blockbuster!

**Channel:** freeCodeCamp.org

* What the video covers: The origin story of Netflix and how a Blockbuster late fee inspired its creation
* Key topics discussed: The founding moment of Netflix, the problem with traditional video rental stores, and how frustration with late fees led to a revolutionary business model
* Why it's worth watching: A fascinating entrepreneurial story that shows how everyday frustrations can spark billion-dollar ideas. Great for anyone interested in startup history, business innovation, or how tech companies disrupt traditional industries.

---

### 🎬 Netflix 的诞生源于一笔滞纳金 - 感谢 Blockbuster!

**频道:** freeCodeCamp.org

* 视频内容概述: Netflix 的起源故事,以及 Blockbuster 的滞纳金如何启发了它的创立
* 主要话题: Netflix 的创立契机、传统录像带租赁店的痛点、以及滞纳金的烦恼如何催生了革命性的商业模式
* 为何值得观看: 一个引人入胜的创业故事,展示了日常生活中的不便如何激发出价值数十亿美元的创意。适合对创业历史、商业创新或科技公司如何颠覆传统行业感兴趣的观众。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=8C-lYCzCVX4)**

### 🎬 Why we're at the beginning of the AI hardware boom | Caitlin Kalinowski (ex–OpenAI, Meta, Apple)

**Channel:** Lenny's Podcast

* **What the video covers:** An in-depth conversation with Caitlin Kalinowski, who has led hardware development at three tech giants (Apple, Meta, and OpenAI), discussing the emerging AI hardware revolution and her experience building robotics and hardware teams from the ground up at OpenAI.

* **Key topics discussed:** The current state and future trajectory of AI hardware development, insights from building hardware at scale across different companies, the intersection of AI and robotics, and what makes this moment a pivotal inflection point for physical AI products.

* **Why it's worth watching:** Rare insider perspective from someone who has shaped hardware strategy at the world's leading tech companies. Kalinowski offers unique insights into how AI is moving from software into physical products, and why we're only at the beginning of a major hardware transformation. Essential viewing for anyone interested in the future of AI, product development, or hardware entrepreneurship.

---

### 🎬 为什么我们正处于 AI 硬件繁荣的起点 | Caitlin Kalinowski（前 OpenAI、Meta、Apple）

**频道:** Lenny's Podcast

* **视频内容概述:** 与 Caitlin Kalinowski 的深度对话，她曾在三大科技巨头（Apple、Meta 和 OpenAI）领导硬件开发，讨论新兴的 AI 硬件革命以及她在 OpenAI 从零开始组建机器人和硬件团队的经验。

* **主要话题:** AI 硬件发展的现状和未来趋势、在不同公司大规模构建硬件的见解、AI 与机器人技术的交叉领域，以及为什么当前时刻是物理 AI 产品的关键转折点。

* **为何值得观看:** 来自塑造了全球领先科技公司硬件战略的业内人士的罕见视角。Kalinowski 提供了关于 AI 如何从软件转向物理产品的独特见解，以及为什么我们仅仅处于重大硬件变革的开端。对于任何对 AI 未来、产品开发或硬件创业感兴趣的人来说都是必看内容。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=G5WTgB87rYQ)**

### 🎬 Why did humans suddenly start making art 50,000 years ago? - David Reich

**Channel:** Dwarkesh Patel

* What the video covers: An exploration of the sudden emergence of sophisticated human art and symbolic behavior approximately 50,000 years ago, featuring insights from geneticist David Reich
* Key topics discussed: The archaeological evidence for the "creative explosion," potential genetic or cognitive changes that enabled artistic expression, theories about what triggered this cultural revolution in human history
* Why it's worth watching: David Reich brings a unique genetic and evolutionary perspective to one of anthropology's most intriguing mysteries—why anatomically modern humans existed for tens of thousands of years before suddenly producing cave paintings, sculptures, and complex symbolic artifacts

### 🎬 人类为何在5万年前突然开始创作艺术？- David Reich

**频道:** Dwarkesh Patel

* 视频内容概述: 探讨约5万年前人类突然出现复杂艺术和符号行为的现象,由遗传学家David Reich提供见解
* 主要话题: 关于"创造力大爆发"的考古证据、可能促成艺术表达的基因或认知变化、引发人类历史上这场文化革命的理论
* 为何值得观看: David Reich从独特的遗传学和进化角度解读人类学最引人入胜的谜团之一——为什么解剖学意义上的现代人类存在了数万年后才突然创作出洞穴壁画、雕塑和复杂的符号艺术品

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=8Qs6W0s-erU)**

### 🎬 The Best Local Agentic Coding Workflow (Complete Guide)
**Channel:** Web Dev Simplified

* Comprehensive guide to setting up and using local AI models for coding workflows
* Covers the complete process from installation to practical implementation of agentic coding assistants
* Worth watching for developers who want privacy, cost savings, and full control over their AI coding tools without relying on cloud services

### 🎬 最佳本地智能编码工作流程（完整指南）
**频道:** Web Dev Simplified

* 全面介绍如何设置和使用本地 AI 模型进行编码工作流程
* 涵盖从安装到实际应用智能编码助手的完整过程
* 适合希望在保护隐私、节省成本的同时完全掌控 AI 编码工具的开发者观看，无需依赖云服务

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=UngVdAsQEiU)**

### 🎬 Do I NEED to learn CODING to make games?!
**Channel:** Crashsune Academy

* What the video covers: Addresses the common question of whether coding knowledge is essential for game development, exploring both code-based and no-code approaches to creating games
* Key topics discussed: Different pathways into game development, visual scripting tools vs traditional programming, no-code game engines and their capabilities, when coding skills become necessary
* Why it's worth watching: Perfect for aspiring game developers unsure about their technical path, provides practical guidance on choosing between learning to code or using visual tools based on project goals and career aspirations

### 🎬 做游戏一定要学编程吗?!
**频道:** Crashsune Academy

* 视频内容概述: 探讨游戏开发是否必须掌握编程知识,分析代码开发和无代码开发两种途径的优劣
* 主要话题: 游戏开发的不同入门路径、可视化脚本工具与传统编程的对比、无代码游戏引擎的功能及局限性、何时需要掌握编程技能
* 为何值得观看: 适合对技术路线犹豫不决的游戏开发初学者,根据项目目标和职业规划提供实用的学习路径建议

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=7KXtysJYYr0)**

### FOSDEM 2026 - Mercurial, 20 Years and Counting: How Are We Still Alive and Kicking?

* Mercurial is a Distributed Version Control System created in 2005 that has remained continuously active for two decades
* Despite losing the popularity battle to Git in the 2010s, Mercurial has fostered modern tooling, introduced innovative ideas, and spawned recent tools like Sapling and Jujutsu from its community
* The project maintains sustained development funding and stays competitive, yet most people mistakenly believe it's dead
* The talk explores this paradox by examining key events, contributor profiles, and technical/community aspects that shaped Mercurial's trajectory
* Key topics include: how Mercurial survived the Git dominance, its hidden impacts on the broader ecosystem, how corporate involvement reshaped the project, and what attracts new users in 2025
* The presentation uses Mercurial's history to assess the current state of version control, predict its future, and demonstrate the enduring relevance of community-based open source

### FOSDEM 2026 - Mercurial，20 年依然坚挺：我们如何存活至今？

* Mercurial 是一个创建于 2005 年的分布式版本控制系统，二十年来持续保持活跃开发
* 尽管在 2010 年代的流行度竞争中输给了 Git，Mercurial 仍在培育现代化工具、引入创新理念，并从其社区中孵化出 Sapling 和 Jujutsu 等新工具
* 该项目获得持续的开发资金支持并保持竞争力，但大多数人误以为它已经死亡
* 本次演讲通过审视关键事件、贡献者概况以及技术和社区方面，探讨这一悖论及 Mercurial 的发展轨迹
* 核心议题包括：Mercurial 如何在 Git 主导下生存、它对更广泛生态系统的隐性影响、企业参与如何重塑项目，以及 2025 年吸引新用户的原因
* 演讲利用 Mercurial 的历史评估版本控制的现状、预测其未来，并展示基于社区的开源软件的持久相关性

**[Read Original / 阅读原文](https://fosdem.org/2026/schedule/event/AGWUVH-mercurial-aint-you-dead-yet/)**

### Debian 12 for Doogee U10 Tablet (RK3562 SoC)

* **rkdebian** is a build system that creates a bootable Debian 12 Bookworm image for the Doogee U10 Android tablet powered by Rockchip RK3562 SoC
* Boot Debian from SD card without unlocking bootloader or modifying internal storage; remove SD card to return to stock Android
* Reverse engineered from scratch using AI assistants (Claude, Codex, Gemini) and Firefly RK3562 open-source repositories as reference
* Hardware: RK3562 (4× Cortex-A53 @ 2.0 GHz), 1× NPU core, 4 GB RAM, 10.1" touchscreen (1280×800)
* Most features work: display, 10-point multitouch, Wi-Fi, Bluetooth, audio, microphone, accelerometer, flashlight, battery/charging, USB OTG
* Partial support: 3D acceleration (Panfrost OpenGL ES), cameras (functional but need color calibration)
* Supports local LLM inference on NPU using RKLLM stack; benchmarks show Qwen3-0.6B at ~5 tok/s generation, Qwen2.5-1.5B at ~2 tok/s
* Pre-installed apps: Firefox ESR, Chromium, FreeTube (Flatpak), Drawing, Snapshot camera app, Dolphin file manager, and more
* Build on x86-64 Linux with `./build.sh all`; customize via environment variables (UI session, GPU stack, CPU governor, rootfs size, etc.)
* Known issue: battery may report 0% after extended power-off, fixed by `rk-battery-gauge-fix.service` on boot

---

### Doogee U10 平板电脑的 Debian 12 系统（RK3562 芯片）

* **rkdebian** 是一个构建系统，可为搭载 Rockchip RK3562 芯片的 Doogee U10 安卓平板电脑创建可启动的 Debian 12 Bookworm 镜像
* 从 SD 卡启动 Debian，无需解锁 bootloader 或修改内部存储；移除 SD 卡即可恢复原生安卓系统
* 从零开始逆向工程，使用 AI 助手（Claude、Codex、Gemini）并参考 Firefly RK3562 开源代码库
* 硬件配置：RK3562（4× Cortex-A53 @ 2.0 GHz）、1× NPU 核心、4 GB 内存、10.1 英寸触摸屏（1280×800）
* 大部分功能正常：显示、10 点触控、Wi-Fi、蓝牙、音频、麦克风、加速度计、闪光灯、电池/充电、USB OTG
* 部分支持：3D 加速（Panfrost OpenGL ES）、摄像头（功能正常但需要颜色校准）
* 支持使用 RKLLM 栈在 NPU 上进行本地 LLM 推理；基准测试显示 Qwen3-0.6B 生成速度约 5 tok/s，Qwen2.5-1.5B 约 2 tok/s
* 预装应用：Firefox ESR、Chromium、FreeTube（Flatpak）、Drawing 绘图、Snapshot 相机、Dolphin 文件管理器等
* 在 x86-64 Linux 上使用 `./build.sh all` 构建；可通过环境变量自定义（UI 会话、GPU 栈、CPU 调度器、根文件系统大小等）
* 已知问题：长时间关机后电池可能显示 0%，启动时由 `rk-battery-gauge-fix.service` 修复

**[Read Original / 阅读原文](https://github.com/tech4bot/rk3562deb)**

### The Occasional `ECONNRESET` Error: Debugging TCP Connection Resets Between Local Services

* **Problem**: Two services on the same machine communicate via TCP localhost connection, but the client occasionally receives `ECONNRESET` errors while reading data, with no other errors or crashes logged
* **Root Cause**: When the server closes a socket that still has unread incoming data buffered, the TCP stack sends a RST (reset) packet to the client instead of a graceful FIN
* **Reproduction**: Created a minimal C server/client pair where the server sends 600,000 bytes and immediately closes the connection; adding a `--spam` flag that sends data from client to server (which the server never reads) triggers the `ECONNRESET` reliably
* **Key Insight**: The timing matters - if the server delays `close()` by 1 second with `sleep(1)`, the client successfully reads all data before the RST occurs
* **Real-World Case**: nginx reverse proxy to gunicorn/Flask app where nginx sends HTTP request in two `writev()` calls (headers + body), but gunicorn sometimes only reads the first part before closing the socket, causing RST when unread body data remains
* **Workaround**: Force the Python application to read the entire HTTP body before closing the connection, ensuring no pending data remains when `close()` is called
* **Verification Tools**: Used `tcpdump` to confirm RST packets on the wire, and `strace` on both client and server to trace syscalls and identify the `close()` timing issue
* **Next Steps**: Confirm that `close()` with pending data definitively causes TCP RST, identify whether gunicorn, Flask, or the app is responsible, and report upstream

---

### 偶发的 `ECONNRESET` 错误：调试本地服务间的 TCP 连接重置问题

* **问题描述**：同一台机器上的两个服务通过 TCP localhost 连接通信，但客户端在读取数据时偶尔会收到 `ECONNRESET` 错误，且日志中没有其他错误或崩溃记录
* **根本原因**：当服务器关闭一个仍有未读入站数据缓冲的套接字时，TCP 协议栈会向客户端发送 RST（重置）数据包，而不是优雅的 FIN 包
* **问题复现**：创建了一个最小化的 C 语言服务器/客户端程序，服务器发送 600,000 字节后立即关闭连接；添加 `--spam` 参数让客户端向服务器发送数据（服务器从不读取），可以稳定触发 `ECONNRESET` 错误
* **关键发现**：时序很重要 - 如果服务器在 `close()` 前用 `sleep(1)` 延迟 1 秒，客户端就能在 RST 发生前成功读取所有数据
* **真实案例**：nginx 反向代理到 gunicorn/Flask 应用，nginx 通过两次 `writev()` 调用发送 HTTP 请求（请求头 + 请求体），但 gunicorn 有时只读取第一部分就关闭套接字，导致未读的请求体数据触发 RST
* **解决方案**：强制 Python 应用在关闭连接前读取完整的 HTTP 请求体，确保调用 `close()` 时没有待处理的数据
* **验证工具**：使用 `tcpdump` 确认网络上的 RST 数据包，使用 `strace` 跟踪客户端和服务器的系统调用，识别 `close()` 时序问题
* **后续工作**：确认带有待处理数据的 `close()` 确实会导致 TCP RST，识别责任方是 gunicorn、Flask 还是应用本身，并向上游报告问题

**[Read Original / 阅读原文](https://movq.de/blog/postings/2026-05-05/1/POSTING-en.html)**

### Bun - Incredibly fast all-in-one JavaScript toolkit

* **What it does**: Bun is a complete JavaScript/TypeScript toolkit that combines a runtime, bundler, test runner, and package manager into a single executable. It serves as a drop-in replacement for Node.js with dramatically faster startup times and lower memory usage.

* **Key features**: 
  - Written in Zig and powered by JavaScriptCore for exceptional performance
  - Native TypeScript and JSX support out-of-the-box
  - Built-in test runner, bundler, and package manager
  - Node.js compatible with minimal changes needed
  - Single executable replaces thousands of node_modules
  - Cross-platform support (Linux, macOS, Windows on x64 & ARM64)

* **Why it's notable**: Gaining 908 stars today, Bun represents a paradigm shift in JavaScript tooling by consolidating the entire development workflow into one blazingly fast tool. It eliminates the complexity of managing multiple tools (Node.js, npm, webpack, Jest, etc.) while delivering significantly better performance, making it an attractive modern alternative for JavaScript developers.

---

### Bun - 极速 JavaScript 全能工具包

* **功能介绍**: Bun 是一个完整的 JavaScript/TypeScript 工具包，将运行时、打包器、测试运行器和包管理器整合到单个可执行文件中。它可以直接替代 Node.js，启动速度更快，内存占用更低。

* **主要特点**:
  - 使用 Zig 编写，基于 JavaScriptCore 引擎，性能卓越
  - 原生支持 TypeScript 和 JSX，无需额外配置
  - 内置测试运行器、打包器和包管理器
  - 与 Node.js 兼容，迁移成本极低
  - 单个可执行文件替代数千个 node_modules 依赖
  - 跨平台支持（Linux、macOS、Windows 的 x64 和 ARM64 架构）

* **为何值得关注**: 今日获得 908 星标，Bun 通过将整个开发工作流整合到一个极速工具中，代表了 JavaScript 工具链的范式转变。它消除了管理多个工具（Node.js、npm、webpack、Jest 等）的复杂性，同时提供显著更好的性能，成为 JavaScript 开发者的现代化替代方案。

**[View Repository / 查看仓库](https://github.com/oven-sh/bun)**

### Open Generative AI - Free Open-Source AI Media Generation Studio

* **What it does**: A self-hosted alternative to commercial AI video platforms that generates images and videos using 200+ state-of-the-art models including Flux, Midjourney, Kling, Sora, Veo, and more. Supports text-to-image, image-to-image, text-to-video, image-to-video, and audio-driven lip sync generation.

* **Key features**: 
  - No content filters or prompt restrictions — complete creative freedom
  - Desktop apps for macOS, Windows, and Linux with one-click installers
  - Local model inference support via bundled sd.cpp engine (runs on Apple Silicon) and Wan2GP server integration for video models
  - Four specialized studios: Image, Video, Lip Sync, and Cinema
  - Multi-image input support (up to 14 reference images)
  - Hosted web version available at muapi.ai for zero-setup usage
  - MIT licensed and fully extensible

* **Why it's notable**: Trending with 704 stars today because it eliminates the subscription fees, vendor lock-in, and content restrictions of commercial platforms while offering broader model access than any single provider. The combination of self-hosting capability, local inference options, and a polished desktop experience makes professional AI media generation accessible to everyone. Related ecosystem includes workflow builders and AI clipping tools, positioning it as a comprehensive open-source creative suite.

---

### Open Generative AI - 免费开源 AI 媒体生成工作室

* **功能介绍**: 商业 AI 视频平台的自托管开源替代方案,使用 200 多个最先进的模型(包括 Flux、Midjourney、Kling、Sora、Veo 等)生成图像和视频。支持文本生成图像、图像转图像、文本生成视频、图像生成视频以及音频驱动的唇形同步生成。

* **主要特点**:
  - 无内容过滤或提示词限制 — 完全的创作自由
  - 提供 macOS、Windows 和 Linux 桌面应用,一键安装
  - 支持本地模型推理,内置 sd.cpp 引擎(可在 Apple Silicon 上运行)和 Wan2GP 服务器集成用于视频模型
  - 四个专业工作室:图像、视频、唇形同步和影院
  - 支持多图像输入(最多 14 张参考图像)
  - 提供托管网页版本,零配置即可使用
  - MIT 许可证,完全可扩展

* **为何值得关注**: 今日获得 704 星标,因其消除了商业平台的订阅费用、供应商锁定和内容限制,同时提供比任何单一供应商更广泛的模型访问。自托管能力、本地推理选项和精美桌面体验的结合,使专业 AI 媒体生成对所有人开放。相关生态系统包括工作流构建器和 AI 剪辑工具,将其定位为全面的开源创意套件。

**[View Repository / 查看仓库](https://github.com/Anil-matcha/Open-Generative-AI)**

### native-feel-skill - Cross-Platform Desktop Architecture for Native-Feeling Apps

* **What it does**: Provides a comprehensive architectural blueprint for building cross-platform desktop apps (macOS/Windows) that feel indistinguishable from native applications, using a four-layer architecture: native shell → system WebView → Node backend → Rust core
* **Key features**: Eight architectural tenets distilled from Raycast 2.0; WebKit/WebView2 survival guide addressing common quirks; 75-item ship-readiness audit checklist; typed IPC contract pattern across Rust/Swift/C#/TypeScript; memory optimization strategies; 70+ native convention checks
* **Why it's notable**: Solves the fundamental tension between convenient cross-platform development and near-native performance—two goals that typically conflict. Based on reverse-engineering Raycast Beta.app and real production patterns. Packaged as an Agent Skill that AI coding assistants can automatically load and apply when discussing desktop architecture, making expert-level architectural knowledge instantly accessible during development

---

### native-feel-skill - 打造原生体验的跨平台桌面应用架构指南

* **功能介绍**: 提供完整的架构蓝图,用于构建在 macOS/Windows 上运行且体验媲美原生应用的跨平台桌面软件,采用四层架构:原生外壳 → 系统 WebView → Node 后端 → Rust 核心
* **主要特点**: 从 Raycast 2.0 提炼的八大架构原则;WebKit/WebView2 生存指南解决常见问题;75 项发布就绪审计清单;跨 Rust/Swift/C#/TypeScript 的类型化 IPC 契约模式;内存优化策略;70+ 项原生规范检查
* **为何值得关注**: 解决了跨平台开发便利性与原生性能之间的根本矛盾——这两个目标通常相互冲突。基于对 Raycast Beta.app 的逆向工程和真实生产模式。以 Agent Skill 形式打包,AI 编程助手可在讨论桌面架构时自动加载应用,让专家级架构知识在开发过程中即时可用

**[View Repository / 查看仓库](https://github.com/yetone/native-feel-skill)**

### Gopay_plus_automatic - Automated claude-sonnet-4-5 Plus Subscription via GoPay

* **What it does**: Fully automated tool that subscribes ChatGPT accounts to Plus tier using the Stripe → Midtrans → GoPay payment chain, completing the first month free trial in ~20 seconds given an `access_token`
* **Key features**: Automatic order creation in IDR currency, tokenized payment processing through Indonesian GoPay, automated OTP verification (3 modes: manual, SMS API, WhatsApp), batch subscription support with concurrent processing, systemd deployment ready
* **Why it's notable**: Eliminates manual subscription friction for ChatGPT Plus using Indonesian payment infrastructure; includes anti-fraud bypass strategies and comprehensive deployment guide; 920 stars indicate strong interest in automated subscription workflows despite author's notice that updates have ceased

---

### Gopay_plus_automatic - GoPay 自动订阅 ChatGPT Plus

* **功能介绍**: 全自动 ChatGPT Plus 订阅工具,通过 Stripe → Midtrans → GoPay 支付链路,输入 `access_token` 后约 20 秒内完成首月 0 元试用订阅
* **主要特点**: 自动创建印尼盾订单、通过 GoPay tokenization 完成支付、自动接收并填写 OTP 验证码(支持手动/短信接码平台/WhatsApp 三种模式)、支持批量并发订阅、提供 systemd 生产部署方案
* **为何值得关注**: 利用印尼支付基础设施解决 ChatGPT Plus 订阅痛点,提供完整的风控绕过策略和部署文档;920 星标显示该自动化订阅方案受到广泛关注,尽管作者已声明不再更新

**[View Repository / 查看仓库](https://github.com/ywnd1144/Gopay_plus_automatic)**

### 🎬 They Built This Without Wheels or Metal - David Reich
**Channel:** Dwarkesh Patel

* What the video covers: An exploration of ancient civilizations that achieved remarkable architectural and engineering feats without access to wheels or metal tools
* Key topics discussed: Archaeological evidence of pre-Columbian societies, construction techniques of ancient monuments, technological innovation constraints, insights from geneticist David Reich on population movements and ancient human capabilities
* Why it's worth watching: Challenges common assumptions about technological prerequisites for advanced civilizations; offers fascinating perspective on human ingenuity and problem-solving across different cultural contexts from a leading expert in ancient DNA research

### 🎬 无轮无金属的古代建筑奇迹 - David Reich
**频道:** Dwarkesh Patel

* 视频内容概述: 探讨古代文明如何在没有轮子和金属工具的情况下创造出非凡的建筑和工程成就
* 主要话题: 前哥伦布时期社会的考古证据、古代纪念碑的建造技术、技术创新的限制条件、遗传学家 David Reich 对人口迁徙和古人类能力的见解
* 为何值得观看: 挑战关于先进文明技术前提的常见假设;从古代 DNA 研究领域的顶尖专家视角,展现不同文化背景下人类的创造力和解决问题的能力

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=MnPwF178DhY)**

### 🎬 Claude Code for Beginners Tutorial [Full Course]
**Channel:** freeCodeCamp.org

* What the video covers: A comprehensive beginner-friendly tutorial on Claude Code, teaching how to integrate Anthropic's Claude AI into your development workflow as a coding assistant
* Key topics discussed: Setting up Claude Code, core features and capabilities, practical coding examples, best practices for AI-assisted development, and real-world implementation scenarios
* Why it's worth watching: Full-length course from freeCodeCamp offering structured, hands-on learning for developers wanting to leverage Claude AI for coding tasks—ideal for those new to AI-powered development tools

---

### 🎬 Claude Code 初学者教程 [完整课程]
**频道:** freeCodeCamp.org

* 视频内容概述: 全面的 Claude Code 入门教程，教授如何将 Anthropic 的 Claude AI 无缝集成到开发工作流程中作为编码助手
* 主要话题: Claude Code 的设置配置、核心功能特性、实用编码示例、AI 辅助开发的最佳实践，以及真实场景的应用实现
* 为何值得观看: freeCodeCamp 出品的完整课程，提供结构化的实践学习体验，适合想要利用 Claude AI 进行编码任务的开发者——特别适合 AI 开发工具的新手

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=gh2_PhgZGsM)**

### 🎬 Automate ML Model Development with HuggingFace ML-Intern

**Channel:** Sumit Paul

* **What the video covers:** An automated agent that handles the entire ML model development pipeline using HuggingFace, from dataset discovery to model deployment
* **Key topics discussed:** Dataset search automation, preprocessing workflows, architecture design selection, hyperparameter tuning, and end-to-end ML automation
* **Why it's worth watching:** Shows how to streamline repetitive ML tasks into a single automated workflow, potentially saving hours of manual work in model development cycles. Practical for ML engineers looking to accelerate their experimentation process.

---

### 🎬 使用 HuggingFace ML-Intern 自动化机器学习模型开发

**频道:** Sumit Paul

* **视频内容概述:** 展示一个自动化代理，使用 HuggingFace 处理从数据集发现到模型部署的完整机器学习开发流程
* **主要话题:** 数据集搜索自动化、预处理工作流、架构设计选择、超参数调优以及端到端机器学习自动化
* **为何值得观看:** 演示如何将重复性的机器学习任务整合到单一自动化工作流中，可为模型开发周期节省大量手动工作时间。对希望加速实验流程的机器学习工程师非常实用。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=b17wpueiX1Q)**

### 🎬 Build almost anything #coding #programming #productivity
**Channel:** SetupsAI

* What the video covers: A guide to building diverse projects using coding and programming techniques
* Key topics discussed: Coding fundamentals, programming approaches, and productivity strategies for developers
* Why it's worth watching: Offers practical insights for developers looking to expand their building capabilities and improve workflow efficiency

### 🎬 构建几乎任何东西 #编程 #开发 #效率
**频道:** SetupsAI

* 视频内容概述: 使用编程技术构建各类项目的指南
* 主要话题: 编程基础、开发方法以及提升开发者生产力的策略
* 为何值得观看: 为希望扩展构建能力和提升工作流效率的开发者提供实用见解

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=BxEO4Thm_Qg)**

### GenCAD: Image-Conditional Parametric CAD Generation Model

* **Core Innovation**: GenCAD generates complete parametric CAD command sequences (CAD programs) from images, not just 3D geometry, enabling full editability and manufacturability
* **Problem Addressed**: Traditional AI approaches use meshes, voxels, or point clouds that sacrifice the accuracy and modifiability critical for engineering tasks and manufacturing
* **Four-Stage Architecture**:
  * Autoregressive transformer encoder learns latent representations of CAD command sequences
  * Contrastive learning model aligns joint representations between CAD commands and CAD images
  * Latent diffusion model generates CAD command latents conditioned on input images
  * Decoder converts latents back into parametric CAD command sequences
* **Key Advantage**: Outputs true parametric CAD programs that can be converted to 3D solids via geometry kernels, preserving design intent and enabling design space exploration
* **Impact**: Advances automated design processes by providing precise, modifiable 3D modeling from images rather than fixed geometric representations

---

### 问问宇航员：333小时宇航员问答视频资料

**根据标题推测的文章内容简介：**
* 一个包含333小时宇航员问答环节的合集或档案库，可能来自各种太空任务或公众科普活动
* 内容可能经过整理或可搜索，让人们能够探索宇航员对公众提问的回答，涉及太空旅行、轨道生活及其个人经历
* 可能是"ISS实时追踪"项目的一部分，表明重点关注国际空间站的宇航员

**为何值得关注：**
* 提供了前所未有的机会，直接了解真正去过太空的人的第一手资料
* 333小时代表着海量的太空知识和个人经历档案，这些内容通常分散在不同来源中
* 既能了解太空飞行的技术层面，也能感受在太空生活和工作的人性化体验
* 对任何对太空探索感兴趣的人来说都是宝贵的教育资源

**[Read Original / 阅读原文](https://askanastronaut.issinrealtime.org/)**

### Prolog Coding Horror: Common Pitfalls and Best Practices

* **Losing Solutions**: Prolog programs can be defective by reporting wrong answers or failing to report intended solutions—the latter is worse because wrong answers can be filtered, but missing solutions cannot be recovered
* **Impure Constructs**: Using non-monotonic language constructs like `!/0` (cut), `(-&gt;)/2` (if-then), and `var/1` causes programs to lose solutions; use clean data structures, constraints like `dif/2`, and meta-predicates like `if_/3` instead
* **Global State Modification**: Beginners often modify the global database with `assertz/1` and `retract/1`, creating implicit dependencies; use predicate arguments or semicontext notation to thread state explicitly
* **Impure Output**: Printing answers directly to the terminal with `format/2` prevents reasoning about output and breaks relational generality; let the toplevel report solutions or use pure formatting with `format_//2`
* **Low-Level Constructs**: Using outdated arithmetic predicates like `(is)/2`, `(=:=)/2`, and `(&gt;)/2` makes Prolog harder to teach and learn; use CLP(FD) constraints for declarative integer arithmetic instead
* **Horror Factorial Example**: The traditional factorial implementation with cut and low-level arithmetic fails on the most general query `factorial(N, F)`, either returning only one solution or throwing instantiation errors
* **Pure Solution**: Replacing low-level arithmetic with CLP(FD) constraints (`#&gt;`, `#=`) and removing cuts creates a truly relational program that works for all query modes, including generating all factorial pairs
* **Key Recommendation**: Stay in the pure monotonic subset of Prolog, use declarative constructs, and rebel against outdated practices—not against modern improvements that make the language more general and maintainable

### Prolog 编程恐怖：常见陷阱与最佳实践

* **丢失解决方案**：Prolog 程序可能存在两种缺陷：报告错误答案或未能报告预期解决方案——后者更糟糕，因为错误答案可以过滤，但丢失的解决方案无法恢复
* **不纯构造**：使用非单调语言构造如 `!/0`（cut）、`(-&gt;)/2`（if-then）和 `var/1` 会导致程序丢失解决方案；应使用干净的数据结构、约束如 `dif/2` 和元谓词如 `if_/3`
* **全局状态修改**：初学者常用 `assertz/1` 和 `retract/1` 修改全局数据库，造成隐式依赖；应使用谓词参数或半上下文记法显式传递状态
* **不纯输出**：用 `format/2` 直接打印答案到终端会阻碍对输出的推理并破坏关系的通用性；应让顶层报告解决方案，或使用纯函数格式化如 `format_//2`
* **低级构造**：使用过时的算术谓词如 `(is)/2`、`(=:=)/2` 和 `(&gt;)/2` 使 Prolog 更难教学和学习；应使用 CLP(FD) 约束实现声明式整数算术
* **恐怖阶乘示例**：传统的带 cut 和低级算术的阶乘实现在最通用查询 `factorial(N, F)` 上失败，要么只返回一个解，要么抛出实例化错误
* **纯函数解决方案**：用 CLP(FD) 约束（`#&gt;`、`#=`）替换低级算术并移除 cut，创建真正的关系型程序，适用于所有查询模式，包括生成所有阶乘对
* **核心建议**：保持在 Prolog 的纯单调子集中，使用声明式构造，反抗过时的实践——而非反抗使语言更通用和可维护的现代改进

**[Read Original / 阅读原文](https://www.metalevel.at/prolog/horror)**

### agents-best-practices - Provider-Neutral Agent Harness Design Framework

* **What it does**: A comprehensive skill/reference for designing production-ready agentic systems with proper runtime controls, tool permissions, and safety guardrails. Works across Codex, Claude Code, and other AI agents to generate MVP blueprints, audit existing agents, and design secure tool architectures.

* **Key features**: Provider-neutral agentic loop design with typed tools and permission checks; planning mode with approval gates; context/memory management with auto-compaction; prompt caching optimization; observability, evals, and launch checklists; MCP and connector governance; works for coding, research, operations, finance, healthcare, and other domains.

* **Why it's notable**: Addresses the critical gap between "model proposes actions" and "safe production execution" with a rigorous harness-first approach. Provides concrete blueprints rather than vague best practices, emphasizing that agents need runtime discipline beyond prompts—validation, authorization, structured observations, and budgets. The 724 stars reflect growing recognition that production agents require engineering rigor around the model, not just better prompts.

---

### agents-best-practices - 提供商中立的智能体运行框架设计

* **功能介绍**: 为设计生产级智能体系统提供全面的技能参考,包含完善的运行时控制、工具权限和安全防护。适配 Codex、Claude Code 等多种 AI 智能体,可生成 MVP 蓝图、审计现有智能体、设计安全的工具架构。

* **主要特点**: 提供商中立的智能体循环设计,包含类型化工具和权限检查;带审批门控的规划模式;支持自动压缩的上下文/内存管理;提示缓存优化;可观测性、评估和发布检查清单;MCP 和连接器治理;适用于编码、研究、运维、金融、医疗等多个领域。

* **为何值得关注**: 填补了"模型提议操作"与"安全生产执行"之间的关键空白,采用严格的运行框架优先方法。提供具体蓝图而非模糊的最佳实践,强调智能体需要超越提示词的运行时规范——验证、授权、结构化观察和预算控制。724 星标反映出业界日益认识到生产级智能体需要围绕模型的工程严谨性,而不仅仅是更好的提示词。

**[View Repository / 查看仓库](https://github.com/DenisSergeevitch/agents-best-practices)**

### GenCAD: Image-Conditional Parametric CAD Generation Model

* **Core Innovation**: GenCAD generates complete parametric CAD command sequences (CAD programs) from images, not just 3D geometry, enabling full editability and manufacturability
* **Problem Addressed**: Traditional AI approaches use meshes, voxels, or point clouds that sacrifice the accuracy and modifiability critical for engineering tasks and manufacturing
* **Four-Stage Architecture**:
  * Autoregressive transformer encoder learns latent representations of CAD command sequences
  * Contrastive learning model aligns joint representations between CAD commands and CAD images
  * Latent diffusion model generates CAD command latent representations conditioned on input images
  * Decoder converts latent representations back into parametric CAD command sequences
* **Key Advantage**: Outputs true parametric CAD programs that can be converted to 3D solids via geometry kernels, preserving design intent and enabling design space exploration
* **Impact**: Advances automated design processes by providing precise, modifiable 3D modeling from images while maintaining engineering-grade accuracy

---

### GenCAD：基于图像条件的参数化 CAD 生成模型

* **核心创新**：GenCAD 从图像生成完整的参数化 CAD 命令序列（CAD 程序），而不仅仅是 3D 几何体，实现完全可编辑性和可制造性
* **解决的问题**：传统 AI 方法使用网格、体素或点云表示，牺牲了工程任务和制造所需的精度和可修改性
* **四阶段架构**：
  * 自回归 Transformer 编码器学习 CAD 命令序列的潜在表示
  * 对比学习模型对齐 CAD 命令和 CAD 图像之间的联合表示
  * 潜在扩散模型根据输入图像生成 CAD 命令的潜在表示
  * 解码器将潜在表示转换回参数化 CAD 命令序列
* **关键优势**：输出真正的参数化 CAD 程序，可通过几何内核转换为 3D 实体，保留设计意图并支持设计空间探索
* **影响意义**：通过从图像提供精确、可修改的 3D 建模来推进自动化设计流程，同时保持工程级精度

**[Read Original / 阅读原文](https://gencad.github.io/)**

### Strange Crystals Found Inside Trinity Nuclear Test Wreckage

* Scientists discovered a new type of clathrate crystal inside trinitite, the glasslike material formed from melted sand after the 1945 Trinity nuclear bomb test in New Mexico
* The clathrate has a cagelike chemical structure made of 12-sided and 14-sided silicon atom formations that trap calcium, copper, and iron atoms inside
* This unique material formed under extreme conditions: temperatures above 1,500°C and pressures tens of thousands of times normal atmospheric pressure, all within seconds
* The same trinitite sample previously yielded a quasicrystal in 2021—another rare form of matter with ordered but non-repeating atomic patterns
* Both the clathrate and quasicrystal contain the same four elements (iron, silicon, copper, calcium) but formed in areas with different copper availability
* These discoveries demonstrate how extreme energy events like nuclear detonations, lightning strikes, and asteroid impacts create materials that cannot yet be replicated in laboratories
* The research was published in *Proceedings of the National Academy of Sciences USA* on May 11

### 三位一体核试验残骸中发现奇异晶体

* 科学家在三位一体石（trinitite）中发现了一种新型笼形晶体（clathrate）——这是1945年新墨西哥州三位一体核弹试验后由熔化沙子形成的玻璃状物质
* 该笼形晶体具有独特的化学结构，由12面和14面的硅原子构型组成，内部困住了钙、铜和铁原子
* 这种独特材料在极端条件下形成：温度超过1500°C，压力是正常大气压的数万倍，整个过程仅在数秒内完成
* 同一三位一体石样本在2021年还发现了准晶体——另一种罕见的物质形态，具有有序但不重复的原子排列模式
* 笼形晶体和准晶体都含有相同的四种元素（铁、硅、铜、钙），但在铜元素可用性不同的区域形成
* 这些发现表明，核爆炸、闪电和小行星撞击等极端能量事件能够创造出实验室尚无法复制的材料
* 该研究于5月11日发表在《美国国家科学院院刊》上

**[Read Original / 阅读原文](https://www.scientificamerican.com/article/strange-crystals-found-inside-wreckage-from-the-first-nuclear-bomb-test/)**

### jank Now Has Its Own Custom IR

* jank has developed a custom intermediate representation (IR) to optimize performance and compete with the JVM
* Unlike LLVM IR, jank's IR operates at Clojure's semantic level, understanding vars, transients, persistent data structures, and lazy sequences
* The IR is SSA-based (single static assignment) and represented as a control flow graph (CFG) with basic blocks
* This high-level IR is specifically tailored to jank rather than being a general-purpose VM, enabling language-specific optimizations
* The IR is stored as C++ data structures but can be rendered to Clojure data for debugging and testing
* jank's IR includes instructions for Clojure-specific operations like var dereferencing and dynamic function calls
* This represents a significant shift from delegating optimization to LLVM, allowing jank to optimize compiled code more effectively
* The IR design prioritizes Clojure semantics over portability, as jank is not building a general compiler platform
* As far as known, no other Clojure dialects have implemented a custom IR at this semantic level

### jank 现在拥有自己的自定义中间表示

* jank 开发了自定义中间表示（IR）以优化性能并与 JVM 竞争
* 与 LLVM IR 不同，jank 的 IR 在 Clojure 语义层面运行，理解 vars、transients、持久化数据结构和惰性序列
* 该 IR 基于 SSA（单静态赋值）并表示为控制流图（CFG），包含基本块
* 这个高级 IR 专门为 jank 定制，而非通用虚拟机，能够实现特定于语言的优化
* IR 以 C++ 数据结构存储，但可以渲染为 Clojure 数据用于调试和测试
* jank 的 IR 包含 Clojure 特定操作的指令，如 var 解引用和动态函数调用
* 这标志着从将优化委托给 LLVM 的重大转变，使 jank 能够更有效地优化编译代码
* IR 设计优先考虑 Clojure 语义而非可移植性，因为 jank 不是构建通用编译器平台
* 据了解，没有其他 Clojure 方言在这个语义层面实现过自定义 IR

**[Read Original / 阅读原文](https://jank-lang.org/blog/2026-05-08-optimization/)**

### VGGT-Omega - Multi-View 3D Vision Foundation Model

* **What it does**: VGGT-Omega is a foundation model that jointly predicts camera poses, depth maps, and 3D scene structure from multiple input images or video frames. It processes collections of images to reconstruct camera parameters (extrinsics and intrinsics), dense depth, and confidence maps in a single forward pass.

* **Key features**: 
  - Handles 1-500+ frames with scalable GPU memory usage (6-43GB on A100)
  - Two model variants: 512px resolution base model and 256px text-aligned version
  - Outputs camera poses, depth maps, confidence scores, and optional text alignment embeddings
  - Includes interactive Gradio demo for visualization with point cloud and camera rendering
  - Built by Meta AI and Oxford's Visual Geometry Group

* **Why it's notable**: Accepted as an **Oral presentation at CVPR 2026** (top ~2% of submissions), representing cutting-edge research in multi-view geometry and 3D reconstruction. The model unifies multiple 3D vision tasks (structure-from-motion, depth estimation, camera calibration) into a single transformer-based architecture, with 830 stars indicating strong early community interest.

---

### VGGT-Omega - 多视图3D视觉基础模型

* **功能介绍**: VGGT-Omega 是一个基础模型,可以从多张输入图像或视频帧中联合预测相机位姿、深度图和3D场景结构。它能够处理图像集合,在单次前向传播中重建相机参数(外参和内参)、密集深度图和置信度图。

* **主要特点**:
  - 支持1-500+帧处理,GPU显存占用可扩展(A100上6-43GB)
  - 两个模型版本:512像素分辨率基础模型和256像素文本对齐版本
  - 输出相机位姿、深度图、置信度分数和可选的文本对齐嵌入
  - 包含交互式Gradio演示,可视化点云和相机渲染
  - 由Meta AI和牛津大学视觉几何组联合开发

* **为何值得关注**: 被 **CVPR 2026 接收为口头报告**(约占投稿的前2%),代表了多视图几何和3D重建领域的前沿研究。该模型将多个3D视觉任务(运动恢复结构、深度估计、相机标定)统一到单个基于Transformer的架构中,830个星标显示了社区的强烈早期关注。

**[View Repository / 查看仓库](https://github.com/facebookresearch/vggt-omega)**

### 🎬 Claude Code Just Got an Agent Dashboard
**Channel:** Nate Herk | AI Automation

* **What the video covers:** This video introduces the new Agent Dashboard feature in Claude Code (likely referring to Anthropic's Claude AI coding assistant), demonstrating how it enhances visibility into AI agent operations during development workflows.

* **Key topics discussed:** 
  - The new Agent Dashboard interface and its capabilities
  - How the dashboard improves transparency in AI-assisted coding
  - Practical demonstrations of monitoring agent actions in real-time
  - Integration with existing Claude Code workflows

* **Why it's worth watching:** If you're using Claude for development or interested in AI coding assistants, this video shows how the Agent Dashboard gives you better control and understanding of what the AI is doing behind the scenes—essential for debugging, learning, and trusting AI-generated code.

---

### 🎬 Claude Code 推出智能体仪表板
**频道:** Nate Herk | AI Automation

* **视频内容概述:** 本视频介绍了 Claude Code（可能指 Anthropic 的 Claude AI 编程助手）的全新智能体仪表板功能，展示了它如何增强开发工作流程中对 AI 智能体操作的可见性。

* **主要话题:**
  - 全新智能体仪表板界面及其功能
  - 仪表板如何提高 AI 辅助编程的透明度
  - 实时监控智能体操作的实际演示
  - 与现有 Claude Code 工作流程的集成

* **为何值得观看:** 如果你正在使用 Claude 进行开发或对 AI 编程助手感兴趣，这个视频展示了智能体仪表板如何让你更好地控制和理解 AI 在幕后的操作——这对于调试、学习和信任 AI 生成的代码至关重要。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=ZAaxx3qyT8g)**

<!-- [Title-Only] -->
### The Foundations of a Provably Secure Operating System (PSOS) (1979)

* Based on the title, this article likely covers the theoretical and architectural foundations of PSOS, an early research project aimed at building an operating system with mathematically provable security properties. It probably discusses formal verification methods, security models, and the design principles needed to create an OS where security guarantees can be formally proven rather than just tested.
* Why it might be interesting: This 1979 paper represents pioneering work in formal methods and secure systems design. It's historically significant as one of the earliest attempts to apply mathematical rigor to OS security, predating modern verified systems like seL4. Readers interested in security engineering, formal verification, or the history of computer science will find valuable insights into how foundational security concepts were developed decades ago.

---

### 可证明安全操作系统（PSOS）的基础（1979）

* 根据标题推测，这篇文章可能介绍了 PSOS 的理论和架构基础，这是一个早期研究项目，旨在构建具有数学可证明安全属性的操作系统。文章可能讨论了形式化验证方法、安全模型，以及创建一个安全性可以被形式化证明（而非仅仅测试）的操作系统所需的设计原则。
* 为何值得关注：这篇 1979 年的论文代表了形式化方法和安全系统设计领域的开创性工作。作为最早将数学严谨性应用于操作系统安全的尝试之一，它具有重要的历史意义，比现代的验证系统（如 seL4）早了数十年。对安全工程、形式化验证或计算机科学历史感兴趣的读者，可以从中了解到几十年前如何发展基础安全概念的宝贵见解。

**[Read Original / 阅读原文](http://www.csl.sri.com/users/neumann/psos.pdf)**

### The Global Fertility Crisis: A Demographic Turning Point

* **Historic milestone**: 2023 marked the first year in human history when global fertility rates fell below replacement level (2.1 children per woman)
* **Widespread decline**: Fertility rates have dropped below replacement in nearly all of North America, South America, Europe, and Southern/Eastern Asia
* **Surprising epicenters**: Tokyo has higher fertility than Mexico City or Bogotá; Europe exceeds Thailand; China may already be lower than Japan
* **Dramatic misses**: UN predicted 350,000 births in South Korea for 2023; actual figure was 230,000—a 50% error
* **China's shift**: Young Chinese women with "no desire for children" surged from 5% (2012) to 47% (2023)
* **Competing explanations**: Technology and social media versus existential anxiety about climate, housing costs, and political instability
* **Long-term context**: Decline reflects positive developments (lower child mortality, women's education, contraception access) alongside modern challenges
* **Momentum effect**: Global population continues growing temporarily due to demographic momentum, but "peak child" may already be behind us
* **Compounding impact**: At current rates, Thailand's population could theoretically decline from 63 million to 2 million over 200 years without immigration
* **Expert perspective**: Economist Jesús Fernández-Villaverde argues fertility and AI are the only two truly important issues of our time

### 全球生育危机：人口转折点

* **历史性里程碑**：2023年是人类历史上首次全球生育率低于更替水平（每名女性2.1个孩子）
* **普遍下降**：北美、南美、欧洲和东亚、南亚几乎所有国家的生育率都低于更替水平
* **令人意外的重灾区**：东京生育率高于墨西哥城或波哥大；欧洲超过泰国；中国可能已低于日本
* **预测严重失准**：联合国预测韩国2023年将有35万新生儿；实际仅23万——误差达50%
* **中国的转变**：中国年轻女性"不想要孩子"的比例从2012年的5%飙升至2023年的47%
* **原因争论**：科技和社交媒体的影响 vs 对气候、房价和政治不稳定的存在焦虑
* **长期背景**：下降反映了积极发展（儿童死亡率降低、女性教育、避孕普及）和现代挑战
* **人口惯性效应**：由于人口惯性，全球人口暂时继续增长，但"儿童峰值"可能已经过去
* **复合影响**：按当前速度，泰国人口理论上可能在200年内从6300万降至200万（无移民情况下）
* **专家观点**：经济学家赫苏斯·费尔南德斯-比利亚韦德认为生育率和人工智能是当今唯一真正重要的两个议题

**[Read Original / 阅读原文](https://www.derekthompson.org/p/why-the-whole-world-stopped-having)**

### There Is No 'Hard Problem Of Consciousness'

* Theoretical physicist Carlo Rovelli argues that consciousness is not fundamentally mysterious, but rather a complex natural phenomenon like thunderstorms or protein folding that we don't yet fully understand
* The "hard problem of consciousness" proposed by philosopher David Chalmers in 1994 claims there's an unbridgeable "explanatory gap" between brain processes and subjective experience
* Rovelli contends this supposed gap stems from outdated dualistic thinking that separates mind from matter, similar to historical resistance against Darwin's evolution or the idea that Earth and heaven share the same nature
* He argues that scientific understanding is inherently experiential and perspectival—we observe the world from within it, not from outside, making the subject-object divide artificial
* The concept of "philosophical zombies" (beings that behave like humans but lack consciousness) is dismissed as a rhetorical trick that assumes dualism upfront
* Rovelli suggests consciousness and subjective experience are simply names for brain processes viewed from different perspectives—first-person versus third-person—not evidence of separate realities
* The article frames the consciousness debate as cultural resistance to accepting that our "soul" or inner life is part of the natural world, not a transcendent spiritual entity

### 意识的"困难问题"并不存在

* 理论物理学家卡洛·罗韦利认为，意识并非根本性的神秘现象，而是像雷暴或蛋白质折叠一样复杂但尚未完全理解的自然现象
* 哲学家大卫·查尔默斯于1994年提出的意识"困难问题"声称，大脑过程与主观体验之间存在无法跨越的"解释鸿沟"
* 罗韦利认为这种所谓的鸿沟源于过时的二元论思维，将心灵与物质分离，类似于历史上对达尔文进化论或天地同质观念的抵制
* 他主张科学理解本质上是经验性和视角性的——我们从世界内部观察世界，而非从外部，这使得主客体分离变得人为
* "哲学僵尸"概念（行为像人类但缺乏意识的存在）被驳斥为预设二元论的修辞技巧
* 罗韦利认为意识和主观体验只是从不同视角（第一人称与第三人称）观察大脑过程的名称，而非独立现实的证据
* 文章将意识辩论框定为文化抵制，即抗拒接受我们的"灵魂"或内在生活是自然世界的一部分，而非超越性的精神实体

**[Read Original / 阅读原文](https://www.noemamag.com/there-is-no-hard-problem-of-consciousness/)**

### Academic Research Skills for Claude Code - AI-Powered Academic Writing Pipeline

* **What it does**: A comprehensive Claude Code plugin that automates the academic research workflow from literature review through peer review to final publication, handling citation verification, formatting, and quality checks while keeping humans in control of critical decisions.

* **Key features**: 
  - 13-agent deep research team with PRISMA systematic review and Semantic Scholar API verification
  - 12-agent paper writing with style calibration, LaTeX formatting, and anti-hallucination safeguards
  - 7-agent multi-perspective peer review system with 0-100 quality rubrics
  - 10-stage pipeline with integrity gates that catch fabricated citations, statistical errors, and AI research failure modes
  - Claim-level citation audit (v3.8) that verifies every reference actually supports the claim it's cited for
  - Material Passport system for reproducibility documentation

* **Why it's notable**: Addresses the citation hallucination crisis documented by Zhao et al. (146,932 hallucinated citations in 2025 alone) with trust-chain provenance tracking and locator infrastructure. Takes a human-in-the-loop approach inspired by Nature's "The AI Scientist" paper, explicitly avoiding the failure modes of fully autonomous AI research. Real-world showcase demonstrates catching 15 fabricated references and 3 statistical errors before publication. Installs in 30 seconds via Claude Code plugin marketplace.

---

### Academic Research Skills for Claude Code - AI 驱动的学术写作流程工具

* **功能介绍**: 一个全面的 Claude Code 插件，自动化学术研究工作流程，从文献综述到同行评审再到最终发表，处理引用验证、格式化和质量检查，同时让人类掌控关键决策。

* **主要特点**:
  - 13 个智能体组成的深度研究团队，支持 PRISMA 系统综述和 Semantic Scholar API 验证
  - 12 个智能体的论文写作系统，具备风格校准、LaTeX 格式化和防幻觉保护措施
  - 7 个智能体的多视角同行评审系统，采用 0-100 质量评分标准
  - 10 阶段流程管道，配备完整性检查点，可捕获虚假引用、统计错误和 AI 研究失败模式
  - 声明级引用审计功能（v3.8），验证每个参考文献是否真正支持其所引用的论点
  - 材料护照系统用于可重现性文档记录

* **为何值得关注**: 针对 Zhao 等人记录的引用幻觉危机（仅 2025 年就有 146,932 条虚假引用）提供解决方案，通过信任链溯源追踪和定位器基础设施进行防范。采用受 Nature《The AI Scientist》论文启发的人机协作方法，明确避免全自动 AI 研究的失败模式。真实案例展示在发表前成功捕获 15 条虚假引用和 3 个统计错误。通过 Claude Code 插件市场 30 秒即可完成安装。

**[View Repository / 查看仓库](https://github.com/Imbad0202/academic-research-skills)**

### Scientific Agent Skills - Comprehensive AI Research Assistant Toolkit

* **What it does**: A collection of 135 ready-to-use skills that transform AI coding agents (Cursor, Claude Code, Codex) into powerful research assistants. Provides curated access to 100+ scientific databases, 70+ optimized Python packages, and specialized tools for executing complex multi-step scientific workflows across biology, chemistry, medicine, physics, and more.

* **Key features**: 
  - Unified access to 78+ public databases (PubChem, ChEMBL, UniProt, COSMIC, ClinicalTrials.gov) plus specialized data sources
  - Pre-documented skills for scientific Python packages (RDKit, Scanpy, PyTorch Lightning, BioPython, OpenMM, scVelo)
  - Covers 17+ scientific domains: genomics, drug discovery, proteomics, clinical research, medical imaging, materials science, geospatial analysis
  - Includes research communication tools (literature review, scientific writing, grant writing)
  - Works with any AI agent supporting the open Agent Skills standard
  - Simple installation via `npx skills add` command

* **Why it's notable**: Bridges the gap between AI coding agents and specialized scientific computing by providing production-ready, tested code examples and comprehensive documentation. Eliminates days of API research and integration work, enabling researchers to execute complex scientific pipelines with simple prompts. The 762 stars today reflect strong demand for accessible AI-powered research tools that work across multiple platforms.

---

### Scientific Agent Skills - 综合 AI 科研助手工具包

* **功能介绍**: 包含 135 个即用型技能的集合,可将 AI 编程助手(Cursor、Claude Code、Codex)转变为强大的科研助手。提供对 100+ 科学数据库、70+ 优化 Python 包的精选访问,以及跨生物学、化学、医学、物理等领域执行复杂多步骤科学工作流的专业工具。

* **主要特点**:
  - 统一访问 78+ 公共数据库(PubChem、ChEMBL、UniProt、COSMIC、ClinicalTrials.gov)及专业数据源
  - 为科学 Python 包(RDKit、Scanpy、PyTorch Lightning、BioPython、OpenMM、scVelo)提供预文档化技能
  - 覆盖 17+ 科学领域:基因组学、药物发现、蛋白质组学、临床研究、医学影像、材料科学、地理空间分析
  - 包含科研交流工具(文献综述、科学写作、基金申请)
  - 兼容所有支持开放 Agent Skills 标准的 AI 助手
  - 通过 `npx skills add` 命令简单安装

* **为何值得关注**: 通过提供生产就绪、经过测试的代码示例和全面文档,弥合了 AI 编程助手与专业科学计算之间的鸿沟。省去数天的 API 研究和集成工作,使研究人员能够通过简单提示执行复杂科学流程。今日获得 762 星标反映了对跨平台 AI 驱动科研工具的强劲需求。

**[View Repository / 查看仓库](https://github.com/K-Dense-AI/scientific-agent-skills)**

### Supertonic - Lightning-Fast, On-Device, Multilingual TTS via ONNX

* **What it does**: Supertonic is a text-to-speech system that runs entirely on your device using ONNX Runtime, supporting 31 languages with zero cloud dependency. It converts text to high-quality 44.1kHz audio locally on desktop, mobile, browsers, and edge devices like Raspberry Pi.

* **Key features**: 
  - Blazingly fast real-time synthesis with a compact 99M-parameter model (much smaller than typical 0.7B-2B TTS systems)
  - 31-language multilingual support with language-agnostic mode (`lang="na"`)
  - 10 inline expression tags (`<laugh>`, `<breath>`, `<sigh>`) for natural speech
  - Multi-runtime SDKs: Python, Node.js, Browser (WebGPU), Java, C++, C#, Go, Swift, iOS, Rust, Flutter
  - Voice Builder for custom voice cloning with permanent ownership
  - Local HTTP server with OpenAI-compatible `/v1/audio/speech` endpoint

* **Why it's notable**: Achieves production-grade TTS quality with complete privacy and no GPU requirement, running fast enough to convert entire webpages to audio in under a second. The open-weight model and edge-device readiness make it ideal for privacy-sensitive applications, offline use cases, and resource-constrained environments. Recently released Supertonic 3 with expanded language support and improved accuracy.

---

### Supertonic - 基于 ONNX 的超快速端侧多语言 TTS

* **功能介绍**: Supertonic 是一个完全在本地设备上运行的文本转语音系统,通过 ONNX Runtime 实现,支持 31 种语言,无需云端依赖。可在桌面、移动端、浏览器和树莓派等边缘设备上将文本转换为高质量 44.1kHz 音频。

* **主要特点**:
  - 采用紧凑的 9900 万参数模型实现超快实时合成(远小于常见的 7 亿-20 亿参数 TTS 系统)
  - 支持 31 种语言的多语言合成,提供语言无关模式(`lang="na"`)
  - 10 种内联表情标签(`<laugh>`、`<breath>`、`<sigh>`)实现自然语音表达
  - 多运行时 SDK:Python、Node.js、浏览器(WebGPU)、Java、C++、C#、Go、Swift、iOS、Rust、Flutter
  - Voice Builder 支持自定义声音克隆并永久拥有
  - 本地 HTTP 服务器,兼容 OpenAI 的 `/v1/audio/speech` 接口

* **为何值得关注**: 在完全保护隐私且无需 GPU 的情况下实现生产级 TTS 质量,速度快到可在一秒内将整个网页转换为音频。开放权重模型和边缘设备就绪特性使其非常适合隐私敏感应用、离线场景和资源受限环境。最近发布的 Supertonic 3 扩展了语言支持并提升了准确性。

**[View Repository / 查看仓库](https://github.com/supertone-inc/supertonic)**

### 🎬 Claude Code FREE UNLIMITED 2026 🤯 (No Ollama, No GPU, No Nvidia Nim)
**Channel:** AI with Hassan

* What the video covers: A tutorial on setting up Claude Code (likely Claude-powered coding assistant) completely free with unlimited usage, without requiring local GPU resources, Ollama installation, or Nvidia NIM
* Key topics discussed: Free setup method for Claude Code, workarounds for hardware limitations, step-by-step configuration guide available on GitHub
* Why it's worth watching: Provides a cost-effective solution for developers who want to use advanced AI coding assistance without expensive hardware or API costs, particularly valuable for those without access to high-end GPUs

### 🎬 Claude Code 免费无限使用 2026 🤯 (无需 Ollama、GPU 或 Nvidia Nim)
**频道:** AI with Hassan

* 视频内容概述: 教程演示如何完全免费且无限制地设置 Claude Code(可能是 Claude 驱动的编码助手),无需本地 GPU 资源、Ollama 安装或 Nvidia NIM
* 主要话题: Claude Code 的免费设置方法、硬件限制的解决方案、GitHub 上提供的分步配置指南
* 为何值得观看: 为开发者提供经济实惠的解决方案,无需昂贵的硬件或 API 费用即可使用先进的 AI 编码辅助工具,特别适合没有高端 GPU 的用户

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=Rssu7r8ANik)**

