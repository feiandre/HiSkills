# Control-adapter contract

<!-- zh-CN:begin ba63f89264c41b82 -->

# 控制适配器契约

<!-- zh-CN:end ba63f89264c41b82 -->

Benny does not know how to start or drive every app. The user must configure one control skill or adapter that implements this contract for the target app.

<!-- zh-CN:begin 457ba9d70f3e9244 -->

Benny 并不知道如何启动或驱动每个应用。用户必须为目标应用配置一个实现本契约的控制技能或适配器。

<!-- zh-CN:end 457ba9d70f3e9244 -->

Set its skill name in `control.skill_name`.

<!-- zh-CN:begin 8682d6447fd4d313 -->

在 `control.skill_name` 中设置其技能名称。

<!-- zh-CN:end 8682d6447fd4d313 -->

Set the completed user-facing feature map path in `control.feature_map_path`. Copy and fill [`feature-map.example.md`](./feature-map.example.md) outside `.cursor/automations/benny/` instead of editing the copied example.

<!-- zh-CN:begin a8b7539d0bab73be -->

在 `control.feature_map_path` 中设置已完成的面向用户功能图路径。将 [`feature-map.example.md`](./feature-map.example.md) 复制并填写到 `.cursor/automations/benny/` 之外，而非编辑已复制的示例。

<!-- zh-CN:end a8b7539d0bab73be -->

If the skill, feature map, or a required capability is absent, ambiguous, or incomplete, repro and fix work must fail closed.

<!-- zh-CN:begin 869c822fa5b31e26 -->

若技能、功能图或任何必需能力缺失、含糊或不完整，复现与修复工作必须以失败关闭方式终止。

<!-- zh-CN:end 869c822fa5b31e26 -->

## Required capabilities

<!-- zh-CN:begin 717e48873d302de1 -->

## 必需能力

<!-- zh-CN:end 717e48873d302de1 -->

### Bring up

<!-- zh-CN:begin 43522107089eb967 -->

### 启动

<!-- zh-CN:end 43522107089eb967 -->

Start the requested app revision in the requested test environment.

<!-- zh-CN:begin 674819aba1ac71f4 -->

在请求的测试环境中启动请求的应用修订版。

<!-- zh-CN:end 674819aba1ac71f4 -->

Input:

<!-- zh-CN:begin a52a169918a78f09 -->

输入：

<!-- zh-CN:end a52a169918a78f09 -->

- Repository and revision

<!-- zh-CN:begin bc74eee248748c76 -->

- 仓库和修订版

<!-- zh-CN:end bc74eee248748c76 -->
- Build or start mode

<!-- zh-CN:begin 32d6f0b8d5c6a529 -->

- 构建或启动模式

<!-- zh-CN:end 32d6f0b8d5c6a529 -->
- Workspace, account, fixture, and feature-state requirements

<!-- zh-CN:begin 58655fc470a082a6 -->

- 工作区、账户、夹具和功能状态要求

<!-- zh-CN:end 58655fc470a082a6 -->
- Artifact directory

<!-- zh-CN:begin 6626e97b4f375fd7 -->

- 制品目录

<!-- zh-CN:end 6626e97b4f375fd7 -->
- Completed feature-map path

<!-- zh-CN:begin 7e7b9efc39e77d03 -->

- 已完成功能图路径

<!-- zh-CN:end 7e7b9efc39e77d03 -->

Return:

<!-- zh-CN:begin 3fec9d0ef658ca5c -->

返回：

<!-- zh-CN:end 3fec9d0ef658ca5c -->

- Session identifier

<!-- zh-CN:begin 2cf190af80935549 -->

- 会话标识符

<!-- zh-CN:end 2cf190af80935549 -->
- How the adapter confirmed the correct app and environment

<!-- zh-CN:begin 0015e7a032db7285 -->

- 适配器如何确认正确的应用与环境

<!-- zh-CN:end 0015e7a032db7285 -->
- Stable app markers

<!-- zh-CN:begin f3317e6fa0dad417 -->

- 稳定应用标记

<!-- zh-CN:end f3317e6fa0dad417 -->
- Running process or target details needed by later calls

<!-- zh-CN:begin 45ef52ecd48808b1 -->

- 后续调用所需的运行进程或目标详情

<!-- zh-CN:end 45ef52ecd48808b1 -->
- Any missing capability

<!-- zh-CN:begin 77864742034bd473 -->

- 任何缺失能力

<!-- zh-CN:end 77864742034bd473 -->

The adapter must distinguish the target app from a similar window, shell, or production instance.

<!-- zh-CN:begin 052016c4ae50f1b3 -->

适配器必须将目标应用与相似窗口、shell 或生产实例区分开。

<!-- zh-CN:end 052016c4ae50f1b3 -->

### Drive UI

<!-- zh-CN:begin 760a5e3417d9359c -->

### 驱动 UI

<!-- zh-CN:end 760a5e3417d9359c -->

Perform real user actions:

<!-- zh-CN:begin 4a162a98d51b8b7a -->

执行真实用户动作：

<!-- zh-CN:end 4a162a98d51b8b7a -->

- Click

<!-- zh-CN:begin 5633e4a58bb3b48d -->

- 点击

<!-- zh-CN:end 5633e4a58bb3b48d -->
- Type

<!-- zh-CN:begin f8e4872dbacbb81c -->

- 输入

<!-- zh-CN:end f8e4872dbacbb81c -->
- Press keys

<!-- zh-CN:begin f605d8de487d2c99 -->

- 按键

<!-- zh-CN:end f605d8de487d2c99 -->
- Scroll

<!-- zh-CN:begin 917e1fe7bc2a1f4b -->

- 滚动

<!-- zh-CN:end 917e1fe7bc2a1f4b -->
- Drag

<!-- zh-CN:begin d818c8d708fa1091 -->

- 拖动

<!-- zh-CN:end d818c8d708fa1091 -->
- Resize

<!-- zh-CN:begin fb79919d5429ec3d -->

- 调整大小

<!-- zh-CN:end fb79919d5429ec3d -->
- Navigate through app controls

<!-- zh-CN:begin 6e0f0ba446265f99 -->

- 通过应用控件导航

<!-- zh-CN:end 6e0f0ba446265f99 -->

Prefer roles, labels, and stable selectors. Use coordinates only after a fresh screenshot.

<!-- zh-CN:begin 288a694792b01041 -->

优先使用角色、标签和稳定选择器。只有在获取新截图后才使用坐标。

<!-- zh-CN:end 288a694792b01041 -->

Return each action and the observed state change.

<!-- zh-CN:begin a0edbeeaf9d8bf9c -->

返回每个动作及观察到的状态变化。

<!-- zh-CN:end a0edbeeaf9d8bf9c -->

Do not set internal state, call hidden app methods, write directly to storage, or inject DOM changes to create the symptom.

<!-- zh-CN:begin 953273e04c1134eb -->

不要设置内部状态、调用隐藏应用方法、直接写存储或注入 DOM 改动来制造症状。

<!-- zh-CN:end 953273e04c1134eb -->

### Drive mapped features and states

<!-- zh-CN:begin 5bdc53c080d1d1da -->

### 驱动已映射功能与状态

<!-- zh-CN:end 5bdc53c080d1d1da -->

Read the relevant feature-map section before driving the app.

<!-- zh-CN:begin 16ac75f1fea5ead3 -->

驱动应用前阅读相关功能图部分。

<!-- zh-CN:end 16ac75f1fea5ead3 -->

The adapter must expose ways to:

<!-- zh-CN:begin 7cab7b038b65d85d -->

适配器必须提供以下方式：

<!-- zh-CN:end 7cab7b038b65d85d -->

- Navigate every mapped feature through the user-visible path.

<!-- zh-CN:begin 19f0e592175c322f -->

- 沿用户可见路径导航每个已映射功能。

<!-- zh-CN:end 19f0e592175c322f -->
- Invoke the adapter action names listed for that feature.

<!-- zh-CN:begin 8514966c5eb93cf0 -->

- 调用该功能列出的适配器动作名。

<!-- zh-CN:end 8514966c5eb93cf0 -->
- Interact with default, hover, focus-visible, active, disabled, loading, empty, error, selected, open, expanded, and feature-specific states when they apply.

<!-- zh-CN:begin a7f1b2ed4009bb8c -->

- 适用时与默认、悬停、焦点可见、活动、禁用、加载、空、错误、选中、打开、展开及功能专属状态交互。

<!-- zh-CN:end a7f1b2ed4009bb8c -->
- Arrange a state through safe fixture data, permissions, flags, service responses, or supported test controls.

<!-- zh-CN:begin 37a870541a18f853 -->

- 通过安全夹具数据、权限、标志、服务响应或支持的测试控件安排状态。

<!-- zh-CN:end 37a870541a18f853 -->
- Reset the feature for a second independent repro attempt.

<!-- zh-CN:begin 859619efc61b19cf -->

- 重置功能以进行第二次独立复现尝试。

<!-- zh-CN:end 859619efc61b19cf -->
- Capture the screenshot, video, and read-only cross-check named by the feature map.

<!-- zh-CN:begin d0d4b292fe7b5d29 -->

- 捕获功能图指定的截图、视频及只读交叉检查。

<!-- zh-CN:end d0d4b292fe7b5d29 -->

Use roles, accessible names, ARIA relationships, stable component markers, and purpose-named data attributes. Never use generated CSS or StyleX classes, dynamic hashes, child indexes, or brittle DOM position.

<!-- zh-CN:begin 0275cfbd768c82ae -->

使用角色、可访问名称、ARIA 关系、稳定组件标记和按用途命名的 data 属性。绝不要使用生成的 CSS 或 StyleX 类、动态哈希、子元素索引或脆弱的 DOM 位置。

<!-- zh-CN:end 0275cfbd768c82ae -->

Arranging a precondition is not permission to inject the reported symptom. The repro itself must still come from real user interaction.

<!-- zh-CN:begin 51e30b1f60e8cf23 -->

安排前置条件不表示可以注入所报告症状。复现本身仍必须来自真实用户交互。

<!-- zh-CN:end 51e30b1f60e8cf23 -->

### Inspect state

<!-- zh-CN:begin 455b345fb6e267b4 -->

### 检查状态

<!-- zh-CN:end 455b345fb6e267b4 -->

Read state to confirm what the UI shows.

<!-- zh-CN:begin 0944609616183694 -->

读取状态以确认 UI 显示的内容。

<!-- zh-CN:end 0944609616183694 -->

Examples:

<!-- zh-CN:begin 0ef529f44fd6bfbb -->

示例：

<!-- zh-CN:end 0ef529f44fd6bfbb -->

- Accessibility tree

<!-- zh-CN:begin 530861fbd0634f28 -->

- 无障碍树

<!-- zh-CN:end 530861fbd0634f28 -->
- DOM or view hierarchy

<!-- zh-CN:begin 901b91b3a03f685b -->

- DOM 或视图层级

<!-- zh-CN:end 901b91b3a03f685b -->
- Process state

<!-- zh-CN:begin 684680e1374469f3 -->

- 进程状态

<!-- zh-CN:end 684680e1374469f3 -->
- Local logs

<!-- zh-CN:begin f0c212bbb5a68900 -->

- 本地日志

<!-- zh-CN:end f0c212bbb5a68900 -->
- Network request status

<!-- zh-CN:begin b24578ec0a94fb00 -->

- 网络请求状态

<!-- zh-CN:end b24578ec0a94fb00 -->
- App-exposed debug state

<!-- zh-CN:begin cc08a28b2e3cb5bb -->

- 应用公开的调试状态

<!-- zh-CN:end cc08a28b2e3cb5bb -->

Inspection is read-only. If a query changes state, it belongs in `drive UI` and must represent a real user action.

<!-- zh-CN:begin e74cc248b04daa16 -->

检查只读。若查询改变状态，它属于 `drive UI`，且必须代表真实用户动作。

<!-- zh-CN:end e74cc248b04daa16 -->

### Screenshot

<!-- zh-CN:begin 8fe98a9c8773cbe2 -->

### 截图

<!-- zh-CN:end 8fe98a9c8773cbe2 -->

Capture the current app state to a requested path.

<!-- zh-CN:begin 97a9dd212e81b38e -->

将当前应用状态捕获到请求路径。

<!-- zh-CN:end 97a9dd212e81b38e -->

Return:

<!-- zh-CN:begin b869161984909932 -->

返回：

<!-- zh-CN:end b869161984909932 -->

- File path

<!-- zh-CN:begin 46c82e92b9a62f36 -->

- 文件路径

<!-- zh-CN:end 46c82e92b9a62f36 -->
- Capture time

<!-- zh-CN:begin 9944e2cce60ea3ac -->

- 捕获时间

<!-- zh-CN:end 9944e2cce60ea3ac -->
- App marker or window title

<!-- zh-CN:begin aaf1747d2792f22a -->

- 应用标记或窗口标题

<!-- zh-CN:end aaf1747d2792f22a -->
- Short description of what should be visible

<!-- zh-CN:begin 7cdea19812402b6e -->

- 应可见内容的简短说明

<!-- zh-CN:end 7cdea19812402b6e -->

The screenshot must show enough app chrome to prove that the correct app is under test.

<!-- zh-CN:begin 4444c8d8239e0556 -->

截图必须显示足够应用界面框架，证明测试的是正确应用。

<!-- zh-CN:end 4444c8d8239e0556 -->

### Recording

<!-- zh-CN:begin f8f2797159725c42 -->

### 录制

<!-- zh-CN:end f8f2797159725c42 -->

Start and stop a screen recording around the full repro path.

<!-- zh-CN:begin 70b4f7a2561adf2b -->

围绕完整复现路径开始和停止屏幕录制。

<!-- zh-CN:end 70b4f7a2561adf2b -->

Return:

<!-- zh-CN:begin ffb86c057c28f541 -->

返回：

<!-- zh-CN:end ffb86c057c28f541 -->

- File path

<!-- zh-CN:begin 04df65b978ee9d66 -->

- 文件路径

<!-- zh-CN:end 04df65b978ee9d66 -->
- Start and stop times

<!-- zh-CN:begin 28a9c340a4ae0871 -->

- 开始与停止时间

<!-- zh-CN:end 28a9c340a4ae0871 -->
- Captured window or region

<!-- zh-CN:begin 3b00bdbda57b890a -->

- 捕获的窗口或区域

<!-- zh-CN:end 3b00bdbda57b890a -->
- Whether audio or sensitive overlays were omitted

<!-- zh-CN:begin fe2a31551d761b29 -->

- 是否省略音频或敏感覆盖层

<!-- zh-CN:end fe2a31551d761b29 -->

The recording must show the discriminating final state, not only setup or a loading screen.

<!-- zh-CN:begin 79fd9d806394f0c6 -->

录制必须显示用于区分的最终状态，不只是设置或加载屏幕。

<!-- zh-CN:end 79fd9d806394f0c6 -->

### Cleanup

<!-- zh-CN:begin 26dc301e21de4757 -->

### 清理

<!-- zh-CN:end 26dc301e21de4757 -->

Stop processes and sessions created by the adapter.

<!-- zh-CN:begin 6a12073ba9d6c530 -->

停止适配器创建的进程和会话。

<!-- zh-CN:end 6a12073ba9d6c530 -->

Remove disposable:

<!-- zh-CN:begin adc394602961a785 -->

移除一次性：

<!-- zh-CN:end adc394602961a785 -->

- Browser or app profiles

<!-- zh-CN:begin dd15d1af598a1446 -->

- 浏览器或应用配置

<!-- zh-CN:end dd15d1af598a1446 -->
- Temporary workspaces

<!-- zh-CN:begin b6f4f2fa7f599885 -->

- 临时工作区

<!-- zh-CN:end b6f4f2fa7f599885 -->
- Test accounts or fixtures when the adapter created them

<!-- zh-CN:begin 0874c8092586daa3 -->

- 适配器创建的测试账户或夹具

<!-- zh-CN:end 0874c8092586daa3 -->
- Debug ports and tunnels

<!-- zh-CN:begin cf63658674ef6581 -->

- 调试端口与隧道

<!-- zh-CN:end cf63658674ef6581 -->
- Captures past their retention window

<!-- zh-CN:begin 54c6c7244aaadf6a -->

- 超过保留窗口的捕获内容

<!-- zh-CN:end 54c6c7244aaadf6a -->

Return what was stopped, removed, retained, or left for a person.

<!-- zh-CN:begin ce1a8e259b631ad4 -->

返回停止、移除、保留或留给人类的内容。

<!-- zh-CN:end ce1a8e259b631ad4 -->

Cleanup must not delete user work.

<!-- zh-CN:begin e7455e96008c0210 -->

清理不得删除用户工作。

<!-- zh-CN:end e7455e96008c0210 -->

## Adapter behavior

<!-- zh-CN:begin 2ff1a727495d8342 -->

## 适配器行为

<!-- zh-CN:end 2ff1a727495d8342 -->

The adapter must:

<!-- zh-CN:begin 1fca098e75b0b9da -->

适配器必须：

<!-- zh-CN:end 1fca098e75b0b9da -->

- Report capabilities before the repro starts.

<!-- zh-CN:begin 996263ce1603f557 -->

- 在复现开始前报告能力。

<!-- zh-CN:end 996263ce1603f557 -->
- Report which feature-map sections it can drive and which are blocked.

<!-- zh-CN:begin d77aacb3b41cdece -->

- 报告可驱动哪些功能图部分，以及哪些受阻。

<!-- zh-CN:end d77aacb3b41cdece -->
- Use the same environment inputs for baseline and patched builds.

<!-- zh-CN:begin 2be6b97baff6afd2 -->

- 基线与修补构建使用相同环境输入。

<!-- zh-CN:end 2be6b97baff6afd2 -->
- Surface startup failures as failures.

<!-- zh-CN:begin 52c8a59100a1c20d -->

- 将启动失败作为失败暴露。

<!-- zh-CN:end 52c8a59100a1c20d -->
- Bound retries.

<!-- zh-CN:begin de213ffb4008d726 -->

- 限制重试。

<!-- zh-CN:end de213ffb4008d726 -->
- Keep secrets out of logs and artifacts.

<!-- zh-CN:begin 2bc4677fce0cdfa4 -->

- 使秘密不进入日志和制品。

<!-- zh-CN:end 2bc4677fce0cdfa4 -->
- Keep captures outside the repository.

<!-- zh-CN:begin 713dd10c2faf5791 -->

- 将捕获内容保留在仓库外。

<!-- zh-CN:end 713dd10c2faf5791 -->
- Support a fresh or reset state between the two repro attempts.

<!-- zh-CN:begin aa586a67cd6f1005 -->

- 支持两次复现尝试之间的全新或重置状态。

<!-- zh-CN:end aa586a67cd6f1005 -->
- Avoid production changes unless the user explicitly configured a safe test action.

<!-- zh-CN:begin 114f4fc103b0349b -->

- 除非用户明确配置安全测试动作，否则避免生产改动。

<!-- zh-CN:end 114f4fc103b0349b -->

## Environment translation

<!-- zh-CN:begin 8b7553d29f3306ac -->

## 环境转换

<!-- zh-CN:end 8b7553d29f3306ac -->

Before declaring an environment block, restate the defect without platform-specific nouns and ask whether the same behavior can be tested safely in the available environment.

<!-- zh-CN:begin 025ceecf862528b0 -->

宣布环境阻塞前，先不使用平台专用名词重述缺陷，并询问同一行为能否在可用环境中安全测试。

<!-- zh-CN:end 025ceecf862528b0 -->

Examples:

<!-- zh-CN:begin 140fd493e236a990 -->

示例：

<!-- zh-CN:end 140fd493e236a990 -->

- A named browser may mean any external browser.

<!-- zh-CN:begin 5e98a8ca54383d23 -->

- 指定浏览器可能表示任意外部浏览器。

<!-- zh-CN:end 5e98a8ca54383d23 -->
- A named key may mean the configured shortcut.

<!-- zh-CN:begin 245f84c07bafbb51 -->

- 指定按键可能表示已配置快捷键。

<!-- zh-CN:end 245f84c07bafbb51 -->
- A named remote host may mean a delayed or disconnected remote target.

<!-- zh-CN:begin 9b1a1e94a8e73266 -->

- 指定远程主机可能表示延迟或断开的远程目标。

<!-- zh-CN:end 9b1a1e94a8e73266 -->

Use a translated attempt only when it tests the same underlying behavior. Label it as translated evidence. Do not call it an exact repro when the missing environment is part of the defect.

<!-- zh-CN:begin 7d623e1882606216 -->

只有转换尝试测试相同底层行为时才使用。将其标为转换后的证据。若缺失环境本身是缺陷的一部分，不要称其为精确复现。

<!-- zh-CN:end 7d623e1882606216 -->

Hardware prompts, operating-system permission dialogs, device-only APIs, and unavailable account states may be real blocks.

<!-- zh-CN:begin 1fd0623265e39abd -->

硬件提示、操作系统权限对话框、仅设备 API 和不可用账户状态可能是真实阻塞。

<!-- zh-CN:end 1fd0623265e39abd -->

## Setup check

<!-- zh-CN:begin cfb7540572ee4be3 -->

## 设置检查

<!-- zh-CN:end cfb7540572ee4be3 -->

Before enabling the repro automation, run one harmless adapter check:

<!-- zh-CN:begin a41eb564733c3afc -->

启用复现自动化前，运行一次无害适配器检查：

<!-- zh-CN:end a41eb564733c3afc -->

1. Bring up the app.

<!-- zh-CN:begin 057c2128ea6c605e -->

1. 启动应用。

<!-- zh-CN:end 057c2128ea6c605e -->
2. Confirm the stable app marker.

<!-- zh-CN:begin d5137ae4392ae0dc -->

2. 确认稳定应用标记。

<!-- zh-CN:end d5137ae4392ae0dc -->
3. Load one completed feature-map section.

<!-- zh-CN:begin 88c14bd66a8323c6 -->

3. 加载一个已完成功能图部分。

<!-- zh-CN:end 88c14bd66a8323c6 -->
4. Navigate to that feature through its user path.

<!-- zh-CN:begin 25c2ce210c4c2902 -->

4. 沿用户路径导航到该功能。

<!-- zh-CN:end 25c2ce210c4c2902 -->
5. Exercise one disposable state through mapped adapter actions.

<!-- zh-CN:begin fc9c897caacf8b5e -->

5. 通过映射适配器动作操作一个一次性状态。

<!-- zh-CN:end fc9c897caacf8b5e -->
6. Inspect the resulting state.

<!-- zh-CN:begin 72ca2d5f79ffdb79 -->

6. 检查结果状态。

<!-- zh-CN:end 72ca2d5f79ffdb79 -->
7. Capture a screenshot.

<!-- zh-CN:begin b527e6748e9c558f -->

7. 捕获截图。

<!-- zh-CN:end b527e6748e9c558f -->
8. Record a short clip.

<!-- zh-CN:begin 7fbf0db9b3ca2a9a -->

8. 录制短片。

<!-- zh-CN:end 7fbf0db9b3ca2a9a -->
9. Clean up.

<!-- zh-CN:begin 2003ee233b7f965d -->

9. 清理。

<!-- zh-CN:end 2003ee233b7f965d -->

Enable repro work only when all nine steps succeed and no source-channel Slack post is involved.

<!-- zh-CN:begin 0e4a07cf6b0106b4 -->

只有九步全部成功且不涉及 source-channel Slack 帖子时，才启用复现工作。

<!-- zh-CN:end 0e4a07cf6b0106b4 -->
