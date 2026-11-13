# hxz-harness

给 AI Agent 的研究工具包：原力 Research Max + Agent Reach + 随身智库。

| 组件 | 用途 | 本仓库包含 |
|---|---|---|
| 原力 Research Max | 研究设计、收集、分析、证伪和交付 | 完整 Skill 与全部 references |
| Agent Reach 1.6.1 | 只读搜索和读取各平台内容 | Skill、参考文件与上游程序源码 |
| zhiku-market | 从随身智库目录寻找 Skills / Agents / MCP | Skill、零依赖 Python CLI、原始许可证 |

## 安装

需要 Git、Python 3.10+，以及能执行本地命令的 AI Agent。macOS / Linux 可直接运行；Windows 推荐 WSL。AI 模型服务由朋友自己配置。

```bash
git clone https://github.com/Gallist/hxz-harness.git
cd hxz-harness
python3 scripts/install.py --target codex
# Claude Code 改为 --target claude
# 其他 Agent：--dest /你的/skills/目录
```

安装器只复制三个 Skill，不联网、不启动浏览器；已有不同文件会停止，避免覆盖。升级前请自行备份并移走旧目录。
重启 Agent 会话后生效。也可手动把 skills 下的三个文件夹放到所用 Agent 的 Skill 目录。

### 安装 Agent Reach 程序

Skill 是使用说明，程序需要另装。推荐已有 uv 的朋友使用本仓库附带源码（不是 PyPI 同名包）：

```bash
uv tool install ./vendor/agent-reach
agent-reach setup
agent-reach doctor --text
```

没有 uv 时可用 Python 虚拟环境：

```bash
python3 -m venv .venv
.venv/bin/python -m pip install ./vendor/agent-reach
.venv/bin/agent-reach setup
.venv/bin/agent-reach doctor --text
```

使用虚拟环境时先运行 `source .venv/bin/activate`，让 Agent 能找到命令。
`setup` 会联网安装平台依赖，可能下载浏览器；请在朋友自己的电脑上执行。平台登录由本人完成。
最新安装说明：[Agent Reach 官方文档](https://github.com/Panniantong/Agent-Reach/blob/main/docs/install.md)。不要运行 `pip install agent-reach`，PyPI 同名包并非本项目。

### 使用 zhiku 命令行

```bash
python3 skills/zhiku-market/zhiku "有没有写公众号的 skill"
python3 skills/zhiku-market/zhiku -t mcps "database"
```

无需 API Key，但需要访问市场在线目录。目录里标记 mine=1 的私有组件需要原作者授权，本包不提供这些私有组件的安装权限。

## 发给 Agent 的开场指令

> 请先读取本仓库 README.md，安装 skills 里的三个 Skill，再按说明安装 Agent Reach 程序并检查状态。不要复制其他人的 Cookie 或账号配置；需要我登录时告诉我。以后深度研究用 yuanli-research-max，平台内容读取用 agent-reach，寻找现成工具用 zhiku-market。

试用：

- “用原力 Research Max 研究一个我正在考虑的产品，先帮我明确决策问题。”
- “用 Agent Reach 读取这个公开链接，并说明实际拿到的是正文、评论还是字幕。”
- “从随身智库找一个适合整理会议纪要的 Skill。”

## 能力边界

Research Max 的核心方法与参考表已完整打包；文中提及的其他模块化 Skill 是可选增强，没有它们仍按本包正文执行。没有本地知识库时明确记录 P1 暂缺，不假装已检索。研究洞察等级必须以实际证据判断，不能为通过闸门编造洞察。

Agent Reach 各渠道可能需要朋友自己的登录、API Key 或额外软件；实验渠道可能因平台变化失效。安装成功不代表所有平台实测成功。本包不含浏览器二进制、离线依赖或任何人的授权状态。

不包含黄晓泽的个人 AGENTS.md、Notion / 飞书连接、招聘资料、私有知识库和平台 Cookie。

## 来源与许可

见 [THIRD_PARTY_NOTICES.md](THIRD_PARTY_NOTICES.md) 和各组件许可证。hxz-harness 是集成分享包，各原作者保留署名。Research Max 上游记录仍标为 v0.1，尚无端到端真实调研验级；不要把打包验收当成方法论效果验证。
