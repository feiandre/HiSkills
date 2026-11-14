# 纵深防御验证

## 概述

修复由无效数据导致的缺陷时，在一处添加验证似乎就足够了。但不同代码路径、重构或 mock 都能绕过单个检查。

**核心原则：** 在数据流经的每一层验证。让缺陷在结构上不可能发生。

## 为何需要多层

单层验证：“我们修复了缺陷”
多层验证：“我们让缺陷不可能发生”

不同层捕获不同情况：

- 入口验证捕获多数缺陷

- 业务逻辑捕获边界情况

- 环境保护防止特定上下文中的危险

- 调试日志在其他层失败时提供帮助

## 四层

### 第 1 层：入口点验证

**目的：** 在 API 边界拒绝明显无效输入

```typescript
function createProject(name: string, workingDirectory: string) {
  if (!workingDirectory || workingDirectory.trim() === '') {
    throw new Error('workingDirectory cannot be empty');
  }
  if (!existsSync(workingDirectory)) {
    throw new Error(`workingDirectory does not exist: ${workingDirectory}`);
  }
  if (!statSync(workingDirectory).isDirectory()) {
    throw new Error(`workingDirectory is not a directory: ${workingDirectory}`);
  }
}
```

### 第 2 层：业务逻辑验证

**目的：** 确保数据对该操作有意义

```typescript
function initializeWorkspace(projectDir: string, sessionId: string) {
  if (!projectDir) {
    throw new Error('projectDir required for workspace initialization');
  }
}
```

### 第 3 层：环境保护

**目的：** 防止特定上下文中的危险操作

```typescript
async function gitInit(directory: string) {
  if (process.env.NODE_ENV === 'test') {
    const normalized = normalize(resolve(directory));
    const tmpDir = normalize(resolve(tmpdir()));

    if (!normalized.startsWith(tmpDir)) {
      throw new Error(
        `Refusing git init outside temp dir during tests: ${directory}`
      );
    }
  }
}
```

### 第 4 层：调试插桩

**目的：** 捕获用于取证的上下文

```typescript
async function gitInit(directory: string) {
  const stack = new Error().stack;
  logger.debug('即将 git init', {
    directory,
    cwd: process.cwd(),
    stack,
  });
}
```

## 应用模式

发现缺陷时：

1. **追踪数据流**——坏值来自哪里？用在哪里？

2. **映射所有检查点**——列出数据流经的每个点

3. **在每层添加验证**——入口、业务、环境、调试

4. **测试每层**——尝试绕过第 1 层，验证第 2 层能捕获

## 会话中的示例

缺陷：空 `projectDir` 导致在源代码目录执行 `git init`

**数据流：**

1. 测试设置 → 空字符串

4. `git init` 在 `process.cwd()` 运行

**添加四层：**

- 第 1 层：`Project.create()` 验证非空、存在、可写

- 第 2 层：`WorkspaceManager` 验证 projectDir 非空

- 第 3 层：`WorktreeManager` 在测试中拒绝临时目录之外的 git init

- 第 4 层：git init 前记录堆栈跟踪

**结果：** 全部 1847 个测试通过，缺陷无法再复现

## 关键洞见

四层都必要。测试期间，每层都捕获了其他层遗漏的缺陷：

- 不同代码路径绕过入口验证

- mock 绕过业务逻辑检查

- 不同平台边界情况需要环境保护

- 调试日志识别了结构性误用

**不要只停在一个验证点。** 在每一层添加检查。
