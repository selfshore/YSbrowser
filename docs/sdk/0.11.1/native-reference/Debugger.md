# 原生 Debugger

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [next](#next)
- [on](#on)
- [once](#once)
- [paused_details](#paused_details)
- [remove_listener](#remove_listener)
- [request_pause](#request_pause)
- [resume](#resume)
- [run_to](#run_to)

## next

### 同步

```python
def next(self) -> None
```

Debugger.next

Resumes script execution and pauses again before the next action. Throws if the debugger is not paused.

### 异步

```python
async def next(self) -> None
```

Debugger.next

Resumes script execution and pauses again before the next action. Throws if the debugger is not paused.


## on

### 同步

```python
def on(self, event: str, f: Callable[..., NoneType]) -> None
```

支持的重载：

```python
def on(self, event: Literal['pausedstatechanged'], f: Callable[[ForwardRef('None')], ForwardRef('None')]) -> None
def on(self, event: str, f: Callable[..., NoneType]) -> None
```

Registers the function ``f`` to the event name ``event``.

### 异步

```python
def on(self, event: str, f: Callable[..., Optional[Awaitable[NoneType]]]) -> None
```

支持的重载：

```python
def on(self, event: Literal['pausedstatechanged'], f: Callable[[ForwardRef('None')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: str, f: Callable[..., Optional[Awaitable[NoneType]]]) -> None
```

Registers the function ``f`` to the event name ``event``.


## once

### 同步

```python
def once(self, event: str, f: Callable[..., NoneType]) -> None
```

支持的重载：

```python
def once(self, event: Literal['pausedstatechanged'], f: Callable[[ForwardRef('None')], ForwardRef('None')]) -> None
def once(self, event: str, f: Callable[..., NoneType]) -> None
```

The same as ``self.on``, except that the listener is automatically
removed after being called.

### 异步

```python
def once(self, event: str, f: Callable[..., Optional[Awaitable[NoneType]]]) -> None
```

支持的重载：

```python
def once(self, event: Literal['pausedstatechanged'], f: Callable[[ForwardRef('None')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: str, f: Callable[..., Optional[Awaitable[NoneType]]]) -> None
```

The same as ``self.on``, except that the listener is automatically
removed after being called.


## paused_details

属性，直接读取；异步入口也不加 await。

```python signature
Debugger.paused_details: typing.Optional[patchright._impl._api_structures.DebuggerPausedDetails]
```

Debugger.paused_details

Returns details about the currently paused call. Returns `null` if the debugger is not paused.

#### Returns
Union[{location: {file: str, line: Union[int, None], column: Union[int, None]}, title: str}, None]


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


## request_pause

### 同步

```python
def request_pause(self) -> None
```

Debugger.request_pause

Configures the debugger to pause before the next action is executed.

Throws if the debugger is already paused. Use `debugger.next()` or `debugger.run_to()` to step while paused.

Note that `page.pause()` is equivalent to a "debugger" statement — it pauses execution at the call site
immediately. On the contrary, `debugger.request_pause()` is equivalent to "pause on next statement" — it configures
the debugger to pause before the next action is executed.

### 异步

```python
async def request_pause(self) -> None
```

Debugger.request_pause

Configures the debugger to pause before the next action is executed.

Throws if the debugger is already paused. Use `debugger.next()` or `debugger.run_to()` to step while paused.

Note that `page.pause()` is equivalent to a "debugger" statement — it pauses execution at the call site
immediately. On the contrary, `debugger.request_pause()` is equivalent to "pause on next statement" — it configures
the debugger to pause before the next action is executed.


## resume

### 同步

```python
def resume(self) -> None
```

Debugger.resume

Resumes script execution. Throws if the debugger is not paused.

### 异步

```python
async def resume(self) -> None
```

Debugger.resume

Resumes script execution. Throws if the debugger is not paused.


## run_to

### 同步

```python
def run_to(self, location: patchright._impl._api_structures.DebuggerLocation) -> None
```

Debugger.run_to

Resumes script execution and pauses when an action originates from the given source location. Throws if the
debugger is not paused.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `location` | {file: str, line: Union[int, None], column: Union[int, None]} | The source location to pause at. |

### 异步

```python
async def run_to(self, location: patchright._impl._api_structures.DebuggerLocation) -> None
```

Debugger.run_to

Resumes script execution and pauses when an action originates from the given source location. Throws if the
debugger is not paused.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `location` | {file: str, line: Union[int, None], column: Union[int, None]} | The source location to pause at. |
