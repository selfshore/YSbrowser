# 原生 Touchscreen

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [on](#on)
- [once](#once)
- [remove_listener](#remove_listener)
- [tap](#tap)

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


## tap

### 同步

```python
def tap(self, x: float, y: float) -> None
```

Touchscreen.tap

Dispatches a `touchstart` and `touchend` event with a single touch at the position (`x`,`y`).

**NOTE** `touchscreen.tap()` will throw if the `has_touch` option of the browser context is false.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `x` | float | X coordinate relative to the main frame's viewport in CSS pixels. |
| `y` | float | Y coordinate relative to the main frame's viewport in CSS pixels. |

### 异步

```python
async def tap(self, x: float, y: float) -> None
```

Touchscreen.tap

Dispatches a `touchstart` and `touchend` event with a single touch at the position (`x`,`y`).

**NOTE** `touchscreen.tap()` will throw if the `has_touch` option of the browser context is false.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `x` | float | X coordinate relative to the main frame's viewport in CSS pixels. |
| `y` | float | Y coordinate relative to the main frame's viewport in CSS pixels. |
