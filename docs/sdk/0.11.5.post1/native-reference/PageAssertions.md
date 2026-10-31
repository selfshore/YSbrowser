# 原生 PageAssertions

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [not_to_have_title](#not_to_have_title)
- [not_to_have_url](#not_to_have_url)
- [not_to_match_aria_snapshot](#not_to_match_aria_snapshot)
- [on](#on)
- [once](#once)
- [remove_listener](#remove_listener)
- [to_have_title](#to_have_title)
- [to_have_url](#to_have_url)
- [to_match_aria_snapshot](#to_match_aria_snapshot)

## not_to_have_title

### 同步

```python signature
def not_to_have_title(self, title_or_reg_exp: Union[str, Pattern[str]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

PageAssertions.not_to_have_title

The opposite of `page_assertions.to_have_title()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `title_or_reg_exp` | Union[Pattern[str], str] | Expected title or RegExp. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def not_to_have_title(self, title_or_reg_exp: Union[str, Pattern[str]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

PageAssertions.not_to_have_title

The opposite of `page_assertions.to_have_title()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `title_or_reg_exp` | Union[Pattern[str], str] | Expected title or RegExp. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## not_to_have_url

### 同步

```python signature
def not_to_have_url(self, url_or_reg_exp: Union[str, Pattern[str]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

PageAssertions.not_to_have_url

The opposite of `page_assertions.to_have_url()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url_or_reg_exp` | Union[Pattern[str], str] | Expected URL string or RegExp. |
| `ignore_case` | Union[bool, None] | Whether to perform case-insensitive match. `ignore_case` option takes precedence over the corresponding regular expression flag if specified. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def not_to_have_url(self, url_or_reg_exp: Union[str, Pattern[str]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

PageAssertions.not_to_have_url

The opposite of `page_assertions.to_have_url()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url_or_reg_exp` | Union[Pattern[str], str] | Expected URL string or RegExp. |
| `ignore_case` | Union[bool, None] | Whether to perform case-insensitive match. `ignore_case` option takes precedence over the corresponding regular expression flag if specified. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## not_to_match_aria_snapshot

### 同步

```python signature
def not_to_match_aria_snapshot(self, expected: str, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

PageAssertions.not_to_match_aria_snapshot

The opposite of `page_assertions.to_match_aria_snapshot()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expected` | str |  |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def not_to_match_aria_snapshot(self, expected: str, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

PageAssertions.not_to_match_aria_snapshot

The opposite of `page_assertions.to_match_aria_snapshot()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expected` | str |  |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

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


## to_have_title

### 同步

```python signature
def to_have_title(self, title_or_reg_exp: Union[str, Pattern[str]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

PageAssertions.to_have_title

Ensures the page has the given title.

**Usage**

```py
import re
from playwright.sync_api import expect

# ...
expect(page).to_have_title(re.compile(r".*checkout"))
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `title_or_reg_exp` | Union[Pattern[str], str] | Expected title or RegExp. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def to_have_title(self, title_or_reg_exp: Union[str, Pattern[str]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

PageAssertions.to_have_title

Ensures the page has the given title.

**Usage**

```py
import re
from playwright.async_api import expect

# ...
await expect(page).to_have_title(re.compile(r".*checkout"))
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `title_or_reg_exp` | Union[Pattern[str], str] | Expected title or RegExp. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## to_have_url

### 同步

```python signature
def to_have_url(self, url_or_reg_exp: Union[str, Pattern[str]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

PageAssertions.to_have_url

Ensures the page is navigated to the given URL.

**Usage**

```py
import re
from playwright.sync_api import expect

# ...
expect(page).to_have_url(re.compile(".*checkout"))
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url_or_reg_exp` | Union[Pattern[str], str] | Expected URL string or RegExp. |
| `ignore_case` | Union[bool, None] | Whether to perform case-insensitive match. `ignore_case` option takes precedence over the corresponding regular expression parameter if specified. A provided predicate ignores this flag. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def to_have_url(self, url_or_reg_exp: Union[str, Pattern[str]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

PageAssertions.to_have_url

Ensures the page is navigated to the given URL.

**Usage**

```py
import re
from playwright.async_api import expect

# ...
await expect(page).to_have_url(re.compile(".*checkout"))
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url_or_reg_exp` | Union[Pattern[str], str] | Expected URL string or RegExp. |
| `ignore_case` | Union[bool, None] | Whether to perform case-insensitive match. `ignore_case` option takes precedence over the corresponding regular expression parameter if specified. A provided predicate ignores this flag. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## to_match_aria_snapshot

### 同步

```python signature
def to_match_aria_snapshot(self, expected: str, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

PageAssertions.to_match_aria_snapshot

Asserts that the page body matches the given [accessibility snapshot](https://playwright.dev/python/docs/aria-snapshots).

**Usage**

```py
page.goto("https://demo.playwright.dev/todomvc/")
expect(page).to_match_aria_snapshot('''
  - heading "todos"
  - textbox "What needs to be done?"
''')
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expected` | str |  |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def to_match_aria_snapshot(self, expected: str, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

PageAssertions.to_match_aria_snapshot

Asserts that the page body matches the given [accessibility snapshot](https://playwright.dev/python/docs/aria-snapshots).

**Usage**

```py
await page.goto("https://demo.playwright.dev/todomvc/")
await expect(page).to_match_aria_snapshot('''
  - heading "todos"
  - textbox "What needs to be done?"
''')
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expected` | str |  |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |
