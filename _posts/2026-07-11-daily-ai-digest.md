---
title: "Daily Tech Digest: July 11, 2026"
date: 2026-07-11
description: "Today's digest: 6 Hacker News articles, 3 GitHub trending repos, 6 fast-moving projects, 8 YouTube videos, 0 Hugging Face models. 今日精选：6篇黑客新闻，3个热门项目，6个快速崛起项目，8个YouTube视频，0个Hugging Face模型。"
categories: [Daily Digest]
tags: [HackerNews, GitHub, YouTube, HuggingFace]
pin: false### Relativistic Effects Alter Chemical Bonding in Heavy Elements

*   A study from Brown University provides direct evidence that Einstein's theory of relativity changes the structure of triple chemical bonds in heavy elements.
*   Using photoelectron spectroscopy, researchers found that the triple bond between carbon and bismuth does not follow the classic "one sigma bond and two pi bonds" model.
*   Instead, the bond structure appears to be "smeared," consisting of one pi bond and two hybrid sigma-pi bonds due to relativistic spin-orbit coupling.
*   This finding challenges textbook chemistry for heavy elements and could influence research in quantum materials and next-generation solar cells using bismuth.

### 爱因斯坦的相对论如何影响重元素的化学键

*   布朗大学的一项研究首次提供了直接证据，表明爱因斯坦的相对论理论会改变重元素中三重化学键的结构。
*   研究人员利用光电子能谱技术发现，碳与铋之间的三重键不符合传统的“一个σ键和两个π键”模型。
*   由于相对论的自旋轨道耦合效应，键的结构变得模糊，呈现出一个π键和两个σ-π杂化键的形态。
*   这一发现挑战了关于重元素的传统化学教科书理论，并可能影响铋在量子材料、量子计算以及新一代太阳能电池等领域的应用研究。

**[Read Original / 阅读原文](https://www.brown.edu/news/2026-07-09/chemical-bonds-relativity)**

### Apple Sues OpenAI for Trade Secret Theft

*   Apple has filed a lawsuit against OpenAI, accusing the company of stealing trade secrets through its former employees for OpenAI's benefit.
*   The lawsuit specifically names former Apple VP of product design, Tang Tan, and senior engineer Chang Liu as defendants. It also names OpenAI and its hardware subsidiary, io Products.
*   Allegations include Tan using Apple's confidential information to grill job candidates and soliciting "show and tell" sessions with Apple hardware parts during interviews.
*   Apple claims a pattern exists where departing employees, like Liu, exploit security bugs to download confidential files and evade security protocols.
*   The suit alleges OpenAI used Apple's proprietary techniques via a misled partner and approached other suppliers using insider knowledge.
*   The lawsuit comes as OpenAI, led by former Apple design chief Jony Ive, develops its first consumer hardware device.

### 苹果起诉OpenAI窃取商业机密

*   苹果公司今日对OpenAI提起诉讼，指控该公司通过其前雇员窃取商业机密，以谋取OpenAI的利益。
*   诉讼明确点名了前苹果产品设计副总裁唐谭（Tang Tan）和高级工程师刘昌（Chang Liu）作为被告，同时也将OpenAI及其硬件子公司io Products列为被告。
*   指控内容包括：唐谭在面试时利用苹果的机密信息盘问求职者，并指导他们携带苹果的实物硬件部件到面试中进行“展示和讲述”。
*   苹果声称存在一种模式，即即将离职的员工（如刘昌）会利用安全漏洞，在离职后下载机密文件并规避旨在保护公司机密信息的安全流程。
*   诉讼还指控OpenAI通过一个受误导的合作方使用了苹果的专有金属处理技术，并利用内部术语向其他供应商询问特定苹果组件的针对性问题。
*   此次诉讼发生在OpenAI由苹果前设计主管乔纳森·艾维（Jony Ive）领导，并即将推出其首款消费级硬件设备之际。

**[Read Original / 阅读原文](https://9to5mac.com/2026/07/10/apple-sues-openai-trade-secret-theft/)**

### QuadRF: Advanced Phased-Array Radio System Overview
* QuadRF is a phased-array radio system built around a Raspberry Pi 5 and an FPGA board, enabling advanced signal processing, beamforming, and picosecond-level timing for high-precision RF analysis.
* It can detect and visualize WiFi signals through walls and track drones in real-time using an augmented reality (AR) RF visualizer, making it useful for local SDR applications and RF environment monitoring.
* The system is part of a larger project aimed at creating a Moon-scale antenna array for Earth-Moon-Earth (EME) radio experiments, with potential for high-power RF operations when chained together.
* It leverages Raspberry Pi's MIPI lanes for low-latency SDR streaming at over 5 Gbps, ensuring efficient I/Q data transfer without relying on USB, and supports daisy-chaining multiple modules for scalability.
* Available via crowdfunding on Crowd Supply at a basic kit price of $499, QuadRF has impressed testers with its functionality despite some UI roughness, offering insights into RF capabilities and privacy implications.

### QuadRF：先进相控阵无线电系统概述
* QuadRF是一款基于Raspberry Pi 5和FPGA板构建的相控阵无线电系统，支持先进的信号处理、波束成形和皮秒级计时，用于高精度射频分析。
* 它能够通过增强现实（AR）射频可视化工具检测并可视化穿透墙壁的WiFi信号，并实时跟踪无人机，适用于本地SDR应用和射频环境监测。
* 该系统是创建用于地月-地月（EME）无线电实验的月球尺度天线阵列更大项目的一部分，通过链接多个模块可实现高功率射频操作。
* 它利用Raspberry Pi的MIPI接口进行低延迟SDR数据流传输，速率超过5 Gbps，确保高效的I/Q数据传输，不依赖USB，并支持多个模块的链接以实现可扩展性。
* 通过Crowd Supply平台众筹，基础套件售价499美元，QuadRF在功能测试中表现出色，尽管UI有些粗糙，但提供了射频能力和隐私影响的重要见解。

**[Read Original / 阅读原文](https://www.jeffgeerling.com/blog/2026/quadrf-can-spot-drones-and-see-wifi-through-my-wall/)**


## 🔥 GitHub Trending / GitHub 热门项目

### DesktopCommanderMCP - A MCP Server for Claude Enabling Terminal & File System Control

*   **What it does**: This is a Model Context Protocol (MCP) server designed for Claude. It grants Claude the ability to directly interact with your local computer, enabling it to execute terminal commands, perform comprehensive file system operations, and edit files using search-and-replace. It essentially turns Claude into a powerful desktop automation and coding assistant.
*   **Key features**:
    *   **Enhanced Terminal Control**: Execute, stream, and manage long-running terminal processes, including interactive ones.
    *   **Advanced File Operations**: Beyond basic read/write, it supports recursive searches, negative offset reading (tail), and surgical text replacements.
    *   **Rich File Format Support**: Native support for reading, writing, and editing Excel (.xlsx), PDF, and Word (.docx) files.
    *   **In-Memory Code Execution**: Run Python, Node.js, or R code directly without saving files to disk.
    *   **Security & Auditing**: Built-in security hardening (symlink protection, command blocklists) and comprehensive audit logging.
    *   **Flexible Installation**: Multiple installation methods including `npx`, a bash script, and a Docker container for sandboxed operation.
*   **Why it's notable**: It's rapidly trending because it significantly expands Claude's utility from a conversational AI to a proactive assistant that can manipulate a user's development environment. It bridges the gap between AI chat and real-world task execution (like fixing code, analyzing data files, managing servers). The focus on using host client subscriptions rather than API keys and the wide array of supported file formats make it particularly practical and cost-effective for developers. The Docker installation option also provides a secure, isolated sandbox for execution.

### DesktopCommanderMCP - 为Claude提供终端与文件系统控制的MCP服务器

*   **功能介绍**：这是一个专为Claude设计的模型上下文协议（MCP）服务器。它让Claude能够直接与您的本地计算机交互，从而执行终端命令、进行全面的文件系统操作，并通过搜索和替换编辑文件。本质上，它将Claude变成了一个强大的桌面自动化和编程助手。
*   **主要特点**：
    *   **增强的终端控制**：执行、流式处理并管理长时间运行的终端进程，包括交互式进程。
    *   **高级文件操作**：除基本的读写外，支持递归搜索、负偏移读取（类似Unix的tail）以及精准的文本替换。
    *   **丰富的文件格式支持**：原生支持读取、写入和编辑Excel (.xlsx)、PDF和Word (.docx)文件。
    *   **内存中代码执行**：直接运行Python、Node.js或R代码，无需将文件保存到磁盘。
    *   **安全与审计**：内置安全加固（符号链接保护、命令黑名单）和全面的审计日志记录。
    *   **灵活的安装方式**：提供多种安装方法，包括`npx`、bash脚本以及用于沙盒环境的Docker容器。
*   **为何值得关注**：它的快速增长是因为它极大地扩展了Claude的效用，使其从一个对话式AI转变为一个能够操作用户开发环境的主动助手。它弥合了AI聊天与现实世界任务执行（如修复代码、分析数据文件、管理服务器）之间的鸿沟。专注于使用主机客户端订阅而非API密钥，以及对众多文件格式的支持，使其对开发者而言既实用又经济。Docker安装选项还提供了一个安全的隔离沙盒用于执行。

**[View Repository / 查看仓库](https://github.com/wonderwhy-er/DesktopCommanderMCP)**

### Bun - Ultra-fast JavaScript Runtime, Bundler, and Toolkit
*   **What it does:** Bun is an all-in-one toolkit designed as a high-performance, drop-in replacement for Node.js. It integrates a JavaScript runtime, a bundler, a test runner, and a package manager into a single executable.
*   **Key features:**
    *   Dramatically faster startup times and lower memory usage than Node.js.
    *   Native support for TypeScript, JSX, and modern JavaScript out-of-the-box.
    *   A built-in, Node.js-compatible package manager (`bun install`) that is significantly faster than npm/yarn/pnpm.
    *   An integrated test runner (`bun test`) and bundler (`Bun.build`).
    *   Provides a rich set of built-in APIs for HTTP servers, file I/O, databases, and more.
*   **Why it's notable:** Bun is trending because it tackles the fragmentation and performance bottlenecks in the JavaScript development ecosystem. By consolidating core tools into one fast, cohesive package, it aims to simplify workflows and significantly boost developer productivity. Its rapid development and ambitious feature set make it a highly watched alternative to established tools.

### Bun - 超快的JavaScript运行时、打包器和工具集
*   **功能介绍：** Bun 是一个一体化的 JavaScript/TypeScript 开发工具包，旨在作为 Node.js 的高性能替代品。它将 JavaScript 运行时、打包器、测试运行器和包管理器集成到一个可执行文件中。
*   **主要特点：**
    *   启动速度和内存使用相比 Node.js 有极大提升。
    *   开箱即用地支持 TypeScript、JSX 和现代 JavaScript。
    *   内置了兼容 Node.js 但速度更快的包管理器（`bun install`）。
    *   集成了测试运行器（`bun test`）和打包器（`Bun.build`）。
    *   提供丰富的内置 API，涵盖 HTTP 服务器、文件操作、数据库访问等。
*   **为何值得关注：** Bun 的流行源于它解决了 JavaScript 生态系统工具碎片化和性能瓶颈的问题。通过将核心工具整合到一个快速、统一的包中，它旨在简化开发流程并显著提升开发效率。其快速的迭代和雄心勃勃的功能集使其成为备受瞩目的新兴工具。

**[View Repository / 查看仓库](https://github.com/oven-sh/bun)**

### abseil/abseil-cpp - Abseil Common Libraries (C++)
*   **What it does**: This is an open-source collection of C++ library code from Google, designed to augment the C++ standard library. It provides foundational utilities, types, and functions that are widely used and tested within Google's own codebase.
*   **Key features**:
    *   Contains over 20 modular libraries (`base`, `strings`, `status`, `container`, `hash`, `time`, etc.) that solve common C++ programming problems.
    *   Provides production-grade, well-tested implementations like Swiss Tables (`absl::flat_hash_map`), robust error handling (`absl::Status`), and string utilities.
    *   Officially supports Bazel and CMake as build systems.
*   **Why it's notable**: Abseil is a direct output of Google's C++ best practices and is heavily battle-tested in their infrastructure. Its modular design and focus on filling gaps in the C++ standard make it a powerful, reliable, and increasingly popular choice for modern C++ development, as indicated by its trending stars.

### abseil/abseil-cpp - Abseil C++ 常用库
*   **功能介绍**: 这是一个来自 Google 的开源 C++ 库集合，旨在扩充 C++ 标准库。它提供了 Google 内部广泛使用和测试的基础工具、类型和函数。
*   **主要特点**:
    *   包含超过 20 个模块化库（`base`、`strings`、`status`、`container`、`hash`、`time` 等），解决常见的 C++ 编程问题。
    *   提供生产级、经过充分测试的实现，例如 Swiss Tables（`absl::flat_hash_map`）、健壮的错误处理（`absl::Status`）和字符串处理工具。
    *   官方支持 Bazel 和 CMake 作为构建系统。
*   **为何值得关注**: Abseil 是 Google C++ 最佳实践的直接产物，在其基础设施中经过大量实战检验。其模块化设计和专注于弥补 C++ 标准库不足的特点，使其成为现代 C++ 开发中强大、可靠且日益流行的选择，其今日的增长星数也证明了其热度。

**[View Repository / 查看仓库](https://github.com/abseil/abseil-cpp)**


## 🚀 Fast-Moving Repos / 快速崛起项目

### os-taxonomy - Marble Skill Taxonomy: A Structured Knowledge Graph of K-12 Education
* **What it does**: This repository provides an open, structured dataset representing a comprehensive knowledge graph of what children learn in primary/elementary education. It decomposes curricula into fine-grained "micro-topics" connected by a prerequisite graph.
* **Key features**: Contains 1,590 micro-topics across 8 subjects (Science, Math, etc.) with 3,221 directed prerequisite edges. Each topic includes descriptions, mastery criteria, type classification, and alignment to standards (NGSS, Common Core, UK National Curriculum). Data is pure JSON with no runtime dependencies.
* **Why it's notable**: It transforms typically flat or siloed curriculum data into a dynamic, interconnected graph, enabling innovative educational tools. Its multi-layered open license (ODbL + CC BY-SA) makes it highly valuable for both research and commercial development without forcing derivative products to be open-sourced.

### os-taxonomy - Marble 技能分类法：结构化的 K-12 教育知识图谱
* **功能介绍**：该仓库提供了一个开放、结构化的数据集，代表了小学/初中阶段学习内容的完整知识图谱。它将课程内容分解为精细的“微主题”，并通过先决条件图谱连接起来。
* **主要特点**：包含8个学科（科学、数学等）的1,590个微主题，以及3,221条有向的先决条件边。每个主题包含描述、掌握标准、类型分类，并与主要课程标准（NGSS、Common Core、英国国家课程）对齐。数据为纯JSON格式，无运行时依赖，开箱即用。
* **为何值得关注**：它将传统扁平化或孤立的课程数据转化为动态互联的图谱，为创新教育工具的开发提供了强大基础。其多层开放许可证（ODbL + CC BY-SA ）模式，使得该数据集既能用于研究和商业开发，又要求衍生数据库保持开放，实现了开放性与实用性的平衡。

**[View Repository / 查看仓库](https://github.com/withmarbleapp/os-taxonomy)**

### Shpigford/knockoff - Amazon Brand Junk Filter for Chrome
* What it does: A browser extension that detects and filters out pseudo-brand "junk" listings on Amazon, helping users buy from real, established brands. It works by identifying brands with names typical of trademark squatting (e.g., random strings) and hides, dims, or labels them directly in search results.
* Key features: Fully local processing with no tracking; multi-layered detection using user block/allow lists, curated lists of known pseudo-brands, and ~5,000 established brands; intelligent name heuristics to score unknown brands; configurable filter levels (Relaxed, Standard, Strict); and actions like hiding or dimming items with click-to-reveal options.
* Why it's notable: It solves a widely recognized pain point of navigating Amazon's marketplace saturated with unregulated, low-trust brands. Its privacy-first, client-side approach combined with community-driven brand curation has earned significant press coverage (e.g., Fast Company, Gizmodo) and a strong GitHub following (1706 stars), making it a trending tool for improving the online shopping experience.

### Shpigford/knockoff - 过滤亚马逊伪品牌垃圾的浏览器扩展
* 功能介绍：这是一个浏览器扩展程序，用于检测并过滤亚马逊上充斥的“伪品牌”垃圾商品，帮助用户购买来自真正、成熟品牌的产品。它通过识别具有典型商标囤积特征的品牌名（如随机字符串），直接在搜索结果中隐藏、淡化或标记这些商品。
* 主要特点：完全本地处理，无用户追踪；采用多层检测机制，结合用户白名单/黑名单、精选伪品牌列表以及约5000个成熟品牌列表；智能的名称启发式算法用于评估未知品牌；提供可配置的过滤级别（宽松、标准、严格）；支持隐藏或淡化商品并可一键恢复查看。
* 为何值得关注：它精准解决了亚马逊市场充斥大量不受监管、信誉度低的品牌这一普遍痛点。其注重隐私的客户端处理方式，结合社区驱动的品牌列表维护，已获得众多科技媒体（如 Fast Company、Gizmodo）报道和 GitHub 上的广泛关注（1706星），是提升在线购物体验的热门工具。

**[View Repository / 查看仓库](https://github.com/Shpigford/knockoff)**


## 🎬 YouTube Tech Videos / YouTube 技术视频

### 🎬 OpenAI is so back... GPT 5.6 Sol first look
**Channel:** Fireship
*   What the video covers: A first look and reaction to the newly released GPT-5.6 "Sol" model from OpenAI, discussing its capabilities and what it means for the AI landscape.
*   Key topics discussed: The features of GPT-5.6, OpenAI's renewed momentum, the model's performance implications, and a brief sponsor mention for Blacksmith.
*   Why it's worth watching: Provides a quick, informed take on a major new AI release from a developer-focused perspective, cutting through the hype to deliver practical insights.

### 🎬 OpenAI强势回归…GPT 5.6 Sol首发体验
**频道:** Fireship
*   视频内容概述：针对OpenAI最新发布的GPT-5.6 "Sol" 模型进行的首个体验与即时反应，分析其功能及对AI领域的影响。
*   主要话题：GPT-5.6的特性、OpenAI的势头回归、模型性能意义，以及对赞助商Blacksmith的简短介绍。
*   为何值得观看：从开发者视角快速、精准地解读此次重大AI发布，剥离炒作成分，提供实用的前沿见解。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=URKml8lgw8Y)**

### 🎬 General relativity from first principles – Adam Brown
**Channel:** Dwarkesh Patel
*   A deep, first-principles exploration of Einstein's theory of general relativity, presented by physicist Adam Brown.
*   Key topics include the foundational concepts of spacetime, gravity as geometry, and the mathematical framework that unifies them, all explained in an accessible way.
*   This video is worth watching for its unique approach to demystifying one of physics' most profound and beautiful theories, making it understandable for a wider audience beyond just experts.

### 🎬 从第一性原理解读广义相对论 - 亚当·布朗
**频道:** Dwarkesh Patel
*   由物理学家亚当·布朗深入浅出地从第一性原理出发，剖析爱因斯坦的广义相对论。
*   主要话题涵盖时空的基本概念、将引力解释为时空几何的弯曲，以及将二者统一的数学框架，全程讲解力求通俗易懂。
*   该视频之所以值得观看，在于它用一种独特的方式，将物理学中最深刻、最优美的理论之一——广义相对论——进行了“去神秘化”处理，使其不再仅仅是少数专家的专属，而能被更广泛的受众所理解。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=QbdbAhaJoCQ)**

### 🎬 YC's Head of Design Shows You How To Design With AI
**Channel:** Y Combinator

*   What the video covers: This episode features Y Combinator's Head of Design discussing the profound shift AI is bringing to the design profession. It moves beyond the idea of AI as just a new tool, exploring how it fundamentally alters the designer's thought process, prototyping workflow, and the entire build cycle.
*   Key topics discussed: The conversation likely delves into AI as a collaborative partner, the evolution of design workflows, practical applications for prototyping, and how designers can adapt their mindset to leverage AI effectively.
*   Why it's worth watching: It provides expert insight from a leading figure in the design and startup world. This is essential viewing for designers, product managers, and anyone interested in the future of technology and creativity, offering a strategic perspective on how to stay relevant and innovative in the AI era.

### 🎬 YC设计主管教你如何与AI协同设计
**频道:** Y Combinator

*   视频内容概述：本期节目邀请了Y Combinator的设计主管，深入探讨AI如何给设计行业带来深刻的变革。视频超越了将AI视为新工具的层面，重点阐释了AI如何从根本上改变设计师的思考模式、原型制作流程以及整个产品构建周期。
*   主要话题：讨论可能涉及AI作为协同伙伴、设计工作流程的演变、在原型制作中的实际应用，以及设计师如何调整思维方式以有效利用AI。
*   为何值得观看：该视频提供了来自设计与创业领域权威专家的深度见解。对于设计师、产品经理以及任何对技术与创意未来感兴趣的人来说，这都是必看内容，它提供了在AI时代保持竞争力和创新力的战略性思考视角。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=VbqaL_eHhKY)**

### 🎬 A proper guide to Fable 5
**Channel:** Theo - t3․gg

*   What the video covers: A comprehensive introductory guide to the game *Fable 5*, likely aimed at new players. The creator shares their overwhelmingly positive first impressions, suggesting it goes beyond the original *Fable* series.
*   Key topics discussed: Core gameplay mechanics, world exploration, story setup, and the overall experience of stepping into the game's universe.
*   Why it's worth watching: The creator's authentic excitement provides a genuine endorsement. This guide is ideal for anyone curious about *Fable 5* but unsure where to start, offering a passionate first look to help decide if the game is right for them.

### 🎬 Fable 5完整攻略指南
**频道:** Theo - t3․gg

*   视频内容概述：这是一份针对新玩家的《Fable 5》综合入门指南。创作者分享了其极为震撼的初体验，认为其成就甚至超越了经典的《神鬼寓言》系列。
*   主要话题：核心游戏机制、世界探索、故事背景介绍以及整体的游戏沉浸感。
*   为何值得观看：创作者发自内心的热情提供了真实可信的推荐。本指南非常适合所有对《Fable 5》感兴趣但不知从何入手的玩家，通过这份充满感染力的初探，可以帮助你判断这款游戏是否适合你。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=8GRmLR__OGQ)**

### 🎬 How to Use AI for Programming
**Channel:** The Cherno

*   **What the video covers:** This video is a practical guide on integrating AI tools, specifically AI code assistants like GitHub Copilot, into a developer's workflow. The creator explores how these tools can be used to write, debug, and understand code more efficiently.
*   **Key topics discussed:**
    *   Effective prompting strategies for AI coding tools.
    *   Practical use cases: generating boilerplate, writing tests, explaining code snippets.
    *   The limitations and ethical considerations of relying on AI for programming.
    *   Maintaining core programming skills while leveraging AI assistance.
*   **Why it's worth watching:** As AI tools become mainstream in software development, this video provides a grounded and practical perspective from an experienced developer. It helps viewers move beyond the hype, teaching them *how* to use AI as a powerful productivity tool while understanding its boundaries, making it essential for modern programmers.

---

### 🎬 如何使用AI进行编程
**频道:** The Cherno

*   **视频内容概述:** 本视频是一份将AI工具（特别是GitHub Copilot等AI编程助手）整合到开发者工作流中的实用指南。创作者探索了如何利用这些工具更高效地编写、调试和理解代码。
*   **主要话题:**
    *   针对AI编程工具的有效提示策略。
    *   实际应用场景：生成样板代码、编写测试、解释代码片段。
    *   依赖AI进行编程的局限性和伦理考量。
    *   在利用AI辅助的同时保持核心编程技能。
*   **为何值得观看:** 随着AI工具在软件开发中逐渐普及，本视频从一位经验丰富的开发者角度提供了务实且实用的见解。它帮助观众超越炒作，教会他们如何将AI作为强大的生产力工具，同时理解其边界，对现代程序员而言必不可少。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=A4aLYwtpyes)**

### Building an iroh-Powered Smart Fan
*   **Concept & Goal:** Create a simple, cloud-free smart fan using an ESP32 microcontroller and the iroh networking library, allowing remote control from anywhere via a WebAssembly-enabled browser.
*   **Hardware Base:** The primary example uses an **ESP32-WROVER devkit** with 4 MiB of PSRAM, which is necessary for iroh's full networking capabilities, including relay connections.
*   **Project Setup:** The project starts by copying and renaming an existing iroh echo server example (`server-esp32-psram` → `server-smart-fan`) and its corresponding client.
*   **Stability & Identity:** The device's endpoint ID is made stable across reboots by generating and storing its secret key in non-volatile memory (NVM) on first boot, which is not erased during flashing.

### 使用 iroh 构建智能风扇
*   **概念与目标：** 使用 ESP32 微控制器和 iroh 网络库构建一个简单的、无需云服务的智能风扇，允许通过支持 WebAssembly 的浏览器从任何地方进行远程控制。
*   **硬件基础：** 主要示例使用配备 4 MiB PSRAM 的 **ESP32-WROVER 开发板**，这对于 iroh 的全部网络功能（包括中继连接）是必需的。
*   **项目设置：** 项目通过复制并重命名一个现有的 iroh 回显服务器示例 (`server-esp32-psram` → `server-smart-fan`) 及其对应的客户端来启动。
*   **稳定性与标识：** 通过在首次启动时将其密钥生成并存储在非易失性存储器 (NVM) 中，该设备的端点 ID 在重启后保持稳定，NVM 在烧录时不会被擦除。

**[Read Original / 阅读原文](https://www.iroh.computer/blog/an-iroh-powered-smart-fan)**

### An update on the scraper situation [LWN.net]
*   The problem of aggressive web scraping to obtain training data for AI models has intensified since early 2025, with traffic increasingly originating from residential and mobile networks via "residential proxies."
*   These proxy networks are operated by various entities, including criminal groups using malware, companies offering "ethically sourced" IPs (like Bright Data via its VPN), and potentially undisclosed AI model developers.
*   Website operators, including LWN, are deploying increasingly sophisticated defenses (like Anubis, optimizations, and data poisoning) to mitigate scraper traffic while trying to avoid impacting legitimate users, search engines, or the Internet Archive.
*   While law enforcement actions (like those against IPIDEA and NetNut botnets) offer temporary relief, the underlying arms race continues, posing a significant threat to the open web's accessibility and sustainability.

### [LWN.net] 关于网络爬虫问题的最新进展
*   自2025年初以来，为获取AI训练数据而进行的激进网络爬取问题日益严重，其流量越来越多地通过“住宅代理”从住宅和移动网络发起。
*   运营这些代理网络的实体多种多样，包括使用恶意软件的犯罪团伙、提供“道德来源IP”的公司（如Bright Data通过其VPN服务），以及可能未公开的AI模型开发者。
*   包括LWN在内的网站运营者正部署日益复杂的防御措施（如Anubis、性能优化、数据投毒），以缓解爬虫流量，同时尽力避免对合法用户、搜索引擎或互联网档案馆造成影响。
*   虽然执法行动（如针对IPIDEA和NetNut僵尸网络）带来了暂时的缓解，但潜在的军备竞赛仍在继续，对开放互联网的可访问性和可持续性构成了重大威胁。

**[Read Original / 阅读原文](https://lwn.net/SubscriberLink/1080822/990a8a5e2d379085/)**

### SpaceX Plans 100,000 Gen3 Satellites for 100x Bandwidth
* SpaceX has filed with the FCC to launch 100,000 new, heavier third-generation (Gen3) Starlink satellites into low Earth orbit (LEO).
* The company promises the Gen3 network will deliver multi-gigabit symmetrical speeds and ultra-low latency (under 20 ms), representing a 100-fold increase in total bandwidth.
* Current real-world Starlink speeds are much lower than advertised, but the service remains vital for users in areas without fiber internet.
* The plan would dwarf all existing satellite constellations and further establish Starlink's dominance, as rivals like Amazon's Project Kuiper and Eutelsat-OneWeb are far behind.
* FCC approval is not guaranteed due to potential interference issues and objections from astronomers, but approval would solidify Starlink as the primary choice for satellite internet.

### SpaceX 计划发射10万颗第三代卫星，实现百倍带宽
* SpaceX 已向美国联邦通信委员会（FCC）提交申请，计划向低地球轨道（LEO）发射10万颗更重的新一代（第三代）星链卫星。
* 公司承诺，第三代网络将提供千兆级对称速度和超低延迟（低于20毫秒），使星链总带宽提升100倍。
* 目前星链的实际速度远低于宣传值，但对于缺乏光纤覆盖地区的用户而言，它仍是至关重要的服务。
* 该计划将使星链规模远超所有现有卫星星座，并进一步巩固其主导地位，因为亚马逊柯伊伯计划、欧洲一网等竞争对手远远落后。
* FCC的批准并非板上钉钉，该计划可能面临干扰问题以及天文学界的反对。但一旦获批，将确立星链作为卫星互联网首选服务的地位。

**[Read Original / 阅读原文](https://www.zdnet.com/home-and-office/networking/spacex-wants-to-launch-100000-more-starlink-satellites/)**

### Agent Skills - Production-Grade Engineering Skills for AI Coding Agents
*   **What it does**: This repository provides a comprehensive set of 24 structured "skills" designed to encode senior engineering workflows, quality gates, and best practices into AI coding agents. These skills guide the AI through every phase of the development lifecycle, from defining an idea (`/spec`) and planning tasks (`/plan`) to building code (`/build`), testing (`/test`), review (`/review`), and shipping to production (`/ship`).
*   **Key features**:
    *   **Lifecycle Automation**: 8 slash commands (`/spec`, `/plan`, `/build`, etc.) that map to key development stages, automatically activating relevant skills.
    *   **Comprehensive Skill Pack**: 24 skills covering meta-discovery, requirement definition (e.g., `interview-me`, `spec-driven-development`), planning, implementation (e.g., `test-driven-development`, `incremental-implementation`), and code quality.
    *   **Broad Agent Compatibility**: Designed to work with numerous AI agents and IDEs, including Claude Code, Cursor, GitHub Copilot, Codex, and more, via a simple CLI installation (`npx skills add`) or native plugin integration.
    *   **Autonomous Execution**: The `/build auto` command can autonomously generate a plan and implement all tasks in a single approved pass while maintaining verification gates.
*   **Why it's notable**: Created by prominent engineer Addy Osmani, this project addresses a critical need in AI-assisted development: ensuring consistency and quality. It moves beyond simple code generation by providing AI agents with a structured, production-grade engineering methodology. Its rapid gain in stars (1,116 today) highlights strong community interest in tools that elevate AI agents from code writers to more reliable engineering collaborators. It standardizes best practices, making complex workflows manageable and repeatable for AI.

### Agent Skills - 面向AI编码代理的生产级工程技能包
*   **功能介绍**: 该仓库提供了一套包含24个结构化“技能”的完整方案，旨在将高级工程师的工作流程、质量关卡和最佳实践编码到AI编码代理中。这些技能引导AI贯穿软件开发生命周期的每一个阶段，从定义想法（`/spec`）、规划任务（`/plan`）到编写代码（`/build`）、测试（`/test`）、审查（`/review`）以及发布到生产环境（`/ship`）。
*   **主要特点**:
    *   **开发生命周期自动化**: 提供8个斜杠命令（如 `/spec`, `/plan`, `/build`），映射到关键开发阶段，并自动激活相应的技能。
    *   **全面的技能库**: 包含24个技能，覆盖元认知发现、需求定义（如 `interview-me`, `spec-driven-development`）、规划、实施（如 `test-driven-development`, `incremental-implementation`）和代码质量保障。
    *   **广泛的代理兼容性**: 可通过简单CLI安装 (`npx skills add`) 或原生插件集成，与包括 Claude Code、Cursor、GitHub Copilot、Codex 在内的多种AI代理和IDE协同工作。
    *   **自主执行能力**: `/build auto` 命令可以在单次批准的流程中自动生成计划并实现所有任务，同时保持验证关卡。
*   **为何值得关注**: 该项目由知名工程师 Addy Osmani 创建，它解决了AI辅助开发中的一个核心需求：确保一致性和质量。它超越了简单的代码生成，为AI代理提供了一套结构化的、生产级的工程方法论。其迅速增长的星标数（今日1116星）凸显了社区对于能够将AI代理从代码编写者提升为更可靠工程协作者的工具的强烈兴趣。它标准化了最佳实践，使复杂工作流对AI而言变得可管理且可重复。

**[View Repository / 查看仓库](https://github.com/addyosmani/agent-skills)**

### yaml-cpp - YAML Parser and Emitter in C++
*   What it does: A C++ library for parsing and emitting YAML data, fully compliant with the YAML 1.2 specification.
*   Key features: Cross-platform build support via CMake, options for static or shared libraries, well-documented API with tutorials, and compatibility with modern build systems like FetchContent.
*   Why it's notable: It's a widely used, actively maintained solution for handling YAML in C++ projects, with recent releases (like v0.9.0) and clear migration paths from older APIs. The library's popularity is reflected in its steady acquisition of stars.

### yaml-cpp - C++ 的 YAML 解析器与生成器
*   功能介绍: 一个完全符合 YAML 1.2 规范的 C++ 库，用于解析和生成 YAML 格式的数据。
*   主要特点: 通过 CMake 提供跨平台构建支持，可选择构建为静态库或动态库，拥有详尽的 API 文档和教程，并支持现代构建系统（如 CMake 的 FetchContent）进行集成。
*   为何值得关注: 它是 C++ 生态中处理 YAML 文件的主流、活跃维护的解决方案。近期有版本更新（如 v0.9.0），并为从旧版 API 迁移提供了清晰路径。其在社区中的广泛采用和持续增长的星标数证明了其价值与可靠性。

**[View Repository / 查看仓库](https://github.com/jbeder/yaml-cpp)**

### riddle — The diary of Tom Riddle for the reMarkable Paper Pro
*   **What it does**: A unique journaling app for the reMarkable Paper Pro e-ink tablet. It allows you to write entries with your pen. After a pause, your writing fades away, and a character named Tom Riddle "thinks" and writes back a response in a flowing, handwritten script directly on the page.
*   **Key features**: Direct pen input; text disappearing effect ("ink drinks your ink"); AI-generated handwritten responses; gesture-based controls (erase, summon guide); a "memory" system that remembers past pages to enable follow-up conversations and recollection of past entries; two "oracle" backends (OpenAI API or local `pi`); direct e-ink hardware control for minimal latency.
*   **Why it's notable**: It's a highly creative and immersive application that deeply integrates hardware control (pen pressure, e-ink engine) with LLM vision capabilities, creating a magical, "living" diary experience. The project is trending due to its innovative user interface, technical achievement in direct hardware interaction, and its connection to a viral demo.

### riddle — reMarkable Paper Pro 上的汤姆·里德尔日记
*   **功能介绍**: 一款专为 reMarkable Paper Pro 电子墨水平板设计的独特日记应用。你可以用笔在页面上书写。稍作停顿后，你的墨迹会逐渐消隐，名为“汤姆·里德尔”的角色会“思考”，并在页面上用流畅的手写体“墨水”回复你的内容。
*   **主要特点**: 支持原生压感笔输入；具有文字淡出的“墨迹消隐”效果；由AI生成的手写风格回复；基于手势的操控（擦除、召唤指南）；具备“记忆”系统，能记住过往页面，从而支持对话延续和内容回顾；提供两种“神谕”后端（OpenAI API或本地`pi`）；直接控制电子墨水硬件引擎以实现极低延迟。
*   **为何值得关注**: 这是一款极具创意和沉浸感的应用，它将硬件底层控制（笔压、电子墨水引擎）与LLM视觉能力深度结合，创造了一种神奇的“活日记”体验。该项目因其创新的用户界面、直接操控硬件的技术成就以及与病毒式传播演示的关联而备受关注。

**[View Repository / 查看仓库](https://github.com/MaximeRivest/riddle)**

### dnsglobe - Global DNS Propagation Checker TUI
*   **What it does:** A terminal user interface (TUI) written in Rust that checks the global propagation of a DNS record by querying 34 public resolvers worldwide in parallel. It displays the status and results on a world map within your terminal.
*   **Key features:**
    *   Parallel querying of 34 global resolvers (including Google, Cloudflare, Quad9, etc.).
    *   Visual world map display (in terminals ≥150 columns) with colored dots for each resolver's status.
    *   Automatic "watch mode" that re-polls until 100% propagation.
    *   Smart grouping of answers to handle round-robin DNS correctly.
    *   Discovery and display of the actual anycast site answering queries (e.g., `→YUL`).
    *   Supports custom resolver lists via a TOML configuration file.
*   **Why it's notable:** It brings a popular web-based functionality (like dnschecker.org) directly into the terminal with enhanced features. The real-time, visual world map and watch mode make it a powerful and unique tool for developers, network engineers, and anyone managing DNS records to monitor propagation instantly and effectively.

### dnsglobe - 全球DNS传播检查器终端工具
*   **功能介绍:** 这是一个用Rust编写的终端用户界面(TUI)工具，它通过并行查询全球34个公共DNS解析器来检查DNS记录的传播情况，并在终端内的世界地图上展示结果。
*   **主要特点:**
    *   并行查询34个全球解析器（包括Google、Cloudflare、Quad9等）。
    *   在宽终端（≥150列）中显示世界地图，用不同颜色圆点表示各解析器状态。
    *   自动“监视模式”，每30秒轮询直至传播达到100%。
    *   智能分组答案，正确处理轮询DNS（Round-robin DNS）。
    *   发现并显示实际应答查询的任播站点（例如，`→YUL`）。
    *   支持通过TOML配置文件自定义解析器列表。
*   **为何值得关注:** 它将流行的网页功能（如dnschecker.org）直接带入终端，并增加了独特功能。实时的视觉世界地图和监视模式使其成为开发者、网络工程师以及任何DNS记录管理者即时、有效监控传播情况的强大且独特的工具。

**[View Repository / 查看仓库](https://github.com/514-labs/dnsglobe)**

### 🎬 Your Button Is Lying to Your Microcontroller...
**Channel:** C Labs
*   This video explores the common and frustrating issue of **"switch bounce"** in mechanical push buttons, where a single physical press registers as multiple erratic signals to a microcontroller.
*   **Key topics discussed:**
    *   The physics behind mechanical switch contact bounce.
    *   Why this can cause unintended multiple triggers in digital circuits and code.
    *   A clear explanation of software and hardware **debouncing** techniques.
    *   Practical examples showing how to implement solutions to ensure one press equals one reliable action.
*   It's a fantastic, essential watch for anyone learning electronics, Arduino, or microcontroller programming, as it demystifies a fundamental real-world problem that can make projects seem buggy and provides immediate, actionable fixes.

### 🎬 你的按钮在对你的微控制器撒谎...
**频道:** C Labs
*   **视频内容概述:** 本视频深入探讨了一个常见且令人头疼的问题——机械按钮的 **“触点抖动”**。即一次物理按压，在微控制器看来却可能表现为一连串杂乱的信号。
*   **主要话题:**
    *   机械开关触点抖动的物理原理。
    *   为什么这会导致数字电路和代码中出现意外的多次触发。
    *   清晰的**软件与硬件消抖**技术讲解。
    *   展示如何实现解决方案，以确保“一次按压等于一次可靠触发”的实际案例。
*   **为何值得观看:** 这是所有学习电子学、Arduino或微控制器编程的人必看的视频。它清晰揭示了使项目看似不稳定的基本现实问题，并提供了立竿见影的实用解决方法。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=3b1QXhSeJKw)**

### 🎬 Claude Desktop Is Now FREE?! Use ALL Claude Models (Full Setup Guide)
**Channel:** Data Scientist Afzal
*   The video provides a complete walkthrough for setting up Claude Desktop, which now apparently offers free access to the entire suite of Claude AI models.
*   Key topics include the process of getting free access, navigating the desktop application, and utilizing the various Claude models (likely different versions like Claude 3 Haiku, Sonnet, Opus, etc.) for different tasks.
*   It's worth watching for anyone interested in AI tools, as it offers a timely guide to accessing a powerful, professional-grade AI assistant platform without cost, which could be a significant resource for productivity, coding, and creative work.

### 🎬 Claude桌面版现在免费了？！使用所有Claude模型（完整设置指南）
**频道:** Data Scientist Afzal
*   视频内容概述：本视频详细演示了如何设置和使用现已提供免费访问所有Claude模型的Claude桌面应用程序。
*   主要话题：讲解获取免费权限的步骤、桌面应用的操作界面，以及如何针对不同任务使用各种Claude模型（如不同版本的Claude 3）。
*   为何值得观看：对于AI工具爱好者和使用者来说，这是一个及时且实用的教程，指导人们免费使用一个强大的专业级AI助手平台，能极大提升生产力、编程和创意工作的效率。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=8NlxDB1VIyY)**

### 🎬 The Ultimate Claude Code Tutorial for Mobile Apps - FULL COURSE
**Channel:** Codesistency
*   This is a comprehensive, full-length tutorial focused on using **Claude Code** specifically for **mobile application development**.
*   The video likely covers everything from setting up Claude Code in your environment, its core commands and workflows, to applying it in practical mobile app projects, possibly including both iOS and Android development.
*   It's worth watching for developers or tech enthusiasts looking to master AI-powered coding tools to dramatically accelerate their mobile app development cycle, build features faster, and solve coding problems efficiently.

### 🎬 Claude Code移动端应用完全教程 (完整课程)
**频道:** Codesistency
*   本视频是一个专注于如何使用 **Claude Code** 进行 **移动应用开发** 的完整教程。
*   视频内容可能涵盖从在开发环境中配置Claude Code、掌握其核心命令与工作流，到在实际移动应用项目中的具体应用，可能同时涉及iOS和Android平台的开发。
*   对于希望利用AI编程工具大幅提升移动应用开发效率、快速构建功能、高效解决编码问题的开发者或科技爱好者而言，本视频极具观看价值。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=p80OV6kjIO8)**

