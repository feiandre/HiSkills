---
name: git-guardrails-claude-code
description: "设置 Claude Code hooks，在危险 git 命令（push、reset --hard、clean、branch -D 等）执行前将其阻止。用户想防止破坏性 git 操作、添加 git 安全 hooks，或在 Claude Code 中阻止 git push/reset 时使用。"
---

# 设置 Git 护栏

设置一个 `PreToolUse` 钩子，在 Claude 执行危险 Git 命令之前拦截并阻止它们。

## 会阻止哪些命令

- `git push`（所有变体，包括 `--force`）。
- `git reset --hard`
- `git clean -f` / `git clean -fd`
- `git branch -D`
- `git checkout .` / `git restore .`

阻止时，Claude 会看到一条消息，告诉它没有权限使用这些命令。

## 步骤

### 1. 询问范围

询问用户：只为**本项目**安装（`.claude/settings.json`），还是为**所有项目**安装（`~/.claude/settings.json`）？

### 2. 复制 hook 脚本

随附脚本位于：[scripts/block-dangerous-git.sh](scripts/block-dangerous-git.sh)。

根据范围，复制到目标位置：

- **项目**：`.claude/hooks/block-dangerous-git.sh`。

- **全局**：`~/.claude/hooks/block-dangerous-git.sh`。

通过 `chmod +x` 使其可执行。

### 3. 将钩子加入设置

添加到相应的设置文件：

**项目**（`.claude/settings.json`）：

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR\"/.claude/hooks/block-dangerous-git.sh"
          }
        ]
      }
    ]
  }
}
```

**全局**（`~/.claude/settings.json`）：

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "~/.claude/hooks/block-dangerous-git.sh"
          }
        ]
      }
    ]
  }
}
```

如果设置文件已经存在，把钩子合并到现有的 `hooks.PreToolUse` 数组。不要覆盖其他设置。

### 4. 询问是否定制

询问用户是否希望从阻止列表中增加或删除任何模式，并相应编辑复制后的脚本。

### 5. 验证

运行快速测试：

```bash
echo '{"tool_input":{"command":"git push origin main"}}' | <path-to-script>
```

应以退出码 2 退出，并向 stderr 打印一条 BLOCKED 消息。
