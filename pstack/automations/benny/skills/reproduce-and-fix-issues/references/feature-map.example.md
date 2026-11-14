# Feature-map example

<!-- zh-CN:begin 7673c0562b759c26 -->

# 功能地图示例

<!-- zh-CN:end 7673c0562b759c26 -->

Map every user-facing feature Benny may reproduce. Read the relevant section before driving the app. Keep this map at the user point of view. Discover internals and current code paths at runtime instead of freezing them here.

<!-- zh-CN:begin 310185d9bc64de77 -->

规划 Benny 可复现的每项用户功能。驱动应用前阅读相关章节。地图保持用户视角；内部细节和当前代码路径运行时发现，不要冻结在此。

<!-- zh-CN:end 310185d9bc64de77 -->

Copy this file outside `.cursor/automations/benny/`, for example to `.cursor/benny/feature-map.md`, and set `control.feature_map_path` to the copy. Pack refreshes must not overwrite it.

<!-- zh-CN:begin 90065bd69eefd5f8 -->

把本文件复制到`.cursor/automations/benny/`外，例如`.cursor/benny/feature-map.md`，把`control.feature_map_path`指向副本；包刷新不得覆盖它。

<!-- zh-CN:end 90065bd69eefd5f8 -->

## Per-feature template

<!-- zh-CN:begin 10d479daa9bef72d -->

## 单项功能模板

<!-- zh-CN:end 10d479daa9bef72d -->

### `<feature name>`

<!-- zh-CN:begin 2545641f53565522 -->

### `<功能名称>` （保留标识：`<feature name>`）

<!-- zh-CN:end 2545641f53565522 -->

`<one-line user-visible purpose>`

<!-- zh-CN:begin a8bd426791642a4b -->

`<一行用户可见目的>` （保留标识：`<one-line user-visible purpose>`）

<!-- zh-CN:end a8bd426791642a4b -->

#### How a user gets there

<!-- zh-CN:begin eb803b10d6e30070 -->

#### 用户如何到达

<!-- zh-CN:end eb803b10d6e30070 -->

- Click path: `<screen> -> <menu, tab, or panel> -> <control>`

<!-- zh-CN:begin b109bf3001fe4a59 -->

- 点击路径：`<屏幕> -> <菜单、标签或面板> -> <控件>` （保留标识：`<screen> -> <menu, tab, or panel> -> <control>`）

<!-- zh-CN:end b109bf3001fe4a59 -->
- Keyboard shortcut: `<shortcut or none>`

<!-- zh-CN:begin d2e66e3223f50c48 -->

- 键盘快捷键：`<快捷键或无>` （保留标识：`<shortcut or none>`）

<!-- zh-CN:end d2e66e3223f50c48 -->

#### How the control adapter drives it

<!-- zh-CN:begin ddf0f940311375da -->

#### 控件适配器如何驱动

<!-- zh-CN:end ddf0f940311375da -->

- `<adapter action>` with `<inputs>` should `<visible result>`.

<!-- zh-CN:begin bfa71c7fc28abdea -->

- `<适配器动作>`配合`<输入>`应产生`<可见结果>`。 （保留标识：`<adapter action>`，`<inputs>`，`<visible result>`）

<!-- zh-CN:end bfa71c7fc28abdea -->
- Reset: `<how the adapter returns to a fresh state>`.

<!-- zh-CN:begin e2012a9148c7d0c6 -->

- 重置：`<适配器如何回到全新状态>`。 （保留标识：`<how the adapter returns to a fresh state>`）

<!-- zh-CN:end e2012a9148c7d0c6 -->

#### Stable selectors

<!-- zh-CN:begin 96cf2179472c88ad -->

#### 稳定选择器

<!-- zh-CN:end 96cf2179472c88ad -->

- `<role and accessible name>`

<!-- zh-CN:begin 3ba09485b4ff7cdf -->

- `<角色和可访问名称>` （保留标识：`<role and accessible name>`）

<!-- zh-CN:end 3ba09485b4ff7cdf -->
- `<ARIA relationship>`

<!-- zh-CN:begin af3b8278d7bfdf61 -->

- `<ARIA关系>` （保留标识：`<ARIA relationship>`）

<!-- zh-CN:end af3b8278d7bfdf61 -->
- `<data-component or purpose-named data attribute>`

<!-- zh-CN:begin d1097d4a31512cba -->

- `<data-component或按用途命名的data属性>` （保留标识：`<data-component or purpose-named data attribute>`）

<!-- zh-CN:end d1097d4a31512cba -->

Never use generated CSS or StyleX classes, dynamic hashes, child indexes, or brittle DOM position.

<!-- zh-CN:begin e441be506b681ae1 -->

绝不使用生成的CSS/StyleX类、动态哈希、子索引或脆弱DOM位置。

<!-- zh-CN:end e441be506b681ae1 -->

#### States to exercise

<!-- zh-CN:begin e2ef51947e650f8f -->

#### 要检查的状态

<!-- zh-CN:end e2ef51947e650f8f -->

- Default, hover, focus-visible, active, disabled

<!-- zh-CN:begin ada2a55d82409b9c -->

- 默认、悬停、焦点可见、激活、禁用

<!-- zh-CN:end ada2a55d82409b9c -->
- Loading, empty, error

<!-- zh-CN:begin 78943f81b4f6fab5 -->

- 加载、空、错误

<!-- zh-CN:end 78943f81b4f6fab5 -->
- Selected, open, expanded

<!-- zh-CN:begin e1371dd742e17818 -->

- 选中、打开、展开

<!-- zh-CN:end e1371dd742e17818 -->
- `<relevant feature-specific variants>`

<!-- zh-CN:begin ada0a5f77e592b6c -->

- `<相关功能变体>` （保留标识：`<relevant feature-specific variants>`）

<!-- zh-CN:end ada0a5f77e592b6c -->

Mark states that do not apply.

<!-- zh-CN:begin 4606e18c228f69c8 -->

标记不适用的状态。

<!-- zh-CN:end 4606e18c228f69c8 -->

#### Preconditions and setup

<!-- zh-CN:begin fd8983441fc48e92 -->

#### 前置条件与设置

<!-- zh-CN:end fd8983441fc48e92 -->

- Auth: `<account state>`

<!-- zh-CN:begin 91821ba328335a9b -->

- 认证：`<账户状态>` （保留标识：`<account state>`）

<!-- zh-CN:end 91821ba328335a9b -->
- Data: `<fixture>`

<!-- zh-CN:begin 14030edd99ed5e8a -->

- 数据：`<夹具>` （保留标识：`<fixture>`）

<!-- zh-CN:end 14030edd99ed5e8a -->
- Permissions: `<role>`

<!-- zh-CN:begin e5536894f66cc8d8 -->

- 权限：`<角色>` （保留标识：`<role>`）

<!-- zh-CN:end e5536894f66cc8d8 -->
- Flags: `<flag or none>`

<!-- zh-CN:begin a789e86900197181 -->

- 功能标志：`<标志或无>` （保留标识：`<flag or none>`）

<!-- zh-CN:end a789e86900197181 -->
- Services: `<required availability>`

<!-- zh-CN:begin ad05397d8ef67466 -->

- 服务：`<所需可用性>` （保留标识：`<required availability>`）

<!-- zh-CN:end ad05397d8ef67466 -->

#### Evidence and cross-check

<!-- zh-CN:begin fd0f9dee8fa88aeb -->

#### 证据与交叉核对

<!-- zh-CN:end fd0f9dee8fa88aeb -->

- Screenshot: `<app identity, feature, and discriminating state>`

<!-- zh-CN:begin fd102cd37d13f61d -->

- 截图：`<应用身份、功能及区分状态>` （保留标识：`<app identity, feature, and discriminating state>`）

<!-- zh-CN:end fd102cd37d13f61d -->
- Video: `<entry path, interaction, and final state>`

<!-- zh-CN:begin 70e4a70385109440 -->

- 视频：`<入口路径、交互和最终状态>` （保留标识：`<entry path, interaction, and final state>`）

<!-- zh-CN:end 70e4a70385109440 -->
- Cross-check: `<read-only state or value that confirms the UI>`

<!-- zh-CN:begin 67f5c03e68906bb5 -->

- 交叉核对：`<确认UI的只读状态或值>` （保留标识：`<read-only state or value that confirms the UI>`）

<!-- zh-CN:end 67f5c03e68906bb5 -->

#### Gotchas

<!-- zh-CN:begin 5aae84df3a006348 -->

#### 易错点

<!-- zh-CN:end 5aae84df3a006348 -->

- `<known dead end or wrong surface>`

<!-- zh-CN:begin 7e6cae824da384a4 -->

- `<已知死路或错误界面>` （保留标识：`<known dead end or wrong surface>`）

<!-- zh-CN:end 7e6cae824da384a4 -->
- `<safe environment translation>`

<!-- zh-CN:begin cc0f58870944ba0f -->

- `<安全的环境转换>` （保留标识：`<safe environment translation>`）

<!-- zh-CN:end cc0f58870944ba0f -->

## Fictional example

<!-- zh-CN:begin e72854167d62ff72 -->

## 虚构示例

<!-- zh-CN:end e72854167d62ff72 -->

These features belong to a fictional task app. They are examples, not required Benny features.

<!-- zh-CN:begin b20746e5e1018629 -->

以下属于虚构任务应用，只是示例，不是Benny必需功能。

<!-- zh-CN:end b20746e5e1018629 -->

### Sign in

<!-- zh-CN:begin cd602638d944c074 -->

### 登录

<!-- zh-CN:end cd602638d944c074 -->

Lets a user enter the task app.

<!-- zh-CN:begin 36828f353ec527d9 -->

让用户进入任务应用。

<!-- zh-CN:end 36828f353ec527d9 -->

#### How a user gets there

<!-- zh-CN:begin fe46ab23940e32f3 -->

#### 用户如何到达

<!-- zh-CN:end fe46ab23940e32f3 -->

- Open the app and choose `Sign in`. No shortcut.

<!-- zh-CN:begin 7cc299c8d5b96e5a -->

- 打开应用并选择`Sign in`，无快捷键。

<!-- zh-CN:end 7cc299c8d5b96e5a -->

#### How the control adapter drives it

<!-- zh-CN:begin fc723837276e7877 -->

#### 控件适配器如何驱动

<!-- zh-CN:end fc723837276e7877 -->

- `open_app`, `click Sign in`, `fill credentials`, and `click Continue` should open the item list.

<!-- zh-CN:begin ea6c359397c16005 -->

- `open_app`、`click Sign in`、`fill credentials`、`click Continue`应打开条目列表。

<!-- zh-CN:end ea6c359397c16005 -->
- Reset by signing out and clearing the disposable session.

<!-- zh-CN:begin 6e9672afc73eb5e4 -->

- 退出并清除一次性会话以重置。

<!-- zh-CN:end 6e9672afc73eb5e4 -->

#### Stable selectors

<!-- zh-CN:begin 55e314c05c5d9aed -->

#### 稳定选择器

<!-- zh-CN:end 55e314c05c5d9aed -->

- Button `Sign in`, textboxes `Email` and `Password`, `data-component="sign-in-form"`

<!-- zh-CN:begin 3574b50e00bdf1d2 -->

- 按钮`Sign in`、文本框`Email`/`Password`、`data-component="sign-in-form"`

<!-- zh-CN:end 3574b50e00bdf1d2 -->

#### States to exercise

<!-- zh-CN:begin dd66c0d817b9b09e -->

#### 要检查的状态

<!-- zh-CN:end dd66c0d817b9b09e -->

- Default, focus-visible, submitting, disabled, loading, error

<!-- zh-CN:begin 0db1a6203b608106 -->

- 默认、焦点可见、提交中、禁用、加载、错误

<!-- zh-CN:end 0db1a6203b608106 -->

#### Preconditions and setup

<!-- zh-CN:begin ccecb8cf084521c2 -->

#### 前置条件与设置

<!-- zh-CN:end ccecb8cf084521c2 -->

- Disposable account and available authentication service

<!-- zh-CN:begin 2a66da5a8c2e761a -->

- 一次性账户和可用的认证服务

<!-- zh-CN:end 2a66da5a8c2e761a -->

#### Evidence and cross-check

<!-- zh-CN:begin 7b6171cea9779b5c -->

#### 证据与交叉核对

<!-- zh-CN:end 7b6171cea9779b5c -->

- Record landing page through item list. Check read-only session state.

<!-- zh-CN:begin 26fe0a0d41196120 -->

- 记录从落地页到条目列表；检查只读会话状态。

<!-- zh-CN:end 26fe0a0d41196120 -->

#### Gotchas

<!-- zh-CN:begin 46bd253f91b9354e -->

#### 易错点

<!-- zh-CN:end 46bd253f91b9354e -->

- A marketing page is the wrong surface. A missing auth service is a block.

<!-- zh-CN:begin c0504fbc1ec1a412 -->

- 营销页是错误界面；缺少认证服务是阻塞。

<!-- zh-CN:end c0504fbc1ec1a412 -->

### Item list and detail

<!-- zh-CN:begin 8be4e951e5342409 -->

### 条目列表与详情

<!-- zh-CN:end 8be4e951e5342409 -->

Lets a user browse items and open one.

<!-- zh-CN:begin c6f1d1ec9b30399b -->

让用户浏览并打开条目。

<!-- zh-CN:end c6f1d1ec9b30399b -->

#### How a user gets there

<!-- zh-CN:begin b76756e088439606 -->

#### 用户如何到达

<!-- zh-CN:end b76756e088439606 -->

- Open the `Items` tab, then choose a row.

<!-- zh-CN:begin f4db8aa6a6d6a2ca -->

- 打开`Items`标签，然后选择一行。

<!-- zh-CN:end f4db8aa6a6d6a2ca -->

#### How the control adapter drives it

<!-- zh-CN:begin ab55c2aae8775ac1 -->

#### 控件适配器如何驱动

<!-- zh-CN:end ab55c2aae8775ac1 -->

- `select_tab Items` and `click <fixture item>` should open its detail.

<!-- zh-CN:begin b605dd9ed5af6524 -->

- `select_tab Items`和`click <fixture item>`应打开详情。

<!-- zh-CN:end b605dd9ed5af6524 -->
- Reset by closing the detail and clearing selection.

<!-- zh-CN:begin 49525089f71f11df -->

- 关闭详情并清除选择以重置。

<!-- zh-CN:end 49525089f71f11df -->

#### Stable selectors

<!-- zh-CN:begin 70550058ac16d935 -->

#### 稳定选择器

<!-- zh-CN:end 70550058ac16d935 -->

- Tab and list named `Items`, fixture-named row, `data-component="item-detail"`

<!-- zh-CN:begin 143c316c32b9f042 -->

- 标签和列表`Items`、夹具名行、`data-component="item-detail"`

<!-- zh-CN:end 143c316c32b9f042 -->

#### States to exercise

<!-- zh-CN:begin 335bea46685ac151 -->

#### 要检查的状态

<!-- zh-CN:end 335bea46685ac151 -->

- Loading, empty, error, selected, open, expanded

<!-- zh-CN:begin 07f2169263620897 -->

- 加载、空、错误、选中、打开、展开

<!-- zh-CN:end 07f2169263620897 -->

#### Preconditions and setup

<!-- zh-CN:begin 3051b01070d39002 -->

#### 前置条件与设置

<!-- zh-CN:end 3051b01070d39002 -->

- Named fixture items, read permission, available item service

<!-- zh-CN:begin 7a456bf35a7f74cb -->

- 命名夹具、读取权限、可用条目服务

<!-- zh-CN:end 7a456bf35a7f74cb -->

#### Evidence and cross-check

<!-- zh-CN:begin f2ae2f6f82f86b3e -->

#### 证据与交叉核对

<!-- zh-CN:end f2ae2f6f82f86b3e -->

- Show selection and matching detail title. Check selected-item ID.

<!-- zh-CN:begin b9ed308f1109241c -->

- 显示选中项与匹配详情标题；检查选中ID。

<!-- zh-CN:end b9ed308f1109241c -->

#### Gotchas

<!-- zh-CN:begin 782725288874666e -->

#### 易错点

<!-- zh-CN:end 782725288874666e -->

- Search results may look similar but use a different path.

<!-- zh-CN:begin 8d10f3a6a137063a -->

- 搜索结果可能相似但走不同路径。

<!-- zh-CN:end 8d10f3a6a137063a -->

### Item editor

<!-- zh-CN:begin 2f12edad4cff705c -->

### 条目编辑器

<!-- zh-CN:end 2f12edad4cff705c -->

Lets a user create or edit an item.

<!-- zh-CN:begin ea3cdda778b61d71 -->

让用户创建或编辑条目。

<!-- zh-CN:end ea3cdda778b61d71 -->

#### How a user gets there

<!-- zh-CN:begin 42dfb5e0e2c6f4aa -->

#### 用户如何到达

<!-- zh-CN:end 42dfb5e0e2c6f4aa -->

- Choose `Edit` from detail or `New item` from the list.

<!-- zh-CN:begin 2455afdffc7f722f -->

- 详情选择`Edit`，或列表选择`New item`。

<!-- zh-CN:end 2455afdffc7f722f -->

#### How the control adapter drives it

<!-- zh-CN:begin ef4fca9123581c56 -->

#### 控件适配器如何驱动

<!-- zh-CN:end ef4fca9123581c56 -->

- `click Edit`, `fill <field>`, and `click Save` should update detail.

<!-- zh-CN:begin a921cdc34cec2c1d -->

- `click Edit`、`fill <field>`、`click Save`应更新详情。

<!-- zh-CN:end a921cdc34cec2c1d -->
- Reset by restoring the fixture.

<!-- zh-CN:begin d698fd05281413b7 -->

- 恢复夹具以重置。

<!-- zh-CN:end d698fd05281413b7 -->

#### Stable selectors

<!-- zh-CN:begin 778cfa3d79e4e375 -->

#### 稳定选择器

<!-- zh-CN:end 778cfa3d79e4e375 -->

- Buttons `Edit`, `New item`, `Save`, form `Item editor`, label-linked fields

<!-- zh-CN:begin ef5fb2db8b42a73f -->

- 按钮`Edit`/`New item`/`Save`、表单`Item editor`、标签关联字段

<!-- zh-CN:end ef5fb2db8b42a73f -->

#### States to exercise

<!-- zh-CN:begin cba9b5b571509bcc -->

#### 要检查的状态

<!-- zh-CN:end cba9b5b571509bcc -->

- Default, focus-visible, dirty, validating, disabled, saving, error, success

<!-- zh-CN:begin 1e98a84364518b47 -->

- 默认、焦点可见、脏数据、验证、禁用、保存中、错误、成功

<!-- zh-CN:end 1e98a84364518b47 -->

#### Preconditions and setup

<!-- zh-CN:begin dda6d9f5538ca1db -->

#### 前置条件与设置

<!-- zh-CN:end dda6d9f5538ca1db -->

- Editable fixture, write permission, available save service

<!-- zh-CN:begin 5b1f9791f8c6b12a -->

- 可编辑夹具、写权限、可用保存服务

<!-- zh-CN:end 5b1f9791f8c6b12a -->

#### Evidence and cross-check

<!-- zh-CN:begin 20083608c19a217d -->

#### 证据与交叉核对

<!-- zh-CN:end 20083608c19a217d -->

- Show field change through updated detail. Check the stored item value read-only.

<!-- zh-CN:begin 59c19938056b01c9 -->

- 从字段变化展示更新详情；只读检查存储值。

<!-- zh-CN:end 59c19938056b01c9 -->

#### Gotchas

<!-- zh-CN:begin 84f6e467ba118d04 -->

#### 易错点

<!-- zh-CN:end 84f6e467ba118d04 -->

- Do not inject form state. A read-only detail field is not the editor.

<!-- zh-CN:begin b58cec502f525cb5 -->

- 不注入表单状态；只读详情字段不是编辑器。

<!-- zh-CN:end b58cec502f525cb5 -->

### Settings

<!-- zh-CN:begin bee706cb6b257d2b -->

### 设置

<!-- zh-CN:end bee706cb6b257d2b -->

Lets a user change personal preferences.

<!-- zh-CN:begin dc59b186759d098e -->

让用户修改个人偏好。

<!-- zh-CN:end dc59b186759d098e -->

#### How a user gets there

<!-- zh-CN:begin 27f1f06c61043561 -->

#### 用户如何到达

<!-- zh-CN:end 27f1f06c61043561 -->

- Open the profile menu, then choose `Settings`.

<!-- zh-CN:begin bd3a1340ad1f4325 -->

- 打开个人资料菜单，选择`Settings`。

<!-- zh-CN:end bd3a1340ad1f4325 -->

#### How the control adapter drives it

<!-- zh-CN:begin 499e056272697814 -->

#### 控件适配器如何驱动

<!-- zh-CN:end 499e056272697814 -->

- `open_menu Profile`, `click Settings`, and `toggle <preference>` should update the control.

<!-- zh-CN:begin 39bcc496cd795ccb -->

- `open_menu Profile`、`click Settings`、`toggle <preference>`应更新控件。

<!-- zh-CN:end 39bcc496cd795ccb -->
- Reset by restoring the starting preference.

<!-- zh-CN:begin d80881cde4c0c441 -->

- 恢复初始偏好以重置。

<!-- zh-CN:end d80881cde4c0c441 -->

#### Stable selectors

<!-- zh-CN:begin 7a11573ee6f11d58 -->

#### 稳定选择器

<!-- zh-CN:end 7a11573ee6f11d58 -->

- Button `Profile`, menu item `Settings`, region `Settings`, purpose-named preference attribute

<!-- zh-CN:begin b3be93ab024617ad -->

- 按钮`Profile`、菜单项`Settings`、区域`Settings`、按用途命名的偏好属性

<!-- zh-CN:end b3be93ab024617ad -->

#### States to exercise

<!-- zh-CN:begin 1171a3592ac63612 -->

#### 要检查的状态

<!-- zh-CN:end 1171a3592ac63612 -->

- Closed, open, selected, focus-visible, disabled, loading, error

<!-- zh-CN:begin 6aab8384340393f0 -->

- 关闭、打开、选中、焦点可见、禁用、加载、错误

<!-- zh-CN:end 6aab8384340393f0 -->

#### Preconditions and setup

<!-- zh-CN:begin f6ebf8c7b68de3a0 -->

#### 前置条件与设置

<!-- zh-CN:end f6ebf8c7b68de3a0 -->

- Signed-in test account, known preferences, available preference service

<!-- zh-CN:begin eea14f0ebabc24ff -->

- 已登录测试账户、已知偏好、可用偏好服务

<!-- zh-CN:end eea14f0ebabc24ff -->

#### Evidence and cross-check

<!-- zh-CN:begin ba3fdbd151f3bfd5 -->

#### 证据与交叉核对

<!-- zh-CN:end ba3fdbd151f3bfd5 -->

- Show the menu path and final control state. Check the preference value read-only.

<!-- zh-CN:begin a1f10cc8390fd997 -->

- 展示菜单路径和最终控件状态；只读检查偏好值。

<!-- zh-CN:end a1f10cc8390fd997 -->

#### Gotchas

<!-- zh-CN:begin b7c67071b90c4e59 -->

#### 易错点

<!-- zh-CN:end b7c67071b90c4e59 -->

- Operating-system settings are a different surface.

<!-- zh-CN:begin 596a3b7da6245f35 -->

- 操作系统设置是不同界面。

<!-- zh-CN:end 596a3b7da6245f35 -->

## Completeness checklist

<!-- zh-CN:begin 5ce6868048bdf3cf -->

## 完整性清单

<!-- zh-CN:end 5ce6868048bdf3cf -->

- Every reproducible user-facing feature has a section.

<!-- zh-CN:begin 221b581341de5a06 -->

- 每个可复现用户功能都有章节。

<!-- zh-CN:end 221b581341de5a06 -->
- Every section names a user path, adapter actions, and reset.

<!-- zh-CN:begin 1e3130fa6f70e5ff -->

- 每节列出用户路径、适配器动作和重置。

<!-- zh-CN:end 1e3130fa6f70e5ff -->
- Selectors use roles, names, ARIA, stable component markers, or purpose-named attributes.

<!-- zh-CN:begin aa61fee745f3f769 -->

- 选择器使用角色、名称、ARIA、稳定组件标记或用途属性。

<!-- zh-CN:end aa61fee745f3f769 -->
- No selector uses generated classes or DOM position.

<!-- zh-CN:begin 11704c1949cea3ec -->

- 不用生成类或DOM位置。

<!-- zh-CN:end 11704c1949cea3ec -->
- Relevant interaction, loading, empty, error, selected, and expanded states are covered.

<!-- zh-CN:begin da5de006a8c8eafe -->

- 覆盖相关交互、加载、空、错误、选中和展开状态。

<!-- zh-CN:end da5de006a8c8eafe -->
- Auth, fixtures, permissions, flags, and services are explicit.

<!-- zh-CN:begin f9ce80c28ca8dc1b -->

- 明确认证、夹具、权限、标志和服务。

<!-- zh-CN:end f9ce80c28ca8dc1b -->
- Screenshot, video, and underlying cross-check requirements are explicit.

<!-- zh-CN:begin 9f7d22554b8ae393 -->

- 明确截图、视频和底层交叉核对。

<!-- zh-CN:end 9f7d22554b8ae393 -->
- Wrong surfaces, dead ends, and safe environment translations are listed.

<!-- zh-CN:begin 33e415e6d7cddaf8 -->

- 列出错误界面、死路和安全环境转换。

<!-- zh-CN:end 33e415e6d7cddaf8 -->
- Implementation details remain runtime discoveries.

<!-- zh-CN:begin 7499cc30f8912c14 -->

- 实现细节保持为运行时发现。

<!-- zh-CN:end 7499cc30f8912c14 -->
