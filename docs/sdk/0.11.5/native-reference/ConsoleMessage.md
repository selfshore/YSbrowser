# 原生 ConsoleMessage

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [args](#args)
- [location](#location)
- [on](#on)
- [once](#once)
- [page](#page)
- [remove_listener](#remove_listener)
- [text](#text)
- [timestamp](#timestamp)
- [type](#type)
- [worker](#worker)

## args

属性，直接读取；异步入口也不加 await。

```python signature
ConsoleMessage.args: typing.List[ForwardRef('JSHandle')]
```

ConsoleMessage.args

List of arguments passed to a `console` function call. See also `page.on('console')`.

#### Returns
List[JSHandle]


## location

属性，直接读取；异步入口也不加 await。

```python signature
ConsoleMessage.location: <class 'patchright._impl._api_structures.SourceLocation'>
```

ConsoleMessage.location

#### Returns
{url: str, line: int, column: int, lineNumber: int, columnNumber: int}


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
ConsoleMessage.page: typing.Optional[ForwardRef('Page')]
```

ConsoleMessage.page

The page that produced this console message, if any.

#### Returns
Union[Page, None]


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


## text

属性，直接读取；异步入口也不加 await。

```python signature
ConsoleMessage.text: <class 'str'>
```

ConsoleMessage.text

The text of the console message.

#### Returns
str


## timestamp

属性，直接读取；异步入口也不加 await。

```python signature
ConsoleMessage.timestamp: <class 'float'>
```

ConsoleMessage.timestamp

The timestamp of the console message in milliseconds since the Unix epoch.

#### Returns
float


## type

属性，直接读取；异步入口也不加 await。

```python signature
ConsoleMessage.type: typing.Literal['assert', 'clear', 'count', 'debug', 'dir', 'dirxml', 'endGroup', 'error', 'info', 'log', 'profile', 'profileEnd', 'startGroup', 'startGroupCollapsed', 'table', 'time', 'timeEnd', 'trace', 'warning']
```

ConsoleMessage.type

#### Returns
Union["assert", "clear", "count", "debug", "dir", "dirxml", "endGroup", "error", "info", "log", "profile", "profileEnd", "startGroup", "startGroupCollapsed", "table", "time", "timeEnd", "trace", "warning"]


## worker

属性，直接读取；异步入口也不加 await。

```python signature
ConsoleMessage.worker: typing.Optional[ForwardRef('Worker')]
```

ConsoleMessage.worker

The web worker or service worker that produced this console message, if any. Note that console messages from web
workers also have non-null `console_message.page`.

#### Returns
Union[Worker, None]
