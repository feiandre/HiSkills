---
name: migrate-to-shoehorn
description: 将测试文件中的 `as` 类型断言迁移到 @total-typescript/shoehorn。当用户提到 shoehorn、想替换测试中的 `as`，或需要部分测试数据时使用。
---

# 迁移到 Shoehorn

## 为什么使用 shoehorn？

`shoehorn` 让你在测试中传入部分数据，同时让 TypeScript 满意。它用类型安全的替代方式取代 `as` 断言。

**仅限测试代码。**绝不要在生产代码中使用 shoehorn。

测试中使用 `as` 的问题：

- 已被告知不要使用

- 必须手动指定目标类型

- 对故意错误的数据需要双重 as（`as unknown as Type`）

## 安装

```bash
npm i @total-typescript/shoehorn
```

## 迁移模式

### 只需要少数属性的大对象

之前：

```ts
type Request = {
  body: { id: string };
  headers: Record<string, string>;
  cookies: Record<string, string>;
};

it("gets user by id", () => {
  getUser({
    body: { id: "123" },
    headers: {},
    cookies: {},
  });
});
```

之后：

```ts
import { fromPartial } from "@total-typescript/shoehorn";

it("gets user by id", () => {
  getUser(
    fromPartial({
      body: { id: "123" },
    }),
  );
});
```

### `as Type` → `fromPartial()`（类型断言迁移）

之前：

```ts
getUser({ body: { id: "123" } } as Request);
```

之后：

```ts
import { fromPartial } from "@total-typescript/shoehorn";

getUser(fromPartial({ body: { id: "123" } }));
```

### `as unknown as Type` → `fromAny()`（未知类型断言迁移）

之前：

```ts
getUser({ body: { id: 123 } } as unknown as Request);
```

之后：

```ts
import { fromAny } from "@total-typescript/shoehorn";

getUser(fromAny({ body: { id: 123 } }));
```

## 各函数何时使用

| 函数 | 使用场景 |
| --------------- | -------------------------------------------------- |
| `fromPartial()` | 传入仍能通过类型检查的部分数据 |
| `fromAny()` | 传入故意错误的数据（保留自动补全） |
| `fromExact()` | 强制完整对象（之后可换成 fromPartial） |

## 工作流

1. **收集需求**——询问用户：

- 哪些测试文件中的 `as` 断言正在引发问题？

- 是否在处理只关心部分属性的大对象？

- 是否需要传入故意错误的数据来测试错误？

2. **安装并迁移**：

- [ ] 安装：`npm i @total-typescript/shoehorn`

- [ ] 查找含 `as` 断言的测试文件：`grep -r " as [A-Z]" --include="*.test.ts" --include="*.spec.ts"`

- [ ] 将 `as Type` 替换为 `fromPartial()`

- [ ] 将 `as unknown as Type` 替换为 `fromAny()`

- [ ] 添加来自 `@total-typescript/shoehorn` 的导入

- [ ] 运行类型检查验证
