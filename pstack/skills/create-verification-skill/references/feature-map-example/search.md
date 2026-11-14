# 搜索说明

搜索让用户按标题或正文查找笔记，查看匹配笔记，并区分没有匹配与搜索不可用。

## 子功能

- `search-open` 可从各受支持浏览器入口打开搜索。

- `search-match` 返回标题和正文匹配，不修改笔记数据。

- `search-open-result` 在笔记编辑器中打开结果。

- `search-empty` 为没有匹配的查询显示完整空状态。

- `search-clear` 清除查询并恢复最近笔记视图。

- `search-cli` 从终端返回相同匹配笔记。

## 如何到达（用户视角）

- 选择浏览器工具栏中的 `Search` 按钮。

- 焦点不在可编辑字段时，在浏览器中按 `/`。

- 在终端运行 `notes search <query>`。

## 用 control-notes 操作

前置条件：

- Notes 在 `http://127.0.0.1:4173` 正常运行。

- 一次性数据目录包含 `Quarterly plan`，正文为 `Draft budget`。

- `control-notes doctor` 报告预期 URL 与数据目录。

- **工具栏入口。** 选择 `Search`，运行 `control-notes browser click --role button --name "Search"`。出现名为 `Search notes` 的对话框，焦点位于搜索框。

- **键盘入口。** 使用按键 `/` 关闭对话框，聚焦页面并运行 `control-notes browser press --key "/"`。出现同一对话框，页面不会插入斜杠。

- **标题匹配。** 输入 `quarterly`，运行 `control-notes browser fill --role searchbox --name "Search notes" --value "quarterly"`。`Search results` 列表含 `Quarterly plan`，不含 `Grocery list`。

- **正文匹配。** 将查询替换为 `budget`，运行 `control-notes browser fill --role searchbox --name "Search notes" --value "budget"`。`Quarterly plan` 仍可见并带正文匹配摘录。

- **打开结果。** 选择 `Quarterly plan`，运行 `control-notes browser click --role link --name "Quarterly plan"`。对话框关闭，编辑器标题为 `Quarterly plan`。

- **空状态。** 重开搜索并输入 `volcano`，运行 `control-notes browser fill --role searchbox --name "Search notes" --value "volcano"`。搜索完成后出现名为 `No matching notes` 的状态。

- **清除查询。** 选择 `Clear search`，运行 `control-notes browser click --role button --name "Clear search"`。搜索框为空，`Recent notes` 区替换结果列表。

- **CLI 匹配。** 从终端运行 `control-notes cli -- notes search "quarterly" --format json`。退出码 `0`，标准输出包含一个标题为 `Quarterly plan` 的对象。

- **CLI 无匹配。** 搜索不存在值，运行 `control-notes cli -- notes search "volcano" --format json`。退出码 `0`，标准输出为 `[]`。

- **证据。** 捕获有结果状态：运行 `control-notes browser snapshot --aria --path artifacts/search/results.aria.txt` 和 `control-notes browser screenshot --path artifacts/search/results.png`。两个产物都标识 Notes、查询及 `Quarterly plan`。

## 注意事项

- 编辑器或搜索框有焦点时按 `/` 会输入文本，而非打开搜索。

- 结果有短暂防抖，等结果列表或空状态出现，不用固定睡眠。

- 除非用户启用 `Include archived`，归档笔记会被排除。

- CLI 默认输出供人阅读内容，稳定断言使用 `--format json`。

- 打开结果会改变浏览器状态，证明下一次查询前重新打开搜索。
