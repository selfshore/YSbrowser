# ProxyHealthResult

[SDK API 目录](../api-reference.md) · [使用章节](../proxy.md)

## 导入与准备

```python
from ysbrowser_sdk.sync_api import ProxyHealthResult
```

结果对象通常由 SDK 返回。下面的构造字段也可用于理解返回对象的结构。

## 构造参数

```python signature
ProxyHealthResult(ok: 'bool', kind: 'str', check_id: 'str', generation: 'str', stale: 'bool', checked_at: 'float', elapsed_ms: 'float', exit_ip: 'str | None' = None, http_status: 'int | None' = None, network_error: 'str | None' = None) -> None
```

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `ok` | bool | `必填` | 本次检查是否成功 |
| `kind` | str | `必填` | 结果分类，如 `success`、`network_error`、`timeout`、`http_error`、`invalid_ip`、`exit_ip_mismatch`；还可能有取消或被新操作替代的分类 |
| `check_id` | str | `必填` | 本次检查标识 |
| `generation` | str | `必填` | 检查关联的代理配置版本，按不透明标识比较 |
| `stale` | bool | `必填` | 返回时是否已被更新的配置/检查替代；`True` 不应用于判定当前代理 |
| `checked_at` | float | `必填` | 检查时间，Unix 毫秒 |
| `elapsed_ms` | float | `必填` | 本次检查耗时，毫秒 |
| `exit_ip` | str \| None | `None` | 解析到的出口 IP |
| `http_status` | int \| None | `None` | HTTP 状态码，没有响应时可为 `None` |
| `network_error` | str \| None | `None` | 浏览器网络错误码或说明 |


## 字段与返回结构

直接用 `对象.字段` 读取；需要普通字典时用 `dataclasses.asdict(对象)`，或使用本类型提供的 to_dict。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `ok` | bool | 本次检查是否成功 |
| `kind` | str | 结果分类，如 `success`、`network_error`、`timeout`、`http_error`、`invalid_ip`、`exit_ip_mismatch`；还可能有取消或被新操作替代的分类 |
| `check_id` | str | 本次检查标识 |
| `generation` | str | 检查关联的代理配置版本，按不透明标识比较 |
| `stale` | bool | 返回时是否已被更新的配置/检查替代；`True` 不应用于判定当前代理 |
| `checked_at` | float | 检查时间，Unix 毫秒 |
| `elapsed_ms` | float | 本次检查耗时，毫秒 |
| `exit_ip` | str \| None | 解析到的出口 IP |
| `http_status` | int \| None | HTTP 状态码，没有响应时可为 `None` |
| `network_error` | str \| None | 浏览器网络错误码或说明 |

## 方法与属性索引

- [ProxyHealthResult.from_cdp](#proxyhealthresult-from-cdp)
- [ProxyHealthResult.to_dict](#proxyhealthresult-to-dict)

## ProxyHealthResult.from_cdp

将原生 camelCase 响应转换为本类型。

```python signature
from_cdp(value: 'dict[str, Any]') -> 'ProxyHealthResult'
```

**同步计算/工厂方法；异步程序中也不加 await。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `value` | dict[str, Any] | `必填` | 本类型对应的原生 CDP camelCase 响应对象，不是 SDK to_dict() 的 snake_case 结果。 |


### 返回值

返回 ProxyHealthResult 实例；输入为原生 CDP 字段，输出字段见本页。此方法不发起请求。

### 示例

以下片段中的结果对象来自对应 SDK 调用；from_cdp 的字典只演示转换。

```python
from ysbrowser_sdk.sync_api import ProxyHealthResult

# 原生响应结构示例；没有执行网络检查。
raw_data = {"ok": False, "kind": "timeout", "generation": "example-generation"}
value = ProxyHealthResult.from_cdp(raw_data)
print(value.to_dict())
```

### 注意事项

先检查 stale，再判断 ok/kind；旧配置的晚返回结果不能代表新配置状态。

[更多示例和完整业务规则](../proxy.md)

## ProxyHealthResult.to_dict

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
data = health.to_dict()
print(data)
```

### 注意事项

先检查 stale，再判断 ok/kind；旧配置的晚返回结果不能代表新配置状态。

[更多示例和完整业务规则](../proxy.md)
