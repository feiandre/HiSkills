# Changes to `misc/` skills

<!-- zh-CN:begin e90870be2f087314 -->

# `misc/` 技能的变更政策

<!-- zh-CN:end e90870be2f087314 -->

The skills under `skills/misc/` (`git-guardrails-claude-code`, `migrate-to-shoehorn`, `scaffold-exercises`, `setup-pre-commit`, and anything else that lands there) are frozen. Bug reports, feature requests and PRs against them are closed.

<!-- zh-CN:begin 6612013dfb438229 -->

`skills/misc/` 下的技能（`git-guardrails-claude-code`、`migrate-to-shoehorn`、`scaffold-exercises`、`setup-pre-commit` 以及以后进入该目录的任何内容）已冻结。针对它们的 bug 报告、功能请求和 PR 会被关闭。

<!-- zh-CN:end 6612013dfb438229 -->

## Why this is out of scope

<!-- zh-CN:begin 50b94de9f1877baf -->

## 为何不在范围内

<!-- zh-CN:end 50b94de9f1877baf -->

`misc/` is where skills go when I keep them around but rarely use them. They aren't promoted: they don't ship in the Claude Code plugin, they have no docs page, and I'm not running them day to day, so I can't tell whether a fix is right or notice when one breaks something else. Maintaining them at the same bar as the promoted skills would cost the same as a promoted skill for a fraction of the use.

<!-- zh-CN:begin c6fa715156937a64 -->

`misc/` 存放我保留但很少使用的技能。它们没有正式发布：不随 Claude Code 插件提供，没有文档页，我也不会日常运行，因此无法判断修复是否正确，或是否破坏了别的东西。按正式技能标准维护，需要付出与正式技能相同的成本，使用量却只占很小一部分。

<!-- zh-CN:end c6fa715156937a64 -->

They stay in the repo, unmaintained, because they still work for some people as-is. If one doesn't work for you, install it with skills.sh and fix your copy: the files are yours to edit.

<!-- zh-CN:begin 69d3ad8c04c0d2ae -->

它们原封不动留在仓库中且不再维护，因为仍有部分人可正常使用。若对你不适用，用 skills.sh 安装并修复自己的副本：文件由你编辑。

<!-- zh-CN:end 69d3ad8c04c0d2ae -->

If a `misc/` skill is promoted back into `engineering/` or `productivity/` later, it's back in scope from that point.

<!-- zh-CN:begin 2dd10d618512e942 -->

如果某个 `misc/` 技能以后重新晋升到 `engineering/` 或 `productivity/`，从那时起重新纳入范围。

<!-- zh-CN:end 2dd10d618512e942 -->

## Prior requests

<!-- zh-CN:begin a46189d5d7f80a9b -->

## 先前请求

<!-- zh-CN:end a46189d5d7f80a9b -->

- #14: "Potential typo in setup-pre-commit/SKILL.md"

<!-- zh-CN:begin 969a910cdd9d365a -->

- #14：“setup-pre-commit/SKILL.md 可能拼写错误”

<!-- zh-CN:end 969a910cdd9d365a -->
- #301: "`block-dangerous-git.sh` is bypassed by any git global option (e.g. `git -C <dir> push`)"

<!-- zh-CN:begin 8421b612a6997317 -->

- #301：“任何 git 全局选项都可绕过 `block-dangerous-git.sh`（例如 `git -C <dir> push`）”

<!-- zh-CN:end 8421b612a6997317 -->
- #465: "git-guardrails-claude-code documentation is missing benefits over built in Claude code deny rules"

<!-- zh-CN:begin 003b470653eda928 -->

- #465：“git-guardrails-claude-code 文档缺少相较 Claude Code 内置拒绝规则的优势”

<!-- zh-CN:end 003b470653eda928 -->
- #898: "git-guardrails-claude-code: hook fails open without jq and misses common git spellings"

<!-- zh-CN:begin 3454531cacd12078 -->

- #898：“git-guardrails-claude-code：没有 jq 时钩子失败开放，且漏掉常见 git 拼写”

<!-- zh-CN:end 3454531cacd12078 -->
