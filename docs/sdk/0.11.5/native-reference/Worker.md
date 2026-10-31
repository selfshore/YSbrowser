# 原生 Worker

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [evaluate](#evaluate)
- [evaluate_handle](#evaluate_handle)
- [expect_event](#expect_event)
- [on](#on)
- [once](#once)
- [remove_listener](#remove_listener)
- [url](#url)

## evaluate

### 同步

```python signature
def evaluate(self, expression: str, arg: Optional[Any] = None, *, isolated_context: Optional[bool] = True) -> Any
```

Worker.evaluate

Returns the return value of `expression`.

If the function passed to the `worker.evaluate()` returns a [Promise], then `worker.evaluate()` would wait for the
promise to resolve and return its value.

If the function passed to the `worker.evaluate()` returns a non-[Serializable] value, then `worker.evaluate()`
returns `undefined`. Playwright also supports transferring some additional values that are not serializable by
`JSON`: `-0`, `NaN`, `Infinity`, `-Infinity`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expression` | str | JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked. |
| `arg` | Union[Any, None] | Optional argument to pass to `expression`. |

#### Returns
Any

### 异步

```python signature
async def evaluate(self, expression: str, arg: Optional[Any] = None, *, isolated_context: Optional[bool] = True) -> Any
```

Worker.evaluate

Returns the return value of `expression`.

If the function passed to the `worker.evaluate()` returns a [Promise], then `worker.evaluate()` would wait for the
promise to resolve and return its value.

If the function passed to the `worker.evaluate()` returns a non-[Serializable] value, then `worker.evaluate()`
returns `undefined`. Playwright also supports transferring some additional values that are not serializable by
`JSON`: `-0`, `NaN`, `Infinity`, `-Infinity`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expression` | str | JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked. |
| `arg` | Union[Any, None] | Optional argument to pass to `expression`. |

#### Returns
Any


## evaluate_handle

### 同步

```python signature
def evaluate_handle(self, expression: str, arg: Optional[Any] = None, *, isolated_context: Optional[bool] = True) -> 'JSHandle'
```

Worker.evaluate_handle

Returns the return value of `expression` as a `JSHandle`.

The only difference between `worker.evaluate()` and `worker.evaluate_handle()` is that `worker.evaluate_handle()`
returns `JSHandle`.

If the function passed to the `worker.evaluate_handle()` returns a [Promise], then `worker.evaluate_handle()` would
wait for the promise to resolve and return its value.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expression` | str | JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked. |
| `arg` | Union[Any, None] | Optional argument to pass to `expression`. |

#### Returns
JSHandle

### 异步

```python signature
async def evaluate_handle(self, expression: str, arg: Optional[Any] = None, *, isolated_context: Optional[bool] = True) -> 'JSHandle'
```

Worker.evaluate_handle

Returns the return value of `expression` as a `JSHandle`.

The only difference between `worker.evaluate()` and `worker.evaluate_handle()` is that `worker.evaluate_handle()`
returns `JSHandle`.

If the function passed to the `worker.evaluate_handle()` returns a [Promise], then `worker.evaluate_handle()` would
wait for the promise to resolve and return its value.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expression` | str | JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked. |
| `arg` | Union[Any, None] | Optional argument to pass to `expression`. |

#### Returns
JSHandle


## expect_event

### 同步

```python signature
def expect_event(self, event: str, predicate: Optional[Callable] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> patchright._impl._sync_base.EventContextManager
```

支持的重载：

```python signature
def expect_event(self, event: Literal['close'], predicate: Optional[Callable[[ForwardRef('Worker')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Worker')]
def expect_event(self, event: Literal['console'], predicate: Optional[Callable[[ForwardRef('ConsoleMessage')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('ConsoleMessage')]
def expect_event(self, event: str, predicate: Optional[Callable[..., bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[typing.Any]
```

Worker.expect_event

Waits for event to fire and passes its value into the predicate function. Returns when the predicate returns truthy
value. Will throw an error if the page is closed before the event is fired. Returns the event data value.

**Usage**

```py
with worker.expect_event("console") as event_info:
    worker.evaluate("console.log(42)")
message = event_info.value
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `event` | str | Event name, same one typically passed into `*.on(event)`. |
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
def expect_event(self, event: Literal['close'], predicate: Optional[Callable[[ForwardRef('Worker')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Worker')]
def expect_event(self, event: Literal['console'], predicate: Optional[Callable[[ForwardRef('ConsoleMessage')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('ConsoleMessage')]
def expect_event(self, event: str, predicate: Optional[Callable[..., bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[typing.Any]
```

Worker.expect_event

Waits for event to fire and passes its value into the predicate function. Returns when the predicate returns truthy
value. Will throw an error if the page is closed before the event is fired. Returns the event data value.

**Usage**

```py
async with worker.expect_event("console") as event_info:
    await worker.evaluate("console.log(42)")
message = await event_info.value
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `event` | str | Event name, same one typically passed into `*.on(event)`. |
| `predicate` | Union[Callable, None] | Receives the event data and resolves to truthy value when the waiting should resolve. |
| `timeout` | Union[float, None] | Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()`. |

#### Returns
EventContextManager


## on

### 同步

```python
def on(self, event: str, f: Callable[..., NoneType]) -> None
```

支持的重载：

```python
def on(self, event: Literal['close'], f: Callable[[ForwardRef('Worker')], ForwardRef('None')]) -> None
def on(self, event: Literal['console'], f: Callable[[ForwardRef('ConsoleMessage')], ForwardRef('None')]) -> None
```

Registers the function ``f`` to the event name ``event``.

### 异步

```python
def on(self, event: str, f: Callable[..., Optional[Awaitable[NoneType]]]) -> None
```

支持的重载：

```python
def on(self, event: Literal['close'], f: Callable[[ForwardRef('Worker')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['console'], f: Callable[[ForwardRef('ConsoleMessage')], ForwardRef('Union[Awaitable[None], None]')]) -> None
```

Registers the function ``f`` to the event name ``event``.


## once

### 同步

```python
def once(self, event: str, f: Callable[..., NoneType]) -> None
```

支持的重载：

```python
def once(self, event: Literal['close'], f: Callable[[ForwardRef('Worker')], ForwardRef('None')]) -> None
def once(self, event: Literal['console'], f: Callable[[ForwardRef('ConsoleMessage')], ForwardRef('None')]) -> None
```

The same as ``self.on``, except that the listener is automatically
removed after being called.

### 异步

```python
def once(self, event: str, f: Callable[..., Optional[Awaitable[NoneType]]]) -> None
```

支持的重载：

```python
def once(self, event: Literal['close'], f: Callable[[ForwardRef('Worker')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['console'], f: Callable[[ForwardRef('ConsoleMessage')], ForwardRef('Union[Awaitable[None], None]')]) -> None
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
Worker.url: <class 'str'>
```

Worker.url

#### Returns
str
