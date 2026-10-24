# YSBrowser

[SDK API 目录](../api-reference.md) · [使用章节](../browser-context.md)

## 导入与准备

```python
from ysbrowser_sdk.sync_api import YSBrowser, ContextOptions

browser = YSBrowser(headless=False)
browser.start()
# 使用完后 browser.close()；完整程序建议 with。
```

## 构造参数

```python signature
YSBrowser(executable_path: 'str | Path | None' = None, *, headless: 'bool' = False, server_gpu_profile: 'str | None' = None, media_router: 'bool' = True, context_gpu: 'bool' = True, server_gpu_backend: 'str' = 'warp', default_proxy: 'ProxyConfig | Direct | None' = None, args: 'list[str] | None' = None, cdp_port: 'int | None' = None)
```

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `executable_path` | str \| Path \| None | `None` | 省略时读取安装清单，默认目录为 `./browsers`，可由 `YSBROWSER_BROWSERS_PATH` 指定。也可传已有 exe 的相对路径；不自动联网下载。 |
| `headless` | bool | `False` | `True` 无界面运行 |
| `server_gpu_profile` | str \| None | `None` | 浏览器启动级 GPU profile |
| `media_router` | bool | `True` | Media Router 启动选项 |
| `context_gpu` | bool | `True` | 是否启用 Context GPU 启动配置 |
| `server_gpu_backend` | str | `'warp'` | 只接受 warp 或 swiftshader，默认 warp；整个浏览器进程共享。不接受 None。 |
| `default_proxy` | ProxyConfig \| Direct \| None | `None` | 未单独指定代理的 Context 使用此配置；`None` 等同 `Direct()` |
| `args` | list[str] \| None | `None` | 附加浏览器参数，例如 `['--window-size=1280,900']` |


| `cdp_port` | int \| None | `None` | 0 自动分配本机 CDP 端口；1–65535 指定；None 不开放 |

## 方法与属性索引

- [YSBrowser.capabilities](#ysbrowser-capabilities)
- [YSBrowser.close](#ysbrowser-close)
- [YSBrowser.close_context](#ysbrowser-close-context)
- [YSBrowser.contexts](#ysbrowser-contexts)
- [YSBrowser.diagnostics](#ysbrowser-diagnostics)
- [YSBrowser.get_context](#ysbrowser-get-context)
- [YSBrowser.new_context](#ysbrowser-new-context)
- [YSBrowser.on_disconnected](#ysbrowser-on-disconnected)
- [YSBrowser.raw](#ysbrowser-raw)
- [YSBrowser.start](#ysbrowser-start)

## YSBrowser.capabilities

BrowserCapabilities，只读。需先启动浏览器，否则抛 BROWSER_NOT_RUNNING。

**只读属性；异步程序也直接读取，不加 await。**

```python
print(browser.capabilities)
```

## YSBrowser.close

关闭所有所属 Context、浏览器和驱动。返回 None；可重复关闭。也可通过 with / async with 自动管理。

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
browser.close()
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
await browser.close()
```

### 注意事项

浏览器方法须在所属线程/事件循环使用；普通 Chrome 缺少配套扩展能力。关闭前保存需要持久化的状态。

[更多示例和完整业务规则](../browser-context.md)

## YSBrowser.close_context

关闭 name 指定的 Context 及其页面，返回 None。找不到名称时抛 ConfigurationError。

```python signature
async close_context(name: 'str') -> 'None'
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `name` | str | `必填` | 当前浏览器中唯一的 Context 名称；创建时 None 自动命名，查询/关闭时须为已有名称。 |


### 返回值

返回 None。操作失败时抛异常。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
browser.close_context("account-001")
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
await browser.close_context("account-001")
```

### 注意事项

浏览器方法须在所属线程/事件循环使用；普通 Chrome 缺少配套扩展能力。关闭前保存需要持久化的状态。

[更多示例和完整业务规则](../browser-context.md)

## YSBrowser.contexts

tuple[YSContext, ...]，只读，当前 SDK 管理的未关闭 Context。

**只读属性；异步程序也直接读取，不加 await。**

```python
print(browser.contexts)
```

## YSBrowser.diagnostics

返回浏览器当前状态字典，含运行时版本、capabilities、browser、GPU 配置、connected、context_count 和 contexts；未启动时部分字段尚不存在。

```python signature
diagnostics() -> 'dict[str, Any]'
```

**同步计算/工厂方法；异步程序中也不加 await。**

### 参数

此方法没有调用参数。


### 返回值

返回浏览器状态 dict；[全部字段](../browser-context.md#断线回调与浏览器诊断)。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
info = browser.diagnostics()
print(info["connected"], info["context_count"])
```

### 注意事项

浏览器方法须在所属线程/事件循环使用；普通 Chrome 缺少配套扩展能力。关闭前保存需要持久化的状态。

[更多示例和完整业务规则](../browser-context.md)

## YSBrowser.get_context

name 为已有未关闭 Context 的名称。返回对应 YSContext；找不到时抛 ConfigurationError。

```python signature
get_context(name: 'str') -> 'YSContext'
```

**同步计算/工厂方法；异步程序中也不加 await。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `name` | str | `必填` | 当前浏览器中唯一的 Context 名称；创建时 None 自动命名，查询/关闭时须为已有名称。 |


### 返回值

返回名称对应的 [YSContext](YSContext.md)。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
context = browser.get_context("account-001")
```

### 注意事项

浏览器方法须在所属线程/事件循环使用；普通 Chrome 缺少配套扩展能力。关闭前保存需要持久化的状态。

[更多示例和完整业务规则](../browser-context.md)

## YSBrowser.new_context

按传入配置创建 Context，先应用指纹和代理及可选检查，再恢复登录状态。返回 YSContext；失败会清理未完成对象。显式参数优先于 config；options 整体覆盖 config.options。

```python signature
async new_context(*, name: 'str | None' = None, fingerprint: 'FingerprintProfile | None' = None, proxy: 'ProxyConfig | Direct | None' = None, check: 'ProxyCheck | None' = None, no_viewport: 'bool | None' = None, config: 'ContextConfig | None' = None, options: 'ContextOptions | None' = None, storage_state: 'dict[str, Any] | str | Path | None' = None) -> 'YSContext'
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `name` | str \| None | `None` | 当前浏览器中唯一的 Context 名称；创建时 None 自动命名，查询/关闭时须为已有名称。 |
| `fingerprint` | FingerprintProfile \| None | `None` | 页面创建前应用的指纹配置；创建时显式值优先于 config。 |
| `proxy` | ProxyConfig \| Direct \| None | `None` | 代理或显式直连策略；创建时 None 按 config/浏览器默认配置决定，set_proxy 不接受 None。 |
| `check` | ProxyCheck \| None | `None` | 创建/切换时的一次出口检查；None 不执行该次检查。 |
| `no_viewport` | bool \| None | `None` | True 不固定视口；创建时指定 options.viewport 会自动选 False，显式冲突时报错。 |
| `config` | ContextConfig \| None | `None` | 可复用配置；显式 fingerprint/proxy/options/no_viewport 覆盖相应配置。 |
| `options` | ContextOptions \| None | `None` | 原生 Context 选项；创建时整体覆盖 config.options，加载配置时非 None 字段补充/覆盖。 |
| `storage_state` | dict[str, Any] \| str \| Path \| None | `None` | 原生登录存储字典或 JSON 路径；在指纹和代理应用后恢复。 |


### 返回值

返回 [YSContext](YSContext.md)，失败不返回可用对象。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
context = browser.new_context(name="account-001", options=ContextOptions(viewport={"width": 1280, "height": 720}))
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
context = await browser.new_context(name="account-001", options=ContextOptions(viewport={"width": 1280, "height": 720}))
```

### 注意事项

浏览器方法须在所属线程/事件循环使用；普通 Chrome 缺少配套扩展能力。关闭前保存需要持久化的状态。

[更多示例和完整业务规则](../browser-context.md)

## YSBrowser.on_disconnected

callback 必须是接收一个事件字典的同步 callable。返回 None。事件字段为 unexpected、at（Unix 毫秒）、context_count。

```python signature
on_disconnected(callback: 'Any') -> 'None'
```

**同步计算/工厂方法；异步程序中也不加 await。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `callback` | Any | `必填` | 同步回调，接收 unexpected:bool、at:Unix毫秒、context_count:int；不要传 async def。 |


### 返回值

返回 None。操作失败时抛异常。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
browser.on_disconnected(lambda event: print(event["unexpected"], event["context_count"]))
```

### 注意事项

浏览器方法须在所属线程/事件循环使用；普通 Chrome 缺少配套扩展能力。关闭前保存需要持久化的状态。

[更多示例和完整业务规则](../browser-context.md)

## YSBrowser.raw

原生 Browser，只读。需已启动且连接可用。

**只读属性；异步程序也直接读取，不加 await。**

```python
print(browser.raw)
```

## YSBrowser.start

启动配套浏览器与驱动并检查能力。返回当前 YSBrowser；已连接时可重复调用。路径、运行时或浏览器不兼容时抛 SDK 异常。

```python signature
async start() -> 'YSBrowser'
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

此方法没有调用参数。


### 返回值

返回当前 YSBrowser 实例，可继续 new_context。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
browser.start()
print(browser.capabilities.protocol_version)
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
await browser.start()
```

### 注意事项

浏览器方法须在所属线程/事件循环使用；普通 Chrome 缺少配套扩展能力。关闭前保存需要持久化的状态。

[更多示例和完整业务规则](../browser-context.md)

## YSBrowser.cdp_endpoint

只读属性，返回 str 或 None。启动时 cdp_port=None（默认）则不开放 TCP 调试端口，返回 None；cdp_port=0 自动选择 loopback 端口；1–65535 指定端口。启动后返回 http://127.0.0.1:端口。未启动时抛 BROWSER_NOT_RUNNING。仅用于本机可信 CDP 集成。
