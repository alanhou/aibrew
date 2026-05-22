---
title: "Daily Tech Digest: May 23, 2026"
date: 2026-05-23
description: "Today's digest: 5 Hacker News articles, 3 GitHub trending repos, 4 fast-moving projects, 9 YouTube videos, 0 Hugging Face models. 今日精选：5篇黑客新闻，3个热门项目，4个快速崛起项目，9个YouTube视频，0个Hugging Face模型。"
categories: [Daily Digest]
tags: [HackerNews, GitHub, YouTube, HuggingFace]
pin: false
---

### 美国研究人员在与外国合作者发表论文时面临新限制

*仅根据标题推测:*

* 本文可能报道美国政府出台的新政策或法规，限制美国研究人员与国际同行在学术出版物上的合作方式
* 文章可能讨论国家安全、知识产权保护或地缘政治紧张局势（特别是与中国等国家）如何推动这些限制措施
* 内容可能探讨这些限制对科学合作、学术自由和全球研究界的影响

**为何值得关注:**
* 凸显国家安全关切与开放科学合作之间日益加剧的矛盾
* 影响全球范围内的研究人员、大学和更广泛的科学界
* 反映影响国际学术合作和知识共享的更广泛地缘政治变化

**[Read Original / 阅读原文](https://www.science.org/content/article/u-s-researchers-face-new-restrictions-publishing-foreign-collaborators)**

### Microsoft Cancels Claude Code Pilot After Budget Overrun

* Microsoft's Claude Code pilot, launched in December 2025, consumed the entire annual AI budget within months due to token-based billing, leading to cancellation effective June 30, 2026
* Token-based pricing created invisible costs under flat seat licensing that became unsustainable once usage-based billing revealed true consumption at enterprise scale
* Microsoft is redirecting developers to GitHub Copilot, while Anthropic faces investor scrutiny during its $900B valuation fundraising round
* Enterprise procurement teams lack frameworks to forecast or cap token-based AI spending, exposing a structural gap in AI cost management
* AI cost management vendors and flat-rate pricing models gain competitive advantage as enterprises seek predictable AI budgeting
* Key unknowns include exact token consumption figures, whether other Microsoft divisions are affected, and the status of Microsoft-Anthropic negotiations

### 微软因预算超支取消 Claude Code 试点项目

* 微软于 2025 年 12 月启动的 Claude Code 试点项目因基于 token 的计费模式在数月内耗尽全年 AI 预算,将于 2026 年 6 月 30 日终止
* 基于 token 的定价在固定席位许可下隐藏了真实成本,一旦切换到基于使用量的计费,企业规模的真实消耗立即变得难以承受
* 微软正将开发人员转向自家的 GitHub Copilot,而 Anthropic 在进行 9000 亿美元估值融资时面临投资者审查
* 企业采购团队缺乏预测或限制基于 token 的 AI 支出的框架,暴露了 AI 成本管理的结构性缺口
* AI 成本管理供应商和固定费率定价模式获得竞争优势,因为企业寻求可预测的 AI 预算方案
* 关键未知信息包括确切的 token 消耗数据、微软其他部门是否受影响,以及微软与 Anthropic 的谈判状态

**[Read Original / 阅读原文](https://aiweekly.co/alerts/microsoft-drops-claude-code-after-budget-overrun)**


## 🔥 GitHub Trending / GitHub 热门项目

### Claude Code Plugins Directory - Official Plugin Marketplace for Claude Code

* **What it does**: Serves as the official, curated directory of high-quality plugins for Claude Code, Anthropic's AI-powered development environment. Provides a centralized marketplace where developers can discover, install, and manage plugins that extend Claude Code's capabilities.

* **Key features**: 
  - Dual plugin ecosystem with internal (Anthropic-developed) and external (community/partner) plugins
  - Standardized plugin structure supporting MCP servers, slash commands, agents, and skills
  - Simple installation via `/plugin install` command or discovery interface
  - Quality and security vetting for external submissions through formal review process
  - Comprehensive plugin metadata system with `.claude-plugin/plugin.json` configuration

* **Why it's notable**: This is Anthropic's first official plugin marketplace for Claude Code, marking a significant expansion of the platform's extensibility. With 2,556 stars in a single day, it demonstrates strong developer interest in customizing and enhancing AI-powered development workflows. The structured approach to plugin management and security vetting addresses common concerns about third-party integrations while fostering an ecosystem around Claude's development tools.

---

### Claude Code 插件目录 - Claude Code 官方插件市场

* **功能介绍**: 作为 Claude Code 的官方精选插件目录，为 Anthropic 的 AI 驱动开发环境提供集中式插件市场。开发者可以在此发现、安装和管理扩展 Claude Code 功能的插件。

* **主要特点**:
  - 双重插件生态系统，包含内部插件（Anthropic 开发）和外部插件（社区/合作伙伴）
  - 标准化插件结构，支持 MCP 服务器、斜杠命令、代理和技能模块
  - 通过 `/plugin install` 命令或发现界面轻松安装
  - 外部插件提交需通过正式审核流程，确保质量和安全性
  - 完善的插件元数据系统，使用 `.claude-plugin/plugin.json` 配置

* **为何值得关注**: 这是 Anthropic 为 Claude Code 推出的首个官方插件市场，标志着该平台可扩展性的重大提升。单日获得 2,556 星标，显示出开发者对定制和增强 AI 驱动开发工作流的强烈兴趣。结构化的插件管理方式和安全审核机制解决了第三方集成的常见顾虑，同时围绕 Claude 开发工具培育了一个健康的生态系统。

**[View Repository / 查看仓库](https://github.com/anthropics/claude-plugins-official)**

### CodeGraph - Pre-indexed Semantic Code Intelligence for AI Coding Assistants

* **What it does**: Creates a local knowledge graph of your codebase that AI coding assistants (Claude Code, Cursor, Codex, OpenCode, Hermes Agent) can query instantly instead of scanning files repeatedly with grep/find/read operations
* **Key features**: 
  - Reduces costs by ~35% and tool calls by ~70% through pre-indexed symbol relationships and call graphs
  - Supports 19+ languages (TypeScript, Python, Rust, Go, Java, etc.) with framework-aware routing for 14+ web frameworks
  - 100% local SQLite database with auto-sync file watching - no API keys or external services
  - Self-contained binaries with bundled runtime - no Node.js installation required
  - One-command installation that auto-configures multiple AI coding agents
* **Why it's notable**: Addresses a major inefficiency in AI coding workflows where agents waste tokens and time repeatedly exploring codebases. Benchmark shows 35% cost reduction, 59% fewer tokens, 49% faster responses, and 70% fewer tool calls across 7 real-world projects. The gains scale with codebase size - on VS Code (~10k files) it achieved 73% fewer tokens and 72% fewer tool calls. Trending with 3,688 stars today as developers seek to optimize AI assistant costs and performance.

---

### CodeGraph - AI 编码助手的预索引语义代码智能工具

* **功能介绍**: 为代码库创建本地知识图谱,让 AI 编码助手(Claude Code、Cursor、Codex、OpenCode、Hermes Agent)可以即时查询,而无需反复使用 grep/find/read 操作扫描文件
* **主要特点**:
  - 通过预索引的符号关系和调用图,降低约 35% 成本和 70% 工具调用次数
  - 支持 19+ 种编程语言(TypeScript、Python、Rust、Go、Java 等),并能识别 14+ 个 Web 框架的路由
  - 100% 本地 SQLite 数据库,带自动同步文件监控 - 无需 API 密钥或外部服务
  - 自包含二进制文件,内置运行时 - 无需安装 Node.js
  - 一键安装,自动配置多个 AI 编码代理
* **为何值得关注**: 解决了 AI 编码工作流中的重大效率问题 - 代理会浪费大量 token 和时间反复探索代码库。基准测试显示在 7 个真实项目中实现了 35% 成本降低、59% token 减少、49% 响应加速和 70% 工具调用减少。收益随代码库规模扩大 - 在 VS Code(约 1 万个文件)上实现了 73% token 减少和 72% 工具调用减少。今日获得 3,688 星标,开发者正在寻求优化 AI 助手的成本和性能。

**[View Repository / 查看仓库](https://github.com/colbymchenry/codegraph)**

### RuView - WiFi-Based Spatial Intelligence Without Cameras

* **What it does**: Transforms ordinary WiFi signals into a contactless sensing system that detects presence, monitors vital signs (breathing and heart rate), tracks movement, and estimates human poses—all through walls and in complete darkness without cameras or wearables.

* **Key features**: 
  - Runs on $9 ESP32 hardware with pretrained 8KB models (100% validation accuracy for presence detection)
  - Real-time vital sign monitoring: breathing rate (6-30 BPM) and heart rate (40-120 BPM) using Channel State Information (CSI)
  - 17-keypoint pose estimation, fall detection, multi-person counting, and through-wall sensing up to 5m
  - 105-module edge intelligence catalog for health, security, retail, and industrial applications
  - Fully local processing with cryptographic attestation—no cloud, no internet required
  - Optional Cognitum Seed integration ($140 total) adds persistent vector storage and witness chain

* **Why it's notable**: Achieves camera-free spatial intelligence using physics-based WiFi sensing at commodity hardware prices. With 992 stars today and 1,463 passing tests, it demonstrates production-ready contactless monitoring for privacy-sensitive applications like healthcare, elderly care, and smart buildings. The pretrained model is published on Hugging Face, and the system processes 164,183 embeddings/second on M4 Pro hardware.

---

### RuView - 基于 WiFi 的无摄像头空间智能系统

* **功能介绍**: 将普通 WiFi 信号转化为非接触式传感系统,可穿墙检测人员存在、监测生命体征(呼吸和心率)、追踪运动并估计人体姿态——完全在黑暗中运行,无需摄像头或可穿戴设备。

* **主要特点**:
  - 运行在 9 美元的 ESP32 硬件上,使用 8KB 预训练模型(存在检测验证准确率 100%)
  - 实时生命体征监测:通过信道状态信息(CSI)测量呼吸频率(6-30 次/分)和心率(40-120 次/分)
  - 17 关键点姿态估计、跌倒检测、多人计数、穿墙感知(最远 5 米)
  - 105 个边缘智能模块目录,涵盖健康、安全、零售和工业应用
  - 完全本地处理并提供加密认证——无需云服务或互联网连接
  - 可选 Cognitum Seed 集成(总成本 140 美元)增加持久化向量存储和见证链

* **为何值得关注**: 以商用硬件价格实现基于物理原理的无摄像头空间智能。今日获得 992 星标,拥有 1,463 个通过测试,展示了面向隐私敏感场景(如医疗保健、老年护理和智能建筑)的生产就绪非接触式监测能力。预训练模型已发布在 Hugging Face,系统在 M4 Pro 硬件上每秒处理 164,183 个嵌入向量。

**[View Repository / 查看仓库](https://github.com/ruvnet/RuView)**


## 🚀 Fast-Moving Repos / 快速崛起项目

### GuJumpgate - Automated GPT Plus Registration Browser Extension

* **What it does**: A browser extension that automates the entire process of registering OpenAI free accounts and upgrading them to GPT Plus using PayPal, including automatic email alias creation, payment form filling, and OAuth callbacks.

* **Key features**: 
  - Fully automated free account registration via FlowPilot integration
  - Complete PayPal activation flow (Stripe billing, PayPal form auto-fill)
  - Hotmail/Outlook automatic alias functionality
  - PayPal phone number pool management
  - Local and panel OAuth callback support
  - Session JSON export (no refresh token) to bypass OAuth restrictions

* **Why it's notable**: Achieves 100% success rate in testing for automated GPT Plus activation, addressing the challenge of manual registration and payment processes. Built on FlowPilot with significant adaptations for current OpenAI registration requirements. Particularly relevant given OAuth restrictions requiring phone verification—the tool pivots to session-based JSON exports as a workaround.

---

### GuJumpgate - 全自动 GPT Plus 注册浏览器扩展

* **功能介绍**: 一个浏览器扩展,可自动完成 OpenAI 免费账号注册并通过 PayPal 升级至 GPT Plus 的全流程,包括自动创建邮箱别名、自动填写支付表单和 OAuth 回调。

* **主要特点**:
  - 通过 FlowPilot 集成实现全自动免费账号注册
  - 完整的 PayPal 激活流程(Stripe 账单、PayPal 表单自动填写)
  - Hotmail/Outlook 自动别名功能
  - PayPal 号码池管理
  - 支持本地及各面板的 OAuth 回调
  - 导出 Session JSON(无刷新令牌)以绕过 OAuth 限制

* **为何值得关注**: 测试中实现了 100% 的 GPT Plus 自动激活成功率,解决了手动注册和支付流程的痛点。基于 FlowPilot 项目进行了大量适配以应对当前 OpenAI 注册要求。特别针对 OAuth 风控严重需要手机验证的问题,提供了基于 Session 的 JSON 导出方案作为替代方案。

**[View Repository / 查看仓库](https://github.com/FoundZiGu/GuJumpgate)**

### 9arm-skills - Claude Code Agent Skills Collection

* **What it does**: A curated collection of specialized skills/prompts that extend Claude Code's capabilities for software engineering and productivity workflows
* **Key features**: 
  - Structured skill library organized by category (engineering, productivity, misc, personal)
  - Each skill is a standalone module with YAML frontmatter defining name and description
  - Includes debugging methodology (debug-mantra), post-mortem documentation, code review (scrutinize), and management communication skills
  - Simple installation via symlink script to `~/.claude/skills/`
* **Why it's notable**: Demonstrates how to systematically enhance AI coding assistants with domain-specific expertise through modular, reusable skill definitions. Shows practical patterns for structuring agent capabilities beyond base model knowledge.

---

### 9arm-skills - Claude Code 智能体技能集合

* **功能介绍**: 为 Claude Code 提供的专业技能/提示词集合,扩展其在软件工程和生产力工作流中的能力
* **主要特点**:
  - 按类别组织的结构化技能库(工程、生产力、杂项、个人)
  - 每个技能都是独立模块,包含 YAML 前置元数据定义名称和描述
  - 包含调试方法论(debug-mantra)、事后分析文档、代码审查(scrutinize)和管理沟通等技能
  - 通过符号链接脚本简单安装到 `~/.claude/skills/`
* **为何值得关注**: 展示了如何通过模块化、可复用的技能定义系统性地增强 AI 编码助手的领域专业能力。为构建超越基础模型知识的智能体能力提供了实用模式参考。

**[View Repository / 查看仓库](https://github.com/thananon/9arm-skills)**


## 🎬 YouTube Tech Videos / YouTube 技术视频

### 🎬 Google's AI endgame is here… everything you missed at Google I/O 2026

**Channel:** Fireship

* What the video covers: A comprehensive recap of Google I/O 2026's major announcements, focusing on Google's latest AI strategy and product releases that signal their "endgame" in the AI race
* Key topics discussed: New AI models and capabilities, integration across Google's product ecosystem, developer tools and APIs, competitive positioning against other AI platforms, and the strategic direction Google is taking with artificial intelligence
* Why it's worth watching: Fireship delivers fast-paced, technically detailed breakdowns of major tech events with sharp analysis and humor. This video cuts through the marketing hype to explain what actually matters for developers and tech professionals from one of 2026's most significant tech conferences

---

### 🎬 Google 的 AI 终局已至……Google I/O 2026 你错过的一切

**频道:** Fireship

* 视频内容概述: 全面回顾 Google I/O 2026 大会的重大发布，聚焦 Google 最新的 AI 战略和标志其在 AI 竞赛中"终局"的产品发布
* 主要话题: 新的 AI 模型和能力、跨 Google 产品生态系统的整合、开发者工具和 API、与其他 AI 平台的竞争定位，以及 Google 在人工智能领域的战略方向
* 为何值得观看: Fireship 以快节奏、技术细节丰富的方式解读重大科技活动，分析犀利且幽默风趣。这个视频剥离营销炒作，为开发者和技术专业人士解释 2026 年最重要的科技大会中真正重要的内容

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=9OQ5vaYbGV0)**

### 🎬 Chip Design from the Bottom Up – Reiner Pope

**Channel:** Dwarkesh Patel

* **What the video covers:** A comprehensive blackboard lecture explaining how computer chips work, starting from fundamental logic gates and building up to modern chip architecture
* **Key topics discussed:** Basic logic gates, transistor-level design, circuit composition, architectural layers that enable modern computing hardware
* **Why it's worth watching:** Rare deep-dive into chip design fundamentals presented in an accessible lecture format; bridges the gap between theoretical computer science and physical hardware implementation; valuable for anyone wanting to understand the foundation of modern computing

---

### 🎬 芯片设计从零开始 – Reiner Pope

**频道:** Dwarkesh Patel

* **视频内容概述:** 一场全面的黑板讲座，从基础逻辑门开始讲解计算机芯片的工作原理，逐步深入到现代芯片架构
* **主要话题:** 基本逻辑门、晶体管级设计、电路组合、支撑现代计算硬件的架构层次
* **为何值得观看:** 难得的芯片设计基础深度讲解，以易懂的讲座形式呈现；连接理论计算机科学与物理硬件实现之间的桥梁；对想要理解现代计算基础的任何人都很有价值

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=oIk3R-sMX5o)**

### 🎬 Why Good Companies Go Bad (And How to Stop It)
**Channel:** Y Combinator

* What the video covers: Eric Ries, author of "The Lean Startup," discusses insights from his new book about why successful companies decline and lose their competitive edge over time
* Key topics discussed: Organizational decay patterns, the transition from startup agility to corporate bureaucracy, systemic issues that cause good companies to fail, and practical frameworks for maintaining innovation and adaptability at scale
* Why it's worth watching: Essential viewing for founders, executives, and anyone interested in organizational health—offers actionable strategies from one of the most influential voices in startup methodology to prevent the common pitfalls that derail even the most promising companies

---

### 🎬 为什么好公司会走向衰败(以及如何阻止)
**频道:** Y Combinator

* 视频内容概述: 《精益创业》作者 Eric Ries 讨论其新书中关于成功公司为何会衰落并失去竞争优势的见解
* 主要话题: 组织衰退模式、从创业公司敏捷性到企业官僚主义的转变、导致优秀公司失败的系统性问题,以及在规模化过程中保持创新和适应能力的实用框架
* 为何值得观看: 创始人、高管和所有关注组织健康的人必看——来自创业方法论领域最具影响力的声音之一,提供可操作的策略来避免导致最有前途的公司脱轨的常见陷阱

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=7VKliOQXQ9M)**

### 🎬 Wait Till The End #shorts #sheryianscodingschool #placement #engineering
**Channel:** Sheryians Coding School

* What the video covers: A satirical take on common career advice given to engineering students in India, particularly around learning Python, DSA (Data Structures & Algorithms), and AI
* Key topics discussed: The repetitive and often oversimplified career guidance that engineering students receive about tech skills and job placement strategies
* Why it's worth watching: Relatable humor for engineering students and tech learners who've experienced the pressure of following trending tech advice; offers a comedic perspective on the gap between advice and reality in tech education

---

### 🎬 等到最后 #shorts #编程学校 #就业 #工程
**频道:** Sheryians Coding School

* 视频内容概述: 讽刺印度工程专业学生常听到的职业建议，特别是关于学习 Python、数据结构与算法(DSA)和人工智能的建议
* 主要话题: 工程学生收到的重复且过于简化的职业指导，涉及技术技能和求职策略
* 为何值得观看: 对于经历过追随热门技术建议压力的工程学生和技术学习者来说非常有共鸣；以幽默视角展现技术教育中建议与现实之间的差距

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=MFiOI1q9oLs)**

### 🎬 How to Make an Arduino Solar Panel Tracker | Easy Project Tutorial #shorts
**Channel:** Seun Tech

* What the video covers: A complete step-by-step tutorial on building an automatic solar tracking system using Arduino and light-dependent resistors (LDRs)
* Key topics discussed: Arduino IDE programming, LDR sensor integration, servo motor control for panel positioning, and automated sun-tracking mechanism
* Why it's worth watching: Perfect beginner-friendly Arduino project that combines hardware and software skills while creating a practical renewable energy application that maximizes solar panel efficiency

---

### 🎬 如何制作 Arduino 太阳能板追踪器 | 简易项目教程
**频道:** Seun Tech

* 视频内容概述: 使用 Arduino 和光敏电阻 (LDR) 构建自动太阳追踪系统的完整分步教程
* 主要话题: Arduino IDE 编程、LDR 传感器集成、伺服电机控制面板定位、自动追日机制
* 为何值得观看: 适合初学者的 Arduino 项目，结合硬件和软件技能，创建实用的可再生能源应用，最大化太阳能板效率

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=xj1FMq41tBg)**

### Project Glasswing: AI-Powered Vulnerability Detection Shows Dramatic Results

* **Anthropic's Project Glasswing has found over 10,000 high/critical-severity vulnerabilities** in one month using Claude Mythos Preview, across critical infrastructure software maintained by ~50 partners
* **Partners report 10x increase in bug-finding rates** - Cloudflare alone discovered 2,000 bugs (400 high/critical-severity) with better accuracy than human testers
* **Mythos Preview is the first model to solve UK AI Security Institute's cyber ranges end-to-end**, and Mozilla found 271 vulnerabilities in Firefox 150 (10x more than previous models)
* **Open-source scan results: 6,202 estimated high/critical vulnerabilities found** across 1,000+ projects; 90.6% true positive rate after independent verification, with 62.4% confirmed as high/critical-severity
* **Bottleneck has shifted from finding bugs to patching them** - major vendors like Palo Alto Networks (5x more patches), Microsoft, and Oracle are accelerating their patch release cycles
* **Notable discovery: wolfSSL certificate forgery vulnerability** (CVE-2026-5194) that could enable attackers to create fake banking/email websites
* **Mythos Preview also proved useful beyond code security**, helping detect and prevent a $1.5M fraudulent wire transfer at a partner bank
* **90-day disclosure policy creates lag in public reporting** - full details will be shared once patches are widely deployed to protect end users

### Glasswing 项目：AI 驱动的漏洞检测显示显著成果

* **Anthropic 的 Glasswing 项目一个月内发现超过 10,000 个高危/严重漏洞**，使用 Claude Mythos Preview 扫描约 50 个合作伙伴维护的关键基础设施软件
* **合作伙伴报告漏洞发现率提高 10 倍** - 仅 Cloudflare 就发现了 2,000 个漏洞（其中 400 个为高危/严重级别），准确率优于人工测试
* **Mythos Preview 是首个端到端解决英国 AI 安全研究所网络靶场的模型**，Mozilla 在 Firefox 150 中发现 271 个漏洞（是之前模型的 10 倍）
* **开源软件扫描结果：在 1,000 多个项目中发现 6,202 个估计的高危/严重漏洞**；经独立验证后真阳性率达 90.6%，其中 62.4% 确认为高危/严重级别
* **瓶颈已从发现漏洞转向修补漏洞** - Palo Alto Networks（补丁数量增加 5 倍）、微软和甲骨文等主要供应商正在加速补丁发布周期
* **重要发现：wolfSSL 证书伪造漏洞**（CVE-2026-5194），可能使攻击者创建虚假银行/电子邮件网站
* **Mythos Preview 在代码安全之外也证明有用**，帮助合作银行检测并阻止了一起 150 万美元的欺诈性电汇
* **90 天披露政策导致公开报告滞后** - 完整细节将在补丁广泛部署后分享，以保护最终用户

**[Read Original / 阅读原文](https://www.anthropic.com/research/glasswing-initial-update)**

### Why Japanese Companies Excel at Diversification: From Toilets to Semiconductors

* **Toto's unexpected pivot**: The world's largest toilet manufacturer now derives most profits from electrostatic chucks (e-chucks) used in semiconductor production, with stock up 60% in 2026 due to AI-driven chip demand
* **Extreme diversification is the norm**: Japanese firms routinely operate across unrelated industries—Kyocera makes ceramics, printers, smartphones, and artificial joints; Yamaha produces pianos, motorcycles, and industrial robots
* **High-precision across domains**: Unlike conglomerates in developing economies, Japanese firms excel at complex, high-tech products across their diverse portfolios—many critical semiconductor components are made almost exclusively by Japanese companies
* **Structural differences from Western firms**: American companies prioritize focus and specialization, while Japanese corporations succeed through a fundamentally different organizational model
* **Post-Fordist manufacturing advantage**: The article references Milgrom and Roberts' 1990 paper on how Japanese firms pioneered flexible, multi-product manufacturing with rapid changeovers, cross-trained workers, and embedded quality control
* **Adapted corporate species**: Japanese corporations represent an alternative form of business organization—not better or worse overall, but exceptionally suited to certain types of production and innovation that Western firms struggle with

### 日本企业为何擅长多元化经营：从马桶到半导体

* **Toto的意外转型**：全球最大马桶制造商现在大部分利润来自半导体生产用的静电吸盘（e-chuck），2026年股价因AI驱动的芯片需求上涨60%
* **极端多元化是常态**：日本企业常规跨不相关行业运营——京瓷生产陶瓷、打印机、智能手机和人工关节；雅马哈生产钢琴、摩托车和工业机器人
* **跨领域高精度制造**：与发展中国家的企业集团不同，日本公司在其多元化产品组合中都擅长复杂高科技产品——许多关键半导体组件几乎只由日本公司制造
* **与西方企业的结构性差异**：美国公司优先考虑专注和专业化，而日本企业通过根本不同的组织模式取得成功
* **后福特制造优势**：文章引用Milgrom和Roberts 1990年论文，说明日本企业如何开创灵活的多产品制造模式，具有快速转换、跨技能培训工人和嵌入式质量控制
* **适应性企业物种**：日本企业代表了一种替代性商业组织形式——总体上不是更好或更差，而是特别适合西方企业难以应对的某些类型的生产和创新

**[Read Original / 阅读原文](https://davidoks.blog/p/why-japanese-companies-do-so-many)**

### Models.dev: Open-Source AI Model Database

* **Comprehensive AI model database** - Open-source repository containing specifications, pricing, and capabilities for AI models across multiple providers
* **RESTful API access** - Query model data via `https://models.dev/api.json` with Model IDs compatible with AI SDK
* **Community-driven contributions** - Data stored as TOML files organized by provider, with automated validation via GitHub Actions
* **Provider logos available** - SVG logos accessible at `https://models.dev/logos/{provider}.svg` with fallback defaults
* **Detailed model specifications** - Tracks pricing (input/output/reasoning tokens), context limits, modalities (text/image/audio/video), capabilities (tool calling, structured output, reasoning), and metadata (release dates, knowledge cutoff)
* **Extends mechanism for wrappers** - Reuse canonical model definitions for wrapper providers to avoid duplication
* **Schema validation** - Enforces required fields including cost structure, token limits, supported modalities, and feature flags
* **Integration with opencode** - Used internally by opencode.ai for model management
* **Active development** - Requires Bun for local development, includes frontend at localhost:3000 and migration comparison tools

### Models.dev:开源 AI 模型数据库

* **全面的 AI 模型数据库** - 开源仓库,包含多个提供商的 AI 模型规格、定价和功能信息
* **RESTful API 访问** - 通过 `https://models.dev/api.json` 查询模型数据,模型 ID 与 AI SDK 兼容
* **社区驱动贡献** - 数据以 TOML 文件按提供商组织存储,通过 GitHub Actions 自动验证
* **提供商 Logo 可用** - SVG 格式 Logo 可通过 `https://models.dev/logos/{provider}.svg` 访问,带默认回退
* **详细模型规格** - 跟踪定价(输入/输出/推理 token)、上下文限制、模态(文本/图像/音频/视频)、功能(工具调用、结构化输出、推理)和元数据(发布日期、知识截止日期)
* **包装器扩展机制** - 为包装提供商重用规范模型定义以避免重复
* **模式验证** - 强制要求必填字段,包括成本结构、token 限制、支持的模态和功能标志
* **与 opencode 集成** - 被 opencode.ai 内部用于模型管理
* **活跃开发** - 本地开发需要 Bun,包含 localhost:3000 前端和迁移对比工具

**[Read Original / 阅读原文](https://github.com/anomalyco/models.dev)**

### ai-engineering-from-scratch - Comprehensive AI Engineering Curriculum from First Principles

* **What it does**: A complete, hands-on curriculum teaching AI engineering from mathematical foundations to production-ready autonomous systems. 435 lessons across 20 phases covering everything from linear algebra to multi-agent swarms, with every lesson producing a reusable artifact (prompt, skill, agent, or MCP server).

* **Key features**: 
  - Four-language implementation (Python, TypeScript, Rust, Julia) with ~320 hours of content
  - "Build it from scratch, then use the framework" approach - implement algorithms from raw math before using PyTorch/sklearn
  - Every lesson ships a working tool: prompts, agent skills, autonomous agents, or MCP servers
  - Built-in placement quiz (`/find-your-level`) and phase-specific comprehension checks
  - Linear progression from math foundations → ML fundamentals → deep learning → transformers → LLMs → agents → production systems

* **Why it's notable**: Bridges the gap between AI tool usage (84% of students) and professional readiness (only 18%). Unlike scattered tutorials, this provides a complete spine connecting theory to practice. Gained 988 stars today because it offers what most AI education lacks: deep understanding through implementation, not just API calls. Free, open-source (MIT), and designed to run on your laptop without expensive cloud resources.

---

### ai-engineering-from-scratch - 从零开始的 AI 工程完整课程

* **功能介绍**: 从数学基础到生产级自主系统的完整 AI 工程实战课程。20 个阶段共 435 节课,涵盖从线性代数到多智能体集群的所有内容,每节课都产出可复用的工件(提示词、技能、智能体或 MCP 服务器)。

* **主要特点**:
  - 四种语言实现(Python、TypeScript、Rust、Julia),约 320 小时内容
  - "先从零构建,再使用框架"的教学方法 - 先用纯数学实现算法,再使用 PyTorch/sklearn
  - 每节课都交付实用工具:提示词、智能体技能、自主智能体或 MCP 服务器
  - 内置水平测试(`/find-your-level`)和分阶段理解检查
  - 线性进阶路径:数学基础 → 机器学习 → 深度学习 → Transformer → LLM → 智能体 → 生产系统

* **为何值得关注**: 弥合了 AI 工具使用(84% 学生)与职业准备(仅 18%)之间的鸿沟。不同于零散教程,本课程提供了连接理论与实践的完整体系。今日获得 988 星是因为它提供了大多数 AI 教育所缺乏的:通过实现获得深度理解,而非仅仅调用 API。免费开源(MIT 协议),可在个人笔记本上运行,无需昂贵的云资源。

**[View Repository / 查看仓库](https://github.com/rohitg00/ai-engineering-from-scratch)**

### Chrome DevTools MCP - Chrome DevTools for Coding Agents

* **What it does**: Enables AI coding assistants (like Claude, Cursor, Copilot) to control and inspect a live Chrome browser through the Model Context Protocol (MCP), providing full access to Chrome DevTools capabilities for automation, debugging, and performance analysis.

* **Key features**: 
  * Performance insights through Chrome DevTools trace recording and analysis
  * Advanced browser debugging with network inspection, screenshots, and console messages with source-mapped stack traces
  * Reliable automation using Puppeteer with automatic action result waiting
  * Supports both full-featured and slim modes for basic browser tasks
  * Integration with Chrome User Experience Report (CrUX) for real-user performance data

* **Why it's notable**: Bridges the gap between AI coding agents and browser automation by exposing Chrome DevTools' powerful debugging and performance tools through a standardized protocol. With 499 stars today, it's gaining rapid traction as developers seek to enhance their AI assistants with real browser control capabilities. Officially supported by the Chrome DevTools team and compatible with major AI coding tools (Claude Code, Copilot, Cursor, Cline, Antigravity).

---

### Chrome DevTools MCP - AI 编程助手的 Chrome 开发者工具

* **功能介绍**: 让 AI 编程助手(如 Claude、Cursor、Copilot)通过模型上下文协议(MCP)控制和检查实时 Chrome 浏览器,提供完整的 Chrome DevTools 功能用于自动化、调试和性能分析。

* **主要特点**:
  * 通过 Chrome DevTools 跟踪记录和分析获取性能洞察
  * 高级浏览器调试功能,包括网络检查、截图和带源映射堆栈跟踪的控制台消息
  * 使用 Puppeteer 实现可靠的自动化,自动等待操作结果
  * 支持完整功能模式和精简模式以满足基本浏览器任务需求
  * 集成 Chrome 用户体验报告(CrUX)获取真实用户性能数据

* **为何值得关注**: 通过标准化协议将 AI 编程助手与浏览器自动化连接起来,暴露 Chrome DevTools 强大的调试和性能工具。今日获得 499 星标,随着开发者寻求用真实浏览器控制能力增强 AI 助手,该项目正快速获得关注。由 Chrome DevTools 团队官方支持,兼容主流 AI 编程工具(Claude Code、Copilot、Cursor、Cline、Antigravity)。

**[View Repository / 查看仓库](https://github.com/ChromeDevTools/chrome-devtools-mcp)**

### 🎬 The current story of human evolution may be incomplete - David Reich

**Channel:** Dwarkesh Patel

* **What the video covers:** David Reich, a leading geneticist, discusses how recent discoveries in ancient DNA are challenging and reshaping our understanding of human evolutionary history
* **Key topics discussed:** Gaps and inaccuracies in the traditional narrative of human evolution, insights from paleogenomics, evidence of previously unknown human populations and migrations, interbreeding between ancient human species
* **Why it's worth watching:** Reich is a pioneer in ancient DNA research whose work has fundamentally altered how we understand human origins. This conversation reveals how much of what we thought we knew about human evolution is being rewritten by genetic evidence, offering a cutting-edge perspective on one of science's most fundamental questions

---

### 🎬 人类进化的现有故事可能并不完整 - David Reich

**频道:** Dwarkesh Patel

* **视频内容概述:** 领先的遗传学家 David Reich 探讨古代 DNA 的最新发现如何挑战并重塑我们对人类进化史的理解
* **主要话题:** 传统人类进化叙事中的空白和不准确之处、古基因组学的洞见、先前未知的人类种群和迁徙的证据、古人类物种之间的杂交
* **为何值得观看:** Reich 是古代 DNA 研究的先驱,他的工作从根本上改变了我们对人类起源的理解。这次对话揭示了我们以为了解的人类进化知识有多少正在被基因证据改写,为科学最基本的问题之一提供了前沿视角

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=avkBfPoennY)**

### 🎬 How to make Jack in Melon Sandbox #melonsanbox #shorts
**Channel:** Vedid

* What the video covers: A tutorial demonstrating how to create a character named "Jack" within Melon Sandbox, a physics-based sandbox game
* Key topics discussed: Step-by-step creation process, game mechanics, character building techniques in Melon Sandbox
* Why it's worth watching: Quick, practical guide for Melon Sandbox players looking to recreate specific characters; credits original idea from @Блекикс, making it a community-driven tutorial

---

### 🎬 如何在 Melon Sandbox 中制作 Jack 角色
**频道:** Vedid

* 视频内容概述: 演示如何在物理沙盒游戏 Melon Sandbox 中创建名为"Jack"的角色的教程
* 主要话题: 分步创建流程、游戏机制、Melon Sandbox 中的角色构建技巧
* 为何值得观看: 为想要重现特定角色的 Melon Sandbox 玩家提供快速实用的指南；创意来自 @Блекикс，体现社区驱动的教学内容

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=k3N-fdn4RSk)**

### 🎬 Build Your Own Claude Code | Full AI Coding Agent Tutorial
**Channel:** Code With Antonio

* What the video covers: A comprehensive tutorial on building an AI coding agent from scratch, inspired by tools like Claude Code (Anthropic's AI coding assistant)
* Key topics discussed: Modern AI coding agent architecture, implementation details, and the underlying mechanisms that power AI-assisted development tools
* Why it's worth watching: Perfect for developers who want to understand how AI coding assistants work under the hood and gain hands-on experience building one themselves. Provides practical insights into the technology behind popular AI development tools.

### 🎬 从零构建你自己的 Claude Code | AI 编码代理完整教程
**频道:** Code With Antonio

* 视频内容概述: 从零开始构建一个受 Claude Code 启发的 AI 编码代理的完整教程，深入了解现代 AI 辅助开发工具的工作原理
* 主要话题: 现代 AI 编码代理的架构设计、具体实现细节，以及驱动 AI 辅助开发工具的核心机制
* 为何值得观看: 适合想要深入理解 AI 编码助手底层工作原理的开发者，通过实践构建自己的 AI 代理，获得对流行 AI 开发工具技术的实用洞察

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=k_D_C3ExypU)**

### 🎬 ОН НЕ ОСТАНАВЛИВАТЬСЯ!! (He Won't Stop!!)
**Channel:** Code mania school

* What the video covers: A Unity game development tutorial focusing on continuous movement mechanics in 2D games
* Key topics discussed: Unity 2D programming, C# scripting for character or object movement, implementing non-stop motion behavior
* Why it's worth watching: Quick tutorial demonstrating how to create persistent movement mechanics in Unity, useful for endless runner games or auto-scrolling platformers; practical for indie developers working on 2D projects

### 🎬 他停不下来!!
**频道:** Code mania school

* 视频内容概述: Unity 游戏开发教程,专注于 2D 游戏中的连续移动机制
* 主要话题: Unity 2D 编程、C# 角色或物体移动脚本、实现不停止运动行为
* 为何值得观看: 快速教程演示如何在 Unity 中创建持续移动机制,适用于无尽跑酷游戏或自动滚动平台游戏;对开发 2D 项目的独立开发者很实用

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=k2LGyKHlc6w)**

