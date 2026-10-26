# 原生 FileChooser

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [element](#element)
- [is_multiple](#is_multiple)
- [on](#on)
- [once](#once)
- [page](#page)
- [remove_listener](#remove_listener)
- [set_files](#set_files)

## element

属性，直接读取；异步入口也不加 await。

```python signature
FileChooser.element: ElementHandle
```

FileChooser.element

Returns input element associated with this file chooser.

#### Returns
ElementHandle


## is_multiple

### 同步

```python
def is_multiple(self) -> bool
```

FileChooser.is_multiple

Returns whether this file chooser accepts multiple files.

#### Returns
bool

### 异步

```python
def is_multiple(self) -> bool
```

FileChooser.is_multiple

Returns whether this file chooser accepts multiple files.

#### Returns
bool


## on

### 同步

```python
def on(self, event: Any, f: Any) -> None
```

Registers the function ``f`` to the event name ``event``.

### 异步

```python
def on(self, event: Any, f: Any) -> None
```

Registers the function ``f`` to the event name ``event``.


## once

### 同步

```python
def once(self, event: Any, f: Any) -> None
```

The same as ``self.on``, except that the listener is automatically
removed after being called.

### 异步

```python
def once(self, event: Any, f: Any) -> None
```

The same as ``self.on``, except that the listener is automatically
removed after being called.


## page

属性，直接读取；异步入口也不加 await。

```python signature
FileChooser.page: Page
```

FileChooser.page

Returns page this file chooser belongs to.

#### Returns
Page


## remove_listener

### 同步

```python
def remove_listener(self, event: Any, f: Any) -> None
```

Removes the function ``f`` from ``event``.

### 异步

```python
def remove_listener(self, event: Any, f: Any) -> None
```

Removes the function ``f`` from ``event``.


## set_files

### 同步

```python signature
def set_files(self, files: Union[str, pathlib.Path, Sequence[Union[str, pathlib.Path]], patchright._impl._api_structures.FilePayload, Sequence[patchright._impl._api_structures.FilePayload]], *, no_wait_after: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

FileChooser.set_files

Sets the value of the file input this chooser is associated with. If some of the `filePaths` are relative paths,
then they are resolved relative to the current working directory. For empty array, clears the selected files.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `files` | Union[Sequence[Union[pathlib.Path, str]], Sequence[{name: str, mimeType: str, buffer: bytes}], pathlib.Path, str, {name: str, mimeType: str, buffer: bytes}] |  |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

### 异步

```python signature
async def set_files(self, files: Union[str, pathlib.Path, Sequence[Union[str, pathlib.Path]], patchright._impl._api_structures.FilePayload, Sequence[patchright._impl._api_structures.FilePayload]], *, no_wait_after: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

FileChooser.set_files

Sets the value of the file input this chooser is associated with. If some of the `filePaths` are relative paths,
then they are resolved relative to the current working directory. For empty array, clears the selected files.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `files` | Union[Sequence[Union[pathlib.Path, str]], Sequence[{name: str, mimeType: str, buffer: bytes}], pathlib.Path, str, {name: str, mimeType: str, buffer: bytes}] |  |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
