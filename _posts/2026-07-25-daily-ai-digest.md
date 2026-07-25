### [Introducing Claude Opus 5]
* Claude Opus 5 is Anthropic's new model, offering near-frontier intelligence at half the price of Claude Fable 5.
* It achieves state-of-the-art results on coding and knowledge work benchmarks like Frontier-Bench and GDPval-AA, though it trails on cybersecurity tasks.
* Designed for daily use, it is more efficient than other models, serving as the new default on Claude Max and the strongest model on Claude Pro.
* At a cost similar to its predecessor (Opus 4.8), Opus 5 delivers significantly improved performance, especially in software engineering, knowledge work, and visual outputs.
* Real-world examples showcase its strong agency, including independently solving complex coding problems, fixing deep-seated bugs, and building entire data pipelines from scratch.

### [Claude Opus 5 模型发布]
* Claude Opus 5 是 Anthropic 推出的新模型，以 Claude Fable 5 一半的价格，提供了接近前沿的智能水平。
* 在 Frontier-Bench 和 GDPval-AA 等编码与知识工作基准测试中达到了最先进水平，但在网络安全任务上仍落后于 Mythos 5。
* 专为日常使用设计，比其他模型更高效，是 Claude Max 上的新默认模型和 Claude Pro 上的最强模型。
* 在与前代 (Opus 4.8) 成本相当的情况下，Opus 5 在软件工程、知识工作和视觉输出等方面性能大幅提升。
* 真实案例展示了其强大的自主行动能力，包括独立解决复杂编码问题、修复深层漏洞以及从头构建完整数据管道。

**[Read Original / 阅读原文](https://www.anthropic.com/news/claude-opus-5)**

### Wasmtime v47 Release: GC and Exceptions Enabled
*   Wasmtime v47 now enables the **WebAssembly GC (Garbage Collection)** and **Exceptions** proposals by default, marking a major milestone to support more high-level languages.
*   The **Wasm GC proposal** allows high-level languages (using objects and references) to run efficiently on WebAssembly without embedding their own garbage collector, reducing binary bloat and improving performance.
*   The **Wasm Exceptions proposal** provides native `try`/`catch`/`throw` semantics, eliminating the need for custom calling conventions and reducing overhead for languages that use exceptions.
*   Wasmtime's current GC implementation uses a **Cheney-style semi-space copying collector**, built atop WebAssembly linear memory for sandboxing, safety, and portability, with a primary focus on correctness and multi-instance use cases.

### Wasmtime v47 版本发布：默认启用 GC 与异常处理
*   Wasmtime v47 现已**默认启用 WebAssembly GC（垃圾回收）**和**异常处理**提案，标志着支持更多高级语言的一个重要里程碑。
*   **Wasm GC 提案**使使用对象和引用模型的高级语言能在 WebAssembly 上高效运行，无需嵌入自己的垃圾回收器，从而减小二进制文件体积并提升性能。
*   **Wasm 异常处理提案**提供了原生的 `try`/`catch`/`throw` 语义，消除了对自定义调用约定的需求，降低了使用异常语言的性能开销。
*   Wasmtime 当前的 GC 实现采用了 **Cheney 式半空间复制收集器**，基于 WebAssembly 线性内存构建，以保障沙箱安全性、安全性和可移植性，其设计主要关注正确性和多实例使用场景。

**[Read Original / 阅读原文](https://bytecodealliance.org/articles/wasmtime-gc)**

### The Scalability of Postgres LISTEN/NOTIFY
* Addresses the criticism that Postgres LISTEN/NOTIFY "does not scale" by analyzing and optimizing its underlying mechanics.
* Identifies the core bottleneck as a global exclusive lock during NOTIFY, which serializes transactions and limits throughput.
* Presents an optimization strategy: buffering notifications in memory and flushing them in batches to reduce lock contention.
* Reports a significant performance improvement, achieving up to 60,000 writes per second with millisecond latency on a single server.

### Postgres LISTEN/NOTIFY 的可扩展性
* 探讨并回应了关于 Postgres LISTEN/NOTIFY “无法扩展”的批评，通过分析和优化其底层机制。
* 核心瓶颈被确定为 NOTIFY 过程中的全局排它锁，该锁会序列化事务并限制吞吐量。
* 提出优化策略：在内存中缓冲通知，并通过批量提交来减少锁争用。
* 实现了性能大幅提升，在单服务器上达到每秒高达 60,000 次写入，且延迟在毫秒级。

**[Read Original / 阅读原文](https://www.dbos.dev/blog/postgres-listen-notify-scalability)**


## 🔥 GitHub Trending / GitHub 热门项目

### buzz - Human-AI Collaboration Platform
*   **What it does**: A self-hostable workspace built on Nostr, enabling seamless collaboration between humans and AI agents within shared "rooms." It unifies chat, code review, workflows, and agent operations into a single, auditable event log.
*   **Key features**:
    *   **First-class Agent Membership**: AI agents are participants with their own identities and audit trails, not just bots.
    *   **Unified Event Log**: All interactions—messages, code patches, CI results, approvals—are signed events on a single Nostr relay, creating a fully searchable and verifiable record.
    *   **Integrated Code Collaboration**: Features like "Branch as Room" bring patches, reviews, and merge decisions into the same channel where discussion happens.
    *   **Self-Hosted Sovereignty**: Designed to be run on your own relay, giving you control over your data and community.
    *   **Agent-First Tooling**: Comes with `buzz-cli` and an Agent Communication Protocol (ACP) for agents to interact programmatically with the workspace.
*   **Why it's notable**: Buzz is gaining significant traction because it presents a unified substrate for team collaboration, aiming to replace the fragmented stack of chat, forge, CI dashboards, and glue code. Its core innovation is treating AI agents as full-fledged members of a workspace with identical capabilities to human teammates, fostering a new paradigm for human-AI collaboration.

### buzz - 人机协作工作空间
*   **功能介绍**：一个基于Nostr协议的可自托管工作空间，让人类和AI代理能够在共享的“房间”内无缝协作。它将聊天、代码审查、工作流和代理操作统一到一个可审计的事件日志中。
*   **主要特点**：
    *   **一等成员身份**：AI代理是拥有独立身份和审计记录的参与者，而不仅仅是机器人。
    *   **统一事件日志**：所有交互——消息、代码补丁、CI结果、审批——都是单一Nostr中继上的签名事件，创建可完全搜索和验证的记录。
    *   **深度集成的代码协作**：“分支即房间”等功能，将补丁、审查和合并决策置于讨论发生的同一频道内。
    *   **自主托管**：设计为在您自己的中继上运行，赋予您对数据和社区的控制权。
    *   **代理优先工具**：提供`buzz-cli`和代理通信协议（ACP），供代理以编程方式与工作空间交互。
*   **为何值得关注**：Buzz因其旨在统一团队协作基础设施（取代分散的聊天、代码托管、CI看板和胶水代码）而迅速获得关注。其核心创新在于将AI代理视为工作空间中拥有与人类队友相同能力的正式成员，开创了人机协作的新范式。

**[View Repository / 查看仓库](https://github.com/block/buzz)**

### World Monitor - Real-time Global Intelligence Dashboard
* **What it does:** An AI-powered situational awareness interface that aggregates news from 500+ sources, monitors geopolitical events, and tracks global infrastructure on interactive maps.
* **Key features:** Features a dual map engine (3D globe & WebGL flat map), a Country Instability Index, finance radar for markets, local AI support via Ollama, 6 themed site variants, and a native desktop app. Provides a unified view of cross-stream data (military, economic, disaster signals).
* **Why it's notable:** Trending for its ambitious scope as an open-source (AGPL v3) "single pane of glass" for global events. Its combination of rich geospatial visualization, AI synthesis, and broad data coverage (finance, tech, energy, etc.) in a highly customizable stack makes it a significant project. The 2,184 stars in one day highlight strong developer interest.

### World Monitor - 实时全球情报仪表盘
* **功能介绍:** 一个AI驱动的态势感知界面，从500多个来源聚合新闻，监测地缘政治事件，并在交互式地图上追踪全球基础设施。
* **主要特点:** 拥有双地图引擎（3D地球仪和WebGL平面地图）、国家不稳定指数、金融市场雷达、通过Ollama支持本地AI、6个主题网站变体以及原生桌面应用。提供跨领域数据（军事、经济、灾难信号）的统一视图。
* **为何值得关注:** 该项目因其作为开源（AGPL v3）的全球事件“单一信息面板”的宏伟目标而迅速走红。其丰富的地理空间可视化、AI合成与广泛数据覆盖（金融、科技、能源等）的结合，以及高度可定制的技术栈，使其成为一个重要的项目。单日获得2,184个星标凸显了开发者的浓厚兴趣。

**[View Repository / 查看仓库](https://github.com/koala73/worldmonitor)**

### ComposioHQ/awesome-claude-skills - A Curated Collection of Production-Ready Claude Skills
* **What it does**: This repository is a comprehensive, community-driven list of over 1,000 "Claude Skills" – reusable instruction packages that teach AI agents (like Claude, Codex, Cursor, etc.) how to perform specific, complex workflows. It goes beyond simple text generation to enable real-world actions like sending emails, creating code artifacts, and managing projects.
* **Key features**:
    * **Vast, Categorized Library**: Skills are organized by domain (Document Processing, Development, Data Analysis, Business, etc.) for easy discovery.
    * **Platform Agnostic**: Skills are designed to work across Claude.ai, Claude Code, and other major coding agents following the open standard.
    * **Production-Focused**: Emphasizes skills that are ready for practical use, often enhanced by integration with the Composio MCP Gateway for secure access to 1,000+ apps.
    * **Clear Documentation**: Provides explanations of what skills are, how they work progressively to save context, and includes a quick-start guide for powerful integrations.
* **Why it's notable**: It's the definitive resource for unlocking the advanced capabilities of Claude and similar AI agents. The rapid growth (663 stars today) highlights its value in helping users move from AI that just *talks* to AI that *does*, by providing a massive, extensible toolkit for complex automation and development tasks.

### ComposioHQ/awesome-claude-skills - 精选的、可直接投入生产的Claude技能集合
* **功能介绍**：本仓库是一个全面、由社区维护的列表，收录了超过1000个“Claude技能”——这些是可复用的指令包，用于指导AI代理（如Claude、Codex、Cursor等）执行特定的复杂工作流。它超越了简单的文本生成，能够使AI执行诸如发送邮件、创建代码制品和管理项目等现实世界中的实际操作。
* **主要特点**：
    * **庞大且分类清晰的库**：技能按领域（文档处理、开发、数据分析、商务等）组织，便于发现和查找。
    * **平台无关性**：技能设计为跨Claude.ai、Claude Code以及其他遵循开放标准的主流编程代理工作。
    * **面向生产环境**：强调适用于实际使用的技能，通常通过集成Composio MCP网关来增强，以实现对1000+应用程序的安全访问。
    * **文档详尽**：解释了技能是什么、如何渐进式加载以节省上下文窗口，并提供了强大集成的快速入门指南。
*   **为何值得关注**：它是解锁Claude及类似AI代理高级能力的权威资源。其快速增长（今日663颗星）凸显了它的价值——它帮助用户将AI从仅仅“能对话”的水平，提升到通过一个庞大的、可扩展的工具包来实现复杂自动化和开发任务的“能执行”的水平。

**[View Repository / 查看仓库](https://github.com/ComposioHQ/awesome-claude-skills)**


## 🚀 Fast-Moving Repos / 快速崛起项目

### OpenWorker - AI Desktop Coworker That Finishes Tasks
* What it does
    * An open-source, local-first AI assistant that lives on your desktop and delivers **finished work** (like documents, reports, emails, calendar updates) rather than just providing chat responses. It integrates with your local files, terminal, and many everyday apps.
* Key features
    * **Model-agnostic**: Use your own API key for providers like OpenAI, Anthropic, Google, or run models fully locally with Ollama.
    * **Action-oriented**: Breaks down tasks, works across your tools, and requires approval before executing consequential actions (sending messages, editing files).
    * **Rich integrations**: Connects with 25+ apps including GitHub, Slack, Jira, Notion, Gmail, and Google Calendar.
    * **Scheduled automations**: Set up recurring tasks like daily briefings or weekly reports.
    * **Privacy-focused**: Your data stays on your machine; only the model and integrations you choose access it.
* Why it's notable
    * It represents a practical, privacy-conscious approach to personal AI agents by focusing on delivering tangible outcomes rather than open-ended conversation. Its "bring your own model" philosophy and extensive tool integrations make it a flexible platform for automating complex workflows. Its active beta status and significant star count (3635) show strong community interest.

### OpenWorker - 完成日常任务的AI桌面助手
* 功能介绍
    * 一个开源、本地优先的AI助手，驻留在你的桌面上，直接交付**完成的工作成果**（如文档、报告、邮件、日程更新），而不仅仅是聊天回复。它能整合你的本地文件、终端和众多常用应用程序。
* 主要特点
    * **模型无关**：使用你自己的API密钥接入OpenAI、Anthropic、Google等服务商，或通过Ollama完全本地运行模型。
    * **任务导向**：分解任务，跨工具工作，并在执行关键操作（发送消息、编辑文件）前需要你的批准。
    * **丰富的集成**：连接25+应用，包括GitHub、Slack、Jira、Notion、Gmail和Google日历。
    * **定时自动化**：设置定期任务，如每日简报或每周报告。
    * **注重隐私**：你的数据保留在本机上；只有你选择的模型和集成服务可以访问它。
* 为何值得关注
    * 它代表了一种实用且注重隐私的个人AI代理方案，核心在于交付具体的成果，而非开放式对话。其“自带模型”的理念和广泛的工具集成，使其成为一个灵活的平台，用于自动化复杂的工作流程。该项目处于活跃的Beta阶段并拥有可观的星标数（3635），显示了社区的浓厚兴趣。

**[View Repository / 查看仓库](https://github.com/andrewyng/openworker)**

### video-shotcraft - AI视频创作技能包，将AI编码代理转变为电影级产品视频工作室
*   **功能介绍**：这是一个为Claude Code或Codex等AI编码代理设计的技能包。它允许AI代理将任何产品页面转化为带有故事板、动画和音效设计的电影级宣传、营销或演示视频。其核心是基于[Remotion](https://www.remotion.dev/)框架，能够生成真实页面捕获、2.5D镜头运动、节拍同步剪辑和电影级音效。
*   **主要特点**：
    *   包含106张“镜头配方卡”，详细定义了镜头的目的、节奏、参数和实施要点。
    *   提供161个动态预览（涵盖162种风格），可在在线画廊中搜索和筛选。
    *   内置一个名为“Ink Press”的完整、可运行的视频模板（36.2秒，1920×1080，30fps，10个镜头）。
    *   包含Remotion实现参考、可复用组件、页面捕获脚本和音效资产。
    *   附带完整的生产方法论指南，涵盖从视觉指导到最终QA的全流程。
*   **为何值得关注**：该项目将AI编码代理的能力拓展到了视频制作领域，提供了一套高度系统化、即用型的工具包。它极大地简化了高质量产品视频的制作流程，使得开发者或创作者能够借助AI快速生成专业级的视觉内容，对于产品营销和展示具有很高的实用价值。其丰富的内容和清晰的架构（1500+星）表明它已成为该领域一个流行且成熟的解决方案。

### video-shotcraft - 为Claude Code和Codex设计的AI视频技能：基于Remotion的电影级产品视频制作工具包
*   **功能介绍**：这是一个AI代理技能，能将Claude Code或Codex转变为动态设计工作室。只需指向你的产品，它就能通过[Remotion](https://www.remotion.dev/)框架，自动生成包含真实页面捕获、2.5D镜头运动、节拍同步剪辑和电影级音效的产品宣传片、营销视频或演示视频。
*   **主要特点**：
    *   拥有106张“镜头配方卡”，涵盖目的、节奏、建议时长、参数和实施要点。
    *   提供161个动态预览，支持在线画廊搜索和筛选。
    *   附带一个经过验证的、完整的视频模板（“Ink Press”），可快速生成成品。
    *   包含Remotion实现、可复用组件、捕获脚本和音效资源。
    *   提供从分镜、视觉指导到音效设计的全套制作方法论。
*   **为何值得关注**：该项目为AI代理赋予了视频创作能力，提供了一套极其专业、系统化的工具库。它显著降低了制作高质量产品宣传视频的门槛，让开发者能借助AI快速完成从构思到成片的整个流程，对于提升产品展示效果和营销效率具有重要价值。其内容之全面和架构之清晰（超1500星）使其在该领域备受关注。

**[View Repository / 查看仓库](https://github.com/Vincentwei1021/video-shotcraft)**


## 🎬 YouTube Tech Videos / YouTube 技术视频

### 🎬 What Big Tech Missed And How Startups Can Still Win
**Channel:** Y Combinator
*   **What the video covers:** A talk from Startup School Paris where Alexandre LeBrun, the CEO of AMI, shares his entrepreneurial journey. He recounts building Vertos, the company behind the AMI voice assistant, and his experience selling his previous venture, Wit.ai, to Facebook (now Meta).
*   **Key topics discussed:** The speaker's personal story of founding and exiting a company, insights gained from the acquisition process, and an analysis of market opportunities that large tech companies (Big Tech) have overlooked or neglected. The core theme focuses on strategic areas where startups can find advantages and win.
*   **Why it's worth watching:** This offers a practical, founder's perspective on navigating the startup landscape adjacent to Big Tech giants. It's a valuable case study on identifying underserved markets and the potential for smaller companies to succeed by focusing where the giants have missed.

### 🎬 大型科技公司错失了什么以及创业公司如何依然能赢
**频道:** Y Combinator
*   **视频内容概述:** 这是来自“创业学校巴黎站”的一次演讲。AMI的CEO Alexandre LeBrun分享了他的创业历程，讲述了如何创立Vertos（AMI语音助手背后的公司），以及将他之前的公司Wit.ai出售给Facebook（现Meta）的经历。
*   **主要话题:** 演讲者个人创立和退出公司的故事，从收购过程中获得的洞察，以及对大型科技公司（Big Tech）所忽视或未充分开发的市场机会的分析。核心主题聚焦于创业公司能够获得优势并获胜的战略领域。
*   **为何值得观看:** 这提供了来自创始人视角的实用经验，探讨如何在与大型科技巨头相邻的领域中发展。这是一个关于如何识别服务不足市场的优秀案例研究，展示了小型公司如何通过专注于巨头错失的领域来获得成功。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=FVsgX0AdDTo)**

### 🎬 Why Physical AI Is the Next Platform Shift
**Channel:** Y Combinator
* This talk from Startup School Paris features Eric Landau, Co-CEO of Encord, discussing the transition from a career in quantitative finance to the frontier of AI. He argues that the next major platform shift in technology will be "Physical AI"—the integration of advanced AI with the physical world, particularly in robotics and automation.
* Key topics include the evolution of AI from digital to physical applications, the data challenges in robotics, the role of computer vision, and the entrepreneurial opportunities in building AI-native hardware and systems.
* It's worth watching for its clear vision of the future beyond software-only AI, offering founders and engineers a compelling roadmap for where foundational, real-world impact will be created next.

### 🎬 为什么物理AI是下一个平台转变
**频道:** Y Combinator
* 这场在巴黎创业学校（Startup School Paris）的演讲中，Encord联合首席执行官埃里克·兰道（Eric Landau）探讨了从量化金融职业生涯转型至AI前沿领域的历程。他认为，科技领域的下一个重大平台转变将是“物理AI”——即先进AI与现实世界的融合，特别是在机器人与自动化领域。
* 主要话题包括：AI从数字领域到物理应用的演进、机器人领域的数据挑战、计算机视觉的作用，以及构建AI原生硬件和系统的创业机遇。
* 值得观看的原因在于，它清晰地描绘了超越纯软件AI的未来图景，为创始人和工程师们指明了在哪里创造下一个具有基础性现实影响力的明确方向。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=F3INH9wZXoQ)**

### 🎬 Data for the Real World
**Channel:** Y Combinator
* What the video covers
* This video explores the critical challenge that AI models face beyond their current superhuman capabilities in code, language, and images: the scarcity and complexity of high-quality, real-world data for physical domains.
* Key topics discussed
* The data bottleneck for AI in robotics, healthcare, and other real-world applications.
* Why real-world data is harder to collect than digital data.
* Potential solutions, including synthetic data generation and new data collection paradigms.
* Why it's worth watching
* It provides a crucial, forward-looking perspective on the next major hurdle for AI advancement, moving the discussion from digital mastery to real-world impact. Essential for anyone interested in the practical future of AI and robotics.

### 🎬 Data for the Real World
**频道:** Y Combinator
* 视频内容概述
* 本视频深入探讨了当前AI模型在代码、语言和图像方面已超越人类后，面临的下一个关键挑战：为机器人、医疗等现实物理领域获取高质量、真实世界数据的稀缺性与复杂性。
* 主要话题
* AI在现实世界应用中的数据瓶颈问题。
* 现实世界数据为何比数字数据更难获取。
* 潜在的解决方案，如合成数据生成和新的数据收集范式。
* 为何值得观看
* 它对AI进化的下一个主要障碍提供了关键且前瞻性的视角，将讨论重点从数字世界的掌握转移到现实世界的影响。对于任何关注AI和机器人技术实际未来的人来说，这都是必看的内容。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=uW7RxkLRsd0)**

### 🎬 Session Hijacking Explained 🔐 | How Browser Sessions Work (Cybersecurity Awareness)
**Channel:** ezCommit

*   **What the video covers:** This video is an educational deep dive into the concept of session hijacking, a common cybersecurity attack. It explains how web sessions function in your browser, detailing the process from initial login to the creation and management of session tokens. The tutorial breaks down the technical mechanics behind how browsers and servers maintain a user's "logged-in" state.
*   **Key topics discussed:**
    *   The role of HTTP cookies and session tokens in maintaining user authentication.
    *   The step-by-step process of how a typical browser session is established.
    *   The fundamental vulnerability that allows attackers to steal or guess session tokens.
    *   Common session hijacking techniques (e.g., Cross-Site Scripting (XSS), network sniffing).
    *   Basic defensive concepts and awareness to protect against such attacks.
*   **Why it's worth watching:** In an era of rampant online accounts, understanding *how* your login session actually works is crucial for digital security. This video demystifies a core cybersecurity concept, moving beyond vague warnings to explain the "why" and "how" behind session vulnerabilities. It’s an excellent resource for anyone looking to build a foundational understanding of web security, from curious beginners to those studying for ethical hacking certifications. The clear, step-by-step explanation makes a complex topic accessible.

### 🎬 会话劫持详解 🔐 | 浏览器会话工作原理（网络安全意识）
**频道:** ezCommit

*   **视频内容概述：** 本视频是对“会话劫持”这一常见网络攻击概念的深入教育讲解。它详细解释了浏览器中网络会话是如何运作的，从用户初始登录到会话令牌的创建与管理全过程。教程拆解了浏览器和服务器维持用户“登录”状态背后的技术机制。
*   **主要话题：**
    *   HTTP Cookie和会话令牌在维持用户认证状态中的作用。
    *   浏览器建立典型会话的逐步流程。
    *   使攻击者能够窃取或猜测会话令牌的根本漏洞。
    *   常见的会话劫持技术（例如：跨站脚本攻击（XSS）、网络嗅探）。
    *   防御此类攻击的基本概念和安全意识。
*   **为何值得观看：** 在网络账户泛滥的时代，理解你的登录会话究竟如何工作，对数字安全至关重要。本视频揭开了一项核心网络安全概念的面纱，超越了模糊的警告，解释了会话漏洞背后的原因和方式。它对于任何希望建立Web安全基础知识的人来说都是绝佳资源，无论是好奇的初学者，还是正在学习道德黑客认证的人士。其清晰的分步讲解让复杂话题变得易于理解。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=tc36mt6RdV4)**

### 🎬 Chat GPT revealed my hidden photos
**Channel:** TheCyborgGirl
* **What the video covers:** An investigation into a privacy concern where the creator discovers that ChatGPT can potentially identify and surface photos of them that are not publicly available, raising alarms about data scraping and AI's access to personal information.
* **Key topics discussed:** AI photo recognition, online data scraping, privacy settings, and how personal data might be harvested and used by large language models.
* **Why it's worth watching:** It serves as a critical awareness piece for anyone concerned about digital privacy, demonstrating a real-world test of how much personal information AI systems might infer or access, and prompting important discussions about data consent and security.

### 🎬 ChatGPT揭露了我的隐藏照片
**频道:** TheCyborgGirl
* **视频内容概述:** 视频记录了一次隐私安全调查，创作者发现ChatGPT能够识别并调取出她并未公开发布的照片，引发了关于网络数据抓取和人工智能访问个人信息的严重担忧。
* **主要话题:** 人工智能图像识别、网络数据爬取、隐私设置、以及大型语言模型如何收集和使用个人数据。
* **为何值得观看:** 对于任何关注数字隐私的人来说，这是一个重要的警示案例。它通过实际测试，直观展示了人工智能系统可能推断或获取的个人信息范围，从而促使观众重新审视数据授权与网络安全的重要性。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=SqW03aaigPI)**

### Android May Soon Restrict On-Device ADB, Affecting Shizuku, libadb and Developers
*   **Early Warning:** Based on a Google IssueTracker feature request (not an official announcement), a core ADB maintainer proposed restricting on-device ADB connections to only the `wlan0` (Wi-Fi) interface for security reasons.
*   **Developer Impact:** This change would break legitimate on-device ADB use cases, including tools like Shizuku and libadb, as well as ADB over VPN or Ethernet. Developers use this method to run ADB commands directly on a device without a computer.
*   **Call to Action:** Developers with unique, constructive use cases are encouraged to provide detailed feedback on the issue tracker. Others can show support via the "+1" button without spamming.
*   **Technical Context:** On-device ADB uses loopback connections (`127.0.0.1`), enabling apps to run with elevated privileges. The article argues this isn't easily exploited by malicious apps due to required user actions and permissions.

### 安卓或将限制设备端ADB，影响Shizuku、libadb及开发者
*   **早期预警：** 基于谷歌问题跟踪器的一个功能请求（非官方公告），一位核心ADB维护者出于安全原因，提议将设备端ADB连接仅限制在`wlan0`（Wi-Fi）接口上。
*   **开发者影响：** 此变更将破坏包括Shizuku和libadb工具在内的合法设备端ADB使用场景，也会影响通过VPN或以太网的ADB连接。开发者使用此方法无需电脑即可直接在设备上执行ADB命令。
*   **行动呼吁：** 鼓励拥有独特、建设性用例的开发者在问题跟踪器上提供详细反馈。其他人可以通过点击“+1”按钮表示支持，而无需刷屏。
*   **技术背景：** 设备端ADB使用回环连接（`127.0.0.1`），使应用能以提升的权限运行。文章认为，由于需要用户操作和权限，恶意应用其实很难轻易利用此方式。

**[Read Original / 阅读原文](https://kitsumed.github.io/blog/posts/android-may-soon-restrict-on-device-adb/)**

### Hannah Fry Awarded Leelavati Prize for Public Mathematics Outreach
*   Professor Hannah Fry of Cambridge's Department of Applied Mathematics and Theoretical Physics (DAMTP) has received the prestigious Leelavati Prize from the International Congress of Mathematicians (ICM).
*   The prize recognizes her outstanding contributions to increasing public awareness of mathematics through creative and engaging media, including books, TV series, podcasts, and a massive social media following.
*   She is celebrated as a global ambassador for mathematical thinking, uniquely translating complex concepts into a "language of wonder and relevance" for the public.
*   Fry's work is driven by a passion to share the "absolute joy" and "secrets" of mathematics, aiming to create motivation and curiosity rather than just presenting information.

### 汉娜·弗莱教授因促进数学公众理解获Leelavati奖
*   剑桥大学应用数学与理论物理系教授汉娜·弗莱在国际数学家大会上荣获著名的Leelavati奖。
*   该奖项表彰她通过富有创造力和吸引力的媒介（包括书籍、电视节目、播客和庞大的社交媒体粉丝群）在提高公众数学意识方面所做出的杰出贡献。
*   她被誉为数学思维的全球大使，能够以“充满惊奇且贴合实际的语言”将复杂的数学概念有效地传达给公众。
*   弗莱教授致力于分享数学的“绝对乐趣”和奥秘，她的核心目标是激发公众的兴趣与好奇心，而不仅仅是传授知识。

**[Read Original / 阅读原文](https://www.maths.cam.ac.uk/features/professor-hannah-fry-wins-leelavati-prize)**

### Apartment Aquaponics System Guide
*   A comprehensive practical guide for setting up and maintaining a small-scale aquaponics system in a New York City apartment, based on lessons learned over two years.
*   Details a vertical, media-based continuous-flow design optimized for limited space, utilizing a 20-gallon fish tank and a grow-bed of clay pebbles.
*   Highlights key improvements made after initial setup, including enhanced drainage, a better pump, and strategic placement of the grow light.
*   Shares crucial lessons learned about tank cycling, the risks of small tanks, choosing resilient aquatic life, and the importance of avoiding overfeeding.

### 公寓水培系统指南
*   这是一份基于两年实践经验的综合性实用指南，旨在帮助读者在纽约市的公寓等有限空间内建立和维护小型水培系统。
*   详细介绍了一种为节省空间而优化的垂直式、介质基连续流系统设计，包含一个20加仑的鱼缸和一个填充了黏土砾的种植床。
*   重点介绍了在初始安装后进行的关键改进，包括增强排水系统、更换更合适的水泵以及优化种植灯的位置。
*   分享了关于建立硝化循环、小鱼缸的风险、选择适应性强的水生生物以及避免过度喂食等重要经验教训。

**[Read Original / 阅读原文](https://erinmurphy.dev/projects/project-2/)**

### Pumpkin - A High-Performance Minecraft Server Written in Rust
* **What it does**: Pumpkin is a Minecraft server implementation built entirely in Rust. It aims to provide a fast, efficient, and customizable server experience for hosting Minecraft games, prioritizing performance and strict adherence to vanilla game mechanics.
* **Key features**:
    * **Performance**: Leverages Rust's capabilities and multi-threading for maximum speed and efficiency.
    * **Cross-Platform Support**: Works with both Java and Bedrock editions of Minecraft.
    * **Comprehensive Mechanics**: Implements a wide range of vanilla features including world loading, chunk management, player actions (inventory, combat, experience), entity handling, and server administration tools like RCON and permissions.
    * **Flexibility**: Highly configurable via TOML files, with the ability to enable/disable features. It also supports proxy setups like Bungeecord and Velocity.
    * **Extensibility**: Designed as a foundation for future plugin development.
* **Why it's notable**: It represents a modern, high-performance alternative to traditional Java-based Minecraft servers. Its use of Rust promises superior speed and memory safety. The project is actively trending, indicating strong community interest, and is in active development towards a stable 1.0.0 release with an ambitious feature set aiming for full compatibility with the latest game versions.

### Pumpkin - 使用 Rust 语言构建的高性能 Minecraft 服务器
* **功能介绍**: Pumpkin 是一个完全使用 Rust 语言重写的 Minecraft 服务器。它旨在为玩家提供一个快速、高效且高度可定制的服务器托管体验，核心目标是追求极致性能并严格遵循原版游戏机制。
* **主要特点**:
    * **高性能**: 充分利用 Rust 语言的优势和多线程技术，以实现最佳的速度与效率。
    * **跨平台支持**: 同时支持 Minecraft Java 版和基岩版。
    * **丰富的原版机制**: 实现了大量游戏功能，包括世界加载、区块管理、玩家操作（如物品栏、战斗、经验值）、实体处理，以及 RCON、权限系统等服务器管理工具。
    * **灵活配置**: 支持通过 TOML 文件进行深度配置，可按需启用或禁用功能。同时支持 BungeeCord 和 Velocity 等代理方案。
    * **可扩展性**: 为未来的插件开发提供了基础架构。
* **为何值得关注**: 该服务器是使用传统 Java 技术栈的 Minecraft 服务器的一个现代化、高性能替代方案。Rust 语言的采用承诺了卓越的速度和内存安全性。该项目当前热度很高，表明其受到了社区的广泛关注，且正处于活跃开发阶段，正朝着兼容最新游戏版本、功能完备的 1.0.0 稳定版迈进。

**[View Repository / 查看仓库](https://github.com/Pumpkin-MC/Pumpkin)**

### Kronos - A Foundation Model for the Language of Financial Markets
*   **What it does:** Kronos is an open-source foundation model designed to understand the "language" of financial markets—specifically, K-line (candlestick) time series data. It pre-processes and learns from high-dimensional, noisy market data to perform unified quantitative forecasting.
*   **Key features:**
    *   **First-of-its-kind:** The first open-source foundation model trained specifically on financial candlestick data from over 45 global exchanges.
    *   **Two-stage framework:** Uses a specialized tokenizer to convert continuous K-line data (OHLCV) into hierarchical discrete tokens, followed by pre-training a large autoregressive Transformer on this sequence.
    *   **Diverse Model Zoo:** Provides a family of pre-trained models (Kronos-mini, small, base) with different parameter scales (4.1M to 102.3M) and context lengths, all accessible via Hugging Face.
    *   **Easy Deployment:** Includes a simple `KronosPredictor` API for quick inference and a `predict_batch` method for efficient parallel forecasting on multiple time series.
*   **Why it's notable:** It addresses the unique challenges of financial time series (high noise, non-stationarity) with a purpose-built architecture rather than general-purpose models. Its recent acceptance at AAAI 2026 and rapid star gain (499 stars in one day) highlight its significance in the AI for Finance community.

### Kronos - 面向金融市场语言的基础模型
*   **功能介绍：** Kronos是一个开源基础模型，旨在理解金融市场的“语言”——即K线（蜡烛图）时间序列数据。它通过对高维、高噪声的市场数据进行预处理和学习，来执行统一的量化预测任务。
*   **主要特点：**
    *   **开创性项目：** 首个专门基于全球45个以上交易所K线数据训练的开源基础模型。
    *   **两阶段框架：** 采用专用分词器将连续的K线数据（开高低收量等）量化为层次化的离散标记，随后在自回归Transformer上对这些序列进行预训练。
    *   **多样化的模型库：** 提供一系列预训练模型（Kronos-mini, small, base），具有不同的参数规模（4.1M到102.3M）和上下文长度，均可通过Hugging Face Hub获取。
    *   **部署简便：** 提供了简单的 `KronosPredictor` API 用于快速推理，以及 `predict_batch` 方法，可高效并行地对多个时间序列进行预测。
*   **为何值得关注：** 它通过专为金融时间序列设计的架构来解决该领域的独特挑战（高噪声、非平稳性），而非使用通用模型。其论文被AAAI 2026接收以及一天内获得499颗星的成绩，凸显了它在“AI+金融”领域的重要性。

**[View Repository / 查看仓库](https://github.com/shiyu-coder/Kronos)**

### thinking-orbs - Dotted thought-orb loading indicators for AI & agent UIs
* **What it does**: Provides a React component (`<ThinkingOrb>`) that renders animated, dotted orb indicators to visually represent the activity state of an AI or agent (e.g., searching, solving, listening).
* **Key features**: Features six hand-tuned animation states, two purpose-built sizes (for avatars and inline use), strict monochrome theming with automatic dark/light mode detection, and uses only plain 2D Canvas for maximum compatibility and performance.
* **Why it's notable**: It is a lightweight, high-performance, and accessible solution specifically designed for modern AI interfaces. Its thoughtful details—like pausing offscreen, respecting `prefers-reduced-motion`, and broad browser support (Chrome, Safari, Firefox)—make it a robust and user-friendly choice for adding clear status feedback in agent UIs.

### thinking-orbs - 用于AI与智能体界面的点状思维球加载指示器
* **功能介绍**：提供一个 React 组件（`<ThinkingOrb>`），用于渲染动画化的点状球体指示器，直观地表示 AI 或智能体的活动状态（例如：搜索、解决、倾听）。
* **主要特点**：包含六种精细调校的动画状态，两种专为不同场景（头像、内联文本）设计的尺寸，严格的单色主题并支持自动深色/浅色模式检测，且完全使用纯 2D Canvas 渲染，以确保极佳的兼容性和性能。
* **为何值得关注**：这是一个专为现代 AI 界面设计的轻量级、高性能且注重可访问性的解决方案。其精细的考量——如自动暂停不在屏幕内的动画、遵循 `prefers-reduced-motion` 减弱动效设置、以及广泛的浏览器兼容性（Chrome、Safari、Firefox）——使其成为在智能体用户界面中添加清晰状态反馈的健壮且用户友好的选择。

**[View Repository / 查看仓库](https://github.com/Jakubantalik/thinking-orbs)**

### Nativ - 本地化 macOS AI 工作台
*   **功能介绍**：Nativ 是一款专为 Apple Silicon Mac 设计的原生应用程序，它将运行、管理、与本地 AI 模型交互的所有流程整合到一个界面中。用户可以通过它与本地模型聊天、将其作为本地 API 服务器使用、管理模型库以及监控性能。
*   **主要特点**：
    *   **一体化工作台**：集成了聊天界面、模型库、性能仪表盘和本地 API 服务器功能。
    *   **深度本地化**：模型完全在用户的 Mac 上运行，保护数据隐私，无需将数据发送至云端。
    *   **强大兼容性**：提供与 OpenAI 和 Anthropic 兼容的 API 端点，可无缝对接现有工具；支持集成 Codex、Claude Code 等编程辅助工具。
    *   **原生与高性能**：基于 SwiftUI 构建，充分利用 Apple Silicon 性能，并通过 MLX 框架进行优化推理。
    *   **丰富的控制选项**：提供从采样参数到 KV-cache 量化等高级推理控制，并在菜单栏提供便捷的操作入口。
*   **为何值得关注**：Nativ 解决了普通用户在本地运行和管理 AI 模型门槛高、流程分散的痛点。它将复杂的底层技术（如 MLX 服务器）封装在一个优雅、易用的原生 Mac 应用中，让隐私优先的本地 AI 体验变得触手可及。其全面的功能集和作为本地 API 网关的潜力，使其成为 Apple Silicon 用户探索本地 AI 的强大工具。

### Nativ - 面向 Mac 的一体化本地 AI 工作台
*   **功能介绍**：Nativ 是一款专为搭载 Apple Silicon 芯片的 Mac 设计的原生应用程序，集本地 AI 模型聊天、服务、监控与管理于一体。它是一个私密的聊天工具、模型管理器、性能监控仪表盘，也是一个兼容主流格式的本地推理服务器。
*   **主要特点**：
    *   **功能全面**：提供带流式输出和图片附件的聊天、模型发现与下载、详细的性能分析、兼容 OpenAI/Anthropic 的本地 API、以及多种编程工具集成。
    *   **原生体验**：使用 SwiftUI 构建，深度集成 macOS 系统，具备菜单栏控制、应用内更新等特性，提供流畅的原生操作体验。
    *   **本地优先**：所有推理均在本地 Mac 上完成，保障数据隐私安全。模型管理器能智能适配用户的 Hugging Face 缓存和内存。
    *   **开发者友好**：提供可配置的本地 API 服务器、运行日志查看、详细的度量指标端点以及完整的项目构建流程。
    *   **高度可控**：支持对采样、思考预算、结构化输出等高级推理参数进行细致调优。
*   **为何值得关注**：该项目将运行本地 AI 所需的多个复杂环节（如服务器管理、模型下载、API 封装）整合进一个美观易用的原生应用，极大降低了使用门槛。它不仅是一个聊天客户端，更是一个强大的本地 AI 开发和运维平台，特别适合注重隐私、希望利用 Apple Silicon 性能进行本地 AI 实验和开发的用户。其清晰的架构和活跃的开发（有“即将推出”的功能）使其成为一个值得关注的项目。

**[View Repository / 查看仓库](https://github.com/Blaizzy/nativ)**

### 🎬 If Code Works Don't Touch It !! #coding #programming #python #shorts
**Channel:** Aziz Codex
*   This is a humorous programming short video, likely depicting a common scenario where a developer is tempted to refactor or modify code that is already functioning, despite the well-known principle of "if it works, don't touch it."
*   Key topics include coding practices, the humor in over-engineering, and the relatable struggle between code perfectionism and pragmatic results.
*   It's worth watching for a quick, relatable laugh that many programmers and developers will find familiar and entertaining. It serves as a light reminder of a common industry saying.

### 🎬 如果代码能用就别动它！！ #编程 #代码 #Python #Shorts
**频道:** Aziz Codex
*   这是一个幽默的编程短片视频，很可能描绘了一个常见场景：程序员忍不住想要重构或修改一段已经能正常工作的代码，尽管业内广为流传着“能用就别动”的原则。
*   主要话题包括编程习惯、过度工程化的幽默，以及程序员在追求代码完美与追求实用结果之间那种令人共鸣的挣扎。
*   值得观看，因为它能为许多程序员和开发者带来快速、会心一笑的共鸣时刻，是对一个常见行业俗语的轻松提醒。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=2xZJk8Vaxvk)**

### 🎬 🛑 No escondas así tus archivos
**Channel:** SCPC Informática
* This video debunks a popular but flawed Windows "trick" for hiding files. It explains why creating a folder with a blank name (using ALT + 255) and a transparent icon is an insecure and easily reversible method.
* Key topics discussed include the specific keystroke trick (ALT + 255), the use of transparent icons, and why these methods provide no real security and can be easily discovered by anyone with basic computer knowledge.
* It's worth watching to understand a common but ineffective security practice and to avoid being misled into thinking your files are safely hidden using this simplistic method.

### 🎬 🛑 No escondas así tus archivos
**频道:** SCPC Informática
* 视频内容概述：本视频揭露了Windows系统中一个流行但无效的文件“隐藏”技巧。它解释了为何通过使用ALT + 255创建空白文件夹名并搭配透明图标，这种方法既不安全又容易被撤销。
* 主要话题：讨论了特定的按键技巧（ALT + 255）、透明图标的使用，以及为何这些方法无法提供真正的安全保护，任何具备基本计算机知识的人都能轻易发现这些文件。
* 为何值得观看：帮助你了解一种常见但低效的安全实践，避免被误导，误以为使用这种简单方法就能安全地隐藏文件。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=1a69pHBA6tE)**

### 🎬 OmniRoute + OpenCode is INSANE (Why I Dropped Claude Code)
**Channel:** Cloud Codes
*   What the video covers
    The video critically examines the practical limitations of using Anthropic's Claude Code, particularly its aggressive 5-hour rate limits, and presents a compelling alternative. It introduces the **OmniRoute** API router/proxy and the **OpenCode** AI coding assistant as a powerful, cost-effective, and flexible combination that outperforms the closed-source Claude Code for many developers.
*   Key topics discussed
    *   **The Problem:** The frustrations and workflow disruptions caused by Claude Code's rate limiting and subscription costs.
    *   **The Solution Stack:**
        *   **OmniRoute:** A tool that acts as a central hub to manage and route requests to various LLM APIs (like OpenAI, Anthropic, and local models).
        *   **OpenCode:** An open-source, terminal-based AI coding assistant designed to be extensible and provider-agnostic.
    *   **Performance & Cost:** Demonstrations showing the combined stack's impressive speed, capability, and the potential for significant cost savings by optimizing model usage and avoiding vendor lock-in.
    *   **Flexibility & Control:** The advantage of an open-source ecosystem, allowing for customization, use of local models, and freedom from a single provider's constraints.
*   Why it's worth watching
    It's essential viewing for any developer feeling constrained by mainstream AI coding tools. It provides a practical, hands-on guide to building a more powerful, affordable, and autonomous developer workflow using leading open-source technologies. You'll learn about tools that put you back in control of your coding assistant experience.

### 🎬 OmniRoute + OpenCode 封神之路（为何我弃用 Claude Code）
**频道:** Cloud Codes
*   视频内容概述
    本视频深入剖析了使用 Anthropic 公司 Claude Code 的实际痛点，尤其是其严格的5小时速率限制，并推荐了一个极具吸引力的替代方案。视频重点介绍了 **OmniRoute**（一个API路由/代理）和 **OpenCode**（一个AI编码助手）的组合，论证了这套方案在性能、成本和灵活性上如何超越闭源的 Claude Code。
*   主要话题
    *   **核心问题：** 开发者在使用 Claude Code 时因速率限制和订阅费用导致的挫折感与工作流中断。
    *   **解决方案组合：**
        *   **OmniRoute：** 一个作为中心枢纽的工具，用于管理和路由到不同大语言模型API（如OpenAI、Anthropic及本地模型）的请求。
        *   **OpenCode：** 一个开源的、基于终端的AI编码助手，设计上具有高度可扩展性和提供商无关性。
    *   **性能与成本：** 通过演示展示该组合方案惊人的速度、能力，以及通过优化模型使用和避免厂商锁定所带来的显著的成本节约潜力。
    *   **灵活性与控制力：** 开源生态系统的优势，允许定制化、使用本地模型，并摆脱单一提供商的限制。
*   为何值得观看
    对于任何受主流AI编码工具所限的开发者而言，这是必看的内容。它提供了一份实践指南，教你如何利用领先的开源技术，构建更强大、更经济、更自主的开发者工作流。你将了解如何重新夺回对编码助手体验的控制权。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=AQm1ig0GrP4)**

### 🎬 (Pt 2) "Cadillac Expert"...has NO CLUE!! ('17 CTS: Key Fob Programming FIASCO)
**Channel:** Pine Hollow Auto Diagnostics
*   **What the video covers:** This is Part 2 of a diagnostic saga. After fixing a complex network fault in a 2017 Cadillac CTS, the technician tackles the customer's second request: programming a new key fob. The process reveals a series of confusing and frustrating failures with the dealership's procedure.
*   **Key topics discussed:** Cadillac key fob programming, diagnosing and resolving CAN network communication faults, the limitations of OEM "expert" procedures, real-world automotive electrical troubleshooting, and the importance of understanding system fundamentals.
*   **Why it's worth watching:** It’s a compelling, real-world case study that goes beyond a simple "how-to." It demonstrates advanced diagnostic logic, highlights the gap between theoretical service information and practical reality, and teaches viewers how to persistently troubleshoot when standard procedures fail.

### 🎬 (Pt 2) "凯迪拉克专家"...竟是一无所知!! ('17款 CTS: 钥匙编程大乱斗)
**频道:** Pine Hollow Auto Diagnostics
*   **视频内容概述:** 这是诊断传奇的第二部分。在修复了一辆2017款凯迪拉克CTS极其复杂的网络故障后，技术人员开始处理客户的第二个要求：编程一把新钥匙。整个过程暴露了经销商提供的编程程序中一系列令人困惑和沮丧的失败。
*   **主要话题:** 凯迪拉克钥匙编程、诊断和解决CAN网络通信故障、OEM“专家”程序的局限性、现实世界中的汽车电气系统故障排查、以及理解系统基础知识的重要性。
*   **为何值得观看:** 这是一部引人入胜的真实案例研究，超越了简单的“操作指南”。它展示了高级诊断逻辑，突出了理论服务信息与实际现实之间的差距，并教会观众当标准程序失败时如何进行坚持不懈的故障排查。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=IOEVfZqMcb8)**

