# CompatibilityError

[SDK API 目录](../api-reference.md) · [使用章节](../diagnostics-errors.md)

## 导入与准备

```python
from ysbrowser_sdk.sync_api import CompatibilityError
```

结果对象通常由 SDK 返回。下面的构造字段也可用于理解返回对象的结构。

## 构造参数

```python signature
CompatibilityError(code: 'str', stage: 'str', message: 'str', *, context_id: 'str | None' = None, details: 'dict[str, Any] | None' = None, original_error: 'Exception | None' = None)
```

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `code` | str | `必填` | SDK 机器可读错误代码，例如 INVALID_CONFIG。 |
| `stage` | str | `必填` | 发生错误的操作阶段标识。 |
| `message` | str | `必填` | 可供显示的错误说明。 |
| `context_id` | str \| None | `None` | 相关浏览器 Context ID；无相关 Context 时为 None。 |
| `details` | dict[str, Any] \| None | `None` | 结构化补充信息；省略时保存为空字典。 |
| `original_error` | Exception \| None | `None` | 原始异常对象，供程序调试，不包含在 to_dict() 中。 |


## 方法与属性索引

- [CompatibilityError.to_dict](#compatibilityerror-to-dict)

## CompatibilityError.to_dict

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
