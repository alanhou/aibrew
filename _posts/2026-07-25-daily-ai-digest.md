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

