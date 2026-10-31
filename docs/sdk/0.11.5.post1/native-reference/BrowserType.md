# 原生 BrowserType

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [connect](#connect)
- [connect_over_cdp](#connect_over_cdp)
- [executable_path](#executable_path)
- [launch](#launch)
- [launch_persistent_context](#launch_persistent_context)
- [name](#name)
- [on](#on)
- [once](#once)
- [remove_listener](#remove_listener)

## connect

### 同步

```python signature
def connect(self, endpoint: str, *, expose_network: Optional[str] = None, headers: Optional[Dict[str, str]] = None, slow_mo: Optional[float] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'Browser'
```

BrowserType.connect

This method attaches Playwright to an existing browser instance created via `BrowserType.launchServer` in Node.js.

**NOTE** The major and minor version of the Playwright instance that connects needs to match the version of
Playwright that launches the browser (1.2.3 → is compatible with 1.2.x).

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `endpoint` | str | A Playwright browser websocket endpoint to connect to. You obtain this endpoint via `BrowserServer.wsEndpoint`. |
| `expose_network` | Union[str, None] | This option exposes network available on the connecting client to the browser being connected to. Consists of a list of rules separated by comma.  Available rules: 1. Hostname pattern, for example: `example.com`, `*.org:99`, `x.*.y.com`, `*foo.org`. 1. IP literal, for example: `127.0.0.1`, `0.0.0.0:99`, `[::1]`, `[0:0::1]:99`. 1. `<loopback>` that matches local loopback interfaces: `localhost`, `*.localhost`, `127.0.0.1`, `[::1]`.  Some common examples: 1. `"*"` to expose all network. 1. `"<loopback>"` to expose localhost network. 1. `"*.test.internal-domain,*.staging.internal-domain,<loopback>"` to expose test/staging deployments and localhost. |
| `headers` | Union[Dict[str, str], None] | Additional HTTP headers to be sent with web socket connect request. Optional. |
| `slow_mo` | Union[float, None] | Slows down Playwright operations by the specified amount of milliseconds. Useful so that you can see what is going on. Defaults to 0. |
| `timeout` | Union[float, None] | Maximum time in milliseconds to wait for the connection to be established. Defaults to `0` (no timeout). |

#### Returns
Browser

### 异步

```python signature
async def connect(self, endpoint: str, *, expose_network: Optional[str] = None, headers: Optional[Dict[str, str]] = None, slow_mo: Optional[float] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'Browser'
```

BrowserType.connect

This method attaches Playwright to an existing browser instance created via `BrowserType.launchServer` in Node.js.

**NOTE** The major and minor version of the Playwright instance that connects needs to match the version of
Playwright that launches the browser (1.2.3 → is compatible with 1.2.x).

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `endpoint` | str | A Playwright browser websocket endpoint to connect to. You obtain this endpoint via `BrowserServer.wsEndpoint`. |
| `expose_network` | Union[str, None] | This option exposes network available on the connecting client to the browser being connected to. Consists of a list of rules separated by comma.  Available rules: 1. Hostname pattern, for example: `example.com`, `*.org:99`, `x.*.y.com`, `*foo.org`. 1. IP literal, for example: `127.0.0.1`, `0.0.0.0:99`, `[::1]`, `[0:0::1]:99`. 1. `<loopback>` that matches local loopback interfaces: `localhost`, `*.localhost`, `127.0.0.1`, `[::1]`.  Some common examples: 1. `"*"` to expose all network. 1. `"<loopback>"` to expose localhost network. 1. `"*.test.internal-domain,*.staging.internal-domain,<loopback>"` to expose test/staging deployments and localhost. |
| `headers` | Union[Dict[str, str], None] | Additional HTTP headers to be sent with web socket connect request. Optional. |
| `slow_mo` | Union[float, None] | Slows down Playwright operations by the specified amount of milliseconds. Useful so that you can see what is going on. Defaults to 0. |
| `timeout` | Union[float, None] | Maximum time in milliseconds to wait for the connection to be established. Defaults to `0` (no timeout). |

#### Returns
Browser


## connect_over_cdp

### 同步

```python signature
def connect_over_cdp(self, endpoint_url: str, *, artifacts_dir: Union[pathlib.Path, str, NoneType] = None, headers: Optional[Dict[str, str]] = None, is_local: Optional[bool] = None, no_defaults: Optional[bool] = None, slow_mo: Optional[float] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'Browser'
```

BrowserType.connect_over_cdp

This method attaches Playwright to an existing browser instance using the Chrome DevTools Protocol.

The default browser context is accessible via `browser.contexts`.

**NOTE** Connecting over the Chrome DevTools Protocol is only supported for Chromium-based browsers.

**NOTE** This connection is significantly lower fidelity than the Playwright protocol connection via
`browser_type.connect()`. If you are experiencing issues or attempting to use advanced functionality, you probably
want to use `browser_type.connect()`.

**NOTE** Playwright maintains a curated list of arguments for launching the browser. If you launch the browser
without Playwright and do not pass the exact same arguments, some of Playwright functionality may be broken upon
connecting to the browser.

**Usage**

```py
browser = playwright.chromium.connect_over_cdp("http://localhost:9222")
default_context = browser.contexts[0]
page = default_context.pages[0]
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `endpoint_url` | str | A CDP websocket endpoint or http url to connect to. For example `http://localhost:9222/` or `ws://127.0.0.1:9222/devtools/browser/387adf4c-243f-4051-a181-46798f4a46f4`. |
| `artifacts_dir` | Union[pathlib.Path, str, None] | If specified, browser artifacts (such as traces and downloads) are saved into this directory. |
| `headers` | Union[Dict[str, str], None] | Additional HTTP headers to be sent with connect request. Optional. |
| `is_local` | Union[bool, None] | Tells Playwright that it runs on the same host as the CDP server. It will enable certain optimizations that rely upon the file system being the same between Playwright and the Browser. |
| `no_defaults` | Union[bool, None] | When true, Playwright will not apply its default overrides to the existing default browser context. Specifically, `accept_downloads` is left at the browser's setting, focus emulation is not enabled, and media emulation options (such as `color_scheme`, `reduced_motion`, `forced_colors`, and `contrast`) are not applied. Useful when attaching to a user's daily-driver browser where these overrides would interfere with existing browser state. New contexts created via `browser.new_context()` are not affected. Defaults to `false`. |
| `slow_mo` | Union[float, None] | Slows down Playwright operations by the specified amount of milliseconds. Useful so that you can see what is going on. Defaults to 0. |
| `timeout` | Union[float, None] | Maximum time in milliseconds to wait for the connection to be established. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. |

#### Returns
Browser

### 异步

```python signature
async def connect_over_cdp(self, endpoint_url: str, *, artifacts_dir: Union[pathlib.Path, str, NoneType] = None, headers: Optional[Dict[str, str]] = None, is_local: Optional[bool] = None, no_defaults: Optional[bool] = None, slow_mo: Optional[float] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'Browser'
```

BrowserType.connect_over_cdp

This method attaches Playwright to an existing browser instance using the Chrome DevTools Protocol.

The default browser context is accessible via `browser.contexts`.

**NOTE** Connecting over the Chrome DevTools Protocol is only supported for Chromium-based browsers.

**NOTE** This connection is significantly lower fidelity than the Playwright protocol connection via
`browser_type.connect()`. If you are experiencing issues or attempting to use advanced functionality, you probably
want to use `browser_type.connect()`.

**NOTE** Playwright maintains a curated list of arguments for launching the browser. If you launch the browser
without Playwright and do not pass the exact same arguments, some of Playwright functionality may be broken upon
connecting to the browser.

**Usage**

```py
browser = await playwright.chromium.connect_over_cdp("http://localhost:9222")
default_context = browser.contexts[0]
page = default_context.pages[0]
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `endpoint_url` | str | A CDP websocket endpoint or http url to connect to. For example `http://localhost:9222/` or `ws://127.0.0.1:9222/devtools/browser/387adf4c-243f-4051-a181-46798f4a46f4`. |
| `artifacts_dir` | Union[pathlib.Path, str, None] | If specified, browser artifacts (such as traces and downloads) are saved into this directory. |
| `headers` | Union[Dict[str, str], None] | Additional HTTP headers to be sent with connect request. Optional. |
| `is_local` | Union[bool, None] | Tells Playwright that it runs on the same host as the CDP server. It will enable certain optimizations that rely upon the file system being the same between Playwright and the Browser. |
| `no_defaults` | Union[bool, None] | When true, Playwright will not apply its default overrides to the existing default browser context. Specifically, `accept_downloads` is left at the browser's setting, focus emulation is not enabled, and media emulation options (such as `color_scheme`, `reduced_motion`, `forced_colors`, and `contrast`) are not applied. Useful when attaching to a user's daily-driver browser where these overrides would interfere with existing browser state. New contexts created via `browser.new_context()` are not affected. Defaults to `false`. |
| `slow_mo` | Union[float, None] | Slows down Playwright operations by the specified amount of milliseconds. Useful so that you can see what is going on. Defaults to 0. |
| `timeout` | Union[float, None] | Maximum time in milliseconds to wait for the connection to be established. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. |

#### Returns
Browser


## executable_path

属性，直接读取；异步入口也不加 await。

```python signature
BrowserType.executable_path: <class 'str'>
```

BrowserType.executable_path

A path where Playwright expects to find a bundled browser executable.

#### Returns
str


## launch

### 同步

```python signature
def launch(self, *, args: Optional[Sequence[str]] = None, artifacts_dir: Union[pathlib.Path, str, NoneType] = None, channel: Optional[str] = None, chromium_sandbox: Optional[bool] = None, downloads_path: Union[pathlib.Path, str, NoneType] = None, env: Optional[Dict[str, Union[str, float, bool]]] = None, executable_path: Union[pathlib.Path, str, NoneType] = None, firefox_user_prefs: Optional[Dict[str, Union[str, float, bool]]] = None, handle_sighup: Optional[bool] = None, handle_sigint: Optional[bool] = None, handle_sigterm: Optional[bool] = None, headless: Optional[bool] = None, ignore_default_args: Union[bool, Sequence[str], NoneType] = None, proxy: Optional[patchright._impl._api_structures.ProxySettings] = None, slow_mo: Optional[float] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, traces_dir: Union[pathlib.Path, str, NoneType] = None) -> 'Browser'
```

BrowserType.launch

Returns the browser instance.

**Usage**

You can use `ignore_default_args` to filter out `--mute-audio` from default arguments:

```py
browser = playwright.chromium.launch( # or "firefox" or "webkit".
    ignore_default_args=["--mute-audio"]
)
```

> **Chromium-only** Playwright can also be used to control the Google Chrome or Microsoft Edge browsers, but it
works best with the version of Chromium it is bundled with. There is no guarantee it will work with any other
version. Use `executable_path` option with extreme caution.
>
> If Google Chrome (rather than Chromium) is preferred, a
[Chrome Canary](https://www.google.com/chrome/browser/canary.html) or
[Dev Channel](https://www.chromium.org/getting-involved/dev-channel) build is suggested.
>
> Stock browsers like Google Chrome and Microsoft Edge are suitable for tests that require proprietary media codecs
for video playback. See
[this article](https://www.howtogeek.com/202825/what%E2%80%99s-the-difference-between-chromium-and-chrome/) for
other differences between Chromium and Chrome.
[This article](https://chromium.googlesource.com/chromium/src/+/lkgr/docs/chromium_browser_vs_google_chrome.md)
describes some differences for Linux users.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `args` | Union[Sequence[str], None] | **NOTE** Use custom browser args at your own risk, as some of them may break Playwright functionality.  Additional arguments to pass to the browser instance. The list of Chromium flags can be found [here](https://peter.sh/experiments/chromium-command-line-switches/). |
| `artifacts_dir` | Union[pathlib.Path, str, None] | If specified, artifacts (traces, videos, downloads, HAR files, etc.) are saved into this directory. The directory is not cleaned up when the browser closes. If not specified, a temporary directory is used and cleaned up when the browser closes. |
| `channel` | Union[str, None] | Browser distribution channel.  Use "chromium" to opt in to new headless mode.  Use "chrome", "chrome-beta", "chrome-dev", "chrome-canary", "msedge", "msedge-beta", "msedge-dev", or "msedge-canary" to use branded Google Chrome and Microsoft Edge. |
| `chromium_sandbox` | Union[bool, None] | Enable Chromium sandboxing. Defaults to `false`. |
| `downloads_path` | Union[pathlib.Path, str, None] | If specified, accepted downloads are downloaded into this directory. Otherwise, temporary directory is created and is deleted when browser is closed. In either case, the downloads are deleted when the browser context they were created in is closed. |
| `env` | Union[Dict[str, Union[bool, float, str]], None] | Specify environment variables that will be visible to the browser. Defaults to `process.env`. |
| `executable_path` | Union[pathlib.Path, str, None] | Path to a browser executable to run instead of the bundled one. If `executable_path` is a relative path, then it is resolved relative to the current working directory. Note that Playwright only works with the bundled Chromium, Firefox or WebKit, use at your own risk. |
| `firefox_user_prefs` | Union[Dict[str, Union[bool, float, str]], None] | Firefox user preferences. Learn more about the Firefox user preferences at [`about:config`](https://support.mozilla.org/en-US/kb/about-config-editor-firefox).  You can also provide a path to a custom [`policies.json` file](https://mozilla.github.io/policy-templates/) via `PLAYWRIGHT_FIREFOX_POLICIES_JSON` environment variable. |
| `handle_sighup` | Union[bool, None] | Close the browser process on SIGHUP. Defaults to `true`. |
| `handle_sigint` | Union[bool, None] | Close the browser process on Ctrl-C. Defaults to `true`. |
| `handle_sigterm` | Union[bool, None] | Close the browser process on SIGTERM. Defaults to `true`. |
| `headless` | Union[bool, None] | Whether to run browser in headless mode. More details for [Chromium](https://developers.google.com/web/updates/2017/04/headless-chrome) and [Firefox](https://hacks.mozilla.org/2017/12/using-headless-mode-in-firefox/). Defaults to `true`. |
| `ignore_default_args` | Union[Sequence[str], bool, None] | If `true`, Playwright does not pass its own configurations args and only uses the ones from `args`. If an array is given, then filters out the given default arguments. Dangerous option; use with care. Defaults to `false`. |
| `proxy` | Union[{server: str, bypass: Union[str, None], username: Union[str, None], password: Union[str, None]}, None] | Network proxy settings. |
| `slow_mo` | Union[float, None] | Slows down Playwright operations by the specified amount of milliseconds. Useful so that you can see what is going on. |
| `timeout` | Union[float, None] | Maximum time in milliseconds to wait for the browser instance to start. Defaults to `180000` (3 minutes). Pass `0` to disable timeout. |
| `traces_dir` | Union[pathlib.Path, str, None] | If specified, traces are saved into this directory. |

#### Returns
Browser

### 异步

```python signature
async def launch(self, *, args: Optional[Sequence[str]] = None, artifacts_dir: Union[pathlib.Path, str, NoneType] = None, channel: Optional[str] = None, chromium_sandbox: Optional[bool] = None, downloads_path: Union[pathlib.Path, str, NoneType] = None, env: Optional[Dict[str, Union[str, float, bool]]] = None, executable_path: Union[pathlib.Path, str, NoneType] = None, firefox_user_prefs: Optional[Dict[str, Union[str, float, bool]]] = None, handle_sighup: Optional[bool] = None, handle_sigint: Optional[bool] = None, handle_sigterm: Optional[bool] = None, headless: Optional[bool] = None, ignore_default_args: Union[bool, Sequence[str], NoneType] = None, proxy: Optional[patchright._impl._api_structures.ProxySettings] = None, slow_mo: Optional[float] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, traces_dir: Union[pathlib.Path, str, NoneType] = None) -> 'Browser'
```

BrowserType.launch

Returns the browser instance.

**Usage**

You can use `ignore_default_args` to filter out `--mute-audio` from default arguments:

```py
browser = await playwright.chromium.launch( # or "firefox" or "webkit".
    ignore_default_args=["--mute-audio"]
)
```

> **Chromium-only** Playwright can also be used to control the Google Chrome or Microsoft Edge browsers, but it
works best with the version of Chromium it is bundled with. There is no guarantee it will work with any other
version. Use `executable_path` option with extreme caution.
>
> If Google Chrome (rather than Chromium) is preferred, a
[Chrome Canary](https://www.google.com/chrome/browser/canary.html) or
[Dev Channel](https://www.chromium.org/getting-involved/dev-channel) build is suggested.
>
> Stock browsers like Google Chrome and Microsoft Edge are suitable for tests that require proprietary media codecs
for video playback. See
[this article](https://www.howtogeek.com/202825/what%E2%80%99s-the-difference-between-chromium-and-chrome/) for
other differences between Chromium and Chrome.
[This article](https://chromium.googlesource.com/chromium/src/+/lkgr/docs/chromium_browser_vs_google_chrome.md)
describes some differences for Linux users.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `args` | Union[Sequence[str], None] | **NOTE** Use custom browser args at your own risk, as some of them may break Playwright functionality.  Additional arguments to pass to the browser instance. The list of Chromium flags can be found [here](https://peter.sh/experiments/chromium-command-line-switches/). |
| `artifacts_dir` | Union[pathlib.Path, str, None] | If specified, artifacts (traces, videos, downloads, HAR files, etc.) are saved into this directory. The directory is not cleaned up when the browser closes. If not specified, a temporary directory is used and cleaned up when the browser closes. |
| `channel` | Union[str, None] | Browser distribution channel.  Use "chromium" to opt in to new headless mode.  Use "chrome", "chrome-beta", "chrome-dev", "chrome-canary", "msedge", "msedge-beta", "msedge-dev", or "msedge-canary" to use branded Google Chrome and Microsoft Edge. |
| `chromium_sandbox` | Union[bool, None] | Enable Chromium sandboxing. Defaults to `false`. |
| `downloads_path` | Union[pathlib.Path, str, None] | If specified, accepted downloads are downloaded into this directory. Otherwise, temporary directory is created and is deleted when browser is closed. In either case, the downloads are deleted when the browser context they were created in is closed. |
| `env` | Union[Dict[str, Union[bool, float, str]], None] | Specify environment variables that will be visible to the browser. Defaults to `process.env`. |
| `executable_path` | Union[pathlib.Path, str, None] | Path to a browser executable to run instead of the bundled one. If `executable_path` is a relative path, then it is resolved relative to the current working directory. Note that Playwright only works with the bundled Chromium, Firefox or WebKit, use at your own risk. |
| `firefox_user_prefs` | Union[Dict[str, Union[bool, float, str]], None] | Firefox user preferences. Learn more about the Firefox user preferences at [`about:config`](https://support.mozilla.org/en-US/kb/about-config-editor-firefox).  You can also provide a path to a custom [`policies.json` file](https://mozilla.github.io/policy-templates/) via `PLAYWRIGHT_FIREFOX_POLICIES_JSON` environment variable. |
| `handle_sighup` | Union[bool, None] | Close the browser process on SIGHUP. Defaults to `true`. |
| `handle_sigint` | Union[bool, None] | Close the browser process on Ctrl-C. Defaults to `true`. |
| `handle_sigterm` | Union[bool, None] | Close the browser process on SIGTERM. Defaults to `true`. |
| `headless` | Union[bool, None] | Whether to run browser in headless mode. More details for [Chromium](https://developers.google.com/web/updates/2017/04/headless-chrome) and [Firefox](https://hacks.mozilla.org/2017/12/using-headless-mode-in-firefox/). Defaults to `true`. |
| `ignore_default_args` | Union[Sequence[str], bool, None] | If `true`, Playwright does not pass its own configurations args and only uses the ones from `args`. If an array is given, then filters out the given default arguments. Dangerous option; use with care. Defaults to `false`. |
| `proxy` | Union[{server: str, bypass: Union[str, None], username: Union[str, None], password: Union[str, None]}, None] | Network proxy settings. |
| `slow_mo` | Union[float, None] | Slows down Playwright operations by the specified amount of milliseconds. Useful so that you can see what is going on. |
| `timeout` | Union[float, None] | Maximum time in milliseconds to wait for the browser instance to start. Defaults to `180000` (3 minutes). Pass `0` to disable timeout. |
| `traces_dir` | Union[pathlib.Path, str, None] | If specified, traces are saved into this directory. |

#### Returns
Browser


## launch_persistent_context

### 同步

```python signature
def launch_persistent_context(self, user_data_dir: Union[str, pathlib.Path], *, accept_downloads: Optional[bool] = None, args: Optional[Sequence[str]] = None, artifacts_dir: Union[pathlib.Path, str, NoneType] = None, base_url: Optional[str] = None, bypass_csp: Optional[bool] = None, channel: Optional[str] = None, chromium_sandbox: Optional[bool] = None, client_certificates: Optional[Sequence[patchright._impl._api_structures.ClientCertificate]] = None, color_scheme: Optional[Literal['dark', 'light', 'no-preference', 'null']] = None, contrast: Optional[Literal['more', 'no-preference', 'null']] = None, device_scale_factor: Optional[float] = None, downloads_path: Union[pathlib.Path, str, NoneType] = None, env: Optional[Dict[str, Union[str, float, bool]]] = None, executable_path: Union[pathlib.Path, str, NoneType] = None, extra_http_headers: Optional[Dict[str, str]] = None, firefox_user_prefs: Optional[Dict[str, Union[str, float, bool]]] = None, forced_colors: Optional[Literal['active', 'none', 'null']] = None, geolocation: Optional[patchright._impl._api_structures.Geolocation] = None, handle_sighup: Optional[bool] = None, handle_sigint: Optional[bool] = None, handle_sigterm: Optional[bool] = None, has_touch: Optional[bool] = None, headless: Optional[bool] = None, http_credentials: Union[patchright._impl._api_structures.HttpCredentials, Sequence[patchright._impl._api_structures.HttpCredentials], NoneType] = None, ignore_default_args: Union[bool, Sequence[str], NoneType] = None, ignore_https_errors: Optional[bool] = None, is_mobile: Optional[bool] = None, java_script_enabled: Optional[bool] = None, locale: Optional[str] = None, no_viewport: Optional[bool] = None, offline: Optional[bool] = None, permissions: Optional[Sequence[str]] = None, proxy: Optional[patchright._impl._api_structures.ProxySettings] = None, record_har_content: Optional[Literal['attach', 'embed', 'omit']] = None, record_har_mode: Optional[Literal['full', 'minimal']] = None, record_har_omit_content: Optional[bool] = None, record_har_path: Union[pathlib.Path, str, NoneType] = None, record_har_url_filter: Union[str, Pattern[str], NoneType] = None, record_video_dir: Union[pathlib.Path, str, NoneType] = None, record_video_fps: Optional[int] = None, record_video_size: Optional[patchright._impl._api_structures.ViewportSize] = None, reduced_motion: Optional[Literal['no-preference', 'null', 'reduce']] = None, screen: Optional[patchright._impl._api_structures.ViewportSize] = None, service_workers: Optional[Literal['allow', 'block']] = None, slow_mo: Optional[float] = None, strict_selectors: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, timezone_id: Optional[str] = None, traces_dir: Union[pathlib.Path, str, NoneType] = None, user_agent: Optional[str] = None, viewport: Optional[patchright._impl._api_structures.ViewportSize] = None, focus_control: Optional[bool] = None) -> 'BrowserContext'
```

BrowserType.launch_persistent_context

Returns the persistent browser context instance.

Launches browser that uses persistent storage located at `user_data_dir` and returns the only context. Closing this
context will automatically close the browser.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `user_data_dir` | Union[pathlib.Path, str] | Path to a User Data Directory, which stores browser session data like cookies and local storage. Pass an empty string to create a temporary directory.  More details for [Chromium](https://chromium.googlesource.com/chromium/src/+/master/docs/user_data_dir.md#introduction) and [Firefox](https://wiki.mozilla.org/Firefox/CommandLineOptions#User_profile). Chromium's user data directory is the **parent** directory of the "Profile Path" seen at `chrome://version`.  Note that browsers do not allow launching multiple instances with the same User Data Directory.  **NOTE** Chromium/Chrome: Due to recent Chrome policy changes, automating the default Chrome user profile is not supported. Pointing `userDataDir` to Chrome's main "User Data" directory (the profile used for your regular browsing) may result in pages not loading or the browser exiting. Create and use a separate directory (for example, an empty folder) as your automation profile instead. See https://developer.chrome.com/blog/remote-debugging-port for details. |
| `accept_downloads` | Union[bool, None] | Whether to automatically download all the attachments. Defaults to `true` where all the downloads are accepted. |
| `args` | Union[Sequence[str], None] | **NOTE** Use custom browser args at your own risk, as some of them may break Playwright functionality.  Additional arguments to pass to the browser instance. The list of Chromium flags can be found [here](https://peter.sh/experiments/chromium-command-line-switches/). |
| `artifacts_dir` | Union[pathlib.Path, str, None] | If specified, artifacts (traces, videos, downloads, HAR files, etc.) are saved into this directory. The directory is not cleaned up when the browser closes. If not specified, a temporary directory is used and cleaned up when the browser closes. |
| `base_url` | Union[str, None] | When using `page.goto()`, `page.route()`, `page.wait_for_url()`, `page.expect_request()`, or `page.expect_response()` it takes the base URL in consideration by using the [`URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) constructor for building the corresponding URL. Unset by default. Examples: - baseURL: `http://localhost:3000` and navigating to `/bar.html` results in `http://localhost:3000/bar.html` - baseURL: `http://localhost:3000/foo/` and navigating to `./bar.html` results in `http://localhost:3000/foo/bar.html` - baseURL: `http://localhost:3000/foo` (without trailing slash) and navigating to `./bar.html` results in `http://localhost:3000/bar.html` |
| `bypass_csp` | Union[bool, None] | Toggles bypassing page's Content-Security-Policy. Defaults to `false`. |
| `channel` | Union[str, None] | Browser distribution channel.  Use "chromium" to opt in to new headless mode.  Use "chrome", "chrome-beta", "chrome-dev", "chrome-canary", "msedge", "msedge-beta", "msedge-dev", or "msedge-canary" to use branded Google Chrome and Microsoft Edge. |
| `chromium_sandbox` | Union[bool, None] | Enable Chromium sandboxing. Defaults to `false`. |
| `client_certificates` | Union[Sequence[{origin: str, certPath: Union[pathlib.Path, str, None], cert: Union[bytes, None], keyPath: Union[pathlib.Path, str, None], key: Union[bytes, None], pfxPath: Union[pathlib.Path, str, None], pfx: Union[bytes, None], passphrase: Union[str, None]}], None] | TLS Client Authentication allows the server to request a client certificate and verify it.  **Details**  An array of client certificates to be used. Each certificate object must have either both `certPath` and `keyPath`, a single `pfxPath`, or their corresponding direct value equivalents (`cert` and `key`, or `pfx`). Optionally, `passphrase` property should be provided if the certificate is encrypted. The `origin` property should be provided with an exact match to the request origin that the certificate is valid for.  Client certificate authentication is only active when at least one client certificate is provided. If you want to reject all client certificates sent by the server, you need to provide a client certificate with an `origin` that does not match any of the domains you plan to visit.  **NOTE** When using WebKit on macOS, accessing `localhost` will not pick up client certificates. You can make it work by replacing `localhost` with `local.playwright`. |
| `color_scheme` | Union["dark", "light", "no-preference", "null", None] | Emulates [prefers-colors-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) media feature, supported values are `'light'` and `'dark'`. See `page.emulate_media()` for more details. Passing `'null'` resets emulation to system defaults. Defaults to `'light'`. |
| `contrast` | Union["more", "no-preference", "null", None] | Emulates `'prefers-contrast'` media feature, supported values are `'no-preference'`, `'more'`. See `page.emulate_media()` for more details. Passing `'null'` resets emulation to system defaults. Defaults to `'no-preference'`. |
| `device_scale_factor` | Union[float, None] | Specify device scale factor (can be thought of as dpr). Defaults to `1`. Learn more about emulating devices with device scale factor. |
| `downloads_path` | Union[pathlib.Path, str, None] | If specified, accepted downloads are downloaded into this directory. Otherwise, temporary directory is created and is deleted when browser is closed. In either case, the downloads are deleted when the browser context they were created in is closed. |
| `env` | Union[Dict[str, Union[bool, float, str]], None] | Specify environment variables that will be visible to the browser. Defaults to `process.env`. |
| `executable_path` | Union[pathlib.Path, str, None] | Path to a browser executable to run instead of the bundled one. If `executable_path` is a relative path, then it is resolved relative to the current working directory. Note that Playwright only works with the bundled Chromium, Firefox or WebKit, use at your own risk. |
| `extra_http_headers` | Union[Dict[str, str], None] | An object containing additional HTTP headers to be sent with every request. Defaults to none. |
| `firefox_user_prefs` | Union[Dict[str, Union[bool, float, str]], None] | Firefox user preferences. Learn more about the Firefox user preferences at [`about:config`](https://support.mozilla.org/en-US/kb/about-config-editor-firefox).  You can also provide a path to a custom [`policies.json` file](https://mozilla.github.io/policy-templates/) via `PLAYWRIGHT_FIREFOX_POLICIES_JSON` environment variable. |
| `forced_colors` | Union["active", "none", "null", None] | Emulates `'forced-colors'` media feature, supported values are `'active'`, `'none'`. See `page.emulate_media()` for more details. Passing `'null'` resets emulation to system defaults. Defaults to `'none'`. |
| `geolocation` | Union[{latitude: float, longitude: float, accuracy: Union[float, None]}, None] |  |
| `handle_sighup` | Union[bool, None] | Close the browser process on SIGHUP. Defaults to `true`. |
| `handle_sigint` | Union[bool, None] | Close the browser process on Ctrl-C. Defaults to `true`. |
| `handle_sigterm` | Union[bool, None] | Close the browser process on SIGTERM. Defaults to `true`. |
| `has_touch` | Union[bool, None] | Specifies if viewport supports touch events. Defaults to false. Learn more about mobile emulation. |
| `headless` | Union[bool, None] | Whether to run browser in headless mode. More details for [Chromium](https://developers.google.com/web/updates/2017/04/headless-chrome) and [Firefox](https://hacks.mozilla.org/2017/12/using-headless-mode-in-firefox/). Defaults to `true`. |
| `http_credentials` | Union[Sequence[{username: str, password: str, origin: Union[str, None], send: Union["always", "unauthorized", None]}], {username: str, password: str, origin: Union[str, None], send: Union["always", "unauthorized", None]}, None] | Credentials for [HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication). If no origin is specified, the username and password are sent to any servers upon unauthorized responses.  Pass an array to use different credentials for different origins. The first entry that matches the request origin is used, and entries with no origin match any request. |
| `ignore_default_args` | Union[Sequence[str], bool, None] | If `true`, Playwright does not pass its own configurations args and only uses the ones from `args`. If an array is given, then filters out the given default arguments. Dangerous option; use with care. Defaults to `false`. |
| `ignore_https_errors` | Union[bool, None] | Whether to ignore HTTPS errors when sending network requests. Defaults to `false`. |
| `is_mobile` | Union[bool, None] | Whether the `meta viewport` tag is taken into account and touch events are enabled. isMobile is a part of device, so you don't actually need to set it manually. Defaults to `false`. Learn more about mobile emulation. |
| `java_script_enabled` | Union[bool, None] | Whether or not to enable JavaScript in the context. Defaults to `true`. Learn more about disabling JavaScript. |
| `locale` | Union[str, None] | Specify user locale, for example `en-GB`, `de-DE`, etc. Locale will affect `navigator.language` value, `Accept-Language` request header value as well as number and date formatting rules. Defaults to the system default locale. Learn more about emulation in our emulation guide. |
| `no_viewport` | Union[bool, None] | Does not enforce fixed viewport, allows resizing window in the headed mode. |
| `offline` | Union[bool, None] | Whether to emulate network being offline. Defaults to `false`. Learn more about network emulation. |
| `permissions` | Union[Sequence[str], None] | A list of permissions to grant to all pages in this context. See `browser_context.grant_permissions()` for more details. Defaults to none. |
| `proxy` | Union[{server: str, bypass: Union[str, None], username: Union[str, None], password: Union[str, None]}, None] | Network proxy settings. |
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
| `slow_mo` | Union[float, None] | Slows down Playwright operations by the specified amount of milliseconds. Useful so that you can see what is going on. |
| `strict_selectors` | Union[bool, None] | If set to true, enables strict selectors mode for this context. In the strict selectors mode all operations on selectors that imply single target DOM element will throw when more than one element matches the selector. This option does not affect any Locator APIs (Locators are always strict). Defaults to `false`. See `Locator` to learn more about the strict mode. |
| `timeout` | Union[float, None] | Maximum time in milliseconds to wait for the browser instance to start. Defaults to `180000` (3 minutes). Pass `0` to disable timeout. |
| `timezone_id` | Union[str, None] | Changes the timezone of the context. See [ICU's metaZones.txt](https://cs.chromium.org/chromium/src/third_party/icu/source/data/misc/metaZones.txt?rcl=faee8bc70570192d82d2978a71e2a615788597d1) for a list of supported timezone IDs. Defaults to the system timezone. |
| `traces_dir` | Union[pathlib.Path, str, None] | If specified, traces are saved into this directory. |
| `user_agent` | Union[str, None] | Specific user agent to use in this context. |
| `viewport` | Union[{width: int, height: int}, None] | Sets a consistent viewport for each page. Defaults to an 1280x720 viewport. `no_viewport` disables the fixed viewport. Learn more about viewport emulation. |

#### Returns
BrowserContext

### 异步

```python signature
async def launch_persistent_context(self, user_data_dir: Union[str, pathlib.Path], *, accept_downloads: Optional[bool] = None, args: Optional[Sequence[str]] = None, artifacts_dir: Union[pathlib.Path, str, NoneType] = None, base_url: Optional[str] = None, bypass_csp: Optional[bool] = None, channel: Optional[str] = None, chromium_sandbox: Optional[bool] = None, client_certificates: Optional[Sequence[patchright._impl._api_structures.ClientCertificate]] = None, color_scheme: Optional[Literal['dark', 'light', 'no-preference', 'null']] = None, contrast: Optional[Literal['more', 'no-preference', 'null']] = None, device_scale_factor: Optional[float] = None, downloads_path: Union[pathlib.Path, str, NoneType] = None, env: Optional[Dict[str, Union[str, float, bool]]] = None, executable_path: Union[pathlib.Path, str, NoneType] = None, extra_http_headers: Optional[Dict[str, str]] = None, firefox_user_prefs: Optional[Dict[str, Union[str, float, bool]]] = None, forced_colors: Optional[Literal['active', 'none', 'null']] = None, geolocation: Optional[patchright._impl._api_structures.Geolocation] = None, handle_sighup: Optional[bool] = None, handle_sigint: Optional[bool] = None, handle_sigterm: Optional[bool] = None, has_touch: Optional[bool] = None, headless: Optional[bool] = None, http_credentials: Union[patchright._impl._api_structures.HttpCredentials, Sequence[patchright._impl._api_structures.HttpCredentials], NoneType] = None, ignore_default_args: Union[bool, Sequence[str], NoneType] = None, ignore_https_errors: Optional[bool] = None, is_mobile: Optional[bool] = None, java_script_enabled: Optional[bool] = None, locale: Optional[str] = None, no_viewport: Optional[bool] = None, offline: Optional[bool] = None, permissions: Optional[Sequence[str]] = None, proxy: Optional[patchright._impl._api_structures.ProxySettings] = None, record_har_content: Optional[Literal['attach', 'embed', 'omit']] = None, record_har_mode: Optional[Literal['full', 'minimal']] = None, record_har_omit_content: Optional[bool] = None, record_har_path: Union[pathlib.Path, str, NoneType] = None, record_har_url_filter: Union[str, Pattern[str], NoneType] = None, record_video_dir: Union[pathlib.Path, str, NoneType] = None, record_video_fps: Optional[int] = None, record_video_size: Optional[patchright._impl._api_structures.ViewportSize] = None, reduced_motion: Optional[Literal['no-preference', 'null', 'reduce']] = None, screen: Optional[patchright._impl._api_structures.ViewportSize] = None, service_workers: Optional[Literal['allow', 'block']] = None, slow_mo: Optional[float] = None, strict_selectors: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, timezone_id: Optional[str] = None, traces_dir: Union[pathlib.Path, str, NoneType] = None, user_agent: Optional[str] = None, viewport: Optional[patchright._impl._api_structures.ViewportSize] = None, focus_control: Optional[bool] = None) -> 'BrowserContext'
```

BrowserType.launch_persistent_context

Returns the persistent browser context instance.

Launches browser that uses persistent storage located at `user_data_dir` and returns the only context. Closing this
context will automatically close the browser.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `user_data_dir` | Union[pathlib.Path, str] | Path to a User Data Directory, which stores browser session data like cookies and local storage. Pass an empty string to create a temporary directory.  More details for [Chromium](https://chromium.googlesource.com/chromium/src/+/master/docs/user_data_dir.md#introduction) and [Firefox](https://wiki.mozilla.org/Firefox/CommandLineOptions#User_profile). Chromium's user data directory is the **parent** directory of the "Profile Path" seen at `chrome://version`.  Note that browsers do not allow launching multiple instances with the same User Data Directory.  **NOTE** Chromium/Chrome: Due to recent Chrome policy changes, automating the default Chrome user profile is not supported. Pointing `userDataDir` to Chrome's main "User Data" directory (the profile used for your regular browsing) may result in pages not loading or the browser exiting. Create and use a separate directory (for example, an empty folder) as your automation profile instead. See https://developer.chrome.com/blog/remote-debugging-port for details. |
| `accept_downloads` | Union[bool, None] | Whether to automatically download all the attachments. Defaults to `true` where all the downloads are accepted. |
| `args` | Union[Sequence[str], None] | **NOTE** Use custom browser args at your own risk, as some of them may break Playwright functionality.  Additional arguments to pass to the browser instance. The list of Chromium flags can be found [here](https://peter.sh/experiments/chromium-command-line-switches/). |
| `artifacts_dir` | Union[pathlib.Path, str, None] | If specified, artifacts (traces, videos, downloads, HAR files, etc.) are saved into this directory. The directory is not cleaned up when the browser closes. If not specified, a temporary directory is used and cleaned up when the browser closes. |
| `base_url` | Union[str, None] | When using `page.goto()`, `page.route()`, `page.wait_for_url()`, `page.expect_request()`, or `page.expect_response()` it takes the base URL in consideration by using the [`URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) constructor for building the corresponding URL. Unset by default. Examples: - baseURL: `http://localhost:3000` and navigating to `/bar.html` results in `http://localhost:3000/bar.html` - baseURL: `http://localhost:3000/foo/` and navigating to `./bar.html` results in `http://localhost:3000/foo/bar.html` - baseURL: `http://localhost:3000/foo` (without trailing slash) and navigating to `./bar.html` results in `http://localhost:3000/bar.html` |
| `bypass_csp` | Union[bool, None] | Toggles bypassing page's Content-Security-Policy. Defaults to `false`. |
| `channel` | Union[str, None] | Browser distribution channel.  Use "chromium" to opt in to new headless mode.  Use "chrome", "chrome-beta", "chrome-dev", "chrome-canary", "msedge", "msedge-beta", "msedge-dev", or "msedge-canary" to use branded Google Chrome and Microsoft Edge. |
| `chromium_sandbox` | Union[bool, None] | Enable Chromium sandboxing. Defaults to `false`. |
| `client_certificates` | Union[Sequence[{origin: str, certPath: Union[pathlib.Path, str, None], cert: Union[bytes, None], keyPath: Union[pathlib.Path, str, None], key: Union[bytes, None], pfxPath: Union[pathlib.Path, str, None], pfx: Union[bytes, None], passphrase: Union[str, None]}], None] | TLS Client Authentication allows the server to request a client certificate and verify it.  **Details**  An array of client certificates to be used. Each certificate object must have either both `certPath` and `keyPath`, a single `pfxPath`, or their corresponding direct value equivalents (`cert` and `key`, or `pfx`). Optionally, `passphrase` property should be provided if the certificate is encrypted. The `origin` property should be provided with an exact match to the request origin that the certificate is valid for.  Client certificate authentication is only active when at least one client certificate is provided. If you want to reject all client certificates sent by the server, you need to provide a client certificate with an `origin` that does not match any of the domains you plan to visit.  **NOTE** When using WebKit on macOS, accessing `localhost` will not pick up client certificates. You can make it work by replacing `localhost` with `local.playwright`. |
| `color_scheme` | Union["dark", "light", "no-preference", "null", None] | Emulates [prefers-colors-scheme](https://developer.mozilla.org/en-US/docs/Web/CSS/@media/prefers-color-scheme) media feature, supported values are `'light'` and `'dark'`. See `page.emulate_media()` for more details. Passing `'null'` resets emulation to system defaults. Defaults to `'light'`. |
| `contrast` | Union["more", "no-preference", "null", None] | Emulates `'prefers-contrast'` media feature, supported values are `'no-preference'`, `'more'`. See `page.emulate_media()` for more details. Passing `'null'` resets emulation to system defaults. Defaults to `'no-preference'`. |
| `device_scale_factor` | Union[float, None] | Specify device scale factor (can be thought of as dpr). Defaults to `1`. Learn more about emulating devices with device scale factor. |
| `downloads_path` | Union[pathlib.Path, str, None] | If specified, accepted downloads are downloaded into this directory. Otherwise, temporary directory is created and is deleted when browser is closed. In either case, the downloads are deleted when the browser context they were created in is closed. |
| `env` | Union[Dict[str, Union[bool, float, str]], None] | Specify environment variables that will be visible to the browser. Defaults to `process.env`. |
| `executable_path` | Union[pathlib.Path, str, None] | Path to a browser executable to run instead of the bundled one. If `executable_path` is a relative path, then it is resolved relative to the current working directory. Note that Playwright only works with the bundled Chromium, Firefox or WebKit, use at your own risk. |
| `extra_http_headers` | Union[Dict[str, str], None] | An object containing additional HTTP headers to be sent with every request. Defaults to none. |
| `firefox_user_prefs` | Union[Dict[str, Union[bool, float, str]], None] | Firefox user preferences. Learn more about the Firefox user preferences at [`about:config`](https://support.mozilla.org/en-US/kb/about-config-editor-firefox).  You can also provide a path to a custom [`policies.json` file](https://mozilla.github.io/policy-templates/) via `PLAYWRIGHT_FIREFOX_POLICIES_JSON` environment variable. |
| `forced_colors` | Union["active", "none", "null", None] | Emulates `'forced-colors'` media feature, supported values are `'active'`, `'none'`. See `page.emulate_media()` for more details. Passing `'null'` resets emulation to system defaults. Defaults to `'none'`. |
| `geolocation` | Union[{latitude: float, longitude: float, accuracy: Union[float, None]}, None] |  |
| `handle_sighup` | Union[bool, None] | Close the browser process on SIGHUP. Defaults to `true`. |
| `handle_sigint` | Union[bool, None] | Close the browser process on Ctrl-C. Defaults to `true`. |
| `handle_sigterm` | Union[bool, None] | Close the browser process on SIGTERM. Defaults to `true`. |
| `has_touch` | Union[bool, None] | Specifies if viewport supports touch events. Defaults to false. Learn more about mobile emulation. |
| `headless` | Union[bool, None] | Whether to run browser in headless mode. More details for [Chromium](https://developers.google.com/web/updates/2017/04/headless-chrome) and [Firefox](https://hacks.mozilla.org/2017/12/using-headless-mode-in-firefox/). Defaults to `true`. |
| `http_credentials` | Union[Sequence[{username: str, password: str, origin: Union[str, None], send: Union["always", "unauthorized", None]}], {username: str, password: str, origin: Union[str, None], send: Union["always", "unauthorized", None]}, None] | Credentials for [HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication). If no origin is specified, the username and password are sent to any servers upon unauthorized responses.  Pass an array to use different credentials for different origins. The first entry that matches the request origin is used, and entries with no origin match any request. |
| `ignore_default_args` | Union[Sequence[str], bool, None] | If `true`, Playwright does not pass its own configurations args and only uses the ones from `args`. If an array is given, then filters out the given default arguments. Dangerous option; use with care. Defaults to `false`. |
| `ignore_https_errors` | Union[bool, None] | Whether to ignore HTTPS errors when sending network requests. Defaults to `false`. |
| `is_mobile` | Union[bool, None] | Whether the `meta viewport` tag is taken into account and touch events are enabled. isMobile is a part of device, so you don't actually need to set it manually. Defaults to `false`. Learn more about mobile emulation. |
| `java_script_enabled` | Union[bool, None] | Whether or not to enable JavaScript in the context. Defaults to `true`. Learn more about disabling JavaScript. |
| `locale` | Union[str, None] | Specify user locale, for example `en-GB`, `de-DE`, etc. Locale will affect `navigator.language` value, `Accept-Language` request header value as well as number and date formatting rules. Defaults to the system default locale. Learn more about emulation in our emulation guide. |
| `no_viewport` | Union[bool, None] | Does not enforce fixed viewport, allows resizing window in the headed mode. |
| `offline` | Union[bool, None] | Whether to emulate network being offline. Defaults to `false`. Learn more about network emulation. |
| `permissions` | Union[Sequence[str], None] | A list of permissions to grant to all pages in this context. See `browser_context.grant_permissions()` for more details. Defaults to none. |
| `proxy` | Union[{server: str, bypass: Union[str, None], username: Union[str, None], password: Union[str, None]}, None] | Network proxy settings. |
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
| `slow_mo` | Union[float, None] | Slows down Playwright operations by the specified amount of milliseconds. Useful so that you can see what is going on. |
| `strict_selectors` | Union[bool, None] | If set to true, enables strict selectors mode for this context. In the strict selectors mode all operations on selectors that imply single target DOM element will throw when more than one element matches the selector. This option does not affect any Locator APIs (Locators are always strict). Defaults to `false`. See `Locator` to learn more about the strict mode. |
| `timeout` | Union[float, None] | Maximum time in milliseconds to wait for the browser instance to start. Defaults to `180000` (3 minutes). Pass `0` to disable timeout. |
| `timezone_id` | Union[str, None] | Changes the timezone of the context. See [ICU's metaZones.txt](https://cs.chromium.org/chromium/src/third_party/icu/source/data/misc/metaZones.txt?rcl=faee8bc70570192d82d2978a71e2a615788597d1) for a list of supported timezone IDs. Defaults to the system timezone. |
| `traces_dir` | Union[pathlib.Path, str, None] | If specified, traces are saved into this directory. |
| `user_agent` | Union[str, None] | Specific user agent to use in this context. |
| `viewport` | Union[{width: int, height: int}, None] | Sets a consistent viewport for each page. Defaults to an 1280x720 viewport. `no_viewport` disables the fixed viewport. Learn more about viewport emulation. |

#### Returns
BrowserContext


## name

属性，直接读取；异步入口也不加 await。

```python signature
BrowserType.name: <class 'str'>
```

BrowserType.name

Returns browser name. For example: `'chromium'`, `'webkit'` or `'firefox'`.

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
