# 原生 Dialog

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [accept](#accept)
- [default_value](#default_value)
- [dismiss](#dismiss)
- [message](#message)
- [on](#on)
- [once](#once)
- [page](#page)
- [remove_listener](#remove_listener)
- [type](#type)

## accept

### 同步

```python
def accept(self, prompt_text: Optional[str] = None) -> None
```

Dialog.accept

Returns when the dialog has been accepted.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `prompt_text` | Union[str, None] | A text to enter in prompt. Does not cause any effects if the dialog's `type` is not prompt. Optional. |

### 异步

```python
async def accept(self, prompt_text: Optional[str] = None) -> None
```

Dialog.accept

Returns when the dialog has been accepted.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `prompt_text` | Union[str, None] | A text to enter in prompt. Does not cause any effects if the dialog's `type` is not prompt. Optional. |

## default_value

属性，直接读取；异步入口也不加 await。

```python signature
Dialog.default_value: <class 'str'>
```

Dialog.default_value

If dialog is prompt, returns default prompt value. Otherwise, returns empty string.

#### Returns
str


## dismiss

### 同步

```python
def dismiss(self) -> None
```

Dialog.dismiss

Returns when the dialog has been dismissed.

### 异步

```python
async def dismiss(self) -> None
```

Dialog.dismiss

Returns when the dialog has been dismissed.


## message

属性，直接读取；异步入口也不加 await。

```python signature
Dialog.message: <class 'str'>
```

Dialog.message

A message displayed in the dialog.

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


## page

属性，直接读取；异步入口也不加 await。

```python signature
Dialog.page: typing.Optional[ForwardRef('Page')]
```

Dialog.page

The page that initiated this dialog, if available.

#### Returns
Union[Page, None]


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


## type

属性，直接读取；异步入口也不加 await。

```python signature
Dialog.type: <class 'str'>
```

Dialog.type

Returns dialog's type, can be one of `alert`, `beforeunload`, `confirm` or `prompt`.

#### Returns
str
