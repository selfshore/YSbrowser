# ConfigurationError

[SDK API 目录](../api-reference.md) · [使用章节](../diagnostics-errors.md)

## 导入与准备

```python
from ysbrowser_sdk.sync_api import ConfigurationError
```

结果对象通常由 SDK 返回。下面的构造字段也可用于理解返回对象的结构。

## 构造参数

```python signature
ConfigurationError(message: 'str')
```

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `message` | str | `必填` | 可供显示的错误说明。 |


## 方法与属性索引

- [ConfigurationError.to_dict](#configurationerror-to-dict)

## ConfigurationError.to_dict

导出本对象的字典结构。

```python signature
to_dict() -> 'dict[str, Any]'
```

**同步计算/工厂方法；异步程序中也不加 await。**

### 参数

此方法没有调用参数。


### 返回值

返回 code、stage、message、context_id、details 五个字段；不包含 original_error。

### 示例

以下片段中的结果对象来自对应 SDK 调用；from_cdp 的字典只演示转换。

```python
data = error.to_dict()
print(data)
```

### 注意事项

此结果不会自动持续更新；异常对象的 to_dict 不导出原始异常文本。

[更多示例和完整业务规则](../diagnostics-errors.md)
