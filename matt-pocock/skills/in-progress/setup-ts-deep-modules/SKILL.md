---
name: setup-ts-deep-modules
description: "将 dependency-cruiser 接入 TypeScript 仓库，确保每个包都是深模块，内部实现隐藏于子文件夹中并仅通过入口文件访问。"
disable-model-invocation: true
---

# 设置 TypeScript 深模块
让此仓库中的每个包成为**深模块**：在小接口后承载大量行为。包的公开表面是其**入口点**（包根目录中的文件），其所有子文件夹内容均隐藏。本技能安装 [dependency-cruiser](https://github.com/sverweij/dependency-cruiser) 及规则，使入口点成为唯一进入方式，然后证明这些规则确实有效。
关于词汇（深模块、接口、接缝、深度），用“codebase-design”调用技能工具，并在整个过程中使用其语言。
## 强制实现的形状
```
src/packages/
  <name>/
    index.ts
    client.ts
    lib/
    tests/
```
公开表面是包的**根文件**，而非指定的单一 `index.ts`。按约定，实现位于 `lib/`，测试位于 `tests/`，使每个包都有相同的双文件夹形状。但规则本身是通用的：*任何*子文件夹中的*任何内容*都是私有的，因此永远无需扩展配置来添加文件夹。
四条规则，全部设为 `error`：
1. **入口点边界**：包外代码（应用代码或另一个包）只能导入该包的入口点（其根文件），绝不能导入其子文件夹中的任何内容。
2. **包内自由**：包自己的文件可自由相互导入。
3. **测试通过入口点**：`<pkg>/tests/` 下的文件可导入任何包的入口点及自己的 `tests/` 夹具，但绝不能导入任何包的子文件夹内部（甚至自己的）。跨包集成测试可以；深层导入不可以。
4. **无循环**：不得存在依赖循环。
**用入口点，不用汇总导出文件。**因为公开表面是*每个*根文件，包可以暴露多个小入口点（`index.ts`、`client.ts`、`server.ts`），而不是把所有内容汇入一个巨大的 `index.ts`。不鼓励重新导出整个子树；保持入口点小，把实现隐藏在子文件夹中。
分层（哪些包可依赖哪些）是*另一个*关注点，在本仓库配置中留作注释桩供填写。
## 步骤
### 1. 检测环境
- **包管理器**：`pnpm-lock.yaml` → pnpm，`yarn.lock` → yarn，`bun.lockb` → bun，否则 npm。下方每条命令均使用它（`pnpm`/`yarn`/`npm run`/`bunx`）。
- **包根目录**：若存在 `src/`，使用 `src/packages`，否则使用 `packages`。若仓库已有明显不同约定，请与用户确认选择。
- **现有配置**：检查 `.dependency-cruiser.*` 文件。若存在，**不要**覆盖：把四条规则及选项合并进去，并告知用户添加了什么。
**完成条件：**包管理器、包根目录和现有配置状态均已明确。
### 2. 安装 dependency-cruiser
使用检测到的包管理器将 `dependency-cruiser` 安装为开发依赖项。
**完成条件：**`dependency-cruiser` 位于 `devDependencies` 中。
### 3. 编写配置
将 [`dependency-cruiser.config.cjs`](./dependency-cruiser.config.cjs) 复制到仓库根目录，命名为 `.dependency-cruiser.cjs`。将 `PACKAGES_ROOT` 设为步骤 1 检测到的根目录。规则基于路径深度且不依赖扩展名，其他内容无需调整。
**完成条件：**`.dependency-cruiser.cjs` 存在，`PACKAGES_ROOT` 正确，且四条禁止规则存在。
### 4. 接入检查
- 添加 `lint:boundaries` 脚本：`depcruise <packages-root>`（或 `depcruise src`）。
- 将其并入仓库的总检查命令，即已运行类型检查的脚本（例如 `check`/`ci`/`validate`）。**不要**修改 `tsconfig` 或添加路径别名。
- 若没有总检查脚本，添加 `lint:boundaries` 并告知用户将其纳入持续集成。
**完成条件：**`lint:boundaries` 存在，并与类型检查在同一命令中运行。
### 5. 搭建示例包
创建已提交的 `<packages-root>/example/`，作为复制模板：
- `index.ts` 是入口点。导出一个委派给内部文件的函数（使包明显*深*，而非直通）。
- `lib/impl.ts`：**子文件夹**中的内部文件，由 `index.ts` 导入，外部无法访问。
- `tests/example.test.ts` **只**导入 `../index`（入口点），并针对公开函数断言。
告诉用户这只是供复制或删除的起始模板。
**完成条件：**示例包存在，通过根入口点暴露行为，并在子文件夹中隐藏 `impl`。
### 6. 证明规则有效
这是整个技能的完成标准：配置若不会对违规失败，就毫无价值。
1. 运行 `lint:boundaries`。干净的示例必须**通过**。
2. 临时向 `tests/example.test.ts` 添加深层导入（例如 `import { thing } from "../lib/impl"`）。再次运行 `lint:boundaries`；必须因 `tests-through-entrypoints` **失败**。
3. 还原深层导入。再运行一次，必须**通过**。
**完成条件：**你观察到一次通过、一次因深层导入失败、然后再次通过。若步骤 2 未失败，规则接线不正确，完成前修复。
### 7. 记录约定
在**包文件夹中**写 `README.md`（`<packages-root>/README.md`，与所管理包并列），涵盖：`src/packages/<name>/` 布局（入口点在根目录、实现为 `lib/`、测试为 `tests/`）、“仅通过包的入口点（根文件）导入”，以及如何运行 `lint:boundaries`。明确**不鼓励汇总导出文件**：暴露多个小入口点，而非通过单一 `index.ts` 重新导出整个子树。只保留复制片段及四条规则、每条一段。
然后从仓库代理说明文件（存在 `CLAUDE.md` 则用它，否则 `AGENTS.md`；两者均无则创建 `AGENTS.md`）添加指向它的**上下文指针**。一行足够，例如 `软件包均为深模块：添加或导入软件包前，请先阅读 [src/packages/README.md](./src/packages/README.md)。`。这使代理发现边界规则，而不是被它绊倒。
**完成条件：**`<packages-root>/README.md` 存在且不鼓励汇总导出文件，仓库 `CLAUDE.md`/`AGENTS.md` 链接到它。
## 说明
- 配置中的 `$1` 反向引用（dependency-cruiser 的组匹配）使包能访问自己的内部，而外部不能。不要将它们拆成逐包独立规则。
- 公开与私有由**深度**决定：包的根文件是入口点，子文件夹中的任何内容均为私有。约定子文件夹为 `lib/`（实现）与 `tests/`，但规则没有硬编码它们：任何子文件夹都私有，因此新文件夹永不需要改配置。添加入口点就是添加根文件（无需汇总导出文件）。
- 包是**扁平的**：根目录下一层直接子项。包内部可任意嵌套；包不能包含另一个包。
- 使用 `.cjs`（而非 `.js`），即使仓库为 `"type": "module"`，配置中的 `module.exports` 也能工作。
