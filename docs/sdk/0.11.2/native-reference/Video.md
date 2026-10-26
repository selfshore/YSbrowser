# 原生 Video

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [delete](#delete)
- [on](#on)
- [once](#once)
- [path](#path)
- [remove_listener](#remove_listener)
- [save_as](#save_as)

## delete

### 同步

```python
def delete(self) -> None
```

Video.delete

Deletes the video file. Will wait for the video to finish if necessary.

### 异步

```python
async def delete(self) -> None
```

Video.delete

Deletes the video file. Will wait for the video to finish if necessary.


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


## path

### 同步

```python
def path(self) -> pathlib.Path
```

Video.path

Returns the file system path this video will be recorded to. The video is guaranteed to be written to the
filesystem upon closing the browser context. This method throws when connected remotely.

#### Returns
pathlib.Path

### 异步

```python
async def path(self) -> pathlib.Path
```

Video.path

Returns the file system path this video will be recorded to. The video is guaranteed to be written to the
filesystem upon closing the browser context. This method throws when connected remotely.

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

Video.save_as

Saves the video to a user-specified path. It is safe to call this method while the video is still in progress, or
after the page has closed. This method waits until the page is closed and the video is fully saved.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `path` | Union[pathlib.Path, str] | Path where the video should be saved. |

### 异步

```python
async def save_as(self, path: Union[str, pathlib.Path]) -> None
```

Video.save_as

Saves the video to a user-specified path. It is safe to call this method while the video is still in progress, or
after the page has closed. This method waits until the page is closed and the video is fully saved.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `path` | Union[pathlib.Path, str] | Path where the video should be saved. |
