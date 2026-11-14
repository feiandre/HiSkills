### 工作树与模拟器清理

1. 快照和审计。记录 `df -h /`，然后运行 `scripts/worktree-audit.sh [-b <pr-base-ref>] [repo-path]`（principle-build-the-lever）。不传 `-b` 时会相对 `origin/HEAD` 检查 `MERGED`，因此 PR 指向其他分支时传 `-b origin/<branch>`。路径从 `git worktree list` 读取，绝不手输，因为手输 `myrepo-worktrees/x` 会漏掉位于 `.cursor/worktrees/myrepo/x` 的工作树（principle-encode-lessons-in-structure）。脚本按大小、年龄、合并状态、未提交工作、PR 状态，以及最近接触它的聊天给每个工作树分类，再建议所属类别。扫描对话记录较慢，放到后台运行。

2. 分类只是建议，不是许可。置顶和活跃聊天才是真实产物（principle-prove-it-works）。从用户或侧栏获取这个集合，逐个交叉核对候选项。工具曾把用户置顶聊天的工作树标成 `safe`，因此以置顶集合为准。

3. 删除前验证使用情况。对每个 `verify-recent-chat` 行或任何存疑项，扇出子代理读取对话记录，报告聊天是否置顶或进行中，以及涉及哪些工作树（principle-guard-the-context-window，对话记录是大批内容）。置顶聊天会通过后台子代理在相邻工作树中启动 arena 与复现树；即使名称从未出现在侧栏，它们也仍在使用。按“子代理”章节，为每个子代理选择适合工作的推理级别及快速或标准速度。

4. 遇到不可逆损失时暂停。`wip:N` 表示 N 处已跟踪但未提交的编辑。先展示差异并取得决定，因为干净工作树删除后可从分支恢复，未提交工作却会丢失。`scratch:N` 是未跟踪的一次性内容，可安全丢弃，但须列出文件名称。按“自主性”，干净、已合并且未使用的继续；有 `wip` 或在使用中的暂停。

5. 清理已确认的集合。逐路径执行 `git worktree remove --force <path>`。若忽略的构建产物使目录残留，对其执行 `rm -rf`，然后 `git worktree prune`。分支引用保留，因此不丢失提交。用 `df -h /` 并重新列出工作树来确认。

6. 模拟器和其他回收来源。模拟器通常是下一个最大收益项。执行 `xcrun simctl --set testing delete all`（XCTestDevices 克隆）、`xcrun simctl delete unavailable`，以及 `xcrun simctl runtime list` 后对旧运行时执行 `runtime delete <id>`。需要时再清理 Xcode `DerivedData` 和 `iOS DeviceSupport`、`~/Library/Application Support/Cursor`（`state.vscdb.backup`，以及 `snapshots/roots/<root>`；以曾作为工作区打开的文件夹命名的 `<root>` 会膨胀）、包缓存（pnpm、uv、brew、yarn）。只清理用户未要求保留的缓存。

这是唯一会删除用户状态、却没有代码审查来发现疏漏的操作手册，因此以上关卡就是审查。

**回复：** 前后的 `df -h /` 及回收空间、清理的工作树，以及每个保留项的一行理由（哪个聊天正在使用，或存在未提交工作）。
