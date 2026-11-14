# GitHub 问题

已安装并认证时使用 `gh`，它处理认证、速率限制和 JSON。否则退回 curl 调公共 API，再退回由协作者打开的 URL。

## 搜索

```bash
gh search issues --repo obra/superpowers --limit 10 "<terms>" \
  --json number,state,title --jq '.[] | "\(.number)\t\(.state)\t\(.title)"'
```

没有 `gh` 时（未认证，每分钟 10 次请求）：

```bash
curl -s -H "Accept: application/vnd.github+json" \
  "https://api.github.com/search/issues?q=repo:obra/superpowers+is:issue+<url-encoded terms>&per_page=10" \
  | jq -r '.items[] | "\(.number)\t\(.state)\t\(.title)"'
```

没有 curl 时，交给协作者 `https://github.com/obra/superpowers/issues?q=<terms>`。

## 提交问题

把填好的 `templates/issue.md` 写入工作区，并展示确切文本。获得批准后：

```bash
gh issue create --repo obra/superpowers --title "<title>" --body-file <path> \
  --label bug --label automated-issue-report
```

报告者没有推送权限时 GitHub 会悄悄忽略标签，所以只有协作者的标签才会生效；模板页脚仍标明问题由技能提交。`gh` 无法附加文件：问题创建后，把包路径交给协作者，通过浏览器附加。

没有 `gh` 时，提供基于 `bug_report.md` 模板的预填链接；此模板会为任何报告者应用 `bug` 标签：

```
https://github.com/obra/superpowers/issues/new?template=bug_report.md&title=<url-encoded title>&body=<url-encoded body>
```

GitHub 会拒绝超过约 8,000 字符的 URL；超过时只在链接中带标题，并让协作者从文件粘贴正文。
