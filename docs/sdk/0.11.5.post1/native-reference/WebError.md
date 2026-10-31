# 原生 WebError

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [error](#error)
- [location](#location)
- [on](#on)
- [once](#once)
- [page](#page)
- [remove_listener](#remove_listener)

## error

属性，直接读取；异步入口也不加 await。

```python signature
WebError.error: Error
```

WebError.error

Unhandled error that was thrown.

#### Returns
Error


## location

属性，直接读取；异步入口也不加 await。

```python signature
WebError.location: <class 'patchright._impl._api_structures.WebErrorLocation'>
```

WebError.location

#### Returns
{url: str, line: int, column: int}


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
WebError.page: typing.Optional[ForwardRef('Page')]
```

WebError.page

The page that produced this unhandled exception, if any.

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
