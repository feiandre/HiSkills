# Guards against sub-agents recursing into skills

<!-- zh-CN:begin 22d16bb26748c8c7 -->

# 防止子代理递归调用技能的防护

<!-- zh-CN:end 22d16bb26748c8c7 -->

Skills do not add guards against sub-agents recursively invoking skills or spawning nested agents (a `/code-review` sub-agent re-invoking `/code-review`, a `/research` agent spawning another agent). Requests to add leaf-agent instructions, depth limits or "do not invoke this skill" lines are out of scope.

<!-- zh-CN:begin dcbc621fb8a3ec21 -->

技能不添加防护来阻止子代理递归调用技能或启动嵌套代理（例如 `/code-review` 子代理再次调用 `/code-review`，或 `/research` 代理再启动一个代理）。添加叶子代理指令、深度限制或“不要调用此技能”等文字的请求不在范围内。

<!-- zh-CN:end dcbc621fb8a3ec21 -->

## Why this is out of scope

<!-- zh-CN:begin c3ab994fefc97a46 -->

## 为什么不在范围内

<!-- zh-CN:end c3ab994fefc97a46 -->

The harness should be responsible for stopping infinite subagent loops, not skills. The harness decides which tools and skills a sub-agent can reach and how deep nesting can go, so a limit set there holds for every skill at once. A guard written into one skill's prose covers only that skill, costs tokens on every run, and still depends on the model choosing to obey it.

<!-- zh-CN:begin f6833b9130d860db -->

阻止子代理无限循环是运行环境的责任，而非技能的责任。运行环境决定子代理能访问哪些工具和技能，以及嵌套能有多深，因此在那里设置的限制能同时覆盖全部技能。写进某个技能正文的防护只覆盖该技能，每次运行都消耗 token，而且仍依赖模型主动遵守。

<!-- zh-CN:end f6833b9130d860db -->

If a sub-agent recurses or fans out without bound, report it to the harness.

<!-- zh-CN:begin 9bfce9477283bf75 -->

如果子代理递归或无界扇出，应向运行环境报告。

<!-- zh-CN:end 9bfce9477283bf75 -->

## Prior requests

<!-- zh-CN:begin 5d8bcd0fee5c5f9b -->

## 以往请求

<!-- zh-CN:end 5d8bcd0fee5c5f9b -->

- #530: "research skill: spawned background agent can recursively re-spawn another agent (uncontrolled nesting)"

<!-- zh-CN:begin 427bb829a14244fc -->

- #530：“research 技能：启动的后台代理可以递归再启动代理（不受控的嵌套）”

<!-- zh-CN:end 427bb829a14244fc -->
- #573: "code-review sub-agents recursively invoke /code-review and fan out" (PR #1186, "code-review: make the Standards and Spec sub-agents leaf reviewers", closed)

<!-- zh-CN:begin 7ab1c1718a28b0a9 -->

- #573：“code-review 子代理递归调用 /code-review 并扇出”（PR #1186，“code-review：使 Standards 与 Spec 子代理成为叶子审查者”，已关闭）

<!-- zh-CN:end 7ab1c1718a28b0a9 -->
