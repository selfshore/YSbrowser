# 原生 Disposable

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [close](#close)
- [dispose](#dispose)
- [on](#on)
- [once](#once)
- [remove_listener](#remove_listener)

## close

### 同步

```python
def close(self) -> None
```

### 异步

```python
async def close(self) -> None
```


## dispose

### 同步

```python
def dispose(self) -> None
```

Disposable.dispose

Removes the associated resource. For example, removes the init script installed via `page.add_init_script()` or
`browser_context.add_init_script()`.

### 异步

```python
async def dispose(self) -> None
```

Disposable.dispose

Removes the associated resource. For example, removes the init script installed via `page.add_init_script()` or
`browser_context.add_init_script()`.


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
