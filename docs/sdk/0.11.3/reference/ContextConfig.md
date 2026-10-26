# ContextConfig

[SDK API 目录](../api-reference.md) · [使用章节](../storage.md)

## 导入与准备

```python
from ysbrowser_sdk.sync_api import ContextConfig, FingerprintProfile

config = ContextConfig(fingerprint=FingerprintProfile(fpseed="account-001"))
```

## 构造参数

```python signature
ContextConfig(fingerprint: 'FingerprintProfile' = <factory>, proxy: 'ProxyConfig | Direct' = <factory>, no_viewport: 'bool' = True, options: 'ContextOptions' = <factory>) -> None
```

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `fingerprint` | FingerprintProfile | `独立默认对象` | 指纹配置 |
| `proxy` | ProxyConfig \| Direct | `独立默认对象` | 显式保存代理策略 |
| `no_viewport` | bool | `True` | 是否不固定视口；有 `options.viewport` 时必须为 `False` |
| `options` | ContextOptions | `独立默认对象` | Context 选项 |


## 字段与返回结构

直接用 `对象.字段` 读取；需要普通字典时用 `dataclasses.asdict(对象)`，或使用本类型提供的 to_dict。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `fingerprint` | FingerprintProfile | 指纹配置 |
| `proxy` | ProxyConfig \| Direct | 显式保存代理策略 |
| `no_viewport` | bool | 是否不固定视口；有 `options.viewport` 时必须为 `False` |
| `options` | ContextOptions | Context 选项 |

## 方法与属性索引

- [ContextConfig.from_dict](#contextconfig-from-dict)
- [ContextConfig.load](#contextconfig-load)
- [ContextConfig.save](#contextconfig-save)
- [ContextConfig.to_dict](#contextconfig-to-dict)

## ContextConfig.from_dict

从 data（schema 1/2 字典）恢复 ContextConfig。认证与 options 参数的规则同 load；不访问文件。

```python signature
from_dict(data: 'dict[str, Any]', *, proxy_username: 'str | None' = None, proxy_password: 'str | None' = None, options: 'ContextOptions | None' = None) -> 'ContextConfig'
```

**同步计算/工厂方法；异步程序中也不加 await。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `data` | dict[str, Any] | `必填` | 本类型 to_dict() 返回的结构；ContextConfig 为 schema 1/2，ContextOptions 为 values/requires。 |
| `proxy_username` | str \| None | `None` | 加载配置时补齐代理用户名，须和 proxy_password 同时提供。 |
| `proxy_password` | str \| None | `None` | 加载配置时补齐代理密码，须和 proxy_username 同时提供。 |
| `options` | ContextOptions \| None | `None` | 原生 Context 选项；创建时整体覆盖 config.options，加载配置时非 None 字段补充/覆盖。 |


### 返回值

返回 ContextConfig 实例，不访问文件。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
restored = ContextConfig.from_dict(config.to_dict())
```

### 注意事项

配置与登录状态是两种文件。默认省略凭据；加载时需要按 requires_auth/options.requires 补齐。

[更多示例和完整业务规则](../storage.md)

## ContextConfig.load

从 path 读取 JSON，返回 ContextConfig。缺少认证时用 proxy_username/password 成对补齐，options 的非 None 字段补充/覆盖已有选项。格式或缺失值错误抛 ConfigurationError。

```python signature
load(path: 'str | Path', *, proxy_username: 'str | None' = None, proxy_password: 'str | None' = None, options: 'ContextOptions | None' = None) -> 'ContextConfig'
```

**同步计算/工厂方法；异步程序中也不加 await。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `path` | str \| Path | `必填` | 读写的 JSON 路径；省略的导出/保存只返回字典；load/save 必须提供路径。 |
| `proxy_username` | str \| None | `None` | 加载配置时补齐代理用户名，须和 proxy_password 同时提供。 |
| `proxy_password` | str \| None | `None` | 加载配置时补齐代理密码，须和 proxy_username 同时提供。 |
| `options` | ContextOptions \| None | `None` | 原生 Context 选项；创建时整体覆盖 config.options，加载配置时非 None 字段补充/覆盖。 |


### 返回值

返回 ContextConfig 实例；其字段见本页构造参数。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
config = ContextConfig.load("config/account.json")
```

### 注意事项

配置与登录状态是两种文件。默认省略凭据；加载时需要按 requires_auth/options.requires 补齐。

[更多示例和完整业务规则](../storage.md)

## ContextConfig.save

将配置 JSON 保存到 path，创建父目录，返回 None。include 开关与 to_dict 相同。

```python signature
save(path: 'str | Path', *, include_proxy_credentials: 'bool' = False, include_sensitive_options: 'bool' = False) -> 'None'
```

**同步计算/工厂方法；异步程序中也不加 await。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `path` | str \| Path | `必填` | 读写的 JSON 路径；省略的导出/保存只返回字典；load/save 必须提供路径。 |
| `include_proxy_credentials` | bool | `False` | 是否在配置中写出代理账号密码；默认省略并标记需要补齐。 |
| `include_sensitive_options` | bool | `False` | 是否写出网站认证、客户端证书、附加请求头等敏感选项。 |


### 返回值

返回 None。操作失败时抛异常。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
config.save("config/account.json")
```

### 注意事项

配置与登录状态是两种文件。默认省略凭据；加载时需要按 requires_auth/options.requires 补齐。

[更多示例和完整业务规则](../storage.md)

## ContextConfig.to_dict

返回 schema 1/2 配置字典；默认省略代理认证和敏感 Context 选项。两个 include 开关均为关键字布尔值。

```python signature
to_dict(*, include_proxy_credentials: 'bool' = False, include_sensitive_options: 'bool' = False) -> 'dict[str, Any]'
```

**同步计算/工厂方法；异步程序中也不加 await。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `include_proxy_credentials` | bool | `False` | 是否在配置中写出代理账号密码；默认省略并标记需要补齐。 |
| `include_sensitive_options` | bool | `False` | 是否写出网站认证、客户端证书、附加请求头等敏感选项。 |


### 返回值

返回 schema 1/2 配置字典；[JSON 字段说明](../storage.md#json-格式)。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
data = config.to_dict()
print(data["schema_version"], data["proxy"]["mode"])
```

### 注意事项

配置与登录状态是两种文件。默认省略凭据；加载时需要按 requires_auth/options.requires 补齐。

[更多示例和完整业务规则](../storage.md)
