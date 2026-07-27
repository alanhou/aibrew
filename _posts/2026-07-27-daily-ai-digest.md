### PGSimCity · How PostgreSQL Works, in 3D
* A 3D interactive model designed to illustrate the inner workings of the PostgreSQL database engine, simulating its processes in a visual format.
* Currently an early, unreviewed prototype that may contain inaccuracies; users are encouraged to report issues or contribute via GitHub for improvements.
* Requires JavaScript and WebGL2 to run, indicating it is web-based and relies on modern browser capabilities for 3D rendering.

### PGSimCity · 如何在3D中了解PostgreSQL的工作原理
* 一个3D交互模型，旨在通过可视化形式模拟PostgreSQL数据库引擎的内部工作机制和过程。
* 目前为早期未审核原型，可能存在不准确之处；鼓励用户通过GitHub提交问题报告或贡献代码以完善项目。
* 需要JavaScript和WebGL2才能运行，表明它基于Web技术，依赖现代浏览器进行3D渲染。

**[Read Original / 阅读原文](https://nikolays.github.io/PGSimCity/)**

<!-- [Title-Only] -->
### Show HN: Physically accurate black hole you can put in your room
* This article likely introduces an interactive, web-based simulation or visualization of a black hole that adheres to real-world physics. Given the "Show HN" format, it's probably a personal or small-team project, possibly using advanced graphics (like WebGL or a game engine) to render accurate gravitational lensing, accretion disks, and event horizons in a browser.
* It could be interesting to readers because it combines complex astrophysical concepts with accessible, immersive technology. The ability to place such a dramatic cosmic phenomenon into a domestic setting (via augmented reality or a 3D viewer) makes cutting-edge science engaging and tangible for a wide audience.

### Show HN: 你可以放进房间里的物理精确黑洞
* 根据标题推测，这篇文章很可能介绍了一个基于网页的交互式黑洞模拟或可视化工具。它声称遵循真实的物理学原理。鉴于“Show HN”的格式，这大概率是一个个人或小团队的项目，可能使用了高级图形技术（如WebGL或游戏引擎）在浏览器中精确渲染引力透镜、吸积盘和事件视界。
* 之所以值得关注，是因为它将复杂的天体物理学概念与易于访问的沉浸式技术相结合。能够将这种宏大的宇宙现象带入家庭环境（通过增强现实或3D查看器），使得前沿科学对更广泛的受众而言变得引人入胜且真实可感。

**[Read Original / 阅读原文](https://blackhole.plav.in)**

### Decker Multimedia Platform Overview
* A multimedia platform for creating interactive documents with sound, images, hypertext, and scripted behavior, inspired by HyperCard and classic MacOS aesthetics.
* Features a novel scripting language called *Lil* (combining Lua and Q), built-in interactive widgets, command-line tools, and cross-platform support (MacOS, Windows, BSD, Linux).
* Emphasizes simplicity, creative constraints ("ditherpunk" aesthetic), and user privacy; open-source under MIT license with active community engagement.

### Decker 多媒体平台概述
* 一个用于创建包含声音、图像、超文本和脚本行为的交互式文档的多媒体平台，灵感来源于 HyperCard 和经典 MacOS 美学。
* 特色包括新型脚本语言 *Lil*（结合 Lua 和 Q 的特点）、内置交互组件、命令行工具，以及跨平台支持（MacOS、Windows、BSD、Linux）。
* 强调简洁性、创意限制（“ditherpunk”美学）和用户隐私；基于 MIT 许可证开源，并拥有活跃的社区参与。

**[Read Original / 阅读原文](https://beyondloom.com/decker/)**


## 🔥 GitHub Trending / GitHub 热门项目

### bitchat - Decentralized P2P Messenger with Bluetooth Mesh & Nostr
*   **What it does**: A decentralized peer-to-peer messaging app that combines a local **Bluetooth mesh network** for offline communication with the internet-based **Nostr protocol** for global reach. It requires no accounts, phone numbers, or central servers.
*   **Key features**:
    *   **Dual Transport Architecture**: Automatically chooses the best path, using Bluetooth first (for privacy/speed) and falling back to Nostr when needed.
    *   **Location-Based Channels**: Create or join geographic chat rooms defined by geohash precision (block, neighborhood, city, etc.) over global Nostr relays.
    *   **Privacy First Design**: No user accounts, no phone numbers, and no central servers. End-to-end encryption uses the Noise Protocol for mesh and proprietary "BitChat private envelopes" for Nostr.
    *   **Intelligent & Resilient**: Features multi-hop message relay over Bluetooth (up to 7 hops), emergency data wipe, and adaptive battery/power management.
    *   **Familiar Interface**: IRC-style commands (`/msg`, `/who`, `/slap`) for a classic chat feel, running as a universal iOS/macOS app.
*   **Why it's notable**: It's a trending project (**1,166 stars today**) because it solves real-world problems of communication in off-grid, high-privacy, or disaster scenarios. Its hybrid architecture offers a compelling blend of **offline resilience** and **global connectivity** without sacrificing user privacy or control. The project's commitment to open-source verification also stands out.

### bitchat - 支持蓝牙网状网络与Nostr协议的去中心化P2P通讯应用
*   **功能介绍**：一款去中心化的点对点即时通讯应用，结合了用于离线通讯的本地**蓝牙网状网络**和用于全球互联的互联网**Nostr协议**。它无需账户、手机号或中央服务器。
*   **主要特点**：
    *   **双传输架构**：智能路由，优先使用蓝牙（隐私/速度快），不可用时自动回退至Nostr协议。
    *   **基于地理位置的频道**：通过Nostr中继服务器，可以加入或创建由地理哈希精度定义的聊天室（街区、社区、城市等）。
    *   **隐私优先设计**：无用户账户、无手机号、无中央服务器。使用Noise协议为网状网络加密，使用专有的“BitChat信封”为Nostr传输加密，实现端到端加密。
    *   **智能与可靠**：支持蓝牙多跳中继（最多7跳），具备紧急数据擦除功能，并优化了电池和功耗管理。
    *   **熟悉的界面**：提供IRC风格命令（`/msg`, `/who`, `/slap`），带来经典的聊天体验，同时作为通用应用支持iOS和macOS。
*   **为何值得关注**：该项目今日新增 **1,166 颗星**，热度很高。它通过创新的混合架构，解决了无网络、高隐私或灾难场景下的真实通讯需求，巧妙地平衡了**离线韧性**与**全球连通性**，同时不牺牲用户隐私和控制权。项目对开源代码可验证性的重视也使其显得与众不同。

**[View Repository / 查看仓库](https://github.com/permissionlesstech/bitchat)**

### ego-lite - AI Agent专用的超速浏览器
* **功能介绍**  
  这是一个专为AI代理（如Codex、Claude Code）设计的极速浏览器，核心目标是让AI代理能够安全、高效地执行网页自动化任务，同时与用户的个人浏览环境（登录状态、标签页、Cookie等）完全隔离，互不干扰。用户可以零成本、零配置地与自己的AI代理并行工作。

* **主要特点**  
  * **代码驱动，效率更高**：暴露给代理的是可直接调用的JavaScript函数而非命令行，代理能一次性编排复杂任务，相比传统CLI方式，复杂工作流执行速度提升最高2.5倍，且token消耗更少。
  * **独立工作空间（Spaces）**：为每个AI代理提供完全隔离的“空间”，多个代理任务可同时并行执行，且不会影响用户自己的标签页。
  * **顶级页面快照**：基于内核级定制，生成高质量的页面快照，能可靠处理深层嵌套iframe等复杂场景，让AI代理更精准地“理解”页面。
  * **通用技能（Skill）集成**：通过`ego-browser`技能连接任意代理CLI（如Cursor、Claude Code），将浏览器操作暴露为一组内联JavaScript工具。
  * **无摩擦继承登录状态**：首次启动时可一键迁移现有Chrome数据（登录、书签、扩展），让代理无缝使用用户的现有账户。

* **为何值得关注**  
  它解决了一个关键痛点：现有浏览器自动化框架（如browser-use）需要独立的浏览器且登录状态无法共享，而内置AI代理的浏览器（如Perplexity Comet）则封闭且不免费。ego-lite是**第一个为“用户与AI代理共享同一个浏览器”而生的设计**，既保证了日常使用的便利性，又提供了高效、并行的自动化能力。今日900+的星标数反映了其快速上升的趋势和市场认可度。

### ego-lite - 专为AI代理打造的超速浏览器
* **功能介绍**  
  这是一款专为AI代理（如Codex、Claude Code）设计的高性能浏览器，旨在让AI代理能够执行网页自动化任务，并与用户个人的浏览器状态（登录信息、标签页等）安全隔离、互不干扰。用户可以零成本、零配置地与AI代理实现并行浏览和工作。

* **主要特点**  
  * **代码驱动，执行更快**：向代理提供可调用的JavaScript函数而非命令行，代理可直接编排复杂任务。与传统CLI方式相比，复杂工作流执行速度提升最高2.5倍，且消耗的token更少。
  * **独立工作空间（Spaces）**：为每个AI代理提供完全隔离的运行环境，多个代理任务可同时并行，且不会占用或干扰用户自己的标签页。
  * **顶级页面快照**：通过内核级定制，生成高质量的页面快照，能可靠处理深层嵌套iframe等复杂情况，提升AI代理对页面的理解与操作精度。
  * **通用技能（Skill）集成**：通过`ego-browser`技能与各类代理CLI（如Cursor、Claude Code）连接，将浏览器操作封装为一组内联的JavaScript工具供代理使用。
  * **无感继承登录状态**：首次启动时可一键迁移现有Chrome数据（登录、书签、扩展等），让代理无缝使用用户的现有账户。

* **为何值得关注**  
  它精准地解决了一个市场空白：现有自动化工具无法共享用户登录状态，而内置AI代理的浏览器又封闭且收费。ego-lite是**首个从设计之初就面向“用户与AI代理共享同一浏览器”场景的解决方案**，兼顾了日常浏览器的实用性与AI自动化任务的高效性、并行性。其今日迅速获得的900+星标，凸显了其创新性和市场热度。

**[View Repository / 查看仓库](https://github.com/citrolabs/ego-lite)**

### block/buzz - A Hive Mind Communication Platform (Rust)
*   **What it does:** Buzz is a self-hostable workspace platform built in Rust where humans and AI agents collaborate in shared digital "rooms." It uses the Nostr protocol as its backbone, meaning all messages, code reviews, workflow steps, and git events are signed events in a single, auditable log.
*   **Key features:**
    *   **Unified Environment:** Agents are treated as first-class members with their own identity keys and audit trails, not as external bots.
    *   **Integrated Workflow:** Seamlessly combines chat, code (patches via NIP-34), CI results, reviews, and release management into a single event stream.
    *   **Agent Capabilities:** Agents can search history, triage issues, create channels, run workflows, and orchestrate tasks with the same interface as humans.
    *   **Flexible Deployment:** Includes a desktop app (Tauri), CLI for agents, and can be self-hosted or run via a hosted relay.
*   **Why it's notable:** Buzz aims to replace the fragmented stack of chat, forge, bots, and CI dashboards with a single, coherent substrate. It's trending because it provides a compelling vision for deep human-AI collaboration, where agents are integrated teammates rather than separate tools. The high number of stars today indicates strong community interest in this approach.

### block/buzz - 一个基于 Rust 的“蜂巢思维”通信平台
*   **功能介绍：** Buzz 是一个可自托管的工作空间平台，使用 Rust 开发。它让人类和 AI 代理能够在共享的数字“房间”中协作。平台底层基于 Nostr 协议，这意味着所有的消息、代码审查、工作流步骤和 git 事件都是一个单一、可审计日志中的签名事件。
*   **主要特点：**
    *   **统一环境：** AI 代理被视为拥有一套独立密钥和审计记录的一等成员，而非外部机器人。
    *   **集成工作流：** 将聊天、代码（通过 NIP-34 提交补丁）、CI 结果、审查和发布管理无缝整合到单一的事件流中。
    *   **代理能力：** 代理可以搜索历史记录、分类问题、创建频道、运行工作流，并使用与人类相同的界面进行任务编排。
    *   **灵活部署：** 包含桌面应用（Tauri）、代理专用 CLI，并且可以自托管或通过托管中继服务运行。
*   **为何值得关注：** Buzz 旨在用单一、连贯的基础设施，取代当前由聊天、代码托管平台、机器人和 CI 仪表盘组成的分散技术栈。它之所以获得关注，是因为它为深度的人机协作提供了一个引人注目的愿景，在此愿景中，代理是融入团队的成员，而非独立的工具。今日的大量星标表明社区对这种协作方式抱有强烈兴趣。

**[View Repository / 查看仓库](https://github.com/block/buzz)**


## 🚀 Fast-Moving Repos / 快速崛起项目

### [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) - Running a 28.9M parameter LLM on an $8 microcontroller
*   **What it does**: This project runs a 28.9 million parameter language model locally on an ESP32-S3 microcontroller (costing ~$8). It generates coherent short stories directly on the device, with no cloud connectivity, at approximately 9 tokens per second.
*   **Key features**: It achieves a ~100x increase in model size compared to previous on-device models by using a clever memory architecture (Per-Layer Embeddings from Google Gemma). The vast majority (25M parameters) of the model is stored in flash memory and sampled on-demand, leaving only the small "thinking" core in fast SRAM.
*   **Why it's notable**: This is a significant breakthrough in edge AI, demonstrating that relatively large, functional language models can run on extremely low-cost, resource-constrained hardware. The architecture is a novel adaptation of a state-of-the-art technique for microcontrollers, making AI inference more accessible.

### [slvDev/esp32-ai](https://github.com/slvDev/esp32-ai) - 在8美元微控制器上运行28.9M参数的大语言模型
*   **功能介绍**: 本项目在ESP32-S3微控制器（成本约8美元）上本地运行一个拥有2890万参数的语言模型。设备无需联网，即可直接生成连贯的短篇故事，速度约为每秒9个token。
*   **主要特点**: 通过采用Google Gemma模型的“每层嵌入”技术，项目成功将模型规模提升了约100倍。其核心在于内存架构创新：将绝大部分参数（2500万）存储在Flash中按需读取，仅让少量负责推理的核心部分驻留在高速SRAM中。
*   **为何值得关注**: 这是边缘AI领域的一项重要突破，证明了在极低成本和资源有限的硬件上，运行相对大型且可用的语言模型是可能的。该架构为微控制器适配了前沿技术，极大地提升了AI推理的可及性。

**[View Repository / 查看仓库](https://github.com/slvDev/esp32-ai)**

### thinking-orbs - Dotted thought-orb loading indicators for AI & agent UIs
*   **What it does:** A lightweight React component library that renders animated, dotted "thought orb" loading indicators. It is specifically designed for AI assistants and agent user interfaces to visually represent different processing states (like working, searching, solving, etc.).
*   **Key features:** Six hand-tuned, distinct animated states; two purpose-built size presets; automatic dark/light theme detection (supports OS, class/attribute, and manual settings); high performance via plain 2D Canvas with no WebGL; built-in accessibility (ARIA labels, respects `prefers-reduced-motion`); and automatic pausing/resuming for performance.
*   **Why it's notable:** It solves a specific design problem for AI/agent UIs with a high level of polish. The focus on six distinct, meaningful states (beyond a generic spinner), performance optimizations (auto-pause, no filters), and broad browser compatibility make it a robust and elegant solution for adding visual feedback in AI applications.

### thinking-orbs - 专为AI与智能体UI设计的点状思考球加载指示器
*   **功能介绍:** 一个轻量级的React组件库，用于渲染动态的“思考球”加载指示器。它专为AI助手和智能体用户界面设计，用于直观地展示不同的处理状态（如工作中、搜索中、解决中等）。
*   **主要特点:** 提供六种精心调校的、各具特色的动画状态；两种专门设计的尺寸预设；支持自动检测暗色/浅色主题（兼容操作系统设置、CSS类/属性及手动指定）；采用纯2D Canvas渲染，无需WebGL，性能高且跨浏览器表现一致；内置无障碍支持（ARIA标签、遵循`prefers-reduced-motion`设置）；并能自动暂停/恢复动画以提升性能。
*   **为何值得关注:** 它精准地解决了AI/智能体UI中的特定设计需求，并且打磨得非常精致。相比通用的旋转加载图标，它专注于六种有意义的差异化状态、出色的性能优化（自动暂停、无滤镜依赖）以及广泛的浏览器兼容性，使其成为在AI应用中添加高质量视觉反馈的可靠而优雅的解决方案。

**[View Repository / 查看仓库](https://github.com/Jakubantalik/thinking-orbs)**


## 🎬 YouTube Tech Videos / YouTube 技术视频

### 🎬 Jensen Huang: The Mindset That Built NVIDIA
**Channel:** Y Combinator
*   The video explores the foundational story of Jensen Huang and NVIDIA, highlighting how the company began with a flawed technology approach before discovering the correct path through self-education.
*   Key topics include NVIDIA's origin story, the critical role of Jensen Huang's leadership and learning mindset, and the subsequent journey of inventing core technologies that shaped modern computing and AI.
*   It's a compelling case study in perseverance, adaptive learning, and visionary leadership, offering crucial lessons on overcoming early failures to build a transformative company.

### 🎬 黄仁勋：塑造NVIDIA的心态
**频道:** Y Combinator
*   本视频深入探讨了黄仁勋与NVIDIA的创业历程，揭示了公司如何从错误的技术方向起步，并通过自我学习找到了正确的道路。
*   主要话题涵盖NVIDIA的起源故事、黄仁勋领导力与学习心态的关键作用，以及随后发明核心技术、引领现代计算与人工智能发展的历程。
*   这是一个关于坚韧、适应性学习与远见领导的生动案例，为如何克服早期失败并构建具有变革性的公司提供了宝贵启示。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=I4B37S1dyQQ)**

### 🎬 Self-Maintaining APIs
**Channel:** Y Combinator
* What the video covers: This video addresses the persistent problem of managing API changes and breaking updates in software development. It critiques the current, flawed communication methods used by API providers and explores the concept of "self-maintaining APIs" as a potential solution.
* Key topics discussed:
    * The constant and disruptive nature of API updates.
    * The breakdown in communication between API providers and developers regarding breaking changes.
    * The introduction of a new paradigm for APIs that can autonomously handle their own maintenance and updates.
* Why it's worth watching: For developers, product managers, and tech leads, API management is a critical and often painful part of building and maintaining modern software. This video presents a forward-looking solution from a reputable source (Y Combinator) that could significantly reduce developer friction, improve system reliability, and change how we build with external services.

### 🎬 自维护API (Self-Maintaining APIs)
**频道:** Y Combinator (YC)
* 视频内容概述： 本视频探讨了软件开发中API变更和破坏性更新的持续性难题。它批判了API提供商目前使用的、有缺陷的沟通方式，并介绍“自维护API”作为一种潜在的解决方案。
* 主要话题：
    * API更新的频繁性及其带来的破坏性影响。
    * API提供商与开发者之间在破坏性变更通知上的沟通断裂。
    * 一种能自主处理自身维护和更新的全新API范式的提出。
* 为何值得观看： 对于开发者、产品经理和技术负责人而言，API管理是构建和维护现代软件时至关重要却常令人头疼的环节。本视频从权威来源（Y Combinator）提出了一个前瞻性解决方案，有望大幅减少开发者的工作摩擦、提升系统可靠性，并改变我们使用外部服务进行构建的方式。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=c3TxAUir2R8)**

### 🎬 How Anthropic builds products like Claude Code before the AI models are ready | Dianne Penn
**Channel:** Lenny's Podcast
*   **What the video covers:** The video features an interview with Dianne Penn, Anthropic's Head of Product for AI Research and Labs. It delves into Anthropic's unique methodology for developing products (like the coding assistant Claude Code) when the underlying AI models are still in a state of rapid evolution and not yet "production-ready."
*   **Key topics discussed:**
    *   The core philosophy of building products *ahead* of the model's final capabilities.
    *   Strategies for creating user value and feedback loops while the foundational model is still improving.
    *   The specific challenges and processes of shipping a product like Claude Code in such a dynamic environment.
    *   The collaboration between product teams and AI research teams at Anthropic.
*   **Why it's worth watching:** This interview provides a rare, inside look at the cutting-edge product development philosophy at a leading AI company. It's essential viewing for product managers, tech leaders, and AI enthusiasts interested in the practical realities of building real-world applications on top of rapidly advancing AI, offering valuable lessons on managing uncertainty and innovation.

### 🎬 Anthropic如何在模型成熟前构建Claude Code等产品 | Dianne Penn
**频道:** Lenny's Podcast
*   **视频内容概述:** 本视频采访了Anthropic AI研究与实验室团队的产品负责人Dianne Penn。深入探讨了Anthropic在底层AI模型仍处于快速演进、尚未“完全就绪”的状态下，开发产品（如编程助手Claude Code）的独特方法论。
*   **主要话题:**
    *   在模型最终能力成型*之前*就着手构建产品的核心理念。
    *   在基础模型持续改进的过程中，如何创造用户价值并建立反馈循环的策略。
    *   在如此动态的环境下，发布像Claude Code这类产品所面临的特定挑战与流程。
    *   Anthropic内部产品团队与AI研究团队之间的协作方式。
*   **为何值得观看:** 本次访谈深入揭示了一家顶尖AI公司前沿的产品开发理念。对于产品经理、技术领导者以及所有对如何在快速进步的AI技术之上构建实际应用感兴趣的爱好者而言，这都是一期必看内容，其中关于管理不确定性和推动创新的实践见解极具价值。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=tivaWTTVRhY)**

### 🎬 How to make a melon with an invisible head in Melon Sandbox #melonsanbox #shorts
**Channel:** Vedid
*   This is a quick, creative tutorial video (a YouTube Short) demonstrating a fun glitch or trick within the "Melon Sandbox" game.
*   It walks you through the specific steps to make a melon character's head disappear, showcasing an exploit or unexpected outcome of the game's physics engine.
*   It's worth watching for players of "Melon Sandbox" looking for entertaining, quirky things to do beyond normal gameplay. It highlights the game's sandbox potential for creative experimentation and is satisfying to see a weird trick executed quickly.

### 🎬 如何在瓜游乐园游戏中制作无头甜瓜 #melonsanbox #shorts
**频道:** Vedid
*   这是一个快速的创意教程视频（YouTube短视频），展示了在“瓜游乐园”游戏中的一种有趣故障或技巧。
*   它逐步指导你如何让甜瓜角色的头部消失，展示了游戏物理引擎的一个漏洞或意外效果。
*   对于“瓜游乐园”的玩家来说，它值得一看，因为它提供了超越正常游戏玩法的娱乐性、奇特玩法。它突出了游戏沙盒机制在创意实验方面的潜力，并且看到一个怪异技巧被快速执行的过程很有趣。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=WnAhgMRotr4)**

### 🎬 I Built an AI Agent That Day Trades Crypto Using Claude Code (Tutorial)
**Channel:** Austin Marcus
*   **What the video covers:** The video is a tutorial demonstrating how to build a fully functional cryptocurrency day trading bot powered by AI. The creator guides viewers through the process of using Claude, an AI model, to generate all the necessary code through "vibe coding," emphasizing that no traditional programming skills are required.
*   **Key topics discussed:**
    *   Leveraging AI (specifically Claude) for code generation.
    *   Concept of "vibe coding" to build applications via natural language prompts.
    *   Creating a practical application: a crypto trading bot.
    *   Steps to set up the agent for automated trading.
*   **Why it's worth watching:** It showcases the powerful and practical application of generative AI in software development. It's highly accessible to beginners or non-programmers interested in cryptocurrency or AI, as it demystifies building complex tools and highlights a new, approachable method for creation.

### 🎬 我用Claude Code构建了一个加密货币日交易AI代理（教程）
**频道:** Austin Marcus
*   **视频内容概述:** 本教程视频展示了如何构建一个由AI驱动的全功能加密货币日内交易机器人。创作者将带领观众了解如何使用Claude AI模型，通过“氛围编程”的方式生成所有必需的代码，并强调这个过程不需要任何传统的编程技能。
*   **主要话题:**
    *   利用AI（特别是Claude）进行代码生成。
    *   通过自然语言提示构建应用程序的“氛围编程”概念。
    *   创建一个实用应用：加密货币交易机器人。
    *   设置代理进行自动交易的步骤。
*   **为何值得观看:** 它展示了生成式AI在软件开发中强大而实际的应用。对于对加密货币或AI感兴趣的初学者或非程序员来说，它极具可及性，因为它揭开了构建复杂工具的神秘面纱，并突显了一种全新的、易于上手的创造方法。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=DkT6UzYX_UA)**

