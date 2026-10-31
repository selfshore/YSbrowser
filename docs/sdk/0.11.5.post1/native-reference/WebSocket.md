# 原生 WebSocket

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [expect_event](#expect_event)
- [is_closed](#is_closed)
- [on](#on)
- [once](#once)
- [remove_listener](#remove_listener)
- [url](#url)
- [wait_for_event](#wait_for_event)

## expect_event

### 同步

```python signature
def expect_event(self, event: str, predicate: Optional[Callable] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> patchright._impl._sync_base.EventContextManager
```

支持的重载：

```python signature
def expect_event(self, event: Literal['close'], predicate: Optional[Callable[[ForwardRef('WebSocket')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('WebSocket')]
def expect_event(self, event: Literal['framereceived'], predicate: Optional[Callable[[ForwardRef('Union[bytes, str]')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('typing.Union[bytes, str]')]
def expect_event(self, event: Literal['framesent'], predicate: Optional[Callable[[ForwardRef('Union[bytes, str]')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('typing.Union[bytes, str]')]
def expect_event(self, event: Literal['socketerror'], predicate: Optional[Callable[[ForwardRef('str')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('str')]
def expect_event(self, event: str, predicate: Optional[Callable[..., bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[typing.Any]
```

WebSocket.expect_event

Waits for event to fire and passes its value into the predicate function. Returns when the predicate returns truthy
value. Will throw an error if the webSocket is closed before the event is fired. Returns the event data value.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `event` | str | Event name, same one would pass into `webSocket.on(event)`. |
| `predicate` | Union[Callable, None] | Receives the event data and resolves to truthy value when the waiting should resolve. |
| `timeout` | Union[float, None] | Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()`. |

#### Returns
EventContextManager

### 异步

```python signature
def expect_event(self, event: str, predicate: Optional[Callable] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> patchright._impl._async_base.AsyncEventContextManager
```

支持的重载：

```python signature
def expect_event(self, event: Literal['close'], predicate: Optional[Callable[[ForwardRef('WebSocket')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('WebSocket')]
def expect_event(self, event: Literal['framereceived'], predicate: Optional[Callable[[ForwardRef('Union[bytes, str]')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('typing.Union[bytes, str]')]
def expect_event(self, event: Literal['framesent'], predicate: Optional[Callable[[ForwardRef('Union[bytes, str]')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('typing.Union[bytes, str]')]
def expect_event(self, event: Literal['socketerror'], predicate: Optional[Callable[[ForwardRef('str')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('str')]
def expect_event(self, event: str, predicate: Optional[Callable[..., bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[typing.Any]
```

WebSocket.expect_event

Waits for event to fire and passes its value into the predicate function. Returns when the predicate returns truthy
value. Will throw an error if the webSocket is closed before the event is fired. Returns the event data value.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `event` | str | Event name, same one would pass into `webSocket.on(event)`. |
| `predicate` | Union[Callable, None] | Receives the event data and resolves to truthy value when the waiting should resolve. |
| `timeout` | Union[float, None] | Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()`. |

#### Returns
EventContextManager


## is_closed

### 同步

```python
def is_closed(self) -> bool
```

WebSocket.is_closed

Indicates that the web socket has been closed.

#### Returns
bool

### 异步

```python
def is_closed(self) -> bool
```

WebSocket.is_closed

Indicates that the web socket has been closed.

#### Returns
bool


## on

### 同步

```python
def on(self, event: str, f: Callable[..., NoneType]) -> None
```

支持的重载：

```python
def on(self, event: Literal['close'], f: Callable[[ForwardRef('WebSocket')], ForwardRef('None')]) -> None
def on(self, event: Literal['framereceived'], f: Callable[[ForwardRef('Union[bytes, str]')], ForwardRef('None')]) -> None
def on(self, event: Literal['framesent'], f: Callable[[ForwardRef('Union[bytes, str]')], ForwardRef('None')]) -> None
def on(self, event: Literal['socketerror'], f: Callable[[ForwardRef('str')], ForwardRef('None')]) -> None
```

Registers the function ``f`` to the event name ``event``.

### 异步

```python
def on(self, event: str, f: Callable[..., Optional[Awaitable[NoneType]]]) -> None
```

支持的重载：

```python
def on(self, event: Literal['close'], f: Callable[[ForwardRef('WebSocket')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['framereceived'], f: Callable[[ForwardRef('Union[bytes, str]')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['framesent'], f: Callable[[ForwardRef('Union[bytes, str]')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['socketerror'], f: Callable[[ForwardRef('str')], ForwardRef('Union[Awaitable[None], None]')]) -> None
```

Registers the function ``f`` to the event name ``event``.


## once

### 同步

```python
def once(self, event: str, f: Callable[..., NoneType]) -> None
```

支持的重载：

```python
def once(self, event: Literal['close'], f: Callable[[ForwardRef('WebSocket')], ForwardRef('None')]) -> None
def once(self, event: Literal['framereceived'], f: Callable[[ForwardRef('Union[bytes, str]')], ForwardRef('None')]) -> None
def once(self, event: Literal['framesent'], f: Callable[[ForwardRef('Union[bytes, str]')], ForwardRef('None')]) -> None
def once(self, event: Literal['socketerror'], f: Callable[[ForwardRef('str')], ForwardRef('None')]) -> None
```

The same as ``self.on``, except that the listener is automatically
removed after being called.

### 异步

```python
def once(self, event: str, f: Callable[..., Optional[Awaitable[NoneType]]]) -> None
```

支持的重载：

```python
def once(self, event: Literal['close'], f: Callable[[ForwardRef('WebSocket')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['framereceived'], f: Callable[[ForwardRef('Union[bytes, str]')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['framesent'], f: Callable[[ForwardRef('Union[bytes, str]')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['socketerror'], f: Callable[[ForwardRef('str')], ForwardRef('Union[Awaitable[None], None]')]) -> None
```

The same as ``self.on``, except that the listener is automatically
removed after being called.


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


## url

属性，直接读取；异步入口也不加 await。

```python signature
WebSocket.url: <class 'str'>
```

WebSocket.url

Contains the URL of the WebSocket.

#### Returns
str


## wait_for_event

### 同步

```python signature
def wait_for_event(self, event: str, predicate: Optional[Callable] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Any
```

支持的重载：

```python signature
def wait_for_event(self, event: Literal['close'], predicate: Optional[Callable[[ForwardRef('WebSocket')], bool]] = None, *, timeout: Optional[float] = None) -> 'WebSocket'
def wait_for_event(self, event: Literal['framereceived'], predicate: Optional[Callable[[ForwardRef('Union[bytes, str]')], bool]] = None, *, timeout: Optional[float] = None) -> 'typing.Union[bytes, str]'
def wait_for_event(self, event: Literal['framesent'], predicate: Optional[Callable[[ForwardRef('Union[bytes, str]')], bool]] = None, *, timeout: Optional[float] = None) -> 'typing.Union[bytes, str]'
def wait_for_event(self, event: Literal['socketerror'], predicate: Optional[Callable[[ForwardRef('str')], bool]] = None, *, timeout: Optional[float] = None) -> 'str'
def wait_for_event(self, event: str, predicate: Optional[Callable[..., bool]] = None, *, timeout: Optional[float] = None) -> Any
```

WebSocket.wait_for_event

**NOTE** In most cases, you should use `web_socket.expect_event()`.

Waits for given `event` to fire. If predicate is provided, it passes event's value into the `predicate` function
and waits for `predicate(event)` to return a truthy value. Will throw an error if the socket is closed before the
`event` is fired.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `event` | str | Event name, same one typically passed into `*.on(event)`. |
| `predicate` | Union[Callable, None] | Receives the event data and resolves to truthy value when the waiting should resolve. |
| `timeout` | Union[float, None] | Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()`. |

#### Returns
Any

### 异步

```python signature
async def wait_for_event(self, event: str, predicate: Optional[Callable] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Any
```

支持的重载：

```python signature
def wait_for_event(self, event: Literal['close'], predicate: Optional[Callable[[ForwardRef('WebSocket')], bool]] = None, *, timeout: Optional[float] = None) -> 'WebSocket'
def wait_for_event(self, event: Literal['framereceived'], predicate: Optional[Callable[[ForwardRef('Union[bytes, str]')], bool]] = None, *, timeout: Optional[float] = None) -> 'typing.Union[bytes, str]'
def wait_for_event(self, event: Literal['framesent'], predicate: Optional[Callable[[ForwardRef('Union[bytes, str]')], bool]] = None, *, timeout: Optional[float] = None) -> 'typing.Union[bytes, str]'
def wait_for_event(self, event: Literal['socketerror'], predicate: Optional[Callable[[ForwardRef('str')], bool]] = None, *, timeout: Optional[float] = None) -> 'str'
def wait_for_event(self, event: str, predicate: Optional[Callable[..., bool]] = None, *, timeout: Optional[float] = None) -> Any
```

WebSocket.wait_for_event

**NOTE** In most cases, you should use `web_socket.expect_event()`.

Waits for given `event` to fire. If predicate is provided, it passes event's value into the `predicate` function
and waits for `predicate(event)` to return a truthy value. Will throw an error if the socket is closed before the
`event` is fired.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `event` | str | Event name, same one typically passed into `*.on(event)`. |
| `predicate` | Union[Callable, None] | Receives the event data and resolves to truthy value when the waiting should resolve. |
| `timeout` | Union[float, None] | Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()`. |

#### Returns
Any
