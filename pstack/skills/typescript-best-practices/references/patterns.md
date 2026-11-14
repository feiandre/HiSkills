# TypeScript 模式

`SKILL.md` 中每条规则的代码示例。底层原则与语言无关。参见 **type-system-discipline** 与 **boundary-discipline** 原则技能。

## 品牌类型

为原始类型添加品牌，避免混用。在边界验证一次。下游代码信任该类型。

```ts
type AgentId = string & { readonly __brand: "AgentId" };

function isAgentId(input: string): input is AgentId {
  return isUUID(input);
}

function parseAgentId(input: string): AgentId {
  if (!isAgentId(input)) throw new Error(`Invalid agent id: ${input}`);
  return input;
}

function focusAgent(id: AgentId): void {
  
}
```

匹配 `readonly __brand: 'X'` 形式。不要发明新约定。

## 可辨识联合

用字面量判别字段建模变体。每个变体共享字段名，每个变体的值唯一，因此不可能组合无法表示。

```ts
type DiffState = { loading: boolean; diff?: GitDiff; error?: string };
type DiffState =
  | { kind: "loading" }
  | { kind: "ready"; diff: GitDiff }
  | { kind: "error"; error: string };
```

选择一个判别字段名（`kind`、`type`、`tag`）并坚持使用。

## 构造式建模

用全部合法的部分构建类型，而不是通过运行时检查限制宽松类型。

非空，通过可变参数元组表示：

```ts
type NonEmpty<T> = [T, ...T[]];
function pickWinner(entries: string[]): string {
  if (entries.length === 0) throw new Error("no entries");
  return entries[Math.floor(Math.random() * entries.length)];
}
function pickWinner(entries: NonEmpty<string>): string {
  return entries[Math.floor(Math.random() * entries.length)];
}
```

若普通 `T[]` 到达，先用守卫收窄一次。事实随后随类型传播：

```ts
const isNonEmpty = <T>(arr: T[]): arr is NonEmpty<T> => arr.length > 0;
```

偶数长度，用成对表示：

```ts
type Pairs<T> = [T, T][];
```

时间范围，用开始时间加持续时间表示：

```ts
type TimeRange = { start: Date; end: Date };
type TimeRange = { start: Date; durationMs: number };
```

让 `durationMs` 保持普通数字。只有原始数字可能在期望持续时间处被传入时才加品牌（按品牌类型一节），不要条件反射地加。选择使坏状态无法构造的表示，然后在上面暴露所需读取方式（`pairs.flat()`、`rangeEnd()` 辅助函数）。

## 最简全函数类型

不要一切都加强。若对 `T[]` 的每个操作都是全函数，就保留它：

```ts
const sum = (xs: number[]) => xs.reduce((a, b) => a + b, 0);
```

当宽松类型迫使用用处说谎时才加强。识别迹象是 `!`、`arr[0] as T` 和“不应发生”的抛出：

```ts
function newestSession(sessions: Session[]): Session {
  return sessions.at(0)!;
}
function newestSession(sessions: NonEmpty<Session>): Session {
  return sessions[0];
}
```

把结果削弱为 `Session | undefined` 是另一种全函数签名。

## 用 `unknown` 取代 `any`

外部数据始终是 `unknown`。使用前收窄。

```ts
function handle(input: any) {
  return input.foo.bar;
}
function handle(input: unknown) {
  if (typeof input === "object" && input !== null && "foo" in input) {
  }
}
```

外部来源包括 RPC 载荷、`JSON.parse`、`postMessage`、IPC、文件内容、环境变量、数据库结果。

## schema 优先于手写守卫

为外部数据编写逐属性类型守卫前，先查找仓库的运行时 schema 库和现有 schema。让一个 schema 负责验证，并从它派生 TypeScript 类型。不要同时维护 schema、重复 interface 和可能漂移的守卫。

```ts
import { z } from "zod";

const UserSchema = z.object({
  id: z.string().uuid(),
  role: z.enum(["admin", "member"]),
});

type User = z.infer<typeof UserSchema>;

function parseUser(input: unknown): User {
  return UserSchema.parse(input);
}
```

失败是预期分支时使用 `safeParse`。仓库使用其他 schema 库时使用相应推断辅助函数。不要为一个守卫添加新的 schema 依赖。本规则优先采用代码库已信任的 schema 系统。

## 不使用 `as` 类型断言

每个 `as` 都可能导致运行时崩溃。只有在类型系统验证该主张后才可断言。

```ts
import { z } from "zod";
const user = data as User;
function isUser(data: unknown): data is User {
  return typeof data === "object" && data !== null && "id" in data;
}
const userSchema = z.object({ id: z.string(), name: z.string() });
type User = z.infer<typeof userSchema>;

function parseUser(data: unknown): User {
  return userSchema.parse(data);
}
```

类型先定义时，用其证明的类型标注验证器。这样编译器会拒绝证明力度不足的验证器。删除下面对象中的 `name`，赋值就无法编译。

```ts
type User = { id: string; name: string };

const userSchema: z.ZodType<User> = z.object({ id: z.string(), name: z.string() });
```

重构现有代码中的 `as` 时，识别 TypeScript 无法推断的原因：

- 缺少判别字段：添加一个，改用可辨识联合。

- 来源类型过宽（例如 `Record<string, unknown>`）：收窄它。

- 边界无类型：用拥有该形状的 schema 解析。仅在不存在 schema 处添加。

- 确实无法表达：使用品牌类型或 `satisfies`。

## 收窄层级

从最佳到最后手段：

1. **可辨识联合的 switch / if。**编译器自动收窄。

2. **`in` 运算符。**`"key" in obj` 会收窄到包含该键的变体。

3. **`typeof` / `instanceof`。**用于原始值和类实例。

4. **用户定义类型守卫。**上述手段不足时使用。

5. **`as` 类型断言。**仅在验证后使用。

```ts
function area(s: Shape): number {
  if ("radius" in s) return Math.PI * s.radius ** 2;
  return s.width * s.height;
}
```

## 类型守卫

守卫必须真正验证主张。说谎的守卫比 `as` 更糟。

```ts
function isCircle(s: Shape): s is Shape & { kind: "circle" } {
  return s.kind === "circle";
}
```

尽可能优先使用判别字段收窄。

## 穷尽性

在 default 分支中，将判别字段赋值给 `never` 类型局部变量。

```ts
function area(s: Shape): number {
  switch (s.kind) {
    case "circle":
      return Math.PI * s.radius ** 2;
    case "rect":
      return s.width * s.height;
    default: {
      const _exhaustive: never = s;
      return _exhaustive;
    }
  }
}
function handle(s: Shape): void {
  switch (s.kind) {
    case "circle":
      drawCircle(s);
      break;
    case "rect":
      drawRect(s);
      break;
    default: {
      const _exhaustive: never = s;
      void _exhaustive;
    }
  }
}
```

有返回值的 switch 用 return 风格，语句 switch 用 void 风格。

## 用 `satisfies` 取代 `as`

`satisfies` 在不拓宽字面量类型的前提下进行验证。

```ts
const config = { theme: "dark", cols: 3 } as Config;
const config = { theme: "dark", cols: 3 } satisfies Config;
```

## 边界验证

数据进入时验证一次。内部信任类型。参见 **boundary-discipline** 原则技能。

- **传输格式**（proto、JSON-RPC）：用 `ignoreUnknownFields` 解析，使向前兼容的改动不会破坏旧客户端。

- **持久化 JSON：**带版本的 blob，并在解析周围使用 try/catch。

- **不要在**深层调用链中**重复验证**。

## 从 schema 派生类型

若 `.proto`、OpenAPI 规范、GraphQL schema 或数据库迁移已经定义形状，就从生成类型派生，不要重复定义。

```ts
type CheckSummary = {
  totalCount: number;
  checks: { name: string; status: string }[];
};
function renderChecks(s: CheckSummary) {
  
}
import type { ChecksMessage } from "<generated module>";
function renderChecks(s: Pick<ChecksMessage, "totalCount" | "checks">) {
  
}
```

编写新 interface 前，先考虑 `Pick`、`Omit`、`Parameters`、`ReturnType`、`Awaited`、`typeof`。

## 对象参数

```ts
openFile(uri, {
  startLineNumber: 10,
  startColumn: 1,
  endLineNumber: 10,
  endColumn: 1,
});
openFile({
  uri,
  selection: {
    startLineNumber: 10,
    startColumn: 1,
    endLineNumber: 10,
    endColumn: 1,
  },
});
```

在热点路径中跳过：逐帧渲染、tokenizer、解析器及任何分配成本重要的紧密循环。
