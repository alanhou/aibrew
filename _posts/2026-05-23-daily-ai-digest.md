---
title: "Daily Tech Digest: May 23, 2026"
date: 2026-05-23
description: "Today's digest: 14 Hacker News articles, 3 GitHub trending repos, 7 fast-moving projects, 12 YouTube videos, 0 Hugging Face models. 今日精选：14篇黑客新闻，3个热门项目，7个快速崛起项目，12个YouTube视频，0个Hugging Face模型。"
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

### Shipping a Laptop to a Refugee Camp in Uganda: A Journey Through Bureaucracy and Perseverance

* **The Challenge**: A Congolese refugee named Django, studying Computer Science remotely from a Ugandan refugee camp with solar power and rationed internet, needed a replacement laptop after his motherboard burned out
* **Failed First Attempt**: Initial shipment via Australia Post ($111.60 AUD) was returned because lithium battery devices cannot be shipped internationally by air through their service
* **Second Attempt via Freight**: Used Pack & Send freight service ($213 AUD) with warnings about customs fees, taxes, and potential $50-100 buffer needed on recipient's end
* **Customs Bureaucracy**: Required Tax Identification Number (TIN) registration through Uganda Revenue Authority (URA) Portal, which refugees cannot complete online
* **Arduous TIN Journey**: Django traveled 5+ hours (2-hour walk + motorcycle + 3-hour bus) to URA office, was told to return for authorization letter, faced network "issues" and implicit bribery requests, waited hours while others were served, finally received TIN in 10 minutes after full day of persistence
* **Tax Payment**: Completed customs clearance with UGX 127,657.76 (~$47 AUD) in taxes, bringing total cost to ~$407 AUD
* **Seizure Issue**: Package routed through 9+ countries, temporarily seized because used laptops require original purchase receipts under Ugandan law
* **Resolution**: After additional UGX 50,000 (~$18.50 AUD) payment and proving it was a used gift, laptop was finally released and delivered
* **Total Journey**: Over one month from initial shipment to delivery, highlighting the extreme barriers refugees face in accessing basic educational resources

### 向乌干达难民营邮寄笔记本电脑:穿越官僚主义与坚持不懈的旅程

* **挑战背景**:刚果难民Django在乌干达难民营依靠太阳能和配给的网络远程攻读计算机科学学位,主板烧毁后急需替换笔记本电脑
* **首次失败尝试**:通过澳大利亚邮政寄送($111.60澳元)被退回,因为含锂电池设备不能通过航空国际邮寄
* **第二次货运尝试**:使用Pack & Send货运服务($213澳元),被警告需要支付关税、税费,收件人需准备$50-100澳元缓冲资金
* **海关官僚程序**:需要通过乌干达税务局(URA)门户网站注册税务识别号(TIN),难民无法在线完成
* **艰难的TIN申请之旅**:Django跋涉5小时以上(步行2小时+摩托车+巴士3小时)到达URA办公室,被要求返回获取授权信,遭遇网络"故障"和隐性贿赂要求,眼看他人正常办理而自己等待数小时,最终在坚持一整天后10分钟内获得TIN
* **税费支付**:完成海关清关,支付UGX 127,657.76(约$47澳元)税费,总成本达到约$407澳元
* **扣押问题**:包裹途经9个以上国家,因乌干达法律规定二手笔记本电脑需要原始购买收据而被临时扣押
* **最终解决**:额外支付UGX 50,000(约$18.50澳元)并证明是二手礼物后,笔记本电脑最终放行并送达
* **全程耗时**:从最初发货到交付超过一个月,凸显难民在获取基本教育资源时面临的极端障碍

**[Read Original / 阅读原文](https://notesbylex.com/shipping-a-laptop-to-a-refugee-camp-in-uganda)**

### How Decades of Sleep Research Led to a New Sleep Apnea Drug

* The article title suggests a breakthrough in sleep apnea treatment resulting from long-term research efforts
* A new pharmaceutical intervention for sleep apnea has been developed, representing a significant advancement in the field
* The development is connected to the Temerty Faculty of Medicine, indicating academic research origins
* Decades of accumulated sleep science knowledge contributed to this medical innovation
* This represents a potential alternative or complement to traditional sleep apnea treatments like CPAP machines

### 数十年睡眠研究催生新型睡眠呼吸暂停药物

* 文章标题表明长期研究工作在睡眠呼吸暂停治疗方面取得突破性进展
* 一种新的睡眠呼吸暂停药物治疗方法已被开发出来，代表该领域的重大进步
* 该研究成果与坦普尔蒂医学院相关，表明源自学术研究
* 数十年积累的睡眠科学知识为这一医学创新做出了贡献
* 这可能为传统睡眠呼吸暂停治疗方法（如CPAP呼吸机）提供替代或补充选择

**[Read Original / 阅读原文](https://temertymedicine.utoronto.ca/news/how-decades-sleep-research-led-new-sleep-apnea-drug)**

### Blood Pumping Mechanism of the Horse Hoof

* The horse's hoof contains a sophisticated "pumping mechanism" that assists in returning venous blood to the heart, compensating for the lack of muscles in the lower leg
* An extensive network of veins called the venous plexus is located on both sides of the lateral cartilages and within the sensitive structures of the hoof
* Compression of these veins by the plantar cushion against the lateral cartilages or the coffin bone against the hoof wall acts as a pump to force blood up the leg
* One-way valves in the leg veins prevent blood from flowing back down to the hoof, while compression creates a "hydraulic cushion" that dissipates concussion and protects the coffin bone
* When the hoof bears weight, veins compress and push blood upward; when lifted, veins open and refill through arterial pulse and gravity—this cycle is often called the horse's "second heart"

### 马蹄的血液泵送机制

* 马蹄包含一个复杂的"泵送机制"，协助将静脉血液输送回心脏，弥补下肢缺乏肌肉的不足
* 一个广泛的静脉网络称为静脉丛，位于每个侧软骨的两侧以及马蹄的敏感结构内
* 这些静脉受到跖垫对侧软骨的压迫，或蹄骨对蹄壁的压迫，起到泵的作用，将血液推向腿部上方
* 腿部静脉中的单向瓣膜防止血液回流到马蹄，而压迫产生的"液压缓冲"可以消散震荡并保护脆弱的蹄骨
* 当马蹄承重时，静脉被压缩并向上推送血液；当抬起时，静脉打开并通过动脉脉搏和重力重新充盈——这个循环常被称为马的"第二心脏"

**[Read Original / 阅读原文](https://horses.extension.org/blood-pumping-mechanism-of-the-hoof/)**

### SmallCode - AI Coding Agent Optimized for Small Local LLMs

* **What it does**: A terminal-native AI coding agent specifically designed to work with small local language models (8B-35B parameters) running on consumer hardware, enabling developers to use AI assistance without cloud dependencies or API costs.

* **Key features**: 
  - **Budget-aware architecture** with context management, forgiving tool-call parsing, and patch-based editing optimized for small model limitations
  - **MarrowScript cognition layer** providing prompt caching, structured traces, tier-based routing, and automatic validation/repair
  - **BoneScript integration** for Node.js/TypeScript projects, compiling single `.bone` files into complete backends
  - **Model escalation** with optional fallback to cloud models (Claude, GPT-5, DeepSeek) on hard failures
  - **TODO-driven planning** that decomposes complex tasks into atomic steps with validation
  - **Persistent shell sessions** and working memory that survives across turns
  - **18 built-in tools** with 2-stage routing to reduce context overhead

* **Why it's notable**: Achieves 87% benchmark performance with 4B-active models by compensating for small model limitations through intelligent architecture rather than requiring frontier models. Offers complete privacy with fully local operation, no network calls needed. Provides prebuilt binaries for all platforms with zero build dependencies. Represents a practical approach to making AI coding assistance accessible on consumer hardware without cloud costs.

---

### SmallCode - 专为小型本地大语言模型优化的 AI 编码代理

* **功能介绍**: 一个专为在消费级硬件上运行的小型本地语言模型(8B-35B 参数)设计的终端原生 AI 编码代理,让开发者无需依赖云服务或支付 API 费用即可使用 AI 辅助编程。

* **主要特点**:
  - **预算感知架构**,包含上下文管理、容错工具调用解析和针对小模型限制优化的补丁式编辑
  - **MarrowScript 认知层**提供提示词缓存、结构化追踪、分层路由和自动验证/修复
  - **BoneScript 集成**用于 Node.js/TypeScript 项目,将单个 `.bone` 文件编译为完整后端
  - **模型升级机制**,在严重失败时可选择回退到云模型(Claude、GPT-5、DeepSeek)
  - **TODO 驱动规划**将复杂任务分解为带验证的原子步骤
  - **持久化 Shell 会话**和跨轮次保留的工作内存
  - **18 个内置工具**,采用两阶段路由减少上下文开销

* **为何值得关注**: 通过智能架构补偿小模型的局限性,而非依赖前沿模型,在 4B 激活参数模型上实现了 87% 的基准性能。提供完全本地化操作,无需网络调用,保证完全隐私。为所有平台提供预编译二进制文件,零构建依赖。代表了一种实用方法,使 AI 编码辅助在消费级硬件上无需云成本即可实现。

**[View Repository / 查看仓库](https://github.com/Doorman11991/smallcode)**

### Agent-Learning-Hub - Curated AI Agent Learning Roadmap and Resource Collection

* **What it does**: Provides a structured, actionable learning path for building production-ready AI agents, moving beyond simple chatbots to real-world agent systems with tool use, memory, evaluation, and safety guardrails.

* **Key features**: 
  - Stage-by-stage todo list from basic agent loops to production harnesses
  - Project ladder with 11 hands-on projects of increasing complexity
  - Curated resources prioritizing official docs, modern agent systems (Claude Code, OpenClaw, Hermes), and protocols (MCP, A2A, ACP)
  - Focus on practical engineering: skills, evaluation, observability, browser agents, and safety
  - Emphasis on modern approaches over outdated role-play frameworks

* **Why it's notable**: Cuts through the noise of scattered agent tutorials by providing a clear, opinionated learning path focused on what actually matters in 2024-2026—coding agents, agent harnesses, skills/protocols, and production readiness. Maintained by Datawhale community with 1,098 stars, it's particularly valuable for Chinese-speaking developers wanting to build useful agents rather than collect random links.

---

### Agent-Learning-Hub - AI 智能体学习路线与资源库

* **功能介绍**: 提供结构化、可执行的 AI Agent 学习路径,帮助开发者构建生产级智能体系统,从基础对话机器人进阶到具备工具调用、记忆管理、评测和安全机制的真实应用。

* **主要特点**:
  - 分阶段学习清单,从最小 agent 循环到生产级 harness
  - 11 个难度递进的实战项目梯度
  - 精选资源优先官方文档、现代智能体系统(Claude Code、OpenClaw、Hermes)和协议标准(MCP、A2A、ACP)
  - 聚焦实用工程能力:技能封装、评测体系、可观测性、浏览器智能体和安全边界
  - 强调现代方法论,避开过时的角色扮演框架

* **为何值得关注**: 在碎片化的 Agent 教程中提供清晰、有主见的学习路径,聚焦 2024-2026 年真正重要的方向——代码智能体、agent harness 工程、技能协议和生产化部署。由 Datawhale 社区维护,获 1,098 星标,特别适合想构建实用智能体而非收集链接的中文开发者。

**[View Repository / 查看仓库](https://github.com/datawhalechina/Agent-Learning-Hub)**

### 🎬 When Claude Handles Your Project

**Channel:** Sheryians Coding School

* What the video covers: A short demonstration of Claude AI managing development projects, likely showcasing its coding capabilities and project handling features
* Key topics discussed: Claude AI's practical application in software development workflows, automated project management, AI-assisted coding
* Why it's worth watching: Quick insight into how AI tools like Claude can streamline development work, relevant for developers exploring AI-powered coding assistants

---

### 🎬 当 Claude 接管你的项目

**频道:** Sheryians Coding School

* 视频内容概述: 简短演示 Claude AI 如何管理开发项目,展示其编码能力和项目处理功能
* 主要话题: Claude AI 在软件开发工作流程中的实际应用、自动化项目管理、AI 辅助编码
* 为何值得观看: 快速了解 Claude 等 AI 工具如何简化开发工作,适合探索 AI 编程助手的开发者观看

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=QGNw9QZHsAA)**

### 🎬 The PAPER Power !! #coding #shorts #programming
**Channel:** 𝗔𝘇𝗶𝘇 𝗖𝗼𝗱𝗲𝘅

* A creative coding demonstration showcasing the visual power and possibilities of programming
* Likely features animation techniques, visual effects, or creative coding concepts using paper-themed elements
* Worth watching for developers interested in creative coding, web animations, and visual programming techniques—perfect bite-sized inspiration in short format

---

### 🎬 纸的力量！！#编程 #短视频 #程序设计
**频道:** 𝗔𝘇𝗶𝘇 𝗖𝗼𝗱𝗲𝘇

* 展示编程视觉效果和创意可能性的创意编程演示
* 可能包含动画技术、视觉特效或以纸张为主题的创意编程概念
* 适合对创意编程、网页动画和视觉编程技术感兴趣的开发者观看——短视频格式提供快速灵感

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=omfU5ra_rcI)**

### sp.h is the standard library that C deserves

* **sp.h is a 15,000-line single-header C99 library** that reimagines C's standard library by programming directly against syscalls instead of wrapping libc
* **Eliminates libc dependencies** where possible, arguing that libc is actively harmful for modern programming needs, especially asynchronous IO
* **Introduces explicit memory management** through custom allocators (`sp_allocator_t`), rejecting the fiction of unlimited heap allocation
* **Replaces null-terminated strings** with `sp_str_t` (pointer + length), enabling O(1) length checks, safe substrings, and eliminating buffer overflow vulnerabilities
* **Achieves both ergonomics and performance** by allowing zero-copy string operations while maintaining readable, high-level code patterns
* **Designed for portability and transparency** - works across Linux, Windows, macOS, WASM, and various compilers (MSVC, MinGW, TCC) with only ~40 platform-specific syscalls
* **Meant to be modified** - ships as a single organized file with namespace conventions and searchable tags for easy customization
* **Provides modern data structures** including hash tables and dynamic arrays that work seamlessly with the string type system

### sp.h 是 C 语言应得的标准库

* **sp.h 是一个 15,000 行的单头文件 C99 库**,通过直接调用系统调用而非封装 libc 来重新构想 C 的标准库
* **尽可能消除 libc 依赖**,认为 libc 对现代编程需求(尤其是异步 IO)是有害的
* **引入显式内存管理**,通过自定义分配器(`sp_allocator_t`)拒绝无限堆分配的虚构概念
* **用 `sp_str_t`(指针+长度)替代空终止字符串**,实现 O(1) 长度检查、安全子串操作,并消除缓冲区溢出漏洞
* **同时实现人体工程学和性能**,允许零拷贝字符串操作,同时保持可读的高级代码模式
* **为可移植性和透明度而设计** - 可在 Linux、Windows、macOS、WASM 和各种编译器(MSVC、MinGW、TCC)上运行,仅需约 40 个平台特定的系统调用
* **设计为可修改** - 作为单个有组织的文件发布,具有命名空间约定和可搜索标签,便于自定义
* **提供现代数据结构**,包括与字符串类型系统无缝协作的哈希表和动态数组

**[Read Original / 阅读原文](https://spader.zone/sp/)**

<!-- [Title-Only] -->
### Neutron scattering explains why gluten-free pasta falls apart (2025)

* Based on the title, this article likely explores the scientific research using neutron scattering techniques to understand the structural differences between traditional and gluten-free pasta at a molecular level, explaining why gluten-free varieties tend to have inferior texture and structural integrity during cooking
* Why it might be interesting: This represents a fascinating intersection of physics, food science, and practical cooking. Understanding the molecular mechanisms behind pasta structure could lead to better gluten-free alternatives, and it showcases how advanced scientific instruments (neutron scattering) can solve everyday culinary problems. For readers interested in food science, materials science, or gluten-free cooking, this offers insights into why gluten-free pasta behaves differently and what might be done to improve it.

### 中子散射解释了无麸质意大利面为何容易散开 (2025)

* 根据标题推测，这篇文章可能探讨了科学家如何利用中子散射技术，从分子层面研究传统意大利面和无麸质意大利面的结构差异，解释为什么无麸质品种在烹饪过程中质地和结构完整性较差
* 为何值得关注：这是物理学、食品科学和实际烹饪的迷人交叉领域。理解意大利面结构背后的分子机制可能有助于开发更好的无麸质替代品，同时展示了先进的科学仪器（中子散射）如何解决日常烹饪问题。对于关注食品科学、材料科学或无麸质饮食的读者来说，这提供了关于无麸质意大利面为何表现不同以及如何改进的见解。

**[Read Original / 阅读原文](https://phys.org/news/2025-09-science-spaghetti-neutron-gluten-free.html)**

### What is the history of the ERROR_ARENA_TRASHED error code?

* **ERROR_ARENA_TRASHED (error code 7)** is a legacy error inherited from MS-DOS, named after corrupted memory management structures called "arenas"
* MS-DOS tracked memory using 16-byte blocks with signatures: **0x4D ('M')** for valid blocks and **0x5A ('Z')** for the last block—the initials of Mark Zbikowski
* The error triggered when MS-DOS detected invalid signatures during memory allocation, indicating corrupted memory structures
* **Not used by Win32 kernel**, making it useful for mocking error conditions in testing since genuine system errors won't produce it
* Many websites claiming to "fix" this error provide vague, generic troubleshooting advice despite the error being obsolete in modern Windows
* The slang term "trashed" reflects Microsoft's informal developer culture in the MS-DOS era

### ERROR_ARENA_TRASHED 错误代码的历史

* **ERROR_ARENA_TRASHED（错误代码 7）** 是从 MS-DOS 继承的遗留错误，因内存管理结构"arena"损坏而得名
* MS-DOS 使用 16 字节的内存块追踪内存，带有签名：**0x4D ('M')** 表示有效块，**0x5A ('Z')** 表示最后一个块——这是 Mark Zbikowski 的首字母缩写
* 当 MS-DOS 在内存分配期间检测到无效签名时触发此错误，表示内存结构已损坏
* **Win32 内核不使用此错误**，因此适合在测试中模拟错误条件，因为真实的系统错误不会产生它
* 许多声称能"修复"此错误的网站提供模糊、通用的故障排除建议，尽管该错误在现代 Windows 中已过时
* 俚语"trashed"反映了 MS-DOS 时代微软开发者的非正式文化

**[Read Original / 阅读原文](https://devblogs.microsoft.com/oldnewthing/20260519-00/?p=112339)**

### HRM-Text - Efficient 1B Text Generation Model with $1000 Pretraining Budget

* **What it does**: A 1B parameter text generation model that can be pretrained from scratch for approximately $1000, using 130-600x less compute and 150-900x less data than traditional approaches. Built on a hierarchical recurrent architecture (HRM) with task completion and latent space reasoning capabilities.

* **Key features**: 
  - Two model sizes: L (0.6B, 8 H100s, ~$800) and XL (1B, 16 H100s, ~$1472)
  - Strong benchmark performance (XL: 84.7% GSM8k, 56.5% MATH, 82.3% DROP, 60.7% MMLU)
  - Complete pretraining framework with PrefixLM sequence packing, FlashAttention 3, PyTorch FSDP2
  - Includes evaluation suite, checkpoint conversion, and fine-tuning (SFT) support
  - Docker environment with full toolchain for reproducible training

* **Why it's notable**: Democratizes foundation model pretraining by making it accessible at consumer-friendly budgets while achieving competitive performance. Provides a complete, production-ready pipeline from data preparation through evaluation and export to Hugging Face format. The dramatic reduction in compute requirements (up to 600x) and data needs (up to 900x) represents a significant breakthrough for researchers and organizations with limited resources.

---

### HRM-Text - 千元预算训练的高效 10 亿参数文本生成模型

* **功能介绍**: 一个可以用约 1000 美元从零开始预训练的 10 亿参数文本生成模型,基于分层递归架构(HRM),通过任务完成和潜在空间推理增强。相比传统方法减少 130-600 倍计算量和 150-900 倍数据需求。

* **主要特点**:
  - 两种模型规格:L 版(6 亿参数,8 张 H100,约 800 美元)和 XL 版(10 亿参数,16 张 H100,约 1472 美元)
  - 强劲的基准测试表现(XL 版:GSM8k 84.7%、MATH 56.5%、DROP 82.3%、MMLU 60.7%)
  - 完整的预训练框架,包含 PrefixLM 序列打包、FlashAttention 3、PyTorch FSDP2
  - 提供评估套件、检查点转换和监督微调(SFT)支持
  - Docker 环境配套完整工具链,确保训练可复现

* **为何值得关注**: 通过将基础模型预训练成本降至消费级预算,同时保持竞争力性能,实现了 AI 民主化。提供从数据准备到评估、导出 Hugging Face 格式的完整生产级流程。计算需求降低高达 600 倍、数据需求降低高达 900 倍,对资源有限的研究人员和组织来说是重大突破。

**[View Repository / 查看仓库](https://github.com/sapientinc/HRM-Text)**

### Rubish: A UNIX Shell Written in Pure Ruby

* **Full Bash compatibility** — Run existing bash scripts without modification; any incompatibility is considered a bug
* **Deep Ruby integration** — Seamlessly mix shell commands with Ruby code, blocks, iterators, and libraries
* **Ruby-enhanced syntax** — Use Ruby expressions as conditions (`if { count.to_i > 3 }`), method call style (`ls('-la')`), and method chaining (`ls().sort.uniq`)
* **Inline Ruby evaluation** — Lines starting with capital letters execute as Ruby code directly (`Time.now`, `Dir.glob('*.rb')`)
* **Ruby-style functions** — Define shell functions with `def...end` syntax, named parameters, and splat args
* **Custom Ruby prompts** — Define `rubish_prompt` and `rubish_right_prompt` as Ruby functions for dynamic, programmatic prompts
* **Lazy loading** — Defer slow initializations (rbenv, nvm, pyenv) to background threads for instant shell startup
* **Zsh compatibility** — Supports `setopt`/`unsetopt`, `compdef`, `autoload`, `%X` prompt codes, and abbreviated path expansion
* **Embeddable API** — Drive rubish sessions in-process from other Ruby programs with tokenization, parsing, completion, and prompt rendering APIs
* **Restricted mode** — Run untrusted scripts safely with `-r` flag, disabling all Ruby integration features
* **Comprehensive builtins** — Includes all standard shell builtins for directory navigation, I/O, variables, process control, job control, and more

---

### Rubish：用纯 Ruby 编写的 UNIX Shell

* **完全兼容 Bash** — 无需修改即可运行现有 bash 脚本；任何不兼容问题都被视为 bug
* **深度 Ruby 集成** — 无缝混合 shell 命令与 Ruby 代码、块、迭代器和库
* **Ruby 增强语法** — 使用 Ruby 表达式作为条件（`if { count.to_i > 3 }`）、方法调用风格（`ls('-la')`）和方法链（`ls().sort.uniq`）
* **内联 Ruby 求值** — 以大写字母开头的行直接作为 Ruby 代码执行（`Time.now`、`Dir.glob('*.rb')`）
* **Ruby 风格函数** — 使用 `def...end` 语法、命名参数和可变参数定义 shell 函数
* **自定义 Ruby 提示符** — 将 `rubish_prompt` 和 `rubish_right_prompt` 定义为 Ruby 函数，实现动态、可编程的提示符
* **延迟加载** — 将慢速初始化（rbenv、nvm、pyenv）推迟到后台线程，实现即时 shell 启动
* **Zsh 兼容性** — 支持 `setopt`/`unsetopt`、`compdef`、`autoload`、`%X` 提示符代码和缩写路径展开
* **可嵌入 API** — 通过分词、解析、补全和提示符渲染 API，从其他 Ruby 程序进程内驱动 rubish 会话
* **受限模式** — 使用 `-r` 标志安全运行不受信任的脚本，禁用所有 Ruby 集成功能
* **全面的内置命令** — 包含所有标准 shell 内置命令，用于目录导航、I/O、变量、进程控制、作业控制等

**[Read Original / 阅读原文](https://github.com/amatsuda/rubish)**

### The Quadratic Sandwich: Understanding Strong Convexity and L-Smoothness

* **Strong convexity** (μ > 0) ensures a function stays above its tangent plane plus a quadratic gap, guaranteeing minimum curvature μ in every direction and preventing flat valleys or plateaus
* **L-smoothness** bounds the gradient's Lipschitz constant, ensuring the gradient cannot change faster than L times the input change, which caps maximum curvature
* The **quadratic sandwich** traps well-behaved functions between two parabolas: a tighter lower bound (curvature μ) and a wider upper bound (curvature L)
* The **condition number** κ = L/μ measures optimization difficulty: κ ≈ 1 means nearly quadratic (easy), large κ means wildly varying curvature (gradient descent zigzags)
* When κ = 1 (μ = L), the function is exactly quadratic and gradient descent converges in one step
* **Without strong convexity** (μ = 0): gradient loses calibration, cannot gauge distance to minimum, condition number explodes to infinity, convergence degrades
* **Without L-smoothness**: gradient can spike unpredictably between steps, causing catastrophic overshoots even with previously safe step sizes (like kicking a ball from mud onto ice)

### 二次三明治：理解强凸性和L-光滑性

* **强凸性**（μ > 0）确保函数始终位于其切平面加上二次间隙之上，保证每个方向上的最小曲率为μ，防止出现平坦的山谷或高原
* **L-光滑性**限制梯度的Lipschitz常数，确保梯度变化速度不超过输入变化的L倍，从而限制最大曲率
* **二次三明治**将良好函数夹在两个抛物线之间：更紧的下界（曲率μ）和更宽的上界（曲率L）
* **条件数** κ = L/μ衡量优化难度：κ ≈ 1表示近似二次函数（容易优化），大κ表示曲率变化剧烈（梯度下降会之字形震荡）
* 当κ = 1（即μ = L）时，函数恰好是二次函数，梯度下降一步收敛
* **缺少强凸性**（μ = 0）：梯度失去校准能力，无法判断与最小值的距离，条件数爆炸至无穷，收敛性能退化
* **缺少L-光滑性**：梯度可能在步骤间不可预测地激增，即使使用之前安全的步长也会导致灾难性的过冲（就像从泥地踢球突然到了冰面上）

**[Read Original / 阅读原文](https://fedemagnani.github.io/math/2026/04/08/the-quadratic-sandwich.html)**

### Microsoft Cancels Claude Code Licenses, Pushes Developers to GitHub Copilot CLI

* Microsoft is canceling most Claude Code licenses by June 30th, 2026, despite the tool's popularity among its developers over the past six months
* The company is transitioning developers to GitHub Copilot CLI, its own command-line AI coding tool, citing both strategic alignment and financial considerations at fiscal year-end
* Claude Code had become surprisingly popular, even among non-engineers like designers and project managers, and was preferred over GitHub Copilot CLI by many Microsoft developers
* Microsoft's Experiences + Devices team (Windows, Microsoft 365, Outlook, Teams, Surface) is leading the transition, with the cutoff aligned to the end of the current financial year
* Anthropic's Claude models will remain accessible through Copilot CLI and continue to be used in Microsoft 365 apps where they outperform OpenAI models at certain tasks
* The move puts pressure on GitHub's team to rapidly improve Copilot CLI to match or exceed Claude Code's capabilities and win back internal developer adoption
* Microsoft had previously reported 91% of engineering teams using GitHub Copilot, but Claude Code's introduction impacted that adoption rate
* The company had considered acquiring Cursor to close the gap but is now exploring other AI startup partnerships to avoid regulatory scrutiny

### 微软开始取消 Claude Code 许可证，推动开发者转向 GitHub Copilot CLI

* 尽管 Claude Code 在过去六个月内深受微软开发者欢迎，微软仍计划在 2026 年 6 月 30 日前取消大部分 Claude Code 许可证
* 公司正将开发者转向其自有的命令行 AI 编码工具 GitHub Copilot CLI，理由包括战略统一和财年末的财务考量
* Claude Code 意外受到欢迎，甚至设计师和项目经理等非工程师也在使用，许多微软开发者更青睐它而非 GitHub Copilot CLI
* 微软体验与设备团队（负责 Windows、Microsoft 365、Outlook、Teams、Surface）正主导这一转型，截止日期与当前财年结束时间一致
* Anthropic 的 Claude 模型将继续通过 Copilot CLI 提供访问，并在 Microsoft 365 应用中继续使用，因其在某些任务上优于 OpenAI 模型
* 此举给 GitHub 团队带来压力，需要快速改进 Copilot CLI 以匹配或超越 Claude Code 的能力，重新赢得内部开发者的采用
* 微软此前报告称 91% 的工程团队使用 GitHub Copilot，但 Claude Code 的引入影响了该采用率
* 公司曾考虑收购 Cursor 以缩小差距，但现在正探索其他 AI 初创公司合作伙伴关系以避免监管审查

**[Read Original / 阅读原文](https://www.theverge.com/tech/930447/microsoft-claude-code-discontinued-notepad)**

### 🎬 The PAPER Power !! #coding #shorts #programming

**Channel:** 𝗔𝘇𝗶𝘇 𝗖𝗼𝗱𝗲𝘇

* A creative coding demonstration showcasing the visual power and possibilities of paper-themed animations or effects in programming
* Likely features web development techniques, CSS animations, or creative coding concepts that bring paper-like interactions to life
* Worth watching for developers interested in creative coding, visual effects, and learning how to build engaging animations with code in a quick, digestible short format

---

### 🎬 纸的力量!! #编程 #短视频 #程序设计

**频道:** 𝗔𝘇𝗶𝘇 𝗖𝗼𝗱𝗲𝘅

* 展示以纸张为主题的创意编程动画效果,演示代码的视觉表现力
* 可能涉及网页开发技术、CSS 动画或创意编程概念,实现逼真的纸张交互效果
* 适合对创意编程、视觉特效感兴趣的开发者观看,通过短视频快速学习如何用代码构建引人入胜的动画效果

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=omfU5ra_rcI)**

