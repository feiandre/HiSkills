# 渲染图表

用 npm 包 `pele@1.9.0` 渲染每个要展示的 `.mmd` 文件，并把 SVG 给用户。Pele 只需在仓库外安装一次。将同名 SVG 写到 `.mmd` 旁。API 在 https://pele.run/api。给 `render` 传 `{ limit: 1_000_000, outputLimit: 8_000_000, maxEdges: 10_000 }`；默认值不足以容纳 500 状态图。出现 `PeleError` 时，把 Mermaid 文本和错误展示给用户。

## 颜色

Pele 忽略 Mermaid 的 `theme` 和 `themeVariables`；在 `.pele` 上设置 `--pele-*` CSS 变量，清单见 https://pele.run/theming。命令给每个状态分组颜色类（如 `class sN teal`），用 `class sN breaks` 或 `class sN mayBreak` 标记坏状态，用 `class sN bugPath` 标记最短 bug 路径，用 `class sN repeats` 标记 PROPERTY 永久重复状态。用 CSS 给这些类着色。

`.mmd` 为 `breaks` 和 `mayBreak` 写入 `classDef`，任意 Mermaid 查看器都能显示 bug 标记；分组颜色、`bugPath`、`repeats` 没有 `classDef`。Pele 把 `classDef` 颜色作为节点 `style` 属性写入，其优先级高于普通 CSS，所以下方标记规则用 `!important`，否则深色主题仍保留浅色。bug 标记设填充和文字，路径/重复设边框；标记规则放在分组颜色后。 本节涉及的标识包括 `bugPath`、`repeats`、`style`。

这些是旧技能的配色建议。将其放入每个 SVG 开头的 `<style>`，使图表跟随查看器明暗设置。

```css
.pele {
  --pele-bg: #ffffff;
  --pele-fg: #1c1c1c;
  --pele-muted: #656565;
  --pele-line: #808080;
  --pele-surface: #fcfcfc;
  --pele-surface-alt: #f1f1f1;
  --pele-border: #c9c9c9;
}
.pele .blue rect { fill: #c3e0ff; }
.pele .orange rect { fill: #f0d3bf; }
.pele .purple rect { fill: #e3d5ff; }
.pele .yellow rect { fill: #f0dcbf; }
.pele .teal rect { fill: #bfe3df; }
.pele .tan rect { fill: #e5d9ce; }
.pele .pink rect { fill: #ffcbe6; }
.pele .breaks rect {
  fill: #ffecee !important;
  stroke: #e72e3b !important;
  stroke-width: 2.5px !important;
}
.pele .breaks text {
  fill: #cd2834 !important;
}
.pele .mayBreak rect {
  fill: #fff3e6 !important;
  stroke: #e8730c !important;
  stroke-width: 2.5px !important;
}
.pele .mayBreak text {
  fill: #b85a06 !important;
}
.pele .bugPath rect {
  stroke: #1680f3 !important;
  stroke-width: 2.5px !important;
}
.pele .repeats rect {
  stroke: #9b35d6 !important;
  stroke-width: 2.5px !important;
  stroke-dasharray: 6 3;
}
@media (prefers-color-scheme: dark) {
  .pele {
    --pele-bg: #1f1f1f;
    --pele-fg: #f5f5f5;
    --pele-muted: #acacac;
    --pele-line: #939393;
    --pele-surface: #121212;
    --pele-surface-alt: #2c2c2c;
    --pele-border: #4e4e4e;
  }
  .pele .blue rect { fill: #1b3857; }
  .pele .orange rect { fill: #573117; }
  .pele .purple rect { fill: #3c2e57; }
  .pele .yellow rect { fill: #573d17; }
  .pele .teal rect { fill: #174641; }
  .pele .tan rect { fill: #3d3127; }
  .pele .pink rect { fill: #57233e; }
  .pele .breaks rect {
    fill: #2e2021 !important;
    stroke: #cf2b35 !important;
  }
  .pele .breaks text {
    fill: #ff6463 !important;
  }
  .pele .mayBreak rect {
    fill: #2e2619 !important;
    stroke: #d0700f !important;
  }
  .pele .mayBreak text {
    fill: #ffa257 !important;
  }
  .pele .bugPath rect {
    stroke: #116dd2 !important;
  }
  .pele .repeats rect {
    stroke: #9a3fcf !important;
  }
}
```
