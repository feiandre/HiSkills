# 代码考古（git 与仓库内部）

## 此来源包含什么

- 提交历史（消息、日期、作者、差异）

- PR 描述、审查评论及讨论线程（通过 `gh`）

- 代码行内注释、TODO、FIXME、弃用说明

- ADR（架构决策记录），如果仓库保留了它们

- 测试：名称和断言通常记录了促成变更的边界情况

- 同一提交中修改的相关文件（共同变更信号）

- 仓库中的 CHANGELOG 条目与发布说明

- 提交消息与 PR 正文中的问题／工单 ID

这是最可信、最完整且直接关联代码的来源。凡是经过仓库的内容都应在这里。

## 如何搜索

扩展种子提交列表：

```bash
git log --follow --oneline -- <file>
git log -S '<exact_string_from_code>' -- <file>
git log -G '<regex>' -- <file>
git blame -L <start>,<end> <file>
git show <hash>
git log <old>..<new> -p -- <file>
```

查找代码之外的文档：

```bash
rg -l -i 'architecture.decision' --glob '*.md'
rg -n -C2 '(TODO|FIXME|HACK|XXX|NOTE)' <target_file>
rg -l '<symbol>' --glob '*test*'
```
