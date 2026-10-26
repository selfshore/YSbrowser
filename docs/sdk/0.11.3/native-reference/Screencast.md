# 原生 Screencast

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [hide_actions](#hide_actions)
- [hide_overlays](#hide_overlays)
- [on](#on)
- [once](#once)
- [remove_listener](#remove_listener)
- [show_actions](#show_actions)
- [show_chapter](#show_chapter)
- [show_overlay](#show_overlay)
- [show_overlays](#show_overlays)
- [start](#start)
- [stop](#stop)

## hide_actions

### 同步

```python
def hide_actions(self) -> None
```

Screencast.hide_actions

Removes action decorations.

### 异步

```python
async def hide_actions(self) -> None
```

Screencast.hide_actions

Removes action decorations.


## hide_overlays

### 同步

```python
def hide_overlays(self) -> None
```

Screencast.hide_overlays

Hides overlays without removing them.

### 异步

```python
async def hide_overlays(self) -> None
```

Screencast.hide_overlays

Hides overlays without removing them.


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


## show_actions

### 同步

```python signature
def show_actions(self, *, cursor: Optional[Literal['none', 'pointer']] = None, duration: Optional[float] = None, font_size: Optional[int] = None, position: Optional[Literal['bottom', 'bottom-left', 'bottom-right', 'top', 'top-left', 'top-right']] = None, style: Optional[patchright._impl._api_structures.ScreencastActionStyle] = None) -> 'SyncContextManager'
```

Screencast.show_actions

Enables visual annotations on interacted elements. Returns a disposable that stops showing actions when disposed.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `cursor` | Union["none", "pointer", None] | Cursor decoration shown for pointer actions. `"pointer"` (the default) renders a mouse pointer that animates from the previous action point to the next one. `"none"` disables the cursor decoration. |
| `duration` | Union[float, None] | How long each annotation is displayed in milliseconds. Defaults to `500`. |
| `font_size` | Union[int, None] | Font size of the action title in pixels. Defaults to `24`. Deprecated: Use `title` in `style` instead, for example `style: { title: 'font-size: 32px' }`. |
| `position` | Union["bottom", "bottom-left", "bottom-right", "top", "top-left", "top-right", None] | Position of the action title overlay. Defaults to `"top-right"`. |
| `style` | Union[{point: Union[str, None], highlight: Union[str, None], title: Union[str, None]}, None] | Styles of the action decorations. All decorations fade out over `duration`.  **Usage** |

#### Returns
SyncContextManager

### 异步

```python signature
async def show_actions(self, *, cursor: Optional[Literal['none', 'pointer']] = None, duration: Optional[float] = None, font_size: Optional[int] = None, position: Optional[Literal['bottom', 'bottom-left', 'bottom-right', 'top', 'top-left', 'top-right']] = None, style: Optional[patchright._impl._api_structures.ScreencastActionStyle] = None) -> 'AsyncContextManager'
```

Screencast.show_actions

Enables visual annotations on interacted elements. Returns a disposable that stops showing actions when disposed.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `cursor` | Union["none", "pointer", None] | Cursor decoration shown for pointer actions. `"pointer"` (the default) renders a mouse pointer that animates from the previous action point to the next one. `"none"` disables the cursor decoration. |
| `duration` | Union[float, None] | How long each annotation is displayed in milliseconds. Defaults to `500`. |
| `font_size` | Union[int, None] | Font size of the action title in pixels. Defaults to `24`. Deprecated: Use `title` in `style` instead, for example `style: { title: 'font-size: 32px' }`. |
| `position` | Union["bottom", "bottom-left", "bottom-right", "top", "top-left", "top-right", None] | Position of the action title overlay. Defaults to `"top-right"`. |
| `style` | Union[{point: Union[str, None], highlight: Union[str, None], title: Union[str, None]}, None] | Styles of the action decorations. All decorations fade out over `duration`.  **Usage** |

#### Returns
AsyncContextManager


## show_chapter

### 同步

```python signature
def show_chapter(self, title: str, *, description: Optional[str] = None, duration: Optional[float] = None) -> None
```

Screencast.show_chapter

Shows a chapter overlay with a title and optional description, centered on the page with a blurred backdrop. Useful
for narrating video recordings. The overlay is removed after the specified duration, or 2000ms.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `title` | str | Title text displayed prominently in the overlay. |
| `description` | Union[str, None] | Optional description text displayed below the title. |
| `duration` | Union[float, None] | Duration in milliseconds after which the overlay is automatically removed. Defaults to `2000`. |

### 异步

```python signature
async def show_chapter(self, title: str, *, description: Optional[str] = None, duration: Optional[float] = None) -> None
```

Screencast.show_chapter

Shows a chapter overlay with a title and optional description, centered on the page with a blurred backdrop. Useful
for narrating video recordings. The overlay is removed after the specified duration, or 2000ms.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `title` | str | Title text displayed prominently in the overlay. |
| `description` | Union[str, None] | Optional description text displayed below the title. |
| `duration` | Union[float, None] | Duration in milliseconds after which the overlay is automatically removed. Defaults to `2000`. |

## show_overlay

### 同步

```python signature
def show_overlay(self, html: str, *, duration: Optional[float] = None) -> 'SyncContextManager'
```

Screencast.show_overlay

Adds an overlay with the given HTML content. The overlay is displayed on top of the page until removed. Returns a
disposable that removes the overlay when disposed.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `html` | str | HTML content for the overlay. |
| `duration` | Union[float, None] | Duration in milliseconds after which the overlay is automatically removed. Overlay stays until dismissed if not provided. |

#### Returns
SyncContextManager

### 异步

```python signature
async def show_overlay(self, html: str, *, duration: Optional[float] = None) -> 'AsyncContextManager'
```

Screencast.show_overlay

Adds an overlay with the given HTML content. The overlay is displayed on top of the page until removed. Returns a
disposable that removes the overlay when disposed.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `html` | str | HTML content for the overlay. |
| `duration` | Union[float, None] | Duration in milliseconds after which the overlay is automatically removed. Overlay stays until dismissed if not provided. |

#### Returns
AsyncContextManager


## show_overlays

### 同步

```python
def show_overlays(self) -> None
```

Screencast.show_overlays

Shows overlays.

### 异步

```python
async def show_overlays(self) -> None
```

Screencast.show_overlays

Shows overlays.


## start

### 同步

```python signature
def start(self, *, fps: Optional[int] = None, on_frame: Optional[Callable[[patchright._impl._api_structures.ScreencastFrame], Any]] = None, path: Union[pathlib.Path, str, NoneType] = None, quality: Optional[int] = None, size: Optional[patchright._impl._api_structures.ScreencastSize] = None) -> 'SyncContextManager'
```

Screencast.start

Starts the screencast. When `path` is provided, it saves video recording to the specified file. When `on_frame` is
provided, delivers JPEG-encoded frames to the callback. Both can be used together.

**Usage**

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `fps` | Union[int, None] | Frame rate of the video recording in frames per second. Only used together with `path`. Defaults to `25`.  Higher frame rates make animations and scrolling smoother at the cost of more CPU spent on encoding. Combine with `size` to record high resolution videos. The video can only contain as many distinct frames as the browser produces; Firefox and WebKit currently capture up to 25 frames per second. |
| `on_frame` | Union[Callable[[{data: bytes, timestamp: float, viewportWidth: int, viewportHeight: int}], Any], None] | Callback that receives JPEG-encoded frame data along with the page viewport size at the time of capture. |
| `path` | Union[pathlib.Path, str, None] | Path where the video should be saved when the screencast is stopped. When provided, video recording is started. |
| `quality` | Union[int, None] | The quality of the image, between 0-100. |
| `size` | Union[{width: int, height: int}, None] | Specifies the dimensions of screencast frames. The actual frame is scaled to preserve the page's aspect ratio and may be smaller than these bounds. If a screencast is already active (e.g. started by tracing or video recording), the existing configuration takes precedence and the frame size may exceed these bounds or this option may be ignored. If not specified the size will be equal to page viewport scaled down to fit into 800×800. |

#### Returns
SyncContextManager

### 异步

```python signature
async def start(self, *, fps: Optional[int] = None, on_frame: Optional[Callable[[patchright._impl._api_structures.ScreencastFrame], Any]] = None, path: Union[pathlib.Path, str, NoneType] = None, quality: Optional[int] = None, size: Optional[patchright._impl._api_structures.ScreencastSize] = None) -> 'AsyncContextManager'
```

Screencast.start

Starts the screencast. When `path` is provided, it saves video recording to the specified file. When `on_frame` is
provided, delivers JPEG-encoded frames to the callback. Both can be used together.

**Usage**

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `fps` | Union[int, None] | Frame rate of the video recording in frames per second. Only used together with `path`. Defaults to `25`.  Higher frame rates make animations and scrolling smoother at the cost of more CPU spent on encoding. Combine with `size` to record high resolution videos. The video can only contain as many distinct frames as the browser produces; Firefox and WebKit currently capture up to 25 frames per second. |
| `on_frame` | Union[Callable[[{data: bytes, timestamp: float, viewportWidth: int, viewportHeight: int}], Any], None] | Callback that receives JPEG-encoded frame data along with the page viewport size at the time of capture. |
| `path` | Union[pathlib.Path, str, None] | Path where the video should be saved when the screencast is stopped. When provided, video recording is started. |
| `quality` | Union[int, None] | The quality of the image, between 0-100. |
| `size` | Union[{width: int, height: int}, None] | Specifies the dimensions of screencast frames. The actual frame is scaled to preserve the page's aspect ratio and may be smaller than these bounds. If a screencast is already active (e.g. started by tracing or video recording), the existing configuration takes precedence and the frame size may exceed these bounds or this option may be ignored. If not specified the size will be equal to page viewport scaled down to fit into 800×800. |

#### Returns
AsyncContextManager


## stop

### 同步

```python
def stop(self) -> None
```

Screencast.stop

Stops the screencast and video recording if active. If a video was being recorded, saves it to the path specified
in `screencast.start()`.

### 异步

```python
async def stop(self) -> None
```

Screencast.stop

Stops the screencast and video recording if active. If a video was being recorded, saves it to the path specified
in `screencast.start()`.
