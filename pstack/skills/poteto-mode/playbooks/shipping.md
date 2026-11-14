### 发布

**你负责最终落地：独立验证每个 PR，从根开始只发布已验证的连续链，然后不干预堆栈。**

1. **确定 forge，并在落地前独立验证每个 PR。**默认用 GitHub CLI（`gh`）。若 `command -v origin` 成功且 Origin 能解析仓库，所有操作改用 `origin pr`；否则留用 `gh` 并记录回退，绝不强制 Graphite（`gt`）。每个 PR 一个 Cursor 云代理验证者，使用匹配的控制技能按用户方式运行父版本与 head，只在该 PR 发布 `PASS`、`PASS+NOTES` 或 `FAIL`。只有未写代码的代理结论有效，因为作者会检查自己原本意图。绿色 CI 和 bot 批准不算结论，它们都没按用户方式运行改动。 本节涉及的标识包括 `control-ui`、`control-cli`、`cursor-team-kit`。

2. **只落地从底部起连续已验证的链。**从最低未合并 PR 向上走，第一个没有 `PASS` 或 `PASS+NOTES` 就停；下方是运行链，顶端是上限。未验证项上方的已验证 PR 要等待，因为没有下方代码无法落地。分支既不包含也不需要该代码时，可移入主干独立落地，但必须先取得新结论，因为旧结论是在那段代码之上运行。

3. **复查结论仍对应代码。**结论覆盖补丁，链式 rebase 会让上方每个 PR 换 SHA 而检查不失败。信任旧结论前，比较结论 SHA 和当前 head 的 `git patch-id`。若仅测试、文档或 lint 配置不同，并且该通道在两侧构建相同（除噪声外），结果仍有效。噪声是结论 SHA 两次构建也出现的差异或嵌入提交 SHA；报告噪声及文件。变更本身仍需新检查和审查，因为旧结论未见过它。没有构建输出的通道必须重跑并重新验证漂移。

4. **自下而上、一次一个 PR。**总是合并链最低未合并 PR：`origin pr merge <pr>` 或 `gh pr merge <pr> --squash`。Origin 普通命令还可能合并下方全部 PR；GitHub 中 base 仍为父分支的 PR 会合并到父分支，而非主干。读回结果（`origin pr view <pr>` 或 `gh pr view <pr> --json state,mergedAt,baseRefName`），因为排队或请求自动合并不等于已合并。已落地应显示 merged 且 base 是主干。只对结论覆盖当前 head 的 PR 用 `--auto`。落地后，将下一 PR 的 base 改为主干（`origin pr edit <pr> --base <trunk>` 或 `gh pr edit <pr> --base <trunk>`），把补丁移到合并结果并 `--force-with-lease` 推送；步骤 3 的 patch-id 规则决定旧结论是否保留。

5. **落地时保持堆栈不变。**步骤 4 对下一 PR 的移动是唯一分支/base 变更，因为合并落地当时内容，不论结论。GitHub 用 `playbooks/babysit.md` 的队列监视（`scripts/watch-pr/watch-pr --queued-stack --stack-prs <bottom-to-top>`）在 `/loop` 下观察到上限 `COMPLETE`；Origin 每次 `origin pr checks <pr> --watch` 后用 `origin pr view <pr> --checks` 重读至 merged。父合并导致 base 移主干是正常的。合并停滞时先查明原因。

6. **到上限即停。**扩展需要新结论，因此从头开始新一轮。

**回复：**已验证链及上限、每个 PR 的结论与验证者、落地内容及确认方式、下一缺口所需工作。
