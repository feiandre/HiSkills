# Claude Code 的跨平台混合钩子

Claude Code 插件需要钩子在 Windows、macOS 和 Linux 工作。本文描述 `hooks/run-hook.cmd` 使用的单一通用分发器模式。

> **权威来源：**`hooks/run-hook.cmd` 是标准实现。本文与代码不一致时以代码为准。

## 问题

Claude Code 通过 shell 运行钩子命令：

- **macOS/Linux**：bash 或 sh

- **安装 Git Bash 的 Windows**：Git Bash

- **未安装 Git Bash 的 Windows**：PowerShell（旧版使用 CMD.exe）

Windows 回退 shell 无法解析命令字符串：PowerShell 会将前导引号路径当字符串表达式；CMD.exe 的 `/c` 引号规则在路径含 `(` 等元字符时移除外层引号。因此钩子声明 `"shell": "bash"`（Claude Code 2.1.81 起支持，旧版忽略），强制 Git Bash 路径；缺失时给出“安装 Git for Windows”的可操作错误。

这带来几个挑战：

1. **脚本执行**：Windows CMD 不能直接执行 `.sh`

2. **路径格式**：Windows 用反斜杠（`C:\path`），Unix 用正斜杠（`/path`）。

3. **环境变量**：CMD 不支持 `$VAR`

4. **`.sh` 自动前置**：Windows 上 Claude Code 会给路径含 `.sh` 的命令前置 `bash`，有扩展名时干扰分发器

## 方案：无扩展名脚本＋单一通用分发器

仓库所有钩子使用 `run-hook.cmd`。脚本无扩展名（`session-start`，而不是 `session-start.sh`），避免 Claude Code 自动给 `.sh` 命令前置 `bash`。

### 文件结构

```
hooks/
├── hooks.json          # 指向无扩展名脚本的 run-hook.cmd
├── run-hook.cmd        # 跨平台分发器（混合脚本包装）
└── session-start       # 实际钩子逻辑——无扩展名 bash 脚本
```

### hooks 配置（hooks.json）

```json
{
  "hooks": {
    "SessionStart": [
      {
        "matcher": "startup|clear|compact",
        "hooks": [
          {
            "type": "command",
            "command": "\"${CLAUDE_PLUGIN_ROOT}/hooks/run-hook.cmd\" session-start",
            "shell": "bash",
            "async": false
          }
        ]
      }
    ]
  }
}
```

路径加引号，因为 `${CLAUDE_PLUGIN_ROOT}` 可能含空格。

## `run-hook.cmd` 的高层工作方式

`run-hook.cmd` 是混合脚本：Windows 将第一块视为批处理，Unix shell 将该块视为空操作 heredoc 后继续。

不要从本文复制实现。修改分发器时直接读 `hooks/run-hook.cmd`，之后运行 `tests/hooks/test-session-start.sh`。

### 在 Windows（CMD.exe）上的工作方式

1. 批处理段校验脚本名，并从分发器位置解析钩子目录。

2. 按顺序在四处找 bash：

- Git 默认安装路径：`C:\Program Files\Git\bin\bash.exe`

- 32 位 Git 安装路径：`C:\Program Files (x86)\Git\bin\bash.exe`

- `%LOCALAPPDATA%\Programs\Git\bin\bash.exe`（仅设置 `LOCALAPPDATA` 时）

- `PATH` 中的 `bash`（MSYS2、Cygwin 或非默认 Git 安装），通过 `%SystemRoot%\System32\where.exe $PATH:bash` 查找，避免从当前目录取得 `where` 或 `bash`；跳过 `System32`、`Sysnative` 或 `%LOCALAPPDATA%\Microsoft\WindowsApps` 中的 `bash.exe` WSL 启动器和无扩展名匹配。

3. 找到 bash 就运行无扩展名脚本并以脚本退出码退出。

4. 找不到就静默退出 `0`，插件继续工作但跳过钩子。

5. `exit /b` 阻止 CMD 进入 Unix 段。

### 在 Unix（bash/sh）上的工作方式

1. `: << 'CMDBLOCK'` 在空操作命令上打开 heredoc。

2. 整个 CMD 批处理块被 heredoc 消费并忽略。

3. `CMDBLOCK` 之后 bash 解析目录并直接 `exec` 无扩展名脚本。

### 关键设计决定

| 决定 | 原因 |
|---|---|
| 无扩展名脚本 | 防止 Windows `.sh` 自动前置干扰 |
| 不用 `-l` | 钩子应自包含，不依赖登录 shell PATH |
| 不用 `cygpath` | Bash 直接接收 Windows 路径并正确处理 |
| 无 bash 时静默退出 | 无 Git for Windows 的用户仍可使用插件，只是跳过注入 `cygpath` `-c "..."` |

## 编写跨平台钩子脚本

钩子逻辑放在无扩展名文件中。可移植做法：

### 应当

- 尽量使用纯 bash 内建

- 用 `$(command)` 而非反引号

- 引用所有变量展开：`"$VAR"`

### 避免

- 依赖 PATH 工具却不给回退（钩子无 `-l`）

- `.sh` 扩展名，会触发 Windows 自动前置

### 示例：不用外部工具的 JSON 转义

```bash
escape_for_json() {
    local input="$1"
    local output=""
    local i char
    for (( i=0; i<${#input}; i++ )); do
        char="${input:$i:1}"
        case "$char" in
            $'\\') output+='\\' ;;
            '"') output+='\"' ;;
            $'\n') output+='\n' ;;
            $'\r') output+='\r' ;;
            $'\t') output+='\t' ;;
            *) output+="$char" ;;
        esac
    done
    printf '%s' "$output"
}
```

## 故障排查

### 错误提示：“bash is not recognized”

CMD 在分发器尝试的四个位置均找不到 `bash`，因此静默退出并跳过钩子。安装 Git for Windows，或确保 `PATH` 中有非 WSL 的 `bash`。

### Unix 正常但 Windows 无动作

检查 `hooks.json` 中的文件名无扩展名。`run-hook.cmd session-start.sh` 可能触发 `.sh` 自动检测并尝试不存在的 `session-start.sh`。

### 钩子完全不触发

确认 `hooks.json` 中的 `matcher` 匹配事件类型；Claude Code 使用 `startup|clear|compact`，Cursor 使用 `sessionStart`，Cursor 变体见 `hooks-cursor.json`。

## 相关问题

- [anthropics/claude-code#9758](https://github.com/anthropics/claude-code/issues/9758)——Windows 上 `.sh` 在编辑器打开

- [anthropics/claude-code#3417](https://github.com/anthropics/claude-code/issues/3417)——钩子在 Windows 不工作
