# 原生 ElementHandle

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [as_element](#as_element)
- [bounding_box](#bounding_box)
- [check](#check)
- [click](#click)
- [content_frame](#content_frame)
- [dblclick](#dblclick)
- [dispatch_event](#dispatch_event)
- [dispose](#dispose)
- [eval_on_selector](#eval_on_selector)
- [eval_on_selector_all](#eval_on_selector_all)
- [evaluate](#evaluate)
- [evaluate_handle](#evaluate_handle)
- [fill](#fill)
- [focus](#focus)
- [get_attribute](#get_attribute)
- [get_properties](#get_properties)
- [get_property](#get_property)
- [hover](#hover)
- [inner_html](#inner_html)
- [inner_text](#inner_text)
- [input_value](#input_value)
- [is_checked](#is_checked)
- [is_disabled](#is_disabled)
- [is_editable](#is_editable)
- [is_enabled](#is_enabled)
- [is_hidden](#is_hidden)
- [is_visible](#is_visible)
- [json_value](#json_value)
- [on](#on)
- [once](#once)
- [owner_frame](#owner_frame)
- [press](#press)
- [query_selector](#query_selector)
- [query_selector_all](#query_selector_all)
- [remove_listener](#remove_listener)
- [screenshot](#screenshot)
- [scroll_into_view_if_needed](#scroll_into_view_if_needed)
- [select_option](#select_option)
- [select_text](#select_text)
- [set_checked](#set_checked)
- [set_input_files](#set_input_files)
- [tap](#tap)
- [text_content](#text_content)
- [type](#type)
- [uncheck](#uncheck)
- [wait_for_element_state](#wait_for_element_state)
- [wait_for_selector](#wait_for_selector)

## as_element

### 同步

```python
def as_element(self) -> Optional[ForwardRef('ElementHandle')]
```

JSHandle.as_element

Returns either `null` or the object handle itself, if the object handle is an instance of `ElementHandle`.

#### Returns
Union[ElementHandle, None]

### 异步

```python
def as_element(self) -> Optional[ForwardRef('ElementHandle')]
```

JSHandle.as_element

Returns either `null` or the object handle itself, if the object handle is an instance of `ElementHandle`.

#### Returns
Union[ElementHandle, None]


## bounding_box

### 同步

```python
def bounding_box(self) -> Optional[patchright._impl._api_structures.FloatRect]
```

ElementHandle.bounding_box

This method returns the bounding box of the element, or `null` if the element is not visible. The bounding box is
calculated relative to the main frame viewport - which is usually the same as the browser window.

Scrolling affects the returned bounding box, similarly to
[Element.getBoundingClientRect](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect).
That means `x` and/or `y` may be negative.

Elements from child frames return the bounding box relative to the main frame, unlike the
[Element.getBoundingClientRect](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect).

Assuming the page is static, it is safe to use bounding box coordinates to perform input. For example, the
following snippet should click the center of the element.

**Usage**

```py
box = element_handle.bounding_box()
page.mouse.click(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
```

#### Returns
Union[{x: float, y: float, width: float, height: float}, None]

### 异步

```python
async def bounding_box(self) -> Optional[patchright._impl._api_structures.FloatRect]
```

ElementHandle.bounding_box

This method returns the bounding box of the element, or `null` if the element is not visible. The bounding box is
calculated relative to the main frame viewport - which is usually the same as the browser window.

Scrolling affects the returned bounding box, similarly to
[Element.getBoundingClientRect](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect).
That means `x` and/or `y` may be negative.

Elements from child frames return the bounding box relative to the main frame, unlike the
[Element.getBoundingClientRect](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect).

Assuming the page is static, it is safe to use bounding box coordinates to perform input. For example, the
following snippet should click the center of the element.

**Usage**

```py
box = await element_handle.bounding_box()
await page.mouse.click(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
```

#### Returns
Union[{x: float, y: float, width: float, height: float}, None]


## check

### 同步

```python signature
def check(self, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

ElementHandle.check

This method checks the element by performing the following steps:
1. Ensure that element is a checkbox or a radio input. If not, this method throws. If the element is already
   checked, this method returns immediately.
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the element, unless `force` option is set.
1. Scroll the element into view if needed.
1. Use `page.mouse` to click in the center of the element.
1. Ensure that the element is now checked. If not, this method throws.

If the element is detached from the DOM at any moment during the action, this method throws.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `position` | Union[{x: float, y: float}, None] | A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. |

### 异步

```python signature
async def check(self, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

ElementHandle.check

This method checks the element by performing the following steps:
1. Ensure that element is a checkbox or a radio input. If not, this method throws. If the element is already
   checked, this method returns immediately.
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the element, unless `force` option is set.
1. Scroll the element into view if needed.
1. Use `page.mouse` to click in the center of the element.
1. Ensure that the element is now checked. If not, this method throws.

If the element is detached from the DOM at any moment during the action, this method throws.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `position` | Union[{x: float, y: float}, None] | A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. |

## click

### 同步

```python signature
def click(self, *, button: Optional[Literal['left', 'middle', 'right']] = None, click_count: Optional[int] = None, delay: Optional[float] = None, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, steps: Optional[int] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

ElementHandle.click

This method clicks the element by performing the following steps:
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the element, unless `force` option is set.
1. Scroll the element into view if needed.
1. Use `page.mouse` to click in the center of the element, or the specified `position`.
1. Wait for initiated navigations to either succeed or fail, unless `no_wait_after` option is set.

If the element is detached from the DOM at any moment during the action, this method throws.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `button` | Union["left", "middle", "right", None] | Defaults to `left`. |
| `click_count` | Union[int, None] | defaults to 1. See [UIEvent.detail]. |
| `delay` | Union[float, None] | Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0. |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `modifiers` | Union[Sequence[Union["Alt", "Control", "ControlOrMeta", "Meta", "Shift"]], None] | Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current modifiers back. If not specified, currently pressed modifiers are used. "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS. |
| `no_wait_after` | Union[bool, None] | Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to inaccessible pages. Defaults to `false`. Deprecated: This option will default to `true` in the future. |
| `position` | Union[{x: float, y: float}, None] | A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `steps` | Union[int, None] | Defaults to 1. Sends `n` interpolated `mousemove` events to represent travel between Playwright's current cursor position and the provided destination. When set to 1, emits a single `mousemove` event at the destination location. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. |

### 异步

```python signature
async def click(self, *, button: Optional[Literal['left', 'middle', 'right']] = None, click_count: Optional[int] = None, delay: Optional[float] = None, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, steps: Optional[int] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

ElementHandle.click

This method clicks the element by performing the following steps:
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the element, unless `force` option is set.
1. Scroll the element into view if needed.
1. Use `page.mouse` to click in the center of the element, or the specified `position`.
1. Wait for initiated navigations to either succeed or fail, unless `no_wait_after` option is set.

If the element is detached from the DOM at any moment during the action, this method throws.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `button` | Union["left", "middle", "right", None] | Defaults to `left`. |
| `click_count` | Union[int, None] | defaults to 1. See [UIEvent.detail]. |
| `delay` | Union[float, None] | Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0. |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `modifiers` | Union[Sequence[Union["Alt", "Control", "ControlOrMeta", "Meta", "Shift"]], None] | Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current modifiers back. If not specified, currently pressed modifiers are used. "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS. |
| `no_wait_after` | Union[bool, None] | Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to inaccessible pages. Defaults to `false`. Deprecated: This option will default to `true` in the future. |
| `position` | Union[{x: float, y: float}, None] | A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `steps` | Union[int, None] | Defaults to 1. Sends `n` interpolated `mousemove` events to represent travel between Playwright's current cursor position and the provided destination. When set to 1, emits a single `mousemove` event at the destination location. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. |

## content_frame

### 同步

```python
def content_frame(self) -> Optional[ForwardRef('Frame')]
```

ElementHandle.content_frame

Returns the content frame for element handles referencing iframe nodes, or `null` otherwise

#### Returns
Union[Frame, None]

### 异步

```python
async def content_frame(self) -> Optional[ForwardRef('Frame')]
```

ElementHandle.content_frame

Returns the content frame for element handles referencing iframe nodes, or `null` otherwise

#### Returns
Union[Frame, None]


## dblclick

### 同步

```python signature
def dblclick(self, *, button: Optional[Literal['left', 'middle', 'right']] = None, delay: Optional[float] = None, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, steps: Optional[int] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

ElementHandle.dblclick

This method double clicks the element by performing the following steps:
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the element, unless `force` option is set.
1. Scroll the element into view if needed.
1. Use `page.mouse` to double click in the center of the element, or the specified `position`.

If the element is detached from the DOM at any moment during the action, this method throws.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

**NOTE** `elementHandle.dblclick()` dispatches two `click` events and a single `dblclick` event.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `button` | Union["left", "middle", "right", None] | Defaults to `left`. |
| `delay` | Union[float, None] | Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0. |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `modifiers` | Union[Sequence[Union["Alt", "Control", "ControlOrMeta", "Meta", "Shift"]], None] | Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current modifiers back. If not specified, currently pressed modifiers are used. "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `position` | Union[{x: float, y: float}, None] | A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `steps` | Union[int, None] | Defaults to 1. Sends `n` interpolated `mousemove` events to represent travel between Playwright's current cursor position and the provided destination. When set to 1, emits a single `mousemove` event at the destination location. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. |

### 异步

```python signature
async def dblclick(self, *, button: Optional[Literal['left', 'middle', 'right']] = None, delay: Optional[float] = None, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, steps: Optional[int] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

ElementHandle.dblclick

This method double clicks the element by performing the following steps:
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the element, unless `force` option is set.
1. Scroll the element into view if needed.
1. Use `page.mouse` to double click in the center of the element, or the specified `position`.

If the element is detached from the DOM at any moment during the action, this method throws.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

**NOTE** `elementHandle.dblclick()` dispatches two `click` events and a single `dblclick` event.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `button` | Union["left", "middle", "right", None] | Defaults to `left`. |
| `delay` | Union[float, None] | Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0. |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `modifiers` | Union[Sequence[Union["Alt", "Control", "ControlOrMeta", "Meta", "Shift"]], None] | Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current modifiers back. If not specified, currently pressed modifiers are used. "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `position` | Union[{x: float, y: float}, None] | A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `steps` | Union[int, None] | Defaults to 1. Sends `n` interpolated `mousemove` events to represent travel between Playwright's current cursor position and the provided destination. When set to 1, emits a single `mousemove` event at the destination location. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. |

## dispatch_event

### 同步

```python
def dispatch_event(self, type: str, event_init: Optional[Dict] = None) -> None
```

ElementHandle.dispatch_event

The snippet below dispatches the `click` event on the element. Regardless of the visibility state of the element,
`click` is dispatched. This is equivalent to calling
[element.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click).

**Usage**

```py
element_handle.dispatch_event("click")
```

Under the hood, it creates an instance of an event based on the given `type`, initializes it with `event_init`
properties and dispatches it on the element. Events are `composed`, `cancelable` and bubble by default.

Since `event_init` is event-specific, please refer to the events documentation for the lists of initial properties:
- [DeviceMotionEvent](https://developer.mozilla.org/en-US/docs/Web/API/DeviceMotionEvent/DeviceMotionEvent)
- [DeviceOrientationEvent](https://developer.mozilla.org/en-US/docs/Web/API/DeviceOrientationEvent/DeviceOrientationEvent)
- [DragEvent](https://developer.mozilla.org/en-US/docs/Web/API/DragEvent/DragEvent)
- [Event](https://developer.mozilla.org/en-US/docs/Web/API/Event/Event)
- [FocusEvent](https://developer.mozilla.org/en-US/docs/Web/API/FocusEvent/FocusEvent)
- [KeyboardEvent](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/KeyboardEvent)
- [MouseEvent](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/MouseEvent)
- [PointerEvent](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent/PointerEvent)
- [TouchEvent](https://developer.mozilla.org/en-US/docs/Web/API/TouchEvent/TouchEvent)
- [WheelEvent](https://developer.mozilla.org/en-US/docs/Web/API/WheelEvent/WheelEvent)

You can also specify `JSHandle` as the property value if you want live objects to be passed into the event:

```py
# note you can only create data_transfer in chromium and firefox
data_transfer = page.evaluate_handle("new DataTransfer()")
element_handle.dispatch_event("#source", "dragstart", {"dataTransfer": data_transfer})
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `type` | str | DOM event type: `"click"`, `"dragstart"`, etc. |
| `event_init` | Union[Dict, None] | Optional event-specific initialization properties. |

### 异步

```python
async def dispatch_event(self, type: str, event_init: Optional[Dict] = None) -> None
```

ElementHandle.dispatch_event

The snippet below dispatches the `click` event on the element. Regardless of the visibility state of the element,
`click` is dispatched. This is equivalent to calling
[element.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click).

**Usage**

```py
await element_handle.dispatch_event("click")
```

Under the hood, it creates an instance of an event based on the given `type`, initializes it with `event_init`
properties and dispatches it on the element. Events are `composed`, `cancelable` and bubble by default.

Since `event_init` is event-specific, please refer to the events documentation for the lists of initial properties:
- [DeviceMotionEvent](https://developer.mozilla.org/en-US/docs/Web/API/DeviceMotionEvent/DeviceMotionEvent)
- [DeviceOrientationEvent](https://developer.mozilla.org/en-US/docs/Web/API/DeviceOrientationEvent/DeviceOrientationEvent)
- [DragEvent](https://developer.mozilla.org/en-US/docs/Web/API/DragEvent/DragEvent)
- [Event](https://developer.mozilla.org/en-US/docs/Web/API/Event/Event)
- [FocusEvent](https://developer.mozilla.org/en-US/docs/Web/API/FocusEvent/FocusEvent)
- [KeyboardEvent](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/KeyboardEvent)
- [MouseEvent](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent/MouseEvent)
- [PointerEvent](https://developer.mozilla.org/en-US/docs/Web/API/PointerEvent/PointerEvent)
- [TouchEvent](https://developer.mozilla.org/en-US/docs/Web/API/TouchEvent/TouchEvent)
- [WheelEvent](https://developer.mozilla.org/en-US/docs/Web/API/WheelEvent/WheelEvent)

You can also specify `JSHandle` as the property value if you want live objects to be passed into the event:

```py
# note you can only create data_transfer in chromium and firefox
data_transfer = await page.evaluate_handle("new DataTransfer()")
await element_handle.dispatch_event("#source", "dragstart", {"dataTransfer": data_transfer})
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `type` | str | DOM event type: `"click"`, `"dragstart"`, etc. |
| `event_init` | Union[Dict, None] | Optional event-specific initialization properties. |

## dispose

### 同步

```python
def dispose(self) -> None
```

JSHandle.dispose

The `jsHandle.dispose` method stops referencing the element handle.

### 异步

```python
async def dispose(self) -> None
```

JSHandle.dispose

The `jsHandle.dispose` method stops referencing the element handle.


## eval_on_selector

### 同步

```python
def eval_on_selector(self, selector: str, expression: str, arg: Optional[Any] = None) -> Any
```

ElementHandle.eval_on_selector

Returns the return value of `expression`.

The method finds an element matching the specified selector in the `ElementHandle`s subtree and passes it as a
first argument to `expression`. If no elements match the selector, the method throws an error.

If `expression` returns a [Promise], then `element_handle.eval_on_selector()` would wait for the promise to resolve
and return its value.

**Usage**

```py
tweet_handle = page.query_selector(".tweet")
assert tweet_handle.eval_on_selector(".like", "node => node.innerText") == "100"
assert tweet_handle.eval_on_selector(".retweets", "node => node.innerText") == "10"
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to query for. |
| `expression` | str | JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked. |
| `arg` | Union[Any, None] | Optional argument to pass to `expression`. |

#### Returns
Any

### 异步

```python
async def eval_on_selector(self, selector: str, expression: str, arg: Optional[Any] = None) -> Any
```

ElementHandle.eval_on_selector

Returns the return value of `expression`.

The method finds an element matching the specified selector in the `ElementHandle`s subtree and passes it as a
first argument to `expression`. If no elements match the selector, the method throws an error.

If `expression` returns a [Promise], then `element_handle.eval_on_selector()` would wait for the promise to resolve
and return its value.

**Usage**

```py
tweet_handle = await page.query_selector(".tweet")
assert await tweet_handle.eval_on_selector(".like", "node => node.innerText") == "100"
assert await tweet_handle.eval_on_selector(".retweets", "node => node.innerText") == "10"
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to query for. |
| `expression` | str | JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked. |
| `arg` | Union[Any, None] | Optional argument to pass to `expression`. |

#### Returns
Any


## eval_on_selector_all

### 同步

```python
def eval_on_selector_all(self, selector: str, expression: str, arg: Optional[Any] = None) -> Any
```

ElementHandle.eval_on_selector_all

Returns the return value of `expression`.

The method finds all elements matching the specified selector in the `ElementHandle`'s subtree and passes an array
of matched elements as a first argument to `expression`.

If `expression` returns a [Promise], then `element_handle.eval_on_selector_all()` would wait for the promise to
resolve and return its value.

**Usage**

```html
<div class="feed">
  <div class="tweet">Hello!</div>
  <div class="tweet">Hi!</div>
</div>
```

```py
feed_handle = page.query_selector(".feed")
assert feed_handle.eval_on_selector_all(".tweet", "nodes => nodes.map(n => n.innerText)") == ["hello!", "hi!"]
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to query for. |
| `expression` | str | JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked. |
| `arg` | Union[Any, None] | Optional argument to pass to `expression`. |

#### Returns
Any

### 异步

```python
async def eval_on_selector_all(self, selector: str, expression: str, arg: Optional[Any] = None) -> Any
```

ElementHandle.eval_on_selector_all

Returns the return value of `expression`.

The method finds all elements matching the specified selector in the `ElementHandle`'s subtree and passes an array
of matched elements as a first argument to `expression`.

If `expression` returns a [Promise], then `element_handle.eval_on_selector_all()` would wait for the promise to
resolve and return its value.

**Usage**

```html
<div class="feed">
  <div class="tweet">Hello!</div>
  <div class="tweet">Hi!</div>
</div>
```

```py
feed_handle = await page.query_selector(".feed")
assert await feed_handle.eval_on_selector_all(".tweet", "nodes => nodes.map(n => n.innerText)") == ["hello!", "hi!"]
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to query for. |
| `expression` | str | JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked. |
| `arg` | Union[Any, None] | Optional argument to pass to `expression`. |

#### Returns
Any


## evaluate

### 同步

```python signature
def evaluate(self, expression: str, arg: Optional[Any] = None, *, isolated_context: Optional[bool] = True) -> Any
```

JSHandle.evaluate

Returns the return value of `expression`.

This method passes this handle as the first argument to `expression`.

If `expression` returns a [Promise], then `handle.evaluate` would wait for the promise to resolve and return its
value.

**Usage**

```py
tweet_handle = page.query_selector(".tweet .retweets")
assert tweet_handle.evaluate("node => node.innerText") == "10 retweets"
```

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

JSHandle.evaluate

Returns the return value of `expression`.

This method passes this handle as the first argument to `expression`.

If `expression` returns a [Promise], then `handle.evaluate` would wait for the promise to resolve and return its
value.

**Usage**

```py
tweet_handle = await page.query_selector(".tweet .retweets")
assert await tweet_handle.evaluate("node => node.innerText") == "10 retweets"
```

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

JSHandle.evaluate_handle

Returns the return value of `expression` as a `JSHandle`.

This method passes this handle as the first argument to `expression`.

The only difference between `jsHandle.evaluate` and `jsHandle.evaluateHandle` is that `jsHandle.evaluateHandle`
returns `JSHandle`.

If the function passed to the `jsHandle.evaluateHandle` returns a [Promise], then `jsHandle.evaluateHandle` would
wait for the promise to resolve and return its value.

See `page.evaluate_handle()` for more details.

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

JSHandle.evaluate_handle

Returns the return value of `expression` as a `JSHandle`.

This method passes this handle as the first argument to `expression`.

The only difference between `jsHandle.evaluate` and `jsHandle.evaluateHandle` is that `jsHandle.evaluateHandle`
returns `JSHandle`.

If the function passed to the `jsHandle.evaluateHandle` returns a [Promise], then `jsHandle.evaluateHandle` would
wait for the promise to resolve and return its value.

See `page.evaluate_handle()` for more details.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expression` | str | JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked. |
| `arg` | Union[Any, None] | Optional argument to pass to `expression`. |

#### Returns
JSHandle


## fill

### 同步

```python signature
def fill(self, value: str, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

ElementHandle.fill

This method waits for [actionability](https://playwright.dev/python/docs/actionability) checks, focuses the element, fills it and triggers an
`input` event after filling. Note that you can pass an empty string to clear the input field.

If the target element is not an `<input>`, `<textarea>` or `[contenteditable]` element, this method throws an
error. However, if the element is inside the `<label>` element that has an associated
[control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), the control will be filled
instead.

To send fine-grained keyboard events, use `locator.press_sequentially()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `value` | str | Value to set for the `<input>`, `<textarea>` or `[contenteditable]` element. |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

### 异步

```python signature
async def fill(self, value: str, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

ElementHandle.fill

This method waits for [actionability](https://playwright.dev/python/docs/actionability) checks, focuses the element, fills it and triggers an
`input` event after filling. Note that you can pass an empty string to clear the input field.

If the target element is not an `<input>`, `<textarea>` or `[contenteditable]` element, this method throws an
error. However, if the element is inside the `<label>` element that has an associated
[control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), the control will be filled
instead.

To send fine-grained keyboard events, use `locator.press_sequentially()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `value` | str | Value to set for the `<input>`, `<textarea>` or `[contenteditable]` element. |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

## focus

### 同步

```python
def focus(self) -> None
```

ElementHandle.focus

Calls [focus](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/focus) on the element.

### 异步

```python
async def focus(self) -> None
```

ElementHandle.focus

Calls [focus](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/focus) on the element.


## get_attribute

### 同步

```python
def get_attribute(self, name: str) -> Optional[str]
```

ElementHandle.get_attribute

Returns element attribute value.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | Attribute name to get the value for. |

#### Returns
Union[str, None]

### 异步

```python
async def get_attribute(self, name: str) -> Optional[str]
```

ElementHandle.get_attribute

Returns element attribute value.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | Attribute name to get the value for. |

#### Returns
Union[str, None]


## get_properties

### 同步

```python
def get_properties(self) -> Dict[str, ForwardRef('JSHandle')]
```

JSHandle.get_properties

The method returns a map with **own property names** as keys and JSHandle instances for the property values.

**Usage**

```py
handle = page.evaluate_handle("({ window, document })")
properties = handle.get_properties()
window_handle = properties.get("window")
document_handle = properties.get("document")
handle.dispose()
```

#### Returns
Dict[str, JSHandle]

### 异步

```python
async def get_properties(self) -> Dict[str, ForwardRef('JSHandle')]
```

JSHandle.get_properties

The method returns a map with **own property names** as keys and JSHandle instances for the property values.

**Usage**

```py
handle = await page.evaluate_handle("({ window, document })")
properties = await handle.get_properties()
window_handle = properties.get("window")
document_handle = properties.get("document")
await handle.dispose()
```

#### Returns
Dict[str, JSHandle]


## get_property

### 同步

```python
def get_property(self, property_name: str) -> 'JSHandle'
```

JSHandle.get_property

Fetches a single property from the referenced object.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `property_name` | str | property to get |

#### Returns
JSHandle

### 异步

```python
async def get_property(self, property_name: str) -> 'JSHandle'
```

JSHandle.get_property

Fetches a single property from the referenced object.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `property_name` | str | property to get |

#### Returns
JSHandle


## hover

### 同步

```python signature
def hover(self, *, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

ElementHandle.hover

This method hovers over the element by performing the following steps:
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the element, unless `force` option is set.
1. Scroll the element into view if needed.
1. Use `page.mouse` to hover over the center of the element, or the specified `position`.

If the element is detached from the DOM at any moment during the action, this method throws.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `modifiers` | Union[Sequence[Union["Alt", "Control", "ControlOrMeta", "Meta", "Shift"]], None] | Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current modifiers back. If not specified, currently pressed modifiers are used. "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `position` | Union[{x: float, y: float}, None] | A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. |

### 异步

```python signature
async def hover(self, *, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

ElementHandle.hover

This method hovers over the element by performing the following steps:
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the element, unless `force` option is set.
1. Scroll the element into view if needed.
1. Use `page.mouse` to hover over the center of the element, or the specified `position`.

If the element is detached from the DOM at any moment during the action, this method throws.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `modifiers` | Union[Sequence[Union["Alt", "Control", "ControlOrMeta", "Meta", "Shift"]], None] | Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current modifiers back. If not specified, currently pressed modifiers are used. "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `position` | Union[{x: float, y: float}, None] | A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. |

## inner_html

### 同步

```python
def inner_html(self) -> str
```

ElementHandle.inner_html

Returns the `element.innerHTML`.

#### Returns
str

### 异步

```python
async def inner_html(self) -> str
```

ElementHandle.inner_html

Returns the `element.innerHTML`.

#### Returns
str


## inner_text

### 同步

```python
def inner_text(self) -> str
```

ElementHandle.inner_text

Returns the `element.innerText`.

#### Returns
str

### 异步

```python
async def inner_text(self) -> str
```

ElementHandle.inner_text

Returns the `element.innerText`.

#### Returns
str


## input_value

### 同步

```python signature
def input_value(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> str
```

ElementHandle.input_value

Returns `input.value` for the selected `<input>` or `<textarea>` or `<select>` element.

Throws for non-input elements. However, if the element is inside the `<label>` element that has an associated
[control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), returns the value of the
control.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Deprecated: This option is ignored. The value is returned immediately. |

#### Returns
str

### 异步

```python signature
async def input_value(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> str
```

ElementHandle.input_value

Returns `input.value` for the selected `<input>` or `<textarea>` or `<select>` element.

Throws for non-input elements. However, if the element is inside the `<label>` element that has an associated
[control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), returns the value of the
control.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Deprecated: This option is ignored. The value is returned immediately. |

#### Returns
str


## is_checked

### 同步

```python
def is_checked(self) -> bool
```

ElementHandle.is_checked

Returns whether the element is checked. Throws if the element is not a checkbox or radio input.

#### Returns
bool

### 异步

```python
async def is_checked(self) -> bool
```

ElementHandle.is_checked

Returns whether the element is checked. Throws if the element is not a checkbox or radio input.

#### Returns
bool


## is_disabled

### 同步

```python
def is_disabled(self) -> bool
```

ElementHandle.is_disabled

Returns whether the element is disabled, the opposite of [enabled](https://playwright.dev/python/docs/actionability#enabled).

#### Returns
bool

### 异步

```python
async def is_disabled(self) -> bool
```

ElementHandle.is_disabled

Returns whether the element is disabled, the opposite of [enabled](https://playwright.dev/python/docs/actionability#enabled).

#### Returns
bool


## is_editable

### 同步

```python
def is_editable(self) -> bool
```

ElementHandle.is_editable

Returns whether the element is [editable](https://playwright.dev/python/docs/actionability#editable).

#### Returns
bool

### 异步

```python
async def is_editable(self) -> bool
```

ElementHandle.is_editable

Returns whether the element is [editable](https://playwright.dev/python/docs/actionability#editable).

#### Returns
bool


## is_enabled

### 同步

```python
def is_enabled(self) -> bool
```

ElementHandle.is_enabled

Returns whether the element is [enabled](https://playwright.dev/python/docs/actionability#enabled).

#### Returns
bool

### 异步

```python
async def is_enabled(self) -> bool
```

ElementHandle.is_enabled

Returns whether the element is [enabled](https://playwright.dev/python/docs/actionability#enabled).

#### Returns
bool


## is_hidden

### 同步

```python
def is_hidden(self) -> bool
```

ElementHandle.is_hidden

Returns whether the element is hidden, the opposite of [visible](https://playwright.dev/python/docs/actionability#visible).

#### Returns
bool

### 异步

```python
async def is_hidden(self) -> bool
```

ElementHandle.is_hidden

Returns whether the element is hidden, the opposite of [visible](https://playwright.dev/python/docs/actionability#visible).

#### Returns
bool


## is_visible

### 同步

```python
def is_visible(self) -> bool
```

ElementHandle.is_visible

Returns whether the element is [visible](https://playwright.dev/python/docs/actionability#visible).

#### Returns
bool

### 异步

```python
async def is_visible(self) -> bool
```

ElementHandle.is_visible

Returns whether the element is [visible](https://playwright.dev/python/docs/actionability#visible).

#### Returns
bool


## json_value

### 同步

```python
def json_value(self) -> Any
```

JSHandle.json_value

Returns a JSON representation of the object. If the object has a `toJSON` function, it **will not be called**.

**NOTE** The method will return an empty JSON object if the referenced object is not stringifiable. It will throw
an error if the object has circular references.

#### Returns
Any

### 异步

```python
async def json_value(self) -> Any
```

JSHandle.json_value

Returns a JSON representation of the object. If the object has a `toJSON` function, it **will not be called**.

**NOTE** The method will return an empty JSON object if the referenced object is not stringifiable. It will throw
an error if the object has circular references.

#### Returns
Any


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


## owner_frame

### 同步

```python
def owner_frame(self) -> Optional[ForwardRef('Frame')]
```

ElementHandle.owner_frame

Returns the frame containing the given element.

#### Returns
Union[Frame, None]

### 异步

```python
async def owner_frame(self) -> Optional[ForwardRef('Frame')]
```

ElementHandle.owner_frame

Returns the frame containing the given element.

#### Returns
Union[Frame, None]


## press

### 同步

```python signature
def press(self, key: str, *, delay: Optional[float] = None, no_wait_after: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

ElementHandle.press

Focuses the element, and then uses `keyboard.down()` and `keyboard.up()`.

`key` can specify the intended
[keyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key) value or a single character
to generate the text for. A superset of the `key` values can be found
[here](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values). Examples of the keys are:

`F1` - `F12`, `Digit0`- `Digit9`, `KeyA`- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`,
`Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp`,
etc.

Following modification shortcuts are also supported: `Shift`, `Control`, `Alt`, `Meta`, `ShiftLeft`,
`ControlOrMeta`.

Holding down `Shift` will type the text that corresponds to the `key` in the upper case.

If `key` is a single character, it is case-sensitive, so the values `a` and `A` will generate different respective
texts.

Shortcuts such as `key: "Control+o"`, `key: "Control++` or `key: "Control+Shift+T"` are supported as well. When
specified with the modifier, modifier is pressed and being held while the subsequent key is being pressed.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | str | Name of the key to press or a character to generate, such as `ArrowLeft` or `a`. |
| `delay` | Union[float, None] | Time to wait between `keydown` and `keyup` in milliseconds. Defaults to 0. |
| `no_wait_after` | Union[bool, None] | Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to inaccessible pages. Defaults to `false`. Deprecated: This option will default to `true` in the future. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

### 异步

```python signature
async def press(self, key: str, *, delay: Optional[float] = None, no_wait_after: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

ElementHandle.press

Focuses the element, and then uses `keyboard.down()` and `keyboard.up()`.

`key` can specify the intended
[keyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key) value or a single character
to generate the text for. A superset of the `key` values can be found
[here](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values). Examples of the keys are:

`F1` - `F12`, `Digit0`- `Digit9`, `KeyA`- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`,
`Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp`,
etc.

Following modification shortcuts are also supported: `Shift`, `Control`, `Alt`, `Meta`, `ShiftLeft`,
`ControlOrMeta`.

Holding down `Shift` will type the text that corresponds to the `key` in the upper case.

If `key` is a single character, it is case-sensitive, so the values `a` and `A` will generate different respective
texts.

Shortcuts such as `key: "Control+o"`, `key: "Control++` or `key: "Control+Shift+T"` are supported as well. When
specified with the modifier, modifier is pressed and being held while the subsequent key is being pressed.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | str | Name of the key to press or a character to generate, such as `ArrowLeft` or `a`. |
| `delay` | Union[float, None] | Time to wait between `keydown` and `keyup` in milliseconds. Defaults to 0. |
| `no_wait_after` | Union[bool, None] | Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to inaccessible pages. Defaults to `false`. Deprecated: This option will default to `true` in the future. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

## query_selector

### 同步

```python
def query_selector(self, selector: str) -> Optional[ForwardRef('ElementHandle')]
```

ElementHandle.query_selector

The method finds an element matching the specified selector in the `ElementHandle`'s subtree. If no elements match
the selector, returns `null`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to query for. |

#### Returns
Union[ElementHandle, None]

### 异步

```python
async def query_selector(self, selector: str) -> Optional[ForwardRef('ElementHandle')]
```

ElementHandle.query_selector

The method finds an element matching the specified selector in the `ElementHandle`'s subtree. If no elements match
the selector, returns `null`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to query for. |

#### Returns
Union[ElementHandle, None]


## query_selector_all

### 同步

```python
def query_selector_all(self, selector: str) -> List[ForwardRef('ElementHandle')]
```

ElementHandle.query_selector_all

The method finds all elements matching the specified selector in the `ElementHandle`s subtree. If no elements match
the selector, returns empty array.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to query for. |

#### Returns
List[ElementHandle]

### 异步

```python
async def query_selector_all(self, selector: str) -> List[ForwardRef('ElementHandle')]
```

ElementHandle.query_selector_all

The method finds all elements matching the specified selector in the `ElementHandle`s subtree. If no elements match
the selector, returns empty array.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to query for. |

#### Returns
List[ElementHandle]


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


## screenshot

### 同步

```python signature
def screenshot(self, *, animations: Optional[Literal['allow', 'disabled']] = None, caret: Optional[Literal['hide', 'initial']] = None, mask: Optional[Sequence[ForwardRef('Locator')]] = None, mask_color: Optional[str] = None, omit_background: Optional[bool] = None, path: Union[pathlib.Path, str, NoneType] = None, quality: Optional[int] = None, scale: Optional[Literal['css', 'device']] = None, style: Optional[str] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, type: Optional[Literal['jpeg', 'png', 'webp']] = None) -> bytes
```

ElementHandle.screenshot

This method captures a screenshot of the page, clipped to the size and position of this particular element. If the
element is covered by other elements, it will not be actually visible on the screenshot. If the element is a
scrollable container, only the currently scrolled content will be visible on the screenshot.

This method waits for the [actionability](https://playwright.dev/python/docs/actionability) checks, then scrolls element into view before taking
a screenshot. If the element is detached from DOM, the method throws an error.

Returns the buffer with the captured screenshot.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `animations` | Union["allow", "disabled", None] | When set to `"disabled"`, stops CSS animations, CSS transitions and Web Animations. Animations get different treatment depending on their duration: - finite animations are fast-forwarded to completion, so they'll fire `transitionend` event. - infinite animations are canceled to initial state, and then played over after the screenshot.  Defaults to `"allow"` that leaves animations untouched. |
| `caret` | Union["hide", "initial", None] | When set to `"hide"`, screenshot will hide text caret. When set to `"initial"`, text caret behavior will not be changed.  Defaults to `"hide"`. |
| `mask` | Union[Sequence[Locator], None] | Specify locators that should be masked when the screenshot is taken. Masked elements will be overlaid with a pink box `#FF00FF` (customized by `mask_color`) that completely covers its bounding box. The mask is also applied to invisible elements, see Matching only visible elements to disable that. |
| `mask_color` | Union[str, None] | Specify the color of the overlay box for masked elements, in [CSS color format](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value). Default color is pink `#FF00FF`. |
| `omit_background` | Union[bool, None] | Hides default white background and allows capturing screenshots with transparency. Not applicable to `jpeg` images. Defaults to `false`. |
| `path` | Union[pathlib.Path, str, None] | The file path to save the image to. The screenshot type will be inferred from file extension. If `path` is a relative path, then it is resolved relative to the current working directory. If no path is provided, the image won't be saved to the disk. |
| `quality` | Union[int, None] | The quality of the image, between 0-100. Not applicable to `png` images. For `jpeg` the default is `80`. For `webp`, a quality of `100` (the default) produces a lossless image, while lower values use lossy compression. |
| `scale` | Union["css", "device", None] | When set to `"css"`, screenshot will have a single pixel per each css pixel on the page. For high-dpi devices, this will keep screenshots small. Using `"device"` option will produce a single pixel per each device pixel, so screenshots of high-dpi devices will be twice as large or even larger.  Defaults to `"device"`. |
| `style` | Union[str, None] | Text of the stylesheet to apply while making the screenshot. This is where you can hide dynamic elements, make elements invisible or change their properties to help you creating repeatable screenshots. This stylesheet pierces the Shadow DOM and applies to the inner frames. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `type` | Union["jpeg", "png", "webp", None] | Specify screenshot type, defaults to `png`. |

#### Returns
bytes

### 异步

```python signature
async def screenshot(self, *, animations: Optional[Literal['allow', 'disabled']] = None, caret: Optional[Literal['hide', 'initial']] = None, mask: Optional[Sequence[ForwardRef('Locator')]] = None, mask_color: Optional[str] = None, omit_background: Optional[bool] = None, path: Union[pathlib.Path, str, NoneType] = None, quality: Optional[int] = None, scale: Optional[Literal['css', 'device']] = None, style: Optional[str] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, type: Optional[Literal['jpeg', 'png', 'webp']] = None) -> bytes
```

ElementHandle.screenshot

This method captures a screenshot of the page, clipped to the size and position of this particular element. If the
element is covered by other elements, it will not be actually visible on the screenshot. If the element is a
scrollable container, only the currently scrolled content will be visible on the screenshot.

This method waits for the [actionability](https://playwright.dev/python/docs/actionability) checks, then scrolls element into view before taking
a screenshot. If the element is detached from DOM, the method throws an error.

Returns the buffer with the captured screenshot.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `animations` | Union["allow", "disabled", None] | When set to `"disabled"`, stops CSS animations, CSS transitions and Web Animations. Animations get different treatment depending on their duration: - finite animations are fast-forwarded to completion, so they'll fire `transitionend` event. - infinite animations are canceled to initial state, and then played over after the screenshot.  Defaults to `"allow"` that leaves animations untouched. |
| `caret` | Union["hide", "initial", None] | When set to `"hide"`, screenshot will hide text caret. When set to `"initial"`, text caret behavior will not be changed.  Defaults to `"hide"`. |
| `mask` | Union[Sequence[Locator], None] | Specify locators that should be masked when the screenshot is taken. Masked elements will be overlaid with a pink box `#FF00FF` (customized by `mask_color`) that completely covers its bounding box. The mask is also applied to invisible elements, see Matching only visible elements to disable that. |
| `mask_color` | Union[str, None] | Specify the color of the overlay box for masked elements, in [CSS color format](https://developer.mozilla.org/en-US/docs/Web/CSS/color_value). Default color is pink `#FF00FF`. |
| `omit_background` | Union[bool, None] | Hides default white background and allows capturing screenshots with transparency. Not applicable to `jpeg` images. Defaults to `false`. |
| `path` | Union[pathlib.Path, str, None] | The file path to save the image to. The screenshot type will be inferred from file extension. If `path` is a relative path, then it is resolved relative to the current working directory. If no path is provided, the image won't be saved to the disk. |
| `quality` | Union[int, None] | The quality of the image, between 0-100. Not applicable to `png` images. For `jpeg` the default is `80`. For `webp`, a quality of `100` (the default) produces a lossless image, while lower values use lossy compression. |
| `scale` | Union["css", "device", None] | When set to `"css"`, screenshot will have a single pixel per each css pixel on the page. For high-dpi devices, this will keep screenshots small. Using `"device"` option will produce a single pixel per each device pixel, so screenshots of high-dpi devices will be twice as large or even larger.  Defaults to `"device"`. |
| `style` | Union[str, None] | Text of the stylesheet to apply while making the screenshot. This is where you can hide dynamic elements, make elements invisible or change their properties to help you creating repeatable screenshots. This stylesheet pierces the Shadow DOM and applies to the inner frames. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `type` | Union["jpeg", "png", "webp", None] | Specify screenshot type, defaults to `png`. |

#### Returns
bytes


## scroll_into_view_if_needed

### 同步

```python signature
def scroll_into_view_if_needed(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

ElementHandle.scroll_into_view_if_needed

This method waits for [actionability](https://playwright.dev/python/docs/actionability) checks, then tries to scroll element into view, unless
it is completely visible as defined by
[IntersectionObserver](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API)'s `ratio`.

Throws when `elementHandle` does not point to an element
[connected](https://developer.mozilla.org/en-US/docs/Web/API/Node/isConnected) to a Document or a ShadowRoot.

See [scrolling](https://playwright.dev/python/docs/input#scrolling) for alternative ways to scroll.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

### 异步

```python signature
async def scroll_into_view_if_needed(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

ElementHandle.scroll_into_view_if_needed

This method waits for [actionability](https://playwright.dev/python/docs/actionability) checks, then tries to scroll element into view, unless
it is completely visible as defined by
[IntersectionObserver](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API)'s `ratio`.

Throws when `elementHandle` does not point to an element
[connected](https://developer.mozilla.org/en-US/docs/Web/API/Node/isConnected) to a Document or a ShadowRoot.

See [scrolling](https://playwright.dev/python/docs/input#scrolling) for alternative ways to scroll.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

## select_option

### 同步

```python signature
def select_option(self, value: Union[str, Sequence[str], NoneType] = None, *, element: Union[ForwardRef('ElementHandle'), Sequence[ForwardRef('ElementHandle')], NoneType] = None, force: Optional[bool] = None, index: Union[int, Sequence[int], NoneType] = None, label: Union[str, Sequence[str], NoneType] = None, no_wait_after: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> List[str]
```

ElementHandle.select_option

This method waits for [actionability](https://playwright.dev/python/docs/actionability) checks, waits until all specified options are present in
the `<select>` element and selects these options.

If the target element is not a `<select>` element, this method throws an error. However, if the element is inside
the `<label>` element that has an associated
[control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), the control will be used
instead.

Returns the array of option values that have been successfully selected.

Triggers a `change` and `input` event once all the provided options have been selected.

**Usage**

```py
# Single selection matching the value or label
handle.select_option("blue")
# single selection matching both the label
handle.select_option(label="blue")
# multiple selection
handle.select_option(value=["red", "green", "blue"])
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `value` | Union[Sequence[str], str, None] | Options to select by value. If the `<select>` has the `multiple` attribute, all given options are selected, otherwise only the first option matching one of the passed options is selected. Optional. |
| `element` | Union[ElementHandle, Sequence[ElementHandle], None] | Option elements to select. Optional. |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `index` | Union[Sequence[int], int, None] | Options to select by index. Optional. |
| `label` | Union[Sequence[str], str, None] | Options to select by label. If the `<select>` has the `multiple` attribute, all given options are selected, otherwise only the first option matching one of the passed options is selected. Optional. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
List[str]

### 异步

```python signature
async def select_option(self, value: Union[str, Sequence[str], NoneType] = None, *, element: Union[ForwardRef('ElementHandle'), Sequence[ForwardRef('ElementHandle')], NoneType] = None, force: Optional[bool] = None, index: Union[int, Sequence[int], NoneType] = None, label: Union[str, Sequence[str], NoneType] = None, no_wait_after: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> List[str]
```

ElementHandle.select_option

This method waits for [actionability](https://playwright.dev/python/docs/actionability) checks, waits until all specified options are present in
the `<select>` element and selects these options.

If the target element is not a `<select>` element, this method throws an error. However, if the element is inside
the `<label>` element that has an associated
[control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), the control will be used
instead.

Returns the array of option values that have been successfully selected.

Triggers a `change` and `input` event once all the provided options have been selected.

**Usage**

```py
# Single selection matching the value or label
await handle.select_option("blue")
# single selection matching the label
await handle.select_option(label="blue")
# multiple selection
await handle.select_option(value=["red", "green", "blue"])
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `value` | Union[Sequence[str], str, None] | Options to select by value. If the `<select>` has the `multiple` attribute, all given options are selected, otherwise only the first option matching one of the passed options is selected. Optional. |
| `element` | Union[ElementHandle, Sequence[ElementHandle], None] | Option elements to select. Optional. |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `index` | Union[Sequence[int], int, None] | Options to select by index. Optional. |
| `label` | Union[Sequence[str], str, None] | Options to select by label. If the `<select>` has the `multiple` attribute, all given options are selected, otherwise only the first option matching one of the passed options is selected. Optional. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
List[str]


## select_text

### 同步

```python signature
def select_text(self, *, force: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

ElementHandle.select_text

This method waits for [actionability](https://playwright.dev/python/docs/actionability) checks, then focuses the element and selects all its
text content.

If the element is inside the `<label>` element that has an associated
[control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), focuses and selects text in
the control instead.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

### 异步

```python signature
async def select_text(self, *, force: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

ElementHandle.select_text

This method waits for [actionability](https://playwright.dev/python/docs/actionability) checks, then focuses the element and selects all its
text content.

If the element is inside the `<label>` element that has an associated
[control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), focuses and selects text in
the control instead.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

## set_checked

### 同步

```python signature
def set_checked(self, checked: bool, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

ElementHandle.set_checked

This method checks or unchecks an element by performing the following steps:
1. Ensure that element is a checkbox or a radio input. If not, this method throws.
1. If the element already has the right checked state, this method returns immediately.
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the matched element, unless `force` option is set. If
   the element is detached during the checks, the whole action is retried.
1. Scroll the element into view if needed.
1. Use `page.mouse` to click in the center of the element.
1. Ensure that the element is now checked or unchecked. If not, this method throws.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `checked` | bool | Whether to check or uncheck the checkbox. |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `position` | Union[{x: float, y: float}, None] | A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. |

### 异步

```python signature
async def set_checked(self, checked: bool, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

ElementHandle.set_checked

This method checks or unchecks an element by performing the following steps:
1. Ensure that element is a checkbox or a radio input. If not, this method throws.
1. If the element already has the right checked state, this method returns immediately.
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the matched element, unless `force` option is set. If
   the element is detached during the checks, the whole action is retried.
1. Scroll the element into view if needed.
1. Use `page.mouse` to click in the center of the element.
1. Ensure that the element is now checked or unchecked. If not, this method throws.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `checked` | bool | Whether to check or uncheck the checkbox. |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `position` | Union[{x: float, y: float}, None] | A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. |

## set_input_files

### 同步

```python signature
def set_input_files(self, files: Union[str, pathlib.Path, Sequence[Union[str, pathlib.Path]], patchright._impl._api_structures.FilePayload, Sequence[patchright._impl._api_structures.FilePayload]], *, no_wait_after: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

ElementHandle.set_input_files

Sets the value of the file input to these file paths or files. If some of the `filePaths` are relative paths, then
they are resolved relative to the current working directory. For empty array, clears the selected files. For inputs
with a `[webkitdirectory]` attribute, only a single directory path is supported.

This method expects `ElementHandle` to point to an
[input element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input). However, if the element is inside
the `<label>` element that has an associated
[control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), targets the control instead.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `files` | Union[Sequence[Union[pathlib.Path, str]], Sequence[{name: str, mimeType: str, buffer: bytes}], pathlib.Path, str, {name: str, mimeType: str, buffer: bytes}] |  |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

### 异步

```python signature
async def set_input_files(self, files: Union[str, pathlib.Path, Sequence[Union[str, pathlib.Path]], patchright._impl._api_structures.FilePayload, Sequence[patchright._impl._api_structures.FilePayload]], *, no_wait_after: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

ElementHandle.set_input_files

Sets the value of the file input to these file paths or files. If some of the `filePaths` are relative paths, then
they are resolved relative to the current working directory. For empty array, clears the selected files. For inputs
with a `[webkitdirectory]` attribute, only a single directory path is supported.

This method expects `ElementHandle` to point to an
[input element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input). However, if the element is inside
the `<label>` element that has an associated
[control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), targets the control instead.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `files` | Union[Sequence[Union[pathlib.Path, str]], Sequence[{name: str, mimeType: str, buffer: bytes}], pathlib.Path, str, {name: str, mimeType: str, buffer: bytes}] |  |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

## tap

### 同步

```python signature
def tap(self, *, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

ElementHandle.tap

This method taps the element by performing the following steps:
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the element, unless `force` option is set.
1. Scroll the element into view if needed.
1. Use `page.touchscreen` to tap the center of the element, or the specified `position`.

If the element is detached from the DOM at any moment during the action, this method throws.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

**NOTE** `elementHandle.tap()` requires that the `hasTouch` option of the browser context be set to true.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `modifiers` | Union[Sequence[Union["Alt", "Control", "ControlOrMeta", "Meta", "Shift"]], None] | Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current modifiers back. If not specified, currently pressed modifiers are used. "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `position` | Union[{x: float, y: float}, None] | A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. |

### 异步

```python signature
async def tap(self, *, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

ElementHandle.tap

This method taps the element by performing the following steps:
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the element, unless `force` option is set.
1. Scroll the element into view if needed.
1. Use `page.touchscreen` to tap the center of the element, or the specified `position`.

If the element is detached from the DOM at any moment during the action, this method throws.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

**NOTE** `elementHandle.tap()` requires that the `hasTouch` option of the browser context be set to true.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `modifiers` | Union[Sequence[Union["Alt", "Control", "ControlOrMeta", "Meta", "Shift"]], None] | Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current modifiers back. If not specified, currently pressed modifiers are used. "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `position` | Union[{x: float, y: float}, None] | A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. |

## text_content

### 同步

```python
def text_content(self) -> Optional[str]
```

ElementHandle.text_content

Returns the `node.textContent`.

#### Returns
Union[str, None]

### 异步

```python
async def text_content(self) -> Optional[str]
```

ElementHandle.text_content

Returns the `node.textContent`.

#### Returns
Union[str, None]


## type

### 同步

```python signature
def type(self, text: str, *, delay: Optional[float] = None, no_wait_after: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

ElementHandle.type

Focuses the element, and then sends a `keydown`, `keypress`/`input`, and `keyup` event for each character in the
text.

To press a special key, like `Control` or `ArrowDown`, use `element_handle.press()`.

**Usage**

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `text` | str | A text to type into a focused element. |
| `delay` | Union[float, None] | Time to wait between key presses in milliseconds. Defaults to 0. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

### 异步

```python signature
async def type(self, text: str, *, delay: Optional[float] = None, no_wait_after: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

ElementHandle.type

Focuses the element, and then sends a `keydown`, `keypress`/`input`, and `keyup` event for each character in the
text.

To press a special key, like `Control` or `ArrowDown`, use `element_handle.press()`.

**Usage**

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `text` | str | A text to type into a focused element. |
| `delay` | Union[float, None] | Time to wait between key presses in milliseconds. Defaults to 0. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

## uncheck

### 同步

```python signature
def uncheck(self, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

ElementHandle.uncheck

This method checks the element by performing the following steps:
1. Ensure that element is a checkbox or a radio input. If not, this method throws. If the element is already
   unchecked, this method returns immediately.
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the element, unless `force` option is set.
1. Scroll the element into view if needed.
1. Use `page.mouse` to click in the center of the element.
1. Ensure that the element is now unchecked. If not, this method throws.

If the element is detached from the DOM at any moment during the action, this method throws.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `position` | Union[{x: float, y: float}, None] | A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. |

### 异步

```python signature
async def uncheck(self, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

ElementHandle.uncheck

This method checks the element by performing the following steps:
1. Ensure that element is a checkbox or a radio input. If not, this method throws. If the element is already
   unchecked, this method returns immediately.
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the element, unless `force` option is set.
1. Scroll the element into view if needed.
1. Use `page.mouse` to click in the center of the element.
1. Ensure that the element is now unchecked. If not, this method throws.

If the element is detached from the DOM at any moment during the action, this method throws.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `position` | Union[{x: float, y: float}, None] | A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. |

## wait_for_element_state

### 同步

```python signature
def wait_for_element_state(self, state: Literal['disabled', 'editable', 'enabled', 'hidden', 'stable', 'visible'], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

ElementHandle.wait_for_element_state

Returns when the element satisfies the `state`.

Depending on the `state` parameter, this method waits for one of the [actionability](https://playwright.dev/python/docs/actionability) checks to
pass. This method throws when the element is detached while waiting, unless waiting for the `"hidden"` state.
- `"visible"` Wait until the element is [visible](https://playwright.dev/python/docs/actionability#visible).
- `"hidden"` Wait until the element is [not visible](https://playwright.dev/python/docs/actionability#visible) or not attached. Note that
  waiting for hidden does not throw when the element detaches.
- `"stable"` Wait until the element is both [visible](https://playwright.dev/python/docs/actionability#visible) and
  [stable](https://playwright.dev/python/docs/actionability#stable).
- `"enabled"` Wait until the element is [enabled](https://playwright.dev/python/docs/actionability#enabled).
- `"disabled"` Wait until the element is [not enabled](https://playwright.dev/python/docs/actionability#enabled).
- `"editable"` Wait until the element is [editable](https://playwright.dev/python/docs/actionability#editable).

If the element does not satisfy the condition for the `timeout` milliseconds, this method will throw.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `state` | Union["disabled", "editable", "enabled", "hidden", "stable", "visible"] | A state to wait for, see below for more details. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

### 异步

```python signature
async def wait_for_element_state(self, state: Literal['disabled', 'editable', 'enabled', 'hidden', 'stable', 'visible'], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

ElementHandle.wait_for_element_state

Returns when the element satisfies the `state`.

Depending on the `state` parameter, this method waits for one of the [actionability](https://playwright.dev/python/docs/actionability) checks to
pass. This method throws when the element is detached while waiting, unless waiting for the `"hidden"` state.
- `"visible"` Wait until the element is [visible](https://playwright.dev/python/docs/actionability#visible).
- `"hidden"` Wait until the element is [not visible](https://playwright.dev/python/docs/actionability#visible) or not attached. Note that
  waiting for hidden does not throw when the element detaches.
- `"stable"` Wait until the element is both [visible](https://playwright.dev/python/docs/actionability#visible) and
  [stable](https://playwright.dev/python/docs/actionability#stable).
- `"enabled"` Wait until the element is [enabled](https://playwright.dev/python/docs/actionability#enabled).
- `"disabled"` Wait until the element is [not enabled](https://playwright.dev/python/docs/actionability#enabled).
- `"editable"` Wait until the element is [editable](https://playwright.dev/python/docs/actionability#editable).

If the element does not satisfy the condition for the `timeout` milliseconds, this method will throw.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `state` | Union["disabled", "editable", "enabled", "hidden", "stable", "visible"] | A state to wait for, see below for more details. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

## wait_for_selector

### 同步

```python signature
def wait_for_selector(self, selector: str, *, state: Optional[Literal['attached', 'detached', 'hidden', 'visible']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Optional[ForwardRef('ElementHandle')]
```

ElementHandle.wait_for_selector

Returns element specified by selector when it satisfies `state` option. Returns `null` if waiting for `hidden` or
`detached`.

Wait for the `selector` relative to the element handle to satisfy `state` option (either appear/disappear from dom,
or become visible/hidden). If at the moment of calling the method `selector` already satisfies the condition, the
method will return immediately. If the selector doesn't satisfy the condition for the `timeout` milliseconds, the
function will throw.

**Usage**

```py
page.set_content("<div><span></span></div>")
div = page.query_selector("div")
# waiting for the "span" selector relative to the div.
span = div.wait_for_selector("span", state="attached")
```

**NOTE** This method does not work across navigations, use `page.wait_for_selector()` instead.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to query for. |
| `state` | Union["attached", "detached", "hidden", "visible", None] | Defaults to `'visible'`. Can be either: - `'attached'` - wait for element to be present in DOM. - `'detached'` - wait for element to not be present in DOM. - `'visible'` - wait for element to have non-empty bounding box and no `visibility:hidden`. Note that element without any content or with `display:none` has an empty bounding box and is not considered visible. - `'hidden'` - wait for element to be either detached from DOM, or have an empty bounding box or `visibility:hidden`. This is opposite to the `'visible'` option. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
Union[ElementHandle, None]

### 异步

```python signature
async def wait_for_selector(self, selector: str, *, state: Optional[Literal['attached', 'detached', 'hidden', 'visible']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Optional[ForwardRef('ElementHandle')]
```

ElementHandle.wait_for_selector

Returns element specified by selector when it satisfies `state` option. Returns `null` if waiting for `hidden` or
`detached`.

Wait for the `selector` relative to the element handle to satisfy `state` option (either appear/disappear from dom,
or become visible/hidden). If at the moment of calling the method `selector` already satisfies the condition, the
method will return immediately. If the selector doesn't satisfy the condition for the `timeout` milliseconds, the
function will throw.

**Usage**

```py
await page.set_content("<div><span></span></div>")
div = await page.query_selector("div")
# waiting for the "span" selector relative to the div.
span = await div.wait_for_selector("span", state="attached")
```

**NOTE** This method does not work across navigations, use `page.wait_for_selector()` instead.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to query for. |
| `state` | Union["attached", "detached", "hidden", "visible", None] | Defaults to `'visible'`. Can be either: - `'attached'` - wait for element to be present in DOM. - `'detached'` - wait for element to not be present in DOM. - `'visible'` - wait for element to have non-empty bounding box and no `visibility:hidden`. Note that element without any content or with `display:none` has an empty bounding box and is not considered visible. - `'hidden'` - wait for element to be either detached from DOM, or have an empty bounding box or `visibility:hidden`. This is opposite to the `'visible'` option. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
Union[ElementHandle, None]
