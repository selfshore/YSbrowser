# 原生 APIResponseAssertions

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [not_to_be_ok](#not_to_be_ok)
- [on](#on)
- [once](#once)
- [remove_listener](#remove_listener)
- [to_be_ok](#to_be_ok)

## not_to_be_ok

### 同步

```python
def not_to_be_ok(self) -> None
```

APIResponseAssertions.not_to_be_ok

The opposite of `api_response_assertions.to_be_ok()`.

### 异步

```python
async def not_to_be_ok(self) -> None
```

APIResponseAssertions.not_to_be_ok

The opposite of `api_response_assertions.to_be_ok()`.


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


## to_be_ok

### 同步

```python
def to_be_ok(self) -> None
```

APIResponseAssertions.to_be_ok

Ensures the response status code is within `200..299` range.

**Usage**

```py
import re
from playwright.sync_api import expect

# ...
expect(response).to_be_ok()
```

### 异步

```python
async def to_be_ok(self) -> None
```

APIResponseAssertions.to_be_ok

Ensures the response status code is within `200..299` range.

**Usage**

```py
from playwright.async_api import expect

# ...
await expect(response).to_be_ok()
```
