# 原生 LocatorAssertions

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [not_to_be_attached](#not_to_be_attached)
- [not_to_be_checked](#not_to_be_checked)
- [not_to_be_disabled](#not_to_be_disabled)
- [not_to_be_editable](#not_to_be_editable)
- [not_to_be_empty](#not_to_be_empty)
- [not_to_be_enabled](#not_to_be_enabled)
- [not_to_be_focused](#not_to_be_focused)
- [not_to_be_hidden](#not_to_be_hidden)
- [not_to_be_in_viewport](#not_to_be_in_viewport)
- [not_to_be_visible](#not_to_be_visible)
- [not_to_contain_class](#not_to_contain_class)
- [not_to_contain_text](#not_to_contain_text)
- [not_to_have_accessible_description](#not_to_have_accessible_description)
- [not_to_have_accessible_error_message](#not_to_have_accessible_error_message)
- [not_to_have_accessible_name](#not_to_have_accessible_name)
- [not_to_have_attribute](#not_to_have_attribute)
- [not_to_have_class](#not_to_have_class)
- [not_to_have_count](#not_to_have_count)
- [not_to_have_css](#not_to_have_css)
- [not_to_have_id](#not_to_have_id)
- [not_to_have_js_property](#not_to_have_js_property)
- [not_to_have_role](#not_to_have_role)
- [not_to_have_text](#not_to_have_text)
- [not_to_have_value](#not_to_have_value)
- [not_to_have_values](#not_to_have_values)
- [not_to_match_aria_snapshot](#not_to_match_aria_snapshot)
- [on](#on)
- [once](#once)
- [remove_listener](#remove_listener)
- [to_be_attached](#to_be_attached)
- [to_be_checked](#to_be_checked)
- [to_be_disabled](#to_be_disabled)
- [to_be_editable](#to_be_editable)
- [to_be_empty](#to_be_empty)
- [to_be_enabled](#to_be_enabled)
- [to_be_focused](#to_be_focused)
- [to_be_hidden](#to_be_hidden)
- [to_be_in_viewport](#to_be_in_viewport)
- [to_be_visible](#to_be_visible)
- [to_contain_class](#to_contain_class)
- [to_contain_text](#to_contain_text)
- [to_have_accessible_description](#to_have_accessible_description)
- [to_have_accessible_error_message](#to_have_accessible_error_message)
- [to_have_accessible_name](#to_have_accessible_name)
- [to_have_attribute](#to_have_attribute)
- [to_have_class](#to_have_class)
- [to_have_count](#to_have_count)
- [to_have_css](#to_have_css)
- [to_have_id](#to_have_id)
- [to_have_js_property](#to_have_js_property)
- [to_have_role](#to_have_role)
- [to_have_text](#to_have_text)
- [to_have_value](#to_have_value)
- [to_have_values](#to_have_values)
- [to_match_aria_snapshot](#to_match_aria_snapshot)

## not_to_be_attached

### 同步

```python signature
def not_to_be_attached(self, *, attached: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_be_attached

The opposite of `locator_assertions.to_be_attached()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `attached` | Union[bool, None] |  |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def not_to_be_attached(self, *, attached: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_be_attached

The opposite of `locator_assertions.to_be_attached()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `attached` | Union[bool, None] |  |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## not_to_be_checked

### 同步

```python signature
def not_to_be_checked(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_be_checked

The opposite of `locator_assertions.to_be_checked()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def not_to_be_checked(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_be_checked

The opposite of `locator_assertions.to_be_checked()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## not_to_be_disabled

### 同步

```python signature
def not_to_be_disabled(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_be_disabled

The opposite of `locator_assertions.to_be_disabled()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def not_to_be_disabled(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_be_disabled

The opposite of `locator_assertions.to_be_disabled()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## not_to_be_editable

### 同步

```python signature
def not_to_be_editable(self, *, editable: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_be_editable

The opposite of `locator_assertions.to_be_editable()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `editable` | Union[bool, None] |  |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def not_to_be_editable(self, *, editable: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_be_editable

The opposite of `locator_assertions.to_be_editable()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `editable` | Union[bool, None] |  |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## not_to_be_empty

### 同步

```python signature
def not_to_be_empty(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_be_empty

The opposite of `locator_assertions.to_be_empty()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def not_to_be_empty(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_be_empty

The opposite of `locator_assertions.to_be_empty()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## not_to_be_enabled

### 同步

```python signature
def not_to_be_enabled(self, *, enabled: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_be_enabled

The opposite of `locator_assertions.to_be_enabled()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `enabled` | Union[bool, None] |  |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def not_to_be_enabled(self, *, enabled: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_be_enabled

The opposite of `locator_assertions.to_be_enabled()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `enabled` | Union[bool, None] |  |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## not_to_be_focused

### 同步

```python signature
def not_to_be_focused(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_be_focused

The opposite of `locator_assertions.to_be_focused()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def not_to_be_focused(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_be_focused

The opposite of `locator_assertions.to_be_focused()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## not_to_be_hidden

### 同步

```python signature
def not_to_be_hidden(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_be_hidden

The opposite of `locator_assertions.to_be_hidden()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def not_to_be_hidden(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_be_hidden

The opposite of `locator_assertions.to_be_hidden()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## not_to_be_in_viewport

### 同步

```python signature
def not_to_be_in_viewport(self, *, ratio: Optional[float] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_be_in_viewport

The opposite of `locator_assertions.to_be_in_viewport()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `ratio` | Union[float, None] |  |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def not_to_be_in_viewport(self, *, ratio: Optional[float] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_be_in_viewport

The opposite of `locator_assertions.to_be_in_viewport()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `ratio` | Union[float, None] |  |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## not_to_be_visible

### 同步

```python signature
def not_to_be_visible(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None, visible: Optional[bool] = None) -> None
```

LocatorAssertions.not_to_be_visible

The opposite of `locator_assertions.to_be_visible()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |
| `visible` | Union[bool, None] |  |

### 异步

```python signature
async def not_to_be_visible(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None, visible: Optional[bool] = None) -> None
```

LocatorAssertions.not_to_be_visible

The opposite of `locator_assertions.to_be_visible()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |
| `visible` | Union[bool, None] |  |

## not_to_contain_class

### 同步

```python signature
def not_to_contain_class(self, expected: Union[str, Sequence[str]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_contain_class

The opposite of `locator_assertions.to_contain_class()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expected` | Union[Sequence[str], str] | Expected class or RegExp or a list of those. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def not_to_contain_class(self, expected: Union[str, Sequence[str]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_contain_class

The opposite of `locator_assertions.to_contain_class()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expected` | Union[Sequence[str], str] | Expected class or RegExp or a list of those. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## not_to_contain_text

### 同步

```python signature
def not_to_contain_text(self, expected: Union[str, Pattern[str], Sequence[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, use_inner_text: Optional[bool] = None) -> None
```

LocatorAssertions.not_to_contain_text

The opposite of `locator_assertions.to_contain_text()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expected` | Union[Pattern[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]], Sequence[str], str] | Expected substring or RegExp or a list of those. |
| `ignore_case` | Union[bool, None] | Whether to perform case-insensitive match. `ignore_case` option takes precedence over the corresponding regular expression flag if specified. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |
| `use_inner_text` | Union[bool, None] | Whether to use `element.innerText` instead of `element.textContent` when retrieving DOM node text. |

### 异步

```python signature
async def not_to_contain_text(self, expected: Union[str, Pattern[str], Sequence[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, use_inner_text: Optional[bool] = None) -> None
```

LocatorAssertions.not_to_contain_text

The opposite of `locator_assertions.to_contain_text()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expected` | Union[Pattern[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]], Sequence[str], str] | Expected substring or RegExp or a list of those. |
| `ignore_case` | Union[bool, None] | Whether to perform case-insensitive match. `ignore_case` option takes precedence over the corresponding regular expression flag if specified. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |
| `use_inner_text` | Union[bool, None] | Whether to use `element.innerText` instead of `element.textContent` when retrieving DOM node text. |

## not_to_have_accessible_description

### 同步

```python signature
def not_to_have_accessible_description(self, name: Union[str, Pattern[str]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_have_accessible_description

The opposite of `locator_assertions.to_have_accessible_description()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | Union[Pattern[str], str] | Expected accessible description. |
| `ignore_case` | Union[bool, None] | Whether to perform case-insensitive match. `ignore_case` option takes precedence over the corresponding regular expression flag if specified. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def not_to_have_accessible_description(self, name: Union[str, Pattern[str]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_have_accessible_description

The opposite of `locator_assertions.to_have_accessible_description()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | Union[Pattern[str], str] | Expected accessible description. |
| `ignore_case` | Union[bool, None] | Whether to perform case-insensitive match. `ignore_case` option takes precedence over the corresponding regular expression flag if specified. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## not_to_have_accessible_error_message

### 同步

```python signature
def not_to_have_accessible_error_message(self, error_message: Union[str, Pattern[str]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_have_accessible_error_message

The opposite of `locator_assertions.to_have_accessible_error_message()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `error_message` | Union[Pattern[str], str] | Expected accessible error message. |
| `ignore_case` | Union[bool, None] | Whether to perform case-insensitive match. `ignore_case` option takes precedence over the corresponding regular expression flag if specified. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def not_to_have_accessible_error_message(self, error_message: Union[str, Pattern[str]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_have_accessible_error_message

The opposite of `locator_assertions.to_have_accessible_error_message()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `error_message` | Union[Pattern[str], str] | Expected accessible error message. |
| `ignore_case` | Union[bool, None] | Whether to perform case-insensitive match. `ignore_case` option takes precedence over the corresponding regular expression flag if specified. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## not_to_have_accessible_name

### 同步

```python signature
def not_to_have_accessible_name(self, name: Union[str, Pattern[str]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_have_accessible_name

The opposite of `locator_assertions.to_have_accessible_name()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | Union[Pattern[str], str] | Expected accessible name. |
| `ignore_case` | Union[bool, None] | Whether to perform case-insensitive match. `ignore_case` option takes precedence over the corresponding regular expression flag if specified. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def not_to_have_accessible_name(self, name: Union[str, Pattern[str]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_have_accessible_name

The opposite of `locator_assertions.to_have_accessible_name()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | Union[Pattern[str], str] | Expected accessible name. |
| `ignore_case` | Union[bool, None] | Whether to perform case-insensitive match. `ignore_case` option takes precedence over the corresponding regular expression flag if specified. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## not_to_have_attribute

### 同步

```python signature
def not_to_have_attribute(self, name: str, value: Union[str, Pattern[str], NoneType] = None, *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_have_attribute

The opposite of `locator_assertions.to_have_attribute()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | Attribute name. |
| `value` | Union[Pattern[str], str, None] | Expected attribute value. If not specified, the assertion verifies that the attribute is absent. |
| `ignore_case` | Union[bool, None] | Whether to perform case-insensitive match. `ignore_case` option takes precedence over the corresponding regular expression flag if specified. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def not_to_have_attribute(self, name: str, value: Union[str, Pattern[str], NoneType] = None, *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_have_attribute

The opposite of `locator_assertions.to_have_attribute()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | Attribute name. |
| `value` | Union[Pattern[str], str, None] | Expected attribute value. If not specified, the assertion verifies that the attribute is absent. |
| `ignore_case` | Union[bool, None] | Whether to perform case-insensitive match. `ignore_case` option takes precedence over the corresponding regular expression flag if specified. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## not_to_have_class

### 同步

```python signature
def not_to_have_class(self, expected: Union[str, Pattern[str], Sequence[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_have_class

The opposite of `locator_assertions.to_have_class()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expected` | Union[Pattern[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]], Sequence[str], str] | Expected class or RegExp or a list of those. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def not_to_have_class(self, expected: Union[str, Pattern[str], Sequence[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_have_class

The opposite of `locator_assertions.to_have_class()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expected` | Union[Pattern[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]], Sequence[str], str] | Expected class or RegExp or a list of those. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## not_to_have_count

### 同步

```python signature
def not_to_have_count(self, count: int, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_have_count

The opposite of `locator_assertions.to_have_count()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `count` | int | Expected count. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def not_to_have_count(self, count: int, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_have_count

The opposite of `locator_assertions.to_have_count()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `count` | int | Expected count. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## not_to_have_css

### 同步

```python signature
def not_to_have_css(self, name: str, value: Union[str, Pattern[str]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_have_css

The opposite of `locator_assertions.to_have_css()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | CSS property name. |
| `value` | Union[Pattern[str], str] | CSS property value. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def not_to_have_css(self, name: str, value: Union[str, Pattern[str]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_have_css

The opposite of `locator_assertions.to_have_css()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | CSS property name. |
| `value` | Union[Pattern[str], str] | CSS property value. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## not_to_have_id

### 同步

```python signature
def not_to_have_id(self, id: Union[str, Pattern[str]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_have_id

The opposite of `locator_assertions.to_have_id()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `id` | Union[Pattern[str], str] | Element id. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def not_to_have_id(self, id: Union[str, Pattern[str]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_have_id

The opposite of `locator_assertions.to_have_id()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `id` | Union[Pattern[str], str] | Element id. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## not_to_have_js_property

### 同步

```python signature
def not_to_have_js_property(self, name: str, value: Any, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_have_js_property

The opposite of `locator_assertions.to_have_js_property()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | Property name. |
| `value` | Any | Property value. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def not_to_have_js_property(self, name: str, value: Any, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_have_js_property

The opposite of `locator_assertions.to_have_js_property()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | Property name. |
| `value` | Any | Property value. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## not_to_have_role

### 同步

```python signature
def not_to_have_role(self, role: Literal['alert', 'alertdialog', 'application', 'article', 'banner', 'blockquote', 'button', 'caption', 'cell', 'checkbox', 'code', 'columnheader', 'combobox', 'complementary', 'contentinfo', 'definition', 'deletion', 'dialog', 'directory', 'document', 'emphasis', 'feed', 'figure', 'form', 'generic', 'grid', 'gridcell', 'group', 'heading', 'img', 'insertion', 'link', 'list', 'listbox', 'listitem', 'log', 'main', 'marquee', 'math', 'menu', 'menubar', 'menuitem', 'menuitemcheckbox', 'menuitemradio', 'meter', 'navigation', 'none', 'note', 'option', 'paragraph', 'presentation', 'progressbar', 'radio', 'radiogroup', 'region', 'row', 'rowgroup', 'rowheader', 'scrollbar', 'search', 'searchbox', 'separator', 'slider', 'spinbutton', 'status', 'strong', 'subscript', 'superscript', 'switch', 'tab', 'table', 'tablist', 'tabpanel', 'term', 'textbox', 'time', 'timer', 'toolbar', 'tooltip', 'tree', 'treegrid', 'treeitem'], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_have_role

The opposite of `locator_assertions.to_have_role()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `role` | Union["alert", "alertdialog", "application", "article", "banner", "blockquote", "button", "caption", "cell", "checkbox", "code", "columnheader", "combobox", "complementary", "contentinfo", "definition", "deletion", "dialog", "directory", "document", "emphasis", "feed", "figure", "form", "generic", "grid", "gridcell", "group", "heading", "img", "insertion", "link", "list", "listbox", "listitem", "log", "main", "marquee", "math", "menu", "menubar", "menuitem", "menuitemcheckbox", "menuitemradio", "meter", "navigation", "none", "note", "option", "paragraph", "presentation", "progressbar", "radio", "radiogroup", "region", "row", "rowgroup", "rowheader", "scrollbar", "search", "searchbox", "separator", "slider", "spinbutton", "status", "strong", "subscript", "superscript", "switch", "tab", "table", "tablist", "tabpanel", "term", "textbox", "time", "timer", "toolbar", "tooltip", "tree", "treegrid", "treeitem"] | Required aria role. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def not_to_have_role(self, role: Literal['alert', 'alertdialog', 'application', 'article', 'banner', 'blockquote', 'button', 'caption', 'cell', 'checkbox', 'code', 'columnheader', 'combobox', 'complementary', 'contentinfo', 'definition', 'deletion', 'dialog', 'directory', 'document', 'emphasis', 'feed', 'figure', 'form', 'generic', 'grid', 'gridcell', 'group', 'heading', 'img', 'insertion', 'link', 'list', 'listbox', 'listitem', 'log', 'main', 'marquee', 'math', 'menu', 'menubar', 'menuitem', 'menuitemcheckbox', 'menuitemradio', 'meter', 'navigation', 'none', 'note', 'option', 'paragraph', 'presentation', 'progressbar', 'radio', 'radiogroup', 'region', 'row', 'rowgroup', 'rowheader', 'scrollbar', 'search', 'searchbox', 'separator', 'slider', 'spinbutton', 'status', 'strong', 'subscript', 'superscript', 'switch', 'tab', 'table', 'tablist', 'tabpanel', 'term', 'textbox', 'time', 'timer', 'toolbar', 'tooltip', 'tree', 'treegrid', 'treeitem'], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_have_role

The opposite of `locator_assertions.to_have_role()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `role` | Union["alert", "alertdialog", "application", "article", "banner", "blockquote", "button", "caption", "cell", "checkbox", "code", "columnheader", "combobox", "complementary", "contentinfo", "definition", "deletion", "dialog", "directory", "document", "emphasis", "feed", "figure", "form", "generic", "grid", "gridcell", "group", "heading", "img", "insertion", "link", "list", "listbox", "listitem", "log", "main", "marquee", "math", "menu", "menubar", "menuitem", "menuitemcheckbox", "menuitemradio", "meter", "navigation", "none", "note", "option", "paragraph", "presentation", "progressbar", "radio", "radiogroup", "region", "row", "rowgroup", "rowheader", "scrollbar", "search", "searchbox", "separator", "slider", "spinbutton", "status", "strong", "subscript", "superscript", "switch", "tab", "table", "tablist", "tabpanel", "term", "textbox", "time", "timer", "toolbar", "tooltip", "tree", "treegrid", "treeitem"] | Required aria role. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## not_to_have_text

### 同步

```python signature
def not_to_have_text(self, expected: Union[str, Pattern[str], Sequence[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, use_inner_text: Optional[bool] = None) -> None
```

LocatorAssertions.not_to_have_text

The opposite of `locator_assertions.to_have_text()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expected` | Union[Pattern[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]], Sequence[str], str] | Expected string or RegExp or a list of those. |
| `ignore_case` | Union[bool, None] | Whether to perform case-insensitive match. `ignore_case` option takes precedence over the corresponding regular expression flag if specified. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |
| `use_inner_text` | Union[bool, None] | Whether to use `element.innerText` instead of `element.textContent` when retrieving DOM node text. |

### 异步

```python signature
async def not_to_have_text(self, expected: Union[str, Pattern[str], Sequence[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, use_inner_text: Optional[bool] = None) -> None
```

LocatorAssertions.not_to_have_text

The opposite of `locator_assertions.to_have_text()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expected` | Union[Pattern[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]], Sequence[str], str] | Expected string or RegExp or a list of those. |
| `ignore_case` | Union[bool, None] | Whether to perform case-insensitive match. `ignore_case` option takes precedence over the corresponding regular expression flag if specified. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |
| `use_inner_text` | Union[bool, None] | Whether to use `element.innerText` instead of `element.textContent` when retrieving DOM node text. |

## not_to_have_value

### 同步

```python signature
def not_to_have_value(self, value: Union[str, Pattern[str]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_have_value

The opposite of `locator_assertions.to_have_value()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `value` | Union[Pattern[str], str] | Expected value. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def not_to_have_value(self, value: Union[str, Pattern[str]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_have_value

The opposite of `locator_assertions.to_have_value()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `value` | Union[Pattern[str], str] | Expected value. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## not_to_have_values

### 同步

```python signature
def not_to_have_values(self, values: Union[Sequence[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_have_values

The opposite of `locator_assertions.to_have_values()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `values` | Union[Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]], Sequence[str]] | Expected options currently selected. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def not_to_have_values(self, values: Union[Sequence[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_have_values

The opposite of `locator_assertions.to_have_values()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `values` | Union[Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]], Sequence[str]] | Expected options currently selected. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## not_to_match_aria_snapshot

### 同步

```python signature
def not_to_match_aria_snapshot(self, expected: str, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_match_aria_snapshot

The opposite of `locator_assertions.to_match_aria_snapshot()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expected` | str |  |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def not_to_match_aria_snapshot(self, expected: str, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.not_to_match_aria_snapshot

The opposite of `locator_assertions.to_match_aria_snapshot()`.

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


## to_be_attached

### 同步

```python signature
def to_be_attached(self, *, attached: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_be_attached

Ensures that `Locator` points to an element that is
[connected](https://developer.mozilla.org/en-US/docs/Web/API/Node/isConnected) to a Document or a ShadowRoot.

**Usage**

```py
expect(page.get_by_text("Hidden text")).to_be_attached()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `attached` | Union[bool, None] |  |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def to_be_attached(self, *, attached: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_be_attached

Ensures that `Locator` points to an element that is
[connected](https://developer.mozilla.org/en-US/docs/Web/API/Node/isConnected) to a Document or a ShadowRoot.

**Usage**

```py
await expect(page.get_by_text("Hidden text")).to_be_attached()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `attached` | Union[bool, None] |  |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## to_be_checked

### 同步

```python signature
def to_be_checked(self, *, checked: Optional[bool] = None, indeterminate: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_be_checked

Ensures the `Locator` points to a checked input.

**Usage**

```py
from playwright.sync_api import expect

locator = page.get_by_label("Subscribe to newsletter")
expect(locator).to_be_checked()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `checked` | Union[bool, None] | Provides state to assert for. Asserts for input to be checked by default. This option can't be used when `indeterminate` is set to true. |
| `indeterminate` | Union[bool, None] | Asserts that the element is in the indeterminate (mixed) state. Only supported for checkboxes and radio buttons. This option can't be true when `checked` is provided. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def to_be_checked(self, *, checked: Optional[bool] = None, indeterminate: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_be_checked

Ensures the `Locator` points to a checked input.

**Usage**

```py
from playwright.async_api import expect

locator = page.get_by_label("Subscribe to newsletter")
await expect(locator).to_be_checked()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `checked` | Union[bool, None] | Provides state to assert for. Asserts for input to be checked by default. This option can't be used when `indeterminate` is set to true. |
| `indeterminate` | Union[bool, None] | Asserts that the element is in the indeterminate (mixed) state. Only supported for checkboxes and radio buttons. This option can't be true when `checked` is provided. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## to_be_disabled

### 同步

```python signature
def to_be_disabled(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_be_disabled

Ensures the `Locator` points to a disabled element. Element is disabled if it has "disabled" attribute or is
disabled via
['aria-disabled'](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-disabled). Note
that only native control elements such as HTML `button`, `input`, `select`, `textarea`, `option`, `optgroup` can be
disabled by setting "disabled" attribute. "disabled" attribute on other elements is ignored by the browser.

**Usage**

```py
from playwright.sync_api import expect

locator = page.locator("button.submit")
expect(locator).to_be_disabled()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def to_be_disabled(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_be_disabled

Ensures the `Locator` points to a disabled element. Element is disabled if it has "disabled" attribute or is
disabled via
['aria-disabled'](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Attributes/aria-disabled). Note
that only native control elements such as HTML `button`, `input`, `select`, `textarea`, `option`, `optgroup` can be
disabled by setting "disabled" attribute. "disabled" attribute on other elements is ignored by the browser.

**Usage**

```py
from playwright.async_api import expect

locator = page.locator("button.submit")
await expect(locator).to_be_disabled()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## to_be_editable

### 同步

```python signature
def to_be_editable(self, *, editable: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_be_editable

Ensures the `Locator` points to an editable element.

**Usage**

```py
from playwright.sync_api import expect

locator = page.get_by_role("textbox")
expect(locator).to_be_editable()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `editable` | Union[bool, None] |  |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def to_be_editable(self, *, editable: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_be_editable

Ensures the `Locator` points to an editable element.

**Usage**

```py
from playwright.async_api import expect

locator = page.get_by_role("textbox")
await expect(locator).to_be_editable()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `editable` | Union[bool, None] |  |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## to_be_empty

### 同步

```python signature
def to_be_empty(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_be_empty

Ensures the `Locator` points to an empty editable element or to a DOM node that has no text.

**Usage**

```py
from playwright.sync_api import expect

locator = page.locator("div.warning")
expect(locator).to_be_empty()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def to_be_empty(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_be_empty

Ensures the `Locator` points to an empty editable element or to a DOM node that has no text.

**Usage**

```py
from playwright.async_api import expect

locator = page.locator("div.warning")
await expect(locator).to_be_empty()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## to_be_enabled

### 同步

```python signature
def to_be_enabled(self, *, enabled: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_be_enabled

Ensures the `Locator` points to an enabled element.

**Usage**

```py
from playwright.sync_api import expect

locator = page.locator("button.submit")
expect(locator).to_be_enabled()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `enabled` | Union[bool, None] |  |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def to_be_enabled(self, *, enabled: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_be_enabled

Ensures the `Locator` points to an enabled element.

**Usage**

```py
from playwright.async_api import expect

locator = page.locator("button.submit")
await expect(locator).to_be_enabled()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `enabled` | Union[bool, None] |  |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## to_be_focused

### 同步

```python signature
def to_be_focused(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_be_focused

Ensures the `Locator` points to a focused DOM node.

**Usage**

```py
from playwright.sync_api import expect

locator = page.get_by_role("textbox")
expect(locator).to_be_focused()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def to_be_focused(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_be_focused

Ensures the `Locator` points to a focused DOM node.

**Usage**

```py
from playwright.async_api import expect

locator = page.get_by_role("textbox")
await expect(locator).to_be_focused()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## to_be_hidden

### 同步

```python signature
def to_be_hidden(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_be_hidden

Ensures that `Locator` either does not resolve to any DOM node, or resolves to a
[non-visible](https://playwright.dev/python/docs/actionability#visible) one.

**Usage**

```py
from playwright.sync_api import expect

locator = page.locator('.my-element')
expect(locator).to_be_hidden()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def to_be_hidden(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_be_hidden

Ensures that `Locator` either does not resolve to any DOM node, or resolves to a
[non-visible](https://playwright.dev/python/docs/actionability#visible) one.

**Usage**

```py
from playwright.async_api import expect

locator = page.locator('.my-element')
await expect(locator).to_be_hidden()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## to_be_in_viewport

### 同步

```python signature
def to_be_in_viewport(self, *, ratio: Optional[float] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_be_in_viewport

Ensures the `Locator` points to an element that intersects viewport, according to the
[intersection observer API](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API).

**Usage**

```py
from playwright.sync_api import expect

locator = page.get_by_role("button")
# Make sure at least some part of element intersects viewport.
expect(locator).to_be_in_viewport()
# Make sure element is fully outside of viewport.
expect(locator).not_to_be_in_viewport()
# Make sure that at least half of the element intersects viewport.
expect(locator).to_be_in_viewport(ratio=0.5)
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `ratio` | Union[float, None] | The minimal ratio of the element to intersect viewport. If equals to `0`, then element should intersect viewport at any positive ratio. Defaults to `0`. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def to_be_in_viewport(self, *, ratio: Optional[float] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_be_in_viewport

Ensures the `Locator` points to an element that intersects viewport, according to the
[intersection observer API](https://developer.mozilla.org/en-US/docs/Web/API/Intersection_Observer_API).

**Usage**

```py
from playwright.async_api import expect

locator = page.get_by_role("button")
# Make sure at least some part of element intersects viewport.
await expect(locator).to_be_in_viewport()
# Make sure element is fully outside of viewport.
await expect(locator).not_to_be_in_viewport()
# Make sure that at least half of the element intersects viewport.
await expect(locator).to_be_in_viewport(ratio=0.5)
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `ratio` | Union[float, None] | The minimal ratio of the element to intersect viewport. If equals to `0`, then element should intersect viewport at any positive ratio. Defaults to `0`. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## to_be_visible

### 同步

```python signature
def to_be_visible(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None, visible: Optional[bool] = None) -> None
```

LocatorAssertions.to_be_visible

Ensures that `Locator` points to an attached and [visible](https://playwright.dev/python/docs/actionability#visible) DOM node.

To check that at least one element from the list is visible, use `locator.first`.

**Usage**

```py
# A specific element is visible.
expect(page.get_by_text("Welcome")).to_be_visible()

# At least one item in the list is visible.
expect(page.get_by_test_id("todo-item").first).to_be_visible()

# At least one of the two elements is visible, possibly both.
expect(
    page.get_by_role("button", name="Sign in")
    .or_(page.get_by_role("button", name="Sign up"))
    .first
).to_be_visible()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |
| `visible` | Union[bool, None] |  |

### 异步

```python signature
async def to_be_visible(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None, visible: Optional[bool] = None) -> None
```

LocatorAssertions.to_be_visible

Ensures that `Locator` points to an attached and [visible](https://playwright.dev/python/docs/actionability#visible) DOM node.

To check that at least one element from the list is visible, use `locator.first`.

**Usage**

```py
# A specific element is visible.
await expect(page.get_by_text("Welcome")).to_be_visible()

# At least one item in the list is visible.
await expect(page.get_by_test_id("todo-item").first).to_be_visible()

# At least one of the two elements is visible, possibly both.
await expect(
    page.get_by_role("button", name="Sign in")
    .or_(page.get_by_role("button", name="Sign up"))
    .first
).to_be_visible()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |
| `visible` | Union[bool, None] |  |

## to_contain_class

### 同步

```python signature
def to_contain_class(self, expected: Union[str, Sequence[str]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_contain_class

Ensures the `Locator` points to an element with given CSS classes. All classes from the asserted value, separated
by spaces, must be present in the
[Element.classList](https://developer.mozilla.org/en-US/docs/Web/API/Element/classList) in any order.

**Usage**

```html
<div class='middle selected row' id='component'></div>
```

```py
from playwright.sync_api import expect

locator = page.locator("#component")
expect(locator).to_contain_class("middle selected row")
expect(locator).to_contain_class("selected")
expect(locator).to_contain_class("row middle")
```

When an array is passed, the method asserts that the list of elements located matches the corresponding list of
expected class lists. Each element's class attribute is matched against the corresponding class in the array:

```html
<div class='list'>
  <div class='component inactive'></div>
  <div class='component active'></div>
  <div class='component inactive'></div>
</div>
```

```py
from playwright.sync_api import expect

locator = page.locator(".list > .component")
await expect(locator).to_contain_class(["inactive", "active", "inactive"])
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expected` | Union[Sequence[str], str] | A string containing expected class names, separated by spaces, or a list of such strings to assert multiple elements. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def to_contain_class(self, expected: Union[str, Sequence[str]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_contain_class

Ensures the `Locator` points to an element with given CSS classes. All classes from the asserted value, separated
by spaces, must be present in the
[Element.classList](https://developer.mozilla.org/en-US/docs/Web/API/Element/classList) in any order.

**Usage**

```html
<div class='middle selected row' id='component'></div>
```

```py
from playwright.async_api import expect

locator = page.locator("#component")
await expect(locator).to_contain_class("middle selected row")
await expect(locator).to_contain_class("selected")
await expect(locator).to_contain_class("row middle")
```

When an array is passed, the method asserts that the list of elements located matches the corresponding list of
expected class lists. Each element's class attribute is matched against the corresponding class in the array:

```html
<div class='list'>
  <div class='component inactive'></div>
  <div class='component active'></div>
  <div class='component inactive'></div>
</div>
```

```py
from playwright.async_api import expect

locator = page.locator(".list > .component")
await expect(locator).to_contain_class(["inactive", "active", "inactive"])
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expected` | Union[Sequence[str], str] | A string containing expected class names, separated by spaces, or a list of such strings to assert multiple elements. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## to_contain_text

### 同步

```python signature
def to_contain_text(self, expected: Union[str, Pattern[str], Sequence[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, use_inner_text: Optional[bool] = None) -> None
```

LocatorAssertions.to_contain_text

Ensures the `Locator` points to an element that contains the given text. All nested elements will be considered
when computing the text content of the element. You can use regular expressions for the value as well.

**Details**

When `expected` parameter is a string, Playwright will normalize whitespaces and line breaks both in the actual
text and in the expected string before matching. When regular expression is used, the actual text is matched as is.

**Usage**

```py
import re
from playwright.sync_api import expect

locator = page.locator('.title')
expect(locator).to_contain_text("substring")
expect(locator).to_contain_text(re.compile(r"\d messages"))
```

If you pass an array as an expected value, the expectations are:
1. Locator resolves to a list of elements.
1. Elements from a **subset** of this list contain text from the expected array, respectively.
1. The matching subset of elements has the same order as the expected array.
1. Each text value from the expected array is matched by some element from the list.

For example, consider the following list:

```html
<ul>
  <li>Item Text 1</li>
  <li>Item Text 2</li>
  <li>Item Text 3</li>
</ul>
```

Let's see how we can use the assertion:

```py
from playwright.sync_api import expect

# ✓ Contains the right items in the right order
expect(page.locator("ul > li")).to_contain_text(["Text 1", "Text 3"])

# ✖ Wrong order
expect(page.locator("ul > li")).to_contain_text(["Text 3", "Text 2"])

# ✖ No item contains this text
expect(page.locator("ul > li")).to_contain_text(["Some 33"])

# ✖ Locator points to the outer list element, not to the list items
expect(page.locator("ul")).to_contain_text(["Text 3"])
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expected` | Union[Pattern[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]], Sequence[str], str] | Expected substring or RegExp or a list of those. |
| `ignore_case` | Union[bool, None] | Whether to perform case-insensitive match. `ignore_case` option takes precedence over the corresponding regular expression flag if specified. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |
| `use_inner_text` | Union[bool, None] | Whether to use `element.innerText` instead of `element.textContent` when retrieving DOM node text. |

### 异步

```python signature
async def to_contain_text(self, expected: Union[str, Pattern[str], Sequence[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, use_inner_text: Optional[bool] = None) -> None
```

LocatorAssertions.to_contain_text

Ensures the `Locator` points to an element that contains the given text. All nested elements will be considered
when computing the text content of the element. You can use regular expressions for the value as well.

**Details**

When `expected` parameter is a string, Playwright will normalize whitespaces and line breaks both in the actual
text and in the expected string before matching. When regular expression is used, the actual text is matched as is.

**Usage**

```py
import re
from playwright.async_api import expect

locator = page.locator('.title')
await expect(locator).to_contain_text("substring")
await expect(locator).to_contain_text(re.compile(r"\d messages"))
```

If you pass an array as an expected value, the expectations are:
1. Locator resolves to a list of elements.
1. Elements from a **subset** of this list contain text from the expected array, respectively.
1. The matching subset of elements has the same order as the expected array.
1. Each text value from the expected array is matched by some element from the list.

For example, consider the following list:

```html
<ul>
  <li>Item Text 1</li>
  <li>Item Text 2</li>
  <li>Item Text 3</li>
</ul>
```

Let's see how we can use the assertion:

```py
from playwright.async_api import expect

# ✓ Contains the right items in the right order
await expect(page.locator("ul > li")).to_contain_text(["Text 1", "Text 3"])

# ✖ Wrong order
await expect(page.locator("ul > li")).to_contain_text(["Text 3", "Text 2"])

# ✖ No item contains this text
await expect(page.locator("ul > li")).to_contain_text(["Some 33"])

# ✖ Locator points to the outer list element, not to the list items
await expect(page.locator("ul")).to_contain_text(["Text 3"])
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expected` | Union[Pattern[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]], Sequence[str], str] | Expected substring or RegExp or a list of those. |
| `ignore_case` | Union[bool, None] | Whether to perform case-insensitive match. `ignore_case` option takes precedence over the corresponding regular expression flag if specified. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |
| `use_inner_text` | Union[bool, None] | Whether to use `element.innerText` instead of `element.textContent` when retrieving DOM node text. |

## to_have_accessible_description

### 同步

```python signature
def to_have_accessible_description(self, description: Union[str, Pattern[str]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_have_accessible_description

Ensures the `Locator` points to an element with a given
[accessible description](https://w3c.github.io/accname/#dfn-accessible-description).

**Usage**

```py
locator = page.get_by_test_id("save-button")
expect(locator).to_have_accessible_description("Save results to disk")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `description` | Union[Pattern[str], str] | Expected accessible description. |
| `ignore_case` | Union[bool, None] | Whether to perform case-insensitive match. `ignore_case` option takes precedence over the corresponding regular expression flag if specified. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def to_have_accessible_description(self, description: Union[str, Pattern[str]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_have_accessible_description

Ensures the `Locator` points to an element with a given
[accessible description](https://w3c.github.io/accname/#dfn-accessible-description).

**Usage**

```py
locator = page.get_by_test_id("save-button")
await expect(locator).to_have_accessible_description("Save results to disk")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `description` | Union[Pattern[str], str] | Expected accessible description. |
| `ignore_case` | Union[bool, None] | Whether to perform case-insensitive match. `ignore_case` option takes precedence over the corresponding regular expression flag if specified. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## to_have_accessible_error_message

### 同步

```python signature
def to_have_accessible_error_message(self, error_message: Union[str, Pattern[str]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_have_accessible_error_message

Ensures the `Locator` points to an element with a given
[aria errormessage](https://w3c.github.io/aria/#aria-errormessage).

**Usage**

```py
locator = page.get_by_test_id("username-input")
expect(locator).to_have_accessible_error_message("Username is required.")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `error_message` | Union[Pattern[str], str] | Expected accessible error message. |
| `ignore_case` | Union[bool, None] | Whether to perform case-insensitive match. `ignore_case` option takes precedence over the corresponding regular expression flag if specified. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def to_have_accessible_error_message(self, error_message: Union[str, Pattern[str]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_have_accessible_error_message

Ensures the `Locator` points to an element with a given
[aria errormessage](https://w3c.github.io/aria/#aria-errormessage).

**Usage**

```py
locator = page.get_by_test_id("username-input")
await expect(locator).to_have_accessible_error_message("Username is required.")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `error_message` | Union[Pattern[str], str] | Expected accessible error message. |
| `ignore_case` | Union[bool, None] | Whether to perform case-insensitive match. `ignore_case` option takes precedence over the corresponding regular expression flag if specified. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## to_have_accessible_name

### 同步

```python signature
def to_have_accessible_name(self, name: Union[str, Pattern[str]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_have_accessible_name

Ensures the `Locator` points to an element with a given
[accessible name](https://w3c.github.io/accname/#dfn-accessible-name).

**Usage**

```py
locator = page.get_by_test_id("save-button")
expect(locator).to_have_accessible_name("Save to disk")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | Union[Pattern[str], str] | Expected accessible name. |
| `ignore_case` | Union[bool, None] | Whether to perform case-insensitive match. `ignore_case` option takes precedence over the corresponding regular expression flag if specified. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def to_have_accessible_name(self, name: Union[str, Pattern[str]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_have_accessible_name

Ensures the `Locator` points to an element with a given
[accessible name](https://w3c.github.io/accname/#dfn-accessible-name).

**Usage**

```py
locator = page.get_by_test_id("save-button")
await expect(locator).to_have_accessible_name("Save to disk")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | Union[Pattern[str], str] | Expected accessible name. |
| `ignore_case` | Union[bool, None] | Whether to perform case-insensitive match. `ignore_case` option takes precedence over the corresponding regular expression flag if specified. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## to_have_attribute

### 同步

```python signature
def to_have_attribute(self, name: str, value: Union[str, Pattern[str], NoneType] = None, *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_have_attribute

Ensures the `Locator` points to an element with given attribute.

**Usage**

```py
from playwright.sync_api import expect

locator = page.locator("input")
expect(locator).to_have_attribute("type", "text")
expect(locator).to_have_attribute("disabled")
expect(locator).not_to_have_attribute("readonly")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | Attribute name. |
| `value` | Union[Pattern[str], str, None] | Expected attribute value. If not specified, the assertion verifies that the attribute is present. |
| `ignore_case` | Union[bool, None] | Whether to perform case-insensitive match. `ignore_case` option takes precedence over the corresponding regular expression flag if specified. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def to_have_attribute(self, name: str, value: Union[str, Pattern[str], NoneType] = None, *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_have_attribute

Ensures the `Locator` points to an element with given attribute.

**Usage**

```py
from playwright.async_api import expect

locator = page.locator("input")
await expect(locator).to_have_attribute("type", "text")
await expect(locator).to_have_attribute("disabled")
await expect(locator).not_to_have_attribute("readonly")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | Attribute name. |
| `value` | Union[Pattern[str], str, None] | Expected attribute value. If not specified, the assertion verifies that the attribute is present. |
| `ignore_case` | Union[bool, None] | Whether to perform case-insensitive match. `ignore_case` option takes precedence over the corresponding regular expression flag if specified. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## to_have_class

### 同步

```python signature
def to_have_class(self, expected: Union[str, Pattern[str], Sequence[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_have_class

Ensures the `Locator` points to an element with given CSS classes. When a string is provided, it must fully match
the element's `class` attribute. To match individual classes use `locator_assertions.to_contain_class()`.

**Usage**

```html
<div class='middle selected row' id='component'></div>
```

```py
from playwright.sync_api import expect

locator = page.locator("#component")
expect(locator).to_have_class("middle selected row")
expect(locator).to_have_class(re.compile(r"(^|\\s)selected(\\s|$)"))
```

When an array is passed, the method asserts that the list of elements located matches the corresponding list of
expected class values. Each element's class attribute is matched against the corresponding string or regular
expression in the array:

```py
from playwright.sync_api import expect

locator = page.locator(".list > .component")
expect(locator).to_have_class(["component", "component selected", "component"])
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expected` | Union[Pattern[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]], Sequence[str], str] | Expected class or RegExp or a list of those. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def to_have_class(self, expected: Union[str, Pattern[str], Sequence[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_have_class

Ensures the `Locator` points to an element with given CSS classes. When a string is provided, it must fully match
the element's `class` attribute. To match individual classes use `locator_assertions.to_contain_class()`.

**Usage**

```html
<div class='middle selected row' id='component'></div>
```

```py
from playwright.async_api import expect

locator = page.locator("#component")
await expect(locator).to_have_class("middle selected row")
await expect(locator).to_have_class(re.compile(r"(^|\\s)selected(\\s|$)"))
```

When an array is passed, the method asserts that the list of elements located matches the corresponding list of
expected class values. Each element's class attribute is matched against the corresponding string or regular
expression in the array:

```py
from playwright.async_api import expect

locator = page.locator(".list > .component")
await expect(locator).to_have_class(["component", "component selected", "component"])
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expected` | Union[Pattern[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]], Sequence[str], str] | Expected class or RegExp or a list of those. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## to_have_count

### 同步

```python signature
def to_have_count(self, count: int, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_have_count

Ensures the `Locator` resolves to an exact number of DOM nodes.

**Usage**

```py
from playwright.sync_api import expect

locator = page.locator("list > .component")
expect(locator).to_have_count(3)
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `count` | int | Expected count. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def to_have_count(self, count: int, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_have_count

Ensures the `Locator` resolves to an exact number of DOM nodes.

**Usage**

```py
from playwright.async_api import expect

locator = page.locator("list > .component")
await expect(locator).to_have_count(3)
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `count` | int | Expected count. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## to_have_css

### 同步

```python signature
def to_have_css(self, name: str, value: Union[str, Pattern[str]], *, pseudo: Optional[Literal['after', 'before']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_have_css

Ensures the `Locator` resolves to an element with the given computed CSS style.

**Usage**

```py
from playwright.sync_api import expect

locator = page.get_by_role("button")
expect(locator).to_have_css("display", "flex")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | CSS property name. |
| `value` | Union[Pattern[str], str] | CSS property value. |
| `pseudo` | Union["after", "before", None] | Pseudo-element to read computed styles from. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def to_have_css(self, name: str, value: Union[str, Pattern[str]], *, pseudo: Optional[Literal['after', 'before']] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_have_css

Ensures the `Locator` resolves to an element with the given computed CSS style.

**Usage**

```py
from playwright.async_api import expect

locator = page.get_by_role("button")
await expect(locator).to_have_css("display", "flex")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | CSS property name. |
| `value` | Union[Pattern[str], str] | CSS property value. |
| `pseudo` | Union["after", "before", None] | Pseudo-element to read computed styles from. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## to_have_id

### 同步

```python signature
def to_have_id(self, id: Union[str, Pattern[str]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_have_id

Ensures the `Locator` points to an element with the given DOM Node ID.

**Usage**

```py
from playwright.sync_api import expect

locator = page.get_by_role("textbox")
expect(locator).to_have_id("lastname")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `id` | Union[Pattern[str], str] | Element id. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def to_have_id(self, id: Union[str, Pattern[str]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_have_id

Ensures the `Locator` points to an element with the given DOM Node ID.

**Usage**

```py
from playwright.async_api import expect

locator = page.get_by_role("textbox")
await expect(locator).to_have_id("lastname")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `id` | Union[Pattern[str], str] | Element id. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## to_have_js_property

### 同步

```python signature
def to_have_js_property(self, name: str, value: Any, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_have_js_property

Ensures the `Locator` points to an element with given JavaScript property. Note that this property can be of a
primitive type as well as a plain serializable JavaScript object.

**Usage**

```py
from playwright.sync_api import expect

locator = page.locator(".component")
expect(locator).to_have_js_property("loaded", True)
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | Property name. |
| `value` | Any | Property value. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def to_have_js_property(self, name: str, value: Any, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_have_js_property

Ensures the `Locator` points to an element with given JavaScript property. Note that this property can be of a
primitive type as well as a plain serializable JavaScript object.

**Usage**

```py
from playwright.async_api import expect

locator = page.locator(".component")
await expect(locator).to_have_js_property("loaded", True)
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | Property name. |
| `value` | Any | Property value. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## to_have_role

### 同步

```python signature
def to_have_role(self, role: Literal['alert', 'alertdialog', 'application', 'article', 'banner', 'blockquote', 'button', 'caption', 'cell', 'checkbox', 'code', 'columnheader', 'combobox', 'complementary', 'contentinfo', 'definition', 'deletion', 'dialog', 'directory', 'document', 'emphasis', 'feed', 'figure', 'form', 'generic', 'grid', 'gridcell', 'group', 'heading', 'img', 'insertion', 'link', 'list', 'listbox', 'listitem', 'log', 'main', 'marquee', 'math', 'menu', 'menubar', 'menuitem', 'menuitemcheckbox', 'menuitemradio', 'meter', 'navigation', 'none', 'note', 'option', 'paragraph', 'presentation', 'progressbar', 'radio', 'radiogroup', 'region', 'row', 'rowgroup', 'rowheader', 'scrollbar', 'search', 'searchbox', 'separator', 'slider', 'spinbutton', 'status', 'strong', 'subscript', 'superscript', 'switch', 'tab', 'table', 'tablist', 'tabpanel', 'term', 'textbox', 'time', 'timer', 'toolbar', 'tooltip', 'tree', 'treegrid', 'treeitem'], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_have_role

Ensures the `Locator` points to an element with a given [ARIA role](https://www.w3.org/TR/wai-aria-1.2/#roles).

Note that role is matched as a string, disregarding the ARIA role hierarchy. For example, asserting  a superclass
role `"checkbox"` on an element with a subclass role `"switch"` will fail.

**Usage**

```py
locator = page.get_by_test_id("save-button")
expect(locator).to_have_role("button")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `role` | Union["alert", "alertdialog", "application", "article", "banner", "blockquote", "button", "caption", "cell", "checkbox", "code", "columnheader", "combobox", "complementary", "contentinfo", "definition", "deletion", "dialog", "directory", "document", "emphasis", "feed", "figure", "form", "generic", "grid", "gridcell", "group", "heading", "img", "insertion", "link", "list", "listbox", "listitem", "log", "main", "marquee", "math", "menu", "menubar", "menuitem", "menuitemcheckbox", "menuitemradio", "meter", "navigation", "none", "note", "option", "paragraph", "presentation", "progressbar", "radio", "radiogroup", "region", "row", "rowgroup", "rowheader", "scrollbar", "search", "searchbox", "separator", "slider", "spinbutton", "status", "strong", "subscript", "superscript", "switch", "tab", "table", "tablist", "tabpanel", "term", "textbox", "time", "timer", "toolbar", "tooltip", "tree", "treegrid", "treeitem"] | Required aria role. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def to_have_role(self, role: Literal['alert', 'alertdialog', 'application', 'article', 'banner', 'blockquote', 'button', 'caption', 'cell', 'checkbox', 'code', 'columnheader', 'combobox', 'complementary', 'contentinfo', 'definition', 'deletion', 'dialog', 'directory', 'document', 'emphasis', 'feed', 'figure', 'form', 'generic', 'grid', 'gridcell', 'group', 'heading', 'img', 'insertion', 'link', 'list', 'listbox', 'listitem', 'log', 'main', 'marquee', 'math', 'menu', 'menubar', 'menuitem', 'menuitemcheckbox', 'menuitemradio', 'meter', 'navigation', 'none', 'note', 'option', 'paragraph', 'presentation', 'progressbar', 'radio', 'radiogroup', 'region', 'row', 'rowgroup', 'rowheader', 'scrollbar', 'search', 'searchbox', 'separator', 'slider', 'spinbutton', 'status', 'strong', 'subscript', 'superscript', 'switch', 'tab', 'table', 'tablist', 'tabpanel', 'term', 'textbox', 'time', 'timer', 'toolbar', 'tooltip', 'tree', 'treegrid', 'treeitem'], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_have_role

Ensures the `Locator` points to an element with a given [ARIA role](https://www.w3.org/TR/wai-aria-1.2/#roles).

Note that role is matched as a string, disregarding the ARIA role hierarchy. For example, asserting  a superclass
role `"checkbox"` on an element with a subclass role `"switch"` will fail.

**Usage**

```py
locator = page.get_by_test_id("save-button")
await expect(locator).to_have_role("button")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `role` | Union["alert", "alertdialog", "application", "article", "banner", "blockquote", "button", "caption", "cell", "checkbox", "code", "columnheader", "combobox", "complementary", "contentinfo", "definition", "deletion", "dialog", "directory", "document", "emphasis", "feed", "figure", "form", "generic", "grid", "gridcell", "group", "heading", "img", "insertion", "link", "list", "listbox", "listitem", "log", "main", "marquee", "math", "menu", "menubar", "menuitem", "menuitemcheckbox", "menuitemradio", "meter", "navigation", "none", "note", "option", "paragraph", "presentation", "progressbar", "radio", "radiogroup", "region", "row", "rowgroup", "rowheader", "scrollbar", "search", "searchbox", "separator", "slider", "spinbutton", "status", "strong", "subscript", "superscript", "switch", "tab", "table", "tablist", "tabpanel", "term", "textbox", "time", "timer", "toolbar", "tooltip", "tree", "treegrid", "treeitem"] | Required aria role. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## to_have_text

### 同步

```python signature
def to_have_text(self, expected: Union[str, Pattern[str], Sequence[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, use_inner_text: Optional[bool] = None) -> None
```

LocatorAssertions.to_have_text

Ensures the `Locator` points to an element with the given text. All nested elements will be considered when
computing the text content of the element. You can use regular expressions for the value as well.

**Details**

When `expected` parameter is a string, Playwright will normalize whitespaces and line breaks both in the actual
text and in the expected string before matching. When regular expression is used, the actual text is matched as is.

**Usage**

```py
import re
from playwright.sync_api import expect

locator = page.locator(".title")
expect(locator).to_have_text(re.compile(r"Welcome, Test User"))
expect(locator).to_have_text(re.compile(r"Welcome, .*"))
```

If you pass an array as an expected value, the expectations are:
1. Locator resolves to a list of elements.
1. The number of elements equals the number of expected values in the array.
1. Elements from the list have text matching expected array values, one by one, in order.

For example, consider the following list:

```html
<ul>
  <li>Text 1</li>
  <li>Text 2</li>
  <li>Text 3</li>
</ul>
```

Let's see how we can use the assertion:

```py
from playwright.sync_api import expect

# ✓ Has the right items in the right order
expect(page.locator("ul > li")).to_have_text(["Text 1", "Text 2", "Text 3"])

# ✖ Wrong order
expect(page.locator("ul > li")).to_have_text(["Text 3", "Text 2", "Text 1"])

# ✖ Last item does not match
expect(page.locator("ul > li")).to_have_text(["Text 1", "Text 2", "Text"])

# ✖ Locator points to the outer list element, not to the list items
expect(page.locator("ul")).to_have_text(["Text 1", "Text 2", "Text 3"])
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expected` | Union[Pattern[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]], Sequence[str], str] | Expected string or RegExp or a list of those. |
| `ignore_case` | Union[bool, None] | Whether to perform case-insensitive match. `ignore_case` option takes precedence over the corresponding regular expression flag if specified. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |
| `use_inner_text` | Union[bool, None] | Whether to use `element.innerText` instead of `element.textContent` when retrieving DOM node text. |

### 异步

```python signature
async def to_have_text(self, expected: Union[str, Pattern[str], Sequence[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]]], *, ignore_case: Optional[bool] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, use_inner_text: Optional[bool] = None) -> None
```

LocatorAssertions.to_have_text

Ensures the `Locator` points to an element with the given text. All nested elements will be considered when
computing the text content of the element. You can use regular expressions for the value as well.

**Details**

When `expected` parameter is a string, Playwright will normalize whitespaces and line breaks both in the actual
text and in the expected string before matching. When regular expression is used, the actual text is matched as is.

**Usage**

```py
import re
from playwright.async_api import expect

locator = page.locator(".title")
await expect(locator).to_have_text(re.compile(r"Welcome, Test User"))
await expect(locator).to_have_text(re.compile(r"Welcome, .*"))
```

If you pass an array as an expected value, the expectations are:
1. Locator resolves to a list of elements.
1. The number of elements equals the number of expected values in the array.
1. Elements from the list have text matching expected array values, one by one, in order.

For example, consider the following list:

```html
<ul>
  <li>Text 1</li>
  <li>Text 2</li>
  <li>Text 3</li>
</ul>
```

Let's see how we can use the assertion:

```py
from playwright.async_api import expect

# ✓ Has the right items in the right order
await expect(page.locator("ul > li")).to_have_text(["Text 1", "Text 2", "Text 3"])

# ✖ Wrong order
await expect(page.locator("ul > li")).to_have_text(["Text 3", "Text 2", "Text 1"])

# ✖ Last item does not match
await expect(page.locator("ul > li")).to_have_text(["Text 1", "Text 2", "Text"])

# ✖ Locator points to the outer list element, not to the list items
await expect(page.locator("ul")).to_have_text(["Text 1", "Text 2", "Text 3"])
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expected` | Union[Pattern[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]], Sequence[str], str] | Expected string or RegExp or a list of those. |
| `ignore_case` | Union[bool, None] | Whether to perform case-insensitive match. `ignore_case` option takes precedence over the corresponding regular expression flag if specified. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |
| `use_inner_text` | Union[bool, None] | Whether to use `element.innerText` instead of `element.textContent` when retrieving DOM node text. |

## to_have_value

### 同步

```python signature
def to_have_value(self, value: Union[str, Pattern[str]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_have_value

Ensures the `Locator` points to an element with the given input value. You can use regular expressions for the
value as well.

**Usage**

```py
import re
from playwright.sync_api import expect

locator = page.locator("input[type=number]")
expect(locator).to_have_value(re.compile(r"[0-9]"))
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `value` | Union[Pattern[str], str] | Expected value. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def to_have_value(self, value: Union[str, Pattern[str]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_have_value

Ensures the `Locator` points to an element with the given input value. You can use regular expressions for the
value as well.

**Usage**

```py
import re
from playwright.async_api import expect

locator = page.locator("input[type=number]")
await expect(locator).to_have_value(re.compile(r"[0-9]"))
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `value` | Union[Pattern[str], str] | Expected value. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## to_have_values

### 同步

```python signature
def to_have_values(self, values: Union[Sequence[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_have_values

Ensures the `Locator` points to multi-select/combobox (i.e. a `select` with the `multiple` attribute) and the
specified values are selected.

**Usage**

For example, given the following element:

```html
<select id="favorite-colors" multiple>
  <option value="R">Red</option>
  <option value="G">Green</option>
  <option value="B">Blue</option>
</select>
```

```py
import re
from playwright.sync_api import expect

locator = page.locator("id=favorite-colors")
locator.select_option(["R", "G"])
expect(locator).to_have_values([re.compile(r"R"), re.compile(r"G")])
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `values` | Union[Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]], Sequence[str]] | Expected options currently selected. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

### 异步

```python signature
async def to_have_values(self, values: Union[Sequence[str], Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]]], *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_have_values

Ensures the `Locator` points to multi-select/combobox (i.e. a `select` with the `multiple` attribute) and the
specified values are selected.

**Usage**

For example, given the following element:

```html
<select id="favorite-colors" multiple>
  <option value="R">Red</option>
  <option value="G">Green</option>
  <option value="B">Blue</option>
</select>
```

```py
import re
from playwright.async_api import expect

locator = page.locator("id=favorite-colors")
await locator.select_option(["R", "G"])
await expect(locator).to_have_values([re.compile(r"R"), re.compile(r"G")])
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `values` | Union[Sequence[Pattern[str]], Sequence[Union[Pattern[str], str]], Sequence[str]] | Expected options currently selected. |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |

## to_match_aria_snapshot

### 同步

```python signature
def to_match_aria_snapshot(self, expected: str, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> None
```

LocatorAssertions.to_match_aria_snapshot

Asserts that the target element matches the given [accessibility snapshot](https://playwright.dev/python/docs/aria-snapshots).

**Usage**

```py
page.goto("https://demo.playwright.dev/todomvc/")
expect(page.locator('body')).to_match_aria_snapshot('''
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

LocatorAssertions.to_match_aria_snapshot

Asserts that the target element matches the given [accessibility snapshot](https://playwright.dev/python/docs/aria-snapshots).

**Usage**

```py
await page.goto("https://demo.playwright.dev/todomvc/")
await expect(page.locator('body')).to_match_aria_snapshot('''
  - heading "todos"
  - textbox "What needs to be done?"
''')
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expected` | str |  |
| `timeout` | Union[float, None] | Time to retry the assertion for in milliseconds. Defaults to `5000`. |
