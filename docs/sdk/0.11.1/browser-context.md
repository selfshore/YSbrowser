# 浏览器与 Context

[返回目录](README.md)

## YSBrowser

```text
YSBrowser(
    executable_path=None, *, headless=False, server_gpu_profile=None,
    media_router=True, context_gpu=True, server_gpu_backend="warp",
    default_proxy=None, args=None, cdp_port=None,
)
```

| 参数 | 类型 / 默认值 | 用法 |
| --- | --- | --- |
| `executable_path` | `str \| Path \| None = None` | 省略时查找安装目录；也可传 `./browser/chrome.exe` 等相对路径。相对路径基于进程工作目录。 |
| `headless` | `bool = False` | `True` 无界面运行 |
| `server_gpu_profile` | `str \| None = None` | 浏览器启动级 GPU 呈现配置；Context 可进一步指定支持的型号 |
| `media_router` | `bool = True` | 保留浏览器 Media Router 功能；`False` 使用原生启动策略中的禁用行为 |
| `context_gpu` | `bool = True` | 准备支持 Context GPU 配置的软件执行后端 |
| `server_gpu_backend` | `str = "warp"` | `warp` 或 `swiftshader`；整个浏览器进程共享 |
| `default_proxy` | `ProxyConfig \| Direct \| None` | 未单独指定代理的 Context 使用此配置；`None` 等同 `Direct()` |
| `args` | `list[str] \| None` | 附加浏览器参数，例如 `['--window-size=1280,900']` |

`args` 不允许覆盖 SDK 管理的 `--disable-features`、`--enable-features`、`--proxy-`、`--user-data-dir`、`--remote-debugging`、`--server-gpu-` 前缀参数。代理使用 `ProxyConfig`，指纹使用 `FingerprintProfile`，GPU 使用相应构造参数。

默认先读取 `YSBROWSER_BROWSERS_PATH` 指定的目录；未设置时读取当前工作目录的 `./browsers/installed.json`。未安装时抛 `BROWSER_NOT_INSTALLED`；构造函数不会联网下载。安装、目录设置和示例见[安装指南](installation.md)。

### 启动和关闭

| 调用 | 返回 | 异步入口 |
| --- | --- | --- |
| `browser.start()` | 当前 `YSBrowser` | `await browser.start()` |
| `browser.close()` | `None` | `await browser.close()` |
| `with YSBrowser(...) as browser:` | 自动启动与关闭 | `async with YSBrowser(...) as browser:` |

已启动且仍连接时，重复 `start()` 返回当前对象。`close()` 关闭 SDK 所有 Context、浏览器与驱动，重复关闭可用。连接意外断开后先关闭旧实例，再新建浏览器并恢复保存的配置及登录状态。

不用上下文管理器时，应使用 `try/finally`：

```python
from ysbrowser_sdk.sync_api import YSBrowser

browser = YSBrowser()
try:
    browser.start()
    context = browser.new_context()
    page = context.new_page()
    page.set_content("<h1>Hello</h1>")
finally:
    browser.close()
```

## 创建 Context

```text
browser.new_context(
    *, name=None, fingerprint=None, proxy=None, check=None,
    no_viewport=None, config=None, options=None, storage_state=None,
) -> YSContext
```

异步入口使用 `await`。各 Context 隔离 Cookie、站点存储、指纹配置和代理配置。

| 参数 | 类型 / 默认值 | 用法 |
| --- | --- | --- |
| `name` | `str \| None` | 在当前浏览器的未关闭 Context 中唯一；省略自动使用 `context-1` 等名称 |
| `fingerprint` | `FingerprintProfile \| None` | 页面创建前应用的指纹 |
| `proxy` | `ProxyConfig \| Direct \| None` | Context 独立代理；`Direct()` 显式直连 |
| `check` | `ProxyCheck \| None` | 创建时做一次出口检查；失败不返回可用 Context |
| `no_viewport` | `bool \| None` | `True` 不固定模拟视口；通常省略 |
| `config` | `ContextConfig \| None` | 一组可保存、复用的配置 |
| `options` | `ContextOptions \| None` | 原生 Context 选项与默认超时 |
| `storage_state` | `dict \| str \| Path \| None` | 登录状态字典或 JSON 文件路径 |

优先级：显式传入的 `fingerprint`、`proxy`、`options`、`no_viewport` 优先于 `config`。未提供 `config` 时，指纹为空配置、代理使用 `browser.default_proxy`、选项为空、`no_viewport=True`。`options` 覆盖的是整组 `config.options`，不会逐字段合并。

指定 `options.viewport` 且省略 `no_viewport` 时，自动采用 `False`；同时显式传 `no_viewport=True` 会报配置错误。使用 `device_scale_factor` 也需要固定视口或 `no_viewport=False`。

创建顺序为指纹 → 代理与可选检查 → 登录状态恢复 → 返回 Context。创建失败会关闭未完成的 Context。不要同时通过 `browser.raw.new_context()` 或另一个 CDP 客户端创建 Context，以免上下文 ID 归属不明确。

## YSContext 的日常接口

Context 通过 `browser.new_context()` 取得，不需要直接调用 `YSContext(...)` 构造器。

| 接口 | 返回 / 用法 | 异步入口 |
| --- | --- | --- |
| `context.name` | `str`；SDK 名称 | 普通属性 |
| `context.context_id` | `str`；浏览器 Context ID | 普通属性 |
| `context.raw` | 原生 `BrowserContext`，可操作 Cookie、权限、路由等 | 普通属性 |
| `context.new_page()` | 原生 `Page` | `await` |
| `context.close()` | `None`；关闭全部所属页面并移出名称索引 | `await` |
| `context.set_fingerprint(profile)` | `None`；仅未锁定时可设置，见指纹章节 | `await` |
| `context.fingerprint_status()` | 原生状态字典 | `await` |
| `context.proxy_status()` | `ProxyStatus` | `await` |
| `context.set_proxy(...)` | `ProxyStatus` | `await` |
| `context.check_proxy(...)` | `ProxyHealthResult` | `await` |
| `context.export_config(...)` | 配置 `dict` | `await` |
| `context.save_storage_state(...)` | 登录状态 `dict` | `await` |
| `context.restore_storage_state(state)` | `None` | `await` |
| `context.mouse(page, ...)` | `TrajectoryMouse` | **不加 await** |
| `context.diagnostics()` | 诊断 `dict` | `await` |
| `context.start_diagnostics(...)` | `None` | `await` |
| `context.capture_diagnostics(...)` | 文件清单及结果 `dict` | `await` |
| `context.stop_diagnostics()` | `None` | `await` |

`raw` 是原生对象，直接调用其方法遵循原生 API 的规则。通过 `raw` 修改设置可能绕过 SDK 的状态记录；需要后续导出、恢复的设置优先通过 SDK 配置。

## 按名称管理

```python
# browser 是已启动的同步 YSBrowser
context = browser.new_context(name="account-001")
same_context = browser.get_context("account-001")
for item in browser.contexts:
    print(item.name, item.context_id)
browser.close_context("account-001")
```

`browser.contexts` 返回当前 SDK Context 的元组；`get_context(name)` 返回对象，找不到名称抛 `ConfigurationError`。`close_context(name)` 返回 `None`，异步入口需要 `await`。关闭后可以复用该名称。

## 能力查询：BrowserCapabilities

浏览器启动后读取 `browser.capabilities`，无需 `await`。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `protocol_version` | `str` | 自定义协议版本 |
| `features` | `tuple[str, ...]` | 支持的功能标识 |
| `gpu_profiles` | `tuple[str, ...]` | 可选择的 GPU 型号 ID |
| `fingerprint_fields` | `tuple[str, ...]` | 支持的原生 camelCase 指纹字段 |
| `context_gpu_available` | `bool` | 当前启动方式是否可使用 Context GPU 配置 |
| `check_timeout_min_ms` | `int` | 检查超时下限，配套版本为 1000 |
| `check_timeout_max_ms` | `int` | 检查超时上限，配套版本为 60000 |
| `check_body_max_bytes` | `int` | 检查正文上限，配套版本为 65536 |

`capabilities.supports(feature: str) -> bool` 按完整名称查询，例如 `proxySwitchBarrier`。`to_dict() -> dict` 导出字段。`BrowserCapabilities.from_cdp(value: dict)` 把原生字段转换为该对象，不发起网络调用；通常直接使用 `browser.capabilities`。

基础必需功能为 `contextFingerprint`、`contextProxy`、`proxyCheck`、`proxyGeneration`。Context GPU 使用 `contextGpuProfile`，有等待屏障的代理切换使用 `proxySwitchBarrier`。

## 断线回调与浏览器诊断

```python
# 同步和异步入口都不加 await；回调必须是普通 def。
def disconnected(event):
    print(event["unexpected"], event["at"], event["context_count"])

browser.on_disconnected(disconnected)
snapshot = browser.diagnostics()
```

`on_disconnected(callback) -> None` 注册接收一个字典的同步回调。`unexpected: bool` 表示是否意外断线，`at: float` 为 Unix 毫秒时间戳，`context_count: int` 为事件发生时 Context 数量。回调异常不向外传播；异步处理可由同步回调安排任务。

`browser.diagnostics() -> dict` 返回当前快照，不加 `await`。启动后的字段包括运行时版本信息、`capabilities`、原生 `browser` 版本信息、`context_gpu`、`server_gpu_backend`、`media_router`、`server_gpu_profile`、`context_count`、`connected` 和 `contexts: [{"context_id": "..."}]`。未启动时版本字段可能尚不存在。该接口不输出自定义启动参数、代理凭据、seed 或用户指定名称。

| 返回字段 | 类型 | 含义 |
| --- | --- | --- |
| `sdk_version` | `str` | SDK 版本 |
| `patchright_version` | `str` | Python Patchright 包版本 |
| `driver_version` | `str` | 内置 driver 版本 |
| `adapter_id` | `str` | SDK 运行时适配标识 |
| `validated_platform` | `str` | 当前支持平台 Windows |
| `browser_bundled` | `bool` | 是否随 SDK 附带浏览器，当前为 False |
| `capabilities` | `dict` | BrowserCapabilities 的字段结构 |
| `browser` | `dict` | 原生版本信息：protocolVersion、product、revision、userAgent、jsVersion，均为字符串 |
| `context_gpu` | `bool` | 是否启用 Context GPU 启动配置 |
| `server_gpu_backend` | `str \| None` | warp、swiftshader 或未使用该配置时的 None |
| `media_router` | `bool` | Media Router 启动选项 |
| `server_gpu_profile` | `str \| None` | 浏览器启动级 GPU profile |
| `context_count` | `int` | 当前 SDK 管理的 Context 数量 |
| `connected` | `bool` | 当前是否连接浏览器 |
| `contexts` | `list[dict]` | 每项仅含 context_id |
| `disconnect` | `dict`，可选 | 断线后出现，结构同 on_disconnected 的事件字典 |
| `disconnect_callback_error` | `str`，可选 | 断线回调抛出异常时的异常类型名 |

构造参数也保存为浏览器实例的同名配置属性，其中 `executable_path` 为解析后的路径字符串。通过构造参数配置启动行为；修改已启动实例的这些属性不会自动重启或重新配置浏览器。

## 并发

不同异步 Context 可使用 `asyncio.gather()` 运行独立业务。对同一页面的定位、滚动和鼠标动作应由调用方顺序安排。同一页面的 SDK 轨迹鼠标共享位置与执行锁，但不能协调同时发生的原生 `page.mouse` 或 `locator.click()` 操作。

## 接入 Browser Use 等本机 CDP 客户端

启动参数 `cdp_port=None` 默认保持管道连接。`cdp_port=0` 额外开放自动分配的本机端口，或传入 1–65535 指定端口。启动后 `browser.cdp_endpoint` 返回 HTTP 调试地址；关闭后不可继续使用。端口占用或启动失败会报错。

```python
from ysbrowser_sdk.sync_api import YSBrowser

with YSBrowser("./browser/chrome.exe", cdp_port=0, headless=False) as browser:
    print(browser.cdp_endpoint)
```

需要原生 Browser Use 时安装 ysbrowser-agent，使用异步 SDK 与 `await YSBrowserSession.attach(browser, context)`，不要把原始浏览器端点直接交给不管理 Context 的客户端。Context 的配置可通过 `context.options` 读取独立副本。
