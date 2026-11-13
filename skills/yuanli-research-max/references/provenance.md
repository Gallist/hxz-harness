# Provenance · 来源清单

`yuanli-research-max` 是 8 个研究能力的方法论内核整合。每个阶段诚实标注出处。
本仓库是**方法论蒸馏**，不含任何私有数据 / token / 客户信息 / 净值真值。MIT License。

| 阶段 | 内核来源 skill | 原始方法论溯源 | 抽出的内核 |
|---|---|---|---|
| P0 设计门 | `research-design-gate` | 骨架借 [revfactory/harness-100](https://github.com/revfactory/harness-100) `thesis-advisor/research-methodology`（MIT），砍学术统计换商业 specialization | 问题类型→设计矩阵、证据标准 S-D 分级、效度威胁前置 |
| P1 前置检索 | `knowledge-liming` + `knowledge-orchestrator` | 本地 LLM-Wiki 检索通道 | facts 优先道、KB-first（已研究的不重做） |
| P2 联网收集 | `hv-deep-research` 第一步 + `gstack-investigate` | hv by 数字生命卡兹克（Khazix）；gstack Boil-the-Lake | 并行子agent、一手优先、充分性自检、完整性 Completeness X/10 |
| P3 双轴分析 | `hv-deep-research` | 横纵分析法（融索绪尔历时-共时 + 社科纵横设计 + 商学院案例法），方法论 by Khazix，蒸馏自 KKKKhazix/khazix-skills | 纵向历时叙事 + 横向共时竞品 + 交汇三剧本 |
| P4 萃取判层 | `info-5l` | 源自 2026-04-22 某公司×某学员「信息5层」商科方法讨论 | L1-L5 判层、糊弄词典、不到 L4 不收尾、可证伪炼丹 |
| P5 失真+证伪 | `quant-fund-factor-product-research` + `gstack-investigate` | quant N=1 某量化机构范本（2026-05-22）；gstack Iron Law | 失真声明三类、实证证伪「允许并要求推翻自己」、无根因不下结论 |
| P6 交付沉淀 | `content-research-writer` + `hv` 写作段 + os-yuanli 收口 | — | 反 AI 写作禁区、引用钩子、evidence-gate、closure-evolution |

## 设计原则

- **整合 ≠ 复制全文**：本 skill 是编排层 + 横切纪律，不是 8 个 SKILL.md 的拼接。
  每阶段是薄蒸馏 + 委派指针，深度 checklist 在 phase-rubrics.md，本地运行时链回模块化 skill。
- **70/30 分离律**：70% 骨架 = 6 阶段研究 OS（不变）；30% specialization = 按任务族加权
  （量化重 P5、内容重 P6、深研重 P3）。
- **反 monolith**：os-yuanli guardrail「不把 skill 变成巨型 prompt」+ 骨架/specialization 分离律。

## 版本

- **v0.1 (2026-06-03)**：初版整合。从 research-design-gate（P0）出发，整合 hv/info-5l/quant/gstack/
  knowledge-liming/knowledge-orchestrator/content-research-writer 的方法论内核为 6 阶段研究 OS。
  **未验级**：尚无端到端 N=1 真实调研 dry-run，待跑通后升 v0.2。

