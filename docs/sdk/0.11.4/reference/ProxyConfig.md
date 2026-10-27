# ProxyConfig

[SDK API 目录](../api-reference.md) · [使用章节](../proxy.md)

## 导入与准备

```python
import os
from ysbrowser_sdk.sync_api import ProxyConfig

proxy = ProxyConfig(os.environ["PROXY_SERVER"])
```

## 构造参数

```python signature
ProxyConfig(server: 'str', username: 'str | None' = None, password: 'str | None' = None, bypass_list: 'str | None' = None) -> None
```

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `server` | str | `必填` | `http://host:port`、`https://host:port` 或 `socks5://host:port`；端口 1–65535，不能带路径、查询、fragment、空白或内嵌账号密码 |
| `username` | str \| None | `None` | 代理用户名，与密码同时提供或同时省略 |
| `password` | str \| None | `None` | 代理密码 |
| `bypass_list` | str \| None | `None` | Chromium 代理绕过规则，例如 `"localhost;127.0.0.1;*.internal.example"` |


## 字段与返回结构

直接用 `对象.字段` 读取；需要普通字典时用 `dataclasses.asdict(对象)`，或使用本类型提供的 to_dict。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `server` | str | `http://host:port`、`https://host:port` 或 `socks5://host:port`；端口 1–65535，不能带路径、查询、fragment、空白或内嵌账号密码 |
| `username` | str \| None | 代理用户名，与密码同时提供或同时省略 |
| `password` | str \| None | 代理密码 |
| `bypass_list` | str \| None | Chromium 代理绕过规则，例如 `"localhost;127.0.0.1;*.internal.example"` |

## 方法与属性索引

- [ProxyConfig.to_cdp](#proxyconfig-to-cdp)

## ProxyConfig.to_cdp

验证并转换为协议字段字典。

```python signature
to_cdp() -> 'dict[str, Any]'
```

**同步计算/工厂方法；异步程序中也不加 await。**

### 参数

此方法没有调用参数。


### 返回值

返回 proxyServer 与可选 username/password/bypassList，包含凭据。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
data = proxy.to_cdp()
# data 用于协议字段转换；包含凭据时不要写入公开日志。
```

### 注意事项

账号密码单独传入，不拼进 server URL；to_cdp() 包含真实凭据。

[更多示例和完整业务规则](../proxy.md)
