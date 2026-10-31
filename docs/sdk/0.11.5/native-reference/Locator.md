# 原生 Locator

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [all](#all)
- [all_inner_texts](#all_inner_texts)
- [all_text_contents](#all_text_contents)
- [and_](#and_)
- [aria_snapshot](#aria_snapshot)
- [blur](#blur)
- [bounding_box](#bounding_box)
- [check](#check)
- [clear](#clear)
- [click](#click)
- [content_frame](#content_frame)
- [count](#count)
- [dblclick](#dblclick)
- [describe](#describe)
- [description](#description)
- [dispatch_event](#dispatch_event)
- [drag_to](#drag_to)
- [drop](#drop)
- [element_handle](#element_handle)
- [element_handles](#element_handles)
- [evaluate](#evaluate)
- [evaluate_all](#evaluate_all)
- [evaluate_handle](#evaluate_handle)
- [fill](#fill)
- [filter](#filter)
- [first](#first)
- [focus](#focus)
- [frame_locator](#frame_locator)
- [get_attribute](#get_attribute)
- [get_by_alt_text](#get_by_alt_text)
- [get_by_label](#get_by_label)
- [get_by_placeholder](#get_by_placeholder)
- [get_by_role](#get_by_role)
- [get_by_test_id](#get_by_test_id)
- [get_by_text](#get_by_text)
- [get_by_title](#get_by_title)
- [hide_highlight](#hide_highlight)
- [highlight](#highlight)
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
- [last](#last)
- [locator](#locator)
- [normalize](#normalize)
- [nth](#nth)
- [on](#on)
- [once](#once)
- [or_](#or_)
- [page](#page)
- [press](#press)
- [press_sequentially](#press_sequentially)
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
- [visible](#visible)
- [wait_for](#wait_for)
- [wait_for_function](#wait_for_function)
- [within](#within)

## all

### 同步

```python
def all(self) -> List[ForwardRef('Locator')]
```

Locator.all

When the locator points to a list of elements, this returns an array of locators, pointing to their respective
elements.

**NOTE** `locator.all()` does not wait for elements to match the locator, and instead immediately returns whatever
is present in the page.

When the list of elements changes dynamically, `locator.all()` will produce unpredictable and flaky results.

When the list of elements is stable, but loaded dynamically, wait for the full list to finish loading before
calling `locator.all()`.

**Usage**

```py
for li in page.get_by_role('listitem').all():
  li.click();
```

#### Returns
List[Locator]

### 异步

```python
async def all(self) -> List[ForwardRef('Locator')]
```

Locator.all

When the locator points to a list of elements, this returns an array of locators, pointing to their respective
elements.

**NOTE** `locator.all()` does not wait for elements to match the locator, and instead immediately returns whatever
is present in the page.

When the list of elements changes dynamically, `locator.all()` will produce unpredictable and flaky results.

When the list of elements is stable, but loaded dynamically, wait for the full list to finish loading before
calling `locator.all()`.

**Usage**

```py
for li in await page.get_by_role('listitem').all():
  await li.click();
```

#### Returns
List[Locator]


## all_inner_texts

### 同步

```python
def all_inner_texts(self) -> List[str]
```

Locator.all_inner_texts

Returns an array of `node.innerText` values for all matching nodes.

**NOTE** If you need to assert text on the page, prefer `locator_assertions.to_have_text()` with `use_inner_text`
option to avoid flakiness. See [assertions guide](https://playwright.dev/python/docs/test-assertions) for more details.

**Usage**

```py
texts = page.get_by_role("link").all_inner_texts()
```

#### Returns
List[str]

### 异步

```python
async def all_inner_texts(self) -> List[str]
```

Locator.all_inner_texts

Returns an array of `node.innerText` values for all matching nodes.

**NOTE** If you need to assert text on the page, prefer `locator_assertions.to_have_text()` with `use_inner_text`
option to avoid flakiness. See [assertions guide](https://playwright.dev/python/docs/test-assertions) for more details.

**Usage**

```py
texts = await page.get_by_role("link").all_inner_texts()
```

#### Returns
List[str]


## all_text_contents

### 同步

```python
def all_text_contents(self) -> List[str]
```

Locator.all_text_contents

Returns an array of `node.textContent` values for all matching nodes.

**NOTE** If you need to assert text on the page, prefer `locator_assertions.to_have_text()` to avoid flakiness. See
[assertions guide](https://playwright.dev/python/docs/test-assertions) for more details.

**Usage**

```py
texts = page.get_by_role("link").all_text_contents()
```

#### Returns
List[str]

### 异步

```python
async def all_text_contents(self) -> List[str]
```

Locator.all_text_contents

Returns an array of `node.textContent` values for all matching nodes.

**NOTE** If you need to assert text on the page, prefer `locator_assertions.to_have_text()` to avoid flakiness. See
[assertions guide](https://playwright.dev/python/docs/test-assertions) for more details.

**Usage**

```py
texts = await page.get_by_role("link").all_text_contents()
```

#### Returns
List[str]


## and_

### 同步

```python
def and_(self, locator: 'Locator') -> 'Locator'
```

Locator.and_

Creates a locator that matches both this locator and the argument locator.

**Usage**

The following example finds a button with a specific title.

```py
button = page.get_by_role("button").and_(page.get_by_title("Subscribe"))
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `locator` | Locator | Additional locator to match. |

#### Returns
Locator

### 异步

```python
def and_(self, locator: 'Locator') -> 'Locator'
```

Locator.and_

Creates a locator that matches both this locator and the argument locator.

**Usage**

The following example finds a button with a specific title.

```py
button = page.get_by_role("button").and_(page.get_by_title("Subscribe"))
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `locator` | Locator | Additional locator to match. |

#### Returns
Locator


## aria_snapshot

### 同步

```python signature
def aria_snapshot(self, *, boxes: Optional[bool] = None, depth: Optional[int] = None, mode: Optional[Literal['ai', 'default']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> str
```

Locator.aria_snapshot

Captures the aria snapshot of the given element. Read more about [aria snapshots](https://playwright.dev/python/docs/aria-snapshots) and
`locator_assertions.to_match_aria_snapshot()` for the corresponding assertion.

**Usage**

```py
page.get_by_role("link").aria_snapshot()
```

**Details**

This method captures the aria snapshot of the given element. The snapshot is a string that represents the state of
the element and its children. The snapshot can be used to assert the state of the element in the test, or to
compare it to state in the future.

The ARIA snapshot is represented using [YAML](https://yaml.org/spec/1.2.2/) markup language:
- The keys of the objects are the roles and optional accessible names of the elements.
- The values are either text content or an array of child elements.
- Generic static text can be represented with the `text` key.

Below is the HTML markup and the respective ARIA snapshot:

```html
<ul aria-label="Links">
  <li><a href="/">Home</a></li>
  <li><a href="/about">About</a></li>
<ul>
```

```yml
- list "Links":
  - listitem:
    - link "Home"
  - listitem:
    - link "About"
```

An AI-optimized snapshot, controlled by `mode`, is different from a default snapshot:
1. Includes element references `[ref=e2]`. 2. Does not wait for an element matching the locator, and throws when
   no elements match. 3. Includes snapshots of `<iframe>`s inside the target.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `boxes` | Union[bool, None] | When `true`, appends each element's bounding box as `[box=x,y,width,height]` to the snapshot. Coordinates are relative to the viewport, in CSS pixels, as returned by [`Element.getBoundingClientRect()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect). Defaults to `false`. |
| `depth` | Union[int, None] | When specified, limits the depth of the snapshot. |
| `mode` | Union["ai", "default", None] | When set to `"ai"`, returns a snapshot optimized for AI consumption. Defaults to `"default"`. See details for more information. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
str

### 异步

```python signature
async def aria_snapshot(self, *, boxes: Optional[bool] = None, depth: Optional[int] = None, mode: Optional[Literal['ai', 'default']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> str
```

Locator.aria_snapshot

Captures the aria snapshot of the given element. Read more about [aria snapshots](https://playwright.dev/python/docs/aria-snapshots) and
`locator_assertions.to_match_aria_snapshot()` for the corresponding assertion.

**Usage**

```py
await page.get_by_role("link").aria_snapshot()
```

**Details**

This method captures the aria snapshot of the given element. The snapshot is a string that represents the state of
the element and its children. The snapshot can be used to assert the state of the element in the test, or to
compare it to state in the future.

The ARIA snapshot is represented using [YAML](https://yaml.org/spec/1.2.2/) markup language:
- The keys of the objects are the roles and optional accessible names of the elements.
- The values are either text content or an array of child elements.
- Generic static text can be represented with the `text` key.

Below is the HTML markup and the respective ARIA snapshot:

```html
<ul aria-label="Links">
  <li><a href="/">Home</a></li>
  <li><a href="/about">About</a></li>
<ul>
```

```yml
- list "Links":
  - listitem:
    - link "Home"
  - listitem:
    - link "About"
```

An AI-optimized snapshot, controlled by `mode`, is different from a default snapshot:
1. Includes element references `[ref=e2]`. 2. Does not wait for an element matching the locator, and throws when
   no elements match. 3. Includes snapshots of `<iframe>`s inside the target.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `boxes` | Union[bool, None] | When `true`, appends each element's bounding box as `[box=x,y,width,height]` to the snapshot. Coordinates are relative to the viewport, in CSS pixels, as returned by [`Element.getBoundingClientRect()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect). Defaults to `false`. |
| `depth` | Union[int, None] | When specified, limits the depth of the snapshot. |
| `mode` | Union["ai", "default", None] | When set to `"ai"`, returns a snapshot optimized for AI consumption. Defaults to `"default"`. See details for more information. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
str


## blur

### 同步

```python signature
def blur(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Locator.blur

Calls [blur](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/blur) on the element.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

### 异步

```python signature
async def blur(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Locator.blur

Calls [blur](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/blur) on the element.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

## bounding_box

### 同步

```python signature
def bounding_box(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Optional[patchright._impl._api_structures.FloatRect]
```

Locator.bounding_box

This method returns the bounding box of the element matching the locator, or `null` if the element is not visible.
The bounding box is calculated relative to the main frame viewport - which is usually the same as the browser
window.

**Details**

Scrolling affects the returned bounding box, similarly to
[Element.getBoundingClientRect](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect).
That means `x` and/or `y` may be negative.

Elements from child frames return the bounding box relative to the main frame, unlike the
[Element.getBoundingClientRect](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect).

Assuming the page is static, it is safe to use bounding box coordinates to perform input. For example, the
following snippet should click the center of the element.

**Usage**

```py
box = page.get_by_role("button").bounding_box()
page.mouse.click(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
Union[{x: float, y: float, width: float, height: float}, None]

### 异步

```python signature
async def bounding_box(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Optional[patchright._impl._api_structures.FloatRect]
```

Locator.bounding_box

This method returns the bounding box of the element matching the locator, or `null` if the element is not visible.
The bounding box is calculated relative to the main frame viewport - which is usually the same as the browser
window.

**Details**

Scrolling affects the returned bounding box, similarly to
[Element.getBoundingClientRect](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect).
That means `x` and/or `y` may be negative.

Elements from child frames return the bounding box relative to the main frame, unlike the
[Element.getBoundingClientRect](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect).

Assuming the page is static, it is safe to use bounding box coordinates to perform input. For example, the
following snippet should click the center of the element.

**Usage**

```py
box = await page.get_by_role("button").bounding_box()
await page.mouse.click(box["x"] + box["width"] / 2, box["y"] + box["height"] / 2)
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
Union[{x: float, y: float, width: float, height: float}, None]


## check

### 同步

```python signature
def check(self, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

Locator.check

Ensure that checkbox or radio element is checked.

**Details**

Performs the following steps:
1. Ensure that element is a checkbox or a radio input. If not, this method throws. If the element is already
   checked, this method returns immediately.
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the element, unless `force` option is set.
1. Scroll the element into view if needed.
1. Use `page.mouse` to click in the center of the element.
1. Ensure that the element is now checked. If not, this method throws.

If the element is detached from the DOM at any moment during the action, this method throws.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

**Usage**

```py
page.get_by_role("checkbox").check()
```

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

Locator.check

Ensure that checkbox or radio element is checked.

**Details**

Performs the following steps:
1. Ensure that element is a checkbox or a radio input. If not, this method throws. If the element is already
   checked, this method returns immediately.
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the element, unless `force` option is set.
1. Scroll the element into view if needed.
1. Use `page.mouse` to click in the center of the element.
1. Ensure that the element is now checked. If not, this method throws.

If the element is detached from the DOM at any moment during the action, this method throws.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

**Usage**

```py
await page.get_by_role("checkbox").check()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `position` | Union[{x: float, y: float}, None] | A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. |

## clear

### 同步

```python signature
def clear(self, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Locator.clear

Clear the input field.

**Details**

This method waits for [actionability](https://playwright.dev/python/docs/actionability) checks, focuses the element, clears it and triggers an
`input` event after clearing.

If the target element is not an `<input>`, `<textarea>` or `[contenteditable]` element, this method throws an
error. However, if the element is inside the `<label>` element that has an associated
[control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), the control will be cleared
instead.

**Usage**

```py
page.get_by_role("textbox").clear()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

### 异步

```python signature
async def clear(self, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Locator.clear

Clear the input field.

**Details**

This method waits for [actionability](https://playwright.dev/python/docs/actionability) checks, focuses the element, clears it and triggers an
`input` event after clearing.

If the target element is not an `<input>`, `<textarea>` or `[contenteditable]` element, this method throws an
error. However, if the element is inside the `<label>` element that has an associated
[control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), the control will be cleared
instead.

**Usage**

```py
await page.get_by_role("textbox").clear()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

## click

### 同步

```python signature
def click(self, *, button: Optional[Literal['left', 'middle', 'right']] = None, click_count: Optional[int] = None, delay: Optional[float] = None, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, steps: Optional[int] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

Locator.click

Click an element.

**Details**

This method clicks the element by performing the following steps:
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the element, unless `force` option is set.
1. Scroll the element into view if needed.
1. Use `page.mouse` to click in the center of the element, or the specified `position`.
1. Wait for initiated navigations to either succeed or fail, unless `no_wait_after` option is set.

If the element is detached from the DOM at any moment during the action, this method throws.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

**Usage**

Click a button:

```py
page.get_by_role("button").click()
```

Shift-right-click at a specific position on a canvas:

```py
page.locator("canvas").click(
    button="right", modifiers=["Shift"], position={"x": 23, "y": 32}
)
```

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
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. Note that keyboard `modifiers` will be pressed regardless of `trial` to allow testing elements which are only visible when those keys are pressed. |

### 异步

```python signature
async def click(self, *, button: Optional[Literal['left', 'middle', 'right']] = None, click_count: Optional[int] = None, delay: Optional[float] = None, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, steps: Optional[int] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

Locator.click

Click an element.

**Details**

This method clicks the element by performing the following steps:
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the element, unless `force` option is set.
1. Scroll the element into view if needed.
1. Use `page.mouse` to click in the center of the element, or the specified `position`.
1. Wait for initiated navigations to either succeed or fail, unless `no_wait_after` option is set.

If the element is detached from the DOM at any moment during the action, this method throws.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

**Usage**

Click a button:

```py
await page.get_by_role("button").click()
```

Shift-right-click at a specific position on a canvas:

```py
await page.locator("canvas").click(
    button="right", modifiers=["Shift"], position={"x": 23, "y": 32}
)
```

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
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. Note that keyboard `modifiers` will be pressed regardless of `trial` to allow testing elements which are only visible when those keys are pressed. |

## content_frame

属性，直接读取；异步入口也不加 await。

```python signature
Locator.content_frame: FrameLocator
```

Locator.content_frame

Returns a `FrameLocator` object pointing to the same `iframe` as this locator.

Useful when you have a `Locator` object obtained somewhere, and later on would like to interact with the content
inside the frame.

For a reverse operation, use `frame_locator.owner`.

**Usage**

```py
locator = page.locator("iframe[name=\"embedded\"]")
# ...
frame_locator = locator.content_frame
frame_locator.get_by_role("button").click()
```

#### Returns
FrameLocator


## count

### 同步

```python
def count(self) -> int
```

Locator.count

Returns the number of elements matching the locator.

**NOTE** If you need to assert the number of elements on the page, prefer `locator_assertions.to_have_count()` to
avoid flakiness. See [assertions guide](https://playwright.dev/python/docs/test-assertions) for more details.

**Usage**

```py
count = page.get_by_role("listitem").count()
```

#### Returns
int

### 异步

```python
async def count(self) -> int
```

Locator.count

Returns the number of elements matching the locator.

**NOTE** If you need to assert the number of elements on the page, prefer `locator_assertions.to_have_count()` to
avoid flakiness. See [assertions guide](https://playwright.dev/python/docs/test-assertions) for more details.

**Usage**

```py
count = await page.get_by_role("listitem").count()
```

#### Returns
int


## dblclick

### 同步

```python signature
def dblclick(self, *, button: Optional[Literal['left', 'middle', 'right']] = None, delay: Optional[float] = None, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, steps: Optional[int] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

Locator.dblclick

Double-click an element.

**Details**

This method double clicks the element by performing the following steps:
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the element, unless `force` option is set.
1. Scroll the element into view if needed.
1. Use `page.mouse` to double click in the center of the element, or the specified `position`.

If the element is detached from the DOM at any moment during the action, this method throws.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

**NOTE** `element.dblclick()` dispatches two `click` events and a single `dblclick` event.

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
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. Note that keyboard `modifiers` will be pressed regardless of `trial` to allow testing elements which are only visible when those keys are pressed. |

### 异步

```python signature
async def dblclick(self, *, button: Optional[Literal['left', 'middle', 'right']] = None, delay: Optional[float] = None, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, steps: Optional[int] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

Locator.dblclick

Double-click an element.

**Details**

This method double clicks the element by performing the following steps:
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the element, unless `force` option is set.
1. Scroll the element into view if needed.
1. Use `page.mouse` to double click in the center of the element, or the specified `position`.

If the element is detached from the DOM at any moment during the action, this method throws.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

**NOTE** `element.dblclick()` dispatches two `click` events and a single `dblclick` event.

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
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. Note that keyboard `modifiers` will be pressed regardless of `trial` to allow testing elements which are only visible when those keys are pressed. |

## describe

### 同步

```python
def describe(self, description: str) -> 'Locator'
```

Locator.describe

Describes the locator, description is used in the trace viewer and reports. Returns the locator pointing to the
same element.

**Usage**

```py
button = page.get_by_test_id("btn-sub").describe("Subscribe button")
button.click()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `description` | str | Locator description. |

#### Returns
Locator

### 异步

```python
def describe(self, description: str) -> 'Locator'
```

Locator.describe

Describes the locator, description is used in the trace viewer and reports. Returns the locator pointing to the
same element.

**Usage**

```py
button = page.get_by_test_id("btn-sub").describe("Subscribe button")
await button.click()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `description` | str | Locator description. |

#### Returns
Locator


## description

属性，直接读取；异步入口也不加 await。

```python signature
Locator.description: typing.Optional[str]
```

Locator.description

Returns locator description previously set with `locator.describe()`. Returns `null` if no custom description has
been set.

**Usage**

```py
button = page.get_by_role("button").describe("Subscribe button")
print(button.description())  # "Subscribe button"

input = page.get_by_role("textbox")
print(input.description())  # None
```

#### Returns
Union[str, None]


## dispatch_event

### 同步

```python signature
def dispatch_event(self, type: str, event_init: Optional[Dict] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Locator.dispatch_event

Programmatically dispatch an event on the matching element.

**Usage**

```py
locator.dispatch_event("click")
```

**Details**

The snippet above dispatches the `click` event on the element. Regardless of the visibility state of the element,
`click` is dispatched. This is equivalent to calling
[element.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click).

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
data_transfer = page.evaluate_handle("new DataTransfer()")
locator.dispatch_event("#source", "dragstart", {"dataTransfer": data_transfer})
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `type` | str | DOM event type: `"click"`, `"dragstart"`, etc. |
| `event_init` | Union[Dict, None] | Optional event-specific initialization properties. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

### 异步

```python signature
async def dispatch_event(self, type: str, event_init: Optional[Dict] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Locator.dispatch_event

Programmatically dispatch an event on the matching element.

**Usage**

```py
await locator.dispatch_event("click")
```

**Details**

The snippet above dispatches the `click` event on the element. Regardless of the visibility state of the element,
`click` is dispatched. This is equivalent to calling
[element.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click).

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
data_transfer = await page.evaluate_handle("new DataTransfer()")
await locator.dispatch_event("#source", "dragstart", {"dataTransfer": data_transfer})
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `type` | str | DOM event type: `"click"`, `"dragstart"`, etc. |
| `event_init` | Union[Dict, None] | Optional event-specific initialization properties. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

## drag_to

### 同步

```python signature
def drag_to(self, target: 'Locator', *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, scroll: Optional[Literal['auto', 'none']] = None, source_position: Optional[patchright._impl._api_structures.Position] = None, steps: Optional[int] = None, target_position: Optional[patchright._impl._api_structures.Position] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

Locator.drag_to

Drag the source element towards the target element and drop it.

**Details**

This method drags the locator to another target locator or target position. It will first move to the source
element, perform a `mousedown`, then move to the target element or position and perform a `mouseup`.

**Usage**

```py
source = page.locator("#source")
target = page.locator("#target")

source.drag_to(target)
# or specify exact positions relative to the top-left corners of the elements:
source.drag_to(
  target,
  source_position={"x": 34, "y": 7},
  target_position={"x": 10, "y": 20}
)
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `target` | Locator | Locator of the element to drag to. |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `source_position` | Union[{x: float, y: float}, None] | Clicks on the source element at this point relative to the top-left corner of the element's padding box. If not specified, some visible point of the element is used. |
| `steps` | Union[int, None] | Defaults to 1. Sends `n` interpolated `mousemove` events to represent travel between the `mousedown` and `mouseup` of the drag. When set to 1, emits a single `mousemove` event at the destination location. |
| `target_position` | Union[{x: float, y: float}, None] | Drops on the target element at this point relative to the top-left corner of the element's padding box. If not specified, some visible point of the element is used. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. |

### 异步

```python signature
async def drag_to(self, target: 'Locator', *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, scroll: Optional[Literal['auto', 'none']] = None, source_position: Optional[patchright._impl._api_structures.Position] = None, steps: Optional[int] = None, target_position: Optional[patchright._impl._api_structures.Position] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

Locator.drag_to

Drag the source element towards the target element and drop it.

**Details**

This method drags the locator to another target locator or target position. It will first move to the source
element, perform a `mousedown`, then move to the target element or position and perform a `mouseup`.

**Usage**

```py
source = page.locator("#source")
target = page.locator("#target")

await source.drag_to(target)
# or specify exact positions relative to the top-left corners of the elements:
await source.drag_to(
  target,
  source_position={"x": 34, "y": 7},
  target_position={"x": 10, "y": 20}
)
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `target` | Locator | Locator of the element to drag to. |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `source_position` | Union[{x: float, y: float}, None] | Clicks on the source element at this point relative to the top-left corner of the element's padding box. If not specified, some visible point of the element is used. |
| `steps` | Union[int, None] | Defaults to 1. Sends `n` interpolated `mousemove` events to represent travel between the `mousedown` and `mouseup` of the drag. When set to 1, emits a single `mousemove` event at the destination location. |
| `target_position` | Union[{x: float, y: float}, None] | Drops on the target element at this point relative to the top-left corner of the element's padding box. If not specified, some visible point of the element is used. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. |

## drop

### 同步

```python signature
def drop(self, payload: patchright._impl._api_structures.DropPayload, *, position: Optional[patchright._impl._api_structures.Position] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Locator.drop

Simulate an external drag-and-drop of files or clipboard-like data onto this locator.

**Details**

Dispatches the native `dragenter`, `dragover`, and `drop` events at the center of the target element with a
synthetic [DataTransfer] carrying the provided files and/or data entries. Works cross-browser by constructing the
[DataTransfer] in the page context.

If the target element's `dragover` listener does not call `preventDefault()`, the target is considered to have
rejected the drop: Playwright dispatches `dragleave` and this method throws.

**Usage**

Drop a file buffer onto an upload area:

Drop plain text and a URL together:

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `payload` | {files: Union[Sequence[Union[pathlib.Path, str]], Sequence[{name: str, mimeType: str, buffer: bytes}], pathlib.Path, str, {name: str, mimeType: str, buffer: bytes}, None], data: Union[Dict[str, str], None]} | Data to drop onto the target. Provide `files` (file paths or in-memory buffers), `data` (a mime-type → string map for clipboard-like content such as `text/plain`, `text/html`, `text/uri-list`), or both. |
| `position` | Union[{x: float, y: float}, None] | A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

### 异步

```python signature
async def drop(self, payload: patchright._impl._api_structures.DropPayload, *, position: Optional[patchright._impl._api_structures.Position] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Locator.drop

Simulate an external drag-and-drop of files or clipboard-like data onto this locator.

**Details**

Dispatches the native `dragenter`, `dragover`, and `drop` events at the center of the target element with a
synthetic [DataTransfer] carrying the provided files and/or data entries. Works cross-browser by constructing the
[DataTransfer] in the page context.

If the target element's `dragover` listener does not call `preventDefault()`, the target is considered to have
rejected the drop: Playwright dispatches `dragleave` and this method throws.

**Usage**

Drop a file buffer onto an upload area:

Drop plain text and a URL together:

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `payload` | {files: Union[Sequence[Union[pathlib.Path, str]], Sequence[{name: str, mimeType: str, buffer: bytes}], pathlib.Path, str, {name: str, mimeType: str, buffer: bytes}, None], data: Union[Dict[str, str], None]} | Data to drop onto the target. Provide `files` (file paths or in-memory buffers), `data` (a mime-type → string map for clipboard-like content such as `text/plain`, `text/html`, `text/uri-list`), or both. |
| `position` | Union[{x: float, y: float}, None] | A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

## element_handle

### 同步

```python signature
def element_handle(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'ElementHandle'
```

Locator.element_handle

Resolves given locator to the first matching DOM element. If there are no matching elements, waits for one. If
multiple elements match the locator, throws.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
ElementHandle

### 异步

```python signature
async def element_handle(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'ElementHandle'
```

Locator.element_handle

Resolves given locator to the first matching DOM element. If there are no matching elements, waits for one. If
multiple elements match the locator, throws.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
ElementHandle


## element_handles

### 同步

```python
def element_handles(self) -> List[ForwardRef('ElementHandle')]
```

Locator.element_handles

Resolves given locator to all matching DOM elements. If there are no matching elements, returns an empty list.

#### Returns
List[ElementHandle]

### 异步

```python
async def element_handles(self) -> List[ForwardRef('ElementHandle')]
```

Locator.element_handles

Resolves given locator to all matching DOM elements. If there are no matching elements, returns an empty list.

#### Returns
List[ElementHandle]


## evaluate

### 同步

```python signature
def evaluate(self, expression: str, arg: Optional[Any] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None, isolated_context: Optional[bool] = True) -> Any
```

Locator.evaluate

Execute JavaScript code in the page, taking the matching element as an argument.

**Details**

Returns the return value of `expression`, called with the matching element as a first argument, and `arg` as a
second argument.

If `expression` returns a [Promise], this method will wait for the promise to resolve and return its value.

If `expression` throws or rejects, this method throws.

**Usage**

Passing argument to `expression`:

```py
result = page.get_by_testid("myId").evaluate("(element, [x, y]) => element.textContent + ' ' + x * y", [7, 8])
print(result) # prints "myId text 56"
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expression` | str | JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked. |
| `arg` | Union[Any, None] | Optional argument to pass to `expression`. |
| `timeout` | Union[float, None] | Maximum time in milliseconds to wait for the locator before evaluating. Note that after locator is resolved, evaluation itself is not limited by the timeout. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. |

#### Returns
Any

### 异步

```python signature
async def evaluate(self, expression: str, arg: Optional[Any] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None, isolated_context: Optional[bool] = True) -> Any
```

Locator.evaluate

Execute JavaScript code in the page, taking the matching element as an argument.

**Details**

Returns the return value of `expression`, called with the matching element as a first argument, and `arg` as a
second argument.

If `expression` returns a [Promise], this method will wait for the promise to resolve and return its value.

If `expression` throws or rejects, this method throws.

**Usage**

Passing argument to `expression`:

```py
result = await page.get_by_testid("myId").evaluate("(element, [x, y]) => element.textContent + ' ' + x * y", [7, 8])
print(result) # prints "myId text 56"
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expression` | str | JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked. |
| `arg` | Union[Any, None] | Optional argument to pass to `expression`. |
| `timeout` | Union[float, None] | Maximum time in milliseconds to wait for the locator before evaluating. Note that after locator is resolved, evaluation itself is not limited by the timeout. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. |

#### Returns
Any


## evaluate_all

### 同步

```python signature
def evaluate_all(self, expression: str, arg: Optional[Any] = None, *, isolated_context: Optional[bool] = True) -> Any
```

Locator.evaluate_all

Execute JavaScript code in the page, taking all matching elements as an argument.

**Details**

Returns the return value of `expression`, called with an array of all matching elements as a first argument, and
`arg` as a second argument.

If `expression` returns a [Promise], this method will wait for the promise to resolve and return its value.

If `expression` throws or rejects, this method throws.

**Usage**

```py
locator = page.locator("div")
more_than_ten = locator.evaluate_all("(divs, min) => divs.length > min", 10)
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
async def evaluate_all(self, expression: str, arg: Optional[Any] = None, *, isolated_context: Optional[bool] = True) -> Any
```

Locator.evaluate_all

Execute JavaScript code in the page, taking all matching elements as an argument.

**Details**

Returns the return value of `expression`, called with an array of all matching elements as a first argument, and
`arg` as a second argument.

If `expression` returns a [Promise], this method will wait for the promise to resolve and return its value.

If `expression` throws or rejects, this method throws.

**Usage**

```py
locator = page.locator("div")
more_than_ten = await locator.evaluate_all("(divs, min) => divs.length > min", 10)
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
def evaluate_handle(self, expression: str, arg: Optional[Any] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None, isolated_context: Optional[bool] = True) -> 'JSHandle'
```

Locator.evaluate_handle

Execute JavaScript code in the page, taking the matching element as an argument, and return a `JSHandle` with the
result.

**Details**

Returns the return value of `expression` as a`JSHandle`, called with the matching element as a first argument, and
`arg` as a second argument.

The only difference between `locator.evaluate()` and `locator.evaluate_handle()` is that
`locator.evaluate_handle()` returns `JSHandle`.

If `expression` returns a [Promise], this method will wait for the promise to resolve and return its value.

If `expression` throws or rejects, this method throws.

See `page.evaluate_handle()` for more details.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expression` | str | JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked. |
| `arg` | Union[Any, None] | Optional argument to pass to `expression`. |
| `timeout` | Union[float, None] | Maximum time in milliseconds to wait for the locator before evaluating. Note that after locator is resolved, evaluation itself is not limited by the timeout. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. |

#### Returns
JSHandle

### 异步

```python signature
async def evaluate_handle(self, expression: str, arg: Optional[Any] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None, isolated_context: Optional[bool] = True) -> 'JSHandle'
```

Locator.evaluate_handle

Execute JavaScript code in the page, taking the matching element as an argument, and return a `JSHandle` with the
result.

**Details**

Returns the return value of `expression` as a`JSHandle`, called with the matching element as a first argument, and
`arg` as a second argument.

The only difference between `locator.evaluate()` and `locator.evaluate_handle()` is that
`locator.evaluate_handle()` returns `JSHandle`.

If `expression` returns a [Promise], this method will wait for the promise to resolve and return its value.

If `expression` throws or rejects, this method throws.

See `page.evaluate_handle()` for more details.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expression` | str | JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked. |
| `arg` | Union[Any, None] | Optional argument to pass to `expression`. |
| `timeout` | Union[float, None] | Maximum time in milliseconds to wait for the locator before evaluating. Note that after locator is resolved, evaluation itself is not limited by the timeout. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. |

#### Returns
JSHandle


## fill

### 同步

```python signature
def fill(self, value: str, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Locator.fill

Set a value to the input field.

**Usage**

```py
page.get_by_role("textbox").fill("example value")
```

**Details**

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

Locator.fill

Set a value to the input field.

**Usage**

```py
await page.get_by_role("textbox").fill("example value")
```

**Details**

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

## filter

### 同步

```python signature
def filter(self, *, has: Optional[ForwardRef('Locator')] = None, has_not: Optional[ForwardRef('Locator')] = None, has_not_text: Union[str, Pattern[str], NoneType] = None, has_text: Union[str, Pattern[str], NoneType] = None, visible: Optional[bool] = None) -> 'Locator'
```

Locator.filter

This method narrows existing locator according to the options, for example filters by text. It can be chained to
filter multiple times.

**Usage**

```py
row_locator = page.locator("tr")
# ...
row_locator.filter(has_text="text in column 1").filter(
    has=page.get_by_role("button", name="column 2 button")
).screenshot()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `has` | Union[Locator, None] | Narrows down the results of the method to those which contain elements matching this relative locator. For example, `article` that has `text=Playwright` matches `<article><div>Playwright</div></article>`.  Inner locator **must be relative** to the outer locator and is queried starting with the outer locator match, not the document root. For example, you can find `content` that has `div` in `<article><content><div>Playwright</div></content></article>`. However, looking for `content` that has `article div` will fail, because the inner locator must be relative and should not use any elements outside the `content`.  Note that outer and inner locators must belong to the same frame. Inner locator must not contain `FrameLocator`s. |
| `has_not` | Union[Locator, None] | Matches elements that do not contain an element that matches an inner locator. Inner locator is queried against the outer one. For example, `article` that does not have `div` matches `<article><span>Playwright</span></article>`.  Note that outer and inner locators must belong to the same frame. Inner locator must not contain `FrameLocator`s. |
| `has_not_text` | Union[Pattern[str], str, None] | Matches elements that do not contain specified text somewhere inside, possibly in a child or a descendant element. When passed a [string], matching is case-insensitive and searches for a substring. |
| `has_text` | Union[Pattern[str], str, None] | Matches elements containing specified text somewhere inside, possibly in a child or a descendant element. When passed a [string], matching is case-insensitive and searches for a substring. For example, `"Playwright"` matches `<article><div>Playwright</div></article>`. |
| `visible` | Union[bool, None] | Only matches visible or invisible elements. Prefer the `locator.visible` shortcut when matching only visible elements. |

#### Returns
Locator

### 异步

```python signature
def filter(self, *, has: Optional[ForwardRef('Locator')] = None, has_not: Optional[ForwardRef('Locator')] = None, has_not_text: Union[str, Pattern[str], NoneType] = None, has_text: Union[str, Pattern[str], NoneType] = None, visible: Optional[bool] = None) -> 'Locator'
```

Locator.filter

This method narrows existing locator according to the options, for example filters by text. It can be chained to
filter multiple times.

**Usage**

```py
row_locator = page.locator("tr")
# ...
await row_locator.filter(has_text="text in column 1").filter(
    has=page.get_by_role("button", name="column 2 button")
).screenshot()

```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `has` | Union[Locator, None] | Narrows down the results of the method to those which contain elements matching this relative locator. For example, `article` that has `text=Playwright` matches `<article><div>Playwright</div></article>`.  Inner locator **must be relative** to the outer locator and is queried starting with the outer locator match, not the document root. For example, you can find `content` that has `div` in `<article><content><div>Playwright</div></content></article>`. However, looking for `content` that has `article div` will fail, because the inner locator must be relative and should not use any elements outside the `content`.  Note that outer and inner locators must belong to the same frame. Inner locator must not contain `FrameLocator`s. |
| `has_not` | Union[Locator, None] | Matches elements that do not contain an element that matches an inner locator. Inner locator is queried against the outer one. For example, `article` that does not have `div` matches `<article><span>Playwright</span></article>`.  Note that outer and inner locators must belong to the same frame. Inner locator must not contain `FrameLocator`s. |
| `has_not_text` | Union[Pattern[str], str, None] | Matches elements that do not contain specified text somewhere inside, possibly in a child or a descendant element. When passed a [string], matching is case-insensitive and searches for a substring. |
| `has_text` | Union[Pattern[str], str, None] | Matches elements containing specified text somewhere inside, possibly in a child or a descendant element. When passed a [string], matching is case-insensitive and searches for a substring. For example, `"Playwright"` matches `<article><div>Playwright</div></article>`. |
| `visible` | Union[bool, None] | Only matches visible or invisible elements. Prefer the `locator.visible` shortcut when matching only visible elements. |

#### Returns
Locator


## first

属性，直接读取；异步入口也不加 await。

```python signature
Locator.first: Locator
```

Locator.first

Returns locator to the first matching element.

#### Returns
Locator


## focus

### 同步

```python signature
def focus(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Locator.focus

Calls [focus](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/focus) on the matching element.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

### 异步

```python signature
async def focus(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Locator.focus

Calls [focus](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/focus) on the matching element.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

## frame_locator

### 同步

```python
def frame_locator(self, selector: str) -> 'FrameLocator'
```

Locator.frame_locator

When working with iframes, you can create a frame locator that will enter the iframe and allow locating elements in
that iframe:

**Usage**

```py
locator = page.frame_locator("iframe").get_by_text("Submit")
locator.click()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to use when resolving DOM element. |

#### Returns
FrameLocator

### 异步

```python
def frame_locator(self, selector: str) -> 'FrameLocator'
```

Locator.frame_locator

When working with iframes, you can create a frame locator that will enter the iframe and allow locating elements in
that iframe:

**Usage**

```py
locator = page.frame_locator("iframe").get_by_text("Submit")
await locator.click()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to use when resolving DOM element. |

#### Returns
FrameLocator


## get_attribute

### 同步

```python signature
def get_attribute(self, name: str, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Optional[str]
```

Locator.get_attribute

Returns the matching element's attribute value.

**NOTE** If you need to assert an element's attribute, prefer `locator_assertions.to_have_attribute()` to avoid
flakiness. See [assertions guide](https://playwright.dev/python/docs/test-assertions) for more details.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | Attribute name to get the value for. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
Union[str, None]

### 异步

```python signature
async def get_attribute(self, name: str, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Optional[str]
```

Locator.get_attribute

Returns the matching element's attribute value.

**NOTE** If you need to assert an element's attribute, prefer `locator_assertions.to_have_attribute()` to avoid
flakiness. See [assertions guide](https://playwright.dev/python/docs/test-assertions) for more details.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | Attribute name to get the value for. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
Union[str, None]


## get_by_alt_text

### 同步

```python signature
def get_by_alt_text(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'
```

Locator.get_by_alt_text

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

Locator.get_by_alt_text

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

Locator.get_by_label

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

Locator.get_by_label

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

Locator.get_by_placeholder

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

Locator.get_by_placeholder

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

Locator.get_by_role

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

Locator.get_by_role

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

Locator.get_by_test_id

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

Locator.get_by_test_id

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

Locator.get_by_text

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

Locator.get_by_text

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

Locator.get_by_title

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

Locator.get_by_title

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


## hide_highlight

### 同步

```python
def hide_highlight(self) -> None
```

Locator.hide_highlight

Hides the element highlight previously added by `locator.highlight()`.

### 异步

```python
async def hide_highlight(self) -> None
```

Locator.hide_highlight

Hides the element highlight previously added by `locator.highlight()`.


## highlight

### 同步

```python signature
def highlight(self, *, style: Optional[str] = None) -> None
```

Locator.highlight

Highlight the corresponding element(s) on the screen. Useful for debugging, don't commit the code that uses
`locator.highlight()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `style` | Union[str, None] | Additional inline CSS applied to the highlight overlay, e.g. `"outline: 2px dashed red"`. |

### 异步

```python signature
async def highlight(self, *, style: Optional[str] = None) -> None
```

Locator.highlight

Highlight the corresponding element(s) on the screen. Useful for debugging, don't commit the code that uses
`locator.highlight()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `style` | Union[str, None] | Additional inline CSS applied to the highlight overlay, e.g. `"outline: 2px dashed red"`. |

## hover

### 同步

```python signature
def hover(self, *, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

Locator.hover

Hover over the matching element.

**Usage**

```py
page.get_by_role("link").hover()
```

**Details**

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
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. Note that keyboard `modifiers` will be pressed regardless of `trial` to allow testing elements which are only visible when those keys are pressed. |

### 异步

```python signature
async def hover(self, *, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

Locator.hover

Hover over the matching element.

**Usage**

```py
await page.get_by_role("link").hover()
```

**Details**

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
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. Note that keyboard `modifiers` will be pressed regardless of `trial` to allow testing elements which are only visible when those keys are pressed. |

## inner_html

### 同步

```python signature
def inner_html(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> str
```

Locator.inner_html

Returns the [`element.innerHTML`](https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML).

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
str

### 异步

```python signature
async def inner_html(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> str
```

Locator.inner_html

Returns the [`element.innerHTML`](https://developer.mozilla.org/en-US/docs/Web/API/Element/innerHTML).

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
str


## inner_text

### 同步

```python signature
def inner_text(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> str
```

Locator.inner_text

Returns the [`element.innerText`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/innerText).

**NOTE** If you need to assert text on the page, prefer `locator_assertions.to_have_text()` with `use_inner_text`
option to avoid flakiness. See [assertions guide](https://playwright.dev/python/docs/test-assertions) for more details.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
str

### 异步

```python signature
async def inner_text(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> str
```

Locator.inner_text

Returns the [`element.innerText`](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/innerText).

**NOTE** If you need to assert text on the page, prefer `locator_assertions.to_have_text()` with `use_inner_text`
option to avoid flakiness. See [assertions guide](https://playwright.dev/python/docs/test-assertions) for more details.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
str


## input_value

### 同步

```python signature
def input_value(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> str
```

Locator.input_value

Returns the value for the matching `<input>` or `<textarea>` or `<select>` element.

**NOTE** If you need to assert input value, prefer `locator_assertions.to_have_value()` to avoid flakiness. See
[assertions guide](https://playwright.dev/python/docs/test-assertions) for more details.

**Usage**

```py
value = page.get_by_role("textbox").input_value()
```

**Details**

Throws elements that are not an input, textarea or a select. However, if the element is inside the `<label>`
element that has an associated
[control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), returns the value of the
control.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
str

### 异步

```python signature
async def input_value(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> str
```

Locator.input_value

Returns the value for the matching `<input>` or `<textarea>` or `<select>` element.

**NOTE** If you need to assert input value, prefer `locator_assertions.to_have_value()` to avoid flakiness. See
[assertions guide](https://playwright.dev/python/docs/test-assertions) for more details.

**Usage**

```py
value = await page.get_by_role("textbox").input_value()
```

**Details**

Throws elements that are not an input, textarea or a select. However, if the element is inside the `<label>`
element that has an associated
[control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), returns the value of the
control.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
str


## is_checked

### 同步

```python signature
def is_checked(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool
```

Locator.is_checked

Returns whether the element is checked. Throws if the element is not a checkbox or radio input.

**NOTE** If you need to assert that checkbox is checked, prefer `locator_assertions.to_be_checked()` to avoid
flakiness. See [assertions guide](https://playwright.dev/python/docs/test-assertions) for more details.

**Usage**

```py
checked = page.get_by_role("checkbox").is_checked()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
bool

### 异步

```python signature
async def is_checked(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool
```

Locator.is_checked

Returns whether the element is checked. Throws if the element is not a checkbox or radio input.

**NOTE** If you need to assert that checkbox is checked, prefer `locator_assertions.to_be_checked()` to avoid
flakiness. See [assertions guide](https://playwright.dev/python/docs/test-assertions) for more details.

**Usage**

```py
checked = await page.get_by_role("checkbox").is_checked()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
bool


## is_disabled

### 同步

```python signature
def is_disabled(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool
```

Locator.is_disabled

Returns whether the element is disabled, the opposite of [enabled](https://playwright.dev/python/docs/actionability#enabled).

**NOTE** If you need to assert that an element is disabled, prefer `locator_assertions.to_be_disabled()` to avoid
flakiness. See [assertions guide](https://playwright.dev/python/docs/test-assertions) for more details.

**Usage**

```py
disabled = page.get_by_role("button").is_disabled()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
bool

### 异步

```python signature
async def is_disabled(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool
```

Locator.is_disabled

Returns whether the element is disabled, the opposite of [enabled](https://playwright.dev/python/docs/actionability#enabled).

**NOTE** If you need to assert that an element is disabled, prefer `locator_assertions.to_be_disabled()` to avoid
flakiness. See [assertions guide](https://playwright.dev/python/docs/test-assertions) for more details.

**Usage**

```py
disabled = await page.get_by_role("button").is_disabled()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
bool


## is_editable

### 同步

```python signature
def is_editable(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool
```

Locator.is_editable

Returns whether the element is [editable](https://playwright.dev/python/docs/actionability#editable). If the target element is not an `<input>`,
`<textarea>`, `<select>`, `[contenteditable]` and does not have a role allowing `[aria-readonly]`, this method
throws an error.

**NOTE** If you need to assert that an element is editable, prefer `locator_assertions.to_be_editable()` to avoid
flakiness. See [assertions guide](https://playwright.dev/python/docs/test-assertions) for more details.

**Usage**

```py
editable = page.get_by_role("textbox").is_editable()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
bool

### 异步

```python signature
async def is_editable(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool
```

Locator.is_editable

Returns whether the element is [editable](https://playwright.dev/python/docs/actionability#editable). If the target element is not an `<input>`,
`<textarea>`, `<select>`, `[contenteditable]` and does not have a role allowing `[aria-readonly]`, this method
throws an error.

**NOTE** If you need to assert that an element is editable, prefer `locator_assertions.to_be_editable()` to avoid
flakiness. See [assertions guide](https://playwright.dev/python/docs/test-assertions) for more details.

**Usage**

```py
editable = await page.get_by_role("textbox").is_editable()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
bool


## is_enabled

### 同步

```python signature
def is_enabled(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool
```

Locator.is_enabled

Returns whether the element is [enabled](https://playwright.dev/python/docs/actionability#enabled).

**NOTE** If you need to assert that an element is enabled, prefer `locator_assertions.to_be_enabled()` to avoid
flakiness. See [assertions guide](https://playwright.dev/python/docs/test-assertions) for more details.

**Usage**

```py
enabled = page.get_by_role("button").is_enabled()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
bool

### 异步

```python signature
async def is_enabled(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool
```

Locator.is_enabled

Returns whether the element is [enabled](https://playwright.dev/python/docs/actionability#enabled).

**NOTE** If you need to assert that an element is enabled, prefer `locator_assertions.to_be_enabled()` to avoid
flakiness. See [assertions guide](https://playwright.dev/python/docs/test-assertions) for more details.

**Usage**

```py
enabled = await page.get_by_role("button").is_enabled()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
bool


## is_hidden

### 同步

```python signature
def is_hidden(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool
```

Locator.is_hidden

Returns whether the element is hidden, the opposite of [visible](https://playwright.dev/python/docs/actionability#visible).

**NOTE** If you need to assert that element is hidden, prefer `locator_assertions.to_be_hidden()` to avoid
flakiness. See [assertions guide](https://playwright.dev/python/docs/test-assertions) for more details.

**Usage**

```py
hidden = page.get_by_role("button").is_hidden()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Deprecated: This option is ignored. `locator.is_hidden()` does not wait for the element to become hidden and returns immediately. |

#### Returns
bool

### 异步

```python signature
async def is_hidden(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool
```

Locator.is_hidden

Returns whether the element is hidden, the opposite of [visible](https://playwright.dev/python/docs/actionability#visible).

**NOTE** If you need to assert that element is hidden, prefer `locator_assertions.to_be_hidden()` to avoid
flakiness. See [assertions guide](https://playwright.dev/python/docs/test-assertions) for more details.

**Usage**

```py
hidden = await page.get_by_role("button").is_hidden()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Deprecated: This option is ignored. `locator.is_hidden()` does not wait for the element to become hidden and returns immediately. |

#### Returns
bool


## is_visible

### 同步

```python signature
def is_visible(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool
```

Locator.is_visible

Returns whether the element is [visible](https://playwright.dev/python/docs/actionability#visible).

**NOTE** If you need to assert that element is visible, prefer `locator_assertions.to_be_visible()` to avoid
flakiness. See [assertions guide](https://playwright.dev/python/docs/test-assertions) for more details.

**Usage**

```py
visible = page.get_by_role("button").is_visible()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Deprecated: This option is ignored. `locator.is_visible()` does not wait for the element to become visible and returns immediately. |

#### Returns
bool

### 异步

```python signature
async def is_visible(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool
```

Locator.is_visible

Returns whether the element is [visible](https://playwright.dev/python/docs/actionability#visible).

**NOTE** If you need to assert that element is visible, prefer `locator_assertions.to_be_visible()` to avoid
flakiness. See [assertions guide](https://playwright.dev/python/docs/test-assertions) for more details.

**Usage**

```py
visible = await page.get_by_role("button").is_visible()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Deprecated: This option is ignored. `locator.is_visible()` does not wait for the element to become visible and returns immediately. |

#### Returns
bool


## last

属性，直接读取；异步入口也不加 await。

```python signature
Locator.last: Locator
```

Locator.last

Returns locator to the last matching element.

**Usage**

```py
banana = page.get_by_role("listitem").last
```

#### Returns
Locator


## locator

### 同步

```python signature
def locator(self, selector_or_locator: Union[str, ForwardRef('Locator')], *, has: Optional[ForwardRef('Locator')] = None, has_not: Optional[ForwardRef('Locator')] = None, has_not_text: Union[str, Pattern[str], NoneType] = None, has_text: Union[str, Pattern[str], NoneType] = None) -> 'Locator'
```

Locator.locator

The method finds an element matching the specified selector in the locator's subtree. It also accepts filter
options, similar to `locator.filter()` method.

[Learn more about locators](https://playwright.dev/python/docs/locators).

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector_or_locator` | Union[Locator, str] | A selector or locator to use when resolving DOM element. |
| `has` | Union[Locator, None] | Narrows down the results of the method to those which contain elements matching this relative locator. For example, `article` that has `text=Playwright` matches `<article><div>Playwright</div></article>`.  Inner locator **must be relative** to the outer locator and is queried starting with the outer locator match, not the document root. For example, you can find `content` that has `div` in `<article><content><div>Playwright</div></content></article>`. However, looking for `content` that has `article div` will fail, because the inner locator must be relative and should not use any elements outside the `content`.  Note that outer and inner locators must belong to the same frame. Inner locator must not contain `FrameLocator`s. |
| `has_not` | Union[Locator, None] | Matches elements that do not contain an element that matches an inner locator. Inner locator is queried against the outer one. For example, `article` that does not have `div` matches `<article><span>Playwright</span></article>`.  Note that outer and inner locators must belong to the same frame. Inner locator must not contain `FrameLocator`s. |
| `has_not_text` | Union[Pattern[str], str, None] | Matches elements that do not contain specified text somewhere inside, possibly in a child or a descendant element. When passed a [string], matching is case-insensitive and searches for a substring. |
| `has_text` | Union[Pattern[str], str, None] | Matches elements containing specified text somewhere inside, possibly in a child or a descendant element. When passed a [string], matching is case-insensitive and searches for a substring. For example, `"Playwright"` matches `<article><div>Playwright</div></article>`. |

#### Returns
Locator

### 异步

```python signature
def locator(self, selector_or_locator: Union[str, ForwardRef('Locator')], *, has: Optional[ForwardRef('Locator')] = None, has_not: Optional[ForwardRef('Locator')] = None, has_not_text: Union[str, Pattern[str], NoneType] = None, has_text: Union[str, Pattern[str], NoneType] = None) -> 'Locator'
```

Locator.locator

The method finds an element matching the specified selector in the locator's subtree. It also accepts filter
options, similar to `locator.filter()` method.

[Learn more about locators](https://playwright.dev/python/docs/locators).

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector_or_locator` | Union[Locator, str] | A selector or locator to use when resolving DOM element. |
| `has` | Union[Locator, None] | Narrows down the results of the method to those which contain elements matching this relative locator. For example, `article` that has `text=Playwright` matches `<article><div>Playwright</div></article>`.  Inner locator **must be relative** to the outer locator and is queried starting with the outer locator match, not the document root. For example, you can find `content` that has `div` in `<article><content><div>Playwright</div></content></article>`. However, looking for `content` that has `article div` will fail, because the inner locator must be relative and should not use any elements outside the `content`.  Note that outer and inner locators must belong to the same frame. Inner locator must not contain `FrameLocator`s. |
| `has_not` | Union[Locator, None] | Matches elements that do not contain an element that matches an inner locator. Inner locator is queried against the outer one. For example, `article` that does not have `div` matches `<article><span>Playwright</span></article>`.  Note that outer and inner locators must belong to the same frame. Inner locator must not contain `FrameLocator`s. |
| `has_not_text` | Union[Pattern[str], str, None] | Matches elements that do not contain specified text somewhere inside, possibly in a child or a descendant element. When passed a [string], matching is case-insensitive and searches for a substring. |
| `has_text` | Union[Pattern[str], str, None] | Matches elements containing specified text somewhere inside, possibly in a child or a descendant element. When passed a [string], matching is case-insensitive and searches for a substring. For example, `"Playwright"` matches `<article><div>Playwright</div></article>`. |

#### Returns
Locator


## normalize

### 同步

```python
def normalize(self) -> 'Locator'
```

Locator.normalize

Returns a new locator that uses best practices for referencing the matched element, prioritizing test ids, aria
roles, and other user-facing attributes over CSS selectors. This is useful for converting implementation-detail
selectors into more resilient, human-readable locators.

**Usage**

An agent can pick an element by its ref from an `page.aria_snapshot()` taken in the `"ai"` mode. Refs only work for
the latest snapshot. Normalize the ref locator and convert it to a string to get resilient locator code in your
language, the same way `codegen` does.

Consider the following aria snapshot.

You can turn the ref into locator code:

```py
normalized = page.get_by_ref("e2").normalize()
print(str(normalized))
# get_by_role("button", name="Submit")
```

#### Returns
Locator

### 异步

```python
async def normalize(self) -> 'Locator'
```

Locator.normalize

Returns a new locator that uses best practices for referencing the matched element, prioritizing test ids, aria
roles, and other user-facing attributes over CSS selectors. This is useful for converting implementation-detail
selectors into more resilient, human-readable locators.

**Usage**

An agent can pick an element by its ref from an `page.aria_snapshot()` taken in the `"ai"` mode. Refs only work for
the latest snapshot. Normalize the ref locator and convert it to a string to get resilient locator code in your
language, the same way `codegen` does.

Consider the following aria snapshot.

You can turn the ref into locator code:

```py
normalized = await page.get_by_ref("e2").normalize()
print(str(normalized))
# get_by_role("button", name="Submit")
```

#### Returns
Locator


## nth

### 同步

```python
def nth(self, index: int) -> 'Locator'
```

Locator.nth

Returns locator to the n-th matching element. It's zero based, `nth(0)` selects the first element.

**Usage**

```py
banana = page.get_by_role("listitem").nth(2)
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `index` | int |  |

#### Returns
Locator

### 异步

```python
def nth(self, index: int) -> 'Locator'
```

Locator.nth

Returns locator to the n-th matching element. It's zero based, `nth(0)` selects the first element.

**Usage**

```py
banana = await page.get_by_role("listitem").nth(2)
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `index` | int |  |

#### Returns
Locator


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


## or_

### 同步

```python
def or_(self, locator: 'Locator') -> 'Locator'
```

Locator.or_

Creates a locator matching all elements that match one or both of the two locators.

Note that when both locators match something, the resulting locator will have multiple matches, potentially causing
a [locator strictness](https://playwright.dev/python/docs/locators#strictness) violation.

**Usage**

Consider a scenario where you'd like to click on a "New email" button, but sometimes a security settings dialog
shows up instead. In this case, you can wait for either a "New email" button, or a dialog and act accordingly.

**NOTE** If both "New email" button and security dialog appear on screen, the "or" locator will match both of them,
possibly throwing the ["strict mode violation" error](https://playwright.dev/python/docs/locators#strictness). In this case, you can use
`locator.first` to only match one of them.

```py
new_email = page.get_by_role("button", name="New")
dialog = page.get_by_text("Confirm security settings")
expect(new_email.or_(dialog).first).to_be_visible()
if (dialog.is_visible()):
  page.get_by_role("button", name="Dismiss").click()
new_email.click()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `locator` | Locator | Alternative locator to match. |

#### Returns
Locator

### 异步

```python
def or_(self, locator: 'Locator') -> 'Locator'
```

Locator.or_

Creates a locator matching all elements that match one or both of the two locators.

Note that when both locators match something, the resulting locator will have multiple matches, potentially causing
a [locator strictness](https://playwright.dev/python/docs/locators#strictness) violation.

**Usage**

Consider a scenario where you'd like to click on a "New email" button, but sometimes a security settings dialog
shows up instead. In this case, you can wait for either a "New email" button, or a dialog and act accordingly.

**NOTE** If both "New email" button and security dialog appear on screen, the "or" locator will match both of them,
possibly throwing the ["strict mode violation" error](https://playwright.dev/python/docs/locators#strictness). In this case, you can use
`locator.first` to only match one of them.

```py
new_email = page.get_by_role("button", name="New")
dialog = page.get_by_text("Confirm security settings")
await expect(new_email.or_(dialog).first).to_be_visible()
if (await dialog.is_visible()):
  await page.get_by_role("button", name="Dismiss").click()
await new_email.click()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `locator` | Locator | Alternative locator to match. |

#### Returns
Locator


## page

属性，直接读取；异步入口也不加 await。

```python signature
Locator.page: Page
```

Locator.page

A page this locator belongs to.

#### Returns
Page


## press

### 同步

```python signature
def press(self, key: str, *, delay: Optional[float] = None, no_wait_after: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Locator.press

Focuses the matching element and presses a combination of the keys.

**Usage**

```py
page.get_by_role("textbox").press("Backspace")
```

**Details**

Focuses the element, and then uses `keyboard.down()` and `keyboard.up()`.

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
| `key` | str | Name of the key to press or a character to generate, such as `ArrowLeft` or `a`. |
| `delay` | Union[float, None] | Time to wait between `keydown` and `keyup` in milliseconds. Defaults to 0. |
| `no_wait_after` | Union[bool, None] | Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to inaccessible pages. Defaults to `false`. Deprecated: This option will default to `true` in the future. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

### 异步

```python signature
async def press(self, key: str, *, delay: Optional[float] = None, no_wait_after: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Locator.press

Focuses the matching element and presses a combination of the keys.

**Usage**

```py
await page.get_by_role("textbox").press("Backspace")
```

**Details**

Focuses the element, and then uses `keyboard.down()` and `keyboard.up()`.

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
| `key` | str | Name of the key to press or a character to generate, such as `ArrowLeft` or `a`. |
| `delay` | Union[float, None] | Time to wait between `keydown` and `keyup` in milliseconds. Defaults to 0. |
| `no_wait_after` | Union[bool, None] | Actions that initiate navigations are waiting for these navigations to happen and for pages to start loading. You can opt out of waiting via setting this flag. You would only need this option in the exceptional cases such as navigating to inaccessible pages. Defaults to `false`. Deprecated: This option will default to `true` in the future. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

## press_sequentially

### 同步

```python signature
def press_sequentially(self, text: str, *, delay: Optional[float] = None, no_wait_after: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Locator.press_sequentially

**NOTE** In most cases, you should use `locator.fill()` instead. You only need to press keys one by one if there is
special keyboard handling on the page.

Focuses the element, and then sends a `keydown`, `keypress`/`input`, and `keyup` event for each character in the
text.

To press a special key, like `Control` or `ArrowDown`, use `locator.press()`.

**Usage**

```py
locator.press_sequentially("hello") # types instantly
locator.press_sequentially("world", delay=100) # types slower, like a user
```

An example of typing into a text field and then submitting the form:

```py
locator = page.get_by_label("Password")
locator.press_sequentially("my password")
locator.press("Enter")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `text` | str | String of characters to sequentially press into a focused element. |
| `delay` | Union[float, None] | Time to wait between key presses in milliseconds. Defaults to 0. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

### 异步

```python signature
async def press_sequentially(self, text: str, *, delay: Optional[float] = None, no_wait_after: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Locator.press_sequentially

**NOTE** In most cases, you should use `locator.fill()` instead. You only need to press keys one by one if there is
special keyboard handling on the page.

Focuses the element, and then sends a `keydown`, `keypress`/`input`, and `keyup` event for each character in the
text.

To press a special key, like `Control` or `ArrowDown`, use `locator.press()`.

**Usage**

```py
await locator.press_sequentially("hello") # types instantly
await locator.press_sequentially("world", delay=100) # types slower, like a user
```

An example of typing into a text field and then submitting the form:

```py
locator = page.get_by_label("Password")
await locator.press_sequentially("my password")
await locator.press("Enter")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `text` | str | String of characters to sequentially press into a focused element. |
| `delay` | Union[float, None] | Time to wait between key presses in milliseconds. Defaults to 0. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

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

Locator.screenshot

Take a screenshot of the element matching the locator.

**Usage**

```py
page.get_by_role("link").screenshot()
```

Disable animations and save screenshot to a file:

```py
page.get_by_role("link").screenshot(animations="disabled", path="link.png")
```

**Details**

This method captures a screenshot of the page, clipped to the size and position of a particular element matching
the locator. If the element is covered by other elements, it will not be actually visible on the screenshot. If the
element is a scrollable container, only the currently scrolled content will be visible on the screenshot.

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

Locator.screenshot

Take a screenshot of the element matching the locator.

**Usage**

```py
await page.get_by_role("link").screenshot()
```

Disable animations and save screenshot to a file:

```py
await page.get_by_role("link").screenshot(animations="disabled", path="link.png")
```

**Details**

This method captures a screenshot of the page, clipped to the size and position of a particular element matching
the locator. If the element is covered by other elements, it will not be actually visible on the screenshot. If the
element is a scrollable container, only the currently scrolled content will be visible on the screenshot.

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

Locator.scroll_into_view_if_needed

This method waits for [actionability](https://playwright.dev/python/docs/actionability) checks, then tries to scroll element into view, unless
it is completely visible as defined by
[IntersectionObserver](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API)'s `ratio`.

See [scrolling](https://playwright.dev/python/docs/input#scrolling) for alternative ways to scroll.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

### 异步

```python signature
async def scroll_into_view_if_needed(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Locator.scroll_into_view_if_needed

This method waits for [actionability](https://playwright.dev/python/docs/actionability) checks, then tries to scroll element into view, unless
it is completely visible as defined by
[IntersectionObserver](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API)'s `ratio`.

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

Locator.select_option

Selects option or options in `<select>`.

**Details**

This method waits for [actionability](https://playwright.dev/python/docs/actionability) checks, waits until all specified options are present in
the `<select>` element and selects these options.

If the target element is not a `<select>` element, this method throws an error. However, if the element is inside
the `<label>` element that has an associated
[control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), the control will be used
instead.

Returns the array of option values that have been successfully selected.

Triggers a `change` and `input` event once all the provided options have been selected.

**Usage**

```html
<select multiple>
  <option value="red">Red</option>
  <option value="green">Green</option>
  <option value="blue">Blue</option>
</select>
```

```py
# single selection matching the value or label
element.select_option("blue")
# single selection matching the label
element.select_option(label="blue")
# multiple selection for blue, red and second option
element.select_option(value=["red", "green", "blue"])
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

Locator.select_option

Selects option or options in `<select>`.

**Details**

This method waits for [actionability](https://playwright.dev/python/docs/actionability) checks, waits until all specified options are present in
the `<select>` element and selects these options.

If the target element is not a `<select>` element, this method throws an error. However, if the element is inside
the `<label>` element that has an associated
[control](https://developer.mozilla.org/en-US/docs/Web/API/HTMLLabelElement/control), the control will be used
instead.

Returns the array of option values that have been successfully selected.

Triggers a `change` and `input` event once all the provided options have been selected.

**Usage**

```html
<select multiple>
  <option value="red">Red</option>
  <option value="green">Green</option>
  <option value="blue">Blue</option>
</select>
```

```py
# single selection matching the value or label
await element.select_option("blue")
# single selection matching the label
await element.select_option(label="blue")
# multiple selection for blue, red and second option
await element.select_option(value=["red", "green", "blue"])
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

Locator.select_text

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

Locator.select_text

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

Locator.set_checked

Set the state of a checkbox or a radio element.

**Usage**

```py
page.get_by_role("checkbox").set_checked(True)
```

**Details**

This method checks or unchecks an element by performing the following steps:
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

Locator.set_checked

Set the state of a checkbox or a radio element.

**Usage**

```py
await page.get_by_role("checkbox").set_checked(True)
```

**Details**

This method checks or unchecks an element by performing the following steps:
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

Locator.set_input_files

Upload file or multiple files into `<input type=file>`. For inputs with a `[webkitdirectory]` attribute, only a
single directory path is supported.

**Usage**

```py
# Select one file
page.get_by_label("Upload file").set_input_files('myfile.pdf')

# Select multiple files
page.get_by_label("Upload files").set_input_files(['file1.txt', 'file2.txt'])

# Select a directory
page.get_by_label("Upload directory").set_input_files('mydir')

# Remove all the selected files
page.get_by_label("Upload file").set_input_files([])

# Upload buffer from memory
page.get_by_label("Upload file").set_input_files(
    files=[
        {"name": "test.txt", "mimeType": "text/plain", "buffer": b"this is a test"}
    ],
)
```

**Details**

Sets the value of the file input to these file paths or files. If some of the `filePaths` are relative paths, then
they are resolved relative to the current working directory. For empty array, clears the selected files.

This method expects `Locator` to point to an
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

Locator.set_input_files

Upload file or multiple files into `<input type=file>`. For inputs with a `[webkitdirectory]` attribute, only a
single directory path is supported.

**Usage**

```py
# Select one file
await page.get_by_label("Upload file").set_input_files('myfile.pdf')

# Select multiple files
await page.get_by_label("Upload files").set_input_files(['file1.txt', 'file2.txt'])

# Select a directory
await page.get_by_label("Upload directory").set_input_files('mydir')

# Remove all the selected files
await page.get_by_label("Upload file").set_input_files([])

# Upload buffer from memory
await page.get_by_label("Upload file").set_input_files(
    files=[
        {"name": "test.txt", "mimeType": "text/plain", "buffer": b"this is a test"}
    ],
)
```

**Details**

Sets the value of the file input to these file paths or files. If some of the `filePaths` are relative paths, then
they are resolved relative to the current working directory. For empty array, clears the selected files.

This method expects `Locator` to point to an
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

Locator.tap

Perform a tap gesture on the element matching the locator. For examples of emulating other gestures by manually
dispatching touch events, see the [emulating legacy touch events](https://playwright.dev/python/docs/touch-events) page.

**Details**

This method taps the element by performing the following steps:
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the element, unless `force` option is set.
1. Scroll the element into view if needed.
1. Use `page.touchscreen` to tap the center of the element, or the specified `position`.

If the element is detached from the DOM at any moment during the action, this method throws.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

**NOTE** `element.tap()` requires that the `hasTouch` option of the browser context be set to true.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `modifiers` | Union[Sequence[Union["Alt", "Control", "ControlOrMeta", "Meta", "Shift"]], None] | Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current modifiers back. If not specified, currently pressed modifiers are used. "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `position` | Union[{x: float, y: float}, None] | A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. Note that keyboard `modifiers` will be pressed regardless of `trial` to allow testing elements which are only visible when those keys are pressed. |

### 异步

```python signature
async def tap(self, *, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

Locator.tap

Perform a tap gesture on the element matching the locator. For examples of emulating other gestures by manually
dispatching touch events, see the [emulating legacy touch events](https://playwright.dev/python/docs/touch-events) page.

**Details**

This method taps the element by performing the following steps:
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the element, unless `force` option is set.
1. Scroll the element into view if needed.
1. Use `page.touchscreen` to tap the center of the element, or the specified `position`.

If the element is detached from the DOM at any moment during the action, this method throws.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

**NOTE** `element.tap()` requires that the `hasTouch` option of the browser context be set to true.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `force` | Union[bool, None] | Whether to bypass the actionability checks. Defaults to `false`. |
| `modifiers` | Union[Sequence[Union["Alt", "Control", "ControlOrMeta", "Meta", "Shift"]], None] | Modifier keys to press. Ensures that only these modifiers are pressed during the operation, and then restores current modifiers back. If not specified, currently pressed modifiers are used. "ControlOrMeta" resolves to "Control" on Windows and Linux and to "Meta" on macOS. |
| `no_wait_after` | Union[bool, None] | This option has no effect. Deprecated: This option has no effect. |
| `position` | Union[{x: float, y: float}, None] | A point to use relative to the top-left corner of element padding box. If not specified, uses some visible point of the element. |
| `scroll` | Union["auto", "none", None] | Controls whether Playwright scrolls the element into view before performing the action. Defaults to `"auto"`, which scrolls the element into view when necessary, including scrolling nested scrollable containers. When set to `"none"`, Playwright does not scroll the element and the action fails if the element is not already in the viewport. This is useful to assert that an element is reachable by the user without additional scrolling. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |
| `trial` | Union[bool, None] | When set, this method only performs the actionability checks and skips the action. Defaults to `false`. Useful to wait until the element is ready for the action without performing it. Note that keyboard `modifiers` will be pressed regardless of `trial` to allow testing elements which are only visible when those keys are pressed. |

## text_content

### 同步

```python signature
def text_content(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Optional[str]
```

Locator.text_content

Returns the [`node.textContent`](https://developer.mozilla.org/en-US/docs/Web/API/Node/textContent).

**NOTE** If you need to assert text on the page, prefer `locator_assertions.to_have_text()` to avoid flakiness. See
[assertions guide](https://playwright.dev/python/docs/test-assertions) for more details.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
Union[str, None]

### 异步

```python signature
async def text_content(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Optional[str]
```

Locator.text_content

Returns the [`node.textContent`](https://developer.mozilla.org/en-US/docs/Web/API/Node/textContent).

**NOTE** If you need to assert text on the page, prefer `locator_assertions.to_have_text()` to avoid flakiness. See
[assertions guide](https://playwright.dev/python/docs/test-assertions) for more details.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
Union[str, None]


## type

### 同步

```python signature
def type(self, text: str, *, delay: Optional[float] = None, no_wait_after: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Locator.type

Focuses the element, and then sends a `keydown`, `keypress`/`input`, and `keyup` event for each character in the
text.

To press a special key, like `Control` or `ArrowDown`, use `locator.press()`.

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

Locator.type

Focuses the element, and then sends a `keydown`, `keypress`/`input`, and `keyup` event for each character in the
text.

To press a special key, like `Control` or `ArrowDown`, use `locator.press()`.

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

Locator.uncheck

Ensure that checkbox or radio element is unchecked.

**Usage**

```py
page.get_by_role("checkbox").uncheck()
```

**Details**

This method unchecks the element by performing the following steps:
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

Locator.uncheck

Ensure that checkbox or radio element is unchecked.

**Usage**

```py
await page.get_by_role("checkbox").uncheck()
```

**Details**

This method unchecks the element by performing the following steps:
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

## visible

属性，直接读取；异步入口也不加 await。

```python signature
Locator.visible: Locator
```

Locator.visible

Returns a locator that matches only [visible](https://playwright.dev/python/docs/actionability#visible) elements, ignoring the invisible ones.
This is the recommended way to distinguish elements by visibility, as opposed to the `:visible` CSS pseudo-class.

Note that visibility is checked every time the locator is used, and not at the moment of the `locator.visible`
call.

**Usage**

Consider a page with two buttons, the first invisible and the second visible.

```html
<button style='display: none'>Invisible</button>
<button>Visible</button>
```

This will only find the second button, because it is visible, and then click it.

```py
page.locator("button").visible.click()
```

To match invisible elements instead, use `locator.filter()` with the `visible` option set to `false`.

#### Returns
Locator


## wait_for

### 同步

```python signature
def wait_for(self, *, state: Optional[Literal['attached', 'detached', 'hidden', 'visible']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Locator.wait_for

Returns when element specified by locator satisfies the `state` option.

If target element already satisfies the condition, the method returns immediately. Otherwise, waits for up to
`timeout` milliseconds until the condition is met.

**Usage**

```py
order_sent = page.locator("#order-sent")
order_sent.wait_for()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `state` | Union["attached", "detached", "hidden", "visible", None] | Defaults to `'visible'`. Can be either: - `'attached'` - wait for element to be present in DOM. - `'detached'` - wait for element to not be present in DOM. - `'visible'` - wait for element to have non-empty bounding box and no `visibility:hidden`. Note that element without any content or with `display:none` has an empty bounding box and is not considered visible. - `'hidden'` - wait for element to be either detached from DOM, or have an empty bounding box or `visibility:hidden`. This is opposite to the `'visible'` option. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

### 异步

```python signature
async def wait_for(self, *, state: Optional[Literal['attached', 'detached', 'hidden', 'visible']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Locator.wait_for

Returns when element specified by locator satisfies the `state` option.

If target element already satisfies the condition, the method returns immediately. Otherwise, waits for up to
`timeout` milliseconds until the condition is met.

**Usage**

```py
order_sent = page.locator("#order-sent")
await order_sent.wait_for()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `state` | Union["attached", "detached", "hidden", "visible", None] | Defaults to `'visible'`. Can be either: - `'attached'` - wait for element to be present in DOM. - `'detached'` - wait for element to not be present in DOM. - `'visible'` - wait for element to have non-empty bounding box and no `visibility:hidden`. Note that element without any content or with `display:none` has an empty bounding box and is not considered visible. - `'hidden'` - wait for element to be either detached from DOM, or have an empty bounding box or `visibility:hidden`. This is opposite to the `'visible'` option. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

## wait_for_function

### 同步

```python signature
def wait_for_function(self, expression: str, *, arg: Optional[Any] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Locator.wait_for_function

Returns when `expression` returns a truthy value, called with the matching element as a first argument, and `arg`
as a second argument.

This is a generic way to wait for an element to reach a custom condition without asserting it. The locator is
re-resolved on each retry, so it tolerates the element being re-rendered while waiting.

If `expression` returns a [Promise], this method will wait for the promise to resolve before checking its value.

If `expression` throws or rejects, this method throws.

**Usage**

Wait for an attribute to appear:

Passing argument to `expression`:

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expression` | str | JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked. |
| `arg` | Union[Any, None] | Optional argument to pass to `expression`. |
| `timeout` | Union[float, None] | Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

### 异步

```python signature
async def wait_for_function(self, expression: str, *, arg: Optional[Any] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Locator.wait_for_function

Returns when `expression` returns a truthy value, called with the matching element as a first argument, and `arg`
as a second argument.

This is a generic way to wait for an element to reach a custom condition without asserting it. The locator is
re-resolved on each retry, so it tolerates the element being re-rendered while waiting.

If `expression` returns a [Promise], this method will wait for the promise to resolve before checking its value.

If `expression` throws or rejects, this method throws.

**Usage**

Wait for an attribute to appear:

Passing argument to `expression`:

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expression` | str | JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked. |
| `arg` | Union[Any, None] | Optional argument to pass to `expression`. |
| `timeout` | Union[float, None] | Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

## within

### 同步

```python
def within(self, locator: 'Locator') -> 'Locator'
```

Locator.within

Returns a locator that matches this locator's elements inside each element matched by `locator`.

Note that relative locators, such as `locator.nth()` or `locator.first`, are resolved separately inside each
matched parent. In the example below, `page.getByRole('cell').nth(2)` picks the third cell of every row, not the
third cell in the whole table.

**Usage**

```py
third_column = page.get_by_role("cell").nth(2).within(page.get_by_role("row"))
expect(third_column).to_have_text(["Apple", "Banana", "Cherry"])
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `locator` | Locator | Locator matching the parent elements to search within. |

#### Returns
Locator

### 异步

```python
def within(self, locator: 'Locator') -> 'Locator'
```

Locator.within

Returns a locator that matches this locator's elements inside each element matched by `locator`.

Note that relative locators, such as `locator.nth()` or `locator.first`, are resolved separately inside each
matched parent. In the example below, `page.getByRole('cell').nth(2)` picks the third cell of every row, not the
third cell in the whole table.

**Usage**

```py
third_column = page.get_by_role("cell").nth(2).within(page.get_by_role("row"))
await expect(third_column).to_have_text(["Apple", "Banana", "Cherry"])
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `locator` | Locator | Locator matching the parent elements to search within. |

#### Returns
Locator
