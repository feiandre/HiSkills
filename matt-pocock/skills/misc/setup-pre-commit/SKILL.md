---
name: setup-pre-commit
description: "在当前仓库中设置 Husky pre-commit 钩子，搭配 lint-staged（Prettier）、类型检查和测试。用户希望添加 pre-commit 钩子、设置 Husky、配置 lint-staged，或添加提交时格式化、类型检查、测试时使用。"
---

# 设置 Pre-Commit 钩子

## 将设置什么

- **Husky** pre-commit 钩子。

- **lint-staged** 对所有暂存文件运行 Prettier。

- **Prettier** 配置（如果缺失）。

- pre-commit 钩子中的 **typecheck** 和 **test** 脚本。

## 步骤

### 1. 检测包管理器

检查 `package-lock.json`（npm）、`pnpm-lock.yaml`（pnpm）、`yarn.lock`（yarn）、`bun.lockb`（bun）。使用实际存在的包管理器。不明确时默认 npm。

### 2. 安装依赖

作为 devDependencies 安装：

```
husky lint-staged prettier
```

### 3. 初始化 Husky

```bash
npx husky init
```

这会创建 `.husky/` 目录，并在 package.json 中添加 `prepare: "husky"`。

### 4. 创建 `.husky/pre-commit`

写入以下文件（Husky v9+ 不需要 shebang）：

```
npx lint-staged
npm run typecheck
npm run test
```

**适配**：把 `npm` 换成检测到的包管理器。如果仓库的 package.json 没有 `typecheck` 或 `test` 脚本，省略相应行，并告知用户。

### 5. 创建 `.lintstagedrc`

```json
{
  "*": "prettier --ignore-unknown --write"
}
```

### 6. 创建 `.prettierrc`（如果缺失）

只有在没有 Prettier 配置时才创建。使用以下默认值：

```json
{
  "useTabs": false,
  "tabWidth": 2,
  "printWidth": 80,
  "singleQuote": false,
  "trailingComma": "es5",
  "semi": true,
  "arrowParens": "always"
}
```

### 7. 验证

- [ ] `.husky/pre-commit` 存在且可执行。

- [ ] `.lintstagedrc` 存在。

- [ ] package.json 中的 `prepare` 脚本为 `"husky"`。

- [ ] `prettier` 配置存在。

- [ ] 运行 `npx lint-staged` 验证它能正常工作。

### 8. 提交

暂存所有修改 / 创建的文件，并使用提交消息：`添加提交前钩子（husky + lint-staged + prettier）`。

这会运行新建的 pre-commit 钩子：是验证一切正常的良好冒烟测试。

## 说明

- Husky v9+ 的钩子文件不需要 shebang。

- `prettier --ignore-unknown` 会跳过 Prettier 无法解析的文件（图片等）。

- pre-commit 先运行 lint-staged（速度快，只针对暂存文件），再运行完整的类型检查和测试。
