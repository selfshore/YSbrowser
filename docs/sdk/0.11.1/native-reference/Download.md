# 原生 Download

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [cancel](#cancel)
- [delete](#delete)
- [failure](#failure)
- [on](#on)
- [once](#once)
- [page](#page)
- [path](#path)
- [remove_listener](#remove_listener)
- [save_as](#save_as)
- [suggested_filename](#suggested_filename)
- [url](#url)

## cancel

### 同步

```python
def cancel(self) -> None
```

Download.cancel

Cancels a download. Will not fail if the download is already finished or canceled. Upon successful cancellations,
`download.failure()` would resolve to `'canceled'`.

### 异步

```python
async def cancel(self) -> None
```

Download.cancel

Cancels a download. Will not fail if the download is already finished or canceled. Upon successful cancellations,
`download.failure()` would resolve to `'canceled'`.


## delete

### 同步

```python
def delete(self) -> None
```

Download.delete

Deletes the downloaded file. Will wait for the download to finish if necessary.

### 异步

```python
async def delete(self) -> None
```

Download.delete

Deletes the downloaded file. Will wait for the download to finish if necessary.


## failure

### 同步

```python
def failure(self) -> Optional[str]
```

Download.failure

Returns download error if any. Will wait for the download to finish if necessary.

#### Returns
Union[str, None]

### 异步

```python
async def failure(self) -> Optional[str]
```

Download.failure

Returns download error if any. Will wait for the download to finish if necessary.

#### Returns
Union[str, None]


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


## page

属性，直接读取；异步入口也不加 await。

```python signature
Download.page: Page
```

Download.page

Get the page that the download belongs to.

#### Returns
Page


## path

### 同步

```python
def path(self) -> pathlib.Path
```

Download.path

Returns path to the downloaded file for a successful download, or throws for a failed/canceled download. The method
will wait for the download to finish if necessary. The method throws when connected remotely.

Note that the download's file name is a random GUID, use `download.suggested_filename` to get suggested file name.

#### Returns
pathlib.Path

### 异步

```python
async def path(self) -> pathlib.Path
```

Download.path

Returns path to the downloaded file for a successful download, or throws for a failed/canceled download. The method
will wait for the download to finish if necessary. The method throws when connected remotely.

Note that the download's file name is a random GUID, use `download.suggested_filename` to get suggested file name.

#### Returns
pathlib.Path


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


## save_as

### 同步

```python
def save_as(self, path: Union[str, pathlib.Path]) -> None
```

Download.save_as

Copy the download to a user-specified path. It is safe to call this method while the download is still in progress.
Will wait for the download to finish if necessary.

**Usage**

```py
download.save_as("/path/to/save/at/" + download.suggested_filename)
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `path` | Union[pathlib.Path, str] | Path where the download should be copied. |

### 异步

```python
async def save_as(self, path: Union[str, pathlib.Path]) -> None
```

Download.save_as

Copy the download to a user-specified path. It is safe to call this method while the download is still in progress.
Will wait for the download to finish if necessary.

**Usage**

```py
await download.save_as("/path/to/save/at/" + download.suggested_filename)
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `path` | Union[pathlib.Path, str] | Path where the download should be copied. |

## suggested_filename

属性，直接读取；异步入口也不加 await。

```python signature
Download.suggested_filename: <class 'str'>
```

Download.suggested_filename

Returns suggested filename for this download. It is typically computed by the browser from the
[`Content-Disposition`](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Content-Disposition) response
header or the `download` attribute. See the spec on [whatwg](https://html.spec.whatwg.org/#downloading-resources).
Different browsers can use different logic for computing it.

#### Returns
str


## url

属性，直接读取；异步入口也不加 await。

```python signature
Download.url: <class 'str'>
```

Download.url

Returns downloaded url.

#### Returns
str
