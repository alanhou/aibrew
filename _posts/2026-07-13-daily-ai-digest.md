### English Summary
* Anthropic promotes the narrative that AI will replace coding and software engineering, influencing business decisions based on fear among executives and investors.
* The Bun project, acquired by Anthropic, rewrote from Zig to Rust using AI agents, criticized by Zig's creator Andrew Kelley as poor engineering and overreliance on AI.
* The author defends Kelley's blunt response as necessary to counter Anthropic's unreliable marketing, emphasizing skepticism in technical decisions.
* The rewrite process is technically interesting, but the rationale is seen as fluff, with suspected business and marketing motives.

### 中文摘要
* Anthropic 宣扬 AI 将取代编码和软件工程的叙事，基于恐惧影响高管和投资者的商业决策。
* Bun 项目被 Anthropic 收购后，使用 AI 代理从 Zig 重写为 Rust，被 Zig 创始人 Andrew Kelley 批评为糟糕的工程和过度依赖 AI。
* 作者支持 Kelley 的直率回应，认为这对反驳 Anthropic 不可靠的营销是必要的，强调技术决策中的怀疑态度。
* 重写过程在技术上有趣，但理由被视为浮夸，怀疑有商业和营销动机。

**[Read Original / 阅读原文](https://raymyers.org/post/zed-creator-calls-spade-a-spade/)**

### Another Ridiculous Interrail Holiday: Insights from a 6,379 Km, 13-Country Trip
*   The author and his wife undertook a 7-week Interrail trip covering 6,379 km across 13 countries, using a 15-travel-day pass as a less intense alternative to their previous month-long adventure.
*   The blog details practical experiences, including train delays, construction issues, lounge access inconsistencies, and the complexities of the Interrail refund process.
*   It provides a country-by-country account of train services, noting differences in first-class amenities, food options (especially for vegans), staff interactions, and journey comforts.
*   Highlights include scenic routes, a beautiful overnight ferry with entertainment, and efficient train changes, contrasted with challenges like poor air conditioning, timezone mix-ups, and confusing booking systems.

### 一次荒诞的Interrail假期：6,379公里与13国七周之旅的实用经验
*   作者夫妇进行了一次为期七周的Interrail铁路通票旅行，途经13个国家，总里程6,379公里。他们选择了15天/2个月的套餐，认为比上次的30天全月通票压力更小。
*   博文详述了旅途中的实际问题，如列车延误、施工影响、休息室使用权不一以及繁琐的Interrail退款流程。
*   内容按国家梳理了火车服务，对比了不同国家一等座的设施、餐食（特别是素食选择）、列车员态度及乘坐舒适度。
*   旅行亮点包括风景优美的线路、提供精彩演出的过夜渡轮以及顺畅的换乘，同时也记录了空调失效、时区搞错、订票系统混乱等挑战。

**[Read Original / 阅读原文](https://shkspr.mobi/blog/2026/07/another-ridiculous-interrail-holiday-6379km-and-13-countries-over-7-weeks/)**

### GhostLock: A 15-Year-Old Stack-UAF in Linux

*   **Vulnerability Overview:** GhostLock (CVE-2026-43499) is a privilege escalation and container escape vulnerability found in the Linux kernel. It was introduced in version 2.6.39 (2011) and fixed in version 7.1, affecting all major distributions for over 15 years.
*   **Impact & Trigger:** An unprivileged local user can trigger the bug without special kernel configuration. It was turned into a 97% stable exploit, earning a $92,337 reward from Google's kernelCTF.
*   **Technical Mechanism:** The flaw is a use-after-free on a kernel stack object (`rt_mutex_waiter`). It is triggered by creating a dependency cycle with three futexes, leading to a dangling `pi_blocked_on` pointer. This pointer can later be hijacked to gain control flow and root access.

### GhostLock：一个存在于所有Linux发行版长达15年的栈UAF漏洞

*   **漏洞概述：** GhostLock（CVE-2026-43499）是一个被发现于Linux内核中的提权与容器逃逸漏洞。它于版本2.6.39（2011年）引入，在版本7.1中修复，影响所有主流发行版超过15年。
*   **影响与触发：** 非特权本地用户可以在无需特殊内核配置的情况下触发此漏洞。该漏洞已被转化为一个成功率为97%的稳定提权利用，获得了Google漏洞赏金计划（kernelCTF）92,337美元的奖励。
*   **技术原理：** 该漏洞是内核栈对象（`rt_mutex_waiter`）的“释放后使用”错误。通过创建一个涉及三个futex的依赖环触发，导致一个悬垂的`pi_blocked_on`指针。该指针随后可被劫持，以控制程序流程并最终获取root权限。

**[Read Original / 阅读原文](https://nebusec.ai/research/ionstack-part-2/)**


## 🔥 GitHub Trending / GitHub 热门项目

### OpenCut - An open-source, cross-platform video editor alternative to CapCut
* What it does: OpenCut is a free and open-source video editor designed for the web, desktop, and mobile platforms. It aims to provide a powerful and accessible editing experience as an alternative to proprietary tools like CapCut.
* Key features: The project is undergoing a major rewrite featuring a plugin-first architecture, first-class third-party plugin support, a unified codebase (using a Rust core) for desktop, mobile, and browser versions, an MCP server for AI agents, headless mode for automation, and an integrated scripting tab.
* Why it's notable: It's gaining significant attention (over 1,000 stars today) as a promising, modern, open-source alternative in the video editing space. Its ambitious rewrite promises a highly extensible and developer-friendly platform, appealing to creators who value open-source tools and customization.

### OpenCut - 开源的、跨平台视频编辑工具，作为 CapCut 的替代品
* 功能介绍：OpenCut 是一个免费开源的视频编辑器，支持网页、桌面和移动端。其目标是提供一个强大且易于获取的编辑体验，作为 CapCut 等专有软件的替代方案。
* 主要特点：该项目正在经历一次彻底的重写，新架构的特点包括：插件优先设计、对第三方插件的一流支持、使用 Rust 核心实现桌面、移动端和浏览器的统一代码库、为 AI 智能体提供的 MCP 服务器、用于自动化和批处理渲染的无头模式，以及直接集成在编辑器中的脚本标签页。
* 为何值得关注：该项目因其作为视频编辑领域一个现代化、开放的替代选择而备受瞩目（今日获得超过 1000 颗星）。其雄心勃勃的重写计划预示着一个高度可扩展且对开发者友好的平台，吸引了重视开源工具和定制化的创作者们。

**[View Repository / 查看仓库](https://github.com/OpenCut-app/OpenCut)**

### destructive_command_guard - A high-performance hook for AI coding agents to block destructive commands.

*   **What it does**: It is a safety hook designed to intercept and block potentially catastrophic commands (like `git reset --hard`, `rm -rf`, or database `DROP TABLE`) before they are executed by AI coding agents (e.g., Claude, Codex, Copilot). It protects uncommitted work from accidental deletion.
*   **Key features**:
    *   **Zero-Config Protection**: Blocks common dangerous git and filesystem commands out of the box.
    *   **Extensive Security Packs**: Offers 50+ pre-configured rules for databases, Kubernetes, Docker, cloud providers (AWS/GCP/Azure), Terraform, and more.
    *   **High Performance**: Utilizes SIMD-accelerated filtering for sub-millisecond latency, ensuring it doesn't slow down workflows.
    *   **Smart Scanning**: Can detect dangerous commands inside heredocs and inline scripts (e.g., `python -c "..."`).
    *   **Rich Context-Aware Output**: Provides clear, human-readable block messages with reasons and safer alternative suggestions on stderr.
    *   **Broad Compatibility**: Natively supports or integrates with a vast ecosystem of AI tools including Claude Code, Codex CLI, Gemini CLI, GitHub Copilot, Cursor, and many others.
*   **Why it's notable**: It solves a critical pain point for developers using AI assistants—the risk of irreversible data loss from a single bad command. Its high performance, extensive rule set, deep integration with major AI tools, and intelligent "fail-open" design make it a robust and practical safeguard that's gaining rapid adoption (as evidenced by 444 stars in a day).

### destructive_command_guard - 用于阻止AI编程代理执行危险命令的高性能钩子。

*   **功能介绍**：这是一个安全钩子，旨在拦截并阻止AI编程代理（如Claude、Codex、Copilot）执行潜在的灾难性命令（如 `git reset --hard`、`rm -rf` 或数据库 `DROP TABLE`）。它保护未提交的工作免遭意外删除。
*   **主要特点**：
    *   **开箱即用的防护**：默认阻止常见的危险git和文件系统命令。
    *   **广泛的安全包**：提供50多个预配置规则，覆盖数据库、Kubernetes、Docker、云服务商（AWS/GCP/Azure）、Terraform等。
    *   **高性能**：采用SIMD加速过滤，实现亚毫秒级延迟，确保不会拖慢工作流程。
    *   **智能扫描**：能检测heredoc和内联脚本中的危险命令。
    *   **丰富的上下文输出**：在标准错误输出中提供清晰、人类可读的阻止信息、原因及更安全的替代方案建议。
    *   **广泛的兼容性**：原生支持或深度集成了众多AI工具，包括Claude Code、Codex CLI、Gemini CLI、GitHub Copilot、Cursor等。
*   **为何值得关注**：它解决了一个开发者在使用AI助手时的核心痛点——单条错误命令导致不可逆的数据损失风险。其高性能、丰富的规则库、与主流AI工具的深度集成以及智能的“故障开放”设计，使其成为一个 robust 且实用的防护工具，并获得了迅速的关注（一天内获得444颗星即为证明）。

**[View Repository / 查看仓库](https://github.com/Dicklesworthstone/destructive_command_guard)**

### HKUDS/Vibe-Trading - Your Personal Trading Agent
*   **What it does:** A comprehensive, agent-powered platform that provides an "all-in-one" solution for modern trading. It enables users to perform multi-asset backtesting, strategy research, data analysis, and even simulated or real trading with a single command.
*   **Key features:**
    *   **Multi-Asset & Multi-Source:** Supports backtesting for equities (including US, Indian NSE/BSE), crypto perpetuals, and futures, integrating data from various providers (yfinance, Tushare, etc.).
    *   **Advanced Strategy & Research Engine:** Includes a factor library, strategy optimization (with multiple optimizers), and an AI-driven "Strategy Development Manager" to convert research papers into tradable strategies.
    *   **Powerful Analytics & UI:** Features a React-based frontend with interactive charts, portfolio analysis, correlation tools, and a "Shadow Account" for risk-free strategy testing.
    *   **Extensible Agent Framework:** Built as a "trading agent" with a skill-based architecture, allowing for customizable trading behaviors, integration with IM channels (Discord, etc.), and LLM-powered analysis.
    *   **Security & Safety:** Emphasizes security with sandboxed backtesting, a Docker-hardened deployment, and built-in safeguards for real-trading operations.
    *   **Active & Open Development:** Features rapid updates, a growing contributor base, and a clear focus on community-driven improvements and new asset support.
*   **Why it's notable:** It stands out as a **unified, developer-friendly, and rapidly evolving** toolkit that significantly lowers the barrier to entry for implementing sophisticated quantitative and algorithmic trading strategies. Its combination of a full-stack application, a vast feature set (from data loading to portfolio optimization), and strong community momentum makes it a trending choice for both learning and practical application in algorithmic trading.

### HKUDS/Vibe-Trading - 你的个人交易代理
*   **功能介绍:** 一个由代理驱动的综合平台，为现代交易提供了“一体化”解决方案。用户只需一条命令，即可执行多资产回测、策略研究、数据分析，甚至进行模拟或真实交易。
*   **主要特点:**
    *   **多资产与多数据源:** 支持股票（包括美股、印度NSE/BSE股市）、加密货币永续合约和期货的回测，整合了来自多种数据提供商的信息。
    *   **先进的策略与研究引擎:** 内置因子库、多种投资组合优化器，以及由AI驱动的“策略开发管理器”，可将学术论文转化为可交易的策略。
    *   **强大的分析与用户界面:** 提供基于React的前端，包含交互式图表、投资组合分析、相关性分析工具，以及用于零风险测试策略的“影子账户”。
    *   **可扩展的代理框架:** 作为一个“交易代理”构建，采用基于技能的架构，允许自定义交易行为、与即时通讯频道（如Discord）集成，并提供大语言模型（LLM）驱动的分析。
    *   **安全性与保障:** 高度重视安全，提供沙盒化的回测环境、Docker加固部署，并为真实交易操作内置安全防护。
    *   **活跃且开源的开发:** 项目更新迅速，贡献者社区不断壮大，专注于社区驱动的改进和对新资产类别的支持。
*   **为何值得关注:** 该仓库作为**统一、对开发者友好且快速演进**的工具集而脱颖而出，显著降低了实施复杂量化和算法交易策略的门槛。其集完整应用栈、庞大功能集（从数据加载到投资组合优化）与强大社区势头于一身的特点，使其成为算法交易领域学习与实践的热门选择。

**[View Repository / 查看仓库](https://github.com/HKUDS/Vibe-Trading)**


## 🚀 Fast-Moving Repos / 快速崛起项目

### os-taxonomy - Marble Skill Taxonomy: A Structured Graph of What Children Learn
* **What it does**  
  An open dataset providing a comprehensive, structured taxonomy of micro-topics in primary/elementary education. It breaks down learning objectives into fine-grained, teachable concepts, connects them via a prerequisite graph, and aligns them with multiple national curriculum standards.
* **Key features**  
  1. **1,590 Micro-Topics**: Each represents a single, teachable idea (e.g., "Building sentences") with a description, mastery criteria, age range, and type.
  2. **3,221 Prerequisite Edges**: Forms a directed acyclic graph (DAG) defining the learning sequence, with edge strengths (hard/soft) and reasons.
  3. **Curriculum Alignment**: Topics are linked to standards from frameworks like NGSS, Common Core, and the UK National Curriculum.
  4. **Multi-Subject Coverage**: Spans 8 subjects, including Science, Math, English, and History.
  5. **Pure Data**: Delivered as schema-validated UTF-8 JSON files, with no runtime dependencies.
* **Why it's notable**  
  It addresses a gap where curriculum data is often either flat lists or proprietary. This open, graph-based structure uniquely visualizes and models the interconnected nature of learning, making it a valuable resource for educational tools, research, and curriculum analysis. Its clear, commercial-friendly licensing (ODbL + CC BY-SA) also encourages widespread use and contribution.

### os-taxonomy - Marble 技能分类法：结构化的儿童学习知识图谱
* **功能介绍**  
  一个开放的数据集，为小学教育提供全面、结构化的微主题分类法。它将学习目标分解为细粒度、可教授的概念，通过先决条件图谱进行连接，并与多国课程标准对齐。
* **主要特点**  
  1. **1,590个微主题**：每个主题代表一个可教授的理念（例如，“构建句子”），包含描述、掌握标准、年龄范围和类型。
  2. **3,221条先决条件关系**：构成一个有向无环图（DAG），定义了学习顺序，并标注了关系强度（强/弱）及原因。
  3. **课程标准对齐**：主题关联至NGSS、Common Core、英国国家课程等标准。
  4. **多学科覆盖**：涵盖科学、数学、英语、历史等8个学科。
  5. **纯数据交付**：以通过Schema验证的UTF-8 JSON文件提供，无任何运行时依赖。
* **为何值得关注**  
  它解决了教育课程数据通常要么是扁平列表、要么被产品封闭的问题。这种开放的、基于图谱的结构独特地可视化并建模了学习的互联本质，为教育工具、研究和课程分析提供了宝贵资源。其清晰且允许商业使用的许可协议（ODbL + CC BY-SA）也鼓励了广泛的使用和贡献。

**[View Repository / 查看仓库](https://github.com/withmarbleapp/os-taxonomy)**

### Robbyant/lingbot-world-v2 - Infinite Worlds with Versatile Interactions
*   **What it does**: This project, also known as LingBot-World-Infinity, is an advanced world generation model capable of creating continuous, interactive video worlds from an initial image and text prompt. It enables real-time, agent-driven interactions within dynamically evolving scenes.
*   **Key features**:
    *   **Unbounded Interaction**: Generates infinitely long video sequences with consistent quality via a causal pretraining paradigm.
    *   **Real-Time Performance**: A distilled model variant (`causal-fast`) guarantees rapid inference, capable of driving 720p video streams at 60 fps.
    *   **Rich Interactive Elements**: Supports diverse character actions (attacking, archery, spell-casting, etc.) and text-driven environmental events.
    *   **Agentic Control**: Integrates a novel agentic framework where a pilot agent plans character behaviors and a director agent synthesizes new environmental elements.
    *   **Open Source**: Provides a 14B-parameter model, inference code, and technical report.
*   **Why it's notable**: It pushes the boundaries of generative world models by combining infinite generation, real-time performance, and complex, agentic interactions. Its open-source release and demonstrated capabilities for driving interactive simulations make it a significant contribution to the field of AI-driven virtual environments and gaming.

### Robbyant/lingbot-world-v2 - 无限交互世界生成模型
*   **功能介绍**：本项目（LingBot-World-Infinity）是一个先进的交互式世界生成模型，能够根据初始图像和文本提示，持续生成具有多样交互的动态视频世界，支持实时、智能体驱动的场景演化。
*   **主要特点**：
    *   **无限生成**：通过因果预训练范式，可生成质量稳定的无限长视频序列。
    *   **实时性能**：提供蒸馏的快速推理模型（`causal-fast`），能够以60fps的速度驱动720p视频流，实现实时响应。
    *   **丰富交互**：支持多样化的角色动作（攻击、射箭、施法等）及文本驱动的环境事件。
    *   **智能体控制**：创新性地引入智能体框架，由规划智能体（pilot agent）执行角色行为，导演智能体（director agent）动态合成新环境元素。
    *   **开源可用**：开源了14B参数模型、推理代码和技术报告。
*   **为何值得关注**：该项目在生成式世界模型领域实现了重大突破，将无限生成、实时性能与复杂的智能体交互相结合。其开源模型和代码为AI驱动的虚拟环境、游戏开发和交互式模拟研究提供了强大工具和重要基准。

**[View Repository / 查看仓库](https://github.com/Robbyant/lingbot-world-v2)**


## 🎬 YouTube Tech Videos / YouTube 技术视频

### 🎬 China's Belt and Road Problem - Sarah Paine
**Channel:** Dwarkesh Patel
*   This video features an in-depth interview with expert Sarah Paine, analyzing the current state, challenges, and global implications of China's Belt and Road Initiative (BRI).
*   Key topics include the initiative's geopolitical strategy, issues of debt sustainability and transparency, its reception and pushback in various regions, and a critical assessment of its long-term viability and impact.
*   It's worth watching for a nuanced, expert-led discussion that goes beyond headlines, offering critical insights into a major pillar of China's global strategy, hosted in Dwarkesh Patel's characteristic deep-conversation style.

### 🎬 中国一带一路的困境 - Sarah Paine
**频道:** Dwarkesh Patel
*   本视频是对专家 Sarah Paine 的深度访谈，深入分析了中国“一带一路”倡议的现状、挑战及其全球影响。
*   主要讨论的话题包括该倡议的地缘政治战略、债务可持续性与透明度问题、其在世界各地区的接受度与阻力，以及对其长期可行性和影响的批判性评估。
*   值得观看的原因是，这是一个由专家主导、超越新闻表象的细致讨论，为深入了解中国全球战略的一个重要支柱提供了关键见解，节目保持了主持人 Dwarkesh Patel 标志性的深度对话风格。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=IO80MYGbJac)**

### 🎬 Why the tech workforce is quietly splitting in two | Annual AI sentiment survey (Noam Segal)
**Channel:** Lenny's Podcast
* This video presents the findings of an annual survey on AI sentiment within the tech industry, hosted by experienced researcher Noam Segal.
* Key topics include the growing polarization in how tech professionals perceive and adopt AI, the divergence in skill development and job security, and the underlying data revealing this quiet split.
* It's worth watching for an expert, data-driven analysis of a major trend shaping the future of tech careers, offering insights valuable for individual professionals and leaders alike.

### 🎬 为何科技劳动力正在悄然分裂 | 年度AI情绪调查 (Noam Segal)
**频道:** Lenny's Podcast
* 本视频呈现了由资深研究员Noam Segal主持的科技行业年度AI情绪调查结果。
* 主要话题涵盖科技从业者对AI的认知与采用日益两极分化、技能发展与工作安全感的分歧，以及揭示这一悄然分裂的底层数据。
* 为何值得观看：它提供了对塑造科技职业未来的一大趋势的专家级、数据驱动分析，其见解对个人从业者和领导者都极具价值。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=_cmpIveXnvE)**

### 🎬 The head of Instagram on why AI content is a tailwind, not a headwind.
**Channel:** Lenny's Podcast
*   This episode features a deep dive with the head of Instagram, exploring the platform's official stance on the rise of AI-generated content.
*   Key topics include Instagram's strategic response to AI, how AI tools will integrate with and empower the creator ecosystem, and the platform's vision for a future where AI-generated and human-created content coexist.
*   It's a must-watch for its unique, insider perspective from a top platform executive. It moves beyond the common fears around AI flooding feeds with spam, offering a reasoned and optimistic case for AI as a tool that will enhance creativity, personalize experiences, and ultimately drive growth—a crucial viewpoint for creators, marketers, and tech watchers.

### 🎬 Instagram负责人谈AI内容：为何是助力而非阻力
**频道:** Lenny's Podcast
*   本期节目深入采访了Instagram的负责人，重点探讨了该平台对AI生成内容兴起的官方立场。
*   主要话题涵盖Instagram应对AI的战略举措、AI工具如何与创作者生态融合并赋能创作者，以及平台对于AI生成与人类创作内容共存的未来愿景。
*   值得观看的理由在于，这提供了来自平台高层决策者的一手、独特视角。内容超越了关于AI内容泛滥的普遍担忧，理性且乐观地论证了AI作为增强创意、个性化体验并最终驱动增长的工具角色——这对创作者、营销人员和科技观察者而言至关重要。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=TNyVjLUy9ck)**

### 🎬 This Hack Effects Millions of Devices
**Channel:** Low Level

*   This video dives into a critical security vulnerability that has the potential to impact a vast number of devices worldwide.
*   Key topics include the technical details of the exploit, its scope of impact, and the mechanisms that make it so widespread.
*   It's worth watching for a clear, low-level explanation of a significant cybersecurity threat, helping viewers understand both the risk and the underlying technology.

### 🎬 这个漏洞影响数百万台设备
**频道:** Low Level

*   本视频深入探讨了一个可能影响全球大量设备的关键安全漏洞。
*   主要话题包括该漏洞的技术细节、其影响范围以及使其如此广泛传播的机制。
*   值得观看，因为它以底层视角清晰地解释了一个重大的网络安全威胁，帮助观众理解风险及其底层技术。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=E0A7IrJtpUY)**

### 🎬 Comment "HOW" and ill tell you how you can money using Al.
**Channel:** ezCommit
*   What the video covers: This video serves as an interactive teaser, promising to reveal methods for generating income using Artificial Intelligence (AI). The creator states it is *not* about simple tools like email automation, but rather more advanced and "crazy" applications.
*   Key topics discussed: AI for income generation, advanced AI applications beyond basic automation, audience engagement (commenting "HOW" to receive information).
*   Why it's worth watching: It targets viewers interested in innovative, non-conventional ways to leverage AI for financial gain. The promise of powerful, lesser-known techniques makes it intriguing for tech enthusiasts and entrepreneurs exploring AI's practical uses.

### 🎬 留言 "HOW"，我会告诉你如何用AI赚钱
**频道:** ezCommit
*   视频内容概述：这是一个互动预告视频，承诺揭示利用人工智能（AI）赚钱的方法。创作者明确指出，这并非关于像电子邮件自动化这样的基础工具，而是更高级、更“疯狂”的应用。
*   主要话题：AI创收、超越基础自动化的高级AI应用、观众互动（通过留言“HOW”获取信息）。
*   为何值得观看：它针对那些对利用AI获取非传统收入感兴趣的观众。其承诺展示强大且鲜为人知的AI技巧，对于科技爱好者和探索AI实际应用的创业者极具吸引力。

**[Watch Video / 观看视频](https://www.youtube.com/watch?v=XX3uieX2xj8)**

