# Context 选项

[返回目录](README.md)

`ContextOptions(...)` 将页面环境、网络认证、录制与超时配置传给 `browser.new_context(options=...)`。所有字段默认 `None`：不传给原生创建接口，使用原生默认值；不是一律关闭功能。

## 全部字段

| 字段 | 类型 | 取值、作用与约束 |
| --- | --- | --- |
| `viewport` | `dict[str, int] \| None` | `{"width": 1280, "height": 720}`，两个值均为正整数，CSS 像素 |
| `accept_downloads` | `bool \| None` | 是否接受下载；需要长期保留时仍须调用 `Download.save_as()` |
| `base_url` | `str \| None` | HTTP(S) 基础 URL，供 `page.goto("/path")` 等解析相对地址；禁止 URL 内嵌账号密码和 fragment |
| `ignore_https_errors` | `bool \| None` | 是否忽略 HTTPS 证书错误 |
| `http_credentials` | `dict \| None` | 网站 HTTP 认证，结构见下文；不用于代理认证 |
| `client_certificates` | `list[dict] \| None` | HTTPS 客户端证书；非空时 Context 只支持 `Direct()` |
| `extra_http_headers` | `dict[str, str] \| None` | 附加请求头；键值均为字符串，不允许换行和受管理的指纹/代理头 |
| `permissions` | `list[str] \| None` | 预授权权限，例如 `["geolocation"]`；权限名称遵循原生 BrowserContext |
| `record_video_dir` | `str \| Path \| None` | 视频保存目录；关闭 Context 后完成视频写入 |
| `record_video_size` | `dict[str, int] \| None` | 视频宽高，正整数；需要 `record_video_dir` |
| `record_video_fps` | `int \| None` | 正整数帧率；需要 `record_video_dir` |
| `record_har_path` | `str \| Path \| None` | HAR 输出文件；关闭 Context 后完成写入 |
| `record_har_content` | `str \| None` | `embed`：内嵌正文；`attach`：附加文件；`omit`：不保存正文；需要 HAR 路径 |
| `record_har_mode` | `str \| None` | `full` 或 `minimal`；需要 HAR 路径 |
| `record_har_omit_content` | `bool \| None` | 是否省略 HAR 响应内容；需要 HAR 路径；避免与 `record_har_content` 设置相互矛盾的策略 |
| `record_har_url_filter` | `str \| None` | HAR URL glob 过滤规则，如 `"**/api/**"`；这里仅接受字符串；需要 HAR 路径 |
| `service_workers` | `str \| None` | `allow` 或 `block`；需要路由拦截时可按用途选择 `block` |
| `java_script_enabled` | `bool \| None` | 是否允许执行页面 JavaScript |
| `offline` | `bool \| None` | 是否以离线网络状态创建 Context |
| `color_scheme` | `str \| None` | `light`、`dark`、`no-preference` 或字符串 `"null"` |
| `reduced_motion` | `str \| None` | `reduce`、`no-preference` 或字符串 `"null"` |
| `forced_colors` | `str \| None` | `active`、`none` 或字符串 `"null"` |
| `contrast` | `str \| None` | `more`、`no-preference` 或字符串 `"null"` |
| `device_scale_factor` | `float \| None` | 正的有限数，设备缩放比例；不能同时使用 `no_viewport=True` |
| `default_timeout_ms` | `float \| None` | 普通原生操作默认超时；非负有限数，`0` 禁用超时 |
| `navigation_timeout_ms` | `float \| None` | 导航默认超时；非负有限数，`0` 禁用超时 |

媒体选项中，Python `None` 表示不设置；字符串 `"null"` 表示原生 API 的重置值。单次操作显式传入的 `timeout=` 优先于默认超时；这些设置不替代 `ProxyCheck.timeout_ms` 或鼠标 `duration_s`。

## 视口、权限和超时

```python
from ysbrowser_sdk.sync_api import ContextOptions, FingerprintProfile

options = ContextOptions(
    viewport={"width": 1440, "height": 900},
    device_scale_factor=1.0,
    permissions=["geolocation"],
    color_scheme="light",
    default_timeout_ms=15000,
    navigation_timeout_ms=45000,
)
# browser 为已启动的 YSBrowser。
context = browser.new_context(
    options=options,
    fingerprint=FingerprintProfile(geolocation="31.2304,121.4737,50"),
)
```

指定固定视口不会等同设置屏幕指纹。`ContextConfig` 内包含视口时，还应显式设置 `no_viewport=False`。

## HTTP 认证

```python
import os
from ysbrowser_sdk.sync_api import ContextOptions

options = ContextOptions(http_credentials={
    "username": os.environ["SITE_USERNAME"],
    "password": os.environ["SITE_PASSWORD"],
    "origin": "https://app.example.com",
    "send": "unauthorized",
})
```

| 子字段 | 必填 | 用法 |
| --- | --- | --- |
| `username` | 是 | 网站认证用户名，字符串 |
| `password` | 是 | 网站认证密码，字符串 |
| `origin` | 否 | 限定认证来源，HTTP(S) scheme + host + 可选端口，不含业务路径或 query |
| `send` | 否 | `unauthorized` 或 `always`；影响原生 APIRequestContext 的认证发送策略，不改变浏览器页面请求的认证策略 |

代理用户名和密码应放在 `ProxyConfig` 中。

## 客户端证书

```python
from ysbrowser_sdk.sync_api import ContextOptions, Direct

options = ContextOptions(client_certificates=[{
    "origin": "https://secure.example.com",
    "certPath": r"./certs/client.pem",
    "keyPath": r"./certs/client-key.pem",
}])
context = browser.new_context(proxy=Direct(), options=options)
```

也可用 PFX/P12：

```python
import os
from ysbrowser_sdk.sync_api import ContextOptions

options = ContextOptions(client_certificates=[{
    "origin": "https://secure.example.com",
    "pfxPath": r"./certs/client.p12",
    "passphrase": os.environ["CERT_PASSPHRASE"],
}])
```

`origin` 必填，精确到 scheme、host、可选端口。二选一：`certPath` 与 `keyPath` 成对传入，或 `pfxPath`；`passphrase` 为可选字符串。字段名使用上述 camelCase。此封装仅支持文件路径，不接受内联证书字节。

配置非空客户端证书列表的 Context 只能使用直连；创建时传代理、继承非直连默认代理、或之后 `set_proxy(ProxyConfig(...))` 均会被拒绝。

## 附加请求头

```python
from ysbrowser_sdk.sync_api import ContextOptions
options = ContextOptions(extra_http_headers={"X-Client-Name": "my-app"})
```

禁止通过此字段设置 `User-Agent`、`Accept-Language`、`Proxy-Authorization`、`Proxy-Connection` 和 `sec-ch-ua` 开头的请求头，匹配不区分大小写。指纹相关值通过 `FingerprintProfile` 设置。

## 视频与 HAR

```python
from ysbrowser_sdk.sync_api import ContextOptions

options = ContextOptions(
    record_video_dir="recordings/video",
    record_video_size={"width": 1280, "height": 720},
    record_video_fps=30,
    record_har_path="recordings/network.har",
    record_har_mode="full",
    record_har_content="embed",
)
context = browser.new_context(options=options)
page = context.new_page()
page.set_content("<h1>Recording</h1>")
video = page.video
context.close()  # 先完成视频和 HAR 写入
if video is not None:
    print(video.path())
```

## 序列化方法

| 方法 | 返回 | 说明 |
| --- | --- | --- |
| `options.to_native()` | `dict` | 验证并生成原生 Context 参数；省略 `None` 与两个 SDK 默认超时字段，路径转换为字符串 |
| `options.to_dict(include_sensitive=False)` | `dict` | 返回 `{"values": {...}, "requires": [...]}`；默认省略网站认证、证书、附加请求头，记录需要补齐的字段名 |
| `ContextOptions.from_dict(data, overrides=None)` | `ContextOptions` | `data` 为上述结构；用 `overrides` 中非 `None` 字段补充或覆盖值 |

三个方法在异步入口也直接调用，不使用 `await`。`include_sensitive=True` 会把 `http_credentials`、`client_certificates`、`extra_http_headers` 也写入结果。缺少 `requires` 声明的必需字段时，加载抛 `ConfigurationError`。
