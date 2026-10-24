# ContextOptions

[SDK API 目录](../api-reference.md) · [使用章节](../context-options.md)

## 导入与准备

```python
from ysbrowser_sdk.sync_api import ContextOptions

options = ContextOptions(viewport={"width": 1280, "height": 720})
```

## 构造参数

```python signature
ContextOptions(viewport: 'dict[str, int] | None' = None, accept_downloads: 'bool | None' = None, base_url: 'str | None' = None, ignore_https_errors: 'bool | None' = None, http_credentials: 'dict[str, Any] | None' = None, client_certificates: 'list[dict[str, Any]] | None' = None, extra_http_headers: 'dict[str, str] | None' = None, permissions: 'list[str] | None' = None, record_video_dir: 'str | Path | None' = None, record_video_size: 'dict[str, int] | None' = None, record_video_fps: 'int | None' = None, record_har_path: 'str | Path | None' = None, record_har_content: 'str | None' = None, record_har_mode: 'str | None' = None, record_har_omit_content: 'bool | None' = None, record_har_url_filter: 'str | None' = None, service_workers: 'str | None' = None, java_script_enabled: 'bool | None' = None, offline: 'bool | None' = None, color_scheme: 'str | None' = None, reduced_motion: 'str | None' = None, forced_colors: 'str | None' = None, contrast: 'str | None' = None, device_scale_factor: 'float | None' = None, default_timeout_ms: 'float | None' = None, navigation_timeout_ms: 'float | None' = None) -> None
```

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `viewport` | dict[str, int] \| None | `None` | `{"width": 1280, "height": 720}`，两个值均为正整数，CSS 像素 |
| `accept_downloads` | bool \| None | `None` | 是否接受下载；需要长期保留时仍须调用 `Download.save_as()` |
| `base_url` | str \| None | `None` | HTTP(S) 基础 URL，供 `page.goto("/path")` 等解析相对地址；禁止 URL 内嵌账号密码和 fragment |
| `ignore_https_errors` | bool \| None | `None` | 是否忽略 HTTPS 证书错误 |
| `http_credentials` | dict[str, Any] \| None | `None` | 网站 HTTP 认证对象，包含 username/password 和可选 origin/send；[嵌套字段与示例](../context-options.md#http-认证)。独立于代理认证。 |
| `client_certificates` | list[dict[str, Any]] \| None | `None` | HTTPS 客户端证书；非空时 Context 只支持 `Direct()` |
| `extra_http_headers` | dict[str, str] \| None | `None` | 附加请求头；键值均为字符串，不允许换行和受管理的指纹/代理头 |
| `permissions` | list[str] \| None | `None` | 预授权权限，例如 `["geolocation"]`；权限名称遵循原生 BrowserContext |
| `record_video_dir` | str \| Path \| None | `None` | 视频保存目录；关闭 Context 后完成视频写入 |
| `record_video_size` | dict[str, int] \| None | `None` | 视频宽高，正整数；需要 `record_video_dir` |
| `record_video_fps` | int \| None | `None` | 正整数帧率；需要 `record_video_dir` |
| `record_har_path` | str \| Path \| None | `None` | HAR 输出文件；关闭 Context 后完成写入 |
| `record_har_content` | str \| None | `None` | `embed`：内嵌正文；`attach`：附加文件；`omit`：不保存正文；需要 HAR 路径 |
| `record_har_mode` | str \| None | `None` | `full` 或 `minimal`；需要 HAR 路径 |
| `record_har_omit_content` | bool \| None | `None` | 是否省略 HAR 响应内容；需要 HAR 路径；避免与 `record_har_content` 设置相互矛盾的策略 |
| `record_har_url_filter` | str \| None | `None` | HAR URL glob 过滤规则，如 `"**/api/**"`；这里仅接受字符串；需要 HAR 路径 |
| `service_workers` | str \| None | `None` | `allow` 或 `block`；需要路由拦截时可按用途选择 `block` |
| `java_script_enabled` | bool \| None | `None` | 是否允许执行页面 JavaScript |
| `offline` | bool \| None | `None` | 是否以离线网络状态创建 Context |
| `color_scheme` | str \| None | `None` | `light`、`dark`、`no-preference` 或字符串 `"null"` |
| `reduced_motion` | str \| None | `None` | `reduce`、`no-preference` 或字符串 `"null"` |
| `forced_colors` | str \| None | `None` | `active`、`none` 或字符串 `"null"` |
| `contrast` | str \| None | `None` | `more`、`no-preference` 或字符串 `"null"` |
| `device_scale_factor` | float \| None | `None` | 正的有限数，设备缩放比例；不能同时使用 `no_viewport=True` |
| `default_timeout_ms` | float \| None | `None` | 普通原生操作默认超时；非负有限数，`0` 禁用超时 |
| `navigation_timeout_ms` | float \| None | `None` | 导航默认超时；非负有限数，`0` 禁用超时 |


## 字段与返回结构

直接用 `对象.字段` 读取；需要普通字典时用 `dataclasses.asdict(对象)`，或使用本类型提供的 to_dict。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `viewport` | dict[str, int] \| None | `{"width": 1280, "height": 720}`，两个值均为正整数，CSS 像素 |
| `accept_downloads` | bool \| None | 是否接受下载；需要长期保留时仍须调用 `Download.save_as()` |
| `base_url` | str \| None | HTTP(S) 基础 URL，供 `page.goto("/path")` 等解析相对地址；禁止 URL 内嵌账号密码和 fragment |
| `ignore_https_errors` | bool \| None | 是否忽略 HTTPS 证书错误 |
| `http_credentials` | dict[str, Any] \| None | 网站 HTTP 认证对象，包含 username/password 和可选 origin/send；[嵌套字段与示例](../context-options.md#http-认证)。独立于代理认证。 |
| `client_certificates` | list[dict[str, Any]] \| None | HTTPS 客户端证书；非空时 Context 只支持 `Direct()` |
| `extra_http_headers` | dict[str, str] \| None | 附加请求头；键值均为字符串，不允许换行和受管理的指纹/代理头 |
| `permissions` | list[str] \| None | 预授权权限，例如 `["geolocation"]`；权限名称遵循原生 BrowserContext |
| `record_video_dir` | str \| Path \| None | 视频保存目录；关闭 Context 后完成视频写入 |
| `record_video_size` | dict[str, int] \| None | 视频宽高，正整数；需要 `record_video_dir` |
| `record_video_fps` | int \| None | 正整数帧率；需要 `record_video_dir` |
| `record_har_path` | str \| Path \| None | HAR 输出文件；关闭 Context 后完成写入 |
| `record_har_content` | str \| None | `embed`：内嵌正文；`attach`：附加文件；`omit`：不保存正文；需要 HAR 路径 |
| `record_har_mode` | str \| None | `full` 或 `minimal`；需要 HAR 路径 |
| `record_har_omit_content` | bool \| None | 是否省略 HAR 响应内容；需要 HAR 路径；避免与 `record_har_content` 设置相互矛盾的策略 |
| `record_har_url_filter` | str \| None | HAR URL glob 过滤规则，如 `"**/api/**"`；这里仅接受字符串；需要 HAR 路径 |
| `service_workers` | str \| None | `allow` 或 `block`；需要路由拦截时可按用途选择 `block` |
| `java_script_enabled` | bool \| None | 是否允许执行页面 JavaScript |
| `offline` | bool \| None | 是否以离线网络状态创建 Context |
| `color_scheme` | str \| None | `light`、`dark`、`no-preference` 或字符串 `"null"` |
| `reduced_motion` | str \| None | `reduce`、`no-preference` 或字符串 `"null"` |
| `forced_colors` | str \| None | `active`、`none` 或字符串 `"null"` |
| `contrast` | str \| None | `more`、`no-preference` 或字符串 `"null"` |
| `device_scale_factor` | float \| None | 正的有限数，设备缩放比例；不能同时使用 `no_viewport=True` |
| `default_timeout_ms` | float \| None | 普通原生操作默认超时；非负有限数，`0` 禁用超时 |
| `navigation_timeout_ms` | float \| None | 导航默认超时；非负有限数，`0` 禁用超时 |

## 方法与属性索引

- [ContextOptions.from_dict](#contextoptions-from-dict)
- [ContextOptions.to_dict](#contextoptions-to-dict)
- [ContextOptions.to_native](#contextoptions-to-native)

## ContextOptions.from_dict

data 为 values/requires 结构；overrides 为可选 ContextOptions，其非 None 值补充或覆盖。返回 ContextOptions，缺少 requires 指定项时抛 ConfigurationError。

```python signature
from_dict(data: 'dict[str, Any]', *, overrides: 'ContextOptions | None' = None) -> 'ContextOptions'
```

**同步计算/工厂方法；异步程序中也不加 await。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `data` | dict[str, Any] | `必填` | 本类型 to_dict() 返回的结构；ContextConfig 为 schema 1/2，ContextOptions 为 values/requires。 |
| `overrides` | ContextOptions \| None | `None` | 用非 None 字段补充/覆盖序列化选项，尤其 requires 指定字段。 |


### 返回值

返回 ContextOptions；字段与校验规则见本页。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
restored = ContextOptions.from_dict(options.to_dict())
```

### 注意事项

None 表示未指定，不等于 False。客户端证书仅支持直连；不要通过附加请求头覆盖专用指纹/代理字段。

[更多示例和完整业务规则](../context-options.md)

## ContextOptions.to_dict

返回 {values: dict, requires: list[str]}。include_sensitive 默认 False，省略 http_credentials、client_certificates、extra_http_headers 的内容。

```python signature
to_dict(*, include_sensitive: 'bool' = False) -> 'dict[str, Any]'
```

**同步计算/工厂方法；异步程序中也不加 await。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `include_sensitive` | bool | `False` | 是否在 ContextOptions.values 中写出敏感选项；默认放入 requires。 |


### 返回值

返回 dict：values 为已保存选项；requires 为缺失的敏感选项名列表。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
data = options.to_dict()
print(data["values"], data["requires"])
```

### 注意事项

None 表示未指定，不等于 False。客户端证书仅支持直连；不要通过附加请求头覆盖专用指纹/代理字段。

[更多示例和完整业务规则](../context-options.md)

## ContextOptions.to_native

验证字段并返回原生创建参数字典，省略 None 和两个 SDK 默认超时字段，路径转换为 str。

```python signature
to_native() -> 'dict[str, Any]'
```

**同步计算/工厂方法；异步程序中也不加 await。**

### 参数

此方法没有调用参数。


### 返回值

返回原生 Context 参数 dict，字段名同本页，省略 None/default_timeout_ms/navigation_timeout_ms，路径转换为 str。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
values = options.to_native()
print(values.get("viewport"))
```

### 注意事项

None 表示未指定，不等于 False。客户端证书仅支持直连；不要通过附加请求头覆盖专用指纹/代理字段。

[更多示例和完整业务规则](../context-options.md)
