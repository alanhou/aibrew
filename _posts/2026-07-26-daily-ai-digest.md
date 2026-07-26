### Romanian F-16 Neutralizes Violating UAV

* An F-16 fighter aircraft from the 86th Air Base in Fetești, Romania, intercepted a UAV that violated national airspace during an air policing mission.
* On July 24th, the aircraft used an air-to-air missile to neutralize the UAV over an unpopulated area near Padina, Buzău County.

### 罗马尼亚F-16战斗机击落侵犯无人机

* 一架来自费特什蒂第86航空基地的F-16战斗机，在空中警戒任务中拦截了一架侵犯国家领空的无人机。
* 7月24日，该战斗机在布泽乌县帕迪纳附近的无人区域，使用空对空导弹击中并摧毁了该无人机。

**[Read Original / 阅读原文](https://english.mapn.ro/)**

### Ruff v0.16.0 Release Announcement
* Ruff v0.16.0 has been released and is available via PyPI or package managers like `uv`.
* Ruff is an extremely fast Python linter and formatter written in Rust, designed to replace tools like Black, Flake8, and isort with superior speed.

### Key Changes & Migration
* This version includes some breaking changes, with the most significant being an updated default rule set.
* The default rule set now enables 413 rules, up from 59 in previous versions, to catch more severe issues like syntax errors and runtime errors out-of-the-box.
* Users who wish to revert to the old defaults can do so by selecting specific rule codes in their configuration.

### New Features
* Ruff can now format Python code blocks embedded in Markdown files (with info strings like `python`, `py`, `pyi`, etc.) and Quarto notebooks.
* New suppression comment formats have been added: `ruff: ignore` (for single or logical lines) and `ruff: file-ignore` (for entire files), offering more flexible control over diagnostics.

### Ruff v0.16.0发布公告
* Ruff v0.16.0现已发布，可通过PyPI或`uv`等包管理器安装。
* Ruff是一个用Rust编写的极快Python代码检查与格式化工具，旨在以远超同类工具（如Black、Flake8、isort）的速度替代它们。

### 关键变更与迁移
* 本次版本包含少量破坏性变更，其中最主要的是更新了默认规则集。
* 默认规则集现在包含413条规则（之前版本为59条），旨在开箱即用地捕获更多严重问题，如语法错误和运行时错误。
* 希望恢复旧默认规则集的用户，可以在配置中通过选择特定规则代码来实现。

### 新功能
* Ruff现在可以格式化嵌入在Markdown文件（使用`python`、`py`、`pyi`等信息字符串）和Quarto笔记本中的Python代码块。
* 新增了抑制注释格式：`ruff: ignore`（用于单行或逻辑行）和`ruff: file-ignore`（用于整个文件），为控制诊断信息提供了更灵活的选择。

**[Read Original / 阅读原文](https://astral.sh/blog/ruff-v0.16.0)**

### GrapheneOS: Comprehensive Data Protection Mechanisms
*   **Foundation on Secure Hardware**: GrapheneOS heavily leverages Android's security features and requires Pixel hardware (with plans to expand via Motorola in 2027) which provides essential hardware security features and updates.
*   **Robust Disk Encryption**: Data is protected by strong disk encryption that cannot be directly broken; attacks must either exploit the OS or brute-force the credential.
*   **Advanced Rate Limiting**: Implements strict, hardware-backed rate limiting for unlock attempts (e.g., 4-hour delay after 10 failures, 41-day delay after 15) with only 20 total attempts allowed.
*   **Insider Attack Resistance**: The secure element requires owner authentication before firmware updates, preventing government-coerced removal of rate limits.
*   **Enhanced Password & PIN Security**: Raises password character limit to 128, allowing high-entropy diceware passphrases. Introduces an optional 2nd-factor fingerprint PIN to balance convenience and security.
*   **Hardened Exploit Protections**: Significantly improves OS security with hardened memory allocators and hardware-based features like Memory Tagging Extension (MTE) to prevent exploits.
*   **Physical Access Defenses**: Blocks new USB connections by default when locked and disables USB data when idle, mitigating physical extraction attacks.
*   **Auto-Reboot to Secure State**: Features a configurable auto-reboot timer (default 18 hours) that returns the device to the encrypted "Before First Unlock" state, clearing RAM and blocking updates.
*   **Per-User Encryption Keys**: Supports resetting secondary user and Private Space profiles to the "Before First Unlock" state without a full reboot.
*   **Duress PIN/Password**: An optional feature that wipes the device if a special duress credential is entered during any authentication prompt, providing a last-resort data destruction method.

### GrapheneOS：全面的数据保护机制
*   **基于安全硬件构建**：GrapheneOS 深度利用 Android 的安全特性，并依赖 Pixel 硬件（计划于 2027 年通过与摩托罗拉合作扩展），该硬件提供必要的安全特性与更新支持。
*   **强磁盘加密**：数据受到强力磁盘加密保护，无法被直接破解；攻击者必须利用操作系统漏洞或暴力破解密码。
*   **高级速率限制**：实施严格的、基于硬件的登录尝试速率限制（例如，10次失败后延迟4小时，15次失败后延迟41天），总共只允许20次尝试。
*   **内部攻击防护**：安全元件要求所有者进行身份验证后才能更新固件，防止政府胁迫移除速率限制。
*   **增强的密码与PIN安全**：将密码字符上限提高至128位，支持使用高熵的diceware密码短语。引入可选的第二因素指纹PIN码，在便利性与安全性之间取得平衡。
*   **强化漏洞利用防护**：通过硬化内存分配器和硬件级特性（如内存标记扩展-MTE）大幅提升操作系统安全性，抵御漏洞利用攻击。
*   **物理访问防护**：默认在锁定时阻止新的USB连接，并在无活动连接时禁用USB数据，以减轻物理提取攻击风险。
*   **自动重启至安全状态**：提供可配置的自动重启计时器（默认18小时），将设备恢复到加密的“首次解锁前”状态，清空RAM并阻止固件更新。
*   **独立用户加密密钥**：支持在无需完全重启的情况下，将辅助用户和隐私空间配置重置回“首次解锁前”状态。
*   **胁迫PIN码/密码**：一项可选功能，当在任何身份验证提示中输入特殊胁迫凭证时会擦除设备，提供最后的数据销毁手段。

**[Read Original / 阅读原文](https://discuss.grapheneos.org/d/40700-grapheneos-protections-against-data-extraction-from-locked-devices)**


## 🔥 GitHub Trending / GitHub 热门项目

### bitchat - Decentralized Peer-to-Peer Chat with Bluetooth Mesh & Nostr
*   **What it does**: A privacy-focused messaging app that operates on a dual-transport architecture. It enables local, offline communication via a Bluetooth mesh network and global, internet-based chat through the Nostr protocol, all without requiring accounts, phone numbers, or central servers.
*   **Key features**:
    *   **Dual Transport**: Automatic fallback from local Bluetooth mesh to global Nostr relays.
    *   **Location-Based Channels**: Geographic chat rooms defined by geohash precision over Nostr.
    *   **Privacy & Security**: End-to-end encryption using Noise Protocol for mesh and custom envelopes for Nostr. Features no persistent identifiers and an emergency data wipe.
    *   **IRC-Style Interface**: Familiar command system (`/slap`, `/msg`, `/who`).
    *   **Cross-Platform**: Native iOS and macOS application.
*   **Why it's notable**: Its innovative hybrid architecture solves a key gap between truly offline, resilient mesh communication and globally connected chat. The strong emphasis on user privacy, combined with the "IRC vibes" and immediate popularity (1,198 stars in a day), makes it a significant and trending project in the decentralized tech space.

### bitchat - 去中心化点对点聊天应用：结合蓝牙Mesh与Nostr协议
*   **功能介绍**：一款注重隐私的消息应用，采用双传输架构。它通过蓝牙Mesh网络支持本地离线通信，并通过Nostr协议实现全球互联网聊天，全程无需账户、手机号或中央服务器。
*   **主要特点**：
    *   **双传输架构**：智能地在本地蓝牙Mesh和全球Nostr中继之间切换。
    *   **基于位置的频道**：在Nostr上创建基于地理哈希（geohash）精度的地理聊天室。
    *   **隐私与安全**：使用Noise协议进行Mesh端到端加密，对Nostr使用专属加密信封。无持久标识符，并支持紧急数据擦除。
    *   **IRC风格界面**：熟悉的命令系统（`/slap`、`/msg`、`/who`）。
    *   **跨平台支持**：原生iOS和macOS应用。
*   **为何值得关注**：其创新的混合架构在真正的离线弹性Mesh通信和全球连接的聊天之间架起了桥梁。对用户隐私的强烈关注，结合其“IRC韵味”和爆发式增长的人气（单日获1,198颗星），使其成为去中心化技术领域一个重要且备受瞩目的项目。

**[View Repository / 查看仓库](https://github.com/permissionlesstech/bitchat)**

### ego-lite - The fastest browser for AI agents to run web automation
*   **What it does:** ego-lite is a standalone browser designed for humans and AI agents (like Codex, Claude Code) to work in parallel. It allows you to share your logged-in browser session with your agents for web automation tasks without conflict.
*   **Key features:**
    *   **Parallel Workspaces:** Each agent gets its own isolated "Space" within the same browser instance, preventing interference with your tabs or other agents.
    *   **Zero-Friction Login Sharing:** Agents inherit your real Chrome logins, cookies, and extensions directly.
    *   **Code-Based, Not CLI:** Exposes browser functions as JavaScript tools for agents to call directly, making complex tasks up to 2.5× faster with fewer tokens than command-line approaches.
    *   **High-Quality Page Snapshots:** Uses kernel-level customization to generate reliable, detailed page representations for AI understanding, handling complex iframes well.
    *   **Universal Compatibility:** The `ego-browser` skill connects any agent CLI (Codex, Claude, etc.) to drive the browser.
    *   **Built for the Browser:** Unlike automation frameworks (e.g., Browser-Use), ego-lite is the browser itself, eliminating login and session issues.
*   **Why it's notable:** ego-lite solves a core pain point in AI-assisted browsing: enabling true, non-disruptive collaboration between humans and agents. Its unique parallel workspace model, performance benchmarks showing significant speed/cost improvements, and zero-cost/zero-config approach make it a standout tool in the growing field of AI-native applications. The high star count (898 stars today) indicates strong initial community interest in this new category of "shared browser" for AI.

### ego-lite - 专为AI代理设计的极速网页自动化浏览器
*   **功能介绍：** ego-lite 是一款独立的浏览器，旨在让人类与AI代理（如Codex、Claude Code）能够并行工作。它允许您与代理共享已登录的浏览器会话来执行网页自动化任务，且过程互不干扰。
*   **主要特点：**
    *   **并行工作区：** 每个代理在同一个浏览器实例中拥有自己独立的“Space（空间）”，确保其任务不会干扰您的标签页或其他代理。
    *   **无摩擦登录共享：** 代理可以直接继承您真实的Chrome登录状态、Cookie和扩展程序。
    *   **代码驱动（非命令行）：** 将浏览器功能封装为JavaScript工具供代理直接调用，使得复杂任务的执行速度提升高达2.5倍，并消耗更少的Token。
    *   **高质量页面快照：** 利用内核级定制生成可靠且详细的页面表示，便于AI理解，能良好处理复杂iframe等情况。
    *   **通用兼容性：** 通过 `ego-browser` 技能，任何代理命令行工具（Codex, Claude 等）都可以控制该浏览器。
    *   **浏览器本体：** 与Browser-Use等自动化框架不同，ego-lite本身就是浏览器，从根本上解决了登录和会话管理问题。
*   **为何值得关注：** ego-lite 解决了AI辅助浏览中的一个核心痛点：实现人类与代理之间真正的、无干扰的协作。其独特的并行工作区模型、显示性能与成本显著改善的基准测试结果，以及零成本、零配置的启动方式，使其在日益增长的AI原生应用领域中脱颖而出。今日获得898颗星标也反映出社区对这款新型“共享AI浏览器”的强烈兴趣。

**[View Repository / 查看仓库](https://github.com/citrolabs/ego-lite)**

### block/buzz - A self-hostable workspace for human-AI collaboration
*   **What it does:** Buzz is a self-hostable communication platform (Nostr relay) where humans and AI agents share the same "rooms." It unifies team chat, code collaboration (git patches), AI agent interactions, workflows, and search into a single, auditable event log. Agents are treated as full team members with their own identities.
*   **Key features:** Channels, threads, DMs, canvases, media with frame-specific comments, search, audit logs, desktop app (Tauri), CLI for agents (`buzz-cli`), YAML-based workflows, and native Git event support (NIP-34).
*   **Why it's notable:** It creates a unified substrate for human and agent collaboration, eliminating the need for disconnected tools like chat, forges, bots, and CI dashboards. The core differentiator is its identity model: AI agents have their own keys and permissions, acting as "room members, not haunted cron jobs." This is a significant step towards practical, integrated human-agent workflows in a developer environment.

### block/buzz - 人类与AI智能体协作的自托管工作空间
*   **功能介绍：** Buzz 是一个自托管的通信平台（Nostr中继），让人类和AI智能体在同一个“房间”内协作。它将团队沟通、代码协作（Git补丁）、AI智能体交互、工作流和搜索统一到一个可审计的事件日志中。智能体被视为拥有独立身份的完整团队成员。
*   **主要特点：** 支持频道、线程、私信、画布、带帧级注释的媒体评论、搜索、审计日志、桌面应用（Tauri）、智能体专用命令行工具（`buzz-cli`）、基于YAML的工作流，以及原生的Git事件支持（NIP-34）。
*   **为何值得关注：** 它为人类与智能体协作创建了一个统一的基础设施，无需再依赖分散的聊天、代码托管、机器人、CI仪表盘等工具。其核心差异化在于身份模型：AI智能体拥有自己的密钥和权限，被视为“房间成员，而非游荡的定时任务”。这是在开发环境中实现实用的、一体化的人机协作的重要一步。

**[View Repository / 查看仓库](https://github.com/block/buzz)**


## 🚀 Fast-Moving Repos / 快速崛起项目

### OpenWorker - AI Desktop Assistant Delivering Finished Work
* **What it does**: An open-source AI coworker that lives on your desktop, automating everyday tasks to produce complete deliverables like polished documents, Slack replies, calendar updates, and triaged inboxes, rather than just providing chat responses.
* **Key features**:
    * **Local-first operation**: Runs on your machine with a privacy-centric model; data only leaves your device via the AI model and integrations you explicitly choose.
    * **Model agnostic**: Works with API keys for OpenAI, Anthropic, Google, and others, or runs fully local with Ollama.
    * **Tool integration**: Connects with 25+ apps (GitHub, Slack, Jira, Notion, Gmail) and your local terminal/files via the MCP protocol.
    * **Approval workflow**: Checks with you before executing consequential actions like sending messages or changing files.
    * **Automation**: Can run scheduled tasks for recurring work.
* **Why it's notable**: Developed by Andrew Ng's team, it stands out for its strong privacy focus, local execution, and practical approach to turning AI from a chatbot into a desktop agent that delivers actionable, finished work. Its open beta status and extensive model/tool support are key highlights.

### OpenWorker - 交付完整工作成果的AI桌面助手
* **功能介绍**：一款运行在桌面端的开源AI同事，能够自动化日常任务并产出完整的交付物，例如成文的文档、包含数据的Slack回复、更新的日历以及分类处理的收件箱，而不仅仅是对话。
* **主要特点**：
    * **本地优先**：在您的设备上运行，注重隐私；数据仅在您选择的模型和集成工具中才会离开设备。
    * **模型无关**：支持使用OpenAI、Anthropic、Google等提供商的API密钥，或通过Ollama完全本地运行。
    * **工具集成**：通过MCP协议，可连接25+款应用（GitHub, Slack, Jira, Notion, Gmail）以及您的本地终端和文件。
    * **审批流程**：在执行发送消息或更改文件等关键操作前，会先与您确认。
    * **自动化**：支持定时运行重复性任务。
*   **为何值得关注**：由吴恩达团队开发，其核心优势在于强大的隐私保护、本地运行能力以及将AI从聊天机器人转变为能交付实际成果的桌面智能体的实用理念。目前处于公开测试阶段，并支持广泛的模型和工具集成。

**[View Repository / 查看仓库](https://github.com/andrewyng/openworker)**

### esp32-ai - Running a 28.9M Parameter LLM on an $8 Microcontroller
* **What it does:** This project demonstrates running a 28.9 million parameter language model (LLM) directly on an ESP32-S3 microcontroller, costing about $8. It generates short, coherent stories locally on the device without any cloud connectivity, writing the output to a small screen.
* **Key features:** The breakthrough is achieved by using **Per-Layer Embeddings** (from Google's Gemma models) to store most of the model's parameters (25M) in the chip's slow flash memory instead of its fast SRAM. This allows a model ~100x larger than previous on-chip models to run, achieving ~9.5 tokens per second. The firmware, wiring instructions, and training code are all provided.
* **Why it's notable:** It represents a significant architectural advancement in edge AI. It proves that a model of meaningful size (28.9M parameters) can run on an extremely low-cost, resource-constrained microcontroller by innovatively leveraging memory hierarchy. This opens new possibilities for offline, private, and low-power AI applications in embedded systems.

### esp32-ai - 在8美元微控制器上运行2890万参数大语言模型
* **功能介绍：** 本项目展示了在仅约8美元的ESP32-S3微控制器上直接运行一个2.89亿参数语言模型的能力。模型能在设备本地生成连贯的短故事，无需任何云端连接，结果直接输出到连接的小屏幕上。
* **主要特点：** 核心突破在于采用了 **Per-Layer Embeddings** 技术（源自Google的Gemma模型），将模型的大部分参数（2500万）存储在芯片的慢速闪存中，而非快速SRAM。这使得在芯片上运行的模型大小比之前提升了约100倍，并达到了约9.5个令牌/秒的生成速度。项目提供了完整的固件、接线说明和训练代码。
* **为何值得关注：** 这是边缘人工智能领域的一项重要架构进步。它证明通过创新性地利用内存层次结构，一个具有实际意义的模型（2890万参数）可以在极低成本、资源受限的微控制器上运行。这为在嵌入式系统中实现离线、隐私保护且低功耗的AI应用开辟了新的可能性。

**[View Repository / 查看仓库](https://github.com/slvDev/esp32-ai)**


## 🎬 YouTube Tech Videos / YouTube 技术视频

### 🎬 Anthropic’s first technical PM on token maxing, the jagged edge, and living in the future
**Channel:** Lenny's Podcast
*   **What the video covers:** An in-depth interview with Dianne Penn, Anthropic's first technical product manager, exploring her role in shaping AI products at the cutting edge of research.
*   **Key topics discussed:** The concept of "token maxing" (optimizing for AI model context windows), the "jagged edge" of AI capabilities (the uneven, unpredictable frontier of model performance), and the philosophical and practical implications of "living in the future" with rapidly advancing AI.
*   **Why it's worth watching:** It offers a unique insider's perspective from a key product leader at one of the world's most influential AI labs. The conversation delves into both highly technical and forward-looking aspects of AI product development, providing valuable insights for builders, strategists, and anyone interested in the trajectory of AI technology.

### 🎬 Anthropic的首任技术产品经理谈：Token最大化、锯齿边缘与活在未来
**频道:** Lenny's Podcast
*   **视频内容概述:** 本期视频专访了Anthropic的首任技术产品经理戴安·佩恩（Dianne Penn），深入探讨她在这家前沿AI实验室中塑造AI产品扮演的角色与思考。
*   **主要话题:** 讨论了“Token最大化”（优化AI模型的上下文窗口）、“锯齿边缘”（AI能力的前沿地带呈现出的不规则、不可预测性）以及“活在未来”的理念——即如何在AI技术快速发展的背景下进行思考和实践。
*   **为何值得观看:** 这是一次来自全球最具影响力AI实验室之一的核心产品领导者的独家视角。对话深入技术细节与前沿思考，为开发者、决策者以及所有关注AI技术走向的人士提供了宝贵见解。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=tivaWTTVRhY)**

### 🎬 How Close Can You Orbit a Black Hole? - Adam Brown
**Channel:** Dwarkesh Patel
*   This video features a discussion with astrophysicist Adam Brown on the extreme physics and engineering challenges of orbiting a black hole. It explores the final stable orbits before certain doom.
*   Key topics include the event horizon, the innermost stable circular orbit (ISCO), gravitational forces, time dilation, and the theoretical feasibility of such a mission.
*   It's worth watching for a fascinating, deep-dive into relativistic astrophysics presented in an accessible dialogue format, making complex concepts engaging.

### 🎬 你能离黑洞的轨道有多近？ - Adam Brown
**频道:** Dwarkesh Patel
*   该视频是与天体物理学家 Adam Brown 的对谈，探讨围绕黑洞运行所涉及的极端物理学和工程挑战，研究在注定毁灭前最后的稳定轨道。
*   主要话题包括事件视界、最内稳定圆轨道（ISCO）、引力、时间膨胀以及此类任务的理论可行性。
*   值得观看的原因在于，它以通俗易懂的对话形式，深入浅出地讲解了复杂的相对论天体物理学概念，引人入胜。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=Gpf4WvQ9uxQ)**

### 🎬 What Actually Makes A Startup Durable
**Channel:** Y Combinator
*   A Q&A session from Startup School Paris where YC partners answer audience questions on the core principles for building a lasting startup.
*   Key topics include founder operating models, critical decisions in scaling, maintaining focus, and the mindset required to weather long-term challenges.
*   Worth watching for its direct, unfiltered advice from experienced investors on the practical, day-to-day choices that separate durable companies from the rest.

### 🎬 什么真正让一家初创公司持久？
**频道:** Y Combinator
*   一场来自Startup School Paris的问答环节，YC合伙人回答了观众关于建立一家持久初创公司核心原则的提问。
*   主要话题涵盖创始人的运营模式、扩展过程中的关键决策、保持专注力，以及应对长期挑战所需的心态。
*   值得观看的原因是，它提供了经验丰富的投资人关于日常实践选择的直接、未经过滤的建议，这些选择区分了持久的公司与其他公司。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=99sPd15j3Zc)**

### 🎬 Session Hijacking Explained 🔐 | How Browser Sessions Work (Cybersecurity Awareness)
**Channel:** ezCommit
*   What the video covers: A technical deep dive into the mechanism of web browser sessions (cookies, tokens) and the methods attackers use for session hijacking, such as packet sniffing, cross-site scripting (XSS), and sidejacking.
*   Key topics discussed: Session creation and management, vulnerabilities in HTTP (non-secure) connections, demonstration of hijacking techniques, and defensive best practices for users and developers.
*   Why it's worth watching: It provides clear, foundational cybersecurity awareness. Understanding session hijacking is crucial for anyone using the internet, as it explains how login sessions can be stolen and how to protect them, especially when using public Wi-Fi.

### 🎬 会话劫持详解 🔐 | 浏览器会话如何工作（网络安全意识）
**频道:** ezCommit
*   视频内容概述：深入讲解浏览器会话的技术机制（如Cookie、令牌）以及攻击者用于实施会话劫持的常见方法，如数据包嗅探、跨站脚本攻击（XSS）和旁路攻击。
*   主要话题：会话的创建与管理、HTTP（非安全）连接存在的漏洞、劫持技术演示，以及面向用户和开发者的最佳防御实践。
*   为何值得观看：视频提供了清晰且实用的网络安全基础教育。了解会话劫持对于所有互联网用户都至关重要，它解释了登录会话如何被盗取以及如何进行有效防护，在使用公共Wi-Fi等场景下尤其有用。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=tc36mt6RdV4)**

### 🎬 Python Answersheets 🤣🙌 | #shorts #shortsfeed #python #pythonprogramming #trending #viral #funny
**Channel:** DevNest Code
*   What the video covers: A humorous short (YouTube Short) video that likely uses comedy to depict a funny or exaggerated scenario related to Python programming answers or interview experiences.
*   Key topics discussed: Python fundamentals, programming culture, and comedic takes on coding challenges or interviews, presented in a quick, viral-friendly format.
*   Why it's worth watching: Offers a lighthearted, relatable break from standard tech tutorials. It's perfect for a quick laugh and sharing within the programming community, highlighting the fun side of coding.

### 🎬 Python 答题卷 🤣🙌 | #shorts #shortsfeed #python #pythonprogramming #trending #viral #funny
**频道:** DevNest Code
*   视频内容概述：一个幽默的YouTube Shorts短视频，很可能以喜剧方式描绘了与Python编程答题或面试经历相关的搞笑或夸张场景。
*   主要话题：Python基础、编程文化，以及以快速、适合病毒传播的形式呈现的关于编程挑战或面试的趣味解读。
*   为何值得观看：为标准的技术教程提供了一个轻松、易产生共鸣的调剂。它非常适合快速放松并分享给编程社区，展示了编程有趣的一面。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=Vci5y4LSgr0)**

