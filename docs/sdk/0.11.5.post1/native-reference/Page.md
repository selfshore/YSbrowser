# 原生 Page

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [add_init_script](#add_init_script)
- [add_locator_handler](#add_locator_handler)
- [add_script_tag](#add_script_tag)
- [add_style_tag](#add_style_tag)
- [aria_snapshot](#aria_snapshot)
- [bring_to_front](#bring_to_front)
- [cancel_pick_locator](#cancel_pick_locator)
- [check](#check)
- [clear_console_messages](#clear_console_messages)
- [clear_page_errors](#clear_page_errors)
- [click](#click)
- [clock](#clock)
- [close](#close)
- [console_messages](#console_messages)
- [content](#content)
- [context](#context)
- [dblclick](#dblclick)
- [dispatch_event](#dispatch_event)
- [drag_and_drop](#drag_and_drop)
- [emulate_media](#emulate_media)
- [eval_on_selector](#eval_on_selector)
- [eval_on_selector_all](#eval_on_selector_all)
- [evaluate](#evaluate)
- [evaluate_handle](#evaluate_handle)
- [expect_console_message](#expect_console_message)
- [expect_download](#expect_download)
- [expect_event](#expect_event)
- [expect_file_chooser](#expect_file_chooser)
- [expect_navigation](#expect_navigation)
- [expect_popup](#expect_popup)
- [expect_request](#expect_request)
- [expect_request_finished](#expect_request_finished)
- [expect_response](#expect_response)
- [expect_websocket](#expect_websocket)
- [expect_worker](#expect_worker)
- [expose_binding](#expose_binding)
- [expose_function](#expose_function)
- [fill](#fill)
- [focus](#focus)
- [frame](#frame)
- [frame_locator](#frame_locator)
- [frames](#frames)
- [get_attribute](#get_attribute)
- [get_by_alt_text](#get_by_alt_text)
- [get_by_label](#get_by_label)
- [get_by_placeholder](#get_by_placeholder)
- [get_by_ref](#get_by_ref)
- [get_by_role](#get_by_role)
- [get_by_test_id](#get_by_test_id)
- [get_by_text](#get_by_text)
- [get_by_title](#get_by_title)
- [go_back](#go_back)
- [go_forward](#go_forward)
- [goto](#goto)
- [hide_highlight](#hide_highlight)
- [hover](#hover)
- [inner_html](#inner_html)
- [inner_text](#inner_text)
- [input_value](#input_value)
- [is_checked](#is_checked)
- [is_closed](#is_closed)
- [is_disabled](#is_disabled)
- [is_editable](#is_editable)
- [is_enabled](#is_enabled)
- [is_hidden](#is_hidden)
- [is_visible](#is_visible)
- [keyboard](#keyboard)
- [local_storage](#local_storage)
- [locator](#locator)
- [main_frame](#main_frame)
- [mouse](#mouse)
- [on](#on)
- [once](#once)
- [opener](#opener)
- [page_errors](#page_errors)
- [pause](#pause)
- [pdf](#pdf)
- [pick_locator](#pick_locator)
- [press](#press)
- [query_selector](#query_selector)
- [query_selector_all](#query_selector_all)
- [reload](#reload)
- [remove_listener](#remove_listener)
- [remove_locator_handler](#remove_locator_handler)
- [request](#request)
- [request_gc](#request_gc)
- [requests](#requests)
- [route](#route)
- [route_from_har](#route_from_har)
- [route_web_socket](#route_web_socket)
- [screencast](#screencast)
- [screenshot](#screenshot)
- [select_option](#select_option)
- [session_storage](#session_storage)
- [set_checked](#set_checked)
- [set_content](#set_content)
- [set_default_navigation_timeout](#set_default_navigation_timeout)
- [set_default_timeout](#set_default_timeout)
- [set_extra_http_headers](#set_extra_http_headers)
- [set_input_files](#set_input_files)
- [set_viewport_size](#set_viewport_size)
- [tap](#tap)
- [text_content](#text_content)
- [title](#title)
- [touchscreen](#touchscreen)
- [type](#type)
- [uncheck](#uncheck)
- [unroute](#unroute)
- [unroute_all](#unroute_all)
- [url](#url)
- [video](#video)
- [viewport_size](#viewport_size)
- [wait_for_event](#wait_for_event)
- [wait_for_function](#wait_for_function)
- [wait_for_load_state](#wait_for_load_state)
- [wait_for_selector](#wait_for_selector)
- [wait_for_timeout](#wait_for_timeout)
- [wait_for_url](#wait_for_url)
- [webmcp](#webmcp)
- [workers](#workers)

## add_init_script

### 同步

```python signature
def add_init_script(self, script: Optional[str] = None, *, path: Union[pathlib.Path, str, NoneType] = None) -> 'SyncContextManager'
```

Page.add_init_script

Adds a script which would be evaluated in one of the following scenarios:
- Whenever the page is navigated.
- Whenever the child frame is attached or navigated. In this case, the script is evaluated in the context of the
  newly attached frame.

The script is evaluated after the document was created but before any of its scripts were run. This is useful to
amend the JavaScript environment, e.g. to seed `Math.random`.

**Usage**

An example of overriding `Math.random` before the page loads:

```py
# in your playwright script, assuming the preload.js file is in same directory
page.add_init_script(path="./preload.js")
```

**NOTE** The order of evaluation of multiple scripts installed via `browser_context.add_init_script()` and
`page.add_init_script()` is not defined.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `script` | Union[str, None] | Script to be evaluated in all pages in the browser context. Optional. |
| `path` | Union[pathlib.Path, str, None] | Path to the JavaScript file. If `path` is a relative path, then it is resolved relative to the current working directory. Optional. |

#### Returns
SyncContextManager

### 异步

```python signature
async def add_init_script(self, script: Optional[str] = None, *, path: Union[pathlib.Path, str, NoneType] = None) -> 'AsyncContextManager'
```

Page.add_init_script

Adds a script which would be evaluated in one of the following scenarios:
- Whenever the page is navigated.
- Whenever the child frame is attached or navigated. In this case, the script is evaluated in the context of the
  newly attached frame.

The script is evaluated after the document was created but before any of its scripts were run. This is useful to
amend the JavaScript environment, e.g. to seed `Math.random`.

**Usage**

An example of overriding `Math.random` before the page loads:

```py
# in your playwright script, assuming the preload.js file is in same directory
await page.add_init_script(path="./preload.js")
```

**NOTE** The order of evaluation of multiple scripts installed via `browser_context.add_init_script()` and
`page.add_init_script()` is not defined.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `script` | Union[str, None] | Script to be evaluated in all pages in the browser context. Optional. |
| `path` | Union[pathlib.Path, str, None] | Path to the JavaScript file. If `path` is a relative path, then it is resolved relative to the current working directory. Optional. |

#### Returns
AsyncContextManager


## add_locator_handler

### 同步

```python signature
def add_locator_handler(self, locator: 'Locator', handler: Union[Callable[[ForwardRef('Locator')], Any], Callable[[], Any]], *, no_wait_after: Optional[bool] = None, times: Optional[int] = None) -> None
```

Page.add_locator_handler

When testing a web page, sometimes unexpected overlays like a "Sign up" dialog appear and block actions you want to
automate, e.g. clicking a button. These overlays don't always show up in the same way or at the same time, making
them tricky to handle in automated tests.

This method lets you set up a special function, called a handler, that activates when it detects that overlay is
visible. The handler's job is to remove the overlay, allowing your test to continue as if the overlay wasn't there.

Things to keep in mind:
- When an overlay is shown predictably, we recommend explicitly waiting for it in your test and dismissing it as
  a part of your normal test flow, instead of using `page.add_locator_handler()`.
- Playwright checks for the overlay every time before executing or retrying an action that requires an
  [actionability check](https://playwright.dev/python/docs/actionability), or before performing an auto-waiting assertion check. When overlay
  is visible, Playwright calls the handler first, and then proceeds with the action/assertion. Note that the
  handler is only called when you perform an action/assertion - if the overlay becomes visible but you don't
  perform any actions, the handler will not be triggered.
- After executing the handler, Playwright will ensure that overlay that triggered the handler is not visible
  anymore. You can opt-out of this behavior with `no_wait_after`.
- The execution time of the handler counts towards the timeout of the action/assertion that executed the handler.
  If your handler takes too long, it might cause timeouts.
- You can register multiple handlers. However, only a single handler will be running at a time. Make sure the
  actions within a handler don't depend on another handler.

**NOTE** Running the handler will alter your page state mid-test. For example it will change the currently focused
element and move the mouse. Make sure that actions that run after the handler are self-contained and do not rely on
the focus and mouse state being unchanged.

For example, consider a test that calls `locator.focus()` followed by `keyboard.press()`. If your handler clicks a
button between these two actions, the focused element most likely will be wrong, and key press will happen on the
unexpected element. Use `locator.press()` instead to avoid this problem.

Another example is a series of mouse actions, where `mouse.move()` is followed by `mouse.down()`. Again, when the
handler runs between these two actions, the mouse position will be wrong during the mouse down. Prefer
self-contained actions like `locator.click()` that do not rely on the state being unchanged by a handler.

**Usage**

An example that closes a "Sign up to the newsletter" dialog when it appears:

```py
# Setup the handler.
def handler():
  page.get_by_role("button", name="No thanks").click()
page.add_locator_handler(page.get_by_text("Sign up to the newsletter"), handler)

# Write the test as usual.
page.goto("https://example.com")
page.get_by_role("button", name="Start here").click()
```

An example that skips the "Confirm your security details" page when it is shown:

```py
# Setup the handler.
def handler():
  page.get_by_role("button", name="Remind me later").click()
page.add_locator_handler(page.get_by_text("Confirm your security details"), handler)

# Write the test as usual.
page.goto("https://example.com")
page.get_by_role("button", name="Start here").click()
```

An example with a custom callback on every actionability check. It uses a `<body>` locator that is always visible,
so the handler is called before every actionability check. It is important to specify `no_wait_after`, because the
handler does not hide the `<body>` element.

```py
# Setup the handler.
def handler():
  page.evaluate("window.removeObstructionsForTestIfNeeded()")
page.add_locator_handler(page.locator("body"), handler, no_wait_after=True)

# Write the test as usual.
page.goto("https://example.com")
page.get_by_role("button", name="Start here").click()
```

Handler takes the original locator as an argument. You can also automatically remove the handler after a number of
invocations by setting `times`:

```py
def handler(locator):
  locator.click()
page.add_locator_handler(page.get_by_label("Close"), handler, times=1)
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `locator` | Locator | Locator that triggers the handler. |
| `handler` | Union[Callable[[Locator], Any], Callable[[], Any]] | Function that should be run once `locator` appears. This function should get rid of the element that blocks actions like click. |
| `no_wait_after` | Union[bool, None] | By default, after calling the handler Playwright will wait until the overlay becomes hidden, and only then Playwright will continue with the action/assertion that triggered the handler. This option allows to opt-out of this behavior, so that overlay can stay visible after the handler has run. |
| `times` | Union[int, None] | Specifies the maximum number of times this handler should be called. Unlimited by default. |

### 异步

```python signature
async def add_locator_handler(self, locator: 'Locator', handler: Union[Callable[[ForwardRef('Locator')], Any], Callable[[], Any]], *, no_wait_after: Optional[bool] = None, times: Optional[int] = None) -> None
```

Page.add_locator_handler

When testing a web page, sometimes unexpected overlays like a "Sign up" dialog appear and block actions you want to
automate, e.g. clicking a button. These overlays don't always show up in the same way or at the same time, making
them tricky to handle in automated tests.

This method lets you set up a special function, called a handler, that activates when it detects that overlay is
visible. The handler's job is to remove the overlay, allowing your test to continue as if the overlay wasn't there.

Things to keep in mind:
- When an overlay is shown predictably, we recommend explicitly waiting for it in your test and dismissing it as
  a part of your normal test flow, instead of using `page.add_locator_handler()`.
- Playwright checks for the overlay every time before executing or retrying an action that requires an
  [actionability check](https://playwright.dev/python/docs/actionability), or before performing an auto-waiting assertion check. When overlay
  is visible, Playwright calls the handler first, and then proceeds with the action/assertion. Note that the
  handler is only called when you perform an action/assertion - if the overlay becomes visible but you don't
  perform any actions, the handler will not be triggered.
- After executing the handler, Playwright will ensure that overlay that triggered the handler is not visible
  anymore. You can opt-out of this behavior with `no_wait_after`.
- The execution time of the handler counts towards the timeout of the action/assertion that executed the handler.
  If your handler takes too long, it might cause timeouts.
- You can register multiple handlers. However, only a single handler will be running at a time. Make sure the
  actions within a handler don't depend on another handler.

**NOTE** Running the handler will alter your page state mid-test. For example it will change the currently focused
element and move the mouse. Make sure that actions that run after the handler are self-contained and do not rely on
the focus and mouse state being unchanged.

For example, consider a test that calls `locator.focus()` followed by `keyboard.press()`. If your handler clicks a
button between these two actions, the focused element most likely will be wrong, and key press will happen on the
unexpected element. Use `locator.press()` instead to avoid this problem.

Another example is a series of mouse actions, where `mouse.move()` is followed by `mouse.down()`. Again, when the
handler runs between these two actions, the mouse position will be wrong during the mouse down. Prefer
self-contained actions like `locator.click()` that do not rely on the state being unchanged by a handler.

**Usage**

An example that closes a "Sign up to the newsletter" dialog when it appears:

```py
# Setup the handler.
async def handler():
  await page.get_by_role("button", name="No thanks").click()
await page.add_locator_handler(page.get_by_text("Sign up to the newsletter"), handler)

# Write the test as usual.
await page.goto("https://example.com")
await page.get_by_role("button", name="Start here").click()
```

An example that skips the "Confirm your security details" page when it is shown:

```py
# Setup the handler.
async def handler():
  await page.get_by_role("button", name="Remind me later").click()
await page.add_locator_handler(page.get_by_text("Confirm your security details"), handler)

# Write the test as usual.
await page.goto("https://example.com")
await page.get_by_role("button", name="Start here").click()
```

An example with a custom callback on every actionability check. It uses a `<body>` locator that is always visible,
so the handler is called before every actionability check. It is important to specify `no_wait_after`, because the
handler does not hide the `<body>` element.

```py
# Setup the handler.
async def handler():
  await page.evaluate("window.removeObstructionsForTestIfNeeded()")
await page.add_locator_handler(page.locator("body"), handler, no_wait_after=True)

# Write the test as usual.
await page.goto("https://example.com")
await page.get_by_role("button", name="Start here").click()
```

Handler takes the original locator as an argument. You can also automatically remove the handler after a number of
invocations by setting `times`:

```py
async def handler(locator):
  await locator.click()
await page.add_locator_handler(page.get_by_label("Close"), handler, times=1)
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `locator` | Locator | Locator that triggers the handler. |
| `handler` | Union[Callable[[Locator], Any], Callable[[], Any]] | Function that should be run once `locator` appears. This function should get rid of the element that blocks actions like click. |
| `no_wait_after` | Union[bool, None] | By default, after calling the handler Playwright will wait until the overlay becomes hidden, and only then Playwright will continue with the action/assertion that triggered the handler. This option allows to opt-out of this behavior, so that overlay can stay visible after the handler has run. |
| `times` | Union[int, None] | Specifies the maximum number of times this handler should be called. Unlimited by default. |

## add_script_tag

### 同步

```python signature
def add_script_tag(self, *, content: Optional[str] = None, path: Union[pathlib.Path, str, NoneType] = None, type: Optional[str] = None, url: Optional[str] = None) -> 'ElementHandle'
```

Page.add_script_tag

Adds a `<script>` tag into the page with the desired url or content. Returns the added tag when the script's onload
fires or when the script content was injected into frame.

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

Page.add_script_tag

Adds a `<script>` tag into the page with the desired url or content. Returns the added tag when the script's onload
fires or when the script content was injected into frame.

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

Page.add_style_tag

Adds a `<link rel="stylesheet">` tag into the page with the desired url or a `<style type="text/css">` tag with the
content. Returns the added tag when the stylesheet's onload fires or when the CSS content was injected into frame.

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

Page.add_style_tag

Adds a `<link rel="stylesheet">` tag into the page with the desired url or a `<style type="text/css">` tag with the
content. Returns the added tag when the stylesheet's onload fires or when the CSS content was injected into frame.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `content` | Union[str, None] | Raw CSS content to be injected into frame. |
| `path` | Union[pathlib.Path, str, None] | Path to the CSS file to be injected into frame. If `path` is a relative path, then it is resolved relative to the current working directory. |
| `url` | Union[str, None] | URL of the `<link>` tag. |

#### Returns
ElementHandle


## aria_snapshot

### 同步

```python signature
def aria_snapshot(self, *, boxes: Optional[bool] = None, depth: Optional[int] = None, mode: Optional[Literal['ai', 'default']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> str
```

Page.aria_snapshot

Captures the aria snapshot of the page. Read more about [aria snapshots](https://playwright.dev/python/docs/aria-snapshots).

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `boxes` | Union[bool, None] | When `true`, appends each element's bounding box as `[box=x,y,width,height]` to the snapshot. Coordinates are relative to the viewport, in CSS pixels, as returned by [`Element.getBoundingClientRect()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect). Defaults to `false`. |
| `depth` | Union[int, None] | When specified, limits the depth of the snapshot. |
| `mode` | Union["ai", "default", None] | When set to `"ai"`, returns a snapshot optimized for AI consumption: including element references like `[ref=e2]` and snapshots of `<iframe>`s. Defaults to `"default"`. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
str

### 异步

```python signature
async def aria_snapshot(self, *, boxes: Optional[bool] = None, depth: Optional[int] = None, mode: Optional[Literal['ai', 'default']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> str
```

Page.aria_snapshot

Captures the aria snapshot of the page. Read more about [aria snapshots](https://playwright.dev/python/docs/aria-snapshots).

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `boxes` | Union[bool, None] | When `true`, appends each element's bounding box as `[box=x,y,width,height]` to the snapshot. Coordinates are relative to the viewport, in CSS pixels, as returned by [`Element.getBoundingClientRect()`](https://developer.mozilla.org/en-US/docs/Web/API/Element/getBoundingClientRect). Defaults to `false`. |
| `depth` | Union[int, None] | When specified, limits the depth of the snapshot. |
| `mode` | Union["ai", "default", None] | When set to `"ai"`, returns a snapshot optimized for AI consumption: including element references like `[ref=e2]` and snapshots of `<iframe>`s. Defaults to `"default"`. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
str


## bring_to_front

### 同步

```python
def bring_to_front(self) -> None
```

Page.bring_to_front

Brings page to front (activates tab).

### 异步

```python
async def bring_to_front(self) -> None
```

Page.bring_to_front

Brings page to front (activates tab).


## cancel_pick_locator

### 同步

```python
def cancel_pick_locator(self) -> None
```

Page.cancel_pick_locator

Cancels an ongoing `page.pick_locator()` call by deactivating pick locator mode. If no pick locator mode is active,
this method is a no-op.

### 异步

```python
async def cancel_pick_locator(self) -> None
```

Page.cancel_pick_locator

Cancels an ongoing `page.pick_locator()` call by deactivating pick locator mode. If no pick locator mode is active,
this method is a no-op.


## check

### 同步

```python signature
def check(self, selector: str, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

Page.check

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

Page.check

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

## clear_console_messages

### 同步

```python
def clear_console_messages(self) -> None
```

Page.clear_console_messages

Clears all stored console messages from this page. Subsequent calls to `page.console_messages()` will only return
messages logged after the clear.

### 异步

```python
async def clear_console_messages(self) -> None
```

Page.clear_console_messages

Clears all stored console messages from this page. Subsequent calls to `page.console_messages()` will only return
messages logged after the clear.


## clear_page_errors

### 同步

```python
def clear_page_errors(self) -> None
```

Page.clear_page_errors

Clears all stored page errors from this page. Subsequent calls to `page.page_errors()` will only return errors
thrown after the clear.

### 异步

```python
async def clear_page_errors(self) -> None
```

Page.clear_page_errors

Clears all stored page errors from this page. Subsequent calls to `page.page_errors()` will only return errors
thrown after the clear.


## click

### 同步

```python signature
def click(self, selector: str, *, button: Optional[Literal['left', 'middle', 'right']] = None, click_count: Optional[int] = None, delay: Optional[float] = None, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

Page.click

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

Page.click

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

## clock

属性，直接读取；异步入口也不加 await。

```python signature
Page.clock: Clock
```

Page.clock

Playwright has ability to mock clock and passage of time.

#### Returns
Clock


## close

### 同步

```python signature
def close(self, *, reason: Optional[str] = None, run_before_unload: Optional[bool] = None) -> None
```

Page.close

If `run_before_unload` is `false`, does not run any unload handlers and waits for the page to be closed. If
`run_before_unload` is `true` the method will run unload handlers, but will **not** wait for the page to close.

By default, `page.close()` **does not** run `beforeunload` handlers.

**NOTE** if `run_before_unload` is passed as true, a `beforeunload` dialog might be summoned and should be handled
manually via `page.on('dialog')` event.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `reason` | Union[str, None] | The reason to be reported to the operations interrupted by the page closure. |
| `run_before_unload` | Union[bool, None] | Defaults to `false`. Whether to run the [before unload](https://developer.mozilla.org/en-US/docs/Web/Events/beforeunload) page handlers. |

### 异步

```python signature
async def close(self, *, reason: Optional[str] = None, run_before_unload: Optional[bool] = None) -> None
```

Page.close

If `run_before_unload` is `false`, does not run any unload handlers and waits for the page to be closed. If
`run_before_unload` is `true` the method will run unload handlers, but will **not** wait for the page to close.

By default, `page.close()` **does not** run `beforeunload` handlers.

**NOTE** if `run_before_unload` is passed as true, a `beforeunload` dialog might be summoned and should be handled
manually via `page.on('dialog')` event.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `reason` | Union[str, None] | The reason to be reported to the operations interrupted by the page closure. |
| `run_before_unload` | Union[bool, None] | Defaults to `false`. Whether to run the [before unload](https://developer.mozilla.org/en-US/docs/Web/Events/beforeunload) page handlers. |

## console_messages

### 同步

```python signature
def console_messages(self, *, filter: Optional[Literal['all', 'since-navigation']] = None) -> List[ForwardRef('ConsoleMessage')]
```

Page.console_messages

Returns up to (currently) 200 last console messages from this page. See `page.on('console')` for more details.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `filter` | Union["all", "since-navigation", None] | Controls which messages are returned: |

#### Returns
List[ConsoleMessage]

### 异步

```python signature
async def console_messages(self, *, filter: Optional[Literal['all', 'since-navigation']] = None) -> List[ForwardRef('ConsoleMessage')]
```

Page.console_messages

Returns up to (currently) 200 last console messages from this page. See `page.on('console')` for more details.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `filter` | Union["all", "since-navigation", None] | Controls which messages are returned: |

#### Returns
List[ConsoleMessage]


## content

### 同步

```python signature
def content(self, *, include_shadow: Optional[bool] = None) -> str
```

Page.content

Gets the full HTML contents of the page, including the doctype.

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

Page.content

Gets the full HTML contents of the page, including the doctype.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `include_shadow` | Union[bool, None] | When true, contents of open shadow roots are included as [declarative shadow DOM](https://developer.mozilla.org/en-US/docs/Web/API/Web_components/Using_shadow_DOM#declaratively_with_html), i.e. `<template shadowrootmode="open">` elements nested inside their host elements. Closed shadow roots are never included. Defaults to `false`. |

#### Returns
str


## context

属性，直接读取；异步入口也不加 await。

```python signature
Page.context: BrowserContext
```

Page.context

Get the browser context that the page belongs to.

#### Returns
BrowserContext


## dblclick

### 同步

```python signature
def dblclick(self, selector: str, *, button: Optional[Literal['left', 'middle', 'right']] = None, delay: Optional[float] = None, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

Page.dblclick

This method double clicks an element matching `selector` by performing the following steps:
1. Find an element matching `selector`. If there is none, wait until a matching element is attached to the DOM.
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the matched element, unless `force` option is set. If
   the element is detached during the checks, the whole action is retried.
1. Scroll the element into view if needed.
1. Use `page.mouse` to double click in the center of the element, or the specified `position`.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

**NOTE** `page.dblclick()` dispatches two `click` events and a single `dblclick` event.

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

Page.dblclick

This method double clicks an element matching `selector` by performing the following steps:
1. Find an element matching `selector`. If there is none, wait until a matching element is attached to the DOM.
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the matched element, unless `force` option is set. If
   the element is detached during the checks, the whole action is retried.
1. Scroll the element into view if needed.
1. Use `page.mouse` to double click in the center of the element, or the specified `position`.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

**NOTE** `page.dblclick()` dispatches two `click` events and a single `dblclick` event.

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

Page.dispatch_event

The snippet below dispatches the `click` event on the element. Regardless of the visibility state of the element,
`click` is dispatched. This is equivalent to calling
[element.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click).

**Usage**

```py
page.dispatch_event("button#submit", "click")
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
page.dispatch_event("#source", "dragstart", { "dataTransfer": data_transfer })
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

Page.dispatch_event

The snippet below dispatches the `click` event on the element. Regardless of the visibility state of the element,
`click` is dispatched. This is equivalent to calling
[element.click()](https://developer.mozilla.org/en-US/docs/Web/API/HTMLElement/click).

**Usage**

```py
await page.dispatch_event("button#submit", "click")
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
await page.dispatch_event("#source", "dragstart", { "dataTransfer": data_transfer })
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

Page.drag_and_drop

This method drags the source element to the target element. It will first move to the source element, perform a
`mousedown`, then move to the target element and perform a `mouseup`.

**Usage**

```py
page.drag_and_drop("#source", "#target")
# or specify exact positions relative to the top-left corners of the elements:
page.drag_and_drop(
  "#source",
  "#target",
  source_position={"x": 34, "y": 7},
  target_position={"x": 10, "y": 20}
)
```

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

Page.drag_and_drop

This method drags the source element to the target element. It will first move to the source element, perform a
`mousedown`, then move to the target element and perform a `mouseup`.

**Usage**

```py
await page.drag_and_drop("#source", "#target")
# or specify exact positions relative to the top-left corners of the elements:
await page.drag_and_drop(
  "#source",
  "#target",
  source_position={"x": 34, "y": 7},
  target_position={"x": 10, "y": 20}
)
```

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

## emulate_media

### 同步

```python signature
def emulate_media(self, *, color_scheme: Optional[Literal['dark', 'light', 'no-preference', 'null']] = None, contrast: Optional[Literal['more', 'no-preference', 'null']] = None, forced_colors: Optional[Literal['active', 'none', 'null']] = None, media: Optional[Literal['null', 'print', 'screen']] = None, reduced_motion: Optional[Literal['no-preference', 'null', 'reduce']] = None) -> None
```

Page.emulate_media

This method changes the `CSS media type` through the `media` argument, and/or the `'prefers-colors-scheme'` media
feature, using the `colorScheme` argument.

**Usage**

```py
page.evaluate("matchMedia('screen').matches")
# → True
page.evaluate("matchMedia('print').matches")
# → False

page.emulate_media(media="print")
page.evaluate("matchMedia('screen').matches")
# → False
page.evaluate("matchMedia('print').matches")
# → True

page.emulate_media()
page.evaluate("matchMedia('screen').matches")
# → True
page.evaluate("matchMedia('print').matches")
# → False
```

```py
page.emulate_media(color_scheme="dark")
page.evaluate("matchMedia('(prefers-color-scheme: dark)').matches")
# → True
page.evaluate("matchMedia('(prefers-color-scheme: light)').matches")
# → False
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `color_scheme` | Union["dark", "light", "no-preference", "null", None] | Emulates [prefers-colors-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) media feature, supported values are `'light'` and `'dark'`. Passing `'Null'` disables color scheme emulation. `'no-preference'` is deprecated. |
| `contrast` | Union["more", "no-preference", "null", None] |  |
| `forced_colors` | Union["active", "none", "null", None] |  |
| `media` | Union["null", "print", "screen", None] | Changes the CSS media type of the page. The only allowed values are `'Screen'`, `'Print'` and `'Null'`. Passing `'Null'` disables CSS media emulation. |
| `reduced_motion` | Union["no-preference", "null", "reduce", None] | Emulates `'prefers-reduced-motion'` media feature, supported values are `'reduce'`, `'no-preference'`. Passing `null` disables reduced motion emulation. |

### 异步

```python signature
async def emulate_media(self, *, color_scheme: Optional[Literal['dark', 'light', 'no-preference', 'null']] = None, contrast: Optional[Literal['more', 'no-preference', 'null']] = None, forced_colors: Optional[Literal['active', 'none', 'null']] = None, media: Optional[Literal['null', 'print', 'screen']] = None, reduced_motion: Optional[Literal['no-preference', 'null', 'reduce']] = None) -> None
```

Page.emulate_media

This method changes the `CSS media type` through the `media` argument, and/or the `'prefers-colors-scheme'` media
feature, using the `colorScheme` argument.

**Usage**

```py
await page.evaluate("matchMedia('screen').matches")
# → True
await page.evaluate("matchMedia('print').matches")
# → False

await page.emulate_media(media="print")
await page.evaluate("matchMedia('screen').matches")
# → False
await page.evaluate("matchMedia('print').matches")
# → True

await page.emulate_media()
await page.evaluate("matchMedia('screen').matches")
# → True
await page.evaluate("matchMedia('print').matches")
# → False
```

```py
await page.emulate_media(color_scheme="dark")
await page.evaluate("matchMedia('(prefers-color-scheme: dark)').matches")
# → True
await page.evaluate("matchMedia('(prefers-color-scheme: light)').matches")
# → False
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `color_scheme` | Union["dark", "light", "no-preference", "null", None] | Emulates [prefers-colors-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) media feature, supported values are `'light'` and `'dark'`. Passing `'Null'` disables color scheme emulation. `'no-preference'` is deprecated. |
| `contrast` | Union["more", "no-preference", "null", None] |  |
| `forced_colors` | Union["active", "none", "null", None] |  |
| `media` | Union["null", "print", "screen", None] | Changes the CSS media type of the page. The only allowed values are `'Screen'`, `'Print'` and `'Null'`. Passing `'Null'` disables CSS media emulation. |
| `reduced_motion` | Union["no-preference", "null", "reduce", None] | Emulates `'prefers-reduced-motion'` media feature, supported values are `'reduce'`, `'no-preference'`. Passing `null` disables reduced motion emulation. |

## eval_on_selector

### 同步

```python signature
def eval_on_selector(self, selector: str, expression: str, arg: Optional[Any] = None, *, strict: Optional[bool] = None) -> Any
```

Page.eval_on_selector

The method finds an element matching the specified selector within the page and passes it as a first argument to
`expression`. If no elements match the selector, the method throws an error. Returns the value of `expression`.

If `expression` returns a [Promise], then `page.eval_on_selector()` would wait for the promise to resolve and
return its value.

**Usage**

```py
search_value = page.eval_on_selector("#search", "el => el.value")
preload_href = page.eval_on_selector("link[rel=preload]", "el => el.href")
html = page.eval_on_selector(".main-container", "(e, suffix) => e.outer_html + suffix", "hello")
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

Page.eval_on_selector

The method finds an element matching the specified selector within the page and passes it as a first argument to
`expression`. If no elements match the selector, the method throws an error. Returns the value of `expression`.

If `expression` returns a [Promise], then `page.eval_on_selector()` would wait for the promise to resolve and
return its value.

**Usage**

```py
search_value = await page.eval_on_selector("#search", "el => el.value")
preload_href = await page.eval_on_selector("link[rel=preload]", "el => el.href")
html = await page.eval_on_selector(".main-container", "(e, suffix) => e.outer_html + suffix", "hello")
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

Page.eval_on_selector_all

The method finds all elements matching the specified selector within the page and passes an array of matched
elements as a first argument to `expression`. Returns the result of `expression` invocation.

If `expression` returns a [Promise], then `page.eval_on_selector_all()` would wait for the promise to resolve and
return its value.

**Usage**

```py
div_counts = page.eval_on_selector_all("div", "(divs, min) => divs.length >= min", 10)
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

Page.eval_on_selector_all

The method finds all elements matching the specified selector within the page and passes an array of matched
elements as a first argument to `expression`. Returns the result of `expression` invocation.

If `expression` returns a [Promise], then `page.eval_on_selector_all()` would wait for the promise to resolve and
return its value.

**Usage**

```py
div_counts = await page.eval_on_selector_all("div", "(divs, min) => divs.length >= min", 10)
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

Page.evaluate

Returns the value of the `expression` invocation.

If the function passed to the `page.evaluate()` returns a [Promise], then `page.evaluate()` would wait for the
promise to resolve and return its value.

If the function passed to the `page.evaluate()` returns a non-[Serializable] value, then `page.evaluate()` resolves
to `undefined`. Playwright also supports transferring some additional values that are not serializable by `JSON`:
`-0`, `NaN`, `Infinity`, `-Infinity`.

**Usage**

Passing argument to `expression`:

```py
result = page.evaluate("([x, y]) => Promise.resolve(x * y)", [7, 8])
print(result) # prints "56"
```

A string can also be passed in instead of a function:

```py
print(page.evaluate("1 + 2")) # prints "3"
x = 10
print(page.evaluate(f"1 + {x}")) # prints "11"
```

`ElementHandle` instances can be passed as an argument to the `page.evaluate()`:

```py
body_handle = page.evaluate_handle("document.body")
html = page.evaluate("([body, suffix]) => body.innerHTML + suffix", [body_handle, "hello"])
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

Page.evaluate

Returns the value of the `expression` invocation.

If the function passed to the `page.evaluate()` returns a [Promise], then `page.evaluate()` would wait for the
promise to resolve and return its value.

If the function passed to the `page.evaluate()` returns a non-[Serializable] value, then `page.evaluate()` resolves
to `undefined`. Playwright also supports transferring some additional values that are not serializable by `JSON`:
`-0`, `NaN`, `Infinity`, `-Infinity`.

**Usage**

Passing argument to `expression`:

```py
result = await page.evaluate("([x, y]) => Promise.resolve(x * y)", [7, 8])
print(result) # prints "56"
```

A string can also be passed in instead of a function:

```py
print(await page.evaluate("1 + 2")) # prints "3"
x = 10
print(await page.evaluate(f"1 + {x}")) # prints "11"
```

`ElementHandle` instances can be passed as an argument to the `page.evaluate()`:

```py
body_handle = await page.evaluate_handle("document.body")
html = await page.evaluate("([body, suffix]) => body.innerHTML + suffix", [body_handle, "hello"])
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

Page.evaluate_handle

Returns the value of the `expression` invocation as a `JSHandle`.

The only difference between `page.evaluate()` and `page.evaluate_handle()` is that `page.evaluate_handle()` returns
`JSHandle`.

If the function passed to the `page.evaluate_handle()` returns a [Promise], then `page.evaluate_handle()` would
wait for the promise to resolve and return its value.

**Usage**

```py
a_window_handle = page.evaluate_handle("Promise.resolve(window)")
a_window_handle # handle for the window object.
```

A string can also be passed in instead of a function:

```py
a_handle = page.evaluate_handle("document") # handle for the "document"
```

`JSHandle` instances can be passed as an argument to the `page.evaluate_handle()`:

```py
a_handle = page.evaluate_handle("document.body")
result_handle = page.evaluate_handle("body => body.innerHTML", a_handle)
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

Page.evaluate_handle

Returns the value of the `expression` invocation as a `JSHandle`.

The only difference between `page.evaluate()` and `page.evaluate_handle()` is that `page.evaluate_handle()` returns
`JSHandle`.

If the function passed to the `page.evaluate_handle()` returns a [Promise], then `page.evaluate_handle()` would
wait for the promise to resolve and return its value.

**Usage**

```py
a_window_handle = await page.evaluate_handle("Promise.resolve(window)")
a_window_handle # handle for the window object.
```

A string can also be passed in instead of a function:

```py
a_handle = await page.evaluate_handle("document") # handle for the "document"
```

`JSHandle` instances can be passed as an argument to the `page.evaluate_handle()`:

```py
a_handle = await page.evaluate_handle("document.body")
result_handle = await page.evaluate_handle("body => body.innerHTML", a_handle)
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


## expect_console_message

### 同步

```python signature
def expect_console_message(self, predicate: Optional[Callable[[ForwardRef('ConsoleMessage')], bool]] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('ConsoleMessage')]
```

Page.expect_console_message

Performs action and waits for a `ConsoleMessage` to be logged by in the page. If predicate is provided, it passes
`ConsoleMessage` value into the `predicate` function and waits for `predicate(message)` to return a truthy value.
Will throw an error if the page is closed before the `page.on('console')` event is fired.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `predicate` | Union[Callable[[ConsoleMessage], bool], None] | Receives the `ConsoleMessage` object and resolves to truthy value when the waiting should resolve. |
| `timeout` | Union[float, None] | Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()`. |

#### Returns
EventContextManager[ConsoleMessage]

### 异步

```python signature
def expect_console_message(self, predicate: Optional[Callable[[ForwardRef('ConsoleMessage')], bool]] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('ConsoleMessage')]
```

Page.expect_console_message

Performs action and waits for a `ConsoleMessage` to be logged by in the page. If predicate is provided, it passes
`ConsoleMessage` value into the `predicate` function and waits for `predicate(message)` to return a truthy value.
Will throw an error if the page is closed before the `page.on('console')` event is fired.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `predicate` | Union[Callable[[ConsoleMessage], bool], None] | Receives the `ConsoleMessage` object and resolves to truthy value when the waiting should resolve. |
| `timeout` | Union[float, None] | Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()`. |

#### Returns
EventContextManager[ConsoleMessage]


## expect_download

### 同步

```python signature
def expect_download(self, predicate: Optional[Callable[[ForwardRef('Download')], bool]] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Download')]
```

Page.expect_download

Performs action and waits for a new `Download`. If predicate is provided, it passes `Download` value into the
`predicate` function and waits for `predicate(download)` to return a truthy value. Will throw an error if the page
is closed before the download event is fired.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `predicate` | Union[Callable[[Download], bool], None] | Receives the `Download` object and resolves to truthy value when the waiting should resolve. |
| `timeout` | Union[float, None] | Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()`. |

#### Returns
EventContextManager[Download]

### 异步

```python signature
def expect_download(self, predicate: Optional[Callable[[ForwardRef('Download')], bool]] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Download')]
```

Page.expect_download

Performs action and waits for a new `Download`. If predicate is provided, it passes `Download` value into the
`predicate` function and waits for `predicate(download)` to return a truthy value. Will throw an error if the page
is closed before the download event is fired.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `predicate` | Union[Callable[[Download], bool], None] | Receives the `Download` object and resolves to truthy value when the waiting should resolve. |
| `timeout` | Union[float, None] | Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()`. |

#### Returns
EventContextManager[Download]


## expect_event

### 同步

```python signature
def expect_event(self, event: str, predicate: Optional[Callable] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> patchright._impl._sync_base.EventContextManager
```

支持的重载：

```python signature
def expect_event(self, event: Literal['close'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Page')]
def expect_event(self, event: Literal['console'], predicate: Optional[Callable[[ForwardRef('ConsoleMessage')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('ConsoleMessage')]
def expect_event(self, event: Literal['crash'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Page')]
def expect_event(self, event: Literal['dialog'], predicate: Optional[Callable[[ForwardRef('Dialog')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Dialog')]
def expect_event(self, event: Literal['dialogclosed'], predicate: Optional[Callable[[ForwardRef('Dialog')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Dialog')]
def expect_event(self, event: Literal['domcontentloaded'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Page')]
def expect_event(self, event: Literal['download'], predicate: Optional[Callable[[ForwardRef('Download')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Download')]
def expect_event(self, event: Literal['filechooser'], predicate: Optional[Callable[[ForwardRef('FileChooser')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('FileChooser')]
def expect_event(self, event: Literal['frameattached'], predicate: Optional[Callable[[ForwardRef('Frame')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Frame')]
def expect_event(self, event: Literal['framedetached'], predicate: Optional[Callable[[ForwardRef('Frame')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Frame')]
def expect_event(self, event: Literal['framenavigated'], predicate: Optional[Callable[[ForwardRef('Frame')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Frame')]
def expect_event(self, event: Literal['load'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Page')]
def expect_event(self, event: Literal['pageerror'], predicate: Optional[Callable[[ForwardRef('Error')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Error')]
def expect_event(self, event: Literal['popup'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Page')]
def expect_event(self, event: Literal['request'], predicate: Optional[Callable[[ForwardRef('Request')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Request')]
def expect_event(self, event: Literal['requestfailed'], predicate: Optional[Callable[[ForwardRef('Request')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Request')]
def expect_event(self, event: Literal['requestfinished'], predicate: Optional[Callable[[ForwardRef('Request')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Request')]
def expect_event(self, event: Literal['response'], predicate: Optional[Callable[[ForwardRef('Response')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Response')]
def expect_event(self, event: Literal['websocket'], predicate: Optional[Callable[[ForwardRef('WebSocket')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('WebSocket')]
def expect_event(self, event: Literal['worker'], predicate: Optional[Callable[[ForwardRef('Worker')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Worker')]
def expect_event(self, event: str, predicate: Optional[Callable[..., bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[typing.Any]
```

Page.expect_event

Waits for event to fire and passes its value into the predicate function. Returns when the predicate returns truthy
value. Will throw an error if the page is closed before the event is fired. Returns the event data value.

**Usage**

```py
with page.expect_event("framenavigated") as event_info:
    page.get_by_role("button")
frame = event_info.value
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `event` | str | Event name, same one typically passed into `*.on(event)`. |
| `predicate` | Union[Callable, None] | Receives the event data and resolves to truthy value when the waiting should resolve. |
| `timeout` | Union[float, None] | Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()`. |

#### Returns
EventContextManager

### 异步

```python signature
def expect_event(self, event: str, predicate: Optional[Callable] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> patchright._impl._async_base.AsyncEventContextManager
```

支持的重载：

```python signature
def expect_event(self, event: Literal['close'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Page')]
def expect_event(self, event: Literal['console'], predicate: Optional[Callable[[ForwardRef('ConsoleMessage')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('ConsoleMessage')]
def expect_event(self, event: Literal['crash'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Page')]
def expect_event(self, event: Literal['dialog'], predicate: Optional[Callable[[ForwardRef('Dialog')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Dialog')]
def expect_event(self, event: Literal['dialogclosed'], predicate: Optional[Callable[[ForwardRef('Dialog')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Dialog')]
def expect_event(self, event: Literal['domcontentloaded'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Page')]
def expect_event(self, event: Literal['download'], predicate: Optional[Callable[[ForwardRef('Download')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Download')]
def expect_event(self, event: Literal['filechooser'], predicate: Optional[Callable[[ForwardRef('FileChooser')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('FileChooser')]
def expect_event(self, event: Literal['frameattached'], predicate: Optional[Callable[[ForwardRef('Frame')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Frame')]
def expect_event(self, event: Literal['framedetached'], predicate: Optional[Callable[[ForwardRef('Frame')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Frame')]
def expect_event(self, event: Literal['framenavigated'], predicate: Optional[Callable[[ForwardRef('Frame')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Frame')]
def expect_event(self, event: Literal['load'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Page')]
def expect_event(self, event: Literal['pageerror'], predicate: Optional[Callable[[ForwardRef('Error')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Error')]
def expect_event(self, event: Literal['popup'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Page')]
def expect_event(self, event: Literal['request'], predicate: Optional[Callable[[ForwardRef('Request')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Request')]
def expect_event(self, event: Literal['requestfailed'], predicate: Optional[Callable[[ForwardRef('Request')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Request')]
def expect_event(self, event: Literal['requestfinished'], predicate: Optional[Callable[[ForwardRef('Request')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Request')]
def expect_event(self, event: Literal['response'], predicate: Optional[Callable[[ForwardRef('Response')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Response')]
def expect_event(self, event: Literal['websocket'], predicate: Optional[Callable[[ForwardRef('WebSocket')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('WebSocket')]
def expect_event(self, event: Literal['worker'], predicate: Optional[Callable[[ForwardRef('Worker')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Worker')]
def expect_event(self, event: str, predicate: Optional[Callable[..., bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[typing.Any]
```

Page.expect_event

Waits for event to fire and passes its value into the predicate function. Returns when the predicate returns truthy
value. Will throw an error if the page is closed before the event is fired. Returns the event data value.

**Usage**

```py
async with page.expect_event("framenavigated") as event_info:
    await page.get_by_role("button")
frame = await event_info.value
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `event` | str | Event name, same one typically passed into `*.on(event)`. |
| `predicate` | Union[Callable, None] | Receives the event data and resolves to truthy value when the waiting should resolve. |
| `timeout` | Union[float, None] | Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()`. |

#### Returns
EventContextManager


## expect_file_chooser

### 同步

```python signature
def expect_file_chooser(self, predicate: Optional[Callable[[ForwardRef('FileChooser')], bool]] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('FileChooser')]
```

Page.expect_file_chooser

Performs action and waits for a new `FileChooser` to be created. If predicate is provided, it passes `FileChooser`
value into the `predicate` function and waits for `predicate(fileChooser)` to return a truthy value. Will throw an
error if the page is closed before the file chooser is opened.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `predicate` | Union[Callable[[FileChooser], bool], None] | Receives the `FileChooser` object and resolves to truthy value when the waiting should resolve. |
| `timeout` | Union[float, None] | Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()`. |

#### Returns
EventContextManager[FileChooser]

### 异步

```python signature
def expect_file_chooser(self, predicate: Optional[Callable[[ForwardRef('FileChooser')], bool]] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('FileChooser')]
```

Page.expect_file_chooser

Performs action and waits for a new `FileChooser` to be created. If predicate is provided, it passes `FileChooser`
value into the `predicate` function and waits for `predicate(fileChooser)` to return a truthy value. Will throw an
error if the page is closed before the file chooser is opened.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `predicate` | Union[Callable[[FileChooser], bool], None] | Receives the `FileChooser` object and resolves to truthy value when the waiting should resolve. |
| `timeout` | Union[float, None] | Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()`. |

#### Returns
EventContextManager[FileChooser]


## expect_navigation

### 同步

```python signature
def expect_navigation(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None, url: Union[str, Pattern[str], Callable[[str], bool], NoneType] = None, wait_until: Optional[Literal['commit', 'domcontentloaded', 'load', 'networkidle']] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Response')]
```

Page.expect_navigation

Waits for the main frame navigation and returns the main resource response. In case of multiple redirects, the
navigation will resolve with the response of the last redirect. In case of navigation to a different anchor or
navigation due to History API usage, the navigation will resolve with `null`.

**Usage**

This resolves when the page navigates to a new URL or reloads. It is useful for when you run code which will
indirectly cause the page to navigate. e.g. The click target has an `onclick` handler that triggers navigation from
a `setTimeout`. Consider this example:

```py
with page.expect_navigation():
    # This action triggers the navigation after a timeout.
    page.get_by_text("Navigate after timeout").click()
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

Page.expect_navigation

Waits for the main frame navigation and returns the main resource response. In case of multiple redirects, the
navigation will resolve with the response of the last redirect. In case of navigation to a different anchor or
navigation due to History API usage, the navigation will resolve with `null`.

**Usage**

This resolves when the page navigates to a new URL or reloads. It is useful for when you run code which will
indirectly cause the page to navigate. e.g. The click target has an `onclick` handler that triggers navigation from
a `setTimeout`. Consider this example:

```py
async with page.expect_navigation():
    # This action triggers the navigation after a timeout.
    await page.get_by_text("Navigate after timeout").click()
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


## expect_popup

### 同步

```python signature
def expect_popup(self, predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Page')]
```

Page.expect_popup

Performs action and waits for a popup `Page`. If predicate is provided, it passes [Popup] value into the
`predicate` function and waits for `predicate(page)` to return a truthy value. Will throw an error if the page is
closed before the popup event is fired.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `predicate` | Union[Callable[[Page], bool], None] | Receives the `Page` object and resolves to truthy value when the waiting should resolve. |
| `timeout` | Union[float, None] | Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()`. |

#### Returns
EventContextManager[Page]

### 异步

```python signature
def expect_popup(self, predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Page')]
```

Page.expect_popup

Performs action and waits for a popup `Page`. If predicate is provided, it passes [Popup] value into the
`predicate` function and waits for `predicate(page)` to return a truthy value. Will throw an error if the page is
closed before the popup event is fired.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `predicate` | Union[Callable[[Page], bool], None] | Receives the `Page` object and resolves to truthy value when the waiting should resolve. |
| `timeout` | Union[float, None] | Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()`. |

#### Returns
EventContextManager[Page]


## expect_request

### 同步

```python signature
def expect_request(self, url_or_predicate: Union[str, Pattern[str], Callable[[ForwardRef('Request')], bool]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Request')]
```

Page.expect_request

Waits for the matching request and returns it. See [waiting for event](https://playwright.dev/python/docs/events#waiting-for-event) for more
details about events.

**Usage**

```py
with page.expect_request("http://example.com/resource") as first:
    page.get_by_text("trigger request").click()
first_request = first.value

# or with a lambda
with page.expect_request(lambda request: request.url == "http://example.com" and request.method == "get") as second:
    page.get_by_text("trigger request").click()
second_request = second.value
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url_or_predicate` | Union[Callable[[Request], bool], Pattern[str], str] | Request URL string, regex or predicate receiving `Request` object. When a `base_url` via the context options was provided and the passed URL is a path, it gets merged via the [`new URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) constructor. |
| `timeout` | Union[float, None] | Maximum wait time in milliseconds, defaults to 30 seconds, pass `0` to disable the timeout. The default value can be changed by using the `page.set_default_timeout()` method. |

#### Returns
EventContextManager[Request]

### 异步

```python signature
def expect_request(self, url_or_predicate: Union[str, Pattern[str], Callable[[ForwardRef('Request')], Union[bool, Awaitable[bool]]]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Request')]
```

Page.expect_request

Waits for the matching request and returns it. See [waiting for event](https://playwright.dev/python/docs/events#waiting-for-event) for more
details about events.

**Usage**

```py
async with page.expect_request("http://example.com/resource") as first:
    await page.get_by_text("trigger request").click()
first_request = await first.value

# or with a lambda
async with page.expect_request(lambda request: request.url == "http://example.com" and request.method == "get") as second:
    await page.get_by_text("trigger request").click()
second_request = await second.value
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url_or_predicate` | Union[Callable[[Request], Union[bool, typing.Awaitable[bool]]], Pattern[str], str] | Request URL string, regex or predicate receiving `Request` object. When a `base_url` via the context options was provided and the passed URL is a path, it gets merged via the [`new URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) constructor. |
| `timeout` | Union[float, None] | Maximum wait time in milliseconds, defaults to 30 seconds, pass `0` to disable the timeout. The default value can be changed by using the `page.set_default_timeout()` method. |

#### Returns
EventContextManager[Request]


## expect_request_finished

### 同步

```python signature
def expect_request_finished(self, predicate: Optional[Callable[[ForwardRef('Request')], bool]] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Request')]
```

Page.expect_request_finished

Performs action and waits for a `Request` to finish loading. If predicate is provided, it passes `Request` value
into the `predicate` function and waits for `predicate(request)` to return a truthy value. Will throw an error if
the page is closed before the `page.on('requestfinished')` event is fired.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `predicate` | Union[Callable[[Request], bool], None] | Receives the `Request` object and resolves to truthy value when the waiting should resolve. |
| `timeout` | Union[float, None] | Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()`. |

#### Returns
EventContextManager[Request]

### 异步

```python signature
def expect_request_finished(self, predicate: Optional[Callable[[ForwardRef('Request')], bool]] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Request')]
```

Page.expect_request_finished

Performs action and waits for a `Request` to finish loading. If predicate is provided, it passes `Request` value
into the `predicate` function and waits for `predicate(request)` to return a truthy value. Will throw an error if
the page is closed before the `page.on('requestfinished')` event is fired.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `predicate` | Union[Callable[[Request], bool], None] | Receives the `Request` object and resolves to truthy value when the waiting should resolve. |
| `timeout` | Union[float, None] | Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()`. |

#### Returns
EventContextManager[Request]


## expect_response

### 同步

```python signature
def expect_response(self, url_or_predicate: Union[str, Pattern[str], Callable[[ForwardRef('Response')], bool]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Response')]
```

Page.expect_response

Returns the matched response. See [waiting for event](https://playwright.dev/python/docs/events#waiting-for-event) for more details about
events.

**Usage**

```py
with page.expect_response("https://example.com/resource") as response_info:
    page.get_by_text("trigger response").click()
response = response_info.value
return response.ok

# or with a lambda
with page.expect_response(lambda response: response.url == "https://example.com" and response.status == 200 and response.request.method == "get") as response_info:
    page.get_by_text("trigger response").click()
response = response_info.value
return response.ok
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url_or_predicate` | Union[Callable[[Response], bool], Pattern[str], str] | Request URL string, regex or predicate receiving `Response` object. When a `base_url` via the context options was provided and the passed URL is a path, it gets merged via the [`new URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) constructor. |
| `timeout` | Union[float, None] | Maximum wait time in milliseconds, defaults to 30 seconds, pass `0` to disable the timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
EventContextManager[Response]

### 异步

```python signature
def expect_response(self, url_or_predicate: Union[str, Pattern[str], Callable[[ForwardRef('Response')], Union[bool, Awaitable[bool]]]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Response')]
```

Page.expect_response

Returns the matched response. See [waiting for event](https://playwright.dev/python/docs/events#waiting-for-event) for more details about
events.

**Usage**

```py
async with page.expect_response("https://example.com/resource") as response_info:
    await page.get_by_text("trigger response").click()
response = await response_info.value
return response.ok

# or with a lambda
async with page.expect_response(lambda response: response.url == "https://example.com" and response.status == 200 and response.request.method == "get") as response_info:
    await page.get_by_text("trigger response").click()
response = await response_info.value
return response.ok
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url_or_predicate` | Union[Callable[[Response], Union[bool, typing.Awaitable[bool]]], Pattern[str], str] | Request URL string, regex or predicate receiving `Response` object. When a `base_url` via the context options was provided and the passed URL is a path, it gets merged via the [`new URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) constructor. |
| `timeout` | Union[float, None] | Maximum wait time in milliseconds, defaults to 30 seconds, pass `0` to disable the timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
EventContextManager[Response]


## expect_websocket

### 同步

```python signature
def expect_websocket(self, predicate: Optional[Callable[[ForwardRef('WebSocket')], bool]] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('WebSocket')]
```

Page.expect_websocket

Performs action and waits for a new `WebSocket`. If predicate is provided, it passes `WebSocket` value into the
`predicate` function and waits for `predicate(webSocket)` to return a truthy value. Will throw an error if the page
is closed before the WebSocket event is fired.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `predicate` | Union[Callable[[WebSocket], bool], None] | Receives the `WebSocket` object and resolves to truthy value when the waiting should resolve. |
| `timeout` | Union[float, None] | Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()`. |

#### Returns
EventContextManager[WebSocket]

### 异步

```python signature
def expect_websocket(self, predicate: Optional[Callable[[ForwardRef('WebSocket')], bool]] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('WebSocket')]
```

Page.expect_websocket

Performs action and waits for a new `WebSocket`. If predicate is provided, it passes `WebSocket` value into the
`predicate` function and waits for `predicate(webSocket)` to return a truthy value. Will throw an error if the page
is closed before the WebSocket event is fired.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `predicate` | Union[Callable[[WebSocket], bool], None] | Receives the `WebSocket` object and resolves to truthy value when the waiting should resolve. |
| `timeout` | Union[float, None] | Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()`. |

#### Returns
EventContextManager[WebSocket]


## expect_worker

### 同步

```python signature
def expect_worker(self, predicate: Optional[Callable[[ForwardRef('Worker')], bool]] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Worker')]
```

Page.expect_worker

Performs action and waits for a new `Worker`. If predicate is provided, it passes `Worker` value into the
`predicate` function and waits for `predicate(worker)` to return a truthy value. Will throw an error if the page is
closed before the worker event is fired.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `predicate` | Union[Callable[[Worker], bool], None] | Receives the `Worker` object and resolves to truthy value when the waiting should resolve. |
| `timeout` | Union[float, None] | Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()`. |

#### Returns
EventContextManager[Worker]

### 异步

```python signature
def expect_worker(self, predicate: Optional[Callable[[ForwardRef('Worker')], bool]] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Worker')]
```

Page.expect_worker

Performs action and waits for a new `Worker`. If predicate is provided, it passes `Worker` value into the
`predicate` function and waits for `predicate(worker)` to return a truthy value. Will throw an error if the page is
closed before the worker event is fired.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `predicate` | Union[Callable[[Worker], bool], None] | Receives the `Worker` object and resolves to truthy value when the waiting should resolve. |
| `timeout` | Union[float, None] | Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()`. |

#### Returns
EventContextManager[Worker]


## expose_binding

### 同步

```python
def expose_binding(self, name: str, callback: Callable) -> 'SyncContextManager'
```

Page.expose_binding

The method adds a function called `name` on the `window` object of every frame in this page. When called, the
function executes `callback` and returns a [Promise] which resolves to the return value of `callback`. If the
`callback` returns a [Promise], it will be awaited.

The first argument of the `callback` function contains information about the caller: `{ browserContext:
BrowserContext, page: Page, frame: Frame }`.

See `browser_context.expose_binding()` for the context-wide version.

**NOTE** Functions installed via `page.expose_binding()` survive navigations.

**Usage**

An example of exposing page URL to all frames in a page:

```py
from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    webkit = playwright.webkit
    browser = webkit.launch(headless=False)
    context = browser.new_context()
    page = context.new_page()
    page.expose_binding("pageURL", lambda source: source["page"].url)
    page.set_content("""
    <script>
      async function onClick() {
        document.querySelector('div').textContent = await window.pageURL();
      }
    </script>
    <button onclick="onClick()">Click me</button>
    <div></div>
    """)
    page.click("button")

with sync_playwright() as playwright:
    run(playwright)
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | Name of the function on the window object. |
| `callback` | Callable | Callback function that will be called in the Playwright's context. |

#### Returns
SyncContextManager

### 异步

```python
async def expose_binding(self, name: str, callback: Callable) -> 'AsyncContextManager'
```

Page.expose_binding

The method adds a function called `name` on the `window` object of every frame in this page. When called, the
function executes `callback` and returns a [Promise] which resolves to the return value of `callback`. If the
`callback` returns a [Promise], it will be awaited.

The first argument of the `callback` function contains information about the caller: `{ browserContext:
BrowserContext, page: Page, frame: Frame }`.

See `browser_context.expose_binding()` for the context-wide version.

**NOTE** Functions installed via `page.expose_binding()` survive navigations.

**Usage**

An example of exposing page URL to all frames in a page:

```py
import asyncio
from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    webkit = playwright.webkit
    browser = await webkit.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.expose_binding("pageURL", lambda source: source["page"].url)
    await page.set_content("""
    <script>
      async function onClick() {
        document.querySelector('div').textContent = await window.pageURL();
      }
    </script>
    <button onclick="onClick()">Click me</button>
    <div></div>
    """)
    await page.click("button")

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | Name of the function on the window object. |
| `callback` | Callable | Callback function that will be called in the Playwright's context. |

#### Returns
AsyncContextManager


## expose_function

### 同步

```python
def expose_function(self, name: str, callback: Callable) -> 'SyncContextManager'
```

Page.expose_function

The method adds a function called `name` on the `window` object of every frame in the page. When called, the
function executes `callback` and returns a [Promise] which resolves to the return value of `callback`.

If the `callback` returns a [Promise], it will be awaited.

See `browser_context.expose_function()` for context-wide exposed function.

**NOTE** Functions installed via `page.expose_function()` survive navigations.

**Usage**

An example of adding a `sha256` function to the page:

```py
import hashlib
from playwright.sync_api import sync_playwright, Playwright

def sha256(text):
    m = hashlib.sha256()
    m.update(bytes(text, "utf8"))
    return m.hexdigest()

def run(playwright: Playwright):
    webkit = playwright.webkit
    browser = webkit.launch(headless=False)
    page = browser.new_page()
    page.expose_function("sha256", sha256)
    page.set_content("""
        <script>
          async function onClick() {
            document.querySelector('div').textContent = await window.sha256('PLAYWRIGHT');
          }
        </script>
        <button onclick="onClick()">Click me</button>
        <div></div>
    """)
    page.click("button")

with sync_playwright() as playwright:
    run(playwright)
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | Name of the function on the window object |
| `callback` | Callable | Callback function which will be called in Playwright's context. |

#### Returns
SyncContextManager

### 异步

```python
async def expose_function(self, name: str, callback: Callable) -> 'AsyncContextManager'
```

Page.expose_function

The method adds a function called `name` on the `window` object of every frame in the page. When called, the
function executes `callback` and returns a [Promise] which resolves to the return value of `callback`.

If the `callback` returns a [Promise], it will be awaited.

See `browser_context.expose_function()` for context-wide exposed function.

**NOTE** Functions installed via `page.expose_function()` survive navigations.

**Usage**

An example of adding a `sha256` function to the page:

```py
import asyncio
import hashlib
from playwright.async_api import async_playwright, Playwright

def sha256(text):
    m = hashlib.sha256()
    m.update(bytes(text, "utf8"))
    return m.hexdigest()

async def run(playwright: Playwright):
    webkit = playwright.webkit
    browser = await webkit.launch(headless=False)
    page = await browser.new_page()
    await page.expose_function("sha256", sha256)
    await page.set_content("""
        <script>
          async function onClick() {
            document.querySelector('div').textContent = await window.sha256('PLAYWRIGHT');
          }
        </script>
        <button onclick="onClick()">Click me</button>
        <div></div>
    """)
    await page.click("button")

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | Name of the function on the window object |
| `callback` | Callable | Callback function which will be called in Playwright's context. |

#### Returns
AsyncContextManager


## fill

### 同步

```python signature
def fill(self, selector: str, value: str, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Page.fill

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

Page.fill

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

Page.focus

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

Page.focus

This method fetches an element with `selector` and focuses it. If there's no element matching `selector`, the
method waits until a matching element appears in the DOM.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

## frame

### 同步

```python signature
def frame(self, name: Optional[str] = None, *, url: Union[str, Pattern[str], Callable[[str], bool], NoneType] = None) -> Optional[ForwardRef('Frame')]
```

Page.frame

Returns frame matching the specified criteria. Either `name` or `url` must be specified.

**Usage**

```py
frame = page.frame(name="frame-name")
```

```py
frame = page.frame(url=r".*domain.*")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | Union[str, None] | Frame name specified in the `iframe`'s `name` attribute. Optional. |
| `url` | Union[Callable[[str], bool], Pattern[str], str, None] | A glob pattern, regex pattern or predicate receiving frame's `url` as a [URL] object. Optional. |

#### Returns
Union[Frame, None]

### 异步

```python signature
def frame(self, name: Optional[str] = None, *, url: Union[str, Pattern[str], Callable[[str], bool], NoneType] = None) -> Optional[ForwardRef('Frame')]
```

Page.frame

Returns frame matching the specified criteria. Either `name` or `url` must be specified.

**Usage**

```py
frame = page.frame(name="frame-name")
```

```py
frame = page.frame(url=r".*domain.*")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | Union[str, None] | Frame name specified in the `iframe`'s `name` attribute. Optional. |
| `url` | Union[Callable[[str], bool], Pattern[str], str, None] | A glob pattern, regex pattern or predicate receiving frame's `url` as a [URL] object. Optional. |

#### Returns
Union[Frame, None]


## frame_locator

### 同步

```python
def frame_locator(self, selector: Optional[str] = None) -> 'FrameLocator'
```

Page.frame_locator

When working with iframes, you can create a frame locator that will enter the iframe and allow selecting elements
in that iframe.

When called without `selector`, the search starts in any frame on the page - the main frame or any of the iframes -
so that you don't need to locate each iframe first. Note that the rest of the locator is resolved inside a single
frame, just like any other locator. If it matches elements inside multiple frames, an error is thrown.

**Usage**

Following snippet locates element with text "Submit" in the iframe with id `my-frame`, like `<iframe
id="my-frame">`:

```py
locator = page.frame_locator("#my-iframe").get_by_text("Submit")
locator.click()
```

Following snippet locates a button, either in the main frame or in one of the iframes:

```py
locator = page.frame_locator().get_by_role("button")
locator.click()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | Union[str, None] | A selector that matches the frame element. When not specified, locator is matched in any frame on the page. |

#### Returns
FrameLocator

### 异步

```python
def frame_locator(self, selector: Optional[str] = None) -> 'FrameLocator'
```

Page.frame_locator

When working with iframes, you can create a frame locator that will enter the iframe and allow selecting elements
in that iframe.

When called without `selector`, the search starts in any frame on the page - the main frame or any of the iframes -
so that you don't need to locate each iframe first. Note that the rest of the locator is resolved inside a single
frame, just like any other locator. If it matches elements inside multiple frames, an error is thrown.

**Usage**

Following snippet locates element with text "Submit" in the iframe with id `my-frame`, like `<iframe
id="my-frame">`:

```py
locator = page.frame_locator("#my-iframe").get_by_text("Submit")
await locator.click()
```

Following snippet locates a button, either in the main frame or in one of the iframes:

```py
locator = page.frame_locator().get_by_role("button")
await locator.click()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | Union[str, None] | A selector that matches the frame element. When not specified, locator is matched in any frame on the page. |

#### Returns
FrameLocator


## frames

属性，直接读取；异步入口也不加 await。

```python signature
Page.frames: typing.List[ForwardRef('Frame')]
```

Page.frames

An array of all frames attached to the page.

#### Returns
List[Frame]


## get_attribute

### 同步

```python signature
def get_attribute(self, selector: str, name: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Optional[str]
```

Page.get_attribute

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

Page.get_attribute

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

Page.get_by_alt_text

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

Page.get_by_alt_text

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

Page.get_by_label

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

Page.get_by_label

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

Page.get_by_placeholder

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

Page.get_by_placeholder

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


## get_by_ref

### 同步

```python
def get_by_ref(self, ref: str) -> 'Locator'
```

Page.get_by_ref

Locate element by its aria ref. Refs like `[ref=e2]` are reported by `page.aria_snapshot()` when called with the
`"ai"` mode, and resolve against the latest snapshot taken in the element's frame.

**Usage**

Consider the following aria snapshot.

You can locate the button by its ref:

```py
page.get_by_ref("e2").click()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `ref` | str | Aria ref of the element, for example `e2` or `f1e3`. |

#### Returns
Locator

### 异步

```python
def get_by_ref(self, ref: str) -> 'Locator'
```

Page.get_by_ref

Locate element by its aria ref. Refs like `[ref=e2]` are reported by `page.aria_snapshot()` when called with the
`"ai"` mode, and resolve against the latest snapshot taken in the element's frame.

**Usage**

Consider the following aria snapshot.

You can locate the button by its ref:

```py
await page.get_by_ref("e2").click()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `ref` | str | Aria ref of the element, for example `e2` or `f1e3`. |

#### Returns
Locator


## get_by_role

### 同步

```python signature
def get_by_role(self, role: Literal['alert', 'alertdialog', 'application', 'article', 'banner', 'blockquote', 'button', 'caption', 'cell', 'checkbox', 'code', 'columnheader', 'combobox', 'complementary', 'contentinfo', 'definition', 'deletion', 'dialog', 'directory', 'document', 'emphasis', 'feed', 'figure', 'form', 'generic', 'grid', 'gridcell', 'group', 'heading', 'img', 'insertion', 'link', 'list', 'listbox', 'listitem', 'log', 'main', 'marquee', 'math', 'menu', 'menubar', 'menuitem', 'menuitemcheckbox', 'menuitemradio', 'meter', 'navigation', 'none', 'note', 'option', 'paragraph', 'presentation', 'progressbar', 'radio', 'radiogroup', 'region', 'row', 'rowgroup', 'rowheader', 'scrollbar', 'search', 'searchbox', 'separator', 'slider', 'spinbutton', 'status', 'strong', 'subscript', 'superscript', 'switch', 'tab', 'table', 'tablist', 'tabpanel', 'term', 'textbox', 'time', 'timer', 'toolbar', 'tooltip', 'tree', 'treegrid', 'treeitem'], *, checked: Optional[bool] = None, description: Union[str, Pattern[str], NoneType] = None, disabled: Optional[bool] = None, exact: Optional[bool] = None, expanded: Optional[bool] = None, include_hidden: Optional[bool] = None, level: Optional[int] = None, name: Union[str, Pattern[str], NoneType] = None, pressed: Optional[bool] = None, selected: Optional[bool] = None) -> 'Locator'
```

Page.get_by_role

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

Page.get_by_role

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

Page.get_by_test_id

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

Page.get_by_test_id

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

Page.get_by_text

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

Page.get_by_text

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

Page.get_by_title

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

Page.get_by_title

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


## go_back

### 同步

```python signature
def go_back(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None, wait_until: Optional[Literal['commit', 'domcontentloaded', 'load', 'networkidle']] = None) -> Optional[ForwardRef('Response')]
```

Page.go_back

Returns the main resource response. In case of multiple redirects, the navigation will resolve with the response of
the last redirect. If cannot go back, returns `null`.

Navigate to the previous page in history.

**NOTE** **Testing Back/Forward Cache (BFCache) is not supported.** By default, Playwright disables the
Back/Forward Cache across all browsers. Even if explicitly enabled, Playwright's internal state relies on
network-level navigation events. Because BFCache restores unfreeze the DOM without firing these events, using
`page.goBack()` or `page.goForward()` to trigger a BFCache restore will result in timeouts and a desynchronized
`Page` state.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_navigation_timeout()`, `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or `page.set_default_timeout()` methods. |
| `wait_until` | Union["commit", "domcontentloaded", "load", "networkidle", None] | When to consider operation succeeded, defaults to `load`. Events can be either: - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired. - `'load'` - consider operation to be finished when the `load` event is fired. - `'networkidle'` - **DISCOURAGED** consider operation to be finished when there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead. - `'commit'` - consider operation to be finished when network response is received and the document started loading. |

#### Returns
Union[Response, None]

### 异步

```python signature
async def go_back(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None, wait_until: Optional[Literal['commit', 'domcontentloaded', 'load', 'networkidle']] = None) -> Optional[ForwardRef('Response')]
```

Page.go_back

Returns the main resource response. In case of multiple redirects, the navigation will resolve with the response of
the last redirect. If cannot go back, returns `null`.

Navigate to the previous page in history.

**NOTE** **Testing Back/Forward Cache (BFCache) is not supported.** By default, Playwright disables the
Back/Forward Cache across all browsers. Even if explicitly enabled, Playwright's internal state relies on
network-level navigation events. Because BFCache restores unfreeze the DOM without firing these events, using
`page.goBack()` or `page.goForward()` to trigger a BFCache restore will result in timeouts and a desynchronized
`Page` state.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_navigation_timeout()`, `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or `page.set_default_timeout()` methods. |
| `wait_until` | Union["commit", "domcontentloaded", "load", "networkidle", None] | When to consider operation succeeded, defaults to `load`. Events can be either: - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired. - `'load'` - consider operation to be finished when the `load` event is fired. - `'networkidle'` - **DISCOURAGED** consider operation to be finished when there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead. - `'commit'` - consider operation to be finished when network response is received and the document started loading. |

#### Returns
Union[Response, None]


## go_forward

### 同步

```python signature
def go_forward(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None, wait_until: Optional[Literal['commit', 'domcontentloaded', 'load', 'networkidle']] = None) -> Optional[ForwardRef('Response')]
```

Page.go_forward

Returns the main resource response. In case of multiple redirects, the navigation will resolve with the response of
the last redirect. If cannot go forward, returns `null`.

Navigate to the next page in history.

**NOTE** **Testing Back/Forward Cache (BFCache) is not supported.** By default, Playwright disables the
Back/Forward Cache across all browsers. Even if explicitly enabled, Playwright's internal state relies on
network-level navigation events. Because BFCache restores unfreeze the DOM without firing these events, using
`page.goBack()` or `page.goForward()` to trigger a BFCache restore will result in timeouts and a desynchronized
`Page` state.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_navigation_timeout()`, `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or `page.set_default_timeout()` methods. |
| `wait_until` | Union["commit", "domcontentloaded", "load", "networkidle", None] | When to consider operation succeeded, defaults to `load`. Events can be either: - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired. - `'load'` - consider operation to be finished when the `load` event is fired. - `'networkidle'` - **DISCOURAGED** consider operation to be finished when there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead. - `'commit'` - consider operation to be finished when network response is received and the document started loading. |

#### Returns
Union[Response, None]

### 异步

```python signature
async def go_forward(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None, wait_until: Optional[Literal['commit', 'domcontentloaded', 'load', 'networkidle']] = None) -> Optional[ForwardRef('Response')]
```

Page.go_forward

Returns the main resource response. In case of multiple redirects, the navigation will resolve with the response of
the last redirect. If cannot go forward, returns `null`.

Navigate to the next page in history.

**NOTE** **Testing Back/Forward Cache (BFCache) is not supported.** By default, Playwright disables the
Back/Forward Cache across all browsers. Even if explicitly enabled, Playwright's internal state relies on
network-level navigation events. Because BFCache restores unfreeze the DOM without firing these events, using
`page.goBack()` or `page.goForward()` to trigger a BFCache restore will result in timeouts and a desynchronized
`Page` state.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_navigation_timeout()`, `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or `page.set_default_timeout()` methods. |
| `wait_until` | Union["commit", "domcontentloaded", "load", "networkidle", None] | When to consider operation succeeded, defaults to `load`. Events can be either: - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired. - `'load'` - consider operation to be finished when the `load` event is fired. - `'networkidle'` - **DISCOURAGED** consider operation to be finished when there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead. - `'commit'` - consider operation to be finished when network response is received and the document started loading. |

#### Returns
Union[Response, None]


## goto

### 同步

```python signature
def goto(self, url: str, *, referer: Optional[str] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, wait_until: Optional[Literal['commit', 'domcontentloaded', 'load', 'networkidle']] = None) -> Optional[ForwardRef('Response')]
```

Page.goto

Returns the main resource response. In case of multiple redirects, the navigation will resolve with the first
non-redirect response.

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
| `url` | str | URL to navigate page to. The url should include scheme, e.g. `https://`. When a `base_url` via the context options was provided and the passed URL is a path, it gets merged via the [`new URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) constructor. |
| `referer` | Union[str, None] | Referer header value. If provided it will take preference over the referer header value set by `page.set_extra_http_headers()`. |
| `timeout` | Union[float, None] | Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_navigation_timeout()`, `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or `page.set_default_timeout()` methods. |
| `wait_until` | Union["commit", "domcontentloaded", "load", "networkidle", None] | When to consider operation succeeded, defaults to `load`. Events can be either: - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired. - `'load'` - consider operation to be finished when the `load` event is fired. - `'networkidle'` - **DISCOURAGED** consider operation to be finished when there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead. - `'commit'` - consider operation to be finished when network response is received and the document started loading. |

#### Returns
Union[Response, None]

### 异步

```python signature
async def goto(self, url: str, *, referer: Optional[str] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, wait_until: Optional[Literal['commit', 'domcontentloaded', 'load', 'networkidle']] = None) -> Optional[ForwardRef('Response')]
```

Page.goto

Returns the main resource response. In case of multiple redirects, the navigation will resolve with the first
non-redirect response.

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
| `url` | str | URL to navigate page to. The url should include scheme, e.g. `https://`. When a `base_url` via the context options was provided and the passed URL is a path, it gets merged via the [`new URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) constructor. |
| `referer` | Union[str, None] | Referer header value. If provided it will take preference over the referer header value set by `page.set_extra_http_headers()`. |
| `timeout` | Union[float, None] | Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_navigation_timeout()`, `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or `page.set_default_timeout()` methods. |
| `wait_until` | Union["commit", "domcontentloaded", "load", "networkidle", None] | When to consider operation succeeded, defaults to `load`. Events can be either: - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired. - `'load'` - consider operation to be finished when the `load` event is fired. - `'networkidle'` - **DISCOURAGED** consider operation to be finished when there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead. - `'commit'` - consider operation to be finished when network response is received and the document started loading. |

#### Returns
Union[Response, None]


## hide_highlight

### 同步

```python
def hide_highlight(self) -> None
```

Page.hide_highlight

Hide all locator highlight overlays previously added by `locator.highlight()` on this page.

### 异步

```python
async def hide_highlight(self) -> None
```

Page.hide_highlight

Hide all locator highlight overlays previously added by `locator.highlight()` on this page.


## hover

### 同步

```python signature
def hover(self, selector: str, *, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

Page.hover

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

Page.hover

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

Page.inner_html

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

Page.inner_html

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

Page.inner_text

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

Page.inner_text

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

Page.input_value

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

Page.input_value

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

Page.is_checked

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

Page.is_checked

Returns whether the element is checked. Throws if the element is not a checkbox or radio input.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
bool


## is_closed

### 同步

```python
def is_closed(self) -> bool
```

Page.is_closed

Indicates that the page has been closed.

#### Returns
bool

### 异步

```python
def is_closed(self) -> bool
```

Page.is_closed

Indicates that the page has been closed.

#### Returns
bool


## is_disabled

### 同步

```python signature
def is_disabled(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool
```

Page.is_disabled

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

Page.is_disabled

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

Page.is_editable

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

Page.is_editable

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

Page.is_enabled

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

Page.is_enabled

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
def is_hidden(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool
```

Page.is_hidden

Returns whether the element is hidden, the opposite of [visible](https://playwright.dev/python/docs/actionability#visible).  `selector` that
does not match any elements is considered hidden.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Deprecated: This option is ignored. `page.is_hidden()` does not wait for the↵element to become hidden and returns immediately. |

#### Returns
bool

### 异步

```python signature
async def is_hidden(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool
```

Page.is_hidden

Returns whether the element is hidden, the opposite of [visible](https://playwright.dev/python/docs/actionability#visible).  `selector` that
does not match any elements is considered hidden.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Deprecated: This option is ignored. `page.is_hidden()` does not wait for the↵element to become hidden and returns immediately. |

#### Returns
bool


## is_visible

### 同步

```python signature
def is_visible(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool
```

Page.is_visible

Returns whether the element is [visible](https://playwright.dev/python/docs/actionability#visible). `selector` that does not match any elements
is considered not visible.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Deprecated: This option is ignored. `page.is_visible()` does not wait↵for the element to become visible and returns immediately. |

#### Returns
bool

### 异步

```python signature
async def is_visible(self, selector: str, *, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> bool
```

Page.is_visible

Returns whether the element is [visible](https://playwright.dev/python/docs/actionability#visible). `selector` that does not match any elements
is considered not visible.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
| `strict` | Union[bool, None] | When true, the call requires selector to resolve to a single element. If given selector resolves to more than one element, the call throws an exception. |
| `timeout` | Union[float, None] | Deprecated: This option is ignored. `page.is_visible()` does not wait↵for the element to become visible and returns immediately. |

#### Returns
bool


## keyboard

属性，直接读取；异步入口也不加 await。

```python signature
Page.keyboard: Keyboard
```

Page.keyboard

#### Returns
Keyboard


## local_storage

属性，直接读取；异步入口也不加 await。

```python signature
Page.local_storage: WebStorage
```

Page.local_storage

Provides access to the page's `localStorage` for the current origin. See `WebStorage`.

#### Returns
WebStorage


## locator

### 同步

```python signature
def locator(self, selector: str, *, has: Optional[ForwardRef('Locator')] = None, has_not: Optional[ForwardRef('Locator')] = None, has_not_text: Union[str, Pattern[str], NoneType] = None, has_text: Union[str, Pattern[str], NoneType] = None) -> 'Locator'
```

Page.locator

The method returns an element locator that can be used to perform actions on this page / frame. Locator is resolved
to the element immediately before performing an action, so a series of actions on the same locator can in fact be
performed on different DOM elements. That would happen if the DOM structure between those actions has changed.

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

Page.locator

The method returns an element locator that can be used to perform actions on this page / frame. Locator is resolved
to the element immediately before performing an action, so a series of actions on the same locator can in fact be
performed on different DOM elements. That would happen if the DOM structure between those actions has changed.

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


## main_frame

属性，直接读取；异步入口也不加 await。

```python signature
Page.main_frame: Frame
```

Page.main_frame

The page's main frame. Page is guaranteed to have a main frame which persists during navigations.

#### Returns
Frame


## mouse

属性，直接读取；异步入口也不加 await。

```python signature
Page.mouse: Mouse
```

Page.mouse

#### Returns
Mouse


## on

### 同步

```python
def on(self, event: str, f: Callable[..., NoneType]) -> None
```

支持的重载：

```python
def on(self, event: Literal['close'], f: Callable[[ForwardRef('Page')], ForwardRef('None')]) -> None
def on(self, event: Literal['console'], f: Callable[[ForwardRef('ConsoleMessage')], ForwardRef('None')]) -> None
def on(self, event: Literal['crash'], f: Callable[[ForwardRef('Page')], ForwardRef('None')]) -> None
def on(self, event: Literal['dialog'], f: Callable[[ForwardRef('Dialog')], ForwardRef('None')]) -> None
def on(self, event: Literal['dialogclosed'], f: Callable[[ForwardRef('Dialog')], ForwardRef('None')]) -> None
def on(self, event: Literal['domcontentloaded'], f: Callable[[ForwardRef('Page')], ForwardRef('None')]) -> None
def on(self, event: Literal['download'], f: Callable[[ForwardRef('Download')], ForwardRef('None')]) -> None
def on(self, event: Literal['filechooser'], f: Callable[[ForwardRef('FileChooser')], ForwardRef('None')]) -> None
def on(self, event: Literal['frameattached'], f: Callable[[ForwardRef('Frame')], ForwardRef('None')]) -> None
def on(self, event: Literal['framedetached'], f: Callable[[ForwardRef('Frame')], ForwardRef('None')]) -> None
def on(self, event: Literal['framenavigated'], f: Callable[[ForwardRef('Frame')], ForwardRef('None')]) -> None
def on(self, event: Literal['load'], f: Callable[[ForwardRef('Page')], ForwardRef('None')]) -> None
def on(self, event: Literal['pageerror'], f: Callable[[ForwardRef('Error')], ForwardRef('None')]) -> None
def on(self, event: Literal['popup'], f: Callable[[ForwardRef('Page')], ForwardRef('None')]) -> None
def on(self, event: Literal['request'], f: Callable[[ForwardRef('Request')], ForwardRef('None')]) -> None
def on(self, event: Literal['requestfailed'], f: Callable[[ForwardRef('Request')], ForwardRef('None')]) -> None
def on(self, event: Literal['requestfinished'], f: Callable[[ForwardRef('Request')], ForwardRef('None')]) -> None
def on(self, event: Literal['response'], f: Callable[[ForwardRef('Response')], ForwardRef('None')]) -> None
def on(self, event: Literal['websocket'], f: Callable[[ForwardRef('WebSocket')], ForwardRef('None')]) -> None
def on(self, event: Literal['worker'], f: Callable[[ForwardRef('Worker')], ForwardRef('None')]) -> None
```

Registers the function ``f`` to the event name ``event``.

### 异步

```python
def on(self, event: str, f: Callable[..., Optional[Awaitable[NoneType]]]) -> None
```

支持的重载：

```python
def on(self, event: Literal['close'], f: Callable[[ForwardRef('Page')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['console'], f: Callable[[ForwardRef('ConsoleMessage')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['crash'], f: Callable[[ForwardRef('Page')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['dialog'], f: Callable[[ForwardRef('Dialog')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['dialogclosed'], f: Callable[[ForwardRef('Dialog')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['domcontentloaded'], f: Callable[[ForwardRef('Page')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['download'], f: Callable[[ForwardRef('Download')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['filechooser'], f: Callable[[ForwardRef('FileChooser')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['frameattached'], f: Callable[[ForwardRef('Frame')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['framedetached'], f: Callable[[ForwardRef('Frame')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['framenavigated'], f: Callable[[ForwardRef('Frame')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['load'], f: Callable[[ForwardRef('Page')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['pageerror'], f: Callable[[ForwardRef('Error')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['popup'], f: Callable[[ForwardRef('Page')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['request'], f: Callable[[ForwardRef('Request')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['requestfailed'], f: Callable[[ForwardRef('Request')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['requestfinished'], f: Callable[[ForwardRef('Request')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['response'], f: Callable[[ForwardRef('Response')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['websocket'], f: Callable[[ForwardRef('WebSocket')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['worker'], f: Callable[[ForwardRef('Worker')], ForwardRef('Union[Awaitable[None], None]')]) -> None
```

Registers the function ``f`` to the event name ``event``.


## once

### 同步

```python
def once(self, event: str, f: Callable[..., NoneType]) -> None
```

支持的重载：

```python
def once(self, event: Literal['close'], f: Callable[[ForwardRef('Page')], ForwardRef('None')]) -> None
def once(self, event: Literal['console'], f: Callable[[ForwardRef('ConsoleMessage')], ForwardRef('None')]) -> None
def once(self, event: Literal['crash'], f: Callable[[ForwardRef('Page')], ForwardRef('None')]) -> None
def once(self, event: Literal['dialog'], f: Callable[[ForwardRef('Dialog')], ForwardRef('None')]) -> None
def once(self, event: Literal['dialogclosed'], f: Callable[[ForwardRef('Dialog')], ForwardRef('None')]) -> None
def once(self, event: Literal['domcontentloaded'], f: Callable[[ForwardRef('Page')], ForwardRef('None')]) -> None
def once(self, event: Literal['download'], f: Callable[[ForwardRef('Download')], ForwardRef('None')]) -> None
def once(self, event: Literal['filechooser'], f: Callable[[ForwardRef('FileChooser')], ForwardRef('None')]) -> None
def once(self, event: Literal['frameattached'], f: Callable[[ForwardRef('Frame')], ForwardRef('None')]) -> None
def once(self, event: Literal['framedetached'], f: Callable[[ForwardRef('Frame')], ForwardRef('None')]) -> None
def once(self, event: Literal['framenavigated'], f: Callable[[ForwardRef('Frame')], ForwardRef('None')]) -> None
def once(self, event: Literal['load'], f: Callable[[ForwardRef('Page')], ForwardRef('None')]) -> None
def once(self, event: Literal['pageerror'], f: Callable[[ForwardRef('Error')], ForwardRef('None')]) -> None
def once(self, event: Literal['popup'], f: Callable[[ForwardRef('Page')], ForwardRef('None')]) -> None
def once(self, event: Literal['request'], f: Callable[[ForwardRef('Request')], ForwardRef('None')]) -> None
def once(self, event: Literal['requestfailed'], f: Callable[[ForwardRef('Request')], ForwardRef('None')]) -> None
def once(self, event: Literal['requestfinished'], f: Callable[[ForwardRef('Request')], ForwardRef('None')]) -> None
def once(self, event: Literal['response'], f: Callable[[ForwardRef('Response')], ForwardRef('None')]) -> None
def once(self, event: Literal['websocket'], f: Callable[[ForwardRef('WebSocket')], ForwardRef('None')]) -> None
def once(self, event: Literal['worker'], f: Callable[[ForwardRef('Worker')], ForwardRef('None')]) -> None
```

The same as ``self.on``, except that the listener is automatically
removed after being called.

### 异步

```python
def once(self, event: str, f: Callable[..., Optional[Awaitable[NoneType]]]) -> None
```

支持的重载：

```python
def once(self, event: Literal['close'], f: Callable[[ForwardRef('Page')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['console'], f: Callable[[ForwardRef('ConsoleMessage')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['crash'], f: Callable[[ForwardRef('Page')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['dialog'], f: Callable[[ForwardRef('Dialog')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['dialogclosed'], f: Callable[[ForwardRef('Dialog')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['domcontentloaded'], f: Callable[[ForwardRef('Page')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['download'], f: Callable[[ForwardRef('Download')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['filechooser'], f: Callable[[ForwardRef('FileChooser')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['frameattached'], f: Callable[[ForwardRef('Frame')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['framedetached'], f: Callable[[ForwardRef('Frame')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['framenavigated'], f: Callable[[ForwardRef('Frame')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['load'], f: Callable[[ForwardRef('Page')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['pageerror'], f: Callable[[ForwardRef('Error')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['popup'], f: Callable[[ForwardRef('Page')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['request'], f: Callable[[ForwardRef('Request')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['requestfailed'], f: Callable[[ForwardRef('Request')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['requestfinished'], f: Callable[[ForwardRef('Request')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['response'], f: Callable[[ForwardRef('Response')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['websocket'], f: Callable[[ForwardRef('WebSocket')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['worker'], f: Callable[[ForwardRef('Worker')], ForwardRef('Union[Awaitable[None], None]')]) -> None
```

The same as ``self.on``, except that the listener is automatically
removed after being called.


## opener

### 同步

```python
def opener(self) -> Optional[ForwardRef('Page')]
```

Page.opener

Returns the opener for popup pages and `null` for others. If the opener has been closed already the returns `null`.

#### Returns
Union[Page, None]

### 异步

```python
async def opener(self) -> Optional[ForwardRef('Page')]
```

Page.opener

Returns the opener for popup pages and `null` for others. If the opener has been closed already the returns `null`.

#### Returns
Union[Page, None]


## page_errors

### 同步

```python signature
def page_errors(self, *, filter: Optional[Literal['all', 'since-navigation']] = None) -> List[ForwardRef('Error')]
```

Page.page_errors

Returns up to (currently) 200 last page errors from this page. See `page.on('pageerror')` for more details.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `filter` | Union["all", "since-navigation", None] | Controls which errors are returned: |

#### Returns
List[Error]

### 异步

```python signature
async def page_errors(self, *, filter: Optional[Literal['all', 'since-navigation']] = None) -> List[ForwardRef('Error')]
```

Page.page_errors

Returns up to (currently) 200 last page errors from this page. See `page.on('pageerror')` for more details.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `filter` | Union["all", "since-navigation", None] | Controls which errors are returned: |

#### Returns
List[Error]


## pause

### 同步

```python
def pause(self) -> None
```

Page.pause

Pauses script execution. Playwright will stop executing the script and wait for the user to either press the
'Resume' button in the page overlay or to call `playwright.resume()` in the DevTools console.

User can inspect selectors or perform manual steps while paused. Resume will continue running the original script
from the place it was paused.

**NOTE** This method requires Playwright to be started in a headed mode, with a falsy `headless` option.

### 异步

```python
async def pause(self) -> None
```

Page.pause

Pauses script execution. Playwright will stop executing the script and wait for the user to either press the
'Resume' button in the page overlay or to call `playwright.resume()` in the DevTools console.

User can inspect selectors or perform manual steps while paused. Resume will continue running the original script
from the place it was paused.

**NOTE** This method requires Playwright to be started in a headed mode, with a falsy `headless` option.


## pdf

### 同步

```python signature
def pdf(self, *, display_header_footer: Optional[bool] = None, footer_template: Optional[str] = None, format: Optional[str] = None, header_template: Optional[str] = None, height: Union[str, float, NoneType] = None, landscape: Optional[bool] = None, margin: Optional[patchright._impl._api_structures.PdfMargins] = None, outline: Optional[bool] = None, page_ranges: Optional[str] = None, path: Union[pathlib.Path, str, NoneType] = None, prefer_css_page_size: Optional[bool] = None, print_background: Optional[bool] = None, scale: Optional[float] = None, tagged: Optional[bool] = None, width: Union[str, float, NoneType] = None) -> bytes
```

Page.pdf

Returns the PDF buffer.

`page.pdf()` generates a pdf of the page with `print` css media. To generate a pdf with `screen` media, call
`page.emulate_media()` before calling `page.pdf()`:

**NOTE** By default, `page.pdf()` generates a pdf with modified colors for printing. Use the
[`-webkit-print-color-adjust`](https://developer.mozilla.org/en-US/docs/Web/CSS/-webkit-print-color-adjust)
property to force rendering of exact colors.

**Usage**

```py
# generates a pdf with "screen" media type.
page.emulate_media(media="screen")
page.pdf(path="page.pdf")
```

The `width`, `height`, and `margin` options accept values labeled with units. Unlabeled values are treated as
pixels.

A few examples:
- `page.pdf({width: 100})` - prints with width set to 100 pixels
- `page.pdf({width: '100px'})` - prints with width set to 100 pixels
- `page.pdf({width: '10cm'})` - prints with width set to 10 centimeters.

All possible units are:
- `px` - pixel
- `in` - inch
- `cm` - centimeter
- `mm` - millimeter

The `format` options are:
- `Letter`: 8.5in x 11in
- `Legal`: 8.5in x 14in
- `Tabloid`: 11in x 17in
- `Ledger`: 17in x 11in
- `A0`: 33.1in x 46.8in
- `A1`: 23.4in x 33.1in
- `A2`: 16.54in x 23.4in
- `A3`: 11.7in x 16.54in
- `A4`: 8.27in x 11.7in
- `A5`: 5.83in x 8.27in
- `A6`: 4.13in x 5.83in

**NOTE** `header_template` and `footer_template` markup have the following limitations: > 1. Script tags inside
templates are not evaluated. > 2. Page styles are not visible inside templates.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `display_header_footer` | Union[bool, None] | Display header and footer. Defaults to `false`. |
| `footer_template` | Union[str, None] | HTML template for the print footer. Should use the same format as the `header_template`. |
| `format` | Union[str, None] | Paper format. If set, takes priority over `width` or `height` options. Defaults to 'Letter'. |
| `header_template` | Union[str, None] | HTML template for the print header. Should be valid HTML markup with following classes used to inject printing values into them: - `'date'` formatted print date - `'title'` document title - `'url'` document location - `'pageNumber'` current page number - `'totalPages'` total pages in the document |
| `height` | Union[float, str, None] | Paper height, accepts values labeled with units. |
| `landscape` | Union[bool, None] | Paper orientation. Defaults to `false`. |
| `margin` | Union[{top: Union[float, str, None], right: Union[float, str, None], bottom: Union[float, str, None], left: Union[float, str, None]}, None] | Paper margins, defaults to none. |
| `outline` | Union[bool, None] | Whether or not to embed the document outline into the PDF. Defaults to `false`. |
| `page_ranges` | Union[str, None] | Paper ranges to print, e.g., '1-5, 8, 11-13'. Defaults to the empty string, which means print all pages. |
| `path` | Union[pathlib.Path, str, None] | The file path to save the PDF to. If `path` is a relative path, then it is resolved relative to the current working directory. If no path is provided, the PDF won't be saved to the disk. |
| `prefer_css_page_size` | Union[bool, None] | Give any CSS `@page` size declared in the page priority over what is declared in `width` and `height` or `format` options. Defaults to `false`, which will scale the content to fit the paper size. |
| `print_background` | Union[bool, None] | Print background graphics. Defaults to `false`. |
| `scale` | Union[float, None] | Scale of the webpage rendering. Defaults to `1`. Scale amount must be between 0.1 and 2. |
| `tagged` | Union[bool, None] | Whether or not to generate tagged (accessible) PDF. Defaults to `false`. |
| `width` | Union[float, str, None] | Paper width, accepts values labeled with units. |

#### Returns
bytes

### 异步

```python signature
async def pdf(self, *, display_header_footer: Optional[bool] = None, footer_template: Optional[str] = None, format: Optional[str] = None, header_template: Optional[str] = None, height: Union[str, float, NoneType] = None, landscape: Optional[bool] = None, margin: Optional[patchright._impl._api_structures.PdfMargins] = None, outline: Optional[bool] = None, page_ranges: Optional[str] = None, path: Union[pathlib.Path, str, NoneType] = None, prefer_css_page_size: Optional[bool] = None, print_background: Optional[bool] = None, scale: Optional[float] = None, tagged: Optional[bool] = None, width: Union[str, float, NoneType] = None) -> bytes
```

Page.pdf

Returns the PDF buffer.

`page.pdf()` generates a pdf of the page with `print` css media. To generate a pdf with `screen` media, call
`page.emulate_media()` before calling `page.pdf()`:

**NOTE** By default, `page.pdf()` generates a pdf with modified colors for printing. Use the
[`-webkit-print-color-adjust`](https://developer.mozilla.org/en-US/docs/Web/CSS/-webkit-print-color-adjust)
property to force rendering of exact colors.

**Usage**

```py
# generates a pdf with "screen" media type.
await page.emulate_media(media="screen")
await page.pdf(path="page.pdf")
```

The `width`, `height`, and `margin` options accept values labeled with units. Unlabeled values are treated as
pixels.

A few examples:
- `page.pdf({width: 100})` - prints with width set to 100 pixels
- `page.pdf({width: '100px'})` - prints with width set to 100 pixels
- `page.pdf({width: '10cm'})` - prints with width set to 10 centimeters.

All possible units are:
- `px` - pixel
- `in` - inch
- `cm` - centimeter
- `mm` - millimeter

The `format` options are:
- `Letter`: 8.5in x 11in
- `Legal`: 8.5in x 14in
- `Tabloid`: 11in x 17in
- `Ledger`: 17in x 11in
- `A0`: 33.1in x 46.8in
- `A1`: 23.4in x 33.1in
- `A2`: 16.54in x 23.4in
- `A3`: 11.7in x 16.54in
- `A4`: 8.27in x 11.7in
- `A5`: 5.83in x 8.27in
- `A6`: 4.13in x 5.83in

**NOTE** `header_template` and `footer_template` markup have the following limitations: > 1. Script tags inside
templates are not evaluated. > 2. Page styles are not visible inside templates.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `display_header_footer` | Union[bool, None] | Display header and footer. Defaults to `false`. |
| `footer_template` | Union[str, None] | HTML template for the print footer. Should use the same format as the `header_template`. |
| `format` | Union[str, None] | Paper format. If set, takes priority over `width` or `height` options. Defaults to 'Letter'. |
| `header_template` | Union[str, None] | HTML template for the print header. Should be valid HTML markup with following classes used to inject printing values into them: - `'date'` formatted print date - `'title'` document title - `'url'` document location - `'pageNumber'` current page number - `'totalPages'` total pages in the document |
| `height` | Union[float, str, None] | Paper height, accepts values labeled with units. |
| `landscape` | Union[bool, None] | Paper orientation. Defaults to `false`. |
| `margin` | Union[{top: Union[float, str, None], right: Union[float, str, None], bottom: Union[float, str, None], left: Union[float, str, None]}, None] | Paper margins, defaults to none. |
| `outline` | Union[bool, None] | Whether or not to embed the document outline into the PDF. Defaults to `false`. |
| `page_ranges` | Union[str, None] | Paper ranges to print, e.g., '1-5, 8, 11-13'. Defaults to the empty string, which means print all pages. |
| `path` | Union[pathlib.Path, str, None] | The file path to save the PDF to. If `path` is a relative path, then it is resolved relative to the current working directory. If no path is provided, the PDF won't be saved to the disk. |
| `prefer_css_page_size` | Union[bool, None] | Give any CSS `@page` size declared in the page priority over what is declared in `width` and `height` or `format` options. Defaults to `false`, which will scale the content to fit the paper size. |
| `print_background` | Union[bool, None] | Print background graphics. Defaults to `false`. |
| `scale` | Union[float, None] | Scale of the webpage rendering. Defaults to `1`. Scale amount must be between 0.1 and 2. |
| `tagged` | Union[bool, None] | Whether or not to generate tagged (accessible) PDF. Defaults to `false`. |
| `width` | Union[float, str, None] | Paper width, accepts values labeled with units. |

#### Returns
bytes


## pick_locator

### 同步

```python
def pick_locator(self) -> 'Locator'
```

Page.pick_locator

Enters pick locator mode where hovering over page elements highlights them and shows the corresponding locator.
Once the user clicks an element, the mode is deactivated and the `Locator` for the picked element is returned.

**Usage**

```py
locator = page.pick_locator()
print(locator)
```

#### Returns
Locator

### 异步

```python
async def pick_locator(self) -> 'Locator'
```

Page.pick_locator

Enters pick locator mode where hovering over page elements highlights them and shows the corresponding locator.
Once the user clicks an element, the mode is deactivated and the `Locator` for the picked element is returned.

**Usage**

```py
locator = await page.pick_locator()
print(locator)
```

#### Returns
Locator


## press

### 同步

```python signature
def press(self, selector: str, key: str, *, delay: Optional[float] = None, no_wait_after: Optional[bool] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Page.press

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

**Usage**

```py
page = browser.new_page()
page.goto("https://keycode.info")
page.press("body", "A")
page.screenshot(path="a.png")
page.press("body", "ArrowLeft")
page.screenshot(path="arrow_left.png")
page.press("body", "Shift+O")
page.screenshot(path="o.png")
browser.close()
```

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

Page.press

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

**Usage**

```py
page = await browser.new_page()
await page.goto("https://keycode.info")
await page.press("body", "A")
await page.screenshot(path="a.png")
await page.press("body", "ArrowLeft")
await page.screenshot(path="arrow_left.png")
await page.press("body", "Shift+O")
await page.screenshot(path="o.png")
await browser.close()
```

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

Page.query_selector

The method finds an element matching the specified selector within the page. If no elements match the selector, the
return value resolves to `null`. To wait for an element on the page, use `locator.wait_for()`.

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

Page.query_selector

The method finds an element matching the specified selector within the page. If no elements match the selector, the
return value resolves to `null`. To wait for an element on the page, use `locator.wait_for()`.

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

Page.query_selector_all

The method finds all elements matching the specified selector within the page. If no elements match the selector,
the return value resolves to `[]`.

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

Page.query_selector_all

The method finds all elements matching the specified selector within the page. If no elements match the selector,
the return value resolves to `[]`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to query for. |

#### Returns
List[ElementHandle]


## reload

### 同步

```python signature
def reload(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None, wait_until: Optional[Literal['commit', 'domcontentloaded', 'load', 'networkidle']] = None) -> Optional[ForwardRef('Response')]
```

Page.reload

This method reloads the current page, in the same way as if the user had triggered a browser refresh. Returns the
main resource response. In case of multiple redirects, the navigation will resolve with the response of the last
redirect.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_navigation_timeout()`, `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or `page.set_default_timeout()` methods. |
| `wait_until` | Union["commit", "domcontentloaded", "load", "networkidle", None] | When to consider operation succeeded, defaults to `load`. Events can be either: - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired. - `'load'` - consider operation to be finished when the `load` event is fired. - `'networkidle'` - **DISCOURAGED** consider operation to be finished when there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead. - `'commit'` - consider operation to be finished when network response is received and the document started loading. |

#### Returns
Union[Response, None]

### 异步

```python signature
async def reload(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None, wait_until: Optional[Literal['commit', 'domcontentloaded', 'load', 'networkidle']] = None) -> Optional[ForwardRef('Response')]
```

Page.reload

This method reloads the current page, in the same way as if the user had triggered a browser refresh. Returns the
main resource response. In case of multiple redirects, the navigation will resolve with the response of the last
redirect.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_navigation_timeout()`, `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or `page.set_default_timeout()` methods. |
| `wait_until` | Union["commit", "domcontentloaded", "load", "networkidle", None] | When to consider operation succeeded, defaults to `load`. Events can be either: - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired. - `'load'` - consider operation to be finished when the `load` event is fired. - `'networkidle'` - **DISCOURAGED** consider operation to be finished when there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead. - `'commit'` - consider operation to be finished when network response is received and the document started loading. |

#### Returns
Union[Response, None]


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


## remove_locator_handler

### 同步

```python
def remove_locator_handler(self, locator: 'Locator') -> None
```

Page.remove_locator_handler

Removes all locator handlers added by `page.add_locator_handler()` for a specific locator.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `locator` | Locator | Locator passed to `page.add_locator_handler()`. |

### 异步

```python
async def remove_locator_handler(self, locator: 'Locator') -> None
```

Page.remove_locator_handler

Removes all locator handlers added by `page.add_locator_handler()` for a specific locator.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `locator` | Locator | Locator passed to `page.add_locator_handler()`. |

## request

属性，直接读取；异步入口也不加 await。

```python signature
Page.request: APIRequestContext
```

Page.request

API testing helper associated with this page. This method returns the same instance as `browser_context.request` on
the page's context. See `browser_context.request` for more details.

#### Returns
APIRequestContext


## request_gc

### 同步

```python
def request_gc(self) -> None
```

Page.request_gc

Request the page to perform garbage collection. Note that there is no guarantee that all unreachable objects will
be collected.

This is useful to help detect memory leaks. For example, if your page has a large object `'suspect'` that might be
leaked, you can check that it does not leak by using a
[`WeakRef`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef).

```py
# 1. In your page, save a WeakRef for the "suspect".
page.evaluate("globalThis.suspectWeakRef = new WeakRef(suspect)")
# 2. Request garbage collection.
page.request_gc()
# 3. Check that weak ref does not deref to the original object.
assert page.evaluate("!globalThis.suspectWeakRef.deref()")
```

### 异步

```python
async def request_gc(self) -> None
```

Page.request_gc

Request the page to perform garbage collection. Note that there is no guarantee that all unreachable objects will
be collected.

This is useful to help detect memory leaks. For example, if your page has a large object `'suspect'` that might be
leaked, you can check that it does not leak by using a
[`WeakRef`](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/WeakRef).

```py
# 1. In your page, save a WeakRef for the "suspect".
await page.evaluate("globalThis.suspectWeakRef = new WeakRef(suspect)")
# 2. Request garbage collection.
await page.request_gc()
# 3. Check that weak ref does not deref to the original object.
assert await page.evaluate("!globalThis.suspectWeakRef.deref()")
```


## requests

### 同步

```python
def requests(self) -> List[ForwardRef('Request')]
```

Page.requests

Returns up to (currently) 100 last network request from this page. See `page.on('request')` for more details.

Returned requests should be accessed immediately, otherwise they might be collected to prevent unbounded memory
growth as new requests come in. Once collected, retrieving most information about the request is impossible.

Note that requests reported through the `page.on('request')` request are not collected, so there is a trade off
between efficient memory usage with `page.requests()` and the amount of available information reported through
`page.on('request')`.

#### Returns
List[Request]

### 异步

```python
async def requests(self) -> List[ForwardRef('Request')]
```

Page.requests

Returns up to (currently) 100 last network request from this page. See `page.on('request')` for more details.

Returned requests should be accessed immediately, otherwise they might be collected to prevent unbounded memory
growth as new requests come in. Once collected, retrieving most information about the request is impossible.

Note that requests reported through the `page.on('request')` request are not collected, so there is a trade off
between efficient memory usage with `page.requests()` and the amount of available information reported through
`page.on('request')`.

#### Returns
List[Request]


## route

### 同步

```python signature
def route(self, url: Union[str, Pattern[str], Callable[[str], bool]], handler: Union[Callable[[ForwardRef('Route')], Any], Callable[[ForwardRef('Route'), ForwardRef('Request')], Any]], *, times: Optional[int] = None) -> 'SyncContextManager'
```

Page.route

Routing provides the capability to modify network requests that are made by a page.

Once routing is enabled, every request matching the url pattern will stall unless it's continued, fulfilled or
aborted.

**NOTE** The handler will only be called for the first url if the response is a redirect.

**NOTE** `page.route()` will not intercept requests intercepted by Service Worker. See
[this](https://github.com/microsoft/playwright/issues/1090) issue. We recommend disabling Service Workers when
using request interception by setting `service_workers` to `'block'`.

**NOTE** `page.route()` will not intercept the first request of a popup page. Use `browser_context.route()`
instead.

**Usage**

An example of a naive handler that aborts all image requests:

```py
page = browser.new_page()
page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())
page.goto("https://example.com")
browser.close()
```

or the same snippet using a regex pattern instead:

```py
page = browser.new_page()
page.route(re.compile(r"(\.png$)|(\.jpg$)"), lambda route: route.abort())
page.goto("https://example.com")
browser.close()
```

It is possible to examine the request to decide the route action. For example, mocking all requests that contain
some post data, and leaving all other requests as is:

```py
def handle_route(route: Route):
  if ("my-string" in route.request.post_data):
    route.fulfill(body="mocked-data")
  else:
    route.continue_()
page.route("/api/**", handle_route)
```

If a request matches multiple registered routes, the most recently registered route takes precedence.

Page routes take precedence over browser context routes (set up with `browser_context.route()`) when request
matches both handlers.

To remove a route with its handler you can use `page.unroute()`.

**NOTE** Enabling routing disables http cache.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url` | Union[Callable[[str], bool], Pattern[str], str] | A glob pattern, regex pattern, or predicate that receives a [URL] to match during routing. If `base_url` is set in the context options and the provided URL is a string that does not start with `*`, it is resolved using the [`new URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) constructor. |
| `handler` | Union[Callable[[Route, Request], Any], Callable[[Route], Any]] | handler function to route the request. |
| `times` | Union[int, None] | How often a route should be used. By default it will be used every time. |

#### Returns
SyncContextManager

### 异步

```python signature
async def route(self, url: Union[str, Pattern[str], Callable[[str], bool]], handler: Union[Callable[[ForwardRef('Route')], Any], Callable[[ForwardRef('Route'), ForwardRef('Request')], Any]], *, times: Optional[int] = None) -> 'AsyncContextManager'
```

Page.route

Routing provides the capability to modify network requests that are made by a page.

Once routing is enabled, every request matching the url pattern will stall unless it's continued, fulfilled or
aborted.

**NOTE** The handler will only be called for the first url if the response is a redirect.

**NOTE** `page.route()` will not intercept requests intercepted by Service Worker. See
[this](https://github.com/microsoft/playwright/issues/1090) issue. We recommend disabling Service Workers when
using request interception by setting `service_workers` to `'block'`.

**NOTE** `page.route()` will not intercept the first request of a popup page. Use `browser_context.route()`
instead.

**Usage**

An example of a naive handler that aborts all image requests:

```py
page = await browser.new_page()
await page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())
await page.goto("https://example.com")
await browser.close()
```

or the same snippet using a regex pattern instead:

```py
page = await browser.new_page()
await page.route(re.compile(r"(\.png$)|(\.jpg$)"), lambda route: route.abort())
await page.goto("https://example.com")
await browser.close()
```

It is possible to examine the request to decide the route action. For example, mocking all requests that contain
some post data, and leaving all other requests as is:

```py
async def handle_route(route: Route):
  if ("my-string" in route.request.post_data):
    await route.fulfill(body="mocked-data")
  else:
    await route.continue_()
await page.route("/api/**", handle_route)
```

If a request matches multiple registered routes, the most recently registered route takes precedence.

Page routes take precedence over browser context routes (set up with `browser_context.route()`) when request
matches both handlers.

To remove a route with its handler you can use `page.unroute()`.

**NOTE** Enabling routing disables http cache.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url` | Union[Callable[[str], bool], Pattern[str], str] | A glob pattern, regex pattern, or predicate that receives a [URL] to match during routing. If `base_url` is set in the context options and the provided URL is a string that does not start with `*`, it is resolved using the [`new URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) constructor. |
| `handler` | Union[Callable[[Route, Request], Any], Callable[[Route], Any]] | handler function to route the request. |
| `times` | Union[int, None] | How often a route should be used. By default it will be used every time. |

#### Returns
AsyncContextManager


## route_from_har

### 同步

```python signature
def route_from_har(self, har: Union[str, pathlib.Path], *, not_found: Optional[Literal['abort', 'fallback']] = None, update: Optional[bool] = None, update_content: Optional[Literal['attach', 'embed']] = None, update_mode: Optional[Literal['full', 'minimal']] = None, url: Union[str, Pattern[str], NoneType] = None) -> None
```

Page.route_from_har

If specified the network requests that are made in the page will be served from the HAR file. Read more about
[Replaying from HAR](https://playwright.dev/python/docs/mock#replaying-from-har).

Playwright will not serve requests intercepted by Service Worker from the HAR file. See
[this](https://github.com/microsoft/playwright/issues/1090) issue. We recommend disabling Service Workers when
using request interception by setting `service_workers` to `'block'`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `har` | Union[pathlib.Path, str] | Path to a [HAR](http://www.softwareishard.com/blog/har-12-spec) file with prerecorded network data. If `path` is a relative path, then it is resolved relative to the current working directory. |
| `not_found` | Union["abort", "fallback", None] | - If set to 'abort' any request not found in the HAR file will be aborted. - If set to 'fallback' missing requests will be sent to the network.  Defaults to abort. |
| `update` | Union[bool, None] | If specified, updates the given HAR with the actual network information instead of serving from file. The file is written to disk when `browser_context.close()` is called. |
| `update_content` | Union["attach", "embed", None] | Optional setting to control resource content management. If `attach` is specified, resources are persisted as separate files or entries in the ZIP archive. If `embed` is specified, content is stored inline the HAR file. |
| `update_mode` | Union["full", "minimal", None] | When set to `minimal`, only record information necessary for routing from HAR. This omits sizes, timing, page, cookies, security and other types of HAR information that are not used when replaying from HAR. Defaults to `minimal`. |
| `url` | Union[Pattern[str], str, None] | A glob pattern, regular expression or predicate to match the request URL. Only requests with URL matching the pattern will be served from the HAR file. If not specified, all requests are served from the HAR file. |

### 异步

```python signature
async def route_from_har(self, har: Union[str, pathlib.Path], *, not_found: Optional[Literal['abort', 'fallback']] = None, update: Optional[bool] = None, update_content: Optional[Literal['attach', 'embed']] = None, update_mode: Optional[Literal['full', 'minimal']] = None, url: Union[str, Pattern[str], NoneType] = None) -> None
```

Page.route_from_har

If specified the network requests that are made in the page will be served from the HAR file. Read more about
[Replaying from HAR](https://playwright.dev/python/docs/mock#replaying-from-har).

Playwright will not serve requests intercepted by Service Worker from the HAR file. See
[this](https://github.com/microsoft/playwright/issues/1090) issue. We recommend disabling Service Workers when
using request interception by setting `service_workers` to `'block'`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `har` | Union[pathlib.Path, str] | Path to a [HAR](http://www.softwareishard.com/blog/har-12-spec) file with prerecorded network data. If `path` is a relative path, then it is resolved relative to the current working directory. |
| `not_found` | Union["abort", "fallback", None] | - If set to 'abort' any request not found in the HAR file will be aborted. - If set to 'fallback' missing requests will be sent to the network.  Defaults to abort. |
| `update` | Union[bool, None] | If specified, updates the given HAR with the actual network information instead of serving from file. The file is written to disk when `browser_context.close()` is called. |
| `update_content` | Union["attach", "embed", None] | Optional setting to control resource content management. If `attach` is specified, resources are persisted as separate files or entries in the ZIP archive. If `embed` is specified, content is stored inline the HAR file. |
| `update_mode` | Union["full", "minimal", None] | When set to `minimal`, only record information necessary for routing from HAR. This omits sizes, timing, page, cookies, security and other types of HAR information that are not used when replaying from HAR. Defaults to `minimal`. |
| `url` | Union[Pattern[str], str, None] | A glob pattern, regular expression or predicate to match the request URL. Only requests with URL matching the pattern will be served from the HAR file. If not specified, all requests are served from the HAR file. |

## route_web_socket

### 同步

```python
def route_web_socket(self, url: Union[str, Pattern[str], Callable[[str], bool]], handler: Callable[[ForwardRef('WebSocketRoute')], Any]) -> None
```

Page.route_web_socket

This method allows to modify websocket connections that are made by the page.

Note that only `WebSocket`s created after this method was called will be routed. It is recommended to call this
method before navigating the page.

**Usage**

Below is an example of a simple mock that responds to a single message. See `WebSocketRoute` for more details and
examples.

```py
def message_handler(ws: WebSocketRoute, message: Union[str, bytes]):
  if message == "request":
    ws.send("response")

def handler(ws: WebSocketRoute):
  ws.on_message(lambda message: message_handler(ws, message))

page.route_web_socket("/ws", handler)
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url` | Union[Callable[[str], bool], Pattern[str], str] | Only WebSockets with the url matching this pattern will be routed. A string pattern can be relative to the `base_url` context option. |
| `handler` | Callable[[WebSocketRoute], Any] | Handler function to route the WebSocket. |

### 异步

```python
async def route_web_socket(self, url: Union[str, Pattern[str], Callable[[str], bool]], handler: Callable[[ForwardRef('WebSocketRoute')], Any]) -> None
```

Page.route_web_socket

This method allows to modify websocket connections that are made by the page.

Note that only `WebSocket`s created after this method was called will be routed. It is recommended to call this
method before navigating the page.

**Usage**

Below is an example of a simple mock that responds to a single message. See `WebSocketRoute` for more details and
examples.

```py
def message_handler(ws: WebSocketRoute, message: Union[str, bytes]):
  if message == "request":
    ws.send("response")

def handler(ws: WebSocketRoute):
  ws.on_message(lambda message: message_handler(ws, message))

await page.route_web_socket("/ws", handler)
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url` | Union[Callable[[str], bool], Pattern[str], str] | Only WebSockets with the url matching this pattern will be routed. A string pattern can be relative to the `base_url` context option. |
| `handler` | Callable[[WebSocketRoute], Any] | Handler function to route the WebSocket. |

## screencast

属性，直接读取；异步入口也不加 await。

```python signature
Page.screencast: Screencast
```

Page.screencast

`Screencast` object associated with this page.

**Usage**

#### Returns
Screencast


## screenshot

### 同步

```python signature
def screenshot(self, *, animations: Optional[Literal['allow', 'disabled']] = None, caret: Optional[Literal['hide', 'initial']] = None, clip: Optional[patchright._impl._api_structures.FloatRect] = None, full_page: Optional[bool] = None, mask: Optional[Sequence[ForwardRef('Locator')]] = None, mask_color: Optional[str] = None, omit_background: Optional[bool] = None, path: Union[pathlib.Path, str, NoneType] = None, quality: Optional[int] = None, scale: Optional[Literal['css', 'device']] = None, style: Optional[str] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, type: Optional[Literal['jpeg', 'png', 'webp']] = None) -> bytes
```

Page.screenshot

Returns the buffer with the captured screenshot.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `animations` | Union["allow", "disabled", None] | When set to `"disabled"`, stops CSS animations, CSS transitions and Web Animations. Animations get different treatment depending on their duration: - finite animations are fast-forwarded to completion, so they'll fire `transitionend` event. - infinite animations are canceled to initial state, and then played over after the screenshot.  Defaults to `"allow"` that leaves animations untouched. |
| `caret` | Union["hide", "initial", None] | When set to `"hide"`, screenshot will hide text caret. When set to `"initial"`, text caret behavior will not be changed.  Defaults to `"hide"`. |
| `clip` | Union[{x: float, y: float, width: float, height: float}, None] | An object which specifies clipping of the resulting image. |
| `full_page` | Union[bool, None] | When true, takes a screenshot of the full scrollable page, instead of the currently visible viewport. Defaults to `false`. |
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
async def screenshot(self, *, animations: Optional[Literal['allow', 'disabled']] = None, caret: Optional[Literal['hide', 'initial']] = None, clip: Optional[patchright._impl._api_structures.FloatRect] = None, full_page: Optional[bool] = None, mask: Optional[Sequence[ForwardRef('Locator')]] = None, mask_color: Optional[str] = None, omit_background: Optional[bool] = None, path: Union[pathlib.Path, str, NoneType] = None, quality: Optional[int] = None, scale: Optional[Literal['css', 'device']] = None, style: Optional[str] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, type: Optional[Literal['jpeg', 'png', 'webp']] = None) -> bytes
```

Page.screenshot

Returns the buffer with the captured screenshot.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `animations` | Union["allow", "disabled", None] | When set to `"disabled"`, stops CSS animations, CSS transitions and Web Animations. Animations get different treatment depending on their duration: - finite animations are fast-forwarded to completion, so they'll fire `transitionend` event. - infinite animations are canceled to initial state, and then played over after the screenshot.  Defaults to `"allow"` that leaves animations untouched. |
| `caret` | Union["hide", "initial", None] | When set to `"hide"`, screenshot will hide text caret. When set to `"initial"`, text caret behavior will not be changed.  Defaults to `"hide"`. |
| `clip` | Union[{x: float, y: float, width: float, height: float}, None] | An object which specifies clipping of the resulting image. |
| `full_page` | Union[bool, None] | When true, takes a screenshot of the full scrollable page, instead of the currently visible viewport. Defaults to `false`. |
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


## select_option

### 同步

```python signature
def select_option(self, selector: str, value: Union[str, Sequence[str], NoneType] = None, *, element: Union[ForwardRef('ElementHandle'), Sequence[ForwardRef('ElementHandle')], NoneType] = None, force: Optional[bool] = None, index: Union[int, Sequence[int], NoneType] = None, label: Union[str, Sequence[str], NoneType] = None, no_wait_after: Optional[bool] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> List[str]
```

Page.select_option

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
page.select_option("select#colors", "blue")
# single selection matching both the label
page.select_option("select#colors", label="blue")
# multiple selection
page.select_option("select#colors", value=["red", "green", "blue"])
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
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

Page.select_option

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
await page.select_option("select#colors", "blue")
# single selection matching the label
await page.select_option("select#colors", label="blue")
# multiple selection
await page.select_option("select#colors", value=["red", "green", "blue"])
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to search for an element. If there are multiple elements satisfying the selector, the first will be used. |
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


## session_storage

属性，直接读取；异步入口也不加 await。

```python signature
Page.session_storage: WebStorage
```

Page.session_storage

Provides access to the page's `sessionStorage` for the current origin. See `WebStorage`.

#### Returns
WebStorage


## set_checked

### 同步

```python signature
def set_checked(self, selector: str, checked: bool, *, force: Optional[bool] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

Page.set_checked

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

Page.set_checked

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

Page.set_content

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

Page.set_content

This method internally calls [document.write()](https://developer.mozilla.org/en-US/docs/Web/API/Document/write),
inheriting all its specific characteristics and behaviors.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `html` | str | HTML markup to assign to the page. |
| `timeout` | Union[float, None] | Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_navigation_timeout()`, `browser_context.set_default_timeout()`, `page.set_default_navigation_timeout()` or `page.set_default_timeout()` methods. |
| `wait_until` | Union["commit", "domcontentloaded", "load", "networkidle", None] | When to consider operation succeeded, defaults to `load`. Events can be either: - `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired. - `'load'` - consider operation to be finished when the `load` event is fired. - `'networkidle'` - **DISCOURAGED** consider operation to be finished when there are no network connections for at least `500` ms. Don't use this method for testing, rely on web assertions to assess readiness instead. - `'commit'` - consider operation to be finished when network response is received and the document started loading. |

## set_default_navigation_timeout

### 同步

```python
def set_default_navigation_timeout(self, timeout: Union[float, datetime.timedelta]) -> None
```

Page.set_default_navigation_timeout

This setting will change the default maximum navigation time for the following methods and related shortcuts:
- `page.go_back()`
- `page.go_forward()`
- `page.goto()`
- `page.reload()`
- `page.set_content()`
- `page.expect_navigation()`
- `page.wait_for_url()`

**NOTE** `page.set_default_navigation_timeout()` takes priority over `page.set_default_timeout()`,
`browser_context.set_default_timeout()` and `browser_context.set_default_navigation_timeout()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | float | Maximum navigation time in milliseconds |

### 异步

```python
def set_default_navigation_timeout(self, timeout: Union[float, datetime.timedelta]) -> None
```

Page.set_default_navigation_timeout

This setting will change the default maximum navigation time for the following methods and related shortcuts:
- `page.go_back()`
- `page.go_forward()`
- `page.goto()`
- `page.reload()`
- `page.set_content()`
- `page.expect_navigation()`
- `page.wait_for_url()`

**NOTE** `page.set_default_navigation_timeout()` takes priority over `page.set_default_timeout()`,
`browser_context.set_default_timeout()` and `browser_context.set_default_navigation_timeout()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | float | Maximum navigation time in milliseconds |

## set_default_timeout

### 同步

```python
def set_default_timeout(self, timeout: Union[float, datetime.timedelta]) -> None
```

Page.set_default_timeout

This setting will change the default maximum time for all the methods accepting `timeout` option.

**NOTE** `page.set_default_navigation_timeout()` takes priority over `page.set_default_timeout()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | float | Maximum time in milliseconds. Pass `0` to disable timeout. |

### 异步

```python
def set_default_timeout(self, timeout: Union[float, datetime.timedelta]) -> None
```

Page.set_default_timeout

This setting will change the default maximum time for all the methods accepting `timeout` option.

**NOTE** `page.set_default_navigation_timeout()` takes priority over `page.set_default_timeout()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | float | Maximum time in milliseconds. Pass `0` to disable timeout. |

## set_extra_http_headers

### 同步

```python
def set_extra_http_headers(self, headers: Dict[str, str]) -> None
```

Page.set_extra_http_headers

The extra HTTP headers will be sent with every request the page initiates.

**NOTE** `page.set_extra_http_headers()` does not guarantee the order of headers in the outgoing requests.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `headers` | Dict[str, str] | An object containing additional HTTP headers to be sent with every request. All header values must be strings. |

### 异步

```python
async def set_extra_http_headers(self, headers: Dict[str, str]) -> None
```

Page.set_extra_http_headers

The extra HTTP headers will be sent with every request the page initiates.

**NOTE** `page.set_extra_http_headers()` does not guarantee the order of headers in the outgoing requests.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `headers` | Dict[str, str] | An object containing additional HTTP headers to be sent with every request. All header values must be strings. |

## set_input_files

### 同步

```python signature
def set_input_files(self, selector: str, files: Union[str, pathlib.Path, Sequence[Union[str, pathlib.Path]], patchright._impl._api_structures.FilePayload, Sequence[patchright._impl._api_structures.FilePayload]], *, no_wait_after: Optional[bool] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Page.set_input_files

Sets the value of the file input to these file paths or files. If some of the `filePaths` are relative paths, then
they are resolved relative to the current working directory. For empty array, clears the selected files. For inputs
with a `[webkitdirectory]` attribute, only a single directory path is supported.

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

Page.set_input_files

Sets the value of the file input to these file paths or files. If some of the `filePaths` are relative paths, then
they are resolved relative to the current working directory. For empty array, clears the selected files. For inputs
with a `[webkitdirectory]` attribute, only a single directory path is supported.

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

## set_viewport_size

### 同步

```python
def set_viewport_size(self, viewport_size: patchright._impl._api_structures.ViewportSize) -> None
```

Page.set_viewport_size

In the case of multiple pages in a single browser, each page can have its own viewport size. However,
`browser.new_context()` allows to set viewport size (and more) for all pages in the context at once.

`page.set_viewport_size()` will resize the page. A lot of websites don't expect phones to change size, so you
should set the viewport size before navigating to the page. `page.set_viewport_size()` will also reset `screen`
size, use `browser.new_context()` with `screen` and `viewport` parameters if you need better control of these
properties.

**Usage**

```py
page = browser.new_page()
page.set_viewport_size({"width": 640, "height": 480})
page.goto("https://example.com")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `viewport_size` | {width: int, height: int} |  |

### 异步

```python
async def set_viewport_size(self, viewport_size: patchright._impl._api_structures.ViewportSize) -> None
```

Page.set_viewport_size

In the case of multiple pages in a single browser, each page can have its own viewport size. However,
`browser.new_context()` allows to set viewport size (and more) for all pages in the context at once.

`page.set_viewport_size()` will resize the page. A lot of websites don't expect phones to change size, so you
should set the viewport size before navigating to the page. `page.set_viewport_size()` will also reset `screen`
size, use `browser.new_context()` with `screen` and `viewport` parameters if you need better control of these
properties.

**Usage**

```py
page = await browser.new_page()
await page.set_viewport_size({"width": 640, "height": 480})
await page.goto("https://example.com")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `viewport_size` | {width: int, height: int} |  |

## tap

### 同步

```python signature
def tap(self, selector: str, *, force: Optional[bool] = None, modifiers: Optional[Sequence[Literal['Alt', 'Control', 'ControlOrMeta', 'Meta', 'Shift']]] = None, no_wait_after: Optional[bool] = None, position: Optional[patchright._impl._api_structures.Position] = None, scroll: Optional[Literal['auto', 'none']] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, trial: Optional[bool] = None) -> None
```

Page.tap

This method taps an element matching `selector` by performing the following steps:
1. Find an element matching `selector`. If there is none, wait until a matching element is attached to the DOM.
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the matched element, unless `force` option is set. If
   the element is detached during the checks, the whole action is retried.
1. Scroll the element into view if needed.
1. Use `page.touchscreen` to tap the center of the element, or the specified `position`.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

**NOTE** `page.tap()` will throw if the `has_touch` option of the browser context is false.

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

Page.tap

This method taps an element matching `selector` by performing the following steps:
1. Find an element matching `selector`. If there is none, wait until a matching element is attached to the DOM.
1. Wait for [actionability](https://playwright.dev/python/docs/actionability) checks on the matched element, unless `force` option is set. If
   the element is detached during the checks, the whole action is retried.
1. Scroll the element into view if needed.
1. Use `page.touchscreen` to tap the center of the element, or the specified `position`.

When all steps combined have not finished during the specified `timeout`, this method throws a `TimeoutError`.
Passing zero timeout disables this.

**NOTE** `page.tap()` will throw if the `has_touch` option of the browser context is false.

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

Page.text_content

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

Page.text_content

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

Page.title

Returns the page's title.

#### Returns
str

### 异步

```python
async def title(self) -> str
```

Page.title

Returns the page's title.

#### Returns
str


## touchscreen

属性，直接读取；异步入口也不加 await。

```python signature
Page.touchscreen: Touchscreen
```

Page.touchscreen

#### Returns
Touchscreen


## type

### 同步

```python signature
def type(self, selector: str, text: str, *, delay: Optional[float] = None, no_wait_after: Optional[bool] = None, strict: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

Page.type

Sends a `keydown`, `keypress`/`input`, and `keyup` event for each character in the text. `page.type` can be used to
send fine-grained keyboard events. To fill values in form fields, use `page.fill()`.

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

Page.type

Sends a `keydown`, `keypress`/`input`, and `keyup` event for each character in the text. `page.type` can be used to
send fine-grained keyboard events. To fill values in form fields, use `page.fill()`.

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

Page.uncheck

This method unchecks an element matching `selector` by performing the following steps:
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

Page.uncheck

This method unchecks an element matching `selector` by performing the following steps:
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

## unroute

### 同步

```python
def unroute(self, url: Union[str, Pattern[str], Callable[[str], bool]], handler: Union[Callable[[ForwardRef('Route')], Any], Callable[[ForwardRef('Route'), ForwardRef('Request')], Any], NoneType] = None) -> None
```

Page.unroute

Removes a route created with `page.route()`. When `handler` is not specified, removes all routes for the `url`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url` | Union[Callable[[str], bool], Pattern[str], str] | A glob pattern, regex pattern, or predicate receiving [URL] to match while routing. |
| `handler` | Union[Callable[[Route, Request], Any], Callable[[Route], Any], None] | Optional handler function to route the request. |

### 异步

```python
async def unroute(self, url: Union[str, Pattern[str], Callable[[str], bool]], handler: Union[Callable[[ForwardRef('Route')], Any], Callable[[ForwardRef('Route'), ForwardRef('Request')], Any], NoneType] = None) -> None
```

Page.unroute

Removes a route created with `page.route()`. When `handler` is not specified, removes all routes for the `url`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url` | Union[Callable[[str], bool], Pattern[str], str] | A glob pattern, regex pattern, or predicate receiving [URL] to match while routing. |
| `handler` | Union[Callable[[Route, Request], Any], Callable[[Route], Any], None] | Optional handler function to route the request. |

## unroute_all

### 同步

```python signature
def unroute_all(self, *, behavior: Optional[Literal['default', 'ignoreErrors', 'wait']] = None) -> None
```

Page.unroute_all

Removes all routes created with `page.route()` and `page.route_from_har()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `behavior` | Union["default", "ignoreErrors", "wait", None] | Specifies whether to wait for already running handlers and what to do if they throw errors: - `'default'` - do not wait for current handler calls (if any) to finish, if unrouted handler throws, it may result in unhandled error - `'wait'` - wait for current handler calls (if any) to finish - `'ignoreErrors'` - do not wait for current handler calls (if any) to finish, all errors thrown by the handlers after unrouting are silently caught |

### 异步

```python signature
async def unroute_all(self, *, behavior: Optional[Literal['default', 'ignoreErrors', 'wait']] = None) -> None
```

Page.unroute_all

Removes all routes created with `page.route()` and `page.route_from_har()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `behavior` | Union["default", "ignoreErrors", "wait", None] | Specifies whether to wait for already running handlers and what to do if they throw errors: - `'default'` - do not wait for current handler calls (if any) to finish, if unrouted handler throws, it may result in unhandled error - `'wait'` - wait for current handler calls (if any) to finish - `'ignoreErrors'` - do not wait for current handler calls (if any) to finish, all errors thrown by the handlers after unrouting are silently caught |

## url

属性，直接读取；异步入口也不加 await。

```python signature
Page.url: <class 'str'>
```

Page.url

#### Returns
str


## video

属性，直接读取；异步入口也不加 await。

```python signature
Page.video: typing.Optional[ForwardRef('Video')]
```

Page.video

Video object associated with this page. Can be used to access the video file when using the `recordVideo` context
option.

#### Returns
Union[Video, None]


## viewport_size

属性，直接读取；异步入口也不加 await。

```python signature
Page.viewport_size: typing.Optional[patchright._impl._api_structures.ViewportSize]
```

Page.viewport_size

#### Returns
Union[{width: int, height: int}, None]


## wait_for_event

### 同步

```python signature
def wait_for_event(self, event: str, predicate: Optional[Callable] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Any
```

支持的重载：

```python signature
def wait_for_event(self, event: Literal['close'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> 'Page'
def wait_for_event(self, event: Literal['console'], predicate: Optional[Callable[[ForwardRef('ConsoleMessage')], bool]] = None, *, timeout: Optional[float] = None) -> 'ConsoleMessage'
def wait_for_event(self, event: Literal['crash'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> 'Page'
def wait_for_event(self, event: Literal['dialog'], predicate: Optional[Callable[[ForwardRef('Dialog')], bool]] = None, *, timeout: Optional[float] = None) -> 'Dialog'
def wait_for_event(self, event: Literal['dialogclosed'], predicate: Optional[Callable[[ForwardRef('Dialog')], bool]] = None, *, timeout: Optional[float] = None) -> 'Dialog'
def wait_for_event(self, event: Literal['domcontentloaded'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> 'Page'
def wait_for_event(self, event: Literal['download'], predicate: Optional[Callable[[ForwardRef('Download')], bool]] = None, *, timeout: Optional[float] = None) -> 'Download'
def wait_for_event(self, event: Literal['filechooser'], predicate: Optional[Callable[[ForwardRef('FileChooser')], bool]] = None, *, timeout: Optional[float] = None) -> 'FileChooser'
def wait_for_event(self, event: Literal['frameattached'], predicate: Optional[Callable[[ForwardRef('Frame')], bool]] = None, *, timeout: Optional[float] = None) -> 'Frame'
def wait_for_event(self, event: Literal['framedetached'], predicate: Optional[Callable[[ForwardRef('Frame')], bool]] = None, *, timeout: Optional[float] = None) -> 'Frame'
def wait_for_event(self, event: Literal['framenavigated'], predicate: Optional[Callable[[ForwardRef('Frame')], bool]] = None, *, timeout: Optional[float] = None) -> 'Frame'
def wait_for_event(self, event: Literal['load'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> 'Page'
def wait_for_event(self, event: Literal['pageerror'], predicate: Optional[Callable[[ForwardRef('Error')], bool]] = None, *, timeout: Optional[float] = None) -> 'Error'
def wait_for_event(self, event: Literal['popup'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> 'Page'
def wait_for_event(self, event: Literal['request'], predicate: Optional[Callable[[ForwardRef('Request')], bool]] = None, *, timeout: Optional[float] = None) -> 'Request'
def wait_for_event(self, event: Literal['requestfailed'], predicate: Optional[Callable[[ForwardRef('Request')], bool]] = None, *, timeout: Optional[float] = None) -> 'Request'
def wait_for_event(self, event: Literal['requestfinished'], predicate: Optional[Callable[[ForwardRef('Request')], bool]] = None, *, timeout: Optional[float] = None) -> 'Request'
def wait_for_event(self, event: Literal['response'], predicate: Optional[Callable[[ForwardRef('Response')], bool]] = None, *, timeout: Optional[float] = None) -> 'Response'
def wait_for_event(self, event: Literal['websocket'], predicate: Optional[Callable[[ForwardRef('WebSocket')], bool]] = None, *, timeout: Optional[float] = None) -> 'WebSocket'
def wait_for_event(self, event: Literal['worker'], predicate: Optional[Callable[[ForwardRef('Worker')], bool]] = None, *, timeout: Optional[float] = None) -> 'Worker'
def wait_for_event(self, event: str, predicate: Optional[Callable[..., bool]] = None, *, timeout: Optional[float] = None) -> Any
```

Page.wait_for_event

**NOTE** In most cases, you should use `page.expect_event()`.

Waits for given `event` to fire. If predicate is provided, it passes event's value into the `predicate` function
and waits for `predicate(event)` to return a truthy value. Will throw an error if the page is closed before the
`event` is fired.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `event` | str | Event name, same one typically passed into `*.on(event)`. |
| `predicate` | Union[Callable, None] | Receives the event data and resolves to truthy value when the waiting should resolve. |
| `timeout` | Union[float, None] | Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()`. |

#### Returns
Any

### 异步

```python signature
async def wait_for_event(self, event: str, predicate: Optional[Callable] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Any
```

支持的重载：

```python signature
def wait_for_event(self, event: Literal['close'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> 'Page'
def wait_for_event(self, event: Literal['console'], predicate: Optional[Callable[[ForwardRef('ConsoleMessage')], bool]] = None, *, timeout: Optional[float] = None) -> 'ConsoleMessage'
def wait_for_event(self, event: Literal['crash'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> 'Page'
def wait_for_event(self, event: Literal['dialog'], predicate: Optional[Callable[[ForwardRef('Dialog')], bool]] = None, *, timeout: Optional[float] = None) -> 'Dialog'
def wait_for_event(self, event: Literal['dialogclosed'], predicate: Optional[Callable[[ForwardRef('Dialog')], bool]] = None, *, timeout: Optional[float] = None) -> 'Dialog'
def wait_for_event(self, event: Literal['domcontentloaded'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> 'Page'
def wait_for_event(self, event: Literal['download'], predicate: Optional[Callable[[ForwardRef('Download')], bool]] = None, *, timeout: Optional[float] = None) -> 'Download'
def wait_for_event(self, event: Literal['filechooser'], predicate: Optional[Callable[[ForwardRef('FileChooser')], bool]] = None, *, timeout: Optional[float] = None) -> 'FileChooser'
def wait_for_event(self, event: Literal['frameattached'], predicate: Optional[Callable[[ForwardRef('Frame')], bool]] = None, *, timeout: Optional[float] = None) -> 'Frame'
def wait_for_event(self, event: Literal['framedetached'], predicate: Optional[Callable[[ForwardRef('Frame')], bool]] = None, *, timeout: Optional[float] = None) -> 'Frame'
def wait_for_event(self, event: Literal['framenavigated'], predicate: Optional[Callable[[ForwardRef('Frame')], bool]] = None, *, timeout: Optional[float] = None) -> 'Frame'
def wait_for_event(self, event: Literal['load'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> 'Page'
def wait_for_event(self, event: Literal['pageerror'], predicate: Optional[Callable[[ForwardRef('Error')], bool]] = None, *, timeout: Optional[float] = None) -> 'Error'
def wait_for_event(self, event: Literal['popup'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> 'Page'
def wait_for_event(self, event: Literal['request'], predicate: Optional[Callable[[ForwardRef('Request')], bool]] = None, *, timeout: Optional[float] = None) -> 'Request'
def wait_for_event(self, event: Literal['requestfailed'], predicate: Optional[Callable[[ForwardRef('Request')], bool]] = None, *, timeout: Optional[float] = None) -> 'Request'
def wait_for_event(self, event: Literal['requestfinished'], predicate: Optional[Callable[[ForwardRef('Request')], bool]] = None, *, timeout: Optional[float] = None) -> 'Request'
def wait_for_event(self, event: Literal['response'], predicate: Optional[Callable[[ForwardRef('Response')], bool]] = None, *, timeout: Optional[float] = None) -> 'Response'
def wait_for_event(self, event: Literal['websocket'], predicate: Optional[Callable[[ForwardRef('WebSocket')], bool]] = None, *, timeout: Optional[float] = None) -> 'WebSocket'
def wait_for_event(self, event: Literal['worker'], predicate: Optional[Callable[[ForwardRef('Worker')], bool]] = None, *, timeout: Optional[float] = None) -> 'Worker'
def wait_for_event(self, event: str, predicate: Optional[Callable[..., bool]] = None, *, timeout: Optional[float] = None) -> Any
```

Page.wait_for_event

**NOTE** In most cases, you should use `page.expect_event()`.

Waits for given `event` to fire. If predicate is provided, it passes event's value into the `predicate` function
and waits for `predicate(event)` to return a truthy value. Will throw an error if the page is closed before the
`event` is fired.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `event` | str | Event name, same one typically passed into `*.on(event)`. |
| `predicate` | Union[Callable, None] | Receives the event data and resolves to truthy value when the waiting should resolve. |
| `timeout` | Union[float, None] | Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()`. |

#### Returns
Any


## wait_for_function

### 同步

```python signature
def wait_for_function(self, expression: str, *, arg: Optional[Any] = None, polling: Union[float, Literal['raf'], NoneType] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'JSHandle'
```

Page.wait_for_function

Returns when the `expression` returns a truthy value. It resolves to a JSHandle of the truthy value.

**Usage**

The `page.wait_for_function()` can be used to observe viewport size change:

```py
from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    webkit = playwright.webkit
    browser = webkit.launch()
    page = browser.new_page()
    page.evaluate("window.x = 0; setTimeout(() => { window.x = 100 }, 1000);")
    page.wait_for_function("() => window.x > 0")
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
```

To pass an argument to the predicate of `page.wait_for_function()` function:

```py
selector = ".foo"
page.wait_for_function("selector => !!document.querySelector(selector)", selector)
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

Page.wait_for_function

Returns when the `expression` returns a truthy value. It resolves to a JSHandle of the truthy value.

**Usage**

The `page.wait_for_function()` can be used to observe viewport size change:

```py
import asyncio
from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    webkit = playwright.webkit
    browser = await webkit.launch()
    page = await browser.new_page()
    await page.evaluate("window.x = 0; setTimeout(() => { window.x = 100 }, 1000);")
    await page.wait_for_function("() => window.x > 0")
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)
asyncio.run(main())
```

To pass an argument to the predicate of `page.wait_for_function()` function:

```py
selector = ".foo"
await page.wait_for_function("selector => !!document.querySelector(selector)", selector)
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

Page.wait_for_load_state

Returns when the required load state has been reached.

This resolves when the page reaches a required load state, `load` by default. The navigation must have been
committed when this method is called. If current document has already reached the required state, resolves
immediately.

**NOTE** Most of the time, this method is not needed because Playwright
[auto-waits before every action](https://playwright.dev/python/docs/actionability).

**Usage**

```py
page.get_by_role("button").click() # click triggers navigation.
page.wait_for_load_state() # the promise resolves after "load" event.
```

```py
with page.expect_popup() as page_info:
    page.get_by_role("button").click() # click triggers a popup.
popup = page_info.value
# Wait for the "DOMContentLoaded" event.
popup.wait_for_load_state("domcontentloaded")
print(popup.title()) # popup is ready to use.
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

Page.wait_for_load_state

Returns when the required load state has been reached.

This resolves when the page reaches a required load state, `load` by default. The navigation must have been
committed when this method is called. If current document has already reached the required state, resolves
immediately.

**NOTE** Most of the time, this method is not needed because Playwright
[auto-waits before every action](https://playwright.dev/python/docs/actionability).

**Usage**

```py
await page.get_by_role("button").click() # click triggers navigation.
await page.wait_for_load_state() # the promise resolves after "load" event.
```

```py
async with page.expect_popup() as page_info:
    await page.get_by_role("button").click() # click triggers a popup.
popup = await page_info.value
# Wait for the "DOMContentLoaded" event.
await popup.wait_for_load_state("domcontentloaded")
print(await popup.title()) # popup is ready to use.
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

Page.wait_for_selector

Returns when element specified by selector satisfies `state` option. Returns `null` if waiting for `hidden` or
`detached`.

**NOTE** Playwright automatically waits for element to be ready before performing an action. Using `Locator`
objects and web-first assertions makes the code wait-for-selector-free.

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
        element = page.wait_for_selector("img")
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

Page.wait_for_selector

Returns when element specified by selector satisfies `state` option. Returns `null` if waiting for `hidden` or
`detached`.

**NOTE** Playwright automatically waits for element to be ready before performing an action. Using `Locator`
objects and web-first assertions makes the code wait-for-selector-free.

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
        element = await page.wait_for_selector("img")
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

Page.wait_for_timeout

Waits for the given `timeout` in milliseconds.

Note that `page.waitForTimeout()` should only be used for debugging. Tests using the timer in production are going
to be flaky. Use signals such as network events, selectors becoming visible and others instead.

**Usage**

```py
# wait for 1 second
page.wait_for_timeout(1000)
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | float | A timeout to wait for |

### 异步

```python
async def wait_for_timeout(self, timeout: Union[float, datetime.timedelta]) -> None
```

Page.wait_for_timeout

Waits for the given `timeout` in milliseconds.

Note that `page.waitForTimeout()` should only be used for debugging. Tests using the timer in production are going
to be flaky. Use signals such as network events, selectors becoming visible and others instead.

**Usage**

```py
# wait for 1 second
await page.wait_for_timeout(1000)
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | float | A timeout to wait for |

## wait_for_url

### 同步

```python signature
def wait_for_url(self, url: Union[str, Pattern[str], Callable[[str], bool]], *, timeout: Union[float, datetime.timedelta, NoneType] = None, wait_until: Optional[Literal['commit', 'domcontentloaded', 'load', 'networkidle']] = None) -> None
```

Page.wait_for_url

Waits for the main frame to navigate to the given URL.

**Usage**

```py
page.click("a.delayed-navigation") # clicking the link will indirectly cause a navigation
page.wait_for_url("**/target.html")
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

Page.wait_for_url

Waits for the main frame to navigate to the given URL.

**Usage**

```py
await page.click("a.delayed-navigation") # clicking the link will indirectly cause a navigation
await page.wait_for_url("**/target.html")
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
Page.webmcp: WebMCP
```

Page.webmcp

Tools that the main frame registers through the experimental `WebMCP` browser API. Shortcut for `frame.webmcp` of
`page.main_frame`, see `WebMCP` for details.

**Usage**

#### Returns
WebMCP


## workers

属性，直接读取；异步入口也不加 await。

```python signature
Page.workers: typing.List[ForwardRef('Worker')]
```

Page.workers

This method returns all of the dedicated
[WebWorkers](https://developer.mozilla.org/en-US/docs/Web/API/Web_Workers_API) associated with the page.

**NOTE** This does not contain ServiceWorkers

#### Returns
List[Worker]
