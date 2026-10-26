# 原生 Expect

[原生 API 目录](README.md) · [手册目录](../README.md)

通过 `from patchright.sync_api import expect`（或 async_api）取得实例。`expect(actual)` 返回相应断言对象，`expect.set_options(timeout=...)` 设置默认断言超时。

## 方法与属性索引

- [__call__](#__call__)
- [set_options](#set_options)
- [soft](#soft)

## __call__

### 同步

```python
def __call__(self, actual: Union[patchright.sync_api._generated.Page, patchright.sync_api._generated.Locator, patchright.sync_api._generated.APIResponse], message: Optional[str] = None) -> Union[patchright.sync_api._generated.PageAssertions, patchright.sync_api._generated.LocatorAssertions, patchright.sync_api._generated.APIResponseAssertions]
```

支持的重载：

```python
def __call__(self, actual: patchright.sync_api._generated.Page, message: Optional[str] = None) -> patchright.sync_api._generated.PageAssertions
def __call__(self, actual: patchright.sync_api._generated.Locator, message: Optional[str] = None) -> patchright.sync_api._generated.LocatorAssertions
def __call__(self, actual: patchright.sync_api._generated.APIResponse, message: Optional[str] = None) -> patchright.sync_api._generated.APIResponseAssertions
```

Call self as a function.

### 异步

```python
def __call__(self, actual: Union[patchright.async_api._generated.Page, patchright.async_api._generated.Locator, patchright.async_api._generated.APIResponse], message: Optional[str] = None) -> Union[patchright.async_api._generated.PageAssertions, patchright.async_api._generated.LocatorAssertions, patchright.async_api._generated.APIResponseAssertions]
```

支持的重载：

```python
def __call__(self, actual: patchright.async_api._generated.Page, message: Optional[str] = None) -> patchright.async_api._generated.PageAssertions
def __call__(self, actual: patchright.async_api._generated.Locator, message: Optional[str] = None) -> patchright.async_api._generated.LocatorAssertions
def __call__(self, actual: patchright.async_api._generated.APIResponse, message: Optional[str] = None) -> patchright.async_api._generated.APIResponseAssertions
```

Call self as a function.


## set_options

### 同步

```python
def set_options(self, timeout: Optional[float] = <object object at 0x0000011701374C90>) -> None
```

This method sets global `expect()` options.

Args:
    timeout (float): Timeout value in milliseconds. Default to 5000 milliseconds.

Returns:
    None

### 异步

```python
def set_options(self, timeout: Optional[float] = <object object at 0x0000011701374A80>) -> None
```

This method sets global `expect()` options.

Args:
    timeout (float): Timeout value in milliseconds. Default to 5000 milliseconds.

Returns:
    None


## soft

### 同步

```python
def soft(self, actual: Union[patchright.sync_api._generated.Page, patchright.sync_api._generated.Locator, patchright.sync_api._generated.APIResponse], message: Optional[str] = None) -> Union[patchright.sync_api._generated.PageAssertions, patchright.sync_api._generated.LocatorAssertions, patchright.sync_api._generated.APIResponseAssertions]
```

支持的重载：

```python
def soft(self, actual: patchright.sync_api._generated.Page, message: Optional[str] = None) -> patchright.sync_api._generated.PageAssertions
def soft(self, actual: patchright.sync_api._generated.Locator, message: Optional[str] = None) -> patchright.sync_api._generated.LocatorAssertions
def soft(self, actual: patchright.sync_api._generated.APIResponse, message: Optional[str] = None) -> patchright.sync_api._generated.APIResponseAssertions
```

Creates a [soft assertion](https://playwright.dev/python/docs/test-assertions#soft-assertions).
Failing soft assertions do not abort test execution, but mark the test
as failed. Multiple failures from the same test are surfaced together
at the end of the test.

Requires the [pytest-playwright](https://pypi.org/project/pytest-playwright/)
plugin to establish the per-test scope that collects soft assertion
failures.

### 异步

```python
def soft(self, actual: Union[patchright.async_api._generated.Page, patchright.async_api._generated.Locator, patchright.async_api._generated.APIResponse], message: Optional[str] = None) -> Union[patchright.async_api._generated.PageAssertions, patchright.async_api._generated.LocatorAssertions, patchright.async_api._generated.APIResponseAssertions]
```

支持的重载：

```python
def soft(self, actual: patchright.async_api._generated.Page, message: Optional[str] = None) -> patchright.async_api._generated.PageAssertions
def soft(self, actual: patchright.async_api._generated.Locator, message: Optional[str] = None) -> patchright.async_api._generated.LocatorAssertions
def soft(self, actual: patchright.async_api._generated.APIResponse, message: Optional[str] = None) -> patchright.async_api._generated.APIResponseAssertions
```

Creates a [soft assertion](https://playwright.dev/python/docs/test-assertions#soft-assertions).
Failing soft assertions do not abort test execution, but mark the test
as failed. Multiple failures from the same test are surfaced together
at the end of the test.

Requires the [pytest-playwright](https://pypi.org/project/pytest-playwright/)
plugin to establish the per-test scope that collects soft assertion
failures.
