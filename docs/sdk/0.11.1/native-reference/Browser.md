# 原生 Browser

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [bind](#bind)
- [browser_type](#browser_type)
- [close](#close)
- [contexts](#contexts)
- [is_connected](#is_connected)
- [new_browser_cdp_session](#new_browser_cdp_session)
- [new_context](#new_context)
- [new_page](#new_page)
- [on](#on)
- [once](#once)
- [remove_listener](#remove_listener)
- [start_tracing](#start_tracing)
- [stop_tracing](#stop_tracing)
- [unbind](#unbind)
- [version](#version)

## bind

### 同步

```python signature
def bind(self, title: str, *, host: Optional[str] = None, port: Optional[int] = None, workspace_dir: Optional[str] = None) -> patchright._impl._api_structures.BrowserBindResult
```

Browser.bind

Binds the browser to a named pipe or web socket, making it available for other clients to connect to.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `title` | str | Title of the browser server, used for identification. |
| `host` | Union[str, None] | Host to bind the web socket server to. When specified, a web socket server is created instead of a named pipe. |
| `port` | Union[int, None] | Port to bind the web socket server to. When specified, a web socket server is created instead of a named pipe. Use `0` to let the OS pick an available port. |
| `workspace_dir` | Union[str, None] | Working directory associated with this browser server. |

#### Returns
{endpoint: str}

### 异步

```python signature
async def bind(self, title: str, *, host: Optional[str] = None, port: Optional[int] = None, workspace_dir: Optional[str] = None) -> patchright._impl._api_structures.BrowserBindResult
```

Browser.bind

Binds the browser to a named pipe or web socket, making it available for other clients to connect to.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `title` | str | Title of the browser server, used for identification. |
| `host` | Union[str, None] | Host to bind the web socket server to. When specified, a web socket server is created instead of a named pipe. |
| `port` | Union[int, None] | Port to bind the web socket server to. When specified, a web socket server is created instead of a named pipe. Use `0` to let the OS pick an available port. |
| `workspace_dir` | Union[str, None] | Working directory associated with this browser server. |

#### Returns
{endpoint: str}


## browser_type

属性，直接读取；异步入口也不加 await。

```python signature
Browser.browser_type: BrowserType
```

Browser.browser_type

Get the browser type (chromium, firefox or webkit) that the browser belongs to.

#### Returns
BrowserType


## close

### 同步

```python signature
def close(self, *, reason: Optional[str] = None) -> None
```

Browser.close

In case this browser is obtained using `browser_type.launch()`, closes the browser and all of its pages (if any
were opened).

In case this browser is connected to, clears all created contexts belonging to this browser and disconnects from
the browser server.

**NOTE** This is similar to force-quitting the browser. To close pages gracefully and ensure you receive page close
events, call `browser_context.close()` on any `BrowserContext` instances you explicitly created earlier using
`browser.new_context()` **before** calling `browser.close()`.

The `Browser` object itself is considered to be disposed and cannot be used anymore.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `reason` | Union[str, None] | The reason to be reported to the operations interrupted by the browser closure. |

### 异步

```python signature
async def close(self, *, reason: Optional[str] = None) -> None
```

Browser.close

In case this browser is obtained using `browser_type.launch()`, closes the browser and all of its pages (if any
were opened).

In case this browser is connected to, clears all created contexts belonging to this browser and disconnects from
the browser server.

**NOTE** This is similar to force-quitting the browser. To close pages gracefully and ensure you receive page close
events, call `browser_context.close()` on any `BrowserContext` instances you explicitly created earlier using
`browser.new_context()` **before** calling `browser.close()`.

The `Browser` object itself is considered to be disposed and cannot be used anymore.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `reason` | Union[str, None] | The reason to be reported to the operations interrupted by the browser closure. |

## contexts

属性，直接读取；异步入口也不加 await。

```python signature
Browser.contexts: typing.List[ForwardRef('BrowserContext')]
```

Browser.contexts

Returns an array of all open browser contexts. In a newly created browser, this will return zero browser contexts.

**Usage**

```py
browser = pw.webkit.launch()
print(len(browser.contexts)) # prints `0`
context = browser.new_context()
print(len(browser.contexts)) # prints `1`
```

#### Returns
List[BrowserContext]


## is_connected

### 同步

```python
def is_connected(self) -> bool
```

Browser.is_connected

Indicates that the browser is connected.

#### Returns
bool

### 异步

```python
def is_connected(self) -> bool
```

Browser.is_connected

Indicates that the browser is connected.

#### Returns
bool


## new_browser_cdp_session

### 同步

```python
def new_browser_cdp_session(self) -> 'CDPSession'
```

Browser.new_browser_cdp_session

**NOTE** CDP Sessions are only supported on Chromium-based browsers.

Returns the newly created browser session.

#### Returns
CDPSession

### 异步

```python
async def new_browser_cdp_session(self) -> 'CDPSession'
```

Browser.new_browser_cdp_session

**NOTE** CDP Sessions are only supported on Chromium-based browsers.

Returns the newly created browser session.

#### Returns
CDPSession


## new_context

### 同步

```python signature
def new_context(self, *, accept_downloads: Optional[bool] = None, base_url: Optional[str] = None, bypass_csp: Optional[bool] = None, client_certificates: Optional[Sequence[patchright._impl._api_structures.ClientCertificate]] = None, color_scheme: Optional[Literal['dark', 'light', 'no-preference', 'null']] = None, contrast: Optional[Literal['more', 'no-preference', 'null']] = None, default_browser_type: Optional[str] = None, device_scale_factor: Optional[float] = None, extra_http_headers: Optional[Dict[str, str]] = None, forced_colors: Optional[Literal['active', 'none', 'null']] = None, geolocation: Optional[patchright._impl._api_structures.Geolocation] = None, has_touch: Optional[bool] = None, http_credentials: Union[patchright._impl._api_structures.HttpCredentials, Sequence[patchright._impl._api_structures.HttpCredentials], NoneType] = None, ignore_https_errors: Optional[bool] = None, is_mobile: Optional[bool] = None, java_script_enabled: Optional[bool] = None, locale: Optional[str] = None, no_viewport: Optional[bool] = None, offline: Optional[bool] = None, permissions: Optional[Sequence[str]] = None, proxy: Optional[patchright._impl._api_structures.ProxySettings] = None, record_har_content: Optional[Literal['attach', 'embed', 'omit']] = None, record_har_mode: Optional[Literal['full', 'minimal']] = None, record_har_omit_content: Optional[bool] = None, record_har_path: Union[pathlib.Path, str, NoneType] = None, record_har_url_filter: Union[str, Pattern[str], NoneType] = None, record_video_dir: Union[pathlib.Path, str, NoneType] = None, record_video_fps: Optional[int] = None, record_video_size: Optional[patchright._impl._api_structures.ViewportSize] = None, reduced_motion: Optional[Literal['no-preference', 'null', 'reduce']] = None, screen: Optional[patchright._impl._api_structures.ViewportSize] = None, service_workers: Optional[Literal['allow', 'block']] = None, storage_state: Union[str, pathlib.Path, patchright._impl._api_structures.StorageState, NoneType] = None, strict_selectors: Optional[bool] = None, timezone_id: Optional[str] = None, user_agent: Optional[str] = None, viewport: Optional[patchright._impl._api_structures.ViewportSize] = None, focus_control: Optional[bool] = None) -> 'BrowserContext'
```

Browser.new_context

Creates a new browser context. It won't share cookies/cache with other browser contexts.

**NOTE** If directly using this method to create `BrowserContext`s, it is best practice to explicitly close the
returned context via `browser_context.close()` when your code is done with the `BrowserContext`, and before calling
`browser.close()`. This will ensure the `context` is closed gracefully and any artifacts—like HARs and videos—are
fully flushed and saved.

**Usage**

```py
browser = playwright.firefox.launch() # or "chromium" or "webkit".
# create a new incognito browser context.
context = browser.new_context()
# create a new page in a pristine context.
page = context.new_page()
page.goto("https://example.com")

# gracefully close up everything
context.close()
browser.close()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `accept_downloads` | Union[bool, None] | Whether to automatically download all the attachments. Defaults to `true` where all the downloads are accepted. |
| `base_url` | Union[str, None] | When using `page.goto()`, `page.route()`, `page.wait_for_url()`, `page.expect_request()`, or `page.expect_response()` it takes the base URL in consideration by using the [`URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) constructor for building the corresponding URL. Unset by default. Examples: - baseURL: `http://localhost:3000` and navigating to `/bar.html` results in `http://localhost:3000/bar.html` - baseURL: `http://localhost:3000/foo/` and navigating to `./bar.html` results in `http://localhost:3000/foo/bar.html` - baseURL: `http://localhost:3000/foo` (without trailing slash) and navigating to `./bar.html` results in `http://localhost:3000/bar.html` |
| `bypass_csp` | Union[bool, None] | Toggles bypassing page's Content-Security-Policy. Defaults to `false`. |
| `client_certificates` | Union[Sequence[{origin: str, certPath: Union[pathlib.Path, str, None], cert: Union[bytes, None], keyPath: Union[pathlib.Path, str, None], key: Union[bytes, None], pfxPath: Union[pathlib.Path, str, None], pfx: Union[bytes, None], passphrase: Union[str, None]}], None] | TLS Client Authentication allows the server to request a client certificate and verify it.  **Details**  An array of client certificates to be used. Each certificate object must have either both `certPath` and `keyPath`, a single `pfxPath`, or their corresponding direct value equivalents (`cert` and `key`, or `pfx`). Optionally, `passphrase` property should be provided if the certificate is encrypted. The `origin` property should be provided with an exact match to the request origin that the certificate is valid for.  Client certificate authentication is only active when at least one client certificate is provided. If you want to reject all client certificates sent by the server, you need to provide a client certificate with an `origin` that does not match any of the domains you plan to visit.  **NOTE** When using WebKit on macOS, accessing `localhost` will not pick up client certificates. You can make it work by replacing `localhost` with `local.playwright`. |
| `color_scheme` | Union["dark", "light", "no-preference", "null", None] | Emulates [prefers-colors-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) media feature, supported values are `'light'` and `'dark'`. See `page.emulate_media()` for more details. Passing `'null'` resets emulation to system defaults. Defaults to `'light'`. |
| `contrast` | Union["more", "no-preference", "null", None] | Emulates `'prefers-contrast'` media feature, supported values are `'no-preference'`, `'more'`. See `page.emulate_media()` for more details. Passing `'null'` resets emulation to system defaults. Defaults to `'no-preference'`. |
| `device_scale_factor` | Union[float, None] | Specify device scale factor (can be thought of as dpr). Defaults to `1`. Learn more about emulating devices with device scale factor. |
| `extra_http_headers` | Union[Dict[str, str], None] | An object containing additional HTTP headers to be sent with every request. Defaults to none. |
| `forced_colors` | Union["active", "none", "null", None] | Emulates `'forced-colors'` media feature, supported values are `'active'`, `'none'`. See `page.emulate_media()` for more details. Passing `'null'` resets emulation to system defaults. Defaults to `'none'`. |
| `geolocation` | Union[{latitude: float, longitude: float, accuracy: Union[float, None]}, None] |  |
| `has_touch` | Union[bool, None] | Specifies if viewport supports touch events. Defaults to false. Learn more about mobile emulation. |
| `http_credentials` | Union[Sequence[{username: str, password: str, origin: Union[str, None], send: Union["always", "unauthorized", None]}], {username: str, password: str, origin: Union[str, None], send: Union["always", "unauthorized", None]}, None] | Credentials for [HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication). If no origin is specified, the username and password are sent to any servers upon unauthorized responses.  Pass an array to use different credentials for different origins. The first entry that matches the request origin is used, and entries with no origin match any request. |
| `ignore_https_errors` | Union[bool, None] | Whether to ignore HTTPS errors when sending network requests. Defaults to `false`. |
| `is_mobile` | Union[bool, None] | Whether the `meta viewport` tag is taken into account and touch events are enabled. isMobile is a part of device, so you don't actually need to set it manually. Defaults to `false`. Learn more about mobile emulation. |
| `java_script_enabled` | Union[bool, None] | Whether or not to enable JavaScript in the context. Defaults to `true`. Learn more about disabling JavaScript. |
| `locale` | Union[str, None] | Specify user locale, for example `en-GB`, `de-DE`, etc. Locale will affect `navigator.language` value, `Accept-Language` request header value as well as number and date formatting rules. Defaults to the system default locale. Learn more about emulation in our emulation guide. |
| `no_viewport` | Union[bool, None] | Does not enforce fixed viewport, allows resizing window in the headed mode. |
| `offline` | Union[bool, None] | Whether to emulate network being offline. Defaults to `false`. Learn more about network emulation. |
| `permissions` | Union[Sequence[str], None] | A list of permissions to grant to all pages in this context. See `browser_context.grant_permissions()` for more details. Defaults to none. |
| `proxy` | Union[{server: str, bypass: Union[str, None], username: Union[str, None], password: Union[str, None]}, None] | Network proxy settings to use with this context. Defaults to none. |
| `record_har_content` | Union["attach", "embed", "omit", None] | Optional setting to control resource content management. If `omit` is specified, content is not persisted. If `attach` is specified, resources are persisted as separate files and all of these files are archived along with the HAR file. Defaults to `embed`, which stores content inline the HAR file as per HAR specification. |
| `record_har_mode` | Union["full", "minimal", None] | When set to `minimal`, only record information necessary for routing from HAR. This omits sizes, timing, page, cookies, security and other types of HAR information that are not used when replaying from HAR. Defaults to `full`. |
| `record_har_omit_content` | Union[bool, None] | Optional setting to control whether to omit request content from the HAR. Defaults to `false`. |
| `record_har_path` | Union[pathlib.Path, str, None] | Enables [HAR](http://www.softwareishard.com/blog/har-12-spec) recording for all pages into the specified HAR file on the filesystem. If not specified, the HAR is not recorded. Make sure to call `browser_context.close()` for the HAR to be saved. |
| `record_har_url_filter` | Union[Pattern[str], str, None] |  |
| `record_video_dir` | Union[pathlib.Path, str, None] | Enables video recording for all pages into the specified directory. If not specified videos are not recorded. Make sure to call `browser_context.close()` for videos to be saved. |
| `record_video_fps` | Union[int, None] | Frame rate of the recorded videos in frames per second. Defaults to `25`. Firefox and WebKit currently capture up to 25 frames per second. |
| `record_video_size` | Union[{width: int, height: int}, None] | Dimensions of the recorded videos. If not specified the size will be equal to `viewport` scaled down to fit into 800x800. If `viewport` is not configured explicitly the video size defaults to 800x450. Actual picture of each page will be scaled down if necessary to fit the specified size. |
| `reduced_motion` | Union["no-preference", "null", "reduce", None] | Emulates `'prefers-reduced-motion'` media feature, supported values are `'reduce'`, `'no-preference'`. See `page.emulate_media()` for more details. Passing `'null'` resets emulation to system defaults. Defaults to `'no-preference'`. |
| `screen` | Union[{width: int, height: int}, None] | Emulates consistent window screen size available inside web page via `window.screen`. Is only used when the `viewport` is set. |
| `service_workers` | Union["allow", "block", None] | Whether to allow sites to register Service workers. Defaults to `'allow'`. - `'allow'`: [Service Workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API) can be registered. - `'block'`: Playwright will block all registration of Service Workers. |
| `storage_state` | Union[pathlib.Path, str, {cookies: Sequence[{name: str, value: str, domain: str, path: str, expires: float, httpOnly: bool, secure: bool, sameSite: Union["Lax", "None", "Strict"]}], origins: Sequence[{origin: str, localStorage: Sequence[{name: str, value: str}]}]}, None] | Learn more about storage state and auth.  Populates context with given storage state. This option can be used to initialize context with logged-in information obtained via `browser_context.storage_state()`. |
| `strict_selectors` | Union[bool, None] | If set to true, enables strict selectors mode for this context. In the strict selectors mode all operations on selectors that imply single target DOM element will throw when more than one element matches the selector. This option does not affect any Locator APIs (Locators are always strict). Defaults to `false`. See `Locator` to learn more about the strict mode. |
| `timezone_id` | Union[str, None] | Changes the timezone of the context. See [ICU's metaZones.txt](https://cs.chromium.org/chromium/src/third_party/icu/source/data/misc/metaZones.txt?rcl=faee8bc70570192d82d2978a71e2a615788597d1) for a list of supported timezone IDs. Defaults to the system timezone. |
| `user_agent` | Union[str, None] | Specific user agent to use in this context. |
| `viewport` | Union[{width: int, height: int}, None] | Sets a consistent viewport for each page. Defaults to an 1280x720 viewport. `no_viewport` disables the fixed viewport. Learn more about viewport emulation. |

#### Returns
BrowserContext

### 异步

```python signature
async def new_context(self, *, accept_downloads: Optional[bool] = None, base_url: Optional[str] = None, bypass_csp: Optional[bool] = None, client_certificates: Optional[Sequence[patchright._impl._api_structures.ClientCertificate]] = None, color_scheme: Optional[Literal['dark', 'light', 'no-preference', 'null']] = None, contrast: Optional[Literal['more', 'no-preference', 'null']] = None, default_browser_type: Optional[str] = None, device_scale_factor: Optional[float] = None, extra_http_headers: Optional[Dict[str, str]] = None, forced_colors: Optional[Literal['active', 'none', 'null']] = None, geolocation: Optional[patchright._impl._api_structures.Geolocation] = None, has_touch: Optional[bool] = None, http_credentials: Union[patchright._impl._api_structures.HttpCredentials, Sequence[patchright._impl._api_structures.HttpCredentials], NoneType] = None, ignore_https_errors: Optional[bool] = None, is_mobile: Optional[bool] = None, java_script_enabled: Optional[bool] = None, locale: Optional[str] = None, no_viewport: Optional[bool] = None, offline: Optional[bool] = None, permissions: Optional[Sequence[str]] = None, proxy: Optional[patchright._impl._api_structures.ProxySettings] = None, record_har_content: Optional[Literal['attach', 'embed', 'omit']] = None, record_har_mode: Optional[Literal['full', 'minimal']] = None, record_har_omit_content: Optional[bool] = None, record_har_path: Union[pathlib.Path, str, NoneType] = None, record_har_url_filter: Union[str, Pattern[str], NoneType] = None, record_video_dir: Union[pathlib.Path, str, NoneType] = None, record_video_fps: Optional[int] = None, record_video_size: Optional[patchright._impl._api_structures.ViewportSize] = None, reduced_motion: Optional[Literal['no-preference', 'null', 'reduce']] = None, screen: Optional[patchright._impl._api_structures.ViewportSize] = None, service_workers: Optional[Literal['allow', 'block']] = None, storage_state: Union[str, pathlib.Path, patchright._impl._api_structures.StorageState, NoneType] = None, strict_selectors: Optional[bool] = None, timezone_id: Optional[str] = None, user_agent: Optional[str] = None, viewport: Optional[patchright._impl._api_structures.ViewportSize] = None, focus_control: Optional[bool] = None) -> 'BrowserContext'
```

Browser.new_context

Creates a new browser context. It won't share cookies/cache with other browser contexts.

**NOTE** If directly using this method to create `BrowserContext`s, it is best practice to explicitly close the
returned context via `browser_context.close()` when your code is done with the `BrowserContext`, and before calling
`browser.close()`. This will ensure the `context` is closed gracefully and any artifacts—like HARs and videos—are
fully flushed and saved.

**Usage**

```py
browser = await playwright.firefox.launch() # or "chromium" or "webkit".
# create a new incognito browser context.
context = await browser.new_context()
# create a new page in a pristine context.
page = await context.new_page()
await page.goto("https://example.com")

# gracefully close up everything
await context.close()
await browser.close()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `accept_downloads` | Union[bool, None] | Whether to automatically download all the attachments. Defaults to `true` where all the downloads are accepted. |
| `base_url` | Union[str, None] | When using `page.goto()`, `page.route()`, `page.wait_for_url()`, `page.expect_request()`, or `page.expect_response()` it takes the base URL in consideration by using the [`URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) constructor for building the corresponding URL. Unset by default. Examples: - baseURL: `http://localhost:3000` and navigating to `/bar.html` results in `http://localhost:3000/bar.html` - baseURL: `http://localhost:3000/foo/` and navigating to `./bar.html` results in `http://localhost:3000/foo/bar.html` - baseURL: `http://localhost:3000/foo` (without trailing slash) and navigating to `./bar.html` results in `http://localhost:3000/bar.html` |
| `bypass_csp` | Union[bool, None] | Toggles bypassing page's Content-Security-Policy. Defaults to `false`. |
| `client_certificates` | Union[Sequence[{origin: str, certPath: Union[pathlib.Path, str, None], cert: Union[bytes, None], keyPath: Union[pathlib.Path, str, None], key: Union[bytes, None], pfxPath: Union[pathlib.Path, str, None], pfx: Union[bytes, None], passphrase: Union[str, None]}], None] | TLS Client Authentication allows the server to request a client certificate and verify it.  **Details**  An array of client certificates to be used. Each certificate object must have either both `certPath` and `keyPath`, a single `pfxPath`, or their corresponding direct value equivalents (`cert` and `key`, or `pfx`). Optionally, `passphrase` property should be provided if the certificate is encrypted. The `origin` property should be provided with an exact match to the request origin that the certificate is valid for.  Client certificate authentication is only active when at least one client certificate is provided. If you want to reject all client certificates sent by the server, you need to provide a client certificate with an `origin` that does not match any of the domains you plan to visit.  **NOTE** When using WebKit on macOS, accessing `localhost` will not pick up client certificates. You can make it work by replacing `localhost` with `local.playwright`. |
| `color_scheme` | Union["dark", "light", "no-preference", "null", None] | Emulates [prefers-colors-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) media feature, supported values are `'light'` and `'dark'`. See `page.emulate_media()` for more details. Passing `'null'` resets emulation to system defaults. Defaults to `'light'`. |
| `contrast` | Union["more", "no-preference", "null", None] | Emulates `'prefers-contrast'` media feature, supported values are `'no-preference'`, `'more'`. See `page.emulate_media()` for more details. Passing `'null'` resets emulation to system defaults. Defaults to `'no-preference'`. |
| `device_scale_factor` | Union[float, None] | Specify device scale factor (can be thought of as dpr). Defaults to `1`. Learn more about emulating devices with device scale factor. |
| `extra_http_headers` | Union[Dict[str, str], None] | An object containing additional HTTP headers to be sent with every request. Defaults to none. |
| `forced_colors` | Union["active", "none", "null", None] | Emulates `'forced-colors'` media feature, supported values are `'active'`, `'none'`. See `page.emulate_media()` for more details. Passing `'null'` resets emulation to system defaults. Defaults to `'none'`. |
| `geolocation` | Union[{latitude: float, longitude: float, accuracy: Union[float, None]}, None] |  |
| `has_touch` | Union[bool, None] | Specifies if viewport supports touch events. Defaults to false. Learn more about mobile emulation. |
| `http_credentials` | Union[Sequence[{username: str, password: str, origin: Union[str, None], send: Union["always", "unauthorized", None]}], {username: str, password: str, origin: Union[str, None], send: Union["always", "unauthorized", None]}, None] | Credentials for [HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication). If no origin is specified, the username and password are sent to any servers upon unauthorized responses.  Pass an array to use different credentials for different origins. The first entry that matches the request origin is used, and entries with no origin match any request. |
| `ignore_https_errors` | Union[bool, None] | Whether to ignore HTTPS errors when sending network requests. Defaults to `false`. |
| `is_mobile` | Union[bool, None] | Whether the `meta viewport` tag is taken into account and touch events are enabled. isMobile is a part of device, so you don't actually need to set it manually. Defaults to `false`. Learn more about mobile emulation. |
| `java_script_enabled` | Union[bool, None] | Whether or not to enable JavaScript in the context. Defaults to `true`. Learn more about disabling JavaScript. |
| `locale` | Union[str, None] | Specify user locale, for example `en-GB`, `de-DE`, etc. Locale will affect `navigator.language` value, `Accept-Language` request header value as well as number and date formatting rules. Defaults to the system default locale. Learn more about emulation in our emulation guide. |
| `no_viewport` | Union[bool, None] | Does not enforce fixed viewport, allows resizing window in the headed mode. |
| `offline` | Union[bool, None] | Whether to emulate network being offline. Defaults to `false`. Learn more about network emulation. |
| `permissions` | Union[Sequence[str], None] | A list of permissions to grant to all pages in this context. See `browser_context.grant_permissions()` for more details. Defaults to none. |
| `proxy` | Union[{server: str, bypass: Union[str, None], username: Union[str, None], password: Union[str, None]}, None] | Network proxy settings to use with this context. Defaults to none. |
| `record_har_content` | Union["attach", "embed", "omit", None] | Optional setting to control resource content management. If `omit` is specified, content is not persisted. If `attach` is specified, resources are persisted as separate files and all of these files are archived along with the HAR file. Defaults to `embed`, which stores content inline the HAR file as per HAR specification. |
| `record_har_mode` | Union["full", "minimal", None] | When set to `minimal`, only record information necessary for routing from HAR. This omits sizes, timing, page, cookies, security and other types of HAR information that are not used when replaying from HAR. Defaults to `full`. |
| `record_har_omit_content` | Union[bool, None] | Optional setting to control whether to omit request content from the HAR. Defaults to `false`. |
| `record_har_path` | Union[pathlib.Path, str, None] | Enables [HAR](http://www.softwareishard.com/blog/har-12-spec) recording for all pages into the specified HAR file on the filesystem. If not specified, the HAR is not recorded. Make sure to call `browser_context.close()` for the HAR to be saved. |
| `record_har_url_filter` | Union[Pattern[str], str, None] |  |
| `record_video_dir` | Union[pathlib.Path, str, None] | Enables video recording for all pages into the specified directory. If not specified videos are not recorded. Make sure to call `browser_context.close()` for videos to be saved. |
| `record_video_fps` | Union[int, None] | Frame rate of the recorded videos in frames per second. Defaults to `25`. Firefox and WebKit currently capture up to 25 frames per second. |
| `record_video_size` | Union[{width: int, height: int}, None] | Dimensions of the recorded videos. If not specified the size will be equal to `viewport` scaled down to fit into 800x800. If `viewport` is not configured explicitly the video size defaults to 800x450. Actual picture of each page will be scaled down if necessary to fit the specified size. |
| `reduced_motion` | Union["no-preference", "null", "reduce", None] | Emulates `'prefers-reduced-motion'` media feature, supported values are `'reduce'`, `'no-preference'`. See `page.emulate_media()` for more details. Passing `'null'` resets emulation to system defaults. Defaults to `'no-preference'`. |
| `screen` | Union[{width: int, height: int}, None] | Emulates consistent window screen size available inside web page via `window.screen`. Is only used when the `viewport` is set. |
| `service_workers` | Union["allow", "block", None] | Whether to allow sites to register Service workers. Defaults to `'allow'`. - `'allow'`: [Service Workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API) can be registered. - `'block'`: Playwright will block all registration of Service Workers. |
| `storage_state` | Union[pathlib.Path, str, {cookies: Sequence[{name: str, value: str, domain: str, path: str, expires: float, httpOnly: bool, secure: bool, sameSite: Union["Lax", "None", "Strict"]}], origins: Sequence[{origin: str, localStorage: Sequence[{name: str, value: str}]}]}, None] | Learn more about storage state and auth.  Populates context with given storage state. This option can be used to initialize context with logged-in information obtained via `browser_context.storage_state()`. |
| `strict_selectors` | Union[bool, None] | If set to true, enables strict selectors mode for this context. In the strict selectors mode all operations on selectors that imply single target DOM element will throw when more than one element matches the selector. This option does not affect any Locator APIs (Locators are always strict). Defaults to `false`. See `Locator` to learn more about the strict mode. |
| `timezone_id` | Union[str, None] | Changes the timezone of the context. See [ICU's metaZones.txt](https://cs.chromium.org/chromium/src/third_party/icu/source/data/misc/metaZones.txt?rcl=faee8bc70570192d82d2978a71e2a615788597d1) for a list of supported timezone IDs. Defaults to the system timezone. |
| `user_agent` | Union[str, None] | Specific user agent to use in this context. |
| `viewport` | Union[{width: int, height: int}, None] | Sets a consistent viewport for each page. Defaults to an 1280x720 viewport. `no_viewport` disables the fixed viewport. Learn more about viewport emulation. |

#### Returns
BrowserContext


## new_page

### 同步

```python signature
def new_page(self, *, accept_downloads: Optional[bool] = None, base_url: Optional[str] = None, bypass_csp: Optional[bool] = None, client_certificates: Optional[Sequence[patchright._impl._api_structures.ClientCertificate]] = None, color_scheme: Optional[Literal['dark', 'light', 'no-preference', 'null']] = None, contrast: Optional[Literal['more', 'no-preference', 'null']] = None, default_browser_type: Optional[str] = None, device_scale_factor: Optional[float] = None, extra_http_headers: Optional[Dict[str, str]] = None, forced_colors: Optional[Literal['active', 'none', 'null']] = None, geolocation: Optional[patchright._impl._api_structures.Geolocation] = None, has_touch: Optional[bool] = None, http_credentials: Union[patchright._impl._api_structures.HttpCredentials, Sequence[patchright._impl._api_structures.HttpCredentials], NoneType] = None, ignore_https_errors: Optional[bool] = None, is_mobile: Optional[bool] = None, java_script_enabled: Optional[bool] = None, locale: Optional[str] = None, no_viewport: Optional[bool] = None, offline: Optional[bool] = None, permissions: Optional[Sequence[str]] = None, proxy: Optional[patchright._impl._api_structures.ProxySettings] = None, record_har_content: Optional[Literal['attach', 'embed', 'omit']] = None, record_har_mode: Optional[Literal['full', 'minimal']] = None, record_har_omit_content: Optional[bool] = None, record_har_path: Union[pathlib.Path, str, NoneType] = None, record_har_url_filter: Union[str, Pattern[str], NoneType] = None, record_video_dir: Union[pathlib.Path, str, NoneType] = None, record_video_fps: Optional[int] = None, record_video_size: Optional[patchright._impl._api_structures.ViewportSize] = None, reduced_motion: Optional[Literal['no-preference', 'null', 'reduce']] = None, screen: Optional[patchright._impl._api_structures.ViewportSize] = None, service_workers: Optional[Literal['allow', 'block']] = None, storage_state: Union[str, pathlib.Path, patchright._impl._api_structures.StorageState, NoneType] = None, strict_selectors: Optional[bool] = None, timezone_id: Optional[str] = None, user_agent: Optional[str] = None, viewport: Optional[patchright._impl._api_structures.ViewportSize] = None, focus_control: Optional[bool] = None) -> 'Page'
```

Browser.new_page

Creates a new page in a new browser context. Closing this page will close the context as well.

This is a convenience API that should only be used for the single-page scenarios and short snippets. Production
code and testing frameworks should explicitly create `browser.new_context()` followed by the
`browser_context.new_page()` to control their exact life times.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `accept_downloads` | Union[bool, None] | Whether to automatically download all the attachments. Defaults to `true` where all the downloads are accepted. |
| `base_url` | Union[str, None] | When using `page.goto()`, `page.route()`, `page.wait_for_url()`, `page.expect_request()`, or `page.expect_response()` it takes the base URL in consideration by using the [`URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) constructor for building the corresponding URL. Unset by default. Examples: - baseURL: `http://localhost:3000` and navigating to `/bar.html` results in `http://localhost:3000/bar.html` - baseURL: `http://localhost:3000/foo/` and navigating to `./bar.html` results in `http://localhost:3000/foo/bar.html` - baseURL: `http://localhost:3000/foo` (without trailing slash) and navigating to `./bar.html` results in `http://localhost:3000/bar.html` |
| `bypass_csp` | Union[bool, None] | Toggles bypassing page's Content-Security-Policy. Defaults to `false`. |
| `client_certificates` | Union[Sequence[{origin: str, certPath: Union[pathlib.Path, str, None], cert: Union[bytes, None], keyPath: Union[pathlib.Path, str, None], key: Union[bytes, None], pfxPath: Union[pathlib.Path, str, None], pfx: Union[bytes, None], passphrase: Union[str, None]}], None] | TLS Client Authentication allows the server to request a client certificate and verify it.  **Details**  An array of client certificates to be used. Each certificate object must have either both `certPath` and `keyPath`, a single `pfxPath`, or their corresponding direct value equivalents (`cert` and `key`, or `pfx`). Optionally, `passphrase` property should be provided if the certificate is encrypted. The `origin` property should be provided with an exact match to the request origin that the certificate is valid for.  Client certificate authentication is only active when at least one client certificate is provided. If you want to reject all client certificates sent by the server, you need to provide a client certificate with an `origin` that does not match any of the domains you plan to visit.  **NOTE** When using WebKit on macOS, accessing `localhost` will not pick up client certificates. You can make it work by replacing `localhost` with `local.playwright`. |
| `color_scheme` | Union["dark", "light", "no-preference", "null", None] | Emulates [prefers-colors-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) media feature, supported values are `'light'` and `'dark'`. See `page.emulate_media()` for more details. Passing `'null'` resets emulation to system defaults. Defaults to `'light'`. |
| `contrast` | Union["more", "no-preference", "null", None] | Emulates `'prefers-contrast'` media feature, supported values are `'no-preference'`, `'more'`. See `page.emulate_media()` for more details. Passing `'null'` resets emulation to system defaults. Defaults to `'no-preference'`. |
| `device_scale_factor` | Union[float, None] | Specify device scale factor (can be thought of as dpr). Defaults to `1`. Learn more about emulating devices with device scale factor. |
| `extra_http_headers` | Union[Dict[str, str], None] | An object containing additional HTTP headers to be sent with every request. Defaults to none. |
| `forced_colors` | Union["active", "none", "null", None] | Emulates `'forced-colors'` media feature, supported values are `'active'`, `'none'`. See `page.emulate_media()` for more details. Passing `'null'` resets emulation to system defaults. Defaults to `'none'`. |
| `geolocation` | Union[{latitude: float, longitude: float, accuracy: Union[float, None]}, None] |  |
| `has_touch` | Union[bool, None] | Specifies if viewport supports touch events. Defaults to false. Learn more about mobile emulation. |
| `http_credentials` | Union[Sequence[{username: str, password: str, origin: Union[str, None], send: Union["always", "unauthorized", None]}], {username: str, password: str, origin: Union[str, None], send: Union["always", "unauthorized", None]}, None] | Credentials for [HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication). If no origin is specified, the username and password are sent to any servers upon unauthorized responses.  Pass an array to use different credentials for different origins. The first entry that matches the request origin is used, and entries with no origin match any request. |
| `ignore_https_errors` | Union[bool, None] | Whether to ignore HTTPS errors when sending network requests. Defaults to `false`. |
| `is_mobile` | Union[bool, None] | Whether the `meta viewport` tag is taken into account and touch events are enabled. isMobile is a part of device, so you don't actually need to set it manually. Defaults to `false`. Learn more about mobile emulation. |
| `java_script_enabled` | Union[bool, None] | Whether or not to enable JavaScript in the context. Defaults to `true`. Learn more about disabling JavaScript. |
| `locale` | Union[str, None] | Specify user locale, for example `en-GB`, `de-DE`, etc. Locale will affect `navigator.language` value, `Accept-Language` request header value as well as number and date formatting rules. Defaults to the system default locale. Learn more about emulation in our emulation guide. |
| `no_viewport` | Union[bool, None] | Does not enforce fixed viewport, allows resizing window in the headed mode. |
| `offline` | Union[bool, None] | Whether to emulate network being offline. Defaults to `false`. Learn more about network emulation. |
| `permissions` | Union[Sequence[str], None] | A list of permissions to grant to all pages in this context. See `browser_context.grant_permissions()` for more details. Defaults to none. |
| `proxy` | Union[{server: str, bypass: Union[str, None], username: Union[str, None], password: Union[str, None]}, None] | Network proxy settings to use with this context. Defaults to none. |
| `record_har_content` | Union["attach", "embed", "omit", None] | Optional setting to control resource content management. If `omit` is specified, content is not persisted. If `attach` is specified, resources are persisted as separate files and all of these files are archived along with the HAR file. Defaults to `embed`, which stores content inline the HAR file as per HAR specification. |
| `record_har_mode` | Union["full", "minimal", None] | When set to `minimal`, only record information necessary for routing from HAR. This omits sizes, timing, page, cookies, security and other types of HAR information that are not used when replaying from HAR. Defaults to `full`. |
| `record_har_omit_content` | Union[bool, None] | Optional setting to control whether to omit request content from the HAR. Defaults to `false`. |
| `record_har_path` | Union[pathlib.Path, str, None] | Enables [HAR](http://www.softwareishard.com/blog/har-12-spec) recording for all pages into the specified HAR file on the filesystem. If not specified, the HAR is not recorded. Make sure to call `browser_context.close()` for the HAR to be saved. |
| `record_har_url_filter` | Union[Pattern[str], str, None] |  |
| `record_video_dir` | Union[pathlib.Path, str, None] | Enables video recording for all pages into the specified directory. If not specified videos are not recorded. Make sure to call `browser_context.close()` for videos to be saved. |
| `record_video_fps` | Union[int, None] | Frame rate of the recorded videos in frames per second. Defaults to `25`. Firefox and WebKit currently capture up to 25 frames per second. |
| `record_video_size` | Union[{width: int, height: int}, None] | Dimensions of the recorded videos. If not specified the size will be equal to `viewport` scaled down to fit into 800x800. If `viewport` is not configured explicitly the video size defaults to 800x450. Actual picture of each page will be scaled down if necessary to fit the specified size. |
| `reduced_motion` | Union["no-preference", "null", "reduce", None] | Emulates `'prefers-reduced-motion'` media feature, supported values are `'reduce'`, `'no-preference'`. See `page.emulate_media()` for more details. Passing `'null'` resets emulation to system defaults. Defaults to `'no-preference'`. |
| `screen` | Union[{width: int, height: int}, None] | Emulates consistent window screen size available inside web page via `window.screen`. Is only used when the `viewport` is set. |
| `service_workers` | Union["allow", "block", None] | Whether to allow sites to register Service workers. Defaults to `'allow'`. - `'allow'`: [Service Workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API) can be registered. - `'block'`: Playwright will block all registration of Service Workers. |
| `storage_state` | Union[pathlib.Path, str, {cookies: Sequence[{name: str, value: str, domain: str, path: str, expires: float, httpOnly: bool, secure: bool, sameSite: Union["Lax", "None", "Strict"]}], origins: Sequence[{origin: str, localStorage: Sequence[{name: str, value: str}]}]}, None] | Learn more about storage state and auth.  Populates context with given storage state. This option can be used to initialize context with logged-in information obtained via `browser_context.storage_state()`. |
| `strict_selectors` | Union[bool, None] | If set to true, enables strict selectors mode for this context. In the strict selectors mode all operations on selectors that imply single target DOM element will throw when more than one element matches the selector. This option does not affect any Locator APIs (Locators are always strict). Defaults to `false`. See `Locator` to learn more about the strict mode. |
| `timezone_id` | Union[str, None] | Changes the timezone of the context. See [ICU's metaZones.txt](https://cs.chromium.org/chromium/src/third_party/icu/source/data/misc/metaZones.txt?rcl=faee8bc70570192d82d2978a71e2a615788597d1) for a list of supported timezone IDs. Defaults to the system timezone. |
| `user_agent` | Union[str, None] | Specific user agent to use in this context. |
| `viewport` | Union[{width: int, height: int}, None] | Sets a consistent viewport for each page. Defaults to an 1280x720 viewport. `no_viewport` disables the fixed viewport. Learn more about viewport emulation. |

#### Returns
Page

### 异步

```python signature
async def new_page(self, *, accept_downloads: Optional[bool] = None, base_url: Optional[str] = None, bypass_csp: Optional[bool] = None, client_certificates: Optional[Sequence[patchright._impl._api_structures.ClientCertificate]] = None, color_scheme: Optional[Literal['dark', 'light', 'no-preference', 'null']] = None, contrast: Optional[Literal['more', 'no-preference', 'null']] = None, default_browser_type: Optional[str] = None, device_scale_factor: Optional[float] = None, extra_http_headers: Optional[Dict[str, str]] = None, forced_colors: Optional[Literal['active', 'none', 'null']] = None, geolocation: Optional[patchright._impl._api_structures.Geolocation] = None, has_touch: Optional[bool] = None, http_credentials: Union[patchright._impl._api_structures.HttpCredentials, Sequence[patchright._impl._api_structures.HttpCredentials], NoneType] = None, ignore_https_errors: Optional[bool] = None, is_mobile: Optional[bool] = None, java_script_enabled: Optional[bool] = None, locale: Optional[str] = None, no_viewport: Optional[bool] = None, offline: Optional[bool] = None, permissions: Optional[Sequence[str]] = None, proxy: Optional[patchright._impl._api_structures.ProxySettings] = None, record_har_content: Optional[Literal['attach', 'embed', 'omit']] = None, record_har_mode: Optional[Literal['full', 'minimal']] = None, record_har_omit_content: Optional[bool] = None, record_har_path: Union[pathlib.Path, str, NoneType] = None, record_har_url_filter: Union[str, Pattern[str], NoneType] = None, record_video_dir: Union[pathlib.Path, str, NoneType] = None, record_video_fps: Optional[int] = None, record_video_size: Optional[patchright._impl._api_structures.ViewportSize] = None, reduced_motion: Optional[Literal['no-preference', 'null', 'reduce']] = None, screen: Optional[patchright._impl._api_structures.ViewportSize] = None, service_workers: Optional[Literal['allow', 'block']] = None, storage_state: Union[str, pathlib.Path, patchright._impl._api_structures.StorageState, NoneType] = None, strict_selectors: Optional[bool] = None, timezone_id: Optional[str] = None, user_agent: Optional[str] = None, viewport: Optional[patchright._impl._api_structures.ViewportSize] = None, focus_control: Optional[bool] = None) -> 'Page'
```

Browser.new_page

Creates a new page in a new browser context. Closing this page will close the context as well.

This is a convenience API that should only be used for the single-page scenarios and short snippets. Production
code and testing frameworks should explicitly create `browser.new_context()` followed by the
`browser_context.new_page()` to control their exact life times.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `accept_downloads` | Union[bool, None] | Whether to automatically download all the attachments. Defaults to `true` where all the downloads are accepted. |
| `base_url` | Union[str, None] | When using `page.goto()`, `page.route()`, `page.wait_for_url()`, `page.expect_request()`, or `page.expect_response()` it takes the base URL in consideration by using the [`URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) constructor for building the corresponding URL. Unset by default. Examples: - baseURL: `http://localhost:3000` and navigating to `/bar.html` results in `http://localhost:3000/bar.html` - baseURL: `http://localhost:3000/foo/` and navigating to `./bar.html` results in `http://localhost:3000/foo/bar.html` - baseURL: `http://localhost:3000/foo` (without trailing slash) and navigating to `./bar.html` results in `http://localhost:3000/bar.html` |
| `bypass_csp` | Union[bool, None] | Toggles bypassing page's Content-Security-Policy. Defaults to `false`. |
| `client_certificates` | Union[Sequence[{origin: str, certPath: Union[pathlib.Path, str, None], cert: Union[bytes, None], keyPath: Union[pathlib.Path, str, None], key: Union[bytes, None], pfxPath: Union[pathlib.Path, str, None], pfx: Union[bytes, None], passphrase: Union[str, None]}], None] | TLS Client Authentication allows the server to request a client certificate and verify it.  **Details**  An array of client certificates to be used. Each certificate object must have either both `certPath` and `keyPath`, a single `pfxPath`, or their corresponding direct value equivalents (`cert` and `key`, or `pfx`). Optionally, `passphrase` property should be provided if the certificate is encrypted. The `origin` property should be provided with an exact match to the request origin that the certificate is valid for.  Client certificate authentication is only active when at least one client certificate is provided. If you want to reject all client certificates sent by the server, you need to provide a client certificate with an `origin` that does not match any of the domains you plan to visit.  **NOTE** When using WebKit on macOS, accessing `localhost` will not pick up client certificates. You can make it work by replacing `localhost` with `local.playwright`. |
| `color_scheme` | Union["dark", "light", "no-preference", "null", None] | Emulates [prefers-colors-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) media feature, supported values are `'light'` and `'dark'`. See `page.emulate_media()` for more details. Passing `'null'` resets emulation to system defaults. Defaults to `'light'`. |
| `contrast` | Union["more", "no-preference", "null", None] | Emulates `'prefers-contrast'` media feature, supported values are `'no-preference'`, `'more'`. See `page.emulate_media()` for more details. Passing `'null'` resets emulation to system defaults. Defaults to `'no-preference'`. |
| `device_scale_factor` | Union[float, None] | Specify device scale factor (can be thought of as dpr). Defaults to `1`. Learn more about emulating devices with device scale factor. |
| `extra_http_headers` | Union[Dict[str, str], None] | An object containing additional HTTP headers to be sent with every request. Defaults to none. |
| `forced_colors` | Union["active", "none", "null", None] | Emulates `'forced-colors'` media feature, supported values are `'active'`, `'none'`. See `page.emulate_media()` for more details. Passing `'null'` resets emulation to system defaults. Defaults to `'none'`. |
| `geolocation` | Union[{latitude: float, longitude: float, accuracy: Union[float, None]}, None] |  |
| `has_touch` | Union[bool, None] | Specifies if viewport supports touch events. Defaults to false. Learn more about mobile emulation. |
| `http_credentials` | Union[Sequence[{username: str, password: str, origin: Union[str, None], send: Union["always", "unauthorized", None]}], {username: str, password: str, origin: Union[str, None], send: Union["always", "unauthorized", None]}, None] | Credentials for [HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication). If no origin is specified, the username and password are sent to any servers upon unauthorized responses.  Pass an array to use different credentials for different origins. The first entry that matches the request origin is used, and entries with no origin match any request. |
| `ignore_https_errors` | Union[bool, None] | Whether to ignore HTTPS errors when sending network requests. Defaults to `false`. |
| `is_mobile` | Union[bool, None] | Whether the `meta viewport` tag is taken into account and touch events are enabled. isMobile is a part of device, so you don't actually need to set it manually. Defaults to `false`. Learn more about mobile emulation. |
| `java_script_enabled` | Union[bool, None] | Whether or not to enable JavaScript in the context. Defaults to `true`. Learn more about disabling JavaScript. |
| `locale` | Union[str, None] | Specify user locale, for example `en-GB`, `de-DE`, etc. Locale will affect `navigator.language` value, `Accept-Language` request header value as well as number and date formatting rules. Defaults to the system default locale. Learn more about emulation in our emulation guide. |
| `no_viewport` | Union[bool, None] | Does not enforce fixed viewport, allows resizing window in the headed mode. |
| `offline` | Union[bool, None] | Whether to emulate network being offline. Defaults to `false`. Learn more about network emulation. |
| `permissions` | Union[Sequence[str], None] | A list of permissions to grant to all pages in this context. See `browser_context.grant_permissions()` for more details. Defaults to none. |
| `proxy` | Union[{server: str, bypass: Union[str, None], username: Union[str, None], password: Union[str, None]}, None] | Network proxy settings to use with this context. Defaults to none. |
| `record_har_content` | Union["attach", "embed", "omit", None] | Optional setting to control resource content management. If `omit` is specified, content is not persisted. If `attach` is specified, resources are persisted as separate files and all of these files are archived along with the HAR file. Defaults to `embed`, which stores content inline the HAR file as per HAR specification. |
| `record_har_mode` | Union["full", "minimal", None] | When set to `minimal`, only record information necessary for routing from HAR. This omits sizes, timing, page, cookies, security and other types of HAR information that are not used when replaying from HAR. Defaults to `full`. |
| `record_har_omit_content` | Union[bool, None] | Optional setting to control whether to omit request content from the HAR. Defaults to `false`. |
| `record_har_path` | Union[pathlib.Path, str, None] | Enables [HAR](http://www.softwareishard.com/blog/har-12-spec) recording for all pages into the specified HAR file on the filesystem. If not specified, the HAR is not recorded. Make sure to call `browser_context.close()` for the HAR to be saved. |
| `record_har_url_filter` | Union[Pattern[str], str, None] |  |
| `record_video_dir` | Union[pathlib.Path, str, None] | Enables video recording for all pages into the specified directory. If not specified videos are not recorded. Make sure to call `browser_context.close()` for videos to be saved. |
| `record_video_fps` | Union[int, None] | Frame rate of the recorded videos in frames per second. Defaults to `25`. Firefox and WebKit currently capture up to 25 frames per second. |
| `record_video_size` | Union[{width: int, height: int}, None] | Dimensions of the recorded videos. If not specified the size will be equal to `viewport` scaled down to fit into 800x800. If `viewport` is not configured explicitly the video size defaults to 800x450. Actual picture of each page will be scaled down if necessary to fit the specified size. |
| `reduced_motion` | Union["no-preference", "null", "reduce", None] | Emulates `'prefers-reduced-motion'` media feature, supported values are `'reduce'`, `'no-preference'`. See `page.emulate_media()` for more details. Passing `'null'` resets emulation to system defaults. Defaults to `'no-preference'`. |
| `screen` | Union[{width: int, height: int}, None] | Emulates consistent window screen size available inside web page via `window.screen`. Is only used when the `viewport` is set. |
| `service_workers` | Union["allow", "block", None] | Whether to allow sites to register Service workers. Defaults to `'allow'`. - `'allow'`: [Service Workers](https://developer.mozilla.org/en-US/docs/Web/API/Service_Worker_API) can be registered. - `'block'`: Playwright will block all registration of Service Workers. |
| `storage_state` | Union[pathlib.Path, str, {cookies: Sequence[{name: str, value: str, domain: str, path: str, expires: float, httpOnly: bool, secure: bool, sameSite: Union["Lax", "None", "Strict"]}], origins: Sequence[{origin: str, localStorage: Sequence[{name: str, value: str}]}]}, None] | Learn more about storage state and auth.  Populates context with given storage state. This option can be used to initialize context with logged-in information obtained via `browser_context.storage_state()`. |
| `strict_selectors` | Union[bool, None] | If set to true, enables strict selectors mode for this context. In the strict selectors mode all operations on selectors that imply single target DOM element will throw when more than one element matches the selector. This option does not affect any Locator APIs (Locators are always strict). Defaults to `false`. See `Locator` to learn more about the strict mode. |
| `timezone_id` | Union[str, None] | Changes the timezone of the context. See [ICU's metaZones.txt](https://cs.chromium.org/chromium/src/third_party/icu/source/data/misc/metaZones.txt?rcl=faee8bc70570192d82d2978a71e2a615788597d1) for a list of supported timezone IDs. Defaults to the system timezone. |
| `user_agent` | Union[str, None] | Specific user agent to use in this context. |
| `viewport` | Union[{width: int, height: int}, None] | Sets a consistent viewport for each page. Defaults to an 1280x720 viewport. `no_viewport` disables the fixed viewport. Learn more about viewport emulation. |

#### Returns
Page


## on

### 同步

```python
def on(self, event: str, f: Callable[..., NoneType]) -> None
```

支持的重载：

```python
def on(self, event: Literal['context'], f: Callable[[ForwardRef('BrowserContext')], ForwardRef('None')]) -> None
def on(self, event: Literal['disconnected'], f: Callable[[ForwardRef('Browser')], ForwardRef('None')]) -> None
```

Registers the function ``f`` to the event name ``event``.

### 异步

```python
def on(self, event: str, f: Callable[..., Optional[Awaitable[NoneType]]]) -> None
```

支持的重载：

```python
def on(self, event: Literal['context'], f: Callable[[ForwardRef('BrowserContext')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def on(self, event: Literal['disconnected'], f: Callable[[ForwardRef('Browser')], ForwardRef('Union[Awaitable[None], None]')]) -> None
```

Registers the function ``f`` to the event name ``event``.


## once

### 同步

```python
def once(self, event: str, f: Callable[..., NoneType]) -> None
```

支持的重载：

```python
def once(self, event: Literal['context'], f: Callable[[ForwardRef('BrowserContext')], ForwardRef('None')]) -> None
def once(self, event: Literal['disconnected'], f: Callable[[ForwardRef('Browser')], ForwardRef('None')]) -> None
```

The same as ``self.on``, except that the listener is automatically
removed after being called.

### 异步

```python
def once(self, event: str, f: Callable[..., Optional[Awaitable[NoneType]]]) -> None
```

支持的重载：

```python
def once(self, event: Literal['context'], f: Callable[[ForwardRef('BrowserContext')], ForwardRef('Union[Awaitable[None], None]')]) -> None
def once(self, event: Literal['disconnected'], f: Callable[[ForwardRef('Browser')], ForwardRef('Union[Awaitable[None], None]')]) -> None
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


## start_tracing

### 同步

```python signature
def start_tracing(self, *, categories: Optional[Sequence[str]] = None, page: Optional[ForwardRef('Page')] = None, path: Union[pathlib.Path, str, NoneType] = None, screenshots: Optional[bool] = None) -> None
```

Browser.start_tracing

**NOTE** This API controls
[Chromium Tracing](https://www.chromium.org/developers/how-tos/trace-event-profiling-tool) which is a low-level
chromium-specific debugging tool. API to control [Playwright Tracing](https://playwright.dev/python/docs/trace-viewer) could be found
[here](https://playwright.dev/python/docs/api/class-tracing).

You can use `browser.start_tracing()` and `browser.stop_tracing()` to create a trace file that can be opened in
Chrome DevTools performance panel.

**Usage**

```py
browser.start_tracing(page, path="trace.json")
page.goto("https://www.google.com")
browser.stop_tracing()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `categories` | Union[Sequence[str], None] | specify custom categories to use instead of default. |
| `page` | Union[Page, None] | Optional, if specified, tracing includes screenshots of the given page. |
| `path` | Union[pathlib.Path, str, None] | A path to write the trace file to. |
| `screenshots` | Union[bool, None] | captures screenshots in the trace. |

### 异步

```python signature
async def start_tracing(self, *, categories: Optional[Sequence[str]] = None, page: Optional[ForwardRef('Page')] = None, path: Union[pathlib.Path, str, NoneType] = None, screenshots: Optional[bool] = None) -> None
```

Browser.start_tracing

**NOTE** This API controls
[Chromium Tracing](https://www.chromium.org/developers/how-tos/trace-event-profiling-tool) which is a low-level
chromium-specific debugging tool. API to control [Playwright Tracing](https://playwright.dev/python/docs/trace-viewer) could be found
[here](https://playwright.dev/python/docs/api/class-tracing).

You can use `browser.start_tracing()` and `browser.stop_tracing()` to create a trace file that can be opened in
Chrome DevTools performance panel.

**Usage**

```py
await browser.start_tracing(page, path="trace.json")
await page.goto("https://www.google.com")
await browser.stop_tracing()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `categories` | Union[Sequence[str], None] | specify custom categories to use instead of default. |
| `page` | Union[Page, None] | Optional, if specified, tracing includes screenshots of the given page. |
| `path` | Union[pathlib.Path, str, None] | A path to write the trace file to. |
| `screenshots` | Union[bool, None] | captures screenshots in the trace. |

## stop_tracing

### 同步

```python
def stop_tracing(self) -> bytes
```

Browser.stop_tracing

**NOTE** This API controls
[Chromium Tracing](https://www.chromium.org/developers/how-tos/trace-event-profiling-tool) which is a low-level
chromium-specific debugging tool. API to control [Playwright Tracing](https://playwright.dev/python/docs/trace-viewer) could be found
[here](https://playwright.dev/python/docs/api/class-tracing).

Returns the buffer with trace data.

#### Returns
bytes

### 异步

```python
async def stop_tracing(self) -> bytes
```

Browser.stop_tracing

**NOTE** This API controls
[Chromium Tracing](https://www.chromium.org/developers/how-tos/trace-event-profiling-tool) which is a low-level
chromium-specific debugging tool. API to control [Playwright Tracing](https://playwright.dev/python/docs/trace-viewer) could be found
[here](https://playwright.dev/python/docs/api/class-tracing).

Returns the buffer with trace data.

#### Returns
bytes


## unbind

### 同步

```python
def unbind(self) -> None
```

Browser.unbind

Unbinds the browser server previously bound with `browser.bind()`.

### 异步

```python
async def unbind(self) -> None
```

Browser.unbind

Unbinds the browser server previously bound with `browser.bind()`.


## version

属性，直接读取；异步入口也不加 await。

```python signature
Browser.version: <class 'str'>
```

Browser.version

Returns the browser version.

#### Returns
str
