# 创建笔记

创建笔记允许用户通过浏览器或 CLI 保存带标题的笔记、取消未完成草稿，并从第二个用户视图确认已保存笔记。

## 子功能

- `create-open` 从每个浏览器入口打开空白编辑器。

- `create-save` 持久化标题和正文。

- `create-cancel` 丢弃未完成的浏览器草稿。

- `create-cli` 从终端创建相同笔记结构。

## 用户视角的进入方式

- 选择浏览器工具栏的 `New note`（新建笔记）。

- 焦点不在可编辑字段时，在浏览器中按 `n`。

- 终端运行 `notes create --title <title> --body <body>`。

## 用 control-notes 驱动

前置条件：

- Notes 在 `http://127.0.0.1:4173` 正常。

- 没有标题为 `Release checklist` 的笔记。

- `control-notes doctor` 报告预期 URL 和可丢弃数据目录。

- **打开编辑器。**选择 `New note`，运行 `control-notes browser click --role button --name "New note"`；出现名为 `Note editor` 的表单，焦点在 `Title` 文本框。

- **输入内容。**运行 `control-notes browser fill --role textbox --name "Title" --value "Release checklist"` 和 `control-notes browser fill --role textbox --name "Body" --value "Tag and publish"`；`Save note` 按钮变为可用。

- **保存。**运行 `control-notes browser click --role button --name "Save note"`；出现 `Note saved` 状态，标题显示 `Release checklist`。 本节涉及的标识包括 `Save note`。

- **确认持久化。**运行 `control-notes browser click --role link --name "All notes"` 再 `control-notes browser click --role link --name "Release checklist"`；编辑器显示两个保存值。

- **取消草稿。**运行新建、填写标题 `Discard me` 和 `control-notes browser click --role button --name "Cancel"`；返回列表且没有 `Discard me` 链接。 本节涉及的标识包括 `Cancel`、`control-notes browser click --role button --name "New note"`、`control-notes browser fill --role textbox --name "Title" --value "Discard me"`。

- **CLI 入口。**运行 `control-notes cli -- notes create --title "CLI note" --body "Created from terminal" --format json`；退出码 `0`，stdout 含新 ID 和标题。

- **证明。**从 `All notes` 重开两条笔记，运行 `control-notes browser snapshot --aria --path artifacts/create-note/list.aria.txt` 和 `control-notes browser screenshot --path artifacts/create-note/list.png`；产物显示两条标题。 本节涉及的标识包括 `Release checklist`、`CLI note`。

## 易错点

- 文本框获得焦点时按 `n` 只会输入字符，不会打开编辑器。

- 保存时会修剪标题；断言渲染后的标题，不检查草稿输入值。

- 仅有保存状态不充分，必须从列表重新打开。

- 清理夹具时删除两条测试笔记，但保留证明产物。 本节涉及的标识包括 `Release checklist`、`CLI note`。
