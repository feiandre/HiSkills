# HTML 报告格式

架构审查渲染为操作系统临时目录中的单个自包含 HTML 文件。Tailwind 和 Mermaid 均来自 CDN。Mermaid 可靠处理图结构；手工 div 和内联 SVG 处理更编辑化的视觉（质量图、截面）。混合两种方式：不要完全依赖 Mermaid，它会显得普通。

## 骨架

```html
<!doctype html>
<html lang="zh-CN">
  <head>
    <meta charset="utf-8" />
    <title>{{repo name}} 的架构审查</title>
    <script src="https://cdn.tailwindcss.com"></script>
    <script type="module">
      import mermaid from "https://cdn.jsdelivr.net/npm/mermaid@11/dist/mermaid.esm.min.mjs";
      mermaid.initialize({ startOnLoad: true, theme: "neutral", securityLevel: "loose" });
    </script>
    <style>
      /* 为 Tailwind 无法干净覆盖的内容提供小型自定义层：
         虚线接缝、手绘感箭头等。 */
      .seam { stroke-dasharray: 4 4; }
      .leak { stroke: #dc2626; }
      .deep { background: linear-gradient(135deg, #0f172a, #1e293b); }
    </style>
  </head>
  <body class="bg-stone-50 text-slate-900 font-sans">
    <main class="max-w-5xl mx-auto px-6 py-12 space-y-12">
      <header>...</header>
      <section id="candidates" class="space-y-10">...</section>
      <section id="top-recommendation">...</section>
    </main>
  </body>
</html>
```

## 页眉

仓库名称、日期和紧凑图例：实线框 = 模块，虚线 = 接缝，红色箭头 = 泄漏，粗深色框 = 深模块。不要引言段落，直接进入候选。

## 候选卡片

图示承担主要信息。文字稀少、朴素，并使用 `/codebase-design` 技能术语表中的词汇，不故作铺陈。

每个候选是一个 `<article>`：

- **标题**：简短，指出深化方式（例如“合并订单接收流水线”）。

- **徽标行**：建议强度（`Strong` = 翠绿，`Worth exploring` = 琥珀，`Speculative` = 石板灰），再加深依赖类别标签（`in-process`、`local-substitutable`、`ports & adapters`、`mock`）。

- **文件**：等宽列表，`font-mono text-sm`。

- **前／后图示**：核心内容。两列并排。见下方模式。

- **问题**：一句话。哪里痛。

- **方案**：一句话。改什么。

- **收益**：列表，每项不超过 6 个词。例如“测试只命中一个接口”“定价逻辑不再泄漏”“删除 4 个浅层包装器”。

- **ADR 提示**（如适用）：琥珀色框中的一行。

不要解释段落。若图示需要一段文字才能理解，就重绘图示。

## 图示模式

选择适合候选的模式，混合使用。不要让所有图看起来一样，多样性本身就是重点。

### Mermaid 图（依赖／调用流的主力）

重点是“X 调 Y、Y 调 Z，看看这团乱麻”时，使用 Mermaid `flowchart` 或 `graph`。包在 Tailwind 样式卡片中，避免突兀。用 classDef 将泄漏边染红、深模块染深。序列图适合“之前 6 次往返；之后 1 次”。

### 手工框与箭头（Mermaid 布局与你冲突时）

模块用带边框和标签的 `<div>`。箭头使用绝对定位在相对容器上的内联 SVG `<line>` 或 `<path>`。希望“之后”图示看起来像一个粗边框深模块、内部灰化时使用此方式，因为 Mermaid 无法以合适重视渲染。

### 截面（适合分层浅薄结构）

堆叠水平带（`h-12 border-l-4`）展示调用穿过的层。之前：6 个各自不做事的小薄层。之后：1 个粗带，标注合并后的职责。

### 质量图（适合“接口与实现一样宽”）

每个模块两个矩形：一个表示接口表面积，一个表示实现。之前：接口矩形几乎与实现矩形同高（浅）。之后：接口矩形短、实现矩形高（深）。

### 调用图合并

之前：函数调用树渲染为嵌套框。之后：同一棵树合并为一个框，现在属于内部的调用在框内淡显。

## 样式指导

- 简洁编辑风格，不是企业仪表板。留足空白。标题可选衬线（`font-serif` 与 stone／slate 很搭）。

- 颜色克制：一种强调色（翠绿或靛蓝），红色用于泄漏，琥珀用于警告。

- 图示保持约 320px 高，使前后视图可舒适并排，无需滚动。

- 图示内模块标签使用 `text-xs uppercase tracking-wider`，让它们像结构示意，而非 UI。

- 唯一脚本是 Tailwind CDN 和 Mermaid ESM 导入。报告其余部分静态：没有应用代码，除 Mermaid 自身渲染外无交互。

## 首选建议区

一张更大的卡片。候选名称、一句理由、指向其卡片的锚点链接。仅此而已。

## 语气

使用朴素英语、简洁表达，但架构名词和动词直接来自 `/codebase-design` 技能。简洁不能成为偏离术语的借口。

**准确使用：** module、interface、implementation、depth、deep、shallow、seam、adapter、leverage、locality。

**绝不替换：** 用 component、service、unit 替代 module · 用 API、signature 替代 interface · 用 boundary 替代 seam · 用 layer、wrapper 替代你想表达的 module。

**符合风格的表达：**

- “订单接收模块很浅：接口几乎与实现同等大小。”

- “定价逻辑跨接缝泄漏。”

- “深化：一个接口，一个测试位置。”

- “两个适配器证明接缝合理：生产用 HTTP，测试用内存实现。”

**收益列表**用术语表词汇命名收益：*“局部性：缺陷集中在一个模块”*、*“杠杆：一个接口，N 个调用点”*、*“接口缩小；实现吸收包装器”*。不要写“更易维护”或“代码更干净”，因为它们不在术语表中，也不值得占位。

不要含糊，不要铺垫，不要“值得注意的是……”。一句话能写成列表项就写成列表项；列表项可以删就删。若某个词不在 `/codebase-design` 术语表中，先找已有词，再考虑发明新词。
