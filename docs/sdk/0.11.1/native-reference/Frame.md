# 原生 Frame

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [add_script_tag](#add_script_tag)
- [add_style_tag](#add_style_tag)
- [check](#check)
- [child_frames](#child_frames)
- [click](#click)
- [content](#content)
- [dblclick](#dblclick)
- [dispatch_event](#dispatch_event)
- [drag_and_drop](#drag_and_drop)
- [eval_on_selector](#eval_on_selector)
- [eval_on_selector_all](#eval_on_selector_all)
- [evaluate](#evaluate)
- [evaluate_handle](#evaluate_handle)
- [expect_navigation](#expect_navigation)
- [fill](#fill)
- [focus](#focus)
- [frame_element](#frame_element)
- [frame_locator](#frame_locator)
- [get_attribute](#get_attribute)
- [get_by_alt_text](#get_by_alt_text)
- [get_by_label](#get_by_label)
- [get_by_placeholder](#get_by_placeholder)
- [get_by_role](#get_by_role)
- [get_by_test_id](#get_by_test_id)
- [get_by_text](#get_by_text)
- [get_by_title](#get_by_title)
- [goto](#goto)
- [hover](#hover)
- [inner_html](#inner_html)
- [inner_text](#inner_text)
- [input_value](#input_value)
- [is_checked](#is_checked)
- [is_detached](#is_detached)
- [is_disabled](#is_disabled)
- [is_editable](#is_editable)
- [is_enabled](#is_enabled)
- [is_hidden](#is_hidden)
- [is_visible](#is_visible)
- [locator](#locator)
- [name](#name)
- [on](#on)
- [once](#once)
- [page](#page)
- [parent_frame](#parent_frame)
- [press](#press)
- [query_selector](#query_selector)
- [query_selector_all](#query_selector_all)
- [remove_listener](#remove_listener)
- [select_option](#select_option)
- [set_checked](#set_checked)
- [set_content](#set_content)
- [set_input_files](#set_input_files)
- [tap](#tap)
- [text_content](#text_content)
- [title](#title)
- [type](#type)
- [uncheck](#uncheck)
- [url](#url)
- [wait_for_function](#wait_for_function)
- [wait_for_load_state](#wait_for_load_state)
- [wait_for_selector](#wait_for_selector)
- [wait_for_timeout](#wait_for_timeout)
- [wait_for_url](#wait_for_url)
- [webmcp](#webmcp)

## add_script_tag

### 同步

```python signature
def add_script_tag(self, *, content: Optional[str] = None, path: Union[pathlib.Path, str, NoneType] = None, type: Optional[str] = None, url: Optional[str] = None) -> 'ElementHandle'
```

Frame.add_script_tag

Returns the added tag when the script's onload fires or when the script content was injected into frame.

Adds a `<script>` tag into the page with the desired url or content.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `content` | Union[str, None] | Raw JavaScript content to be injected into frame. |
| `path` | Union[pathlib.Path, str, None] | Path to the JavaScript file to be injected into frame. If `path` is a relative path, then it is resolved relative to the current working directory. |
| `type` | Union[str, None] | Script type. Use 'module' in order to load a JavaScript ES6 module. See [script](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script) for more details. |
| `url` | Union[str, None] | URL of a script to be added. |

#### Returns
ElementHandle

### 异步

```python signature
async def add_script_tag(self, *, content: Optional[str] = None, path: Union[pathlib.Path, str, NoneType] = None, type: Optional[str] = None, url: Optional[str] = None) -> 'ElementHandle'
```

Frame.add_script_tag

Returns the added tag when the script's onload fires or when the script content was injected into frame.

Adds a `<script>` tag into the page with the desired url or content.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `content` | Union[str, None] | Raw JavaScript content to be injected into frame. |
| `path` | Union[pathlib.Path, str, None] | Path to the JavaScript file to be injected into frame. If `path` is a relative path, then it is resolved relative to the current working directory. |
| `type` | Union[str, None] | Script type. Use 'module' in order to load a JavaScript ES6 module. See [script](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/script) for more details. |
| `url` | Union[str, None] | URL of a script to be added. |

#### Returns
ElementHandle


## add_style_tag

### 同步

```python signature
def add_style_tag(self, *, content: Optional[str] = None, path: Union[pathlib.Path, str, NoneType] = None, url: Optional[str] = None) -> 'ElementHandle'
```

Frame.add_style_tag

Returns the added tag when the stylesheet's onload fires or when the CSS content was injected into frame.

Adds a `<link rel="stylesheet">` tag into the page with the desired url or a `<style type="text/css">` tag with the
content.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `content` | Union[str, None] | Raw CSS content to be injected into frame. |
| `path` | Union[pathlib.Path, str, None] | Path to the CSS file to be injected into frame. If `path` is a relative path, then it is resolved relative to the current working directory. |
| `url` | Union[str, None] | URL of the `<link>` tag. |

#### Returns
ElementHandle

### 异步

```python signature
async def add_style_tag(self, *, content: Optional[str] = None, path: Union[pathlib.Path, str, NoneType] = None, url: Optional[str] = None) -> 'ElementHandle'
```

Frame.add_style_tag

Returns the added tag when the stylesheet's onload fires or when the CSS content was injected into frame.

Adds a `<link rel="stylesheet">` tag into the page with the desired url or a `<style type="text/css">` tag with the
content.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `content` | Union[str, None] | Raw CSS content to be injected into frame. |
| `path` | Union[pathlib.Path, str, None] | Path to the CSS file to be injected into frame. If `path` is a relative path, then it is resolved relative to the current working directory. |
| `url` | Union[str, None] | URL of the `<link>` tag. |

#### Returns
ElementHandle


## check

### 同步

```python signature
def check(self, selector: str, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

Frame.check

This method checks an element matching `selector` by performing the following steps:
1. Find an element matching `selector`. If there is none, wait until a matching element is attached to the DOM.
1. Ensure that matched element is a checkbox or a radio input. If not, this method throws. If the element is
   already checked, this method returns immediately.
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the matched element, unless `force` option is set. If
   the element is detached during the checks, the whole action is retried.
1. Scroll the element into view if needed.
1. Use `page.mouse` to click in the center of the element.
1. Ensure that the element is now checked. If not, this method throws.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `position` | Union[{x: float, y: float}, None] | A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. |

### 异步

```python signature
async def check(self, selector: str, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

Frame.check

This method checks an element matching `selector` by performing the following steps:
1. Find an element matching `selector`. If there is none, wait until a matching element is attached to the DOM.
1. Ensure that matched element is a checkbox or a radio input. If not, this method throws. If the element is
   already checked, this method returns immediately.
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the matched element, unless `force` option is set. If
   the element is detached during the checks, the whole action is retried.
1. Scroll the element into view if needed.
1. Use `page.mouse` to click in the center of the element.
1. Ensure that the element is now checked. If not, this method throws.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `position` | Union[{x: float, y: float}, None] | A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. |

## child_frames

属性，直接读取；异步入口也不加 await。

```python signature
Frame.child_frames: typing.List[ForwardRef('Frame')]
```

Frame.child_frames

#### Returns
List[Frame]


## click

### 同步

```python signature
def click(self, selector: str, *, button: Optional[Literal['left', 'middle', 'right']] = None, click_count: Optional[int] = None, delay: Optional[float] = None, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

Frame.click

This method clicks an element matching `selector` by performing the following steps:
1. Find an element matching `selector`. If there is none, wait until a matching element is attached to the DOM.
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the matched element, unless `force` option is set. If
   the element is detached during the checks, the whole action is retried.
1. Scroll the element into view if needed.
1. Use `page.mouse` to click in the center of the element, or the specified `position`.
1. Wait for initiated navigations to either succeed or fail, unless `no_wait_after` option is set.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `button` | Union["left", "middle", "right", None] | Defaults to `left`. |
| `click_count` | Union[int, None] | defaults to 1. See [UIEvent.detail]. |
| `delay` | Union[float, None] | Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0. |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `modifiers` | Union[Sequence[Union["Alt", "Control", "ControlOrMeta", "Meta", "Shift"]], None] | Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current modifiers back. If not specified, currently pressed modifiers are used. "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS. |
| `no_wait_after` | Union[bool, None] | Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to inaccessible pages. Defaults to `false`. Deprecated: This option will default to `true` in the future. |
| `position` | Union[{x: float, y: float}, None] | A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. Note that keyboard `modifiers` will be pressed regardless of `trial` to allow testing elements which are only visible when those keys are pressed. |

### 异步

```python signature
async def click(self, selector: str, *, button: Optional[Literal['left', 'middle', 'right']] = None, click_count: Optional[int] = None, delay: Optional[float] = None, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

Frame.click

This method clicks an element matching `selector` by performing the following steps:
1. Find an element matching `selector`. If there is none, wait until a matching element is attached to the DOM.
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the matched element, unless `force` option is set. If
   the element is detached during the checks, the whole action is retried.
1. Scroll the element into view if needed.
1. Use `page.mouse` to click in the center of the element, or the specified `position`.
1. Wait for initiated navigations to either succeed or fail, unless `no_wait_after` option is set.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `button` | Union["left", "middle", "right", None] | Defaults to `left`. |
| `click_count` | Union[int, None] | defaults to 1. See [UIEvent.detail]. |
| `delay` | Union[float, None] | Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0. |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `modifiers` | Union[Sequence[Union["Alt", "Control", "ControlOrMeta", "Meta", "Shift"]], None] | Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current modifiers back. If not specified, currently pressed modifiers are used. "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS. |
| `no_wait_after` | Union[bool, None] | Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to inaccessible pages. Defaults to `false`. Deprecated: This option will default to `true` in the future. |
| `position` | Union[{x: float, y: float}, None] | A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. Note that keyboard `modifiers` will be pressed regardless of `trial` to allow testing elements which are only visible when those keys are pressed. |

## content

### 同步

```python signature
def content(self, *, include_shadow: Optional[bool] = None) -> str
```

Frame.content

Gets the full HTML contents of the frame, including the doctype.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `include_shadow` | Union[bool, None] | When true, contents of open shadow roots are included as [declarative shadow DOM](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_shadow_DOM#declaratively_with_html), i.e. `<template shadowrootmode="open">` elements nested inside their host elements. Closed shadow roots are never included. Defaults to `false`. |

#### Returns
str

### 异步

```python signature
async def content(self, *, include_shadow: Optional[bool] = None) -> str
```

Frame.content

Gets the full HTML contents of the frame, including the doctype.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `include_shadow` | Union[bool, None] | When true, contents of open shadow roots are included as [declarative shadow DOM](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_shadow_DOM#declaratively_with_html), i.e. `<template shadowrootmode="open">` elements nested inside their host elements. Closed shadow roots are never included. Defaults to `false`. |

#### Returns
str


## dblclick

### 同步

```python signature
def dblclick(self, selector: str, *, button: Optional[Literal['left', 'middle', 'right']] = None, delay: Optional[float] = None, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

Frame.dblclick

This method double clicks an element matching `selector` by performing the following steps:
1. Find an element matching `selector`. If there is none, wait until a matching element is attached to the DOM.
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the matched element, unless `force` option is set. If
   the element is detached during the checks, the whole action is retried.
1. Scroll the element into view if needed.
1. Use `page.mouse` to double click in the center of the element, or the specified `position`. if the first
   click of the `dblclick()` triggers a navigation event, this method will throw.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

**NOTE** `frame.dblclick()` dispatches two `click` events and a single `dblclick` event.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `button` | Union["left", "middle", "right", None] | Defaults to `left`. |
| `delay` | Union[float, None] | Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0. |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `modifiers` | Union[Sequence[Union["Alt", "Control", "ControlOrMeta", "Meta", "Shift"]], None] | Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current modifiers back. If not specified, currently pressed modifiers are used. "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `position` | Union[{x: float, y: float}, None] | A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. Note that keyboard `modifiers` will be pressed regardless of `trial` to allow testing elements which are only visible when those keys are pressed. |

### 异步

```python signature
async def dblclick(self, selector: str, *, button: Optional[Literal['left', 'middle', 'right']] = None, delay: Optional[float] = None, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

Frame.dblclick

This method double clicks an element matching `selector` by performing the following steps:
1. Find an element matching `selector`. If there is none, wait until a matching element is attached to the DOM.
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the matched element, unless `force` option is set. If
   the element is detached during the checks, the whole action is retried.
1. Scroll the element into view if needed.
1. Use `page.mouse` to double click in the center of the element, or the specified `position`. if the first
   click of the `dblclick()` triggers a navigation event, this method will throw.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

**NOTE** `frame.dblclick()` dispatches two `click` events and a single `dblclick` event.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `button` | Union["left", "middle", "right", None] | Defaults to `left`. |
| `delay` | Union[float, None] | Time to wait between `mousedown` and `mouseup` in milliseconds. Defaults to 0. |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `modifiers` | Union[Sequence[Union["Alt", "Control", "ControlOrMeta", "Meta", "Shift"]], None] | Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current modifiers back. If not specified, currently pressed modifiers are used. "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `position` | Union[{x: float, y: float}, None] | A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. Note that keyboard `modifiers` will be pressed regardless of `trial` to allow testing elements which are only visible when those keys are pressed. |

## dispatch_event

### 同步

```python signature
def dispatch_event(self, selector: str, type: str, event_init: Optional[Dict] = None, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Frame.dispatch_event

The snippet below dispatches the `click` event on the element. Regardless of the visibility state of the element,
`click` is dispatched. This is equivalent to calling
[element.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click).

**Usage**

```py
frame.dispatch_event("button#submit", "click")
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
data_transfer = frame.evaluate_handle("new DataTransfer()")
frame.dispatch_event("#source", "dragstart", { "dataTransfer": data_transfer })
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `type` | str | DOM event type: `"click"`, `"dragstart"`, etc. |
| `event_init` | Union[Dict, None] | Optional event-specific initialization properties. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

### 异步

```python signature
async def dispatch_event(self, selector: str, type: str, event_init: Optional[Dict] = None, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Frame.dispatch_event

The snippet below dispatches the `click` event on the element. Regardless of the visibility state of the element,
`click` is dispatched. This is equivalent to calling
[element.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click).

**Usage**

```py
await frame.dispatch_event("button#submit", "click")
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
data_transfer = await frame.evaluate_handle("new DataTransfer()")
await frame.dispatch_event("#source", "dragstart", { "dataTransfer": data_transfer })
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `type` | str | DOM event type: `"click"`, `"dragstart"`, etc. |
| `event_init` | Union[Dict, None] | Optional event-specific initialization properties. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

## drag_and_drop

### 同步

```python signature
def drag_and_drop(self, source: str, target: str, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, scroll: Optional[Literal['auto', 'none']] = None, source_position: Optional[patchright._impl._api_structures.Position] = None, steps: Optional[int] = None, strict: Optional[bool] = None, target_position: Optional[patchright._impl._api_structures.Position] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

Frame.drag_and_drop

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `source` | str | A selector to search for an element to drag. If there are multiple elements satisfying the selector, the first will be used. |
| `target` | str | A selector to search for an element to drop onto. If there are multiple elements satisfying the selector, the first will be used. |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `source_position` | Union[{x: float, y: float}, None] | Clicks on the source element at this point relative to the top-left corner of the element's padding box. If not specified, some visible point of the element is used. |
| `steps` | Union[int, None] | Defaults to 1. Sends `n` interpolated `mousemove` events to represent travel between the `mousedown` and `mouseup` of the drag. When set to 1, emits a single `mousemove` event at the destination location. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `target_position` | Union[{x: float, y: float}, None] | Drops on the target element at this point relative to the top-left corner of the element's padding box. If not specified, some visible point of the element is used. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. |

### 异步

```python signature
async def drag_and_drop(self, source: str, target: str, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, scroll: Optional[Literal['auto', 'none']] = None, source_position: Optional[patchright._impl._api_structures.Position] = None, steps: Optional[int] = None, strict: Optional[bool] = None, target_position: Optional[patchright._impl._api_structures.Position] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

Frame.drag_and_drop

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `source` | str | A selector to search for an element to drag. If there are multiple elements satisfying the selector, the first will be used. |
| `target` | str | A selector to search for an element to drop onto. If there are multiple elements satisfying the selector, the first will be used. |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `source_position` | Union[{x: float, y: float}, None] | Clicks on the source element at this point relative to the top-left corner of the element's padding box. If not specified, some visible point of the element is used. |
| `steps` | Union[int, None] | Defaults to 1. Sends `n` interpolated `mousemove` events to represent travel between the `mousedown` and `mouseup` of the drag. When set to 1, emits a single `mousemove` event at the destination location. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `target_position` | Union[{x: float, y: float}, None] | Drops on the target element at this point relative to the top-left corner of the element's padding box. If not specified, some visible point of the element is used. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. |

## eval_on_selector

### 同步

```python signature
def eval_on_selector(self, selector: str, expression: str, arg: Optional[Any] = None, *, strict: Optional[bool] = None) -> Any
```

Frame.eval_on_selector

Returns the return value of `expression`.

The method finds an element matching the specified selector within the frame and passes it as a first argument to
`expression`. If no elements match the selector, the method throws an error.

If `expression` returns a [Promise], then `frame.eval_on_selector()` would wait for the promise to resolve and
return its value.

**Usage**

```py
search_value = frame.eval_on_selector("#search", "el => el.value")
preload_href = frame.eval_on_selector("link[rel=preload]", "el => el.href")
html = frame.eval_on_selector(".main-container", "(e, suffix) => e.outerHTML + suffix", "hello")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to query for. |
| `expression` | str | JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked. |
| `arg` | Union[Any, None] | Optional argument to pass to `expression`. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |

#### Returns
Any

### 异步

```python signature
async def eval_on_selector(self, selector: str, expression: str, arg: Optional[Any] = None, *, strict: Optional[bool] = None) -> Any
```

Frame.eval_on_selector

Returns the return value of `expression`.

The method finds an element matching the specified selector within the frame and passes it as a first argument to
`expression`. If no elements match the selector, the method throws an error.

If `expression` returns a [Promise], then `frame.eval_on_selector()` would wait for the promise to resolve and
return its value.

**Usage**

```py
search_value = await frame.eval_on_selector("#search", "el => el.value")
preload_href = await frame.eval_on_selector("link[rel=preload]", "el => el.href")
html = await frame.eval_on_selector(".main-container", "(e, suffix) => e.outerHTML + suffix", "hello")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to query for. |
| `expression` | str | JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked. |
| `arg` | Union[Any, None] | Optional argument to pass to `expression`. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |

#### Returns
Any


## eval_on_selector_all

### 同步

```python
def eval_on_selector_all(self, selector: str, expression: str, arg: Optional[Any] = None) -> Any
```

Frame.eval_on_selector_all

Returns the return value of `expression`.

The method finds all elements matching the specified selector within the frame and passes an array of matched
elements as a first argument to `expression`.

If `expression` returns a [Promise], then `frame.eval_on_selector_all()` would wait for the promise to resolve and
return its value.

**Usage**

```py
divs_counts = frame.eval_on_selector_all("div", "(divs, min) => divs.length >= min", 10)
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

Frame.eval_on_selector_all

Returns the return value of `expression`.

The method finds all elements matching the specified selector within the frame and passes an array of matched
elements as a first argument to `expression`.

If `expression` returns a [Promise], then `frame.eval_on_selector_all()` would wait for the promise to resolve and
return its value.

**Usage**

```py
divs_counts = await frame.eval_on_selector_all("div", "(divs, min) => divs.length >= min", 10)
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

Frame.evaluate

Returns the return value of `expression`.

If the function passed to the `frame.evaluate()` returns a [Promise], then `frame.evaluate()` would wait for the
promise to resolve and return its value.

If the function passed to the `frame.evaluate()` returns a non-[Serializable] value, then `frame.evaluate()`
returns `undefined`. Playwright also supports transferring some additional values that are not serializable by
`JSON`: `-0`, `NaN`, `Infinity`, `-Infinity`.

**Usage**

```py
result = frame.evaluate("([x, y]) => Promise.resolve(x * y)", [7, 8])
print(result) # prints "56"
```

A string can also be passed in instead of a function.

```py
print(frame.evaluate("1 + 2")) # prints "3"
x = 10
print(frame.evaluate(f"1 + {x}")) # prints "11"
```

`ElementHandle` instances can be passed as an argument to the `frame.evaluate()`:

```py
body_handle = frame.evaluate_handle("document.body")
html = frame.evaluate("([body, suffix]) => body.innerHTML + suffix", [body_handle, "hello"])
body_handle.dispose()
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

Frame.evaluate

Returns the return value of `expression`.

If the function passed to the `frame.evaluate()` returns a [Promise], then `frame.evaluate()` would wait for the
promise to resolve and return its value.

If the function passed to the `frame.evaluate()` returns a non-[Serializable] value, then `frame.evaluate()`
returns `undefined`. Playwright also supports transferring some additional values that are not serializable by
`JSON`: `-0`, `NaN`, `Infinity`, `-Infinity`.

**Usage**

```py
result = await frame.evaluate("([x, y]) => Promise.resolve(x * y)", [7, 8])
print(result) # prints "56"
```

A string can also be passed in instead of a function.

```py
print(await frame.evaluate("1 + 2")) # prints "3"
x = 10
print(await frame.evaluate(f"1 + {x}")) # prints "11"
```

`ElementHandle` instances can be passed as an argument to the `frame.evaluate()`:

```py
body_handle = await frame.evaluate_handle("document.body")
html = await frame.evaluate("([body, suffix]) => body.innerHTML + suffix", [body_handle, "hello"])
await body_handle.dispose()
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

Frame.evaluate_handle

Returns the return value of `expression` as a `JSHandle`.

The only difference between `frame.evaluate()` and `frame.evaluate_handle()` is that `frame.evaluate_handle()`
returns `JSHandle`.

If the function, passed to the `frame.evaluate_handle()`, returns a [Promise], then `frame.evaluate_handle()` would
wait for the promise to resolve and return its value.

**Usage**

```py
a_window_handle = frame.evaluate_handle("Promise.resolve(window)")
a_window_handle # handle for the window object.
```

A string can also be passed in instead of a function.

```py
a_handle = frame.evaluate_handle("document") # handle for the "document"
```

`JSHandle` instances can be passed as an argument to the `frame.evaluate_handle()`:

```py
a_handle = frame.evaluate_handle("document.body")
result_handle = frame.evaluate_handle("body => body.innerHTML", a_handle)
print(result_handle.json_value())
result_handle.dispose()
```

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

Frame.evaluate_handle

Returns the return value of `expression` as a `JSHandle`.

The only difference between `frame.evaluate()` and `frame.evaluate_handle()` is that `frame.evaluate_handle()`
returns `JSHandle`.

If the function, passed to the `frame.evaluate_handle()`, returns a [Promise], then `frame.evaluate_handle()` would
wait for the promise to resolve and return its value.

**Usage**

```py
a_window_handle = await frame.evaluate_handle("Promise.resolve(window)")
a_window_handle # handle for the window object.
```

A string can also be passed in instead of a function.

```py
a_handle = await frame.evaluate_handle("document") # handle for the "document"
```

`JSHandle` instances can be passed as an argument to the `frame.evaluate_handle()`:

```py
a_handle = await frame.evaluate_handle("document.body")
result_handle = await frame.evaluate_handle("body => body.innerHTML", a_handle)
print(await result_handle.json_value())
await result_handle.dispose()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expression` | str | JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked. |
| `arg` | Union[Any, None] | Optional argument to pass to `expression`. |

#### Returns
JSHandle


## expect_navigation

### 同步

```python signature
def expect_navigation(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None, url: Union[str, Pattern[str], Callable[[str], bool], NoneType] = None, wait_until: Optional[Literal['commit', 'domcontentloaded', 'load', 'networkidle']] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Response')]
```

Frame.expect_navigation

Waits for the frame navigation and returns the main resource response. In case of multiple redirects, the
navigation will resolve with the response of the last redirect. In case of navigation to a different anchor or
navigation due to History API usage, the navigation will resolve with `null`.

**Usage**

This method waits for the frame to navigate to a new URL. It is useful for when you run code which will indirectly
cause the frame to navigate. Consider this example:

```py
with frame.expect_navigation():
    frame.click("a.delayed-navigation") # clicking the link will indirectly cause a navigation
# Resolves after navigation has finished
```

**NOTE** Usage of the [History API](https://developer.mozilla.org/en-US/docs/Web/API/History_API) to change the URL
is considered a navigation.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_navigation_timeout()`, `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or `page.set_default_timeout()` methods. |
| `url` | Union[Callable[[str], bool], Pattern[str], str, None] | A glob pattern, regex pattern, or predicate receiving [URL] to match while waiting for the navigation. Note that if the parameter is a string without wildcard characters, the method will wait for navigation to URL that is exactly equal to the string. |
| `wait_until` | Union["commit", "domcontentloaded", "load", "networkidle", None] | When to consider operation succeeded, defaults to `load`. Events can be either: - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired. - `'load'` - consider operation to be finished when the `load` event is fired. - `'networkidle'` - **DISCOURAGED** consider operation to be finished when there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead. - `'commit'` - consider operation to be finished when network response is received and the document started loading. |

#### Returns
EventContextManager[Response]

### 异步

```python signature
def expect_navigation(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None, url: Union[str, Pattern[str], Callable[[str], bool], NoneType] = None, wait_until: Optional[Literal['commit', 'domcontentloaded', 'load', 'networkidle']] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Response')]
```

Frame.expect_navigation

Waits for the frame navigation and returns the main resource response. In case of multiple redirects, the
navigation will resolve with the response of the last redirect. In case of navigation to a different anchor or
navigation due to History API usage, the navigation will resolve with `null`.

**Usage**

This method waits for the frame to navigate to a new URL. It is useful for when you run code which will indirectly
cause the frame to navigate. Consider this example:

```py
async with frame.expect_navigation():
    await frame.click("a.delayed-navigation") # clicking the link will indirectly cause a navigation
# Resolves after navigation has finished
```

**NOTE** Usage of the [History API](https://developer.mozilla.org/en-US/docs/Web/API/History_API) to change the URL
is considered a navigation.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_navigation_timeout()`, `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or `page.set_default_timeout()` methods. |
| `url` | Union[Callable[[str], bool], Pattern[str], str, None] | A glob pattern, regex pattern, or predicate receiving [URL] to match while waiting for the navigation. Note that if the parameter is a string without wildcard characters, the method will wait for navigation to URL that is exactly equal to the string. |
| `wait_until` | Union["commit", "domcontentloaded", "load", "networkidle", None] | When to consider operation succeeded, defaults to `load`. Events can be either: - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired. - `'load'` - consider operation to be finished when the `load` event is fired. - `'networkidle'` - **DISCOURAGED** consider operation to be finished when there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead. - `'commit'` - consider operation to be finished when network response is received and the document started loading. |

#### Returns
EventContextManager[Response]


## fill

### 同步

```python signature
def fill(self, selector: str, value: str, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Frame.fill

This method waits for an element matching `selector`, waits for [actionability](https://playwright.dev/python/docs/actionability) checks,
focuses the element, fills it and triggers an `input` event after filling. Note that you can pass an empty string
to clear the input field.

If the target element is not an `<input>`, `<textarea>` or `[contenteditable]` element, this method throws an
error. However, if the element is inside the `<label>` element that has an associated
[control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), the control will be filled
instead.

To send fine-grained keyboard events, use `locator.press_sequentially()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `value` | str | Value to fill for the `<input>`, `<textarea>` or `[contenteditable]` element. |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

### 异步

```python signature
async def fill(self, selector: str, value: str, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Frame.fill

This method waits for an element matching `selector`, waits for [actionability](https://playwright.dev/python/docs/actionability) checks,
focuses the element, fills it and triggers an `input` event after filling. Note that you can pass an empty string
to clear the input field.

If the target element is not an `<input>`, `<textarea>` or `[contenteditable]` element, this method throws an
error. However, if the element is inside the `<label>` element that has an associated
[control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), the control will be filled
instead.

To send fine-grained keyboard events, use `locator.press_sequentially()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `value` | str | Value to fill for the `<input>`, `<textarea>` or `[contenteditable]` element. |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

## focus

### 同步

```python signature
def focus(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Frame.focus

This method fetches an element with `selector` and focuses it. If there's no element matching `selector`, the
method waits until a matching element appears in the DOM.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

### 异步

```python signature
async def focus(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Frame.focus

This method fetches an element with `selector` and focuses it. If there's no element matching `selector`, the
method waits until a matching element appears in the DOM.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

## frame_element

### 同步

```python
def frame_element(self) -> 'ElementHandle'
```

Frame.frame_element

Returns the `frame` or `iframe` element handle which corresponds to this frame.

This is an inverse of `element_handle.content_frame()`. Note that returned handle actually belongs to the parent
frame.

This method throws an error if the frame has been detached before `frameElement()` returns.

**Usage**

```py
frame_element = frame.frame_element()
content_frame = frame_element.content_frame()
assert frame == content_frame
```

#### Returns
ElementHandle

### 异步

```python
async def frame_element(self) -> 'ElementHandle'
```

Frame.frame_element

Returns the `frame` or `iframe` element handle which corresponds to this frame.

This is an inverse of `element_handle.content_frame()`. Note that returned handle actually belongs to the parent
frame.

This method throws an error if the frame has been detached before `frameElement()` returns.

**Usage**

```py
frame_element = await frame.frame_element()
content_frame = await frame_element.content_frame()
assert frame == content_frame
```

#### Returns
ElementHandle


## frame_locator

### 同步

```python
def frame_locator(self, selector: Optional[str] = None) -> 'FrameLocator'
```

Frame.frame_locator

When working with iframes, you can create a frame locator that will enter the iframe and allow selecting elements
in that iframe.

When called without `selector`, the search starts in this frame or in any of the iframes inside it, so that you
don't need to locate each iframe first. Note that the rest of the locator is resolved inside a single frame, just
like any other locator. If it matches elements inside multiple frames, an error is thrown.

**Usage**

Following snippet locates element with text "Submit" in the iframe with id `my-frame`, like `<iframe
id="my-frame">`:

```py
locator = frame.frame_locator("#my-iframe").get_by_text("Submit")
locator.click()
```

Following snippet locates a button, either in the frame or in one of the iframes inside it:

```py
locator = frame.frame_locator().get_by_role("button")
locator.click()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | Union[str, None] | A selector that matches the frame element. When not specified, locator is matched in this frame or in any of the iframes inside it. |

#### Returns
FrameLocator

### 异步

```python
def frame_locator(self, selector: Optional[str] = None) -> 'FrameLocator'
```

Frame.frame_locator

When working with iframes, you can create a frame locator that will enter the iframe and allow selecting elements
in that iframe.

When called without `selector`, the search starts in this frame or in any of the iframes inside it, so that you
don't need to locate each iframe first. Note that the rest of the locator is resolved inside a single frame, just
like any other locator. If it matches elements inside multiple frames, an error is thrown.

**Usage**

Following snippet locates element with text "Submit" in the iframe with id `my-frame`, like `<iframe
id="my-frame">`:

```py
locator = frame.frame_locator("#my-iframe").get_by_text("Submit")
await locator.click()
```

Following snippet locates a button, either in the frame or in one of the iframes inside it:

```py
locator = frame.frame_locator().get_by_role("button")
await locator.click()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | Union[str, None] | A selector that matches the frame element. When not specified, locator is matched in this frame or in any of the iframes inside it. |

#### Returns
FrameLocator


## get_attribute

### 同步

```python signature
def get_attribute(self, selector: str, name: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Optional[str]
```

Frame.get_attribute

Returns element attribute value.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `name` | str | Attribute name to get the value for. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
Union[str, None]

### 异步

```python signature
async def get_attribute(self, selector: str, name: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Optional[str]
```

Frame.get_attribute

Returns element attribute value.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `name` | str | Attribute name to get the value for. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
Union[str, None]


## get_by_alt_text

### 同步

```python signature
def get_by_alt_text(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'
```

Frame.get_by_alt_text

Allows locating elements by their alt text.

**Usage**

For example, this method will find the image by alt text "Playwright logo":

```html
<img alt='Playwright logo'>
```

```py
page.get_by_alt_text("Playwright logo").click()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `text` | Union[Pattern[str], str] | Text to locate the element for. |
| `exact` | Union[bool, None] | Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace. |

#### Returns
Locator

### 异步

```python signature
def get_by_alt_text(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'
```

Frame.get_by_alt_text

Allows locating elements by their alt text.

**Usage**

For example, this method will find the image by alt text "Playwright logo":

```html
<img alt='Playwright logo'>
```

```py
await page.get_by_alt_text("Playwright logo").click()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `text` | Union[Pattern[str], str] | Text to locate the element for. |
| `exact` | Union[bool, None] | Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace. |

#### Returns
Locator


## get_by_label

### 同步

```python signature
def get_by_label(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'
```

Frame.get_by_label

Allows locating input elements by the text of the associated `<label>` or `aria-labelledby` element, or by the
`aria-label` attribute.

**Usage**

For example, this method will find inputs by label "Username" and "Password" in the following DOM:

```html
<input aria-label="Username">
<label for="password-input">Password:</label>
<input id="password-input">
```

```py
page.get_by_label("Username").fill("john")
page.get_by_label("Password").fill("secret")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `text` | Union[Pattern[str], str] | Text to locate the element for. |
| `exact` | Union[bool, None] | Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace. |

#### Returns
Locator

### 异步

```python signature
def get_by_label(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'
```

Frame.get_by_label

Allows locating input elements by the text of the associated `<label>` or `aria-labelledby` element, or by the
`aria-label` attribute.

**Usage**

For example, this method will find inputs by label "Username" and "Password" in the following DOM:

```html
<input aria-label="Username">
<label for="password-input">Password:</label>
<input id="password-input">
```

```py
await page.get_by_label("Username").fill("john")
await page.get_by_label("Password").fill("secret")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `text` | Union[Pattern[str], str] | Text to locate the element for. |
| `exact` | Union[bool, None] | Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace. |

#### Returns
Locator


## get_by_placeholder

### 同步

```python signature
def get_by_placeholder(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'
```

Frame.get_by_placeholder

Allows locating input elements by the placeholder text.

**Usage**

For example, consider the following DOM structure.

```html
<input type="email" placeholder="name@example.com" />
```

You can fill the input after locating it by the placeholder text:

```py
page.get_by_placeholder("name@example.com").fill("playwright@microsoft.com")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `text` | Union[Pattern[str], str] | Text to locate the element for. |
| `exact` | Union[bool, None] | Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace. |

#### Returns
Locator

### 异步

```python signature
def get_by_placeholder(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'
```

Frame.get_by_placeholder

Allows locating input elements by the placeholder text.

**Usage**

For example, consider the following DOM structure.

```html
<input type="email" placeholder="name@example.com" />
```

You can fill the input after locating it by the placeholder text:

```py
await page.get_by_placeholder("name@example.com").fill("playwright@microsoft.com")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `text` | Union[Pattern[str], str] | Text to locate the element for. |
| `exact` | Union[bool, None] | Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace. |

#### Returns
Locator


## get_by_role

### 同步

```python signature
def get_by_role(self, role: Literal['alert', 'alertdialog', 'application', 'article', 'banner', 'blockquote', 'button', 'caption', 'cell', 'checkbox', 'code', 'columnheader', 'combobox', 'complementary', 'contentinfo', 'definition', 'deletion', 'dialog', 'directory', 'document', 'emphasis', 'feed', 'figure', 'form', 'generic', 'grid', 'gridcell', 'group', 'heading', 'img', 'insertion', 'link', 'list', 'listbox', 'listitem', 'log', 'main', 'marquee', 'math', 'menu', 'menubar', 'menuitem', 'menuitemcheckbox', 'menuitemradio', 'meter', 'navigation', 'none', 'note', 'option', 'paragraph', 'presentation', 'progressbar', 'radio', 'radiogroup', 'region', 'row', 'rowgroup', 'rowheader', 'scrollbar', 'search', 'searchbox', 'separator', 'slider', 'spinbutton', 'status', 'strong', 'subscript', 'superscript', 'switch', 'tab', 'table', 'tablist', 'tabpanel', 'term', 'textbox', 'time', 'timer', 'toolbar', 'tooltip', 'tree', 'treegrid', 'treeitem'], *, checked: Optional[bool] = None, description: Union[str, Pattern[str], NoneType] = None, disabled: Optional[bool] = None, exact: Optional[bool] = None, expanded: Optional[bool] = None, include_hidden: Optional[bool] = None, level: Optional[int] = None, name: Union[str, Pattern[str], NoneType] = None, pressed: Optional[bool] = None, selected: Optional[bool] = None) -> 'Locator'
```

Frame.get_by_role

Allows locating elements by their [ARIA role](https://www.w3.org/TR/wai-aria-1.2/#roles),
[ARIA attributes](https://www.w3.org/TR/wai-aria-1.2/#aria-attributes) and
[accessible name](https://w3c.github.io/accname/#dfn-accessible-name).

**Usage**

Consider the following DOM structure.

```html
<h3>Sign up</h3>
<label>
  <input type="checkbox" /> Subscribe
</label>
<br/>
<button>Submit</button>
```

You can locate each element by its implicit role:

```py
expect(page.get_by_role("heading", name="Sign up")).to_be_visible()

page.get_by_role("checkbox", name="Subscribe").check()

page.get_by_role("button", name=re.compile("submit", re.IGNORECASE)).click()
```

**Details**

Role selector **does not replace** accessibility audits and conformance tests, but rather gives early feedback
about the ARIA guidelines.

Many html elements have an implicitly [defined role](https://w3c.github.io/html-aam/#html-element-role-mappings)
that is recognized by the role selector. You can find all the
[supported roles here](https://www.w3.org/TR/wai-aria-1.2/#role_definitions). ARIA guidelines **do not recommend**
duplicating implicit roles and attributes by setting `role` and/or `aria-*` attributes to default values.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `role` | Union["alert", "alertdialog", "application", "article", "banner", "blockquote", "button", "caption", "cell", "checkbox", "code", "columnheader", "combobox", "complementary", "contentinfo", "definition", "deletion", "dialog", "directory", "document", "emphasis", "feed", "figure", "form", "generic", "grid", "gridcell", "group", "heading", "img", "insertion", "link", "list", "listbox", "listitem", "log", "main", "marquee", "math", "menu", "menubar", "menuitem", "menuitemcheckbox", "menuitemradio", "meter", "navigation", "none", "note", "option", "paragraph", "presentation", "progressbar", "radio", "radiogroup", "region", "row", "rowgroup", "rowheader", "scrollbar", "search", "searchbox", "separator", "slider", "spinbutton", "status", "strong", "subscript", "superscript", "switch", "tab", "table", "tablist", "tabpanel", "term", "textbox", "time", "timer", "toolbar", "tooltip", "tree", "treegrid", "treeitem"] | Required aria role. |
| `checked` | Union[bool, None] | An attribute that is usually set by `aria-checked` or native `<input type=checkbox>` controls.  Learn more about [`aria-checked`](https://www.w3.org/TR/wai-aria-1.2/#aria-checked). |
| `description` | Union[Pattern[str], str, None] | Option to match the [accessible description](https://w3c.github.io/accname/#dfn-accessible-description). By default, matching is case-insensitive and searches for a substring, use `exact` to control this behavior.  Learn more about [accessible description](https://w3c.github.io/accname/#dfn-accessible-description). |
| `disabled` | Union[bool, None] | An attribute that is usually set by `aria-disabled` or `disabled`.  **NOTE** Unlike most other attributes, `disabled` is inherited through the DOM hierarchy. Learn more about [`aria-disabled`](https://www.w3.org/TR/wai-aria-1.2/#aria-disabled). |
| `exact` | Union[bool, None] | Whether `name` and `description` are matched exactly: case-sensitive and whole-string. Defaults to false. Ignored when the value is a regular expression. Note that exact match still trims whitespace. |
| `expanded` | Union[bool, None] | An attribute that is usually set by `aria-expanded`.  Learn more about [`aria-expanded`](https://www.w3.org/TR/wai-aria-1.2/#aria-expanded). |
| `include_hidden` | Union[bool, None] | Option that controls whether hidden elements are matched. By default, only non-hidden elements, as [defined by ARIA](https://www.w3.org/TR/wai-aria-1.2/#tree_exclusion), are matched by role selector.  Learn more about [`aria-hidden`](https://www.w3.org/TR/wai-aria-1.2/#aria-hidden). |
| `level` | Union[int, None] | A number attribute that is usually present for roles `heading`, `listitem`, `row`, `treeitem`, with default values for `<h1>-<h6>` elements.  Learn more about [`aria-level`](https://www.w3.org/TR/wai-aria-1.2/#aria-level). |
| `name` | Union[Pattern[str], str, None] | Option to match the [accessible name](https://w3c.github.io/accname/#dfn-accessible-name). By default, matching is case-insensitive and searches for a substring, use `exact` to control this behavior.  Learn more about [accessible name](https://w3c.github.io/accname/#dfn-accessible-name). |
| `pressed` | Union[bool, None] | An attribute that is usually set by `aria-pressed`.  Learn more about [`aria-pressed`](https://www.w3.org/TR/wai-aria-1.2/#aria-pressed). |
| `selected` | Union[bool, None] | An attribute that is usually set by `aria-selected`.  Learn more about [`aria-selected`](https://www.w3.org/TR/wai-aria-1.2/#aria-selected). |

#### Returns
Locator

### 异步

```python signature
def get_by_role(self, role: Literal['alert', 'alertdialog', 'application', 'article', 'banner', 'blockquote', 'button', 'caption', 'cell', 'checkbox', 'code', 'columnheader', 'combobox', 'complementary', 'contentinfo', 'definition', 'deletion', 'dialog', 'directory', 'document', 'emphasis', 'feed', 'figure', 'form', 'generic', 'grid', 'gridcell', 'group', 'heading', 'img', 'insertion', 'link', 'list', 'listbox', 'listitem', 'log', 'main', 'marquee', 'math', 'menu', 'menubar', 'menuitem', 'menuitemcheckbox', 'menuitemradio', 'meter', 'navigation', 'none', 'note', 'option', 'paragraph', 'presentation', 'progressbar', 'radio', 'radiogroup', 'region', 'row', 'rowgroup', 'rowheader', 'scrollbar', 'search', 'searchbox', 'separator', 'slider', 'spinbutton', 'status', 'strong', 'subscript', 'superscript', 'switch', 'tab', 'table', 'tablist', 'tabpanel', 'term', 'textbox', 'time', 'timer', 'toolbar', 'tooltip', 'tree', 'treegrid', 'treeitem'], *, checked: Optional[bool] = None, description: Union[str, Pattern[str], NoneType] = None, disabled: Optional[bool] = None, exact: Optional[bool] = None, expanded: Optional[bool] = None, include_hidden: Optional[bool] = None, level: Optional[int] = None, name: Union[str, Pattern[str], NoneType] = None, pressed: Optional[bool] = None, selected: Optional[bool] = None) -> 'Locator'
```

Frame.get_by_role

Allows locating elements by their [ARIA role](https://www.w3.org/TR/wai-aria-1.2/#roles),
[ARIA attributes](https://www.w3.org/TR/wai-aria-1.2/#aria-attributes) and
[accessible name](https://w3c.github.io/accname/#dfn-accessible-name).

**Usage**

Consider the following DOM structure.

```html
<h3>Sign up</h3>
<label>
  <input type="checkbox" /> Subscribe
</label>
<br/>
<button>Submit</button>
```

You can locate each element by its implicit role:

```py
await expect(page.get_by_role("heading", name="Sign up")).to_be_visible()

await page.get_by_role("checkbox", name="Subscribe").check()

await page.get_by_role("button", name=re.compile("submit", re.IGNORECASE)).click()
```

**Details**

Role selector **does not replace** accessibility audits and conformance tests, but rather gives early feedback
about the ARIA guidelines.

Many html elements have an implicitly [defined role](https://w3c.github.io/html-aam/#html-element-role-mappings)
that is recognized by the role selector. You can find all the
[supported roles here](https://www.w3.org/TR/wai-aria-1.2/#role_definitions). ARIA guidelines **do not recommend**
duplicating implicit roles and attributes by setting `role` and/or `aria-*` attributes to default values.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `role` | Union["alert", "alertdialog", "application", "article", "banner", "blockquote", "button", "caption", "cell", "checkbox", "code", "columnheader", "combobox", "complementary", "contentinfo", "definition", "deletion", "dialog", "directory", "document", "emphasis", "feed", "figure", "form", "generic", "grid", "gridcell", "group", "heading", "img", "insertion", "link", "list", "listbox", "listitem", "log", "main", "marquee", "math", "menu", "menubar", "menuitem", "menuitemcheckbox", "menuitemradio", "meter", "navigation", "none", "note", "option", "paragraph", "presentation", "progressbar", "radio", "radiogroup", "region", "row", "rowgroup", "rowheader", "scrollbar", "search", "searchbox", "separator", "slider", "spinbutton", "status", "strong", "subscript", "superscript", "switch", "tab", "table", "tablist", "tabpanel", "term", "textbox", "time", "timer", "toolbar", "tooltip", "tree", "treegrid", "treeitem"] | Required aria role. |
| `checked` | Union[bool, None] | An attribute that is usually set by `aria-checked` or native `<input type=checkbox>` controls.  Learn more about [`aria-checked`](https://www.w3.org/TR/wai-aria-1.2/#aria-checked). |
| `description` | Union[Pattern[str], str, None] | Option to match the [accessible description](https://w3c.github.io/accname/#dfn-accessible-description). By default, matching is case-insensitive and searches for a substring, use `exact` to control this behavior.  Learn more about [accessible description](https://w3c.github.io/accname/#dfn-accessible-description). |
| `disabled` | Union[bool, None] | An attribute that is usually set by `aria-disabled` or `disabled`.  **NOTE** Unlike most other attributes, `disabled` is inherited through the DOM hierarchy. Learn more about [`aria-disabled`](https://www.w3.org/TR/wai-aria-1.2/#aria-disabled). |
| `exact` | Union[bool, None] | Whether `name` and `description` are matched exactly: case-sensitive and whole-string. Defaults to false. Ignored when the value is a regular expression. Note that exact match still trims whitespace. |
| `expanded` | Union[bool, None] | An attribute that is usually set by `aria-expanded`.  Learn more about [`aria-expanded`](https://www.w3.org/TR/wai-aria-1.2/#aria-expanded). |
| `include_hidden` | Union[bool, None] | Option that controls whether hidden elements are matched. By default, only non-hidden elements, as [defined by ARIA](https://www.w3.org/TR/wai-aria-1.2/#tree_exclusion), are matched by role selector.  Learn more about [`aria-hidden`](https://www.w3.org/TR/wai-aria-1.2/#aria-hidden). |
| `level` | Union[int, None] | A number attribute that is usually present for roles `heading`, `listitem`, `row`, `treeitem`, with default values for `<h1>-<h6>` elements.  Learn more about [`aria-level`](https://www.w3.org/TR/wai-aria-1.2/#aria-level). |
| `name` | Union[Pattern[str], str, None] | Option to match the [accessible name](https://w3c.github.io/accname/#dfn-accessible-name). By default, matching is case-insensitive and searches for a substring, use `exact` to control this behavior.  Learn more about [accessible name](https://w3c.github.io/accname/#dfn-accessible-name). |
| `pressed` | Union[bool, None] | An attribute that is usually set by `aria-pressed`.  Learn more about [`aria-pressed`](https://www.w3.org/TR/wai-aria-1.2/#aria-pressed). |
| `selected` | Union[bool, None] | An attribute that is usually set by `aria-selected`.  Learn more about [`aria-selected`](https://www.w3.org/TR/wai-aria-1.2/#aria-selected). |

#### Returns
Locator


## get_by_test_id

### 同步

```python
def get_by_test_id(self, test_id: Union[str, Pattern[str]]) -> 'Locator'
```

Frame.get_by_test_id

Locate element by the test id.

**Usage**

Consider the following DOM structure.

```html
<button data-testid="directions">Itinéraire</button>
```

You can locate the element by its test id:

```py
page.get_by_test_id("directions").click()
```

**Details**

By default, the `data-testid` attribute is used as a test id. Use `selectors.set_test_id_attribute()` to configure
a different test id attribute if necessary.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `test_id` | Union[Pattern[str], str] | Id to locate the element by. |

#### Returns
Locator

### 异步

```python
def get_by_test_id(self, test_id: Union[str, Pattern[str]]) -> 'Locator'
```

Frame.get_by_test_id

Locate element by the test id.

**Usage**

Consider the following DOM structure.

```html
<button data-testid="directions">Itinéraire</button>
```

You can locate the element by its test id:

```py
await page.get_by_test_id("directions").click()
```

**Details**

By default, the `data-testid` attribute is used as a test id. Use `selectors.set_test_id_attribute()` to configure
a different test id attribute if necessary.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `test_id` | Union[Pattern[str], str] | Id to locate the element by. |

#### Returns
Locator


## get_by_text

### 同步

```python signature
def get_by_text(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'
```

Frame.get_by_text

Allows locating elements that contain given text.

See also `locator.filter()` that allows to match by another criteria, like an accessible role, and then filter by
the text content.

**Usage**

Consider the following DOM structure:

```html
<div>Hello <span>world</span></div>
<div>Hello</div>
```

You can locate by text substring, exact string, or a regular expression:

```py
# Matches <span>
page.get_by_text("world")

# Matches first <div>
page.get_by_text("Hello world")

# Matches second <div>
page.get_by_text("Hello", exact=True)

# Matches both <div>s
page.get_by_text(re.compile("Hello"))

# Matches second <div>
page.get_by_text(re.compile("^hello$", re.IGNORECASE))
```

**Details**

Matching by text always normalizes whitespace, even with exact match. For example, it turns multiple spaces into
one, turns line breaks into spaces and ignores leading and trailing whitespace.

Input elements of the type `button` and `submit` are matched by their `value` instead of the text content. For
example, locating by text `"Log in"` matches `<input type=button value="Log in">`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `text` | Union[Pattern[str], str] | Text to locate the element for. |
| `exact` | Union[bool, None] | Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace. |

#### Returns
Locator

### 异步

```python signature
def get_by_text(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'
```

Frame.get_by_text

Allows locating elements that contain given text.

See also `locator.filter()` that allows to match by another criteria, like an accessible role, and then filter by
the text content.

**Usage**

Consider the following DOM structure:

```html
<div>Hello <span>world</span></div>
<div>Hello</div>
```

You can locate by text substring, exact string, or a regular expression:

```py
# Matches <span>
page.get_by_text("world")

# Matches first <div>
page.get_by_text("Hello world")

# Matches second <div>
page.get_by_text("Hello", exact=True)

# Matches both <div>s
page.get_by_text(re.compile("Hello"))

# Matches second <div>
page.get_by_text(re.compile("^hello$", re.IGNORECASE))
```

**Details**

Matching by text always normalizes whitespace, even with exact match. For example, it turns multiple spaces into
one, turns line breaks into spaces and ignores leading and trailing whitespace.

Input elements of the type `button` and `submit` are matched by their `value` instead of the text content. For
example, locating by text `"Log in"` matches `<input type=button value="Log in">`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `text` | Union[Pattern[str], str] | Text to locate the element for. |
| `exact` | Union[bool, None] | Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace. |

#### Returns
Locator


## get_by_title

### 同步

```python signature
def get_by_title(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'
```

Frame.get_by_title

Allows locating elements by their title attribute.

**Usage**

Consider the following DOM structure.

```html
<span title='Issues count'>25 issues</span>
```

You can check the issues count after locating it by the title text:

```py
expect(page.get_by_title("Issues count")).to_have_text("25 issues")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `text` | Union[Pattern[str], str] | Text to locate the element for. |
| `exact` | Union[bool, None] | Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace. |

#### Returns
Locator

### 异步

```python signature
def get_by_title(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'
```

Frame.get_by_title

Allows locating elements by their title attribute.

**Usage**

Consider the following DOM structure.

```html
<span title='Issues count'>25 issues</span>
```

You can check the issues count after locating it by the title text:

```py
await expect(page.get_by_title("Issues count")).to_have_text("25 issues")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `text` | Union[Pattern[str], str] | Text to locate the element for. |
| `exact` | Union[bool, None] | Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace. |

#### Returns
Locator


## goto

### 同步

```python signature
def goto(self, url: str, *, referer: Optional[str] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, wait_until: Optional[Literal['commit', 'domcontentloaded', 'load', 'networkidle']] = None) -> Optional[ForwardRef('Response')]
```

Frame.goto

Returns the main resource response. In case of multiple redirects, the navigation will resolve with the response of
the last redirect.

The method will throw an error if:
- there's an SSL error (e.g. in case of self-signed certificates).
- target URL is invalid.
- the `timeout` is exceeded during navigation.
- the remote server does not respond or is unreachable.
- the main resource failed to load.

The method will not throw an error when any valid HTTP status code is returned by the remote server, including 404
"Not Found" and 500 "Internal Server Error".  The status code for such responses can be retrieved by calling
`response.status`.

**NOTE** The method either throws an error or returns a main resource response. The only exceptions are navigation
to `about:blank` or navigation to the same URL with a different hash, which would succeed and return `null`.

**NOTE** Headless mode doesn't support navigation to a PDF document. See the
[upstream issue](https://bugs.chromium.org/p/chromium/issues/detail?id=761295).

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url` | str | URL to navigate frame to. The url should include scheme, e.g. `https://`. |
| `referer` | Union[str, None] | Referer header value. If provided it will take preference over the referer header value set by `page.set_extra_http_headers()`. |
| `timeout` | Union[float, None] | Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_navigation_timeout()`, `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or `page.set_default_timeout()` methods. |
| `wait_until` | Union["commit", "domcontentloaded", "load", "networkidle", None] | When to consider operation succeeded, defaults to `load`. Events can be either: - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired. - `'load'` - consider operation to be finished when the `load` event is fired. - `'networkidle'` - **DISCOURAGED** consider operation to be finished when there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead. - `'commit'` - consider operation to be finished when network response is received and the document started loading. |

#### Returns
Union[Response, None]

### 异步

```python signature
async def goto(self, url: str, *, referer: Optional[str] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, wait_until: Optional[Literal['commit', 'domcontentloaded', 'load', 'networkidle']] = None) -> Optional[ForwardRef('Response')]
```

Frame.goto

Returns the main resource response. In case of multiple redirects, the navigation will resolve with the response of
the last redirect.

The method will throw an error if:
- there's an SSL error (e.g. in case of self-signed certificates).
- target URL is invalid.
- the `timeout` is exceeded during navigation.
- the remote server does not respond or is unreachable.
- the main resource failed to load.

The method will not throw an error when any valid HTTP status code is returned by the remote server, including 404
"Not Found" and 500 "Internal Server Error".  The status code for such responses can be retrieved by calling
`response.status`.

**NOTE** The method either throws an error or returns a main resource response. The only exceptions are navigation
to `about:blank` or navigation to the same URL with a different hash, which would succeed and return `null`.

**NOTE** Headless mode doesn't support navigation to a PDF document. See the
[upstream issue](https://bugs.chromium.org/p/chromium/issues/detail?id=761295).

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url` | str | URL to navigate frame to. The url should include scheme, e.g. `https://`. |
| `referer` | Union[str, None] | Referer header value. If provided it will take preference over the referer header value set by `page.set_extra_http_headers()`. |
| `timeout` | Union[float, None] | Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_navigation_timeout()`, `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or `page.set_default_timeout()` methods. |
| `wait_until` | Union["commit", "domcontentloaded", "load", "networkidle", None] | When to consider operation succeeded, defaults to `load`. Events can be either: - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired. - `'load'` - consider operation to be finished when the `load` event is fired. - `'networkidle'` - **DISCOURAGED** consider operation to be finished when there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead. - `'commit'` - consider operation to be finished when network response is received and the document started loading. |

#### Returns
Union[Response, None]


## hover

### 同步

```python signature
def hover(self, selector: str, *, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

Frame.hover

This method hovers over an element matching `selector` by performing the following steps:
1. Find an element matching `selector`. If there is none, wait until a matching element is attached to the DOM.
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the matched element, unless `force` option is set. If
   the element is detached during the checks, the whole action is retried.
1. Scroll the element into view if needed.
1. Use `page.mouse` to hover over the center of the element, or the specified `position`.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `modifiers` | Union[Sequence[Union["Alt", "Control", "ControlOrMeta", "Meta", "Shift"]], None] | Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current modifiers back. If not specified, currently pressed modifiers are used. "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `position` | Union[{x: float, y: float}, None] | A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. Note that keyboard `modifiers` will be pressed regardless of `trial` to allow testing elements which are only visible when those keys are pressed. |

### 异步

```python signature
async def hover(self, selector: str, *, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

Frame.hover

This method hovers over an element matching `selector` by performing the following steps:
1. Find an element matching `selector`. If there is none, wait until a matching element is attached to the DOM.
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the matched element, unless `force` option is set. If
   the element is detached during the checks, the whole action is retried.
1. Scroll the element into view if needed.
1. Use `page.mouse` to hover over the center of the element, or the specified `position`.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `modifiers` | Union[Sequence[Union["Alt", "Control", "ControlOrMeta", "Meta", "Shift"]], None] | Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current modifiers back. If not specified, currently pressed modifiers are used. "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `position` | Union[{x: float, y: float}, None] | A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. Note that keyboard `modifiers` will be pressed regardless of `trial` to allow testing elements which are only visible when those keys are pressed. |

## inner_html

### 同步

```python signature
def inner_html(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> str
```

Frame.inner_html

Returns `element.innerHTML`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
str

### 异步

```python signature
async def inner_html(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> str
```

Frame.inner_html

Returns `element.innerHTML`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
str


## inner_text

### 同步

```python signature
def inner_text(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> str
```

Frame.inner_text

Returns `element.innerText`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
str

### 异步

```python signature
async def inner_text(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> str
```

Frame.inner_text

Returns `element.innerText`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
str


## input_value

### 同步

```python signature
def input_value(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> str
```

Frame.input_value

Returns `input.value` for the selected `<input>` or `<textarea>` or `<select>` element.

Throws for non-input elements. However, if the element is inside the `<label>` element that has an associated
[control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), returns the value of the
control.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
str

### 异步

```python signature
async def input_value(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> str
```

Frame.input_value

Returns `input.value` for the selected `<input>` or `<textarea>` or `<select>` element.

Throws for non-input elements. However, if the element is inside the `<label>` element that has an associated
[control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), returns the value of the
control.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
str


## is_checked

### 同步

```python signature
def is_checked(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool
```

Frame.is_checked

Returns whether the element is checked. Throws if the element is not a checkbox or radio input.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
bool

### 异步

```python signature
async def is_checked(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool
```

Frame.is_checked

Returns whether the element is checked. Throws if the element is not a checkbox or radio input.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
bool


## is_detached

### 同步

```python
def is_detached(self) -> bool
```

Frame.is_detached

Returns `true` if the frame has been detached, or `false` otherwise.

#### Returns
bool

### 异步

```python
def is_detached(self) -> bool
```

Frame.is_detached

Returns `true` if the frame has been detached, or `false` otherwise.

#### Returns
bool


## is_disabled

### 同步

```python signature
def is_disabled(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool
```

Frame.is_disabled

Returns whether the element is disabled, the opposite of [enabled](https://playwright.dev/python/docs/actionability#enabled).

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
bool

### 异步

```python signature
async def is_disabled(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool
```

Frame.is_disabled

Returns whether the element is disabled, the opposite of [enabled](https://playwright.dev/python/docs/actionability#enabled).

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
bool


## is_editable

### 同步

```python signature
def is_editable(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool
```

Frame.is_editable

Returns whether the element is [editable](https://playwright.dev/python/docs/actionability#editable).

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
bool

### 异步

```python signature
async def is_editable(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool
```

Frame.is_editable

Returns whether the element is [editable](https://playwright.dev/python/docs/actionability#editable).

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
bool


## is_enabled

### 同步

```python signature
def is_enabled(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool
```

Frame.is_enabled

Returns whether the element is [enabled](https://playwright.dev/python/docs/actionability#enabled).

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
bool

### 异步

```python signature
async def is_enabled(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool
```

Frame.is_enabled

Returns whether the element is [enabled](https://playwright.dev/python/docs/actionability#enabled).

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
bool


## is_hidden

### 同步

```python signature
def is_hidden(self, selector: str, *, strict: Optional[bool] = None) -> bool
```

Frame.is_hidden

Returns whether the element is hidden, the opposite of [visible](https://playwright.dev/python/docs/actionability#visible).  `selector` that
does not match any elements is considered hidden.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |

#### Returns
bool

### 异步

```python signature
async def is_hidden(self, selector: str, *, strict: Optional[bool] = None) -> bool
```

Frame.is_hidden

Returns whether the element is hidden, the opposite of [visible](https://playwright.dev/python/docs/actionability#visible).  `selector` that
does not match any elements is considered hidden.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |

#### Returns
bool


## is_visible

### 同步

```python signature
def is_visible(self, selector: str, *, strict: Optional[bool] = None) -> bool
```

Frame.is_visible

Returns whether the element is [visible](https://playwright.dev/python/docs/actionability#visible). `selector` that does not match any elements
is considered not visible.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |

#### Returns
bool

### 异步

```python signature
async def is_visible(self, selector: str, *, strict: Optional[bool] = None) -> bool
```

Frame.is_visible

Returns whether the element is [visible](https://playwright.dev/python/docs/actionability#visible). `selector` that does not match any elements
is considered not visible.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |

#### Returns
bool


## locator

### 同步

```python signature
def locator(self, selector: str, *, has: Optional[ForwardRef('Locator')] = None, has_not: Optional[ForwardRef('Locator')] = None, has_not_text: Union[str, Pattern[str], NoneType] = None, has_text: Union[str, Pattern[str], NoneType] = None) -> 'Locator'
```

Frame.locator

The method returns an element locator that can be used to perform actions on this page / frame. Locator is resolved
to the element immediately before performing an action, so a series of actions on the same locator can in fact be
performed on different DOM elements. That would happen if the DOM structure between those actions has changed.

[Learn more about locators](https://playwright.dev/python/docs/locators).

[Learn more about locators](https://playwright.dev/python/docs/locators).

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to use when resolving DOM element. |
| `has` | Union[Locator, None] | Narrows down the results of the method to those which contain elements matching this relative locator. For example, `article` that has `text=Playwright` matches `<article><div>Playwright</div></article>`.  Inner locator **must be relative** to the outer locator and is queried starting with the outer locator match, not the document root. For example, you can find `content` that has `div` in `<article><content><div>Playwright</div></content></article>`. However, looking for `content` that has `article div` will fail, because the inner locator must be relative and should not use any elements outside the `content`.  Note that outer and inner locators must belong to the same frame. Inner locator must not contain `FrameLocator`s. |
| `has_not` | Union[Locator, None] | Matches elements that do not contain an element that matches an inner locator. Inner locator is queried against the outer one. For example, `article` that does not have `div` matches `<article><span>Playwright</span></article>`.  Note that outer and inner locators must belong to the same frame. Inner locator must not contain `FrameLocator`s. |
| `has_not_text` | Union[Pattern[str], str, None] | Matches elements that do not contain specified text somewhere inside, possibly in a child or a descendant element. When passed a [string], matching is case-insensitive and searches for a substring. |
| `has_text` | Union[Pattern[str], str, None] | Matches elements containing specified text somewhere inside, possibly in a child or a descendant element. When passed a [string], matching is case-insensitive and searches for a substring. For example, `"Playwright"` matches `<article><div>Playwright</div></article>`. |

#### Returns
Locator

### 异步

```python signature
def locator(self, selector: str, *, has: Optional[ForwardRef('Locator')] = None, has_not: Optional[ForwardRef('Locator')] = None, has_not_text: Union[str, Pattern[str], NoneType] = None, has_text: Union[str, Pattern[str], NoneType] = None) -> 'Locator'
```

Frame.locator

The method returns an element locator that can be used to perform actions on this page / frame. Locator is resolved
to the element immediately before performing an action, so a series of actions on the same locator can in fact be
performed on different DOM elements. That would happen if the DOM structure between those actions has changed.

[Learn more about locators](https://playwright.dev/python/docs/locators).

[Learn more about locators](https://playwright.dev/python/docs/locators).

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to use when resolving DOM element. |
| `has` | Union[Locator, None] | Narrows down the results of the method to those which contain elements matching this relative locator. For example, `article` that has `text=Playwright` matches `<article><div>Playwright</div></article>`.  Inner locator **must be relative** to the outer locator and is queried starting with the outer locator match, not the document root. For example, you can find `content` that has `div` in `<article><content><div>Playwright</div></content></article>`. However, looking for `content` that has `article div` will fail, because the inner locator must be relative and should not use any elements outside the `content`.  Note that outer and inner locators must belong to the same frame. Inner locator must not contain `FrameLocator`s. |
| `has_not` | Union[Locator, None] | Matches elements that do not contain an element that matches an inner locator. Inner locator is queried against the outer one. For example, `article` that does not have `div` matches `<article><span>Playwright</span></article>`.  Note that outer and inner locators must belong to the same frame. Inner locator must not contain `FrameLocator`s. |
| `has_not_text` | Union[Pattern[str], str, None] | Matches elements that do not contain specified text somewhere inside, possibly in a child or a descendant element. When passed a [string], matching is case-insensitive and searches for a substring. |
| `has_text` | Union[Pattern[str], str, None] | Matches elements containing specified text somewhere inside, possibly in a child or a descendant element. When passed a [string], matching is case-insensitive and searches for a substring. For example, `"Playwright"` matches `<article><div>Playwright</div></article>`. |

#### Returns
Locator


## name

属性，直接读取；异步入口也不加 await。

```python signature
Frame.name: <class 'str'>
```

Frame.name

Returns frame's name attribute as specified in the tag.

If the name is empty, returns the id attribute instead.

**NOTE** This value is calculated once when the frame is created, and will not update if the attribute is changed
later.

#### Returns
str


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


## page

属性，直接读取；异步入口也不加 await。

```python signature
Frame.page: Page
```

Frame.page

Returns the page containing this frame.

#### Returns
Page


## parent_frame

属性，直接读取；异步入口也不加 await。

```python signature
Frame.parent_frame: typing.Optional[ForwardRef('Frame')]
```

Frame.parent_frame

Parent frame, if any. Detached frames and main frames return `null`.

#### Returns
Union[Frame, None]


## press

### 同步

```python signature
def press(self, selector: str, key: str, *, delay: Optional[float] = None, no_wait_after: Optional[bool] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Frame.press

`key` can specify the intended
[keyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key) value or a single character
to generate the text for. A superset of the `key` values can be found
[here](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values). Examples of the keys are:

`F1` - `F12`, `Digit0`- `Digit9`, `KeyA`- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`,
`Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp`,
etc.

Following modification shortcuts are also supported: `Shift`, `Control`, `Alt`, `Meta`, `ShiftLeft`,
`ControlOrMeta`. `ControlOrMeta` resolves to `Control` on Windows and Linux and to `Meta` on macOS.

Holding down `Shift` will type the text that corresponds to the `key` in the upper case.

If `key` is a single character, it is case-sensitive, so the values `a` and `A` will generate different respective
texts.

Shortcuts such as `key: "Control+o"`, `key: "Control++` or `key: "Control+Shift+T"` are supported as well. When
specified with the modifier, modifier is pressed and being held while the subsequent key is being pressed.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `key` | str | Name of the key to press or a character to generate, such as `ArrowLeft` or `a`. |
| `delay` | Union[float, None] | Time to wait between `keydown` and `keyup` in milliseconds. Defaults to 0. |
| `no_wait_after` | Union[bool, None] | Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to inaccessible pages. Defaults to `false`. Deprecated: This option will default to `true` in the future. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

### 异步

```python signature
async def press(self, selector: str, key: str, *, delay: Optional[float] = None, no_wait_after: Optional[bool] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Frame.press

`key` can specify the intended
[keyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key) value or a single character
to generate the text for. A superset of the `key` values can be found
[here](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values). Examples of the keys are:

`F1` - `F12`, `Digit0`- `Digit9`, `KeyA`- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`,
`Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp`,
etc.

Following modification shortcuts are also supported: `Shift`, `Control`, `Alt`, `Meta`, `ShiftLeft`,
`ControlOrMeta`. `ControlOrMeta` resolves to `Control` on Windows and Linux and to `Meta` on macOS.

Holding down `Shift` will type the text that corresponds to the `key` in the upper case.

If `key` is a single character, it is case-sensitive, so the values `a` and `A` will generate different respective
texts.

Shortcuts such as `key: "Control+o"`, `key: "Control++` or `key: "Control+Shift+T"` are supported as well. When
specified with the modifier, modifier is pressed and being held while the subsequent key is being pressed.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `key` | str | Name of the key to press or a character to generate, such as `ArrowLeft` or `a`. |
| `delay` | Union[float, None] | Time to wait between `keydown` and `keyup` in milliseconds. Defaults to 0. |
| `no_wait_after` | Union[bool, None] | Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to inaccessible pages. Defaults to `false`. Deprecated: This option will default to `true` in the future. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

## query_selector

### 同步

```python signature
def query_selector(self, selector: str, *, strict: Optional[bool] = None) -> Optional[ForwardRef('ElementHandle')]
```

Frame.query_selector

Returns the ElementHandle pointing to the frame element.

**NOTE** The use of `ElementHandle` is discouraged, use `Locator` objects and web-first assertions instead.

The method finds an element matching the specified selector within the frame. If no elements match the selector,
returns `null`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to query for. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |

#### Returns
Union[ElementHandle, None]

### 异步

```python signature
async def query_selector(self, selector: str, *, strict: Optional[bool] = None) -> Optional[ForwardRef('ElementHandle')]
```

Frame.query_selector

Returns the ElementHandle pointing to the frame element.

**NOTE** The use of `ElementHandle` is discouraged, use `Locator` objects and web-first assertions instead.

The method finds an element matching the specified selector within the frame. If no elements match the selector,
returns `null`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to query for. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |

#### Returns
Union[ElementHandle, None]


## query_selector_all

### 同步

```python
def query_selector_all(self, selector: str) -> List[ForwardRef('ElementHandle')]
```

Frame.query_selector_all

Returns the ElementHandles pointing to the frame elements.

**NOTE** The use of `ElementHandle` is discouraged, use `Locator` objects instead.

The method finds all elements matching the specified selector within the frame. If no elements match the selector,
returns empty array.

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

Frame.query_selector_all

Returns the ElementHandles pointing to the frame elements.

**NOTE** The use of `ElementHandle` is discouraged, use `Locator` objects instead.

The method finds all elements matching the specified selector within the frame. If no elements match the selector,
returns empty array.

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


## select_option

### 同步

```python signature
def select_option(self, selector: str, value: Union[str, Sequence[str], NoneType] = None, *, element: Union[ForwardRef('ElementHandle'), Sequence[ForwardRef('ElementHandle')], NoneType] = None, force: Optional[bool] = None, index: Union[int, Sequence[int], NoneType] = None, label: Union[str, Sequence[str], NoneType] = None, no_wait_after: Optional[bool] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> List[str]
```

Frame.select_option

This method waits for an element matching `selector`, waits for [actionability](https://playwright.dev/python/docs/actionability) checks, waits
until all specified options are present in the `<select>` element and selects these options.

If the target element is not a `<select>` element, this method throws an error. However, if the element is inside
the `<label>` element that has an associated
[control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), the control will be used
instead.

Returns the array of option values that have been successfully selected.

Triggers a `change` and `input` event once all the provided options have been selected.

**Usage**

```py
# Single selection matching the value or label
frame.select_option("select#colors", "blue")
# single selection matching both the label
frame.select_option("select#colors", label="blue")
# multiple selection
frame.select_option("select#colors", value=["red", "green", "blue"])
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to query for. |
| `value` | Union[Sequence[str], str, None] | Options to select by value. If the `<select>` has the `multiple` attribute, all given options are selected, otherwise only the first option matching one of the passed options is selected. Optional. |
| `element` | Union[ElementHandle, Sequence[ElementHandle], None] | Option elements to select. Optional. |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `index` | Union[Sequence[int], int, None] | Options to select by index. Optional. |
| `label` | Union[Sequence[str], str, None] | Options to select by label. If the `<select>` has the `multiple` attribute, all given options are selected, otherwise only the first option matching one of the passed options is selected. Optional. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
List[str]

### 异步

```python signature
async def select_option(self, selector: str, value: Union[str, Sequence[str], NoneType] = None, *, element: Union[ForwardRef('ElementHandle'), Sequence[ForwardRef('ElementHandle')], NoneType] = None, force: Optional[bool] = None, index: Union[int, Sequence[int], NoneType] = None, label: Union[str, Sequence[str], NoneType] = None, no_wait_after: Optional[bool] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> List[str]
```

Frame.select_option

This method waits for an element matching `selector`, waits for [actionability](https://playwright.dev/python/docs/actionability) checks, waits
until all specified options are present in the `<select>` element and selects these options.

If the target element is not a `<select>` element, this method throws an error. However, if the element is inside
the `<label>` element that has an associated
[control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), the control will be used
instead.

Returns the array of option values that have been successfully selected.

Triggers a `change` and `input` event once all the provided options have been selected.

**Usage**

```py
# Single selection matching the value or label
await frame.select_option("select#colors", "blue")
# single selection matching the label
await frame.select_option("select#colors", label="blue")
# multiple selection
await frame.select_option("select#colors", value=["red", "green", "blue"])
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to query for. |
| `value` | Union[Sequence[str], str, None] | Options to select by value. If the `<select>` has the `multiple` attribute, all given options are selected, otherwise only the first option matching one of the passed options is selected. Optional. |
| `element` | Union[ElementHandle, Sequence[ElementHandle], None] | Option elements to select. Optional. |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `index` | Union[Sequence[int], int, None] | Options to select by index. Optional. |
| `label` | Union[Sequence[str], str, None] | Options to select by label. If the `<select>` has the `multiple` attribute, all given options are selected, otherwise only the first option matching one of the passed options is selected. Optional. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
List[str]


## set_checked

### 同步

```python signature
def set_checked(self, selector: str, checked: bool, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

Frame.set_checked

This method checks or unchecks an element matching `selector` by performing the following steps:
1. Find an element matching `selector`. If there is none, wait until a matching element is attached to the DOM.
1. Ensure that matched element is a checkbox or a radio input. If not, this method throws.
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
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `checked` | bool | Whether to check or uncheck the checkbox. |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `position` | Union[{x: float, y: float}, None] | A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. |

### 异步

```python signature
async def set_checked(self, selector: str, checked: bool, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

Frame.set_checked

This method checks or unchecks an element matching `selector` by performing the following steps:
1. Find an element matching `selector`. If there is none, wait until a matching element is attached to the DOM.
1. Ensure that matched element is a checkbox or a radio input. If not, this method throws.
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
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `checked` | bool | Whether to check or uncheck the checkbox. |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `position` | Union[{x: float, y: float}, None] | A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. |

## set_content

### 同步

```python signature
def set_content(self, html: str, *, timeout: Union[float, datetime.timedelta, NoneType] = None, wait_until: Optional[Literal['commit', 'domcontentloaded', 'load', 'networkidle']] = None) -> None
```

Frame.set_content

This method internally calls [document.write()](https://developer.mozilla.org/en-US/docs/Web/API/Document/write),
inheriting all its specific characteristics and behaviors.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `html` | str | HTML markup to assign to the page. |
| `timeout` | Union[float, None] | Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_navigation_timeout()`, `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or `page.set_default_timeout()` methods. |
| `wait_until` | Union["commit", "domcontentloaded", "load", "networkidle", None] | When to consider operation succeeded, defaults to `load`. Events can be either: - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired. - `'load'` - consider operation to be finished when the `load` event is fired. - `'networkidle'` - **DISCOURAGED** consider operation to be finished when there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead. - `'commit'` - consider operation to be finished when network response is received and the document started loading. |

### 异步

```python signature
async def set_content(self, html: str, *, timeout: Union[float, datetime.timedelta, NoneType] = None, wait_until: Optional[Literal['commit', 'domcontentloaded', 'load', 'networkidle']] = None) -> None
```

Frame.set_content

This method internally calls [document.write()](https://developer.mozilla.org/en-US/docs/Web/API/Document/write),
inheriting all its specific characteristics and behaviors.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `html` | str | HTML markup to assign to the page. |
| `timeout` | Union[float, None] | Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_navigation_timeout()`, `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or `page.set_default_timeout()` methods. |
| `wait_until` | Union["commit", "domcontentloaded", "load", "networkidle", None] | When to consider operation succeeded, defaults to `load`. Events can be either: - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired. - `'load'` - consider operation to be finished when the `load` event is fired. - `'networkidle'` - **DISCOURAGED** consider operation to be finished when there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead. - `'commit'` - consider operation to be finished when network response is received and the document started loading. |

## set_input_files

### 同步

```python signature
def set_input_files(self, selector: str, files: Union[str, pathlib.Path, Sequence[Union[str, pathlib.Path]], patchright._impl._api_structures.FilePayload, Sequence[patchright._impl._api_structures.FilePayload]], *, no_wait_after: Optional[bool] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Frame.set_input_files

Sets the value of the file input to these file paths or files. If some of the `filePaths` are relative paths, then
they are resolved relative to the current working directory. For empty array, clears the selected files.

This method expects `selector` to point to an
[input element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input). However, if the element is inside
the `<label>` element that has an associated
[control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), targets the control instead.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `files` | Union[Sequence[Union[pathlib.Path, str]], Sequence[{name: str, mimeType: str, buffer: bytes}], pathlib.Path, str, {name: str, mimeType: str, buffer: bytes}] |  |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

### 异步

```python signature
async def set_input_files(self, selector: str, files: Union[str, pathlib.Path, Sequence[Union[str, pathlib.Path]], patchright._impl._api_structures.FilePayload, Sequence[patchright._impl._api_structures.FilePayload]], *, no_wait_after: Optional[bool] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Frame.set_input_files

Sets the value of the file input to these file paths or files. If some of the `filePaths` are relative paths, then
they are resolved relative to the current working directory. For empty array, clears the selected files.

This method expects `selector` to point to an
[input element](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/input). However, if the element is inside
the `<label>` element that has an associated
[control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), targets the control instead.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `files` | Union[Sequence[Union[pathlib.Path, str]], Sequence[{name: str, mimeType: str, buffer: bytes}], pathlib.Path, str, {name: str, mimeType: str, buffer: bytes}] |  |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

## tap

### 同步

```python signature
def tap(self, selector: str, *, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

Frame.tap

This method taps an element matching `selector` by performing the following steps:
1. Find an element matching `selector`. If there is none, wait until a matching element is attached to the DOM.
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the matched element, unless `force` option is set. If
   the element is detached during the checks, the whole action is retried.
1. Scroll the element into view if needed.
1. Use `page.touchscreen` to tap the center of the element, or the specified `position`.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

**NOTE** `frame.tap()` requires that the `hasTouch` option of the browser context be set to true.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `modifiers` | Union[Sequence[Union["Alt", "Control", "ControlOrMeta", "Meta", "Shift"]], None] | Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current modifiers back. If not specified, currently pressed modifiers are used. "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `position` | Union[{x: float, y: float}, None] | A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. Note that keyboard `modifiers` will be pressed regardless of `trial` to allow testing elements which are only visible when those keys are pressed. |

### 异步

```python signature
async def tap(self, selector: str, *, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

Frame.tap

This method taps an element matching `selector` by performing the following steps:
1. Find an element matching `selector`. If there is none, wait until a matching element is attached to the DOM.
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the matched element, unless `force` option is set. If
   the element is detached during the checks, the whole action is retried.
1. Scroll the element into view if needed.
1. Use `page.touchscreen` to tap the center of the element, or the specified `position`.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

**NOTE** `frame.tap()` requires that the `hasTouch` option of the browser context be set to true.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `modifiers` | Union[Sequence[Union["Alt", "Control", "ControlOrMeta", "Meta", "Shift"]], None] | Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current modifiers back. If not specified, currently pressed modifiers are used. "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `position` | Union[{x: float, y: float}, None] | A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. Note that keyboard `modifiers` will be pressed regardless of `trial` to allow testing elements which are only visible when those keys are pressed. |

## text_content

### 同步

```python signature
def text_content(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Optional[str]
```

Frame.text_content

Returns `element.textContent`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
Union[str, None]

### 异步

```python signature
async def text_content(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Optional[str]
```

Frame.text_content

Returns `element.textContent`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
Union[str, None]


## title

### 同步

```python
def title(self) -> str
```

Frame.title

Returns the page title.

#### Returns
str

### 异步

```python
async def title(self) -> str
```

Frame.title

Returns the page title.

#### Returns
str


## type

### 同步

```python signature
def type(self, selector: str, text: str, *, delay: Optional[float] = None, no_wait_after: Optional[bool] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Frame.type

Sends a `keydown`, `keypress`/`input`, and `keyup` event for each character in the text. `frame.type` can be used
to send fine-grained keyboard events. To fill values in form fields, use `frame.fill()`.

To press a special key, like `Control` or `ArrowDown`, use `keyboard.press()`.

**Usage**

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `text` | str | A text to type into a focused element. |
| `delay` | Union[float, None] | Time to wait between key presses in milliseconds. Defaults to 0. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

### 异步

```python signature
async def type(self, selector: str, text: str, *, delay: Optional[float] = None, no_wait_after: Optional[bool] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Frame.type

Sends a `keydown`, `keypress`/`input`, and `keyup` event for each character in the text. `frame.type` can be used
to send fine-grained keyboard events. To fill values in form fields, use `frame.fill()`.

To press a special key, like `Control` or `ArrowDown`, use `keyboard.press()`.

**Usage**

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `text` | str | A text to type into a focused element. |
| `delay` | Union[float, None] | Time to wait between key presses in milliseconds. Defaults to 0. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

## uncheck

### 同步

```python signature
def uncheck(self, selector: str, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

Frame.uncheck

This method checks an element matching `selector` by performing the following steps:
1. Find an element matching `selector`. If there is none, wait until a matching element is attached to the DOM.
1. Ensure that matched element is a checkbox or a radio input. If not, this method throws. If the element is
   already unchecked, this method returns immediately.
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the matched element, unless `force` option is set. If
   the element is detached during the checks, the whole action is retried.
1. Scroll the element into view if needed.
1. Use `page.mouse` to click in the center of the element.
1. Ensure that the element is now unchecked. If not, this method throws.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `position` | Union[{x: float, y: float}, None] | A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. |

### 异步

```python signature
async def uncheck(self, selector: str, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

Frame.uncheck

This method checks an element matching `selector` by performing the following steps:
1. Find an element matching `selector`. If there is none, wait until a matching element is attached to the DOM.
1. Ensure that matched element is a checkbox or a radio input. If not, this method throws. If the element is
   already unchecked, this method returns immediately.
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the matched element, unless `force` option is set. If
   the element is detached during the checks, the whole action is retried.
1. Scroll the element into view if needed.
1. Use `page.mouse` to click in the center of the element.
1. Ensure that the element is now unchecked. If not, this method throws.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `position` | Union[{x: float, y: float}, None] | A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. |

## url

属性，直接读取；异步入口也不加 await。

```python signature
Frame.url: <class 'str'>
```

Frame.url

Returns frame's url.

#### Returns
str


## wait_for_function

### 同步

```python signature
def wait_for_function(self, expression: str, *, arg: Optional[Any] = None, polling: Union[float, Literal['raf'], NoneType] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'JSHandle'
```

Frame.wait_for_function

Returns when the `expression` returns a truthy value, returns that value.

**Usage**

The `frame.wait_for_function()` can be used to observe viewport size change:

```py
from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    webkit = playwright.webkit
    browser = webkit.launch()
    page = browser.new_page()
    page.evaluate("window.x = 0; setTimeout(() => { window.x = 100 }, 1000);")
    page.main_frame.wait_for_function("() => window.x > 0")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
```

To pass an argument to the predicate of `frame.waitForFunction` function:

```py
selector = ".foo"
frame.wait_for_function("selector => !!document.querySelector(selector)", selector)
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expression` | str | JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked. |
| `arg` | Union[Any, None] | Optional argument to pass to `expression`. |
| `polling` | Union["raf", float, None] | If `polling` is `'raf'`, then `expression` is constantly executed in `requestAnimationFrame` callback. If `polling` is a number, then it is treated as an interval in milliseconds at which the function would be executed. Defaults to `raf`. |
| `timeout` | Union[float, None] | Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
JSHandle

### 异步

```python signature
async def wait_for_function(self, expression: str, *, arg: Optional[Any] = None, polling: Union[float, Literal['raf'], NoneType] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'JSHandle'
```

Frame.wait_for_function

Returns when the `expression` returns a truthy value, returns that value.

**Usage**

The `frame.wait_for_function()` can be used to observe viewport size change:

```py
import asyncio
from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    webkit = playwright.webkit
    browser = await webkit.launch()
    page = await browser.new_page()
    await page.evaluate("window.x = 0; setTimeout(() => { window.x = 100 }, 1000);")
    await page.main_frame.wait_for_function("() => window.x > 0")
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())
```

To pass an argument to the predicate of `frame.waitForFunction` function:

```py
selector = ".foo"
await frame.wait_for_function("selector => !!document.querySelector(selector)", selector)
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expression` | str | JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked. |
| `arg` | Union[Any, None] | Optional argument to pass to `expression`. |
| `polling` | Union["raf", float, None] | If `polling` is `'raf'`, then `expression` is constantly executed in `requestAnimationFrame` callback. If `polling` is a number, then it is treated as an interval in milliseconds at which the function would be executed. Defaults to `raf`. |
| `timeout` | Union[float, None] | Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
JSHandle


## wait_for_load_state

### 同步

```python signature
def wait_for_load_state(self, state: Optional[Literal['domcontentloaded', 'load', 'networkidle']] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Frame.wait_for_load_state

Waits for the required load state to be reached.

This returns when the frame reaches a required load state, `load` by default. The navigation must have been
committed when this method is called. If current document has already reached the required state, resolves
immediately.

**NOTE** Most of the time, this method is not needed because Playwright
[auto-waits before every action](https://playwright.dev/python/docs/actionability).

**Usage**

```py
frame.click("button") # click triggers navigation.
frame.wait_for_load_state() # the promise resolves after "load" event.
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `state` | Union["domcontentloaded", "load", "networkidle", None] | Optional load state to wait for, defaults to `load`. If the state has been already reached while loading current document, the method resolves immediately. Can be one of: - `'load'` - wait for the `load` event to be fired. - `'domcontentloaded'` - wait for the `DOMContentLoaded` event to be fired. - `'networkidle'` - **DISCOURAGED** wait until there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead. |
| `timeout` | Union[float, None] | Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_navigation_timeout()`, `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or `page.set_default_timeout()` methods. |

### 异步

```python signature
async def wait_for_load_state(self, state: Optional[Literal['domcontentloaded', 'load', 'networkidle']] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Frame.wait_for_load_state

Waits for the required load state to be reached.

This returns when the frame reaches a required load state, `load` by default. The navigation must have been
committed when this method is called. If current document has already reached the required state, resolves
immediately.

**NOTE** Most of the time, this method is not needed because Playwright
[auto-waits before every action](https://playwright.dev/python/docs/actionability).

**Usage**

```py
await frame.click("button") # click triggers navigation.
await frame.wait_for_load_state() # the promise resolves after "load" event.
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `state` | Union["domcontentloaded", "load", "networkidle", None] | Optional load state to wait for, defaults to `load`. If the state has been already reached while loading current document, the method resolves immediately. Can be one of: - `'load'` - wait for the `load` event to be fired. - `'domcontentloaded'` - wait for the `DOMContentLoaded` event to be fired. - `'networkidle'` - **DISCOURAGED** wait until there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead. |
| `timeout` | Union[float, None] | Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_navigation_timeout()`, `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or `page.set_default_timeout()` methods. |

## wait_for_selector

### 同步

```python signature
def wait_for_selector(self, selector: str, *, state: Optional[Literal['attached', 'detached', 'hidden', 'visible']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Optional[ForwardRef('ElementHandle')]
```

Frame.wait_for_selector

Returns when element specified by selector satisfies `state` option. Returns `null` if waiting for `hidden` or
`detached`.

**NOTE** Playwright automatically waits for element to be ready before performing an action. Using `Locator`
objects and web-first assertions make the code wait-for-selector-free.

Wait for the `selector` to satisfy `state` option (either appear/disappear from dom, or become visible/hidden). If
at the moment of calling the method `selector` already satisfies the condition, the method will return immediately.
If the selector doesn't satisfy the condition for the `timeout` milliseconds, the function will throw.

**Usage**

This method works across navigations:

```py
from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = chromium.launch()
    page = browser.new_page()
    for current_url in ["https://google.com", "https://bbc.com"]:
        page.goto(current_url, wait_until="domcontentloaded")
        element = page.main_frame.wait_for_selector("img")
        print("Loaded image: " + str(element.get_attribute("src")))
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
```

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

Frame.wait_for_selector

Returns when element specified by selector satisfies `state` option. Returns `null` if waiting for `hidden` or
`detached`.

**NOTE** Playwright automatically waits for element to be ready before performing an action. Using `Locator`
objects and web-first assertions make the code wait-for-selector-free.

Wait for the `selector` to satisfy `state` option (either appear/disappear from dom, or become visible/hidden). If
at the moment of calling the method `selector` already satisfies the condition, the method will return immediately.
If the selector doesn't satisfy the condition for the `timeout` milliseconds, the function will throw.

**Usage**

This method works across navigations:

```py
import asyncio
from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = await chromium.launch()
    page = await browser.new_page()
    for current_url in ["https://google.com", "https://bbc.com"]:
        await page.goto(current_url, wait_until="domcontentloaded")
        element = await page.main_frame.wait_for_selector("img")
        print("Loaded image: " + str(await element.get_attribute("src")))
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to query for. |
| `state` | Union["attached", "detached", "hidden", "visible", None] | Defaults to `'visible'`. Can be either: - `'attached'` - wait for element to be present in DOM. - `'detached'` - wait for element to not be present in DOM. - `'visible'` - wait for element to have non-empty bounding box and no `visibility:hidden`. Note that element without any content or with `display:none` has an empty bounding box and is not considered visible. - `'hidden'` - wait for element to be either detached from DOM, or have an empty bounding box or `visibility:hidden`. This is opposite to the `'visible'` option. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
Union[ElementHandle, None]


## wait_for_timeout

### 同步

```python
def wait_for_timeout(self, timeout: Union[float, datetime.timedelta]) -> None
```

Frame.wait_for_timeout

Waits for the given `timeout` in milliseconds.

Note that `frame.waitForTimeout()` should only be used for debugging. Tests using the timer in production are going
to be flaky. Use signals such as network events, selectors becoming visible and others instead.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | float | A timeout to wait for |

### 异步

```python
async def wait_for_timeout(self, timeout: Union[float, datetime.timedelta]) -> None
```

Frame.wait_for_timeout

Waits for the given `timeout` in milliseconds.

Note that `frame.waitForTimeout()` should only be used for debugging. Tests using the timer in production are going
to be flaky. Use signals such as network events, selectors becoming visible and others instead.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | float | A timeout to wait for |

## wait_for_url

### 同步

```python signature
def wait_for_url(self, url: Union[str, Pattern[str], Callable[[str], bool]], *, timeout: Union[float, datetime.timedelta, NoneType] = None, wait_until: Optional[Literal['commit', 'domcontentloaded', 'load', 'networkidle']] = None) -> None
```

Frame.wait_for_url

Waits for the frame to navigate to the given URL.

**Usage**

```py
frame.click("a.delayed-navigation") # clicking the link will indirectly cause a navigation
frame.wait_for_url("**/target.html")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url` | Union[Callable[[str], bool], Pattern[str], str] | A glob pattern, regex pattern, or predicate receiving [URL] to match while waiting for the navigation. Note that if the parameter is a string without wildcard characters, the method will wait for navigation to URL that is exactly equal to the string. |
| `timeout` | Union[float, None] | Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_navigation_timeout()`, `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or `page.set_default_timeout()` methods. |
| `wait_until` | Union["commit", "domcontentloaded", "load", "networkidle", None] | When to consider operation succeeded, defaults to `load`. Events can be either: - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired. - `'load'` - consider operation to be finished when the `load` event is fired. - `'networkidle'` - **DISCOURAGED** consider operation to be finished when there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead. - `'commit'` - consider operation to be finished when network response is received and the document started loading. |

### 异步

```python signature
async def wait_for_url(self, url: Union[str, Pattern[str], Callable[[str], bool]], *, timeout: Union[float, datetime.timedelta, NoneType] = None, wait_until: Optional[Literal['commit', 'domcontentloaded', 'load', 'networkidle']] = None) -> None
```

Frame.wait_for_url

Waits for the frame to navigate to the given URL.

**Usage**

```py
await frame.click("a.delayed-navigation") # clicking the link will indirectly cause a navigation
await frame.wait_for_url("**/target.html")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url` | Union[Callable[[str], bool], Pattern[str], str] | A glob pattern, regex pattern, or predicate receiving [URL] to match while waiting for the navigation. Note that if the parameter is a string without wildcard characters, the method will wait for navigation to URL that is exactly equal to the string. |
| `timeout` | Union[float, None] | Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_navigation_timeout()`, `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or `page.set_default_timeout()` methods. |
| `wait_until` | Union["commit", "domcontentloaded", "load", "networkidle", None] | When to consider operation succeeded, defaults to `load`. Events can be either: - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired. - `'load'` - consider operation to be finished when the `load` event is fired. - `'networkidle'` - **DISCOURAGED** consider operation to be finished when there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead. - `'commit'` - consider operation to be finished when network response is received and the document started loading. |

## webmcp

属性，直接读取；异步入口也不加 await。

```python signature
Frame.webmcp: WebMCP
```

Frame.webmcp

Tools that the frame registers through the experimental `WebMCP` browser API. See `WebMCP` for details.

#### Returns
WebMCP
