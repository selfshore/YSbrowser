# 原生 Playwright

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [chromium](#chromium)
- [devices](#devices)
- [firefox](#firefox)
- [on](#on)
- [once](#once)
- [remove_listener](#remove_listener)
- [request](#request)
- [selectors](#selectors)
- [stop](#stop)
- [webkit](#webkit)

## chromium

属性，直接读取；异步入口也不加 await。

```python signature
Playwright.chromium: BrowserType
```

Playwright.chromium

This object can be used to launch or connect to Chromium, returning instances of `Browser`.

#### Returns
BrowserType


## devices

属性，直接读取；异步入口也不加 await。

```python signature
Playwright.devices: typing.Dict
```

Playwright.devices

Returns a dictionary of devices to be used with `browser.new_context()` or `browser.new_page()`.

```py
from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    webkit = playwright.webkit
    iphone = playwright.devices["iPhone 6"]
    browser = webkit.launch()
    context = browser.new_context(**iphone)
    page = context.new_page()
    page.goto("http://example.com")
    # other actions...
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
```

#### Returns
Dict


## firefox

属性，直接读取；异步入口也不加 await。

```python signature
Playwright.firefox: BrowserType
```

Playwright.firefox

This object can be used to launch or connect to Firefox, returning instances of `Browser`.

#### Returns
BrowserType


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


## request

属性，直接读取；异步入口也不加 await。

```python signature
Playwright.request: APIRequest
```

Playwright.request

Exposes API that can be used for the Web API testing.

#### Returns
APIRequest


## selectors

属性，直接读取；异步入口也不加 await。

```python signature
Playwright.selectors: Selectors
```

Playwright.selectors

Selectors can be used to install custom selector engines. See [extensibility](https://playwright.dev/python/docs/extensibility) for more
information.

#### Returns
Selectors


## stop

### 同步

```python
def stop(self) -> None
```

Playwright.stop

Terminates this instance of Playwright in case it was created bypassing the Python context manager. This is useful
in REPL applications.

```py
from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()

browser = playwright.chromium.launch()
page = browser.new_page()
page.goto("https://playwright.dev/")
page.screenshot(path="example.png")
browser.close()

playwright.stop()
```

### 异步

```python
async def stop(self) -> None
```

Playwright.stop

Terminates this instance of Playwright in case it was created bypassing the Python context manager. This is useful
in REPL applications.

```py
from playwright.sync_api import sync_playwright

playwright = sync_playwright().start()

browser = playwright.chromium.launch()
page = browser.new_page()
page.goto("https://playwright.dev/")
page.screenshot(path="example.png")
browser.close()

playwright.stop()
```


## webkit

属性，直接读取；异步入口也不加 await。

```python signature
Playwright.webkit: BrowserType
```

Playwright.webkit

This object can be used to launch or connect to WebKit, returning instances of `Browser`.

#### Returns
BrowserType
