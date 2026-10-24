# 原生 Selectors

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [on](#on)
- [once](#once)
- [register](#register)
- [remove_listener](#remove_listener)
- [set_test_id_attribute](#set_test_id_attribute)

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


## register

### 同步

```python signature
def register(self, name: str, script: Optional[str] = None, *, content_script: Optional[bool] = None, path: Union[pathlib.Path, str, NoneType] = None) -> None
```

Selectors.register

Selectors must be registered before creating the page.

**Usage**

An example of registering selector engine that queries elements based on a tag name:

```py
from playwright.sync_api import sync_playwright, Playwright

def run(playwright: Playwright):
    tag_selector = """
      {
          // Returns the first element matching given selector in the root's subtree.
          query(root, selector) {
              return root.querySelector(selector);
          },
          // Returns all elements matching given selector in the root's subtree.
          queryAll(root, selector) {
              return Array.from(root.querySelectorAll(selector));
          }
      }"""

    # Register the engine. Selectors will be prefixed with "tag=".
    playwright.selectors.register("tag", tag_selector)
    browser = playwright.chromium.launch()
    page = browser.new_page()
    page.set_content('<div><button>Click me</button></div>')

    # Use the selector prefixed with its name.
    button = page.locator('tag=button')
    # Combine it with built-in locators.
    page.locator('tag=div').get_by_text('Click me').click()
    # Can use it in any methods supporting selectors.
    button_count = page.locator('tag=button').count()
    print(button_count)
    browser.close()

with sync_playwright() as playwright:
    run(playwright)
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | Name that is used in selectors as a prefix, e.g. `{name: 'foo'}` enables `foo=myselectorbody` selectors. May only contain `[a-zA-Z0-9_]` characters. |
| `script` | Union[str, None] | Raw script content. |
| `content_script` | Union[bool, None] | Whether to run this selector engine in isolated JavaScript environment. This environment has access to the same DOM, but not any JavaScript objects from the frame's scripts. Defaults to `false`. Note that running as a content script is not guaranteed when this engine is used together with other registered engines. |
| `path` | Union[pathlib.Path, str, None] | Path to the JavaScript file. If `path` is a relative path, then it is resolved relative to the current working directory. |

### 异步

```python signature
async def register(self, name: str, script: Optional[str] = None, *, content_script: Optional[bool] = None, path: Union[pathlib.Path, str, NoneType] = None) -> None
```

Selectors.register

Selectors must be registered before creating the page.

**Usage**

An example of registering selector engine that queries elements based on a tag name:

```py
import asyncio
from playwright.async_api import async_playwright, Playwright

async def run(playwright: Playwright):
    tag_selector = """
      {
          // Returns the first element matching given selector in the root's subtree.
          query(root, selector) {
              return root.querySelector(selector);
          },
          // Returns all elements matching given selector in the root's subtree.
          queryAll(root, selector) {
              return Array.from(root.querySelectorAll(selector));
          }
      }"""

    # Register the engine. Selectors will be prefixed with "tag=".
    await playwright.selectors.register("tag", tag_selector)
    browser = await playwright.chromium.launch()
    page = await browser.new_page()
    await page.set_content('<div><button>Click me</button></div>')

    # Use the selector prefixed with its name.
    button = await page.query_selector('tag=button')
    # Combine it with built-in locators.
    await page.locator('tag=div').get_by_text('Click me').click()
    # Can use it in any methods supporting selectors.
    button_count = await page.locator('tag=button').count()
    print(button_count)
    await browser.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | Name that is used in selectors as a prefix, e.g. `{name: 'foo'}` enables `foo=myselectorbody` selectors. May only contain `[a-zA-Z0-9_]` characters. |
| `script` | Union[str, None] | Raw script content. |
| `content_script` | Union[bool, None] | Whether to run this selector engine in isolated JavaScript environment. This environment has access to the same DOM, but not any JavaScript objects from the frame's scripts. Defaults to `false`. Note that running as a content script is not guaranteed when this engine is used together with other registered engines. |
| `path` | Union[pathlib.Path, str, None] | Path to the JavaScript file. If `path` is a relative path, then it is resolved relative to the current working directory. |

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


## set_test_id_attribute

### 同步

```python
def set_test_id_attribute(self, attribute_name: str) -> None
```

Selectors.set_test_id_attribute

Defines custom attribute name to be used in `page.get_by_test_id()`. `data-testid` is used by default.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `attribute_name` | str | Test id attribute name. To match elements with any of several attributes, pass them as a comma-separated list, e.g. `"data-pw,data-ti"`. |

### 异步

```python
def set_test_id_attribute(self, attribute_name: str) -> None
```

Selectors.set_test_id_attribute

Defines custom attribute name to be used in `page.get_by_test_id()`. `data-testid` is used by default.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `attribute_name` | str | Test id attribute name. To match elements with any of several attributes, pass them as a comma-separated list, e.g. `"data-pw,data-ti"`. |
