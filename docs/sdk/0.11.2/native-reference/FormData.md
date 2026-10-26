# 原生 FormData

[原生 API 目录](README.md) · [手册目录](../README.md)

使用 `FormData()` 创建表单字段集合，传给原生 APIRequestContext 的 multipart 参数。`append(name, value)` 追加同名字段，`set(name, value)` 替换同名字段；均返回当前 FormData 以便链式调用。name 为字段名字符串，value 可为 bool、float、str、Path 或 FilePayload。文件内容结构见 types 页面。两种入口中的 FormData 方法都为同步方法。

## 方法与属性索引

- [append](#append)
- [set](#set)

## append

### 同步

```python
def append(self, name: str, value: Union[bool, float, str, pathlib.Path, patchright._impl._api_structures.FilePayload]) -> 'FormData'
```

### 异步

```python
def append(self, name: str, value: Union[bool, float, str, pathlib.Path, patchright._impl._api_structures.FilePayload]) -> 'FormData'
```


## set

### 同步

```python
def set(self, name: str, value: Union[bool, float, str, pathlib.Path, patchright._impl._api_structures.FilePayload]) -> 'FormData'
```

### 异步

```python
def set(self, name: str, value: Union[bool, float, str, pathlib.Path, patchright._impl._api_structures.FilePayload]) -> 'FormData'
```
