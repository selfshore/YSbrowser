# YSContext

[SDK API 目录](../api-reference.md) · [使用章节](../browser-context.md)

## 导入与准备

```python
from ysbrowser_sdk.sync_api import YSBrowser, ContextOptions, FingerprintProfile, Direct

# browser 为已启动的 YSBrowser；使用完后关闭 browser。
context = browser.new_context(name="account-001")
# page = context.new_page()，仅在需要页面的方法示例前创建。
```

## 构造参数

```python signature
YSContext(owner: 'YSBrowser', raw: 'BrowserContext', context_id: 'str', name: 'str')
```

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `owner` | YSBrowser | `必填` | 所属浏览器；YSContext 由 browser.new_context() 创建，不建议直接构造。 |
| `raw` | BrowserContext | `必填` | 原生 Context；由 SDK 管理其归属与生命周期。 |
| `context_id` | str | `必填` | 相关浏览器 Context ID；无相关 Context 时为 None。 |
| `name` | str | `必填` | 当前浏览器中唯一的 Context 名称；创建时 None 自动命名，查询/关闭时须为已有名称。 |


## 实例属性

`name: str` 为 SDK 名称；`context_id: str` 为浏览器 ID；`raw` 是原生 BrowserContext。通过 browser.new_context 创建，不手动组装构造参数。

## 方法与属性索引

- [YSContext.capture_diagnostics](#yscontext-capture-diagnostics)
- [YSContext.check_proxy](#yscontext-check-proxy)
- [YSContext.close](#yscontext-close)
- [YSContext.diagnostics](#yscontext-diagnostics)
- [YSContext.export_config](#yscontext-export-config)
- [YSContext.fingerprint_status](#yscontext-fingerprint-status)
- [YSContext.mouse](#yscontext-mouse)
- [YSContext.new_page](#yscontext-new-page)
- [YSContext.proxy_status](#yscontext-proxy-status)
- [YSContext.restore_storage_state](#yscontext-restore-storage-state)
- [YSContext.save_storage_state](#yscontext-save-storage-state)
- [YSContext.set_fingerprint](#yscontext-set-fingerprint)
- [YSContext.set_proxy](#yscontext-set-proxy)
- [YSContext.start_diagnostics](#yscontext-start-diagnostics)
- [YSContext.stop_diagnostics](#yscontext-stop-diagnostics)

## YSContext.capture_diagnostics

在 directory 下新建独立诊断目录，返回包含 report_path、pages、errors、trace 等的字典。page 可限定页面，max_pages 为 1–100，timeout_ms 为每次截图的正有限超时。

```python signature
async capture_diagnostics(directory: 'str | Path', *, page=None, screenshot: 'bool' = True, full_page: 'bool' = False, stop_trace: 'bool' = True, max_pages: 'int' = 5, timeout_ms: 'float' = 5000) -> 'dict'
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `directory` | str \| Path | `必填` | 诊断输出父目录；每次生成独立子目录，返回实际路径。 |
| `page` | Page \| None | `None` | 当前 Context 的原生页面；context.mouse 和鼠标构造必须提供；截图采集省略时选择 Context 页面。 |
| `screenshot` | bool | `True` | 是否保存选中页面的 PNG 截图。 |
| `full_page` | bool | `False` | 是否包含页面完整可滚动区域。 |
| `stop_trace` | bool | `True` | 结束已启动的 SDK trace 并写文件；False 本次不保存 trace，继续录制。 |
| `max_pages` | int | `5` | 最多截图的页面数，1–100。 |
| `timeout_ms` | float | `5000` | 每次截图的正有限毫秒超时，不是总采集预算。 |


### 返回值

返回诊断文件清单 dict；[pages/errors/trace 等嵌套结构](../diagnostics-errors.md#返回字段)。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
report = context.capture_diagnostics("diagnostics", page=page, screenshot=True)
print(report["report_path"], report["pages"])
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
report = await context.capture_diagnostics("diagnostics", page=page, screenshot=True)
```

### 注意事项

同步方法直接调用；标为 await 的方法在异步入口必须等待。页面/Context 关闭后多数操作会抛异常。

[更多示例和完整业务规则](../browser-context.md)

## YSContext.check_proxy

通过当前 Context 做独立出口检查。check_url 为 HTTP(S) URL；timeout_ms 为 1000–60000；expected_exit_ip 可省略。返回 ProxyHealthResult，普通检查失败以 ok=False 表示；命令失败抛 SDKError。

```python signature
async check_proxy(check_url: 'str', *, expected_exit_ip: 'str | None' = None, timeout_ms: 'int' = 10000) -> 'ProxyHealthResult'
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `check_url` | str | `必填` | HTTP(S) 出口检查 URL；不含内嵌账号密码或 fragment；需返回支持格式的出口 IP。 |
| `expected_exit_ip` | str \| None | `None` | 期望的 IPv4/IPv6；None 不做固定 IP 比对。轮换出口不要盲目固定。 |
| `timeout_ms` | int | `10000` | 代理检查超时，整数 1000–60000 毫秒。 |


### 返回值

返回 [ProxyHealthResult](ProxyHealthResult.md)。普通检查失败以 ok=False 表示，命令失败抛 SDKError。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
import os
health = context.check_proxy(os.environ["IP_CHECK_URL"], timeout_ms=10000)
print(health.ok, health.kind, health.exit_ip)
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
import os
health = await context.check_proxy(os.environ["IP_CHECK_URL"], timeout_ms=10000)
```

### 注意事项

同步方法直接调用；标为 await 的方法在异步入口必须等待。页面/Context 关闭后多数操作会抛异常。

[更多示例和完整业务规则](../browser-context.md)

## YSContext.close

关闭当前 Context 的所有页面和采集器，并从浏览器名称索引移除。返回 None。

```python signature
async close() -> 'None'
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

此方法没有调用参数。


### 返回值

返回 None。操作失败时抛异常。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
context.close()
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
await context.close()
```

### 注意事项

同步方法直接调用；标为 await 的方法在异步入口必须等待。页面/Context 关闭后多数操作会抛异常。

[更多示例和完整业务规则](../browser-context.md)

## YSContext.diagnostics

返回 Context 当前状态与近期事件摘要，含 context_id、closed、browser_connected、versions、recent_network_errors、recent_page_events 等字段。

```python signature
async diagnostics() -> 'dict[str, Any]'
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

此方法没有调用参数。


### 返回值

返回 Context 状态 dict；[全部字段](../diagnostics-errors.md#读取-context-状态)。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
info = context.diagnostics()
print(info["closed"], info["recent_network_errors"])
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
info = await context.diagnostics()
```

### 注意事项

同步方法直接调用；标为 await 的方法在异步入口必须等待。页面/Context 关闭后多数操作会抛异常。

[更多示例和完整业务规则](../browser-context.md)

## YSContext.export_config

返回可复用配置 dict；path 非 None 时同时写 JSON。两个 include 开关决定是否包含代理凭据和敏感选项。外部修改导致配置无法确认时抛 CONFIG_CHANGED_EXTERNALLY。

```python signature
async export_config(path: 'str | Path | None' = None, *, include_proxy_credentials: 'bool' = False, include_sensitive_options: 'bool' = False) -> 'dict[str, Any]'
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `path` | str \| Path \| None | `None` | 读写的 JSON 路径；省略的导出/保存只返回字典；load/save 必须提供路径。 |
| `include_proxy_credentials` | bool | `False` | 是否在配置中写出代理账号密码；默认省略并标记需要补齐。 |
| `include_sensitive_options` | bool | `False` | 是否写出网站认证、客户端证书、附加请求头等敏感选项。 |


### 返回值

返回配置 dict；[schema 1/2、proxy 和 options 的嵌套结构](../storage.md#json-格式)。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
data = context.export_config("config/account.json")
print(data["schema_version"])
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
data = await context.export_config("config/account.json")
```

### 注意事项

同步方法直接调用；标为 await 的方法在异步入口必须等待。页面/Context 关闭后多数操作会抛异常。

[更多示例和完整业务规则](../browser-context.md)

## YSContext.fingerprint_status

返回原生状态 dict，主要字段 locked: bool、profile: dict；profile 使用 camelCase 字段。

```python signature
async fingerprint_status() -> 'dict[str, Any]'
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

此方法没有调用参数。


### 返回值

返回 dict：locked（bool，是否锁定）、profile（dict，camelCase 指纹字段）。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
status = context.fingerprint_status()
print(status["locked"])
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
status = await context.fingerprint_status()
```

### 注意事项

同步方法直接调用；标为 await 的方法在异步入口必须等待。页面/Context 关闭后多数操作会抛异常。

[更多示例和完整业务规则](../browser-context.md)

## YSContext.mouse

创建使用随包 Transformer 的鼠标适配器。Page 归属与关闭状态会被检查；不会替换原生 page.mouse。

```python signature
mouse(page: 'Page', *, model: 'TrajectoryModel | str | Path | None' = None, fallback: 'str' = 'error', viewport: 'tuple[float, float] | None' = None, **model_options) -> 'TrajectoryMouse'
```

**同步计算/工厂方法；异步程序中也不加 await。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `page` | Page | `必填` | 当前 Context 的原生页面；context.mouse 和鼠标构造必须提供；截图采集省略时选择 Context 页面。 |
| `model` | TrajectoryModel \| str \| Path \| None | `None` | 模型实例或含 model.json、vector_field.onnx 的目录；None 使用随包模型。 |
| `fallback` | str | `'error'` | 只接受 error。范围/采样错误会抛异常，不替换为其他算法。 |
| `viewport` | tuple[float, float] \| None | `None` | 轨迹边界 (width,height)，均为正数；鼠标省略时读取 Page.viewport_size，离线生成省略则不裁定视口。 |
| `model_options` | 关键字参数 | `展开字段见下表` | steps、threads、drag_source、move_source、click_source、allow_extrapolation；model 为实例时须在实例构造时配置。 |
| `steps`（展开） | int | `24` | ODE 积分步数，4–128；值增大通常增加耗时，不保证效果提高。 |
| `threads`（展开） | int | `2` | ONNX CPU 线程数，1–16。 |
| `drag_source`（展开） | str | `'auto'` | auto 按范围选择 user_mousedata/bogazici/sapimouse，或显式指定其中一个来源。 |
| `move_source`（展开） | str | `'bogazici'` | 普通移动条件来源：bogazici 或 sapimouse。 |
| `click_source`（展开） | str | `'bogazici'` | 接近点击和按住时长条件来源：bogazici 或 sapimouse。 |
| `allow_extrapolation`（展开） | bool | `False` | 允许距离/方向超出已观察范围；True 不代表范围外质量已验证。 |


### 返回值

返回 [TrajectoryMouse](TrajectoryMouse.md)，工厂本身不移动鼠标。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
mouse = context.mouse(page)
result = mouse.move_between(100, 200, 800, 400)
```

### 注意事项

同步方法直接调用；标为 await 的方法在异步入口必须等待。页面/Context 关闭后多数操作会抛异常。

[更多示例和完整业务规则](../browser-context.md)

## YSContext.new_page

创建当前 Context 的页面并返回原生 Page。已关闭或断线时抛 SDKError。

```python signature
async new_page() -> 'Page'
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

此方法没有调用参数。


### 返回值

返回原生 [Page](../native-reference/Page.md)，其操作遵循 Patchright 同步/异步入口。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
page = context.new_page()
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
page = await context.new_page()
```

### 注意事项

同步方法直接调用；标为 await 的方法在异步入口必须等待。页面/Context 关闭后多数操作会抛异常。

[更多示例和完整业务规则](../browser-context.md)

## YSContext.proxy_status

返回 ProxyStatus，仅查询配置与既有检查结果，不发起出口请求。

```python signature
async proxy_status() -> 'ProxyStatus'
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

此方法没有调用参数。


### 返回值

返回 [ProxyStatus](ProxyStatus.md)，字段与嵌套 health 见类型表。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
status = context.proxy_status()
print(status.mode, status.check_state, status.health)
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
status = await context.proxy_status()
```

### 注意事项

同步方法直接调用；标为 await 的方法在异步入口必须等待。页面/Context 关闭后多数操作会抛异常。

[更多示例和完整业务规则](../browser-context.md)

## YSContext.restore_storage_state

state 为原生存储字典或 JSON 文件路径。要求 Context 尚无页面；返回 None。

```python signature
async restore_storage_state(state: 'dict[str, Any] | str | Path') -> 'None'
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `state` | dict[str, Any] \| str \| Path | `必填` | cookies/origins 结构或其 JSON 路径；仅能恢复到尚无页面的 Context。 |


### 返回值

返回 None。操作失败时抛异常。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
context.restore_storage_state("state/account.json")
page = context.new_page()
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
await context.restore_storage_state("state/account.json")
```

### 注意事项

必须在 Context 尚无页面时恢复；之后再 new_page。只恢复 cookies/origins，不恢复 SessionStorage 或页面现场。

[更多示例和完整业务规则](../browser-context.md)

## YSContext.save_storage_state

返回 cookies/origins 结构；默认包含 IndexedDB。path 为可选 JSON 路径。文件与 Context 错误包装为 STORAGE_SAVE_FAILED。

```python signature
async save_storage_state(path: 'str | Path | None' = None, *, indexed_db: 'bool' = True) -> 'dict[str, Any]'
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `path` | str \| Path \| None | `None` | 读写的 JSON 路径；省略的导出/保存只返回字典；load/save 必须提供路径。 |
| `indexed_db` | bool | `True` | 是否把 IndexedDB 包含在登录状态中；不包括 SessionStorage。 |


### 返回值

返回 cookies/origins 字典；[完整结构与字段](../storage.md#保存登录状态)。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
state = context.save_storage_state("state/account.json", indexed_db=True)
print(len(state["cookies"]), len(state["origins"]))
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
state = await context.save_storage_state("state/account.json", indexed_db=True)
```

### 注意事项

同步方法直接调用；标为 await 的方法在异步入口必须等待。页面/Context 关闭后多数操作会抛异常。

[更多示例和完整业务规则](../browser-context.md)

## YSContext.set_fingerprint

profile 为完整 FingerprintProfile。必须在 renderer 创建前设置，成功返回 None，锁定时抛 FingerprintLockedError。

```python signature
async set_fingerprint(profile: 'FingerprintProfile') -> 'None'
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `profile` | FingerprintProfile | `必填` | 完整配置；须在指纹锁定前设置。 |


### 返回值

返回 None。操作失败时抛异常。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
context.set_fingerprint(FingerprintProfile(fpseed="account-001", cpu_cores=8))
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
await context.set_fingerprint(FingerprintProfile(fpseed="account-001", cpu_cores=8))
```

### 注意事项

同步方法直接调用；标为 await 的方法在异步入口必须等待。页面/Context 关闭后多数操作会抛异常。

[更多示例和完整业务规则](../browser-context.md)

## YSContext.set_proxy

proxy 为 ProxyConfig 或 Direct；check 为可选 ProxyCheck。mode 支持 None、drain、immediate。返回本次操作后的 ProxyStatus；检查失败抛 ProxyCheckError，切换屏障错误可抛 SDKError。

```python signature
async set_proxy(proxy: 'ProxyConfig | Direct', *, check: 'ProxyCheck | None' = None, mode: 'str | None' = None, drain_timeout_ms: 'int | None' = None) -> 'ProxyStatus'
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `proxy` | ProxyConfig \| Direct | `必填` | 代理或显式直连策略；创建时 None 按 config/浏览器默认配置决定，set_proxy 不接受 None。 |
| `check` | ProxyCheck \| None | `None` | 创建/切换时的一次出口检查；None 不执行该次检查。 |
| `mode` | str \| None | `None` | set_proxy 的切换策略：None 旧行为、drain 等旧请求结束、immediate 取消旧请求；后两者需浏览器能力支持。 |
| `drain_timeout_ms` | int \| None | `None` | drain 等待上限，1–60000 毫秒，不包含出口检查时间。 |


### 返回值

返回 [ProxyStatus](ProxyStatus.md)，检查失败可能抛 ProxyCheckError；不是简单 bool。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
status = context.set_proxy(Direct(), mode="drain", drain_timeout_ms=10000)
print(status.mode, status.generation)
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
status = await context.set_proxy(Direct(), mode="drain", drain_timeout_ms=10000)
```

### 注意事项

drain/immediate 需要 proxySwitchBarrier；取消 await 不等于撤销浏览器端操作。immediate 不自动重放已取消业务请求。

[更多示例和完整业务规则](../browser-context.md)

## YSContext.start_diagnostics

开始有界事件采集，返回 None。max_events 为 1–10000；trace 开启截图/DOM trace；include_messages 控制正文；runtime_events 控制 Runtime 事件。重复开始抛 DIAGNOSTICS_ACTIVE。

```python signature
async start_diagnostics(*, include_messages: 'bool' = False, max_events: 'int' = 100, trace: 'bool' = False, runtime_events: 'bool' = True) -> 'None'
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `include_messages` | bool | `False` | 是否保存 console/异常正文；单条最多 2000 字符。 |
| `max_events` | int | `100` | 事件缓冲上限，1–10000，超出后保留最近事件。 |
| `trace` | bool | `False` | 是否开始包含截图与 DOM 快照的 trace。 |
| `runtime_events` | bool | `True` | 是否启用页面 CDP Runtime 事件采集；False 使用原生事件，可能不完整。 |


### 返回值

返回 None。操作失败时抛异常。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
context.start_diagnostics(trace=True, max_events=100, include_messages=False)
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
await context.start_diagnostics(trace=True, max_events=100, include_messages=False)
```

### 注意事项

重复开始会抛 DIAGNOSTICS_ACTIVE。需要 trace 文件时先 capture，再 stop；stop 会丢弃未保存的 SDK trace。

[更多示例和完整业务规则](../browser-context.md)

## YSContext.stop_diagnostics

停止事件收集并解除监听，返回 None。尚未 capture 的 trace 会被丢弃。

```python signature
async stop_diagnostics() -> 'None'
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

此方法没有调用参数。


### 返回值

返回 None。操作失败时抛异常。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
context.stop_diagnostics()
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
await context.stop_diagnostics()
```

### 注意事项

同步方法直接调用；标为 await 的方法在异步入口必须等待。页面/Context 关闭后多数操作会抛异常。

[更多示例和完整业务规则](../browser-context.md)

## YSContext.options

只读属性，返回创建 Context 时所用 ContextOptions 的独立副本。修改该副本不会改变运行中的 Context。同步和异步都直接读取，不加 await。
