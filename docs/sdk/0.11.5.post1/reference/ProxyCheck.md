# ProxyCheck

[SDK API 目录](../api-reference.md) · [使用章节](../proxy.md)

## 导入与准备

```python
import os
from ysbrowser_sdk.sync_api import ProxyCheck

check = ProxyCheck(check_url=os.environ["IP_CHECK_URL"])
```

## 构造参数

```python signature
ProxyCheck(check_url: 'str', expected_exit_ip: 'str | None' = None, timeout_ms: 'int' = 10000, rollback_on_failure: 'bool' = True) -> None
```

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `check_url` | str | `必填` | 可匿名 GET 的 HTTP(S) 出口检查 URL，不含内嵌认证或 fragment |
| `expected_exit_ip` | str \| None | `None` | 预期的合法 IPv4/IPv6；省略则只验证返回有效 IP，不固定出口 |
| `timeout_ms` | int | `10000` | 整数，1000–60000 毫秒 |
| `rollback_on_failure` | bool | `True` | 切换检查失败后是否恢复旧代理配置 |


## 字段与返回结构

直接用 `对象.字段` 读取；需要普通字典时用 `dataclasses.asdict(对象)`，或使用本类型提供的 to_dict。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `check_url` | str | 可匿名 GET 的 HTTP(S) 出口检查 URL，不含内嵌认证或 fragment |
| `expected_exit_ip` | str \| None | 预期的合法 IPv4/IPv6；省略则只验证返回有效 IP，不固定出口 |
| `timeout_ms` | int | 整数，1000–60000 毫秒 |
| `rollback_on_failure` | bool | 切换检查失败后是否恢复旧代理配置 |

## 方法与属性索引

- [ProxyCheck.to_cdp](#proxycheck-to-cdp)

## ProxyCheck.to_cdp

验证并转换为协议字段字典。

```python signature
to_cdp() -> 'dict[str, Any]'
```

**同步计算/工厂方法；异步程序中也不加 await。**

### 参数

此方法没有调用参数。


### 返回值

返回 checkUrl、checkTimeoutMs、rollbackOnFailure 与可选 expectedExitIp。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
data = check.to_cdp()
# data 用于协议字段转换；包含凭据时不要写入公开日志。
```

### 注意事项

检查服务须返回支持格式的出口 IP；它不是自动持续监测。

[更多示例和完整业务规则](../proxy.md)
