# 诊断与异常处理

[返回目录](README.md)

本节说明应用运行时如何取得状态和保存诊断文件。诊断采集默认关闭，由调用者主动开始。

## 读取 Context 状态

`context.diagnostics() -> dict`；异步入口使用 `await`。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `context_id` | `str` | 浏览器 Context ID |
| `closed` | `bool` | Context 是否已关闭 |
| `browser_connected` | `bool` | 浏览器连接是否仍存在 |
| `versions` | `dict` | `browser.diagnostics()` 的快照，包含运行时、能力及浏览器状态 |
| `recent_network_errors` | `list[dict]` | 最近最多 20 条导航级网络失败或 HTTP 错误 |
| `recent_page_events` | `list[dict]` | 已采集页面事件摘要，此接口移除 message 正文 |
| `diagnostics_collecting` | `bool` | 是否正在采集页面事件 |
| `fingerprint` | `dict`，可选 | `locked`、`configured_fields`、`server_gpu_profile` |
| `proxy` | `dict`，可选 | `ProxyStatus.to_dict()` 结构 |
| `status_error` | `dict`，可选 | 查询原生状态失败时的 SDK 异常结构 |

Context 已关闭或浏览器意外断开时，仍可返回已有摘要，但不包含新的指纹和代理查询结果。

导航错误项有 `kind`、`at`（Unix 毫秒）、`origin`；`navigation_network_error` 附 `network_error`，`navigation_http_error` 附 `http_status`。`origin` 去除 URL 的账号密码、路径、query 和 fragment。

## 开始采集

```python
context.start_diagnostics(
    include_messages=False,
    max_events=100,
    trace=True,
    runtime_events=True,
)
```

`start_diagnostics(*, include_messages=False, max_events=100, trace=False, runtime_events=True) -> None`；异步入口使用 `await`。

| 参数 | 类型 / 默认值 | 用法 |
| --- | --- | --- |
| `include_messages` | `bool = False` | 是否保存 console/页面异常的文字；开启后每条最多 2000 字符 |
| `max_events` | `int = 100` | 事件环形缓冲上限，1–10000，超过后保留最近事件 |
| `trace` | `bool = False` | 是否开始原生 trace，包含截图和 DOM 快照，不包含源码收集 |
| `runtime_events` | `bool = True` | 是否通过页面 CDP Runtime 事件收集 console 与异常 |

`runtime_events=True` 会对页面启用 Runtime 事件。设为 `False` 使用原生 Patchright 事件，其 console/pageerror 在部分运行方式下可能不完整。默认只在明确调用本方法后启用诊断。

采集期间重复开始会抛 `DIAGNOSTICS_ACTIVE`。已有页面和随后经 SDK 创建的页面会附加采集；原生弹窗在完成附加前的早期事件可能遗漏。该接口不保证覆盖所有 worker 或跨进程 frame 的 console。

## 保存诊断文件

```python
report = context.capture_diagnostics(
    "diagnostics", page=page, screenshot=True, full_page=False,
    stop_trace=True, max_pages=5, timeout_ms=5000,
)
print(report["report_path"])
context.stop_diagnostics()
```

`capture_diagnostics(directory, *, page=None, screenshot=True, full_page=False, stop_trace=True, max_pages=5, timeout_ms=5000) -> dict`；异步入口使用 `await`。

| 参数 | 类型 / 默认值 | 用法 |
| --- | --- | --- |
| `directory` | `str \| Path`，必填 | 输出父目录；每次新建独立 `ysdiagnostics-...` 子目录 |
| `page` | `Page \| None` | 只截图此页面；省略时从 Context 页面列表选择；必须属于当前 Context |
| `screenshot` | `bool = True` | 是否保存页面 PNG |
| `full_page` | `bool = False` | 是否截图完整可滚动页面 |
| `stop_trace` | `bool = True` | 是否结束已开启的 trace 并保存为 `trace.zip` |
| `max_pages` | `int = 5` | 最多处理页面数，1–100 |
| `timeout_ms` | `float = 5000` | 每次截图的正有限超时；不是整个诊断采集的总超时 |

无需提前 `start_diagnostics()` 也能取得当前状态与截图，但不会有之前的事件或 trace。要保存 trace，必须先 `start_diagnostics(trace=True)`，再 capture，最后 stop。`stop_trace=False` 继续录制，本次不生成 trace 文件。

### 返回字段

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `schema_version` | `int` | 当前为 1 |
| `created_at` | `float` | 创建时间，Unix 毫秒 |
| `directory` | `str` | 本次子目录绝对路径 |
| `report_path` | `str` | `report.json` 绝对路径 |
| `context` | `dict`，可选 | Context 诊断快照 |
| `pages` | `list[dict]` | 页面结果，每项字段见下文 |
| `pages_omitted` | `int` | 因 `max_pages` 未处理的页面数 |
| `errors` | `list[dict]` | 非截图采集失败项：`stage` 和 `error_type` |
| `trace` | `str \| None` | 相对子目录的 `trace.zip` 文件名；未保存时为 `None` |
| `trace_still_recording` | `bool` | 是否仍录制 SDK 开启的 trace |
| `messages_included` | `bool` | 是否允许在事件中包含正文 |
| `page_events` | `list[dict]` | 最近页面事件 |
| `runtime_events` | `bool` | 是否选择 Runtime 事件采集 |
| `event_attachment_errors` | `list[dict]` | 页面附加事件采集失败，字段为 `origin`、`error_type` |

`pages` 每项包含 `origin: str`、`closed: bool`、`screenshot: str | None`；失败时额外有 `screenshot_error: str`。截图文件名相对子目录，例如 `page-1.png`。

`page_events` 每项包含 `kind`（如 `console`、`page_error`、`page_crash`）、`at`（Unix 毫秒）、`origin`，console 可带 `level`；只有允许正文且存在文字时才带 `message`。

单页截图或状态查询失败时尽量返回其他结果，在相应字段记录失败；目录不可写等文件系统错误仍可能直接抛出。此方法不会重试页面业务操作，也不会停止事件收集。

`stop_diagnostics() -> None` 解除采集，异步入口使用 `await`。尚未 capture 的 SDK trace 会被丢弃。不要同时用 `context.raw.tracing` 管理同一段 SDK trace。

诊断元数据不自动导出登录状态、Cookie 文件、启动参数或完整 HTML 文件。截图、trace 内的页面/网络内容以及开启的 message 正文仍可能含业务数据；`include_messages=False` 不会对图片和 trace 做内容脱敏。

## 异常类型

```python
from ysbrowser_sdk.sync_api import (
    SDKError, ConfigurationError, CompatibilityError,
    FingerprintLockedError, ProxyCheckError,
)
from patchright.sync_api import Error as BrowserError, TimeoutError as BrowserTimeoutError

try:
    page.goto("https://app.example.com", timeout=15000)
except BrowserTimeoutError as exc:
    print("页面操作超时：", str(exc))
except BrowserError as exc:
    print("页面操作失败：", str(exc))
except SDKError as exc:
    print(exc.to_dict())
```

URL 为占位地址；将 `try` 内替换为自己的 SDK 或页面操作。异步程序从 `patchright.async_api` 导入原生异常，并对异步操作使用 `await`。

| 类型 | 基类 / 用途 |
| --- | --- |
| `SDKError` | 继承 `RuntimeError`；SDK 生命周期、协议操作等错误 |
| `ConfigurationError` | 继承 `SDKError`；参数、格式或组合不合法 |
| `CompatibilityError` | 继承 `SDKError`；运行时版本或浏览器扩展不兼容 |
| `FingerprintLockedError` | 继承 `SDKError`；Context 指纹已锁定 |
| `ProxyCheckError` | 继承 `SDKError`；代理设置时的检查失败 |

`SDKError(code, stage, message, *, context_id=None, details=None, original_error=None)` 可用于应用自己的错误包装。四个子类中，`ConfigurationError(message)` 固定 `code="INVALID_CONFIG"`、`stage="validate"`；其余三类沿用基类构造参数。

| 异常属性 | 类型 | 含义 |
| --- | --- | --- |
| `code` | `str` | 可用于程序分支的错误码 |
| `stage` | `str` | 失败阶段，如 `proxy.set` |
| `message` | `str` | SDK 错误说明 |
| `context_id` | `str \| None` | 关联 Context ID |
| `details` | `dict` | 补充信息，缺省为空字典 |
| `original_error` | 异常对象或 `None` | 原始异常对象，供调用者进一步处理 |

`to_dict() -> dict` 返回 `code`、`stage`、`message`、`context_id`、`details`，不含 `original_error`。

原生 Page/Locator 方法抛 Patchright `Error` / `TimeoutError`；鼠标模型还会抛 `ValueError`、`RuntimeError`、`NotImplementedError` 等。仅捕获 `SDKError` 不能涵盖所有页面和模型异常。

## 错误码与处理

| 错误码 | 操作方式 |
| --- | --- |
| `INVALID_CONFIG` | 根据 message 调整类型、范围、缺失字段或不兼容的选项组合 |
| `UNSUPPORTED_RUNTIME` / `UNSUPPORTED_DRIVER` | 使用当前 wheel 对应的固定 Patchright 和 driver 环境 |
| `BROWSER_CAPABILITIES_UNAVAILABLE` | 指定支持本 SDK 扩展的配套浏览器 |
| `BROWSER_CAPABILITIES_UNSUPPORTED` | 检查浏览器协议版本与缺少的 features |
| `UNSUPPORTED_FINGERPRINT_FIELDS` | 使用 capabilities 声明支持的指纹字段 |
| `CONTEXT_GPU_UNSUPPORTED` | 使用支持并确认 Context GPU profile 的浏览器 |
| `LAUNCH_FAILED` | 检查 exe 路径、配套依赖、启动参数和进程环境 |
| `BROWSER_NOT_RUNNING` | 先 start 或进入 with/async with |
| `BROWSER_DISCONNECTED` | 关闭旧实例，新建浏览器并恢复已保存状态 |
| `BROWSER_CLOSING` | 等待关闭完成后新建浏览器，不再创建 Context |
| `CONTEXT_CLOSED` | 创建新的 Context |
| `CONTEXT_ID_AMBIGUOUS` | 避免同时从 raw 或其他 CDP 客户端创建 Context |
| `FINGERPRINT_LOCKED` | 新建 Context，在打开页面前设置指纹 |
| `FINGERPRINT_STATUS_FAILED` / `FINGERPRINT_SET_FAILED` | 检查浏览器扩展支持、字段取值和连接状态 |
| `PROXY_STATUS_FAILED` | 检查浏览器连接及代理扩展接口 |
| `PROXY_SET_FAILED` | 查询当前代理状态，确认服务配置与协议错误 |
| `PROXY_CHECK_FAILED` | 读取异常 details 中的 proxy_status，检查认证、HTTP 状态、出口格式及回滚结果 |
| `PROXY_CHECK_COMMAND_FAILED` | 独立检查命令未能正常完成；检查连接和 Context 生命周期 |
| `PROXY_SWITCH_UNSUPPORTED` | 需要支持 proxySwitchBarrier 的浏览器，或在业务空闲时省略 mode |
| `PROXY_DRAIN_TIMEOUT` | 旧请求未结束；查询旧代理状态，安排结束长连接或调整等待时间 |
| `PROXY_SWITCH_IN_PROGRESS` | 已有切换正在进行；等待该操作结束后再查询状态 |
| `PROXY_SWITCH_CONTEXT_LOST` | 切换关联的 Context 已失效；新建 Context 并应用配置 |
| `PROXY_SWITCH_CANCELLED` | 切换已取消；查询当前状态后决定下一步 |
| `PROXY_SWITCH_LEASE_EXPIRED` | 切换控制已过期；检查连接并查询实际代理配置 |
| `PROXY_SWITCH_MULTIPLE_PARTITIONS_UNSUPPORTED` | 当前存在不支持的多分区条件；不要将此 Context 当作已完成切换 |
| `PROXY_SWITCH_BUSY_OR_INVALID` | 操作冲突或原生参数被拒绝；检查模式、超时和当前操作状态 |
| `CONFIG_CHANGED_EXTERNALLY` | 对可配置的 Context 重新成功应用明确设置，或新建 Context |
| `STORAGE_SAVE_FAILED` | 检查目录权限、Context 状态和原始异常 |
| `STORAGE_RESTORE_FAILED` | 检查状态文件格式、路径及原始异常 |
| `STORAGE_RESTORE_REQUIRES_EMPTY_CONTEXT` | 在创建任何页面之前恢复，优先传 new_context(storage_state=...) |
| `DIAGNOSTICS_ACTIVE` | 先 capture/stop，再启动新一轮采集 |

代理切换还可能透传浏览器返回的其他 `PROXY_*` 操作错误码；读取 `code`、`stage` 和 `details`，并重新查询状态，不假定错误后必然已应用新代理。
