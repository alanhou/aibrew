<!-- [Title-Only] -->
### Apple: Embarrassingly Simple Self-Distillation Improves Code Generation
* **Based on the title alone**, this article likely discusses a simple self-distillation method developed or studied by Apple that improves the performance of code-generating AI models. “Self-distillation” usually means a model is trained using outputs or signals derived from itself, often to refine quality without needing a much larger teacher model.
* It might be interesting to readers because code generation is a major practical use case for AI, and a method described as “embarrassingly simple” suggests the improvement could be easy to implement, efficient, and broadly useful for researchers and engineers working on LLM training or developer tools.

### 苹果：非常简单的自蒸馏方法可提升代码生成能力
* **仅根据标题推测**，这篇文章大概介绍了苹果提出或研究的一种非常简单的“自蒸馏”方法，并说明这种方法能够提升 AI 模型的代码生成效果。这里的“自蒸馏”通常指模型利用自身生成的输出或训练信号来进一步优化自己，而不一定依赖更大的教师模型。
* 它值得关注的原因在于，代码生成是当前 AI 很重要的应用方向之一，而“非常简单”意味着这种改进方法可能易于实现、成本较低，并且对从事大语言模型训练、代码助手或开发工具的人都有实际参考价值。

**[Read Original / 阅读原文](https://arxiv.org/abs/2604.01193)**

### CMS Isn’t Dead: AI Changes the Interface, Not the Need
* The article argues that AI-generated websites and modern JavaScript frameworks do not make CMS platforms like WordPress obsolete; many simple sites never needed a CMS, but CMSs still remain valuable for managing content, workflows, permissions, and long-term maintainability.
* The author warns that replacing WordPress with AI-built bespoke sites often shifts complexity rather than removing it, creating risks like dependency hell, vendor lock-in, fragile maintenance, and poorer usability for non-technical editors; instead, AI can be layered on top of CMS capabilities rather than replacing them.

### CMS 没死：AI 改变的是交互方式，不是需求本身
* 文章认为，AI 生成网站和现代 JavaScript 框架并没有让 WordPress 这类 CMS 过时；很多简单网站本来就不一定需要 CMS，但 CMS 在内容管理、工作流、权限控制以及长期维护方面仍然非常重要。
* 作者警告说，用 AI 构建的定制网站替代 WordPress，往往只是转移复杂性而不是消除复杂性，还会带来依赖地狱、供应商锁定、维护脆弱，以及对非技术编辑者不友好等问题；更合理的方向是把 AI 叠加到 CMS 之上，而不是取代 CMS。

**[Read Original / 阅读原文](https://next.jazzsequence.com/posts/the-cms-is-dead-long-live-the-cms)**

### Unusual Trees and Their Remarkable Traits
* The article shares the author’s fascination with unusual trees discovered while reading an old *Encyclopaedia Britannica*, moving from personal curiosity to a survey of extraordinary species.
* It highlights trees with surprising adaptations and records: mangroves protect coasts while spreading seaward; banyans expand through aerial roots and can cover acres; traveller’s trees store water; talipot palms flower once after decades and then die.
* Other examples emphasize extreme size, age, or rarity: the double coconut has enormous seeds, coast redwoods are the tallest trees, Australian mountain ash is the tallest flowering plant, bristlecone pine is among the oldest single trees, and Old Tjikko is ancient through its long-lived root system.

### 不寻常的树木及其惊人特征
* 这篇文章源于作者翻阅旧版《大英百科全书》时的阅读兴趣，介绍了一系列令人惊讶的特殊树种。
* 文中重点讲到许多树木的独特适应能力和反常特征：红树林一边向海扩展一边保护海岸；榕树通过气生根扩展，甚至能覆盖数英亩；旅人蕉能在叶基储水；董棕几十年只开花一次，结果后便死亡。
* 文章还介绍了多种在体型、寿命或稀有性上极端突出的树木：海椰子的种子巨大而罕见，海岸红杉是世界最高树种，澳洲山灰是最高的开花植物，刺果松是最古老的单体树木之一，而“老蒂科”则因其极其古老的根系而闻名。

**[Read Original / 阅读原文](https://thoughts.wyounas.com/p/some-unusual-trees)**


## 🔥 GitHub Trending / GitHub 热门项目

### mlx-vlm - MLX toolkit for running and fine-tuning vision-language models on Mac

* **What it does**
  * Enables inference and fine-tuning of vision-language and omni models on macOS using **MLX**.
  * Supports multimodal inputs including **text, images, audio**, and combinations like image+audio.
  * Provides multiple ways to use models: **CLI**, **Python API**, **Gradio chat UI**, and a **FastAPI server** with OpenAI-compatible endpoints.

* **Key features**
  * Broad support for many model families, including OCR, reasoning vision, multimodal, and omni models.
  * Built-in **multi-image chat**, **audio input**, and **thinking budget** controls for reasoning-style models.
  * Includes server mode with dynamic model loading/unloading, adapter support, and local API deployment.
  * Offers model-specific docs for prompt formats, examples, and best practices.
  * Mentions advanced optimization features like **TurboQuant KV Cache** and **activation quantization**.

* **Why it's notable**
  * It taps into the growing interest in running powerful multimodal AI models **locally on Apple hardware**.
  * The repo stands out by combining **developer tooling**, **interactive UI**, and **production-style API serving** in one package.
  * With **499 stars today**, it’s clearly trending as demand rises for practical, local-first VLM workflows on Mac.

### mlx-vlm - 基于 MLX 在 Mac 上运行与微调视觉语言模型的工具包

* **功能介绍**
  * 该项目用于在 macOS 上借助 **MLX** 对视觉语言模型（VLM）和 Omni 多模态模型进行**推理与微调**。
  * 支持 **文本、图片、音频** 等多种输入形式，也支持图片+音频的组合多模态场景。
  * 提供多种使用方式，包括 **命令行工具、Python 接口、Gradio 聊天界面** 以及 **FastAPI 服务端 API**。

* **主要特点**
  * 支持丰富的模型类型，涵盖 **OCR、视觉推理、多模态理解、Omni 模型** 等。
  * 内置 **多图片对话**、**音频输入**、以及面向推理模型的 **thinking budget（思考预算）** 控制。
  * 可作为服务端运行，支持**动态加载/卸载模型**、**适配器权重**，并提供 **兼容 OpenAI 风格的接口**。
  * 为多个具体模型提供独立文档，包含提示词格式、示例和最佳实践。
  * README 还提到 **TurboQuant KV Cache** 与 **激活量化** 等性能优化能力。

* **为何值得关注**
  * 该仓库切中了一个热门方向：在 **Apple 芯片/Mac 本地部署多模态 AI**。
  * 它不仅能做研究和实验，也兼顾了 **开发接入、交互界面、API 服务化部署**，实用性很强。
  * **今日新增 499 星**，说明它在本地化、多模态模型运行方案中正受到开发者广泛关注。

**[View Repository / 查看仓库](https://github.com/Blaizzy/mlx-vlm)**

### onyx - Open Source AI platform for chat, RAG, agents, and multi-LLM workflows
* **What it does**: Onyx is an open-source application layer for LLMs that provides a deployable AI chat platform with advanced capabilities like RAG, web search, code execution, deep research, file/artifact generation, and agent workflows.
* **Key features**:
  * Works with major LLM providers, including self-hosted and proprietary models.
  * Includes agentic RAG, deep research, custom agents, MCP/actions, web search, voice mode, image generation, and sandboxed code execution.
  * Offers 50+ connectors for indexing external knowledge sources.
  * Supports multiple deployment modes: lightweight **Lite** mode and full **Standard** mode, with Docker/Kubernetes/Helm/Terraform support.
  * Provides enterprise-ready capabilities such as SSO, RBAC, analytics, audit history, and whitelabeling.
* **Why it's notable**:
  * It positions itself as a full open-source AI platform rather than just a chat UI.
  * Broad compatibility with “every LLM” and rich built-in tooling make it attractive for teams building internal AI assistants.
  * The repo is trending strongly with **1,212 stars today**, suggesting high current interest from the open-source AI community.

### onyx - 面向聊天、RAG、智能体与多模型工作流的开源 AI 平台
* **功能介绍**：Onyx 是一个开源的 LLM 应用层平台，提供可自行部署的 AI 聊天系统，支持 RAG、网页搜索、代码执行、深度研究、文件/制品生成，以及智能体工作流等高级能力。
* **主要特点**：
  * 兼容主流大模型服务商，包括自托管模型和商业模型。
  * 内置 Agentic RAG、深度研究、自定义智能体、MCP/Actions、网页搜索、语音模式、图像生成和沙箱代码执行。
  * 提供 **50+** 外部知识源连接器，可用于索引和检索。
  * 支持多种部署方式：轻量级 **Lite** 模式与完整 **Standard** 模式，并兼容 Docker、Kubernetes、Helm、Terraform。
  * 面向企业场景提供 SSO、RBAC、分析统计、审计历史和白标定制等能力。
* **为何值得关注**：
  * 它不仅是聊天界面，而是一个较完整的开源 AI 应用平台。
  * 对多种 LLM 的广泛兼容，以及丰富的开箱即用功能，使其非常适合企业内部 AI 助手和知识检索场景。
  * 该仓库今日新增 **1,212** 星，说明它在当前开源 AI 领域具有很高的关注度与热度。

**[View Repository / 查看仓库](https://github.com/onyx-dot-app/onyx)**

### oh-my-codex - Workflow Layer for OpenAI Codex CLI

* **What it does**
  * Adds a structured productivity layer on top of OpenAI Codex CLI rather than replacing it.
  * Helps users run stronger coding sessions with reusable prompts, guided workflows, agent teams, and persistent project state stored in `.omx/`.
  * Supports a recommended flow from clarification to planning to execution using commands like `$deep-interview`, `$ralplan`, `$ralph`, and `$team`.

* **Key features**
  * Reusable workflow skills for clarifying requirements, approving plans, and executing tasks.
  * Multi-agent/team runtime with durable coordination via `tmux` or `psmux`.
  * Project guidance and memory through scoped `AGENTS.md` plus persistent logs, plans, and runtime state in `.omx/`.
  * Operator tools like `omx setup`, `omx doctor`, `omx hud`, `explore`, and `sparkshell`.
  * Broad documentation and multilingual README support.

* **Why it's notable**
  * It targets a hot category: improving the day-to-day developer experience around AI coding agents instead of building yet another standalone agent.
  * The project is highly practical, with a clear default workflow and runtime tooling for real coding sessions.
  * **1,803 stars today** suggests strong momentum and interest from developers using or experimenting with Codex-based workflows.

### oh-my-codex - 面向 OpenAI Codex CLI 的工作流增强层

* **功能介绍**
  * 这是一个构建在 OpenAI Codex CLI 之上的工作流增强工具，不是替代 Codex，而是让 Codex 更易用、更强大。
  * 它通过更好的提示词、流程编排、代理团队协作和 `.omx/` 持久化状态管理，提升日常开发体验。
  * 提供从需求澄清、方案制定到执行落地的一整套推荐流程，例如 `$deep-interview`、`$ralplan`、`$ralph` 和 `$team`。

* **主要特点**
  * 内置可复用技能，支持需求澄清、方案评审、持续执行等典型开发流程。
  * 支持多代理团队运行模式，可借助 `tmux` 或 `psmux` 进行持久化协作。
  * 通过 `AGENTS.md` 和 `.omx/` 保存项目规则、计划、日志、记忆与运行状态。
  * 提供 `omx setup`、`omx doctor`、`omx hud`、`explore`、`sparkshell` 等辅助工具。
  * 文档完整，并提供多语言 README。

* **为何值得关注**
  * 它切入的是当前非常热门的方向：不是重新造一个 AI 编程代理，而是增强现有 Codex 的工作流和运行时体验。
  * 项目定位清晰，默认流程明确，既适合个人使用，也适合更复杂的并行协作场景。
  * **今日新增 1,803 星**，说明它在开发者社区中传播速度快、关注度高，具备明显的趋势性。

**[View Repository / 查看仓库](https://github.com/Yeachan-Heo/oh-my-codex)**


## 🚀 Fast-Moving Repos / 快速崛起项目

### claw-code - Clean-room rewrite and Rust/Python port of an AI agent harness project

* **What it does**
  * Rebuilds the architecture of the original “Claw Code” as a clean-room implementation rather than hosting leaked source.
  * Provides a **Python-first workspace** for parity tracking and summaries, plus an in-progress **Rust port** intended to become the faster, memory-safe main version.
  * Includes CLI utilities, tool/command inventories, runtime orchestration pieces, and compatibility layers for editor integration.

* **Key features**
  * **Rust workspace** with modular crates for API client, runtime, tools, commands, plugins, compatibility harness, and interactive CLI.
  * **Python workspace** for manifest generation, subsystem modeling, parity audit, and verification tests.
  * **AI-assisted development workflow** using **oh-my-codex** and **oh-my-opencode** for scaffolding, orchestration, implementation, and verification.
  * Focus on **harness engineering**: tool wiring, session/runtime management, MCP orchestration, prompt construction, and plugin hooks.
  * Repository notice says the main repo is **temporarily locked during ownership transfer**, with maintenance continuing in a parity repo.

* **Why it's notable**
  * Extremely high visibility: the repo claims to be among the **fastest ever to hit major GitHub star milestones**, and it currently has **164k+ stars**.
  * It stands out as a **clean-room reimplementation** of a highly discussed AI coding/harness system, which makes it interesting both technically and legally/ethically.
  * The combination of **Rust migration**, modular agent tooling, and AI-assisted development has made it a trending project in the open-source AI tooling space.

### claw-code - 一个 AI Agent Harness 项目的洁净室重写与 Rust/Python 移植版

* **功能介绍**
  * 该项目并非继续保存泄露源码，而是以 **clean-room（洁净室）方式** 重写“Claw Code”的整体架构。
  * 当前以 **Python 工作区** 进行功能对齐与摘要生成，同时推进 **Rust 版本**，目标是成为更快、更安全的主实现。
  * 提供 CLI、工具与命令清单、运行时编排组件，以及面向编辑器集成的兼容层。

* **主要特点**
  * **Rust 模块化架构**：包含 API 客户端、运行时、工具系统、命令系统、插件框架、兼容 harness 和交互式 CLI。
  * **Python 工作区**：用于清单生成、子系统建模、功能对齐审计和测试验证。
  * 借助 **oh-my-codex** 与 **oh-my-opencode** 进行 AI 辅助开发，包括脚手架生成、编排、实现加速与验证。
  * 聚焦 **harness engineering（代理执行框架工程）**：如工具调用、会话管理、MCP 编排、Prompt 构造和插件 Hook 流程。
  * 仓库说明当前因 **所有权转移暂时锁定**，维护工作已转到另一个 parity 仓库继续进行。

* **为何值得关注**
  * 关注度极高：README 强调其曾以极快速度突破 GitHub 星标里程碑，目前已拥有 **16.4 万+ Stars**。
  * 它不是简单备份源码，而是一个围绕热门 AI 编码/代理系统展开的 **洁净室重构项目**，在技术和合规层面都很有话题性。
  * **Rust 重写 + 模块化 Agent 工具链 + AI 辅助工程流程** 的组合，使其成为近期开源 AI 工具领域里非常吸睛的项目。

**[View Repository / 查看仓库](https://github.com/ultraworkers/claw-code)**

### claude-code - Reconstructed, runnable TypeScript version of Claude Code CLI

* **What it does**
  * A reverse-engineered/recreated version of Anthropic’s Claude Code CLI, built to be runnable, buildable, and debuggable.
  * Lets users run the CLI locally with **Bun**, configure compatible third-party API platforms via `/login`, and use it without relying strictly on Anthropic’s official account flow.
  * Aims to restore and extend much of the original tool’s functionality and engineering workflow.

* **Key features**
  * **TypeScript fixes and engineering cleanup**: claims full type repair, build pipeline completion, and improved reliability.
  * **Cross-runtime support**: build outputs can run on both **Bun** and **Node**.
  * **Debug support**: includes inspect/attach workflow for VS Code debugging.
  * **Custom platform login**: supports Anthropic-compatible APIs, including OpenAI-compatible setups and other proxy/platform providers.
  * **Expanded feature set**: web search, remote control/bridge mode, voice mode, memory/dream commands, browser/computer-use integrations, and environment-variable-based feature flags.
  * **Enterprise-oriented additions**: custom Sentry reporting, GrowthBook integration, monitoring hooks, and disabled auto-update.

* **Why it’s notable**
  * **Highly starred and fast-moving**: over **13k stars** and positioned as an actively updated community-driven project.
  * **Unusual scope**: not just a clone, but a heavily engineered reconstruction with docs, tests, debugging, and deployment support.
  * **Appeals to power users**: especially notable for developers who want a hackable, self-hostable, or API-flexible Claude Code-like CLI experience.
  * **Trending factor**: combines a popular AI developer tool, reverse-engineering curiosity, and practical enhancements that lower usage barriers.

### claude-code - Claude Code CLI 的可运行 TypeScript 重建版

* **功能介绍**
  * 这是一个对 Anthropic 官方 **Claude Code CLI** 的源码进行反编译/逆向还原后的重建项目，目标是实现其大部分功能与工程化能力。
  * 用户可以通过 **Bun** 直接安装、运行、构建和调试，并通过 `/login` 接入第三方兼容 API 平台。
  * 项目不仅追求“能跑”，还强调可维护、可构建、可调试的完整开发体验。

* **主要特点**
  * **TypeScript 类型修复完整**：README 强调类型问题已大量修复，并补齐工程化设施。
  * **Bun / Node 双运行支持**：构建产物可在 Bun 和 Node 环境中启动。
  * **支持调试**：提供 Bun inspect + VS Code attach 的调试方案。
  * **自定义登录与平台兼容**：支持 Anthropic API 兼容服务，也支持 OpenAI 接口兼容配置。
  * **功能扩展丰富**：包括 web search、Bridge Mode、voice、dream 记忆整理、Chrome/computer use 等能力。
  * **企业级增强**：加入自定义 Sentry、GrowthBook、监控上报、关闭自动更新等特性。
  * **特性开关灵活**：全部通过环境变量控制 feature flags，方便开发和部署。

* **为何值得关注**
  * **热度高**：仓库已有 **13,341 Stars**，在 AI CLI / 开发工具类项目中非常吸睛。
  * **话题性强**：逆向还原 Claude Code 本身就很有讨论度，同时还加入了大量社区增强功能。
  * **实用性突出**：对希望自定义模型平台、替代官方接入方式、或深入调试 Claude Code 工作流的开发者很有吸引力。
  * **文档和迭代都很积极**：README 展示了清晰的版本路线、在线文档、测试补充和持续更新节奏，因此更容易形成社区关注。

**[View Repository / 查看仓库](https://github.com/claude-code-best/claude-code)**


## 🎬 YouTube Tech Videos / YouTube 技术视频

### 🎬 Why was the developer unhappy at their job...?
**Channel:** freeCodeCamp.org

* **What the video covers:** A short, joke-style tech video centered on the question of why a developer was unhappy at work, likely delivering a programming-related punchline.
* **Key topics discussed:** Developer humor, workplace frustration in tech, coding culture, and lighthearted programming jokes.
* **Why it's worth watching:** It's a quick, fun watch for developers and tech fans who enjoy relatable coding humor and a break from more serious programming content.

### 🎬 为什么开发者对自己的工作不开心……？
**频道:** freeCodeCamp.org

* **视频内容概述：** 这是一支偏段子/笑话风格的技术短视频，围绕“为什么开发者在工作中不开心”这个问题展开，可能会以程序员梗作为结尾。
* **主要话题：** 程序员幽默、技术职场烦恼、编码文化，以及轻松有趣的开发者笑话。
* **为何值得观看：** 适合想放松一下的开发者或科技爱好者观看，内容简短轻松，容易引发共鸣。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=gM2Ra8GpGuU)**

### 🎬 The cognitive cost of AI coding
**Channel:** Lenny's Podcast

* **What the video covers:** A discussion on the mental tradeoffs of using AI for programming—how AI coding tools can boost speed while potentially changing how developers think, learn, and solve problems.
* **Key topics discussed:** AI-assisted coding, cognitive load, developer skill development, overreliance on tools, productivity vs. understanding, and the broader impact of tools like Claude Code, OpenAI, and ChatGPT on software work.
* **Why it's worth watching:** Worth watching if you want a thoughtful take on the hidden costs—not just the benefits—of AI coding, especially for developers, founders, and tech leaders deciding how deeply to rely on these tools.

### 🎬 AI 编程的认知成本
**频道:** Lenny's Podcast

* **视频内容概述:** 探讨使用 AI 编程工具时带来的思维层面权衡：虽然 AI 能提升开发速度，但也可能改变程序员理解问题、学习知识与解决问题的方式。
* **主要话题:** AI 辅助编程、认知负担、开发者能力成长、对工具的过度依赖、效率与理解之间的平衡，以及 Claude Code、OpenAI、ChatGPT 等工具对软件开发工作的影响。
* **为何值得观看:** 如果你不仅关心 AI 编程带来的效率提升，也关心它对思考能力和长期技术成长的影响，这支视频很值得看，尤其适合开发者、创业者和技术管理者。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=Obk_fVOXZzM)**

### 🎬 Why Florence's Top Cop Was Always a Foreigner - Ada Palmer
**Channel:** Dwarkesh Patel

* **What the video covers:** Likely an interview or discussion with historian and author Ada Palmer about why Florence historically appointed an outsider as its chief law-enforcement official, and what that reveals about politics, power, and governance in Renaissance Italy.
* **Key topics discussed:** Florence’s political structure, the role of foreign officials in maintaining neutrality, factional conflict, civic institutions, and the broader logic of premodern statecraft.
* **Why it's worth watching:** If you enjoy history explained through sharp institutional questions, this looks valuable. The topic offers a fascinating lens on how societies tried to control corruption, local bias, and elite rivalry.

### 🎬 为什么佛罗伦萨的最高警务官总是外国人 - Ada Palmer
**频道:** Dwarkesh Patel

* **视频内容概述：** 这期视频很可能是与历史学家、作家 Ada Palmer 的一场访谈，讨论佛罗伦萨为何长期任命“外来者”担任最高警务或执法官员，以及这一制度反映出的文艺复兴时期意大利政治逻辑。
* **主要话题：** 佛罗伦萨的政治制度、任用外国官员以维持中立、派系斗争、市政治理，以及前现代国家如何处理腐败与权力制衡。
* **为何值得观看：** 如果你对历史、政治制度和文艺复兴城市治理感兴趣，这个选题非常有意思。它通过一个具体问题切入，更容易看懂复杂的权力运作机制。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=B37saIexYr4)**

### 🎬 Subscribe for more coding tips⬆️ Breakup😭 #funny #codingtips #comedyfilms #motivation #codeprep
**Channel:** Coding avani

* **What the video covers:** A short, comedic coding-themed clip that appears to mix breakup humor with coding motivation and quick coder-focused entertainment.
* **Key topics discussed:** Coding tips, comedy/skit-style presentation, motivation for learners, and lighthearted relatable programmer content.
* **Why it's worth watching:** It looks like a fun, fast watch for viewers who enjoy coding memes, humorous tech shorts, and motivational content aimed at aspiring programmers.

### 🎬 订阅获取更多编程技巧⬆️ 失恋😭 #funny #codingtips #comedyfilms #motivation #codeprep
**频道:** Coding avani

* **视频内容概述：** 这似乎是一支将“失恋”情节与编程元素结合的搞笑短视频，主打轻松娱乐和学习动力。
* **主要话题：** 编程技巧、喜剧式短片、学习编程的激励内容，以及程序员日常相关的轻松梗。
* **为何值得观看：** 如果你喜欢编程幽默、轻量级技术短视频，或想在轻松氛围中获得一点学习动力，这类视频会很适合。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=-w4A69iyuog)**

### 🎬 When You Hire a Free Intern #sheryians #shorts
**Channel:** Sheryians Coding School

* **What the video covers:** A short, humorous take on why simply watching tutorials doesn’t translate into real project-building skills.
* **Key topics discussed:** Tutorial dependency, the gap between theory and hands-on practice, and the importance of actually building projects to learn coding effectively.
* **Why it's worth watching:** It delivers a quick but relatable reminder for coding students: passive learning isn’t enough, and real growth comes from practical experience.

### 🎬 当你雇了一个免费实习生 #sheryians #shorts
**频道:** Sheryians Coding School

* **视频内容概述：** 这是一则简短又带点幽默感的视频，点出为什么很多人看了大量教程后，依然不会真正做项目。
* **主要话题：** 教程依赖、理论与实战之间的差距，以及通过亲手做项目来提升编程能力的重要性。
* **为何值得观看：** 内容短小直接、很有共鸣，特别适合正在学编程的人反思自己的学习方式。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=IWyLERVVp8c)**

