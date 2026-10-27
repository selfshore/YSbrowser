# ProxyStatus

[SDK API 目录](../api-reference.md) · [使用章节](../proxy.md)

## 导入与准备

```python
from ysbrowser_sdk.sync_api import ProxyStatus
```

结果对象通常由 SDK 返回。下面的构造字段也可用于理解返回对象的结构。

## 构造参数

```python signature
ProxyStatus(mode: 'str', check_state: 'str', context_id: 'str', auth_configured: 'bool', runtime_override: 'bool', last_exit_ip: 'str | None', last_http_status: 'int | None', last_rollback: 'bool | None', proxy_server: 'str', check_url: 'str | None', generation: 'str | None' = None, health_check_in_progress: 'bool' = False, health: 'ProxyHealthResult | None' = None, last_error_kind: 'str | None' = None, last_network_error: 'str | None' = None, switch_in_progress: 'bool' = False) -> None
```

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `mode` | str | `必填` | 代理配置模式：system / direct / fixed_servers；不是切换策略 drain/immediate，也不是在线状态。 |
| `check_state` | str | `必填` | 配置/切换时的检查记录：unchecked、checking、success、failed_rolled_back、failed_no_rollback；历史 success 不代表当前在线。 |
| `context_id` | str | `必填` | 浏览器 Context ID |
| `auth_configured` | bool | `必填` | 是否配置代理认证 |
| `runtime_override` | bool | `必填` | 是否存在运行时代理覆盖 |
| `last_exit_ip` | str \| None | `必填` | 最近配置检查解析到的出口 |
| `last_http_status` | int \| None | `必填` | 最近配置检查的 HTTP 状态 |
| `last_rollback` | bool \| None | `必填` | 最近配置检查失败后是否回滚 |
| `proxy_server` | str | `必填` | 已去除凭据等信息的代理地址，直连为 `direct://` |
| `check_url` | str \| None | `必填` | 可匿名 GET 的 HTTP(S) 出口检查 URL，不含内嵌认证或 fragment |
| `generation` | str \| None | `None` | 检查关联的代理配置版本，按不透明标识比较 |
| `health_check_in_progress` | bool | `False` | 是否有独立健康检查正在执行 |
| `health` | ProxyHealthResult \| None | `None` | 最近独立健康检查结果 |
| `last_error_kind` | str \| None | `None` | 最近配置检查错误分类，如 `proxy_auth_error`、`http_error`、`network_error`、`timeout`、`invalid_ip`、`exit_ip_mismatch`、`cancelled`、`unknown` |
| `last_network_error` | str \| None | `None` | 最近配置检查提取的 `net::ERR_...` 错误码 |
| `switch_in_progress` | bool | `False` | 是否处于有屏障的代理切换过程 |


## 字段与返回结构

直接用 `对象.字段` 读取；需要普通字典时用 `dataclasses.asdict(对象)`，或使用本类型提供的 to_dict。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `mode` | str | 代理配置模式：system / direct / fixed_servers；不是切换策略 drain/immediate，也不是在线状态。 |
| `check_state` | str | 配置/切换时的检查记录：unchecked、checking、success、failed_rolled_back、failed_no_rollback；历史 success 不代表当前在线。 |
| `context_id` | str | 浏览器 Context ID |
| `auth_configured` | bool | 是否配置代理认证 |
| `runtime_override` | bool | 是否存在运行时代理覆盖 |
| `last_exit_ip` | str \| None | 最近配置检查解析到的出口 |
| `last_http_status` | int \| None | 最近配置检查的 HTTP 状态 |
| `last_rollback` | bool \| None | 最近配置检查失败后是否回滚 |
| `proxy_server` | str | 已去除凭据等信息的代理地址，直连为 `direct://` |
| `check_url` | str \| None | 可匿名 GET 的 HTTP(S) 出口检查 URL，不含内嵌认证或 fragment |
| `generation` | str \| None | 检查关联的代理配置版本，按不透明标识比较 |
| `health_check_in_progress` | bool | 是否有独立健康检查正在执行 |
| `health` | ProxyHealthResult \| None | 最近独立健康检查结果 |
| `last_error_kind` | str \| None | 最近配置检查错误分类，如 `proxy_auth_error`、`http_error`、`network_error`、`timeout`、`invalid_ip`、`exit_ip_mismatch`、`cancelled`、`unknown` |
| `last_network_error` | str \| None | 最近配置检查提取的 `net::ERR_...` 错误码 |
| `switch_in_progress` | bool | 是否处于有屏障的代理切换过程 |

## 方法与属性索引

- [ProxyStatus.from_cdp](#proxystatus-from-cdp)
- [ProxyStatus.to_dict](#proxystatus-to-dict)

## ProxyStatus.from_cdp

将原生 camelCase 响应转换为本类型。

```python signature
from_cdp(status: 'dict[str, Any]') -> 'ProxyStatus'
```

**同步计算/工厂方法；异步程序中也不加 await。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `status` | dict[str, Any] | `必填` | 原生 Browser.getProxyStatus 返回的 status 对象。 |


### 返回值

返回 ProxyStatus 实例；输入为原生 CDP 字段，输出字段见本页。此方法不发起请求。

### 示例

以下片段中的结果对象来自对应 SDK 调用；from_cdp 的字典只演示转换。

```python
from ysbrowser_sdk.sync_api import ProxyStatus

# 原生响应结构示例；没有执行网络检查。
raw_data = {"mode": "direct", "browserContextId": "example-context", "proxyServer": "direct://"}
value = ProxyStatus.from_cdp(raw_data)
print(value.to_dict())
```

### 注意事项

这是配置和最近检查的记录。check_state=success 不能证明此刻代理在线；需要当前结果时调用 check_proxy。

[更多示例和完整业务规则](../proxy.md)

## ProxyStatus.to_dict

导出本对象的字典结构。

```python signature
to_dict() -> 'dict[str, Any]'
```

**同步计算/工厂方法；异步程序中也不加 await。**

### 参数

此方法没有调用参数。


### 返回值

返回 dict，字段名与本页结果字段一致；嵌套数据类展开为字典。

### 示例

以下片段中的结果对象来自对应 SDK 调用；from_cdp 的字典只演示转换。

```python
data = status.to_dict()
print(data)
```

### 注意事项

这是配置和最近检查的记录。check_state=success 不能证明此刻代理在线；需要当前结果时调用 check_proxy。

[更多示例和完整业务规则](../proxy.md)
