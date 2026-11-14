# 平台中立的 README 排序——C 阶段设计

## 背景

A、B 阶段（参见 `2026-05-05-platform-neutral-prose-design.md` 和 `2026-05-05-platform-neutral-config-refs-design.md`）已中立化 README 中泛指 Claude 的文字及配置文件引用。剩余的平台倾向来自布局：README 的两处平台列表都将 Claude Code 放在首位，其他位置也未严格按字母排序。

本阶段修复排序，不改正文措辞。

## 范围内

1. **快速入门平台列表**（`README.md:7`）——支持的运行环境的行内链接列表

2. **安装章节顺序**（`README.md:35–152`）——各运行环境的安装子节

## 范围外

- 正文、市场名称、插件 ID、URL——目前事实均正确。

- Claude Code 章节的视觉分量（它有两个子节：Anthropic 官方市场与 Superpowers 市场）。两者都是真实安装路径；折叠会隐藏正确信息。

- 各安装块内的章节标题与内容——只改变块的顺序。

## 替换

两处列表均重排为严格字母序：

| 旧顺序 | 新顺序 |
|-----------|-----------|
| Claude Code | Claude Code |
| Codex CLI | Codex App |
| Codex App | Codex CLI |
| Factory Droid | Cursor |
| Gemini CLI | Factory Droid |
| OpenCode | Gemini CLI |
| Cursor | GitHub Copilot CLI |
| GitHub Copilot CLI | OpenCode |

三处移动：Codex App 与 Codex CLI 交换；Cursor 上移两位；GitHub Copilot CLI 上移一位。

Claude Code 因字母序巧合仍排第一（`Cl…` 在 `Co…` 前）。

## 提交计划

一个原子提交覆盖两处列表，因为只改一处会使快速入门与安装章节不一致。

## 验证

- 快速入门锚点（`#claude-code`、`#codex-app` 等）仍能指向现有 `### …` 标题；没有重命名标题。

- 每个安装子节的正文前后逐字节相同；只变了位置。

- `git diff README.md` 仅展示章节移动，没有内容编辑。
