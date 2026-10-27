# BrowserCapabilities

[SDK API 目录](../api-reference.md) · [使用章节](../browser-context.md)

## 导入与准备

```python
from ysbrowser_sdk.sync_api import BrowserCapabilities
```

结果对象通常由 SDK 返回。下面的构造字段也可用于理解返回对象的结构。

## 构造参数

```python signature
BrowserCapabilities(protocol_version: 'str', features: 'tuple[str, ...]', gpu_profiles: 'tuple[str, ...]', fingerprint_fields: 'tuple[str, ...]', context_gpu_available: 'bool', check_timeout_min_ms: 'int', check_timeout_max_ms: 'int', check_body_max_bytes: 'int') -> None
```

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `protocol_version` | str | `必填` | 自定义协议版本 |
| `features` | tuple[str, ...] | `必填` | 支持的功能标识 |
| `gpu_profiles` | tuple[str, ...] | `必填` | 可选择的 GPU 型号 ID |
| `fingerprint_fields` | tuple[str, ...] | `必填` | 支持的原生 camelCase 指纹字段 |
| `context_gpu_available` | bool | `必填` | 当前启动方式是否可使用 Context GPU 配置 |
| `check_timeout_min_ms` | int | `必填` | 检查超时下限，配套版本为 1000 |
| `check_timeout_max_ms` | int | `必填` | 检查超时上限，配套版本为 60000 |
| `check_body_max_bytes` | int | `必填` | 检查正文上限，配套版本为 65536 |


## 字段与返回结构

直接用 `对象.字段` 读取；需要普通字典时用 `dataclasses.asdict(对象)`，或使用本类型提供的 to_dict。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `protocol_version` | str | 自定义协议版本 |
| `features` | tuple[str, ...] | 支持的功能标识 |
| `gpu_profiles` | tuple[str, ...] | 可选择的 GPU 型号 ID |
| `fingerprint_fields` | tuple[str, ...] | 支持的原生 camelCase 指纹字段 |
| `context_gpu_available` | bool | 当前启动方式是否可使用 Context GPU 配置 |
| `check_timeout_min_ms` | int | 检查超时下限，配套版本为 1000 |
| `check_timeout_max_ms` | int | 检查超时上限，配套版本为 60000 |
| `check_body_max_bytes` | int | 检查正文上限，配套版本为 65536 |

## 方法与属性索引

- [BrowserCapabilities.from_cdp](#browsercapabilities-from-cdp)
- [BrowserCapabilities.supports](#browsercapabilities-supports)
- [BrowserCapabilities.to_dict](#browsercapabilities-to-dict)

## BrowserCapabilities.from_cdp

将原生 camelCase 响应转换为本类型。

```python signature
from_cdp(value: 'dict[str, Any]') -> 'BrowserCapabilities'
```

**同步计算/工厂方法；异步程序中也不加 await。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `value` | dict[str, Any] | `必填` | 本类型对应的原生 CDP camelCase 响应对象，不是 SDK to_dict() 的 snake_case 结果。 |


### 返回值

返回 BrowserCapabilities 实例；输入为原生 CDP 字段，输出字段见本页。此方法不发起请求。

### 示例

以下片段中的结果对象来自对应 SDK 调用；from_cdp 的字典只演示转换。

```python
from ysbrowser_sdk.sync_api import BrowserCapabilities

# 原生响应结构示例；没有执行网络检查。
raw_data = {"protocolVersion": "1.0", "features": ["proxySwitchBarrier"]}
value = BrowserCapabilities.from_cdp(raw_data)
print(value.to_dict())
```

### 注意事项

能力存在不表示业务请求已成功；supports 只按完整字符串检查 features。

[更多示例和完整业务规则](../browser-context.md)

## BrowserCapabilities.supports

feature 为完整能力名称，例如 proxySwitchBarrier。返回 bool，仅检查 features 是否包含该名称。

```python signature
supports(feature: 'str') -> 'bool'
```

**同步计算/工厂方法；异步程序中也不加 await。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `feature` | str | `必填` | 完整能力标识，例如 proxySwitchBarrier；只查询，不启用功能。 |


### 返回值

返回 bool：features 是否包含指定完整标识。

### 示例

以下片段中的结果对象来自对应 SDK 调用；from_cdp 的字典只演示转换。

```python
print(browser.capabilities.supports("proxySwitchBarrier"))
```

### 注意事项

能力存在不表示业务请求已成功；supports 只按完整字符串检查 features。

[更多示例和完整业务规则](../browser-context.md)

## BrowserCapabilities.to_dict

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
data = browser.capabilities.to_dict()
print(data)
```

### 注意事项

能力存在不表示业务请求已成功；supports 只按完整字符串检查 features。

[更多示例和完整业务规则](../browser-context.md)
