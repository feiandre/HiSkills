# Routing map example

<!-- zh-CN:begin 0a4e2ea2b9c960fe -->

# 路由图示例

<!-- zh-CN:end 0a4e2ea2b9c960fe -->

Copy this file outside `.cursor/automations/benny/`, for example to `.cursor/benny/routing.md`, and replace every placeholder. Point `routing.map_path` at the copy. Pack refreshes must not overwrite it.

<!-- zh-CN:begin 568ff6436ba97b0e -->

将此文件复制到 `.cursor/automations/benny/` 之外，例如 `.cursor/benny/routing.md`，并替换每个占位符。将 `routing.map_path` 指向副本。刷新包时不得覆盖它。

<!-- zh-CN:end 568ff6436ba97b0e -->

The triage skill treats this as data. A route needs evidence from the report or cause trace. A keyword match alone is not enough.

<!-- zh-CN:begin bdd652726d4f0dae -->

分诊技能将本文件视为数据。路由需要报告或原因追踪中的证据。仅关键词匹配不够。

<!-- zh-CN:end bdd652726d4f0dae -->

```yaml
routes:
  - name: "billing-example"
    match:
      product_areas:
        - "billing-area-placeholder"
      code_paths:
        - "billing-code-path-placeholder"
      error_signatures:
        - "billing-error-placeholder"
    destination:
      slack_channel: "billing-channel-placeholder"
      tracker_team: "billing-team-placeholder"
    owners:
      - "billing-owner-placeholder"
    allow_feature_owner_ping: false

  - name: "desktop-example"
    match:
      product_areas:
        - "desktop-area-placeholder"
      code_paths:
        - "desktop-code-path-placeholder"
      error_signatures:
        - "desktop-error-placeholder"
    destination:
      slack_channel: "desktop-channel-placeholder"
      tracker_team: "desktop-team-placeholder"
    owners:
      - "desktop-owner-placeholder"
    allow_feature_owner_ping: false

fallback:
  destination: ""
  owners: []
  allow_feature_owner_ping: false

ping_policy:
  default: "off"
  allow:
    - "configured-feature-owner"
    - "confirmed-regression-author"
  deny:
    - "broad-on-call-group"
    - "unverified-owner"
```

## Rules

<!-- zh-CN:begin 7c4862307710f905 -->

## 规则

<!-- zh-CN:end 7c4862307710f905 -->

- Leave `fallback.destination` empty unless one team accepts all unmatched reports.

<!-- zh-CN:begin 3f7293f71d754764 -->

- 除非一个团队接收所有未匹配报告，否则让 `fallback.destination` 留空。

<!-- zh-CN:end 3f7293f71d754764 -->
- Use stable product areas, code paths, and error signatures.

<!-- zh-CN:begin d833b8f2a0e5c88e -->

- 使用稳定的产品区域、代码路径和错误签名。

<!-- zh-CN:end d833b8f2a0e5c88e -->
- Do not include private data in a public copy.

<!-- zh-CN:begin 1e6c08d138f66a1e -->

- 不要在公开副本中包含私有数据。

<!-- zh-CN:end 1e6c08d138f66a1e -->
- Do not paste raw user or channel IDs into an example that will be published.

<!-- zh-CN:begin 319498a19b09f9dd -->

- 不要粘贴原始用户或频道 ID 到将发布的示例。

<!-- zh-CN:end 319498a19b09f9dd -->
- Keep feature-owner pings off until the target team agrees to them.

<!-- zh-CN:begin 469b93c78a1343ef -->

- 在目标团队同意前保持功能所有者 ping 关闭。

<!-- zh-CN:end 469b93c78a1343ef -->
- A reroute tells the reporter where to go. The automation never cross-posts.

<!-- zh-CN:begin 7ed804e54934e2d7 -->

- 改路由会告诉报告者去向。自动化绝不跨帖。

<!-- zh-CN:end 7ed804e54934e2d7 -->
