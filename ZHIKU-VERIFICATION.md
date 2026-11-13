# zhiku 实测记录

2026-11-14，完整复制本机 `zhiku-market` 的五个原始文件：SKILL.md、README.md、LICENSE、install.sh、zhiku，逐字节核对一致。未修改作者程序。

在临时 HOME、没有历史缓存的环境运行原版 CLI：

- `python3 skills/zhiku-market/zhiku --refresh --json -n 3 "会议纪要"`：成功联网下载目录，返回 3 个推荐。
- `python3 skills/zhiku-market/zhiku --json -t mcps -n 3 database`：成功返回 3 个 MCP 结果，类型筛选正确。

这验证了新用户首次联网查询及命令行搜索。尚未逐一安装目录中的组件，也不代表所有组件的外部依赖都已验证。朋友可直接使用本包内的原版 zhiku；查询无需登录或 API Key。组件正文按目录中的来源按需安装。
