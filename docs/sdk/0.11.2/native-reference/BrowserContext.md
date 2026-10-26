# 原生 BrowserContext

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [add_cookies](#add_cookies)
- [add_init_script](#add_init_script)
- [background_pages](#background_pages)
- [browser](#browser)
- [clear_cookies](#clear_cookies)
- [clear_permissions](#clear_permissions)
- [clock](#clock)
- [close](#close)
- [cookies](#cookies)
- [credentials](#credentials)
- [debugger](#debugger)
- [expect_console_message](#expect_console_message)
- [expect_event](#expect_event)
- [expect_page](#expect_page)
- [expose_binding](#expose_binding)
- [expose_function](#expose_function)
- [grant_permissions](#grant_permissions)
- [is_closed](#is_closed)
- [new_cdp_session](#new_cdp_session)
- [new_page](#new_page)
- [on](#on)
- [once](#once)
- [pages](#pages)
- [remove_listener](#remove_listener)
- [request](#request)
- [route](#route)
- [route_from_har](#route_from_har)
- [route_web_socket](#route_web_socket)
- [service_workers](#service_workers)
- [set_default_navigation_timeout](#set_default_navigation_timeout)
- [set_default_timeout](#set_default_timeout)
- [set_extra_http_headers](#set_extra_http_headers)
- [set_geolocation](#set_geolocation)
- [set_offline](#set_offline)
- [set_storage_state](#set_storage_state)
- [storage_state](#storage_state)
- [tracing](#tracing)
- [unroute](#unroute)
- [unroute_all](#unroute_all)
- [wait_for_event](#wait_for_event)

## add_cookies

### 同步

```python
def add_cookies(self, cookies: Sequence[patchright._impl._api_structures.SetCookieParam]) -> None
```

BrowserContext.add_cookies

Adds cookies into this browser context. All pages within this context will have these cookies installed. Cookies
can be obtained via `browser_context.cookies()`.

**Usage**

```py
browser_context.add_cookies([cookie_object1, cookie_object2])
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `cookies` | Sequence[{name: str, value: str, url: Union[str, None], domain: Union[str, None], path: Union[str, None], expires: Union[float, None], httpOnly: Union[bool, None], secure: Union[bool, None], sameSite: Union["Lax", "None", "Strict", None], partitionKey: Union[str, None]}] |  |

### 异步

```python
async def add_cookies(self, cookies: Sequence[patchright._impl._api_structures.SetCookieParam]) -> None
```

BrowserContext.add_cookies

Adds cookies into this browser context. All pages within this context will have these cookies installed. Cookies
can be obtained via `browser_context.cookies()`.

**Usage**

```py
await browser_context.add_cookies([cookie_object1, cookie_object2])
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `cookies` | Sequence[{name: str, value: str, url: Union[str, None], domain: Union[str, None], path: Union[str, None], expires: Union[float, None], httpOnly: Union[bool, None], secure: Union[bool, None], sameSite: Union["Lax", "None", "Strict", None], partitionKey: Union[str, None]}] |  |

## add_init_script

### 同步

```python signature
def add_init_script(self, script: Optional[str] = None, *, path: Union[pathlib.Path, str, NoneType] = None) -> 'SyncContextManager'
```

BrowserContext.add_init_script

Adds a script which would be evaluated in one of the following scenarios:
- Whenever a page is created in the browser context or is navigated.
- Whenever a child frame is attached or navigated in any page in the browser context. In this case, the script is
  evaluated in the context of the newly attached frame.

The script is evaluated after the document was created but before any of its scripts were run. This is useful to
amend the JavaScript environment, e.g. to seed `Math.random`.

**Usage**

An example of overriding `Math.random` before the page loads:

```py
# in your playwright script, assuming the preload.js file is in same directory.
browser_context.add_init_script(path="preload.js")
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

BrowserContext.add_init_script

Adds a script which would be evaluated in one of the following scenarios:
- Whenever a page is created in the browser context or is navigated.
- Whenever a child frame is attached or navigated in any page in the browser context. In this case, the script is
  evaluated in the context of the newly attached frame.

The script is evaluated after the document was created but before any of its scripts were run. This is useful to
amend the JavaScript environment, e.g. to seed `Math.random`.

**Usage**

An example of overriding `Math.random` before the page loads:

```py
# in your playwright script, assuming the preload.js file is in same directory.
await browser_context.add_init_script(path="preload.js")
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


## background_pages

属性，直接读取；异步入口也不加 await。

```python signature
BrowserContext.background_pages: typing.List[ForwardRef('Page')]
```

BrowserContext.background_pages

Returns an empty list.

#### Returns
List[Page]


## browser

属性，直接读取；异步入口也不加 await。

```python signature
BrowserContext.browser: typing.Optional[ForwardRef('Browser')]
```

BrowserContext.browser

Gets the browser instance that owns the context. Returns `null` if the context is created outside of normal
browser, e.g. Android or Electron.

#### Returns
Union[Browser, None]


## clear_cookies

### 同步

```python signature
def clear_cookies(self, *, domain: Union[str, Pattern[str], NoneType] = None, name: Union[str, Pattern[str], NoneType] = None, path: Union[str, Pattern[str], NoneType] = None) -> None
```

BrowserContext.clear_cookies

Removes cookies from context. Accepts optional filter.

**Usage**

```py
context.clear_cookies()
context.clear_cookies(name="session-id")
context.clear_cookies(domain="my-origin.com")
context.clear_cookies(path="/api/v1")
context.clear_cookies(name="session-id", domain="my-origin.com")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `domain` | Union[Pattern[str], str, None] | Only removes cookies with the given domain. |
| `name` | Union[Pattern[str], str, None] | Only removes cookies with the given name. |
| `path` | Union[Pattern[str], str, None] | Only removes cookies with the given path. |

### 异步

```python signature
async def clear_cookies(self, *, domain: Union[str, Pattern[str], NoneType] = None, name: Union[str, Pattern[str], NoneType] = None, path: Union[str, Pattern[str], NoneType] = None) -> None
```

BrowserContext.clear_cookies

Removes cookies from context. Accepts optional filter.

**Usage**

```py
await context.clear_cookies()
await context.clear_cookies(name="session-id")
await context.clear_cookies(domain="my-origin.com")
await context.clear_cookies(path="/api/v1")
await context.clear_cookies(name="session-id", domain="my-origin.com")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `domain` | Union[Pattern[str], str, None] | Only removes cookies with the given domain. |
| `name` | Union[Pattern[str], str, None] | Only removes cookies with the given name. |
| `path` | Union[Pattern[str], str, None] | Only removes cookies with the given path. |

## clear_permissions

### 同步

```python
def clear_permissions(self) -> None
```

BrowserContext.clear_permissions

Clears all permission overrides for the browser context.

**Usage**

```py
context = browser.new_context()
context.grant_permissions(["clipboard-read"])
# do stuff ..
context.clear_permissions()
```

### 异步

```python
async def clear_permissions(self) -> None
```

BrowserContext.clear_permissions

Clears all permission overrides for the browser context.

**Usage**

```py
context = await browser.new_context()
await context.grant_permissions(["clipboard-read"])
# do stuff ..
context.clear_permissions()
```


## clock

属性，直接读取；异步入口也不加 await。

```python signature
BrowserContext.clock: Clock
```

BrowserContext.clock

Playwright has ability to mock clock and passage of time.

#### Returns
Clock


## close

### 同步

```python signature
def close(self, *, reason: Optional[str] = None) -> None
```

BrowserContext.close

Closes the browser context. All the pages that belong to the browser context will be closed.

**NOTE** The default browser context cannot be closed.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `reason` | Union[str, None] | The reason to be reported to the operations interrupted by the context closure. |

### 异步

```python signature
async def close(self, *, reason: Optional[str] = None) -> None
```

BrowserContext.close

Closes the browser context. All the pages that belong to the browser context will be closed.

**NOTE** The default browser context cannot be closed.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `reason` | Union[str, None] | The reason to be reported to the operations interrupted by the context closure. |

## cookies

### 同步

```python
def cookies(self, urls: Union[str, Sequence[str], NoneType] = None) -> List[patchright._impl._api_structures.Cookie]
```

BrowserContext.cookies

If no URLs are specified, this method returns all cookies. If URLs are specified, only cookies that affect those
URLs are returned.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `urls` | Union[Sequence[str], str, None] | Optional list of URLs. |

#### Returns
List[{name: str, value: str, domain: str, path: str, expires: float, httpOnly: bool, secure: bool, sameSite: Union["Lax", "None", "Strict"], partitionKey: Union[str, None]}]

### 异步

```python
async def cookies(self, urls: Union[str, Sequence[str], NoneType] = None) -> List[patchright._impl._api_structures.Cookie]
```

BrowserContext.cookies

If no URLs are specified, this method returns all cookies. If URLs are specified, only cookies that affect those
URLs are returned.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `urls` | Union[Sequence[str], str, None] | Optional list of URLs. |

#### Returns
List[{name: str, value: str, domain: str, path: str, expires: float, httpOnly: bool, secure: bool, sameSite: Union["Lax", "None", "Strict"], partitionKey: Union[str, None]}]


## credentials

属性，直接读取；异步入口也不加 await。

```python signature
BrowserContext.credentials: Credentials
```

BrowserContext.credentials

Virtual WebAuthn authenticator for this context. Lets tests seed credentials and intercept
`navigator.credentials.create()` / `navigator.credentials.get()` ceremonies.

#### Returns
Credentials


## debugger

属性，直接读取；异步入口也不加 await。

```python signature
BrowserContext.debugger: Debugger
```

BrowserContext.debugger

Debugger allows to pause and resume the execution.

#### Returns
Debugger


## expect_console_message

### 同步

```python signature
def expect_console_message(self, predicate: Optional[Callable[[ForwardRef('ConsoleMessage')], bool]] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('ConsoleMessage')]
```

BrowserContext.expect_console_message

Performs action and waits for a `ConsoleMessage` to be logged by in the pages in the context. If predicate is
provided, it passes `ConsoleMessage` value into the `predicate` function and waits for `predicate(message)` to
return a truthy value. Will throw an error if the page is closed before the `browser_context.on('console')` event
is fired.

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

BrowserContext.expect_console_message

Performs action and waits for a `ConsoleMessage` to be logged by in the pages in the context. If predicate is
provided, it passes `ConsoleMessage` value into the `predicate` function and waits for `predicate(message)` to
return a truthy value. Will throw an error if the page is closed before the `browser_context.on('console')` event
is fired.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `predicate` | Union[Callable[[ConsoleMessage], bool], None] | Receives the `ConsoleMessage` object and resolves to truthy value when the waiting should resolve. |
| `timeout` | Union[float, None] | Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()`. |

#### Returns
EventContextManager[ConsoleMessage]


## expect_event

### 同步

```python signature
def expect_event(self, event: str, predicate: Optional[Callable] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> patchright._impl._sync_base.EventContextManager
```

支持的重载：

```python signature
def expect_event(self, event: Literal['backgroundpage'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Page')]
def expect_event(self, event: Literal['close'], predicate: Optional[Callable[[ForwardRef('BrowserContext')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('BrowserContext')]
def expect_event(self, event: Literal['console'], predicate: Optional[Callable[[ForwardRef('ConsoleMessage')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('ConsoleMessage')]
def expect_event(self, event: Literal['dialog'], predicate: Optional[Callable[[ForwardRef('Dialog')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Dialog')]
def expect_event(self, event: Literal['dialogclosed'], predicate: Optional[Callable[[ForwardRef('Dialog')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Dialog')]
def expect_event(self, event: Literal['download'], predicate: Optional[Callable[[ForwardRef('Download')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Download')]
def expect_event(self, event: Literal['frameattached'], predicate: Optional[Callable[[ForwardRef('Frame')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Frame')]
def expect_event(self, event: Literal['framedetached'], predicate: Optional[Callable[[ForwardRef('Frame')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Frame')]
def expect_event(self, event: Literal['framenavigated'], predicate: Optional[Callable[[ForwardRef('Frame')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Frame')]
def expect_event(self, event: Literal['page'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Page')]
def expect_event(self, event: Literal['pageclose'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Page')]
def expect_event(self, event: Literal['pageload'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Page')]
def expect_event(self, event: Literal['request'], predicate: Optional[Callable[[ForwardRef('Request')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Request')]
def expect_event(self, event: Literal['requestfailed'], predicate: Optional[Callable[[ForwardRef('Request')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Request')]
def expect_event(self, event: Literal['requestfinished'], predicate: Optional[Callable[[ForwardRef('Request')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Request')]
def expect_event(self, event: Literal['response'], predicate: Optional[Callable[[ForwardRef('Response')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Response')]
def expect_event(self, event: Literal['serviceworker'], predicate: Optional[Callable[[ForwardRef('Worker')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Worker')]
def expect_event(self, event: Literal['weberror'], predicate: Optional[Callable[[ForwardRef('WebError')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('WebError')]
def expect_event(self, event: str, predicate: Optional[Callable[..., bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._sync_base.EventContextManager[typing.Any]
```

BrowserContext.expect_event

Waits for event to fire and passes its value into the predicate function. Returns when the predicate returns truthy
value. Will throw an error if the context closes before the event is fired. Returns the event data value.

**Usage**

```py
with context.expect_event("page") as event_info:
    page.get_by_role("button").click()
page = event_info.value
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `event` | str | Event name, same one would pass into `browserContext.on(event)`. |
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
def expect_event(self, event: Literal['backgroundpage'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Page')]
def expect_event(self, event: Literal['close'], predicate: Optional[Callable[[ForwardRef('BrowserContext')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('BrowserContext')]
def expect_event(self, event: Literal['console'], predicate: Optional[Callable[[ForwardRef('ConsoleMessage')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('ConsoleMessage')]
def expect_event(self, event: Literal['dialog'], predicate: Optional[Callable[[ForwardRef('Dialog')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Dialog')]
def expect_event(self, event: Literal['dialogclosed'], predicate: Optional[Callable[[ForwardRef('Dialog')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Dialog')]
def expect_event(self, event: Literal['download'], predicate: Optional[Callable[[ForwardRef('Download')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Download')]
def expect_event(self, event: Literal['frameattached'], predicate: Optional[Callable[[ForwardRef('Frame')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Frame')]
def expect_event(self, event: Literal['framedetached'], predicate: Optional[Callable[[ForwardRef('Frame')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Frame')]
def expect_event(self, event: Literal['framenavigated'], predicate: Optional[Callable[[ForwardRef('Frame')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Frame')]
def expect_event(self, event: Literal['page'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Page')]
def expect_event(self, event: Literal['pageclose'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Page')]
def expect_event(self, event: Literal['pageload'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Page')]
def expect_event(self, event: Literal['request'], predicate: Optional[Callable[[ForwardRef('Request')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Request')]
def expect_event(self, event: Literal['requestfailed'], predicate: Optional[Callable[[ForwardRef('Request')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Request')]
def expect_event(self, event: Literal['requestfinished'], predicate: Optional[Callable[[ForwardRef('Request')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Request')]
def expect_event(self, event: Literal['response'], predicate: Optional[Callable[[ForwardRef('Response')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Response')]
def expect_event(self, event: Literal['serviceworker'], predicate: Optional[Callable[[ForwardRef('Worker')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Worker')]
def expect_event(self, event: Literal['weberror'], predicate: Optional[Callable[[ForwardRef('WebError')], bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('WebError')]
def expect_event(self, event: str, predicate: Optional[Callable[..., bool]] = None, *, timeout: Optional[float] = None) -> patchright._impl._async_base.AsyncEventContextManager[typing.Any]
```

BrowserContext.expect_event

Waits for event to fire and passes its value into the predicate function. Returns when the predicate returns truthy
value. Will throw an error if the context closes before the event is fired. Returns the event data value.

**Usage**

```py
async with context.expect_event("page") as event_info:
    await page.get_by_role("button").click()
page = await event_info.value
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `event` | str | Event name, same one would pass into `browserContext.on(event)`. |
| `predicate` | Union[Callable, None] | Receives the event data and resolves to truthy value when the waiting should resolve. |
| `timeout` | Union[float, None] | Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()`. |

#### Returns
EventContextManager


## expect_page

### 同步

```python signature
def expect_page(self, predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> patchright._impl._sync_base.EventContextManager[ForwardRef('Page')]
```

BrowserContext.expect_page

Performs action and waits for a new `Page` to be created in the context. If predicate is provided, it passes `Page`
value into the `predicate` function and waits for `predicate(event)` to return a truthy value. Will throw an error
if the context closes before new `Page` is created.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `predicate` | Union[Callable[[Page], bool], None] | Receives the `Page` object and resolves to truthy value when the waiting should resolve. |
| `timeout` | Union[float, None] | Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()`. |

#### Returns
EventContextManager[Page]

### 异步

```python signature
def expect_page(self, predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> patchright._impl._async_base.AsyncEventContextManager[ForwardRef('Page')]
```

BrowserContext.expect_page

Performs action and waits for a new `Page` to be created in the context. If predicate is provided, it passes `Page`
value into the `predicate` function and waits for `predicate(event)` to return a truthy value. Will throw an error
if the context closes before new `Page` is created.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `predicate` | Union[Callable[[Page], bool], None] | Receives the `Page` object and resolves to truthy value when the waiting should resolve. |
| `timeout` | Union[float, None] | Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()`. |

#### Returns
EventContextManager[Page]


## expose_binding

### 同步

```python
def expose_binding(self, name: str, callback: Callable) -> 'SyncContextManager'
```

BrowserContext.expose_binding

The method adds a function called `name` on the `window` object of every frame in every page in the context. When
called, the function executes `callback` and returns a [Promise] which resolves to the return value of `callback`.
If the `callback` returns a [Promise], it will be awaited.

The first argument of the `callback` function contains information about the caller: `{ browserContext:
BrowserContext, page: Page, frame: Frame }`.

See `page.expose_binding()` for page-only version.

**Usage**

An example of exposing page URL to all frames in all pages in the context:

```py
from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    webkit = playwright.webkit
    browser = webkit.launch(headless=False)
    context = browser.new_context()
    context.expose_binding("pageURL", lambda source: source["page"].url)
    page = context.new_page()
    page.set_content("""
    <script>
      async function onClick() {
        document.querySelector('div').textContent = await window.pageURL();
      }
    </script>
    <button onclick="onClick()">Click me</button>
    <div></div>
    """)
    page.get_by_role("button").click()

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

BrowserContext.expose_binding

The method adds a function called `name` on the `window` object of every frame in every page in the context. When
called, the function executes `callback` and returns a [Promise] which resolves to the return value of `callback`.
If the `callback` returns a [Promise], it will be awaited.

The first argument of the `callback` function contains information about the caller: `{ browserContext:
BrowserContext, page: Page, frame: Frame }`.

See `page.expose_binding()` for page-only version.

**Usage**

An example of exposing page URL to all frames in all pages in the context:

```py
import asyncio
from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    webkit = playwright.webkit
    browser = await webkit.launch(headless=False)
    context = await browser.new_context()
    await context.expose_binding("pageURL", lambda source: source["page"].url)
    page = await context.new_page()
    await page.set_content("""
    <script>
      async function onClick() {
        document.querySelector('div').textContent = await window.pageURL();
      }
    </script>
    <button onclick="onClick()">Click me</button>
    <div></div>
    """)
    await page.get_by_role("button").click()

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

BrowserContext.expose_function

The method adds a function called `name` on the `window` object of every frame in every page in the context. When
called, the function executes `callback` and returns a [Promise] which resolves to the return value of `callback`.

If the `callback` returns a [Promise], it will be awaited.

See `page.expose_function()` for page-only version.

**Usage**

An example of adding a `sha256` function to all pages in the context:

```py
import hashlib
from playwright.sync_api import sync_playwright

def sha256(text: str) -> str:
    m = hashlib.sha256()
    m.update(bytes(text, "utf8"))
    return m.hexdigest()

def run(playwright: Playwright):
    webkit = playwright.webkit
    browser = webkit.launch(headless=False)
    context = browser.new_context()
    context.expose_function("sha256", sha256)
    page = context.new_page()
    page.set_content("""
        <script>
          async function onClick() {
            document.querySelector('div').textContent = await window.sha256('PLAYWRIGHT');
          }
        </script>
        <button onclick="onClick()">Click me</button>
        <div></div>
    """)
    page.get_by_role("button").click()

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
async def expose_function(self, name: str, callback: Callable) -> 'AsyncContextManager'
```

BrowserContext.expose_function

The method adds a function called `name` on the `window` object of every frame in every page in the context. When
called, the function executes `callback` and returns a [Promise] which resolves to the return value of `callback`.

If the `callback` returns a [Promise], it will be awaited.

See `page.expose_function()` for page-only version.

**Usage**

An example of adding a `sha256` function to all pages in the context:

```py
import asyncio
import hashlib
from playwright.async_api import async_playwright, Playwright

def sha256(text: str) -> str:
    m = hashlib.sha256()
    m.update(bytes(text, "utf8"))
    return m.hexdigest()

async def run(playwright: Playwright):
    webkit = playwright.webkit
    browser = await webkit.launch(headless=False)
    context = await browser.new_context()
    await context.expose_function("sha256", sha256)
    page = await context.new_page()
    await page.set_content("""
        <script>
          async function onClick() {
            document.querySelector('div').textContent = await window.sha256('PLAYWRIGHT');
          }
        </script>
        <button onclick="onClick()">Click me</button>
        <div></div>
    """)
    await page.get_by_role("button").click()

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


## grant_permissions

### 同步

```python signature
def grant_permissions(self, permissions: Sequence[str], *, origin: Optional[str] = None) -> None
```

BrowserContext.grant_permissions

Grants specified permissions to the browser context. Only grants corresponding permissions to the given origin if
specified.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `permissions` | Sequence[str] | A list of permissions to grant.  **NOTE** Supported permissions differ between browsers, and even between different versions of the same browser. Any permission may stop working after an update.  Here are some permissions that may be supported by some browsers: - `'accelerometer'` - `'ambient-light-sensor'` - `'background-sync'` - `'camera'` - `'clipboard-read'` - `'clipboard-write'` - `'geolocation'` - `'gyroscope'` - `'local-fonts'` - `'local-network-access'` - `'magnetometer'` - `'microphone'` - `'midi-sysex'` (system-exclusive midi) - `'midi'` - `'notifications'` - `'payment-handler'` - `'storage-access'` - `'screen-wake-lock'` |
| `origin` | Union[str, None] | The [origin] to grant permissions to, e.g. "https://example.com". |

### 异步

```python signature
async def grant_permissions(self, permissions: Sequence[str], *, origin: Optional[str] = None) -> None
```

BrowserContext.grant_permissions

Grants specified permissions to the browser context. Only grants corresponding permissions to the given origin if
specified.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `permissions` | Sequence[str] | A list of permissions to grant.  **NOTE** Supported permissions differ between browsers, and even between different versions of the same browser. Any permission may stop working after an update.  Here are some permissions that may be supported by some browsers: - `'accelerometer'` - `'ambient-light-sensor'` - `'background-sync'` - `'camera'` - `'clipboard-read'` - `'clipboard-write'` - `'geolocation'` - `'gyroscope'` - `'local-fonts'` - `'local-network-access'` - `'magnetometer'` - `'microphone'` - `'midi-sysex'` (system-exclusive midi) - `'midi'` - `'notifications'` - `'payment-handler'` - `'storage-access'` - `'screen-wake-lock'` |
| `origin` | Union[str, None] | The [origin] to grant permissions to, e.g. "https://example.com". |

## is_closed

### 同步

```python
def is_closed(self) -> bool
```

BrowserContext.is_closed

Indicates that the browser context is in the process of closing or has already been closed.

#### Returns
bool

### 异步

```python
def is_closed(self) -> bool
```

BrowserContext.is_closed

Indicates that the browser context is in the process of closing or has already been closed.

#### Returns
bool


## new_cdp_session

### 同步

```python
def new_cdp_session(self, page: Union[ForwardRef('Page'), ForwardRef('Frame')]) -> 'CDPSession'
```

BrowserContext.new_cdp_session

**NOTE** CDP sessions are only supported on Chromium-based browsers.

Returns the newly created session.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `page` | Union[Frame, Page] | Target to create new session for. For backwards-compatibility, this parameter is named `page`, but it can be a `Page` or `Frame` type. |

#### Returns
CDPSession

### 异步

```python
async def new_cdp_session(self, page: Union[ForwardRef('Page'), ForwardRef('Frame')]) -> 'CDPSession'
```

BrowserContext.new_cdp_session

**NOTE** CDP sessions are only supported on Chromium-based browsers.

Returns the newly created session.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `page` | Union[Frame, Page] | Target to create new session for. For backwards-compatibility, this parameter is named `page`, but it can be a `Page` or `Frame` type. |

#### Returns
CDPSession


## new_page

### 同步

```python signature
def new_page(self, *, focus_control: Optional[bool] = None) -> 'Page'
```

BrowserContext.new_page

Creates a new page in the browser context.

#### Returns
Page

### 异步

```python
async def new_page(self) -> 'Page'
```

BrowserContext.new_page

Creates a new page in the browser context.

#### Returns
Page


## on

### 同步

```python
def on(self, event: str, f: Callable[..., NoneType]) -> None
```

支持的重载：

```python
def on(self, event: Literal['backgroundpage'], f: Callable[[ForwardRef('Page')], ForwardRef('None')]) -> None
def on(self, event: Literal['close'], f: Callable[[ForwardRef('BrowserContext')], ForwardRef('None')]) -> None
def on(self, event: Literal['console'], f: Callable[[ForwardRef('ConsoleMessage')], ForwardRef('None')]) -> None
def on(self, event: Literal['dialog'], f: Callable[[ForwardRef('Dialog')], ForwardRef('None')]) -> None
def on(self, event: Literal['dialogclosed'], f: Callable[[ForwardRef('Dialog')], ForwardRef('None')]) -> None
def on(self, event: Literal['download'], f: Callable[[ForwardRef('Download')], ForwardRef('None')]) -> None
def on(self, event: Literal['frameattached'], f: Callable[[ForwardRef('Frame')], ForwardRef('None')]) -> None
def on(self, event: Literal['framedetached'], f: Callable[[ForwardRef('Frame')], ForwardRef('None')]) -> None
def on(self, event: Literal['framenavigated'], f: Callable[[ForwardRef('Frame')], ForwardRef('None')]) -> None
def on(self, event: Literal['page'], f: Callable[[ForwardRef('Page')], ForwardRef('None')]) -> None
def on(self, event: Literal['pageclose'], f: Callable[[ForwardRef('Page')], ForwardRef('None')]) -> None
def on(self, event: Literal['pageload'], f: Callable[[ForwardRef('Page')], ForwardRef('None')]) -> None
def on(self, event: Literal['request'], f: Callable[[ForwardRef('Request')], ForwardRef('None')]) -> None
def on(self, event: Literal['requestfailed'], f: Callable[[ForwardRef('Request')], ForwardRef('None')]) -> None
def on(self, event: Literal['requestfinished'], f: Callable[[ForwardRef('Request')], ForwardRef('None')]) -> None
def on(self, event: Literal['response'], f: Callable[[ForwardRef('Response')], ForwardRef('None')]) -> None
def on(self, event: Literal['serviceworker'], f: Callable[[ForwardRef('Worker')], ForwardRef('None')]) -> None
def on(self, event: Literal['weberror'], f: Callable[[ForwardRef('WebError')], ForwardRef('None')]) -> None
```

Registers the function ``f`` to the event name ``event``.

### 异步

```python
def on(self, event: str, f: Callable[..., Optional[Awaitable[NoneType]]]) -> None
```

支持的重载：

```python
def on(self, event: Literal['backgroundpage'], f: Callable[[ForwardRef('Page')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['close'], f: Callable[[ForwardRef('BrowserContext')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['console'], f: Callable[[ForwardRef('ConsoleMessage')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['dialog'], f: Callable[[ForwardRef('Dialog')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['dialogclosed'], f: Callable[[ForwardRef('Dialog')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['download'], f: Callable[[ForwardRef('Download')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['frameattached'], f: Callable[[ForwardRef('Frame')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['framedetached'], f: Callable[[ForwardRef('Frame')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['framenavigated'], f: Callable[[ForwardRef('Frame')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['page'], f: Callable[[ForwardRef('Page')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['pageclose'], f: Callable[[ForwardRef('Page')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['pageload'], f: Callable[[ForwardRef('Page')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['request'], f: Callable[[ForwardRef('Request')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['requestfailed'], f: Callable[[ForwardRef('Request')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['requestfinished'], f: Callable[[ForwardRef('Request')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['response'], f: Callable[[ForwardRef('Response')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['serviceworker'], f: Callable[[ForwardRef('Worker')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['weberror'], f: Callable[[ForwardRef('WebError')], ForwardRef('Union[Awaitable[None], None]')]) -> None
```

Registers the function ``f`` to the event name ``event``.


## once

### 同步

```python
def once(self, event: str, f: Callable[..., NoneType]) -> None
```

支持的重载：

```python
def once(self, event: Literal['backgroundpage'], f: Callable[[ForwardRef('Page')], ForwardRef('None')]) -> None
def once(self, event: Literal['close'], f: Callable[[ForwardRef('BrowserContext')], ForwardRef('None')]) -> None
def once(self, event: Literal['console'], f: Callable[[ForwardRef('ConsoleMessage')], ForwardRef('None')]) -> None
def once(self, event: Literal['dialog'], f: Callable[[ForwardRef('Dialog')], ForwardRef('None')]) -> None
def once(self, event: Literal['dialogclosed'], f: Callable[[ForwardRef('Dialog')], ForwardRef('None')]) -> None
def once(self, event: Literal['download'], f: Callable[[ForwardRef('Download')], ForwardRef('None')]) -> None
def once(self, event: Literal['frameattached'], f: Callable[[ForwardRef('Frame')], ForwardRef('None')]) -> None
def once(self, event: Literal['framedetached'], f: Callable[[ForwardRef('Frame')], ForwardRef('None')]) -> None
def once(self, event: Literal['framenavigated'], f: Callable[[ForwardRef('Frame')], ForwardRef('None')]) -> None
def once(self, event: Literal['page'], f: Callable[[ForwardRef('Page')], ForwardRef('None')]) -> None
def once(self, event: Literal['pageclose'], f: Callable[[ForwardRef('Page')], ForwardRef('None')]) -> None
def once(self, event: Literal['pageload'], f: Callable[[ForwardRef('Page')], ForwardRef('None')]) -> None
def once(self, event: Literal['request'], f: Callable[[ForwardRef('Request')], ForwardRef('None')]) -> None
def once(self, event: Literal['requestfailed'], f: Callable[[ForwardRef('Request')], ForwardRef('None')]) -> None
def once(self, event: Literal['requestfinished'], f: Callable[[ForwardRef('Request')], ForwardRef('None')]) -> None
def once(self, event: Literal['response'], f: Callable[[ForwardRef('Response')], ForwardRef('None')]) -> None
def once(self, event: Literal['serviceworker'], f: Callable[[ForwardRef('Worker')], ForwardRef('None')]) -> None
def once(self, event: Literal['weberror'], f: Callable[[ForwardRef('WebError')], ForwardRef('None')]) -> None
```

The same as ``self.on``, except that the listener is automatically
removed after being called.

### 异步

```python
def once(self, event: str, f: Callable[..., Optional[Awaitable[NoneType]]]) -> None
```

支持的重载：

```python
def once(self, event: Literal['backgroundpage'], f: Callable[[ForwardRef('Page')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['close'], f: Callable[[ForwardRef('BrowserContext')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['console'], f: Callable[[ForwardRef('ConsoleMessage')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['dialog'], f: Callable[[ForwardRef('Dialog')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['dialogclosed'], f: Callable[[ForwardRef('Dialog')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['download'], f: Callable[[ForwardRef('Download')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['frameattached'], f: Callable[[ForwardRef('Frame')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['framedetached'], f: Callable[[ForwardRef('Frame')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['framenavigated'], f: Callable[[ForwardRef('Frame')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['page'], f: Callable[[ForwardRef('Page')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['pageclose'], f: Callable[[ForwardRef('Page')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['pageload'], f: Callable[[ForwardRef('Page')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['request'], f: Callable[[ForwardRef('Request')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['requestfailed'], f: Callable[[ForwardRef('Request')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['requestfinished'], f: Callable[[ForwardRef('Request')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['response'], f: Callable[[ForwardRef('Response')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['serviceworker'], f: Callable[[ForwardRef('Worker')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['weberror'], f: Callable[[ForwardRef('WebError')], ForwardRef('Union[Awaitable[None], None]')]) -> None
```

The same as ``self.on``, except that the listener is automatically
removed after being called.


## pages

属性，直接读取；异步入口也不加 await。

```python signature
BrowserContext.pages: typing.List[ForwardRef('Page')]
```

BrowserContext.pages

Returns all open pages in the context.

#### Returns
List[Page]


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


## request

属性，直接读取；异步入口也不加 await。

```python signature
BrowserContext.request: APIRequestContext
```

BrowserContext.request

API testing helper associated with this context. Requests made with this API will use context cookies.

#### Returns
APIRequestContext


## route

### 同步

```python signature
def route(self, url: Union[str, Pattern[str], Callable[[str], bool]], handler: Union[Callable[[ForwardRef('Route')], Any], Callable[[ForwardRef('Route'), ForwardRef('Request')], Any]], *, times: Optional[int] = None) -> 'SyncContextManager'
```

BrowserContext.route

Routing provides the capability to modify network requests that are made by any page in the browser context. Once
route is enabled, every request matching the url pattern will stall unless it's continued, fulfilled or aborted.

**NOTE** `browser_context.route()` will not intercept requests intercepted by Service Worker. See
[this](https://github.com/microsoft/playwright/issues/1090) issue. We recommend disabling Service Workers when
using request interception by setting `service_workers` to `'block'`.

**Usage**

An example of a naive handler that aborts all image requests:

```py
context = browser.new_context()
page = context.new_page()
context.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())
page.goto("https://example.com")
browser.close()
```

or the same snippet using a regex pattern instead:

```py
context = browser.new_context()
page = context.new_page()
context.route(re.compile(r"(\.png$)|(\.jpg$)"), lambda route: route.abort())
page = await context.new_page()
page = context.new_page()
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
context.route("/api/**", handle_route)
```

Page routes (set up with `page.route()`) take precedence over browser context routes when request matches both
handlers.

To remove a route with its handler you can use `browser_context.unroute()`.

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

BrowserContext.route

Routing provides the capability to modify network requests that are made by any page in the browser context. Once
route is enabled, every request matching the url pattern will stall unless it's continued, fulfilled or aborted.

**NOTE** `browser_context.route()` will not intercept requests intercepted by Service Worker. See
[this](https://github.com/microsoft/playwright/issues/1090) issue. We recommend disabling Service Workers when
using request interception by setting `service_workers` to `'block'`.

**Usage**

An example of a naive handler that aborts all image requests:

```py
context = await browser.new_context()
page = await context.new_page()
await context.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())
await page.goto("https://example.com")
await browser.close()
```

or the same snippet using a regex pattern instead:

```py
context = await browser.new_context()
page = await context.new_page()
await context.route(re.compile(r"(\.png$)|(\.jpg$)"), lambda route: route.abort())
page = await context.new_page()
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
await context.route("/api/**", handle_route)
```

Page routes (set up with `page.route()`) take precedence over browser context routes when request matches both
handlers.

To remove a route with its handler you can use `browser_context.unroute()`.

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

BrowserContext.route_from_har

If specified the network requests that are made in the context will be served from the HAR file. Read more about
[Replaying from HAR](https://playwright.dev/python/docs/mock#replaying-from-har).

Playwright will not serve requests intercepted by Service Worker from the HAR file. See
[this](https://github.com/microsoft/playwright/issues/1090) issue. We recommend disabling Service Workers when
using request interception by setting `service_workers` to `'block'`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `har` | Union[pathlib.Path, str] | Path to a [HAR](http://www.softwareishard.com/blog/har-12-spec) file with prerecorded network data. If `path` is a relative path, then it is resolved relative to the current working directory. |
| `not_found` | Union["abort", "fallback", None] | - If set to 'abort' any request not found in the HAR file will be aborted. - If set to 'fallback' falls through to the next route handler in the handler chain.  Defaults to abort. |
| `update` | Union[bool, None] | If specified, updates the given HAR with the actual network information instead of serving from file. The file is written to disk when `browser_context.close()` is called. |
| `update_content` | Union["attach", "embed", None] | Optional setting to control resource content management. If `attach` is specified, resources are persisted as separate files or entries in the ZIP archive. If `embed` is specified, content is stored inline the HAR file. |
| `update_mode` | Union["full", "minimal", None] | When set to `minimal`, only record information necessary for routing from HAR. This omits sizes, timing, page, cookies, security and other types of HAR information that are not used when replaying from HAR. Defaults to `minimal`. |
| `url` | Union[Pattern[str], str, None] | A glob pattern, regular expression or predicate to match the request URL. Only requests with URL matching the pattern will be served from the HAR file. If not specified, all requests are served from the HAR file. |

### 异步

```python signature
async def route_from_har(self, har: Union[str, pathlib.Path], *, not_found: Optional[Literal['abort', 'fallback']] = None, update: Optional[bool] = None, update_content: Optional[Literal['attach', 'embed']] = None, update_mode: Optional[Literal['full', 'minimal']] = None, url: Union[str, Pattern[str], NoneType] = None) -> None
```

BrowserContext.route_from_har

If specified the network requests that are made in the context will be served from the HAR file. Read more about
[Replaying from HAR](https://playwright.dev/python/docs/mock#replaying-from-har).

Playwright will not serve requests intercepted by Service Worker from the HAR file. See
[this](https://github.com/microsoft/playwright/issues/1090) issue. We recommend disabling Service Workers when
using request interception by setting `service_workers` to `'block'`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `har` | Union[pathlib.Path, str] | Path to a [HAR](http://www.softwareishard.com/blog/har-12-spec) file with prerecorded network data. If `path` is a relative path, then it is resolved relative to the current working directory. |
| `not_found` | Union["abort", "fallback", None] | - If set to 'abort' any request not found in the HAR file will be aborted. - If set to 'fallback' falls through to the next route handler in the handler chain.  Defaults to abort. |
| `update` | Union[bool, None] | If specified, updates the given HAR with the actual network information instead of serving from file. The file is written to disk when `browser_context.close()` is called. |
| `update_content` | Union["attach", "embed", None] | Optional setting to control resource content management. If `attach` is specified, resources are persisted as separate files or entries in the ZIP archive. If `embed` is specified, content is stored inline the HAR file. |
| `update_mode` | Union["full", "minimal", None] | When set to `minimal`, only record information necessary for routing from HAR. This omits sizes, timing, page, cookies, security and other types of HAR information that are not used when replaying from HAR. Defaults to `minimal`. |
| `url` | Union[Pattern[str], str, None] | A glob pattern, regular expression or predicate to match the request URL. Only requests with URL matching the pattern will be served from the HAR file. If not specified, all requests are served from the HAR file. |

## route_web_socket

### 同步

```python
def route_web_socket(self, url: Union[str, Pattern[str], Callable[[str], bool]], handler: Callable[[ForwardRef('WebSocketRoute')], Any]) -> None
```

BrowserContext.route_web_socket

This method allows to modify websocket connections that are made by any page in the browser context.

Note that only `WebSocket`s created after this method was called will be routed. It is recommended to call this
method before creating any pages.

**Usage**

Below is an example of a simple handler that blocks some websocket messages. See `WebSocketRoute` for more details
and examples.

```py
def message_handler(ws: WebSocketRoute, message: Union[str, bytes]):
  if message == "to-be-blocked":
    return
  ws.send(message)

def handler(ws: WebSocketRoute):
  ws.route_send(lambda message: message_handler(ws, message))
  ws.connect()

context.route_web_socket("/ws", handler)
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

BrowserContext.route_web_socket

This method allows to modify websocket connections that are made by any page in the browser context.

Note that only `WebSocket`s created after this method was called will be routed. It is recommended to call this
method before creating any pages.

**Usage**

Below is an example of a simple handler that blocks some websocket messages. See `WebSocketRoute` for more details
and examples.

```py
def message_handler(ws: WebSocketRoute, message: Union[str, bytes]):
  if message == "to-be-blocked":
    return
  ws.send(message)

async def handler(ws: WebSocketRoute):
  ws.route_send(lambda message: message_handler(ws, message))
  await ws.connect()

await context.route_web_socket("/ws", handler)
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url` | Union[Callable[[str], bool], Pattern[str], str] | Only WebSockets with the url matching this pattern will be routed. A string pattern can be relative to the `base_url` context option. |
| `handler` | Callable[[WebSocketRoute], Any] | Handler function to route the WebSocket. |

## service_workers

属性，直接读取；异步入口也不加 await。

```python signature
BrowserContext.service_workers: typing.List[ForwardRef('Worker')]
```

BrowserContext.service_workers

**NOTE** Service workers are only supported on Chromium-based browsers.

All existing service workers in the context.

#### Returns
List[Worker]


## set_default_navigation_timeout

### 同步

```python
def set_default_navigation_timeout(self, timeout: Union[float, datetime.timedelta]) -> None
```

BrowserContext.set_default_navigation_timeout

This setting will change the default maximum navigation time for the following methods and related shortcuts:
- `page.go_back()`
- `page.go_forward()`
- `page.goto()`
- `page.reload()`
- `page.set_content()`
- `page.expect_navigation()`

**NOTE** `page.set_default_navigation_timeout()` and `page.set_default_timeout()` take priority over
`browser_context.set_default_navigation_timeout()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | float | Maximum navigation time in milliseconds |

### 异步

```python
def set_default_navigation_timeout(self, timeout: Union[float, datetime.timedelta]) -> None
```

BrowserContext.set_default_navigation_timeout

This setting will change the default maximum navigation time for the following methods and related shortcuts:
- `page.go_back()`
- `page.go_forward()`
- `page.goto()`
- `page.reload()`
- `page.set_content()`
- `page.expect_navigation()`

**NOTE** `page.set_default_navigation_timeout()` and `page.set_default_timeout()` take priority over
`browser_context.set_default_navigation_timeout()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | float | Maximum navigation time in milliseconds |

## set_default_timeout

### 同步

```python
def set_default_timeout(self, timeout: Union[float, datetime.timedelta]) -> None
```

BrowserContext.set_default_timeout

This setting will change the default maximum time for all the methods accepting `timeout` option.

**NOTE** `page.set_default_navigation_timeout()`, `page.set_default_timeout()` and
`browser_context.set_default_navigation_timeout()` take priority over `browser_context.set_default_timeout()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | float | Maximum time in milliseconds. Pass `0` to disable timeout. |

### 异步

```python
def set_default_timeout(self, timeout: Union[float, datetime.timedelta]) -> None
```

BrowserContext.set_default_timeout

This setting will change the default maximum time for all the methods accepting `timeout` option.

**NOTE** `page.set_default_navigation_timeout()`, `page.set_default_timeout()` and
`browser_context.set_default_navigation_timeout()` take priority over `browser_context.set_default_timeout()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | float | Maximum time in milliseconds. Pass `0` to disable timeout. |

## set_extra_http_headers

### 同步

```python
def set_extra_http_headers(self, headers: Dict[str, str]) -> None
```

BrowserContext.set_extra_http_headers

The extra HTTP headers will be sent with every request initiated by any page in the context. These headers are
merged with page-specific extra HTTP headers set with `page.set_extra_http_headers()`. If page overrides a
particular header, page-specific header value will be used instead of the browser context header value.

**NOTE** `browser_context.set_extra_http_headers()` does not guarantee the order of headers in the outgoing
requests.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `headers` | Dict[str, str] | An object containing additional HTTP headers to be sent with every request. All header values must be strings. |

### 异步

```python
async def set_extra_http_headers(self, headers: Dict[str, str]) -> None
```

BrowserContext.set_extra_http_headers

The extra HTTP headers will be sent with every request initiated by any page in the context. These headers are
merged with page-specific extra HTTP headers set with `page.set_extra_http_headers()`. If page overrides a
particular header, page-specific header value will be used instead of the browser context header value.

**NOTE** `browser_context.set_extra_http_headers()` does not guarantee the order of headers in the outgoing
requests.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `headers` | Dict[str, str] | An object containing additional HTTP headers to be sent with every request. All header values must be strings. |

## set_geolocation

### 同步

```python
def set_geolocation(self, geolocation: Optional[patchright._impl._api_structures.Geolocation] = None) -> None
```

BrowserContext.set_geolocation

Sets the context's geolocation. Passing `null` or `undefined` emulates position unavailable.

**Usage**

```py
browser_context.set_geolocation({"latitude": 59.95, "longitude": 30.31667})
```

**NOTE** Consider using `browser_context.grant_permissions()` to grant permissions for the browser context pages to
read its geolocation.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `geolocation` | Union[{latitude: float, longitude: float, accuracy: Union[float, None]}, None] |  |

### 异步

```python
async def set_geolocation(self, geolocation: Optional[patchright._impl._api_structures.Geolocation] = None) -> None
```

BrowserContext.set_geolocation

Sets the context's geolocation. Passing `null` or `undefined` emulates position unavailable.

**Usage**

```py
await browser_context.set_geolocation({"latitude": 59.95, "longitude": 30.31667})
```

**NOTE** Consider using `browser_context.grant_permissions()` to grant permissions for the browser context pages to
read its geolocation.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `geolocation` | Union[{latitude: float, longitude: float, accuracy: Union[float, None]}, None] |  |

## set_offline

### 同步

```python
def set_offline(self, offline: bool) -> None
```

BrowserContext.set_offline

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `offline` | bool | Whether to emulate network being offline for the browser context.  **NOTE** Offline emulation only affects requests that go through the browser's regular network stack, such as page navigations, `fetch()`, `XMLHttpRequest` and WebSockets. It does not affect WebRTC traffic: established `RTCPeerConnection`s keep sending and receiving media over UDP. To test WebRTC connection loss, interrupt the connection outside the browser, for example by stopping the TURN server or using an OS-level firewall. |

### 异步

```python
async def set_offline(self, offline: bool) -> None
```

BrowserContext.set_offline

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `offline` | bool | Whether to emulate network being offline for the browser context.  **NOTE** Offline emulation only affects requests that go through the browser's regular network stack, such as page navigations, `fetch()`, `XMLHttpRequest` and WebSockets. It does not affect WebRTC traffic: established `RTCPeerConnection`s keep sending and receiving media over UDP. To test WebRTC connection loss, interrupt the connection outside the browser, for example by stopping the TURN server or using an OS-level firewall. |

## set_storage_state

### 同步

```python
def set_storage_state(self, storage_state: Union[str, pathlib.Path, patchright._impl._api_structures.StorageState]) -> None
```

BrowserContext.set_storage_state

Clears the existing cookies, local storage, IndexedDB entries, origin private file system entries and virtual
WebAuthn credentials, and sets the new storage state. When the storage state contains credentials, the virtual
WebAuthn authenticator is installed (equivalent to `credentials.install()`), preventing all real authenticators
from working in this context.

**Usage**

```py
# Load storage state from a file and apply it to the context.
context.set_storage_state("state.json")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `storage_state` | Union[pathlib.Path, str, {cookies: Sequence[{name: str, value: str, domain: str, path: str, expires: float, httpOnly: bool, secure: bool, sameSite: Union["Lax", "None", "Strict"]}], origins: Sequence[{origin: str, localStorage: Sequence[{name: str, value: str}]}]}] | Learn more about storage state and auth.  Populates context with given storage state. This option can be used to initialize context with logged-in information obtained via `browser_context.storage_state()`. |

### 异步

```python
async def set_storage_state(self, storage_state: Union[str, pathlib.Path, patchright._impl._api_structures.StorageState]) -> None
```

BrowserContext.set_storage_state

Clears the existing cookies, local storage, IndexedDB entries, origin private file system entries and virtual
WebAuthn credentials, and sets the new storage state. When the storage state contains credentials, the virtual
WebAuthn authenticator is installed (equivalent to `credentials.install()`), preventing all real authenticators
from working in this context.

**Usage**

```py
# Load storage state from a file and apply it to the context.
await context.set_storage_state("state.json")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `storage_state` | Union[pathlib.Path, str, {cookies: Sequence[{name: str, value: str, domain: str, path: str, expires: float, httpOnly: bool, secure: bool, sameSite: Union["Lax", "None", "Strict"]}], origins: Sequence[{origin: str, localStorage: Sequence[{name: str, value: str}]}]}] | Learn more about storage state and auth.  Populates context with given storage state. This option can be used to initialize context with logged-in information obtained via `browser_context.storage_state()`. |

## storage_state

### 同步

```python signature
def storage_state(self, *, credentials: Optional[bool] = None, indexed_db: Optional[bool] = None, opfs: Optional[bool] = None, path: Union[pathlib.Path, str, NoneType] = None) -> patchright._impl._api_structures.StorageState
```

BrowserContext.storage_state

Returns storage state for this browser context, contains current cookies, local storage snapshot, IndexedDB
snapshot, origin private file system snapshot and virtual WebAuthn credentials.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `credentials` | Union[bool, None] | Set to `true` to include the context's virtual WebAuthn `browser_context.credentials` (passkeys) in the storage state snapshot. The captured credentials carry their private keys and signature counters, so they can be re-seeded into a later context via the `storage_state` option or `browser_context.set_storage_state()`. Note that restoring the storage state that contains credentials will automatically install the virtual WebAuthn authenticator (see `credentials.install()`), and prevent all real authenticators from working in this context. |
| `indexed_db` | Union[bool, None] | Set to `true` to include [IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API) in the storage state snapshot. If your application uses IndexedDB to store authentication tokens, like Firebase Authentication, enable this. |
| `opfs` | Union[bool, None] | Set to `true` to include the [origin private file system](https://developer.mozilla.org/en-US/docs/Web/API/File_System_API/Origin_private_file_system) in the storage state snapshot.  **NOTE** OPFS is currently not supported in ephemeral WebKit contexts. |
| `path` | Union[pathlib.Path, str, None] | The file path to save the storage state to. If `path` is a relative path, then it is resolved relative to current working directory. If no path is provided, storage state is still returned, but won't be saved to the disk. |

#### Returns
{cookies: List[{name: str, value: str, domain: str, path: str, expires: float, httpOnly: bool, secure: bool, sameSite: Union["Lax", "None", "Strict"]}], origins: List[{origin: str, localStorage: List[{name: str, value: str}]}]}

### 异步

```python signature
async def storage_state(self, *, credentials: Optional[bool] = None, indexed_db: Optional[bool] = None, opfs: Optional[bool] = None, path: Union[pathlib.Path, str, NoneType] = None) -> patchright._impl._api_structures.StorageState
```

BrowserContext.storage_state

Returns storage state for this browser context, contains current cookies, local storage snapshot, IndexedDB
snapshot, origin private file system snapshot and virtual WebAuthn credentials.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `credentials` | Union[bool, None] | Set to `true` to include the context's virtual WebAuthn `browser_context.credentials` (passkeys) in the storage state snapshot. The captured credentials carry their private keys and signature counters, so they can be re-seeded into a later context via the `storage_state` option or `browser_context.set_storage_state()`. Note that restoring the storage state that contains credentials will automatically install the virtual WebAuthn authenticator (see `credentials.install()`), and prevent all real authenticators from working in this context. |
| `indexed_db` | Union[bool, None] | Set to `true` to include [IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API) in the storage state snapshot. If your application uses IndexedDB to store authentication tokens, like Firebase Authentication, enable this. |
| `opfs` | Union[bool, None] | Set to `true` to include the [origin private file system](https://developer.mozilla.org/en-US/docs/Web/API/File_System_API/Origin_private_file_system) in the storage state snapshot.  **NOTE** OPFS is currently not supported in ephemeral WebKit contexts. |
| `path` | Union[pathlib.Path, str, None] | The file path to save the storage state to. If `path` is a relative path, then it is resolved relative to current working directory. If no path is provided, storage state is still returned, but won't be saved to the disk. |

#### Returns
{cookies: List[{name: str, value: str, domain: str, path: str, expires: float, httpOnly: bool, secure: bool, sameSite: Union["Lax", "None", "Strict"]}], origins: List[{origin: str, localStorage: List[{name: str, value: str}]}]}


## tracing

属性，直接读取；异步入口也不加 await。

```python signature
BrowserContext.tracing: Tracing
```

BrowserContext.tracing

#### Returns
Tracing


## unroute

### 同步

```python
def unroute(self, url: Union[str, Pattern[str], Callable[[str], bool]], handler: Union[Callable[[ForwardRef('Route')], Any], Callable[[ForwardRef('Route'), ForwardRef('Request')], Any], NoneType] = None) -> None
```

BrowserContext.unroute

Removes a route created with `browser_context.route()`. When `handler` is not specified, removes all routes for the
`url`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url` | Union[Callable[[str], bool], Pattern[str], str] | A glob pattern, regex pattern, or predicate receiving [URL] used to register a routing with `browser_context.route()`. |
| `handler` | Union[Callable[[Route, Request], Any], Callable[[Route], Any], None] | Optional handler function used to register a routing with `browser_context.route()`. |

### 异步

```python
async def unroute(self, url: Union[str, Pattern[str], Callable[[str], bool]], handler: Union[Callable[[ForwardRef('Route')], Any], Callable[[ForwardRef('Route'), ForwardRef('Request')], Any], NoneType] = None) -> None
```

BrowserContext.unroute

Removes a route created with `browser_context.route()`. When `handler` is not specified, removes all routes for the
`url`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url` | Union[Callable[[str], bool], Pattern[str], str] | A glob pattern, regex pattern, or predicate receiving [URL] used to register a routing with `browser_context.route()`. |
| `handler` | Union[Callable[[Route, Request], Any], Callable[[Route], Any], None] | Optional handler function used to register a routing with `browser_context.route()`. |

## unroute_all

### 同步

```python signature
def unroute_all(self, *, behavior: Optional[Literal['default', 'ignoreErrors', 'wait']] = None) -> None
```

BrowserContext.unroute_all

Removes all routes created with `browser_context.route()` and `browser_context.route_from_har()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `behavior` | Union["default", "ignoreErrors", "wait", None] | Specifies whether to wait for already running handlers and what to do if they throw errors: - `'default'` - do not wait for current handler calls (if any) to finish, if unrouted handler throws, it may result in unhandled error - `'wait'` - wait for current handler calls (if any) to finish - `'ignoreErrors'` - do not wait for current handler calls (if any) to finish, all errors thrown by the handlers after unrouting are silently caught |

### 异步

```python signature
async def unroute_all(self, *, behavior: Optional[Literal['default', 'ignoreErrors', 'wait']] = None) -> None
```

BrowserContext.unroute_all

Removes all routes created with `browser_context.route()` and `browser_context.route_from_har()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `behavior` | Union["default", "ignoreErrors", "wait", None] | Specifies whether to wait for already running handlers and what to do if they throw errors: - `'default'` - do not wait for current handler calls (if any) to finish, if unrouted handler throws, it may result in unhandled error - `'wait'` - wait for current handler calls (if any) to finish - `'ignoreErrors'` - do not wait for current handler calls (if any) to finish, all errors thrown by the handlers after unrouting are silently caught |

## wait_for_event

### 同步

```python signature
def wait_for_event(self, event: str, predicate: Optional[Callable] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Any
```

支持的重载：

```python signature
def wait_for_event(self, event: Literal['backgroundpage'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> 'Page'
def wait_for_event(self, event: Literal['close'], predicate: Optional[Callable[[ForwardRef('BrowserContext')], bool]] = None, *, timeout: Optional[float] = None) -> 'BrowserContext'
def wait_for_event(self, event: Literal['console'], predicate: Optional[Callable[[ForwardRef('ConsoleMessage')], bool]] = None, *, timeout: Optional[float] = None) -> 'ConsoleMessage'
def wait_for_event(self, event: Literal['dialog'], predicate: Optional[Callable[[ForwardRef('Dialog')], bool]] = None, *, timeout: Optional[float] = None) -> 'Dialog'
def wait_for_event(self, event: Literal['dialogclosed'], predicate: Optional[Callable[[ForwardRef('Dialog')], bool]] = None, *, timeout: Optional[float] = None) -> 'Dialog'
def wait_for_event(self, event: Literal['download'], predicate: Optional[Callable[[ForwardRef('Download')], bool]] = None, *, timeout: Optional[float] = None) -> 'Download'
def wait_for_event(self, event: Literal['frameattached'], predicate: Optional[Callable[[ForwardRef('Frame')], bool]] = None, *, timeout: Optional[float] = None) -> 'Frame'
def wait_for_event(self, event: Literal['framedetached'], predicate: Optional[Callable[[ForwardRef('Frame')], bool]] = None, *, timeout: Optional[float] = None) -> 'Frame'
def wait_for_event(self, event: Literal['framenavigated'], predicate: Optional[Callable[[ForwardRef('Frame')], bool]] = None, *, timeout: Optional[float] = None) -> 'Frame'
def wait_for_event(self, event: Literal['page'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> 'Page'
def wait_for_event(self, event: Literal['pageclose'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> 'Page'
def wait_for_event(self, event: Literal['pageload'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> 'Page'
def wait_for_event(self, event: Literal['request'], predicate: Optional[Callable[[ForwardRef('Request')], bool]] = None, *, timeout: Optional[float] = None) -> 'Request'
def wait_for_event(self, event: Literal['requestfailed'], predicate: Optional[Callable[[ForwardRef('Request')], bool]] = None, *, timeout: Optional[float] = None) -> 'Request'
def wait_for_event(self, event: Literal['requestfinished'], predicate: Optional[Callable[[ForwardRef('Request')], bool]] = None, *, timeout: Optional[float] = None) -> 'Request'
def wait_for_event(self, event: Literal['response'], predicate: Optional[Callable[[ForwardRef('Response')], bool]] = None, *, timeout: Optional[float] = None) -> 'Response'
def wait_for_event(self, event: Literal['serviceworker'], predicate: Optional[Callable[[ForwardRef('Worker')], bool]] = None, *, timeout: Optional[float] = None) -> 'Worker'
def wait_for_event(self, event: Literal['weberror'], predicate: Optional[Callable[[ForwardRef('WebError')], bool]] = None, *, timeout: Optional[float] = None) -> 'WebError'
def wait_for_event(self, event: str, predicate: Optional[Callable[..., bool]] = None, *, timeout: Optional[float] = None) -> Any
```

BrowserContext.wait_for_event

**NOTE** In most cases, you should use `browser_context.expect_event()`.

Waits for given `event` to fire. If predicate is provided, it passes event's value into the `predicate` function
and waits for `predicate(event)` to return a truthy value. Will throw an error if the browser context is closed
before the `event` is fired.

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
def wait_for_event(self, event: Literal['backgroundpage'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> 'Page'
def wait_for_event(self, event: Literal['close'], predicate: Optional[Callable[[ForwardRef('BrowserContext')], bool]] = None, *, timeout: Optional[float] = None) -> 'BrowserContext'
def wait_for_event(self, event: Literal['console'], predicate: Optional[Callable[[ForwardRef('ConsoleMessage')], bool]] = None, *, timeout: Optional[float] = None) -> 'ConsoleMessage'
def wait_for_event(self, event: Literal['dialog'], predicate: Optional[Callable[[ForwardRef('Dialog')], bool]] = None, *, timeout: Optional[float] = None) -> 'Dialog'
def wait_for_event(self, event: Literal['dialogclosed'], predicate: Optional[Callable[[ForwardRef('Dialog')], bool]] = None, *, timeout: Optional[float] = None) -> 'Dialog'
def wait_for_event(self, event: Literal['download'], predicate: Optional[Callable[[ForwardRef('Download')], bool]] = None, *, timeout: Optional[float] = None) -> 'Download'
def wait_for_event(self, event: Literal['frameattached'], predicate: Optional[Callable[[ForwardRef('Frame')], bool]] = None, *, timeout: Optional[float] = None) -> 'Frame'
def wait_for_event(self, event: Literal['framedetached'], predicate: Optional[Callable[[ForwardRef('Frame')], bool]] = None, *, timeout: Optional[float] = None) -> 'Frame'
def wait_for_event(self, event: Literal['framenavigated'], predicate: Optional[Callable[[ForwardRef('Frame')], bool]] = None, *, timeout: Optional[float] = None) -> 'Frame'
def wait_for_event(self, event: Literal['page'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> 'Page'
def wait_for_event(self, event: Literal['pageclose'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> 'Page'
def wait_for_event(self, event: Literal['pageload'], predicate: Optional[Callable[[ForwardRef('Page')], bool]] = None, *, timeout: Optional[float] = None) -> 'Page'
def wait_for_event(self, event: Literal['request'], predicate: Optional[Callable[[ForwardRef('Request')], bool]] = None, *, timeout: Optional[float] = None) -> 'Request'
def wait_for_event(self, event: Literal['requestfailed'], predicate: Optional[Callable[[ForwardRef('Request')], bool]] = None, *, timeout: Optional[float] = None) -> 'Request'
def wait_for_event(self, event: Literal['requestfinished'], predicate: Optional[Callable[[ForwardRef('Request')], bool]] = None, *, timeout: Optional[float] = None) -> 'Request'
def wait_for_event(self, event: Literal['response'], predicate: Optional[Callable[[ForwardRef('Response')], bool]] = None, *, timeout: Optional[float] = None) -> 'Response'
def wait_for_event(self, event: Literal['serviceworker'], predicate: Optional[Callable[[ForwardRef('Worker')], bool]] = None, *, timeout: Optional[float] = None) -> 'Worker'
def wait_for_event(self, event: Literal['weberror'], predicate: Optional[Callable[[ForwardRef('WebError')], bool]] = None, *, timeout: Optional[float] = None) -> 'WebError'
def wait_for_event(self, event: str, predicate: Optional[Callable[..., bool]] = None, *, timeout: Optional[float] = None) -> Any
```

BrowserContext.wait_for_event

**NOTE** In most cases, you should use `browser_context.expect_event()`.

Waits for given `event` to fire. If predicate is provided, it passes event's value into the `predicate` function
and waits for `predicate(event)` to return a truthy value. Will throw an error if the browser context is closed
before the `event` is fired.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `event` | str | Event name, same one typically passed into `*.on(event)`. |
| `predicate` | Union[Callable, None] | Receives the event data and resolves to truthy value when the waiting should resolve. |
| `timeout` | Union[float, None] | Maximum time to wait for in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()`. |

#### Returns
Any
