<!-- [Title-Only] -->
### AI's top startups are barely publishing their research
* Based on the title, this article likely investigates a trend where leading AI startup companies are choosing not to publish their scientific and technical research findings. It probably explores the reasons behind this shift away from the traditional academic openness in the field and analyzes the implications for the broader AI research community, transparency, and the pace of innovation.
* This topic is interesting as it highlights a potential tension between commercial secrecy and the spirit of open scientific collaboration that has historically fueled AI progress. It raises questions about the future of knowledge sharing, the role of academia, and the motivations of well-funded, competitive AI labs.

### 头部AI初创企业几乎不再公开发表其研究
* 根据标题推测，这篇文章可能探讨了一个趋势：领先的AI初创公司正选择不公开其科研与技术成果。文章很可能分析了这种转变背后的原因，及其对AI学术界、研究透明度和整体创新速度可能产生的影响。
* 该话题值得关注，因为它揭示了商业保密性与传统上推动AI进步的开放科学合作精神之间的潜在矛盾。这引发了关于未来知识共享模式、学术界的角色，以及那些资金雄厚、竞争激烈的AI实验室的动机的思考。

**[Read Original / 阅读原文](https://www.science.org/content/article/ai-s-top-startups-are-barely-publishing-their-research)**

### The Coolest Use for the Vision Pro: Home Design Visualization
*   The author discovered a transformative use case for the Vision Pro: **visualizing and walking through a 3D model of a future home**.
*   This solves the challenge of judging scale, layout, and feel from traditional 2D floor plans, especially when building a custom house.
*   The process involves creating a basic 3D model in software like Fusion 360, adding textures and furniture models (from IKEA and 3D Warehouse), and then exporting it as a USDZ file.
*   A custom-built **USDZ viewer app called "Prospector"** was developed for the Vision Pro, featuring controls for easy navigation, flying between floors, and toggling real-world visibility for safety.
*   This application provides a powerful, immersive way to understand a space, make design decisions, and collaborate with others before construction begins.

### Vision Pro 最酷的用途：家居设计可视化
*   作者发现了一个改变游戏规则的 Vision Pro 用例：**在虚拟现实中可视化并“行走”于未来房屋的3D模型中**。
*   这解决了从传统2D平面图难以判断空间尺度、布局和实际感受的痛点，对于定制房屋尤为有用。
*   整个流程包括在 Fusion 360 等软件中创建基础3D模型，添加纹理和家具模型（来自宜家和3D Warehouse），最后导出为 USDZ 文件。
*   作者为 Vision Pro 开发了一个名为 **“Prospector”的自定义 USDZ 查看器应用**，具备便捷导航控制、跨楼层飞行以及切换现实世界视图（以增强安全性）等功能。
*   这种应用提供了一种强大、沉浸式的方式来理解空间、做出设计决策，并在施工开始前与他人协作。

**[Read Original / 阅读原文](https://christianselig.com/2026/07/vision-pro-house/)**

### TurboFieldfare: Optimized Runtime for Large Language Models on Apple Silicon
* A specialized Swift + Metal runtime enabling the 26-billion-parameter Gemma 4 26B-A4B model to run with only about 2 GB of RAM on Apple Silicon Macs, including 8 GB models.
* Core innovation lies in keeping the shared model core and KV cache in memory while streaming only the required "expert" weights from SSD for each token, drastically reducing RAM usage.
* Provides a complete ecosystem: a native Mac app, command-line interface (CLI), and an OpenAI-compatible local server for model installation, interaction, and inference.
* Model is installed via a streaming repack process, taking up about 14.3 GB of storage, with performance benchmarks reaching 5.1-6.3 tok/s on an 8 GB M2 MacBook Air and 31-35 tok/s on a 24 GB M5 Pro.

### TurboFieldfare: 适用于 Apple Silicon 的大语言模型优化运行时
* 这是一个基于 Swift 和 Metal 的专用运行时，使拥有 260 亿参数的 Gemma 4 26B-A4B 模型能够在仅配备 8GB 内存的 Apple Silicon Mac 上运行，所需 RAM 约仅为 2 GB。
* 其核心创新在于将模型的共享核心与 KV 缓存常驻于内存中，同时仅为每个词元从 SSD 流式加载所需的“专家”权重，从而大幅降低内存占用。
* 提供完整的工具生态系统：包含原生 Mac 应用程序、命令行界面（CLI）和一个兼容 OpenAI 的本地服务器，用于模型安装、交互和推理。
* 模型通过流式重打包过程安装，占用约 14.3 GB 存储空间。基准测试显示，在 8GB 内存的 M2 MacBook Air 上解码速度为 5.1-6.3 词元/秒，在 24GB 内存的 M5 Pro 上可达 31-35 词元/秒。

**[Read Original / 阅读原文](https://github.com/drumih/turbo-fieldfare)**


## 🔥 GitHub Trending / GitHub 热门项目

### GeoLibre - A Lightweight, Cloud-Native GIS Platform
*   **What it does**: GeoLibre is a free and open-source Geographic Information System (GIS) designed for visualizing, exploring, and analyzing geospatial data directly in your browser, on desktops, mobile devices, and within Jupyter notebooks.
*   **Key features**:
    *   **Cloud-Native & Cross-Platform**: Runs everywhere via a single workspace—as a web app, native desktop app (Windows, macOS, Linux), Android app, and Jupyter extension. It is built with Tauri v2, React, and TypeScript.
    *   **Powerful Tech Stack**: Integrates MapLibre GL JS for mapping, deck.gl for visualization, and DuckDB-WASM Spatial for in-browser spatial analysis and SQL queries.
    *   **Local & Private**: Emphasizes keeping your data local and private.
    *   **Extensive Functionality**: Supports 3D Tiles, 3D city data, planetary basemaps (Moon, Mars, etc.), and hundreds of geoprocessing tools. It features a responsive UI adaptable to different screen sizes.
    *   **Rich Ecosystem**: Includes plugins, a project sharing platform, and integrations with Python/Conda for Jupyter use.
*   **Why it's notable**: It represents a significant trend towards powerful, accessible, and privacy-focused GIS tools. Its ability to deliver a full-featured GIS experience entirely within a web browser or as a lightweight cross-platform app, using modern web technologies, makes it a highly versatile and approachable option for both casual users and developers. The rapid accumulation of GitHub stars highlights strong community interest.

### GeoLibre - 轻量级云原生地理信息系统平台
*   **功能介绍**：GeoLibre 是一个免费开源的地理信息系统（GIS），专为在浏览器、桌面、移动设备以及 Jupyter Notebook 中直接可视化、探索和分析地理空间数据而设计。
*   **主要特点**：
    *   **云原生与跨平台**：通过单一工作区实现全平台运行——可作为网页应用、原生桌面应用（Windows、macOS、Linux）、安卓应用及 Jupyter 扩展。基于 Tauri v2、React 和 TypeScript 构建。
    *   **强大的技术栈**：整合了 MapLibre GL JS（地图渲染）、deck.gl（可视化）和 DuckDB-WASM Spatial（浏览器内空间分析与 SQL 查询）。
    *   **本地化与隐私保护**：强调将数据保留在本地，确保隐私安全。
    *   **丰富的功能**：支持 3D 瓦片、3D 城市数据、行星底图（月球、火星等）以及数百种地理处理工具。具有响应式用户界面，可适配不同屏幕尺寸。
    *   **丰富的生态系统**：包含插件、项目分享平台，并集成了 Python/Conda 以便在 Jupyter 中使用。
*   **为何值得关注**：GeoLibre 体现了向强大、易用且注重隐私的 GIS 工具发展的趋势。它利用现代网络技术，在浏览器中或作为轻量级跨平台应用提供功能完整的 GIS 体验，使其成为普通用户和开发者都极易上手的通用工具。其在 GitHub 上迅速积累的星标数也凸显了社区的高度兴趣。

**[View Repository / 查看仓库](https://github.com/opengeos/GeoLibre)**

### Project AIRI - Self-hosted AI Companion Emulating Neuro-sama
*   **What it does**: AIRI is a self-hosted, user-owned AI companion project aiming to recreate the capabilities of Neuro-sama. It functions as a "soul container" for AI virtual characters (waifu), enabling real-time voice chat and the ability to play games like Minecraft and Factorio.
*   **Key features**:
    *   Real-time voice conversation capabilities.
    *   Ability to play and interact within popular games (Minecraft, Factorio).
    *   Cross-platform support for Web, macOS, and Windows (including installation via winget, Scoop, and Homebrew Cask).
    *   Fully open-source and self-hosted, giving users complete control over their AI companion and data.
    *   Part of a larger ecosystem with sub-projects for RAG, memory systems, and Live2D utilities.
*   **Why it's notable**: It is rapidly trending (682 stars in a day) due to its ambitious goal of creating a proactive, game-playing AI companion beyond simple chat. Its open-source, self-hosted nature offers full ownership and customization, appealing to users concerned with privacy and control. The project's polish, evidenced by its multi-language README and easy installation methods, makes advanced AI interaction more accessible.

### Project AIRI - 自托管的 Neuro-sama 风格 AI 伴侣
*   **功能介绍**: AIRI 是一个自托管、用户完全拥有的 AI 伴侣项目，旨在复刻 Neuro-sama 的能力。它作为 AI 虚拟角色（waifu）的“灵魂容器”，支持实时语音聊天，并能游玩《我的世界》（Minecraft）和《异星工厂》（Factorio）等游戏。
*   **主要特点**:
    *   支持实时语音交互。
    *   具备在流行游戏中游玩和互动的能力。
    *   跨平台支持，涵盖 Web、macOS 和 Windows（可通过 winget、Scoop 和 Homebrew Cask 安装）。
    *   完全开源且自托管，用户对 AI 伴侣及其数据拥有完全控制权。
    *   是更广泛生态系统的一部分，包含 RAG、记忆系统、Live2D 工具等多个子项目。
*   **为何值得关注**: 该项目今日获得了 682 颗星，热度极高，因其超越了简单聊天的范畴，致力于创造一个能主动参与游戏互动的 AI 伴侣。其开源和自托管的特性提供了完全的自主权和隐私控制，吸引了重视数据主权的用户。项目文档完善（多语言README）且安装便捷，降低了用户接触和使用高级 AI 交互的门槛。

**[View Repository / 查看仓库](https://github.com/moeru-ai/airi)**

### ECC - Agent Performance Optimization System
*   **What it does**: ECC (Entity Coordination Core) is an open-source framework that transforms AI coding assistants (like Claude Code, Codex, Cursor) from simple code generators into coordinated engineering agents. It provides a pre-built system of skills, workflows, and memory to enforce a disciplined development process: `plan -> test -> implement -> review -> verify -> remember -> improve`.
*   **Key features**: Includes 67 specialized agents, 281 skills (covering TDD, security, docs, etc.), 94 commands, runtime hooks, persistent memory for continuous learning, configurable rules, and built-in security scanning via AgentShield. It emphasizes optimizing the context window while persisting crucial data.
*   **Why it's notable**: It is a trending and comprehensive solution for standardizing and optimizing the performance of AI-driven development. By installing once, developers equip their AI agents with a complete engineering methodology, moving beyond ad-hoc prompting. The project is MIT-licensed, has strong community and sponsor backing, and is designed for multi-harness compatibility.

### ECC - 智能体性能优化系统
*   **功能介绍**: ECC（实体协调核心）是一个开源框架，旨在将 Claude Code、Codex、Cursor 等 AI 编码助手从简单的代码生成器转变为协调的工程智能体。它提供了一套预先构建的技能、工作流和记忆系统，强制执行规范的开发流程：`规划 -> 测试 -> 实现 -> 审查 -> 验证 -> 记忆 -> 改进`。
*   **主要特点**: 包含 67 个专用智能体、281 项技能（覆盖测试驱动开发、安全、文档等）、94 个命令、运行时钩子、用于持续学习的持久记忆、可配置规则，以及通过 AgentShield 实现的内置安全扫描。其核心在于优化上下文窗口，同时持久化关键数据。
*   **为何值得关注**: 这是一个日益流行且全面的解决方案，用于标准化和优化 AI 驱动的开发性能。通过一次性安装，开发者就能为其 AI 智能体配备完整的工程方法论，从而超越临时性的提示。该项目采用 MIT 许可证，拥有强大的社区和赞助商支持，并设计为兼容多种 AI 开发工具。

**[View Repository / 查看仓库](https://github.com/affaan-m/ECC)**


## 🚀 Fast-Moving Repos / 快速崛起项目

### Kimi-K3 - Open Frontier Intelligence from Moonshot AI
* **What it does**: Kimi K3 is an open-weight, native multimodal agentic model with 2.8 trillion parameters. Designed for "frontier intelligence," it excels at long-horizon coding, complex knowledge work, and deep reasoning across massive codebases and documents.
* **Key features**:
    * **Massive Scale & Novel Architecture**: A 3T-class MoE model (104B activated parameters) built on Kimi Delta Attention (KDA) and Attention Residuals (AttnRes), claiming ~2.5x scaling efficiency improvement over its predecessor.
    * **Native Multimodality & Long Context**: Natively understands text, images, and video with a 1-million-token context window.
    * **Agentic Capabilities**: Sustains minimal human oversight for long engineering sessions, orchestrates terminal tools, and can handle end-to-end knowledge work from deep research to motion design.
    * **Open Weights**: The full model weights are released under the Kimi K3 License for research and innovation.
* **Why it's notable**: Kimi K3 is the **world's first open-source model in the 3T parameter class**, pushing the boundaries of what publicly available models can achieve. It demonstrates performance competitive with leading proprietary models (like GPT and Claude variants) on reasoning and coding benchmarks, making advanced frontier AI capabilities more accessible.

### Kimi-K3 - 月之暗面推出的前沿开源智能体
* **功能介绍**: Kimi K3 是由 Moonshot AI（月之暗面）开源的、原生多模态智能体模型，拥有2.8万亿参数。它专为“前沿智能”设计，擅长处理长周期编码任务、复杂的知识工作，并对超长代码库和文档进行深度推理。
* **主要特点**:
    * **巨大规模与新型架构**: 采用混合专家模型（MoE）架构，总参数2.8万亿，激活参数1040亿。基于自研的 Kimi Delta Attention (KDA) 和 Attention Residuals (AttnRes) 构建，声称整体缩放效率相比 Kimi K2 提升约2.5倍。
    * **原生多模态与超长上下文**: 原生支持文本、图像、视频理解，上下文窗口长达100万token。
    * **智能体能力**: 能够在极少人工干预下进行长时间工程会话，指挥终端工具，并能执行从深度研究到动态图形设计的端到端知识工作。
    * **开源权重**: 完整的模型权重已在 Kimi K3 许可证下开源，供研究和创新使用。
* **为何值得关注**: Kimi K3 是**全球首个开源的3万亿参数级别模型**，突破了开源模型的规模和能力边界。其在推理、编码等基准测试中的表现可与GPT、Claude等领先闭源模型相媲美，使得前沿的AI能力更加开放和可及，对学术研究和产业创新具有重要意义。

**[View Repository / 查看仓库](https://github.com/MoonshotAI/Kimi-K3)**

### mshumer/Claude-of-Duty - A Call of Duty-quality FPS built entirely from code with AI
*   **What it does:** A first-person shooter built in the browser using Three.js and WebGL2. Its core innovation is that it has **zero external art assets**; every texture, mesh, animation, and sound is generated procedurally at runtime from code.
*   **Key features:**
    *   **Procedural Everything:** 19 procedural surfaces (concrete, metal, wood, etc.), procedural geometry for weapons and world, and fully synthesized audio.
    *   **Advanced Rendering:** Features a complex HDR pipeline with effects like cascaded shadow maps, GTAO, TAA, motion blur, bloom, and procedural LUT.
    *   **Custom Physics Engine:** A from-scratch physics system with a high-performance BVH, capsule character controller, rigid bodies, ragdolls, and bullet penetration.
    *   **Full Game Systems:** Includes AI with navmesh pathing, a detailed world, multiple weapons with ballistics, a DOM-based HUD, and a complete audio system.
    *   **AI-Orchestrated Development:** The 55k+ line codebase was written by a fleet of AI agents following a strict architectural contract.
*   **Why it's notable:** It represents a groundbreaking experiment in **fully procedural, code-generated game development** pushed to an ambitious, near-AAA scope. While the author's honest assessment concludes it doesn't match a real Call of Duty, the project's technical achievement—building such a complex system without any art files using AI orchestration—is highly significant and a major reason for its visibility.

### mshumer/Claude-of-Duty - 一个完全由代码生成、使用AI协作构建的《使命召唤》级FPS游戏
*   **功能介绍：** 一款使用Three.js和WebGL2在浏览器中构建的第一人称射击游戏。其核心创新在于**完全没有任何外部美术资产**；所有的纹理、模型、动画和音效全部在运行时由代码程序化生成。
*   **主要特点：**
    *   **全面程序化生成：** 拥有19种程序化表面（如混凝土、金属、木材等）、武器和场景的程序化几何体，以及完全合成的音频。
    *   **高级渲染技术：** 采用复杂的HDR渲染管线，包含级联阴影贴图、GTAO、TAA、运动模糊、泛光、程序化LUT等效果。
    *   **自研物理引擎：** 从零开始构建的物理系统，包含高性能BVH、胶囊体角色控制器、刚体、布娃娃系统和子弹穿透。
    *   **完整游戏系统：** 包含带导航网格路径规划的AI、详细的游戏世界、多种具有弹道学的武器、基于DOM的HUD以及完整的音频系统。
    *   **AI协作开发：** 超过5.5万行代码由一个AI智能体团队在严格的架构约束下协作编写完成。
*   **为何值得关注：** 这是**完全程序化、代码生成游戏开发**的一次突破性实验，其规模宏大，接近3A级标准。尽管作者诚实地评估认为它尚未达到真实《使命召唤》的水平，但该项目在不依赖任何美术文件、利用AI协作来构建如此复杂系统方面所取得的技术成就具有重大意义，这也是其备受瞩目的主要原因。

**[View Repository / 查看仓库](https://github.com/mshumer/Claude-of-Duty)**


## 🎬 YouTube Tech Videos / YouTube 技术视频

### 🎬 How We Proved That Black Holes Exist
**Channel:** Dwarkesh Patel

*   What the video covers: This video features astrophysicist Adam Brown discussing the journey from theoretical prediction to experimental confirmation of black holes.
*   Key topics discussed: The history of black hole theory, key evidence such as gravitational waves and the Event Horizon Telescope's image of a black hole, and the scientific process of proving a cosmic phenomenon.
*   Why it's worth watching: It provides a clear and engaging explanation of one of the most profound discoveries in modern physics, breaking down complex concepts to show how we finally had proof of these enigmatic objects.

### 🎬 如何证明黑洞的存在——Adam Brown
**频道:** Dwarkesh Patel

*   视频内容概述：本视频邀请了天体物理学家Adam Brown，共同探讨黑洞如何从理论预测发展到被实验证实的历程。
*   主要话题：黑洞理论的发展史，包括引力波探测和事件视界望远镜拍摄的黑洞影像等关键证据，以及证明宇宙天体的科学方法论。
*   为何值得观看：该视频清晰而生动地阐释了现代物理学中最重大的发现之一，将复杂的科学概念简化，展示了人类是如何最终获得黑洞存在的确凿证据的。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=5a7KVZQExRc)**

### 🎬 Multi-GPU Kernels, Intelligence per Watt, Heterogeneous Inference, and More | YC Paper Club
**Channel:** Y Combinator
*   What the video covers
    A session from Y Combinator's Paper Club featuring researchers and builders presenting cutting-edge technical discussions on optimizing AI hardware and software efficiency.
*   Key topics discussed
    Multi-GPU kernel optimization, the metric of "intelligence per watt" for local AI models, and techniques for heterogeneous inference across different hardware types.
*   Why it's worth watching
    It provides deep technical insights into making AI more efficient and accessible, particularly relevant for developers and founders working on on-device or resource-constrained AI applications.

### 🎬 Multi-GPU Kernels, Intelligence per Watt, Heterogeneous Inference, and More | YC Paper Club
**频道:** Y Combinator
*   视频内容概述
    这是Y Combinator论文俱乐部的一场会议，研究人员和实践者就AI硬件和软件效率的前沿技术讨论进行了演讲。
*   主要话题
    多GPU内核优化、衡量本地AI模型的“每瓦特智能”指标，以及在不同硬件类型上进行异构推理的技术。
*   为何值得观看
    它提供了关于如何使AI更高效和更易获取的深刻技术见解，尤其适用于在设备端或资源受限环境中开发AI应用的开发者和创始人。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=n8dz2FX0_uY)**

### 🎬 Alexandr Wang: “This is a Once-in-a-Civilization Opportunity”
**Channel:** Y Combinator
*   **What the video covers:** Alexandr Wang, founder of Scale AI, offers reflective advice to his 18-year-old self, focusing on the crucial development of an "internal compass" to anticipate and navigate future technological and societal shifts, particularly in the age of AI.
*   **Key topics discussed:** Building foresight for the future, the transformative potential of artificial intelligence, personal growth strategies for founders, and understanding paradigm-shifting opportunities.
*   **Why it's worth watching:** Provides a unique, high-level perspective from a successful AI founder on how to think about and prepare for the immense changes ahead. It's less about tactical advice and more about cultivating the mindset required to lead in an era of unprecedented technological change.

### 🎬 Alexandr Wang: “This is a Once-in-a-Civilization Opportunity”
**频道:** Y Combinator
*   **视频内容概述：** Scale AI 创始人 Alexandr Wang 向18岁的自己分享了反思性建议，核心在于培养一种"内在指南针"，以预见和驾驭未来科技与社会的变革，尤其是在人工智能时代。
*   **主要话题：** 建立对未来的洞察力、人工智能的变革潜力、创始人的个人成长策略，以及理解范式转移级别的机遇。
*   **为何值得观看：** 观众可以从一位成功的AI创始人那里获得独特的高维视角，学习如何思考并准备迎接前方的巨大变革。其重点不在于具体战术，而在于培养在前所未有的技术变革时代所需领先的思维模式。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=sJ4VJWycX9M)**

### 🎬 How to make a melon with an invisible head in Melon Sandbox #melonsanbox #shorts
**Channel:** Vedid
* A quick tutorial demonstrating a specific trick or glitch within the "Melon Sandbox" physics simulation game.
* Key topics: Game mechanics, physics interactions, achieving a specific visual effect (the invisible head).
* Why it's worth watching: It's a concise guide for players interested in discovering unique tricks, glitches, or creative outcomes in the game.

### 🎬 Melon Sandbox 中如何制作无头甜瓜 #melonsanbox #shorts
**频道:** Vedid
* 一段快速教程，演示了在"甜瓜沙盒"物理模拟游戏中实现特定技巧或漏洞的方法。
* 主要话题：游戏机制、物理交互、达成特定视觉效果（无头状态）。
* 为何值得观看：对于希望在游戏中发现独特技巧、漏洞或创意结果的玩家来说，这是一份简洁的指南。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=WnAhgMRotr4)**

### 🎬 Python Full Course for Beginners
**Channel:** Apna College**
*   This is a comprehensive, beginner-friendly Python programming course designed to take you from zero knowledge to a solid foundation.
*   Key topics likely include Python fundamentals, data types, control structures, functions, object-oriented programming (OOP), file handling, and possibly an introduction to libraries.
*   It's worth watching because it's offered by a popular educational channel focused on tech placements, making it a practical choice for those aiming for a career in programming. The video is newly published (2026).

### 🎬 Python 零基础完整教程
**频道:** Apna College
*   这是一个面向零基础学习者的全面Python编程课程，旨在带你从零开始掌握Python编程的坚实基础。
*   主要话题预计包括Python基础语法、数据类型、流程控制、函数、面向对象编程（OOP）、文件处理，以及可能涉及常用库的入门介绍。
*   该视频值得关注，因为它来自一个以科技就业为导向的知名教育频道，非常适合那些希望以此为基础进入编程领域的人。视频刚刚发布（2026年）。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=q3AuP01daL4)**

### VPNs as Lawful Technical Tools: EU Court Ruling

*   The Court of Justice of the European Union (CJEU) ruled that publishers and VPN providers are not liable for copyright infringement caused by users bypassing geo-blocked content.
*   The court stated that geo-blocking is the copyright holder's responsibility, not that of the VPN provider.
*   This landmark ruling establishes VPNs as lawful technical tools and could set a precedent for other jurisdictions like the UK.

### 欧洲法院关于版权的里程碑式裁决：VPN是合法的技术工具

*   欧盟法院裁定，发布者和VPN提供商对用户绕过地理封锁访问版权内容所导致的侵权行为不承担责任。
*   法院指出，地理封锁是版权所有者的问题，而非VPN提供商的责任。
*   这一里程碑式的裁决确立了VPN作为合法技术工具的地位，并可能为英国等其他司法管辖区设定先例。

**[Read Original / 阅读原文](https://remysharp.com/links/2026-07-23-35890312)**

### OpenJDK Interim Policy on Generative AI

*   The OpenJDK Community has adopted an interim policy restricting the use of generative AI (like large language models) for creating contributions (code, text, images) due to risks to reviewer workload, project security, and intellectual property.
*   The policy prohibits contributing content that is generated in part or in full by generative AI tools to OpenJDK repositories, pull requests, emails, wikis, or issues.
*   Contributors are permitted to use generative AI tools privately to help comprehend, debug, review code, and conduct research, as long as the generated content is not contributed.
*   Key risks cited include increasing reviewer burden with plausible but incorrect code, jeopardizing the security of the critical Java Platform, and potential copyright/IP violations under the Oracle Contributor Agreement (OCA).
*   Future enforcement will involve a new checkbox in GitHub pull requests via Skara, requiring contributors to affirm compliance with the policy.

### OpenJDK 对生成式 AI 的临时政策

*   由于对审查工作量、项目安全和知识产权构成风险，OpenJDK 社区通过了一项临时政策，限制使用生成式 AI（如大型语言模型）来创建贡献内容（代码、文本、图像）。
*   该政策禁止将全部或部分由生成式 AI 工具生成的内容贡献到 OpenJDK 的代码库、拉取请求、电子邮件、维基或问题追踪系统中。
*   贡献者可以私下使用生成式 AI 工具来帮助理解、调试、审查代码和进行研究，前提是不将此类工具生成的内容作为贡献提交。
*   引用的主要风险包括：看似合理但错误的代码会增加审查员负担、危及关键 Java 平台的安全性，以及在 Oracle 贡献者协议（OCA）下可能侵犯版权/知识产权。
*   未来的执行措施将包括通过 Skara 在 GitHub 拉取请求中添加一个新复选框，要求贡献者确认其贡献符合该政策。

**[Read Original / 阅读原文](https://openjdk.org/legal/ai)**

### RFC 8890 - The Internet is for End Users: Analysis

*   **Core Issue & Context:** The Internet Architecture Board (IAB) published RFC 8890 to explicitly guide the Internet Engineering Task Force (IETF) in prioritizing the interests of end-users (actual people) when making standards decisions, acknowledging that technical choices often have political and societal consequences.
*   **IETF's Process & Challenge:** The IETF operates on "rough consensus and running code," valuing technical merit. However, the RFC argues this model is insufficient in a world where protocol designs inherently affect power, privacy, and freedom, making decisions politically laden regardless of intent.
*   **Principle-Driven Governance:** The article posits that to maintain legitimacy, the IETF must move beyond pure technical arguments and document explicit principles (like the end-to-end principle and the stance against pervasive monitoring) to navigate conflicts between stakeholders (e.g., privacy vs. network management).
*   **A Call for Principled Stance:** RFC 8890 is presented not as a radical takeover by the IETF, but as a necessary clarification of its existing role as a guardian of Internet health. It asks the community to consciously favor the public good and end-user welfare when faced with trade-offs, thereby strengthening the Internet's foundational values.

### RFC 8890 - 互联网为终端用户而生：分析

*   **核心议题与背景：** 互联网架构委员会（IAB）发布 RFC 8890，旨在明确指导互联网工程任务组（IETF），要求其在制定标准决策时优先考虑终端用户（即实际的人）的利益，承认技术选择通常伴随着政治和社会后果。
*   **IETF的流程与挑战：** IETF 以“粗略共识和可运行代码”为原则运作，重视技术优势。然而，该文章认为，在当今世界，协议设计本质上会影响权力、隐私和自由，这使得决策不可避免地带有政治色彩，因此该模式存在不足。
*   **原则驱动的治理：** 文章指出，为维持其决策的合法性，IETF 必须超越纯粹的技术论证，记录明确的原则（如端到端原则和反对无处不在监控的立场），以应对利益相关方之间的冲突（例如，隐私与网络管理的权衡）。
*   **对有原则立场的呼吁：** RFC 8890 被阐述为并非 IETF 的激进夺权，而是对其现有角色（作为互联网健康守护者）的必要澄清。它要求社区在面临权衡取舍时，有意识地倾向于公共利益和终端用户的福祉，从而强化互联网的基础价值。

**[Read Original / 阅读原文](https://mnot.net/blog/2020/for_the_users)**

### huggingface/speech-to-speech - Build local voice agents with open-source models
*   **What it does**: Provides a low-latency, fully modular voice-agent pipeline (VAD -> STT -> LLM -> TTS) with an OpenAI Realtime-compatible WebSocket API, enabling the creation of local or cloud-based voice interaction systems using a mix of open-source and proprietary models.
*   **Key features**:
    *   **Fully Modular**: Every component (VAD, STT, LLM, TTS) is swappable via CLI flags, supporting numerous backends like Parakeet, Whisper, Qwen3-TTS, Kokoro, and OpenAI APIs.
    *   **OpenAI Compatible**: The LLM backend speaks OpenAI-compatible protocols, allowing seamless switching between hosted providers, Hugging Face Inference, or self-hosted servers (vLLM, llama.cpp).
    *   **Production-Ready**: Powers the conversation backend for thousands of Reachy Mini robots.
    *   **Multi-Platform**: Supports deployment on various hardware including NVIDIA CUDA, Apple Silicon (MPS/MLX), and CPU-only setups.
    *   **Flexible Run Modes**: Offers `realtime` (WebSocket API), `local` (mic/speaker), `websocket`, and `socket` modes for different integration needs.
*   **Why it's notable**: It simplifies building advanced voice agents by providing a production-tested, flexible, and open-source stack that avoids vendor lock-in. The ability to run the entire pipeline locally with open models is a significant advantage for privacy and customization, driving its trend as a practical solution for real-world voice AI applications.

### huggingface/speech-to-speech - 使用开源模型构建语音智能体
*   **功能介绍**：一个低延迟、完全模块化的语音智能体管道（语音活动检测 -> 语音转文本 -> 大语言模型 -> 文本转语音），通过兼容 OpenAI Realtime 协议的 WebSocket API 对外提供服务，支持使用开源模型与商业 API 混合构建本地或云端语音交互系统。
*   **主要特点**：
    *   **完全模块化**：每个组件（VAD、STT、LLM、TTS）均可通过命令行参数自由切换，支持 Parakeet、Whisper、Qwen3-TTS、Kokoro 及 OpenAI API 等众多后端。
    *   **OpenAI 兼容**：LLM 后端兼容 OpenAI 协议，可无缝切换至托管服务商、Hugging Face 推理服务或自建服务器（vLLM、llama.cpp）。
    *   **生产就绪**：已作为对话后端在数千台 Reachy Mini 机器人上运行。
    *   **跨平台支持**：可在 NVIDIA CUDA、Apple Silicon (MPS/MLX) 及纯 CPU 等多种硬件上部署。
    *   **灵活运行模式**：提供 `realtime`（WebSocket API）、`local`（本机麦克风/扬声器）、`websocket` 和 `socket` 模式，满足不同集成需求。
*   **为何值得关注**：该项目通过提供一个经过生产验证、灵活且开源的语音 AI 技术栈，极大地简化了高级语音智能体的构建过程。其支持全本地开源模型运行的能力，在隐私保护与定制化方面优势显著，使其成为当前语音 AI 应用领域一个切实可行的热门解决方案。

**[View Repository / 查看仓库](https://github.com/huggingface/speech-to-speech)**

### **Microsoft/AI-For-Beginners** - Microsoft's Official 12-Week, 24-Lesson AI Curriculum
* **What it does**: Provides a comprehensive, beginner-friendly curriculum for learning Artificial Intelligence, structured as a 12-week course with 24 lessons. It covers core AI topics from symbolic AI and knowledge representation to modern neural networks and deep learning.
* **Key features**: Features practical Jupyter Notebook-based lessons, quizzes, and lab exercises. It supports TensorFlow and PyTorch, offers extensive multi-language translation (50+ languages), and includes a supportive community via Discord.
* **Why it's notable**: As an official Microsoft project, it is a high-quality, well-structured, and widely accessible open-source resource for AI education. Its rapid star growth (115 stars today) reflects strong community interest and its value as a definitive learning path for AI beginners globally.

### **Microsoft/AI-For-Beginners** - 微软官方12周24课人工智能入门课程
* **功能介绍**：提供了一套全面、适合初学者的人工智能学习课程体系，结构化为12周、24课时的学习路径。内容涵盖从符号AI、知识表示到现代神经网络与深度学习等核心AI主题。
* **主要特点**：课程包含基于Jupyter Notebook的实践课程、测验与实验室练习。支持TensorFlow和PyTorch两大主流框架，提供超过50种语言的广泛翻译，并通过Discord提供活跃的社区支持。
* **为何值得关注**：作为微软官方项目，它是一个高质量、结构清晰且高度易得的开源AI教育资源。其快速增长的星标数（今日新增115星）反映了社区的强烈兴趣，使其成为全球AI初学者公认的权威学习路径之一。

**[View Repository / 查看仓库](https://github.com/microsoft/AI-For-Beginners)**

### Awesome Systematic Trading - A Curated Resource Hub for Quantitative Trading
* What it does: This repository is a comprehensive, community-curated list of resources for systematic (quantitative) trading. It aggregates tools, knowledge, and strategies across the entire workflow.
* Key features: It provides a structured index of 97+ Python libraries and packages (for backtesting, data, ML, etc.), 40+ described trading strategies, 55 books, 23 videos, blogs, and courses. Resources are categorized for easy navigation.
* Why it's notable: It has gained significant traction (628 stars in one day) due to its breadth and quality. It serves as a one-stop "awesome list" for both beginners and professionals in quant trading, linking to an ecosystem of open-source code and educational material.

### Awesome Systematic Trading - 量化交易资源的精选集合
* 功能介绍：这是一个全面的、由社区维护的系统化（量化）交易资源清单。它汇集了贯穿整个量化交易工作流程的工具、知识和策略。
* 主要特点：它提供了97+个Python库和包的结构化索引（涵盖回测、数据、机器学习等），40+个详细描述的交易策略，55本书籍，23个视频，以及博客和课程。资源分类清晰，便于查找。
* 为何值得关注：该仓库在一天内获得了628颗星，因其内容的广度和质量而备受瞩目。它成为量化交易新手和专业人士的一站式“awesome列表”，连接了一个庞大的开源代码和教育资源生态系统。

**[View Repository / 查看仓库](https://github.com/paperswithbacktest/awesome-systematic-trading)**

### 🎬 Project-based learning is a popular way to teach these days
**Channel:** freeCodeCamp.org
*   The video features an interview with educator Mark, who discusses his project-based learning approach with freeCodeCamp founder Quincy Larson.
*   It explores Mark's teaching methods, how he structures projects for his students, and the practical implementation of this educational philosophy.
*   It provides valuable insights for educators, students, and anyone interested in alternative, hands-on approaches to teaching and learning technical skills.

### 🎬 Project-based learning is a popular way to teach these days
**频道:** freeCodeCamp.org
*   视频内容概述：视频中，教育者 Mark 与 freeCodeCamp 创始人 Quincy Larson 进行了访谈，深入探讨了 Mark 所采用的项目制学习方法。
*   主要话题：讨论涵盖了 Mark 的具体教学方法、他如何为学生设计和组织项目，以及这种教育理念的实际应用。
*   为何值得观看：对于教育工作者、学生，以及任何对动手实践型教学和技术技能培训新方法感兴趣的观众来说，本视频提供了宝贵的经验和见解。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=YHQWuLG78Hw)**

### 🎬 How We Proved That Black Holes Exist - Adam Brown
**Channel:** Dwarkesh Patel

*   What the video covers: This video features an in-depth conversation with physicist Adam Brown exploring the historical and scientific journey toward proving the existence of black holes. It likely delves into the theoretical foundations laid by general relativity and the crucial observational evidence that confirmed these objects are real, not just mathematical constructs.
*   Key topics discussed: The evolution of black hole theory, pivotal observational breakthroughs (like the Event Horizon Telescope image), the interplay between theory and experiment in astrophysics, and the implications of black holes for our understanding of gravity and the universe.
*   Why it's worth watching: It offers a compelling, expert-driven narrative on one of the most profound discoveries in modern physics. The video promises to make complex scientific concepts accessible, highlighting the clever methodology and perseverance required to confirm the existence of these cosmic phenomena.

### 🎬 我们如何证明黑洞存在 - Adam Brown
**频道:** Dwarkesh Patel

*   视频内容概述：本视频深入探讨了物理学家Adam Brown解释人类如何证明黑洞真实存在的历程。内容涵盖从广义相对论的理论预测到关键的天文观测证据，讲述了这一科学确认的完整故事。
*   主要话题：黑洞理论的发展历史、决定性观测技术的突破（如事件视界望远镜成像）、理论与观测天体物理学的结合，以及黑洞发现对我们理解引力和宇宙的深刻影响。
*   为何值得观看：该视频通过权威专家的讲解，将复杂的理论物理概念娓娓道来，清晰展示了从假说到证实的科学探究过程。它是了解这一现代物理学重大里程碑的绝佳资源，兼具教育性与启发性。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=5a7KVZQExRc)**

### 🎬 Multi-GPU Kernels, Intelligence per Watt, Heterogeneous Inference, and More | YC Paper Club
**Channel:** Y Combinator
*   The video features presentations and discussions from the latest YC Paper Club, focusing on cutting-edge research and practical techniques for optimizing machine learning systems.
*   Key topics include optimization techniques for multi-GPU kernels, the emerging concept of "intelligence per watt" for evaluating the efficiency of local and edge AI models, and strategies for implementing heterogeneous inference.
*   It's worth watching for a concise, builder-focused update on key performance and efficiency frontiers in AI infrastructure, offering practical insights from researchers and developers.

### 🎬 多GPU内核优化、每瓦智能、异构推理等 | YC 论文俱乐部
**频道:** Y Combinator
*   本视频汇集了最新一期YC论文俱乐部的演讲与讨论，核心聚焦于机器学习系统的前沿研究与实用优化技术。
*   主要话题包括：多GPU内核的优化方法、用于评估本地及边缘AI模型效率的新概念“每瓦智能”，以及异构推理的实现策略。
*   值得观看的原因在于，它为开发者和研究者提供了一个关于AI基础设施性能与能效前沿的、高度实用的更新，内容精炼且极具前瞻性。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=n8dz2FX0_uY)**

### 🎬 Python Full Course for Beginners
**Channel:** Apna College

*   What the video covers
    This video is a complete, end-to-end beginner's course for the Python programming language. It is designed to take you from absolute zero knowledge to being proficient in core Python concepts, making you ready for programming and placements.

*   Key topics discussed
    The course likely covers fundamental topics such as: Python syntax, variables, data types, operators, control flow (if-else, loops), functions, data structures (lists, tuples, dictionaries), object-oriented programming (OOP), file handling, and potentially introductory libraries.

*   Why it's worth watching
    It's a valuable resource for anyone starting their programming journey in Python. The "placement-ready" focus from Apna College suggests a practical, job-oriented approach. It provides a solid, structured foundation in a single video, which is ideal for learners who prefer comprehensive, linear tutorials.

### 🎬 Python 完全初学者教程
**频道:** Apna College

*   视频内容概述
    该视频是一套完整、从零开始的 Python 编程语言入门课程。旨在帮助你从无任何编程基础到熟练掌握 Python 核心概念，为编程学习和求职面试做好准备。

*   主要话题
    课程可能涵盖以下核心主题：Python 基础语法、变量、数据类型、运算符、流程控制（if-else、循环）、函数、数据结构（列表、元组、字典）、面向对象编程（OOP）、文件处理，以及可能的入门级库介绍。

*   为何值得观看
    对于任何开始 Python 编程学习之旅的人来说，这都是一个宝贵资源。Apna College 的“就业导向”特点表明其注重实践和应用。它以单个视频的形式提供了坚实、结构化的知识基础，非常适合喜欢全面、线性教程的学习者。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=q3AuP01daL4)**

### 🎬 KIMI K3 ✨ TUTORIAL per fare VIBE CODING con AI
**Channel:** Andrea Ciraolo
*   **What the video covers:** This video is a tutorial on using the KIMI K3, a powerful Chinese AI model, for "Vibe Coding" – a concept of using AI to assist and streamline the coding process.
*   **Key topics discussed:** It introduces the KIMI AI platform, explains its capabilities (comparable to leading AI models), and likely demonstrates how to use it effectively for coding tasks, project building, or development workflows.
*   **Why it's worth watching:** It offers a practical guide to leveraging a potentially under-the-radar but powerful AI tool for software development. It's valuable for developers and tech enthusiasts looking to enhance their productivity with AI-driven coding assistants.

### 🎬 KIMI K3 ✨ AI编程辅助教程
**频道:** Andrea Ciraolo
*   **视频内容概述:** 本视频是一份关于如何使用强大的中国AI模型KIMI K3进行“Vibe Coding”的教程，旨在展示如何利用AI来辅助和优化编程流程。
*   **主要话题:** 介绍了KIMI AI平台，阐述了其强大的功能（可与顶级AI模型媲美），并可能演示了如何将其高效地应用于编码任务、项目构建或开发工作流中。
*   **为何值得观看:** 该视频为开发者和科技爱好者提供了一份实用的指南，教你如何运用这款强大但可能尚未被广泛熟知的AI工具来提升软件开发效率，是探索AI辅助编程的绝佳入门资源。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=-RzPQSS3Bhw)**

