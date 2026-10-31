# 原生 CDPSession

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [detach](#detach)
- [on](#on)
- [once](#once)
- [remove_listener](#remove_listener)
- [send](#send)

## detach

### 同步

```python
def detach(self) -> None
```

CDPSession.detach

Detaches the CDPSession from the target. Once detached, the CDPSession object won't emit any events and can't be
used to send messages.

### 异步

```python
async def detach(self) -> None
```

CDPSession.detach

Detaches the CDPSession from the target. Once detached, the CDPSession object won't emit any events and can't be
used to send messages.


## on

### 同步

```python
def on(self, event: str, f: Callable[..., NoneType]) -> None
```

支持的重载：

```python
def on(self, event: Literal['close'], f: Callable[[ForwardRef('CDPSession')], ForwardRef('None')]) -> None
def on(self, event: str, f: Callable[..., NoneType]) -> None
```

Registers the function ``f`` to the event name ``event``.

### 异步

```python
def on(self, event: str, f: Callable[..., Optional[Awaitable[NoneType]]]) -> None
```

支持的重载：

```python
def on(self, event: Literal['close'], f: Callable[[ForwardRef('CDPSession')], ForwardRef('Union[Awaitable[None], None]')]) -> None
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
def once(self, event: Literal['close'], f: Callable[[ForwardRef('CDPSession')], ForwardRef('None')]) -> None
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
def once(self, event: Literal['close'], f: Callable[[ForwardRef('CDPSession')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: str, f: Callable[..., Optional[Awaitable[NoneType]]]) -> None
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


## send

### 同步

```python
def send(self, method: str, params: Optional[Dict] = None) -> Dict
```

CDPSession.send

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `method` | str | Protocol method name. |
| `params` | Union[Dict, None] | Optional method parameters. |

#### Returns
Dict

### 异步

```python
async def send(self, method: str, params: Optional[Dict] = None) -> Dict
```

CDPSession.send

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `method` | str | Protocol method name. |
| `params` | Union[Dict, None] | Optional method parameters. |

#### Returns
Dict
