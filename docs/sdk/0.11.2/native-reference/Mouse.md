# 原生 Mouse

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [click](#click)
- [dblclick](#dblclick)
- [down](#down)
- [move](#move)
- [on](#on)
- [once](#once)
- [remove_listener](#remove_listener)
- [up](#up)
- [wheel](#wheel)

## click

### 同步

```python signature
def click(self, x: float, y: float, *, button: Optional[Literal['left', 'middle', 'right']] = None, click_count: Optional[int] = None, delay: Optional[float] = None) -> None
```

Mouse.click

Shortcut for `mouse.move()`, `mouse.down()`, `mouse.up()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `x` | float | X coordinate relative to the main frame's viewport in CSS pixels. |
| `y` | float | Y coordinate relative to the main frame's viewport in CSS pixels. |
| `button` | Union["left", "middle", "right", None] | Defaults to `left`. |
| `click_count` | Union[int, None] | defaults to 1. See [UIEvent.detail]. |
| `delay` | Union[float, None] | Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0. |

### 异步

```python signature
async def click(self, x: float, y: float, *, button: Optional[Literal['left', 'middle', 'right']] = None, click_count: Optional[int] = None, delay: Optional[float] = None) -> None
```

Mouse.click

Shortcut for `mouse.move()`, `mouse.down()`, `mouse.up()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `x` | float | X coordinate relative to the main frame's viewport in CSS pixels. |
| `y` | float | Y coordinate relative to the main frame's viewport in CSS pixels. |
| `button` | Union["left", "middle", "right", None] | Defaults to `left`. |
| `click_count` | Union[int, None] | defaults to 1. See [UIEvent.detail]. |
| `delay` | Union[float, None] | Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0. |

## dblclick

### 同步

```python signature
def dblclick(self, x: float, y: float, *, button: Optional[Literal['left', 'middle', 'right']] = None, delay: Optional[float] = None) -> None
```

Mouse.dblclick

Shortcut for `mouse.move()`, `mouse.down()`, `mouse.up()`, `mouse.down()` and `mouse.up()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `x` | float | X coordinate relative to the main frame's viewport in CSS pixels. |
| `y` | float | Y coordinate relative to the main frame's viewport in CSS pixels. |
| `button` | Union["left", "middle", "right", None] | Defaults to `left`. |
| `delay` | Union[float, None] | Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0. |

### 异步

```python signature
async def dblclick(self, x: float, y: float, *, button: Optional[Literal['left', 'middle', 'right']] = None, delay: Optional[float] = None) -> None
```

Mouse.dblclick

Shortcut for `mouse.move()`, `mouse.down()`, `mouse.up()`, `mouse.down()` and `mouse.up()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `x` | float | X coordinate relative to the main frame's viewport in CSS pixels. |
| `y` | float | Y coordinate relative to the main frame's viewport in CSS pixels. |
| `button` | Union["left", "middle", "right", None] | Defaults to `left`. |
| `delay` | Union[float, None] | Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0. |

## down

### 同步

```python signature
def down(self, *, button: Optional[Literal['left', 'middle', 'right']] = None, click_count: Optional[int] = None) -> None
```

Mouse.down

Dispatches a `mousedown` event.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `button` | Union["left", "middle", "right", None] | Defaults to `left`. |
| `click_count` | Union[int, None] | defaults to 1. See [UIEvent.detail]. |

### 异步

```python signature
async def down(self, *, button: Optional[Literal['left', 'middle', 'right']] = None, click_count: Optional[int] = None) -> None
```

Mouse.down

Dispatches a `mousedown` event.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `button` | Union["left", "middle", "right", None] | Defaults to `left`. |
| `click_count` | Union[int, None] | defaults to 1. See [UIEvent.detail]. |

## move

### 同步

```python signature
def move(self, x: float, y: float, *, steps: Optional[int] = None) -> None
```

Mouse.move

Dispatches a `mousemove` event.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `x` | float | X coordinate relative to the main frame's viewport in CSS pixels. |
| `y` | float | Y coordinate relative to the main frame's viewport in CSS pixels. |
| `steps` | Union[int, None] | Defaults to 1. Sends `n` interpolated `mousemove` events to represent travel between Playwright's current cursor position and the provided destination. When set to 1, emits a single `mousemove` event at the destination location. |

### 异步

```python signature
async def move(self, x: float, y: float, *, steps: Optional[int] = None) -> None
```

Mouse.move

Dispatches a `mousemove` event.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `x` | float | X coordinate relative to the main frame's viewport in CSS pixels. |
| `y` | float | Y coordinate relative to the main frame's viewport in CSS pixels. |
| `steps` | Union[int, None] | Defaults to 1. Sends `n` interpolated `mousemove` events to represent travel between Playwright's current cursor position and the provided destination. When set to 1, emits a single `mousemove` event at the destination location. |

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


## up

### 同步

```python signature
def up(self, *, button: Optional[Literal['left', 'middle', 'right']] = None, click_count: Optional[int] = None) -> None
```

Mouse.up

Dispatches a `mouseup` event.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `button` | Union["left", "middle", "right", None] | Defaults to `left`. |
| `click_count` | Union[int, None] | defaults to 1. See [UIEvent.detail]. |

### 异步

```python signature
async def up(self, *, button: Optional[Literal['left', 'middle', 'right']] = None, click_count: Optional[int] = None) -> None
```

Mouse.up

Dispatches a `mouseup` event.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `button` | Union["left", "middle", "right", None] | Defaults to `left`. |
| `click_count` | Union[int, None] | defaults to 1. See [UIEvent.detail]. |

## wheel

### 同步

```python
def wheel(self, delta_x: float, delta_y: float) -> None
```

Mouse.wheel

Dispatches a `wheel` event. This method is usually used to manually scroll the page. See
[scrolling](https://playwright.dev/python/docs/input#scrolling) for alternative ways to scroll.

**NOTE** Wheel events may cause scrolling if they are not handled, and this method does not wait for the scrolling
to finish before returning.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `delta_x` | float | Pixels to scroll horizontally. |
| `delta_y` | float | Pixels to scroll vertically. |

### 异步

```python
async def wheel(self, delta_x: float, delta_y: float) -> None
```

Mouse.wheel

Dispatches a `wheel` event. This method is usually used to manually scroll the page. See
[scrolling](https://playwright.dev/python/docs/input#scrolling) for alternative ways to scroll.

**NOTE** Wheel events may cause scrolling if they are not handled, and this method does not wait for the scrolling
to finish before returning.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `delta_x` | float | Pixels to scroll horizontally. |
| `delta_y` | float | Pixels to scroll vertically. |
