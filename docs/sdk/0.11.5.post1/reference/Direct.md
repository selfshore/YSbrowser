# Direct

[SDK API 目录](../api-reference.md) · [使用章节](../proxy.md)

## 导入与准备

```python
from ysbrowser_sdk.sync_api import Direct

proxy = Direct()
```

## 构造参数

```python signature
Direct() -> None
```

此方法没有调用参数。


## 字段与返回结构

直接用 `对象.字段` 读取；需要普通字典时用 `dataclasses.asdict(对象)`，或使用本类型提供的 to_dict。

| 字段 | 类型 | 含义 |
| --- | --- | --- |

## 方法与属性索引

- [Direct.to_cdp](#direct-to-cdp)

## Direct.to_cdp

验证并转换为协议字段字典。

```python signature
to_cdp() -> 'dict[str, Any]'
```

**同步计算/工厂方法；异步程序中也不加 await。**

### 参数

此方法没有调用参数。


### 返回值

返回 {"proxyServer":"direct://"}。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
data = proxy.to_cdp()
# data 用于协议字段转换；包含凭据时不要写入公开日志。
```

### 注意事项

显式直连策略；不是使用操作系统代理。

[更多示例和完整业务规则](../proxy.md)
