# Verify an existing fix

<!-- zh-CN:begin aad650e3399f03a7 -->

# 验证现有修复

<!-- zh-CN:end aad650e3399f03a7 -->

Use this mode when an open pull request or merged commit plausibly fixes the report.

<!-- zh-CN:begin 2b7984b5e913d34b -->

当开放的拉取请求或已合并提交看起来能修复报告时，使用此模式。

<!-- zh-CN:end 2b7984b5e913d34b -->

The existing artifact owns the fix. Verify it. Do not edit it, author a competing patch, or open another pull request.

<!-- zh-CN:begin 4450a0d6aaa0eceb -->

现有产物负责修复。验证它。不要编辑它、编写竞争补丁或另开拉取请求。

<!-- zh-CN:end 4450a0d6aaa0eceb -->

## Qualify the artifact

<!-- zh-CN:begin 047a7a954df9fac1 -->

## 确认产物资格

<!-- zh-CN:end 047a7a954df9fac1 -->

Require one concrete artifact:

<!-- zh-CN:begin 36a2ccc3f6e00869 -->

要求一个具体产物：

<!-- zh-CN:end 36a2ccc3f6e00869 -->

- An open pull request with code changes that address the symptom

<!-- zh-CN:begin e47cf4c526025ec2 -->

- 包含针对症状代码变更的开放拉取请求

<!-- zh-CN:end e47cf4c526025ec2 -->
- A merged pull request

<!-- zh-CN:begin 63d2b4ce86ed6a39 -->

- 已合并的拉取请求

<!-- zh-CN:end 63d2b4ce86ed6a39 -->
- A merged commit with matching code and intent

<!-- zh-CN:begin d84725e8cc27503d -->

- 代码与意图匹配的已合并提交

<!-- zh-CN:end d84725e8cc27503d -->

A thread claim, tracker status, branch name, or cause hypothesis without a pull request or commit is not enough.

<!-- zh-CN:begin ff6f4ae4e15e4ddd -->

线程中的说法、跟踪器状态、分支名称或原因假设，若没有拉取请求或提交，不足够。

<!-- zh-CN:end ff6f4ae4e15e4ddd -->

When several artifacts exist, choose the one linked from the source thread or tracker. Otherwise choose the closest match to the affected code and state why.

<!-- zh-CN:begin 2c7520a01729312c -->

存在多个产物时，选择源线程或跟踪器链接的那个。否则选择与受影响代码最接近的，并说明原因。

<!-- zh-CN:end 2c7520a01729312c -->

## Protect the working tree

<!-- zh-CN:begin cacd8b999bd69013 -->

## 保护工作树

<!-- zh-CN:end cacd8b999bd69013 -->

Use an isolated worktree or another clean checkout when the repository supports it. Do not overwrite user changes.

<!-- zh-CN:begin 3a18dc13053ae1a3 -->

仓库支持时使用独立工作树或其他干净检出。不要覆盖用户变更。

<!-- zh-CN:end 3a18dc13053ae1a3 -->

Record:

<!-- zh-CN:begin e356783db9872ca5 -->

记录：

<!-- zh-CN:end e356783db9872ca5 -->

- Baseline revision

<!-- zh-CN:begin eabff6e796a608b6 -->

- 基线修订

<!-- zh-CN:end eabff6e796a608b6 -->
- Patched revision

<!-- zh-CN:begin 592e8b511b232cc0 -->

- 打补丁后的修订

<!-- zh-CN:end 592e8b511b232cc0 -->
- Pull request or commit URL

<!-- zh-CN:begin 9ab2e4bd3b6d6d2c -->

- 拉取请求或提交 URL

<!-- zh-CN:end 9ab2e4bd3b6d6d2c -->
- Build and environment inputs shared by both runs

<!-- zh-CN:begin 486ac4bf2458ff9b -->

- 两次运行共用的构建与环境输入

<!-- zh-CN:end 486ac4bf2458ff9b -->

Use regular `github.com` pull request links.

<!-- zh-CN:begin 5710beb59dca38b7 -->

使用常规 `github.com` 拉取请求链接。

<!-- zh-CN:end 5710beb59dca38b7 -->

## Measure the baseline

<!-- zh-CN:begin a6c2c2550616cdcc -->

## 测量基线

<!-- zh-CN:end a6c2c2550616cdcc -->

For an open pull request, use its base branch as the baseline.

<!-- zh-CN:begin 43f2db3813be3c48 -->

对开放拉取请求，以基分支为基线。

<!-- zh-CN:end 43f2db3813be3c48 -->

For a merged fix, use the revision immediately before the fix when that revision builds and represents the old behavior.

<!-- zh-CN:begin 58c240a59549b0a8 -->

对已合并修复，若紧邻修复前的修订可构建并代表旧行为，则使用该修订。

<!-- zh-CN:end 58c240a59549b0a8 -->

Through the configured control adapter:

<!-- zh-CN:begin df77274e9ac3600b -->

通过配置的控制适配器：

<!-- zh-CN:end df77274e9ac3600b -->

1. Bring up the baseline app.

<!-- zh-CN:begin 3713b54773e65067 -->

1. 启动基线应用。

<!-- zh-CN:end 3713b54773e65067 -->
2. Confirm the correct app and environment.

<!-- zh-CN:begin e5cafe5ffda672f4 -->

2. 确认应用和环境正确。

<!-- zh-CN:end e5cafe5ffda672f4 -->
3. Run the reported path through real UI actions.

<!-- zh-CN:begin 84310498e47f7eaa -->

3. 通过真实 UI 操作运行报告中的路径。

<!-- zh-CN:end 84310498e47f7eaa -->
4. Observe the discriminating symptom.

<!-- zh-CN:begin 40aa307e9a5c5ec3 -->

4. 观察可区分症状。

<!-- zh-CN:end 40aa307e9a5c5ec3 -->
5. Reset and repeat it.

<!-- zh-CN:begin 5babfdc327f83c29 -->

5. 重置并重复。

<!-- zh-CN:end 5babfdc327f83c29 -->
6. Capture baseline recording, screenshot, and state check.

<!-- zh-CN:begin 47ed849d79a01100 -->

6. 捕获基线录像、截图和状态检查。

<!-- zh-CN:end 47ed849d79a01100 -->

If the symptom does not appear twice on the baseline, there is no baseline. Do not claim that the fix works.

<!-- zh-CN:begin f3026e294e5f2e87 -->

如果症状未在基线出现两次，就没有基线。不要声称修复有效。

<!-- zh-CN:end f3026e294e5f2e87 -->

## Measure the patched build

<!-- zh-CN:begin dfe9399568b3dc96 -->

## 测量打补丁构建

<!-- zh-CN:end dfe9399568b3dc96 -->

Build and run the pull request or fix commit with the same environment and data.

<!-- zh-CN:begin 1f2d76b7670d50e6 -->

用相同环境和数据构建并运行拉取请求或修复提交。

<!-- zh-CN:end 1f2d76b7670d50e6 -->

1. Run the same UI path.

<!-- zh-CN:begin aa0e92b2dd73b637 -->

1. 运行相同 UI 路径。

<!-- zh-CN:end aa0e92b2dd73b637 -->
2. Repeat it twice.

<!-- zh-CN:begin 477d97b2a70e3fac -->

2. 重复两次。

<!-- zh-CN:end 477d97b2a70e3fac -->
3. Confirm that the broken state is gone.

<!-- zh-CN:begin 8b37e4e4990724d2 -->

3. 确认故障状态消失。

<!-- zh-CN:end 8b37e4e4990724d2 -->
4. Confirm the expected state appears.

<!-- zh-CN:begin 69cdf068047824e8 -->

4. 确认预期状态出现。

<!-- zh-CN:end 69cdf068047824e8 -->
5. Capture after recording, screenshot, and the same state check.

<!-- zh-CN:begin 06a2715f483ed01b -->

5. 捕获修复后录像、截图和相同状态检查。

<!-- zh-CN:end 06a2715f483ed01b -->

Do not stop at compilation or tests. The after result must come from a running patched app.

<!-- zh-CN:begin 32b37a7768b0e111 -->

不要止步于编译或测试。修复后结果必须来自运行中的打补丁应用。

<!-- zh-CN:end 32b37a7768b0e111 -->

## Outcomes

<!-- zh-CN:begin dd6fccb175ce7877 -->

## 结果

<!-- zh-CN:end dd6fccb175ce7877 -->

### Confirmed

<!-- zh-CN:begin a00c1f141170e9ca -->

### 已确认

<!-- zh-CN:end a00c1f141170e9ca -->

The baseline reproduces twice and the patched build resolves it twice.

<!-- zh-CN:begin 8cef383fc465413e -->

基线复现两次，打补丁构建解决两次。

<!-- zh-CN:end 8cef383fc465413e -->

- Mark operations status as verified.

<!-- zh-CN:begin e4325812ff970f6e -->

- 将操作状态标为已验证。

<!-- zh-CN:end e4325812ff970f6e -->
- Link the artifact.

<!-- zh-CN:begin c19729dd1ace7b99 -->

- 链接产物。

<!-- zh-CN:end c19729dd1ace7b99 -->
- Post one concise source-thread reply after the source preflight.

<!-- zh-CN:begin a424057a91d2f4b2 -->

- 源线程预检后发布一条简洁回复。

<!-- zh-CN:end a424057a91d2f4b2 -->
- Include the before and after result.

<!-- zh-CN:begin 213d4a1e44892308 -->

- 包含前后结果。

<!-- zh-CN:end 213d4a1e44892308 -->
- Open no pull request.

<!-- zh-CN:begin dca9eb815c5483c6 -->

- 不创建拉取请求。

<!-- zh-CN:end dca9eb815c5483c6 -->

### Insufficient fix

<!-- zh-CN:begin bb5fbf0359551135 -->

### 修复不足

<!-- zh-CN:end bb5fbf0359551135 -->

The symptom appears on both baseline and patched builds.

<!-- zh-CN:begin 4c7a2168bf40eda3 -->

症状在基线和打补丁构建上都出现。

<!-- zh-CN:end 4c7a2168bf40eda3 -->

- Mark operations status as reproduced but not fixed.

<!-- zh-CN:begin 32a560d82ac24f5e -->

- 将操作状态标为已复现但未修复。

<!-- zh-CN:end 32a560d82ac24f5e -->
- Link the artifact and say it did not resolve the symptom.

<!-- zh-CN:begin 87ad0ff15977b1c1 -->

- 链接产物并说明它未解决症状。

<!-- zh-CN:end 87ad0ff15977b1c1 -->
- Post the normal confirmed-repro source update if the run has not already used it.

<!-- zh-CN:begin 9c626ab623028c48 -->

- 若本次运行尚未使用，发布常规的已确认复现源线程更新。

<!-- zh-CN:end 9c626ab623028c48 -->
- Open no competing pull request.

<!-- zh-CN:begin 3e9240ea842c6c41 -->

- 不创建竞争拉取请求。

<!-- zh-CN:end 3e9240ea842c6c41 -->

### Inconclusive

<!-- zh-CN:begin 653842b7b8228914 -->

### 无法确定

<!-- zh-CN:end 653842b7b8228914 -->

The baseline does not reproduce, the patched app cannot run, or the evidence does not show the discriminating state.

<!-- zh-CN:begin f82720a7bcd6b058 -->

基线未复现、打补丁应用无法运行，或证据未显示可区分状态。

<!-- zh-CN:end f82720a7bcd6b058 -->

- Do not claim success.

<!-- zh-CN:begin f19acb43978fa6e0 -->

- 不要声称成功。

<!-- zh-CN:end f19acb43978fa6e0 -->
- State which half could not be measured.

<!-- zh-CN:begin 3f060b10b8e9813b -->

- 说明哪一半无法测量。

<!-- zh-CN:end 3f060b10b8e9813b -->
- Keep the result in the operations thread or run output.

<!-- zh-CN:begin d444459ec5f305bb -->

- 将结果保留在操作线程或运行输出中。

<!-- zh-CN:end d444459ec5f305bb -->
- Post nothing in the source thread unless a direct question requires an answer.

<!-- zh-CN:begin ffa6d4775894c3b8 -->

- 除非直接问题需要回答，否则源线程中不发布内容。

<!-- zh-CN:end ffa6d4775894c3b8 -->

## Cleanup

<!-- zh-CN:begin ddd5edf3ec90c29c -->

## 清理

<!-- zh-CN:end ddd5edf3ec90c29c -->

Stop both builds, remove temporary profiles and captures according to retention policy, and return the repository to its prior state without discarding user work.

<!-- zh-CN:begin e6bb2ba1d6c888a0 -->

停止两个构建，按保留策略删除临时配置文件和捕获材料，并在不丢弃用户工作的前提下将仓库恢复到先前状态。

<!-- zh-CN:end e6bb2ba1d6c888a0 -->
