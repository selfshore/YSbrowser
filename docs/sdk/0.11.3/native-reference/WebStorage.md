# 原生 WebStorage

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [clear](#clear)
- [get_item](#get_item)
- [items](#items)
- [on](#on)
- [once](#once)
- [remove_item](#remove_item)
- [remove_listener](#remove_listener)
- [set_item](#set_item)

## clear

### 同步

```python
def clear(self) -> None
```

WebStorage.clear

Removes all items from the storage.

### 异步

```python
async def clear(self) -> None
```

WebStorage.clear

Removes all items from the storage.


## get_item

### 同步

```python
def get_item(self, name: str) -> Optional[str]
```

WebStorage.get_item

Returns the value for the given `name` if present.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | Name of the item to retrieve. |

#### Returns
Union[str, None]

### 异步

```python
async def get_item(self, name: str) -> Optional[str]
```

WebStorage.get_item

Returns the value for the given `name` if present.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | Name of the item to retrieve. |

#### Returns
Union[str, None]


## items

### 同步

```python
def items(self) -> List[patchright._impl._api_structures.NameValue]
```

WebStorage.items

Returns all items in the storage as name/value pairs.

#### Returns
List[{name: str, value: str}]

### 异步

```python
async def items(self) -> List[patchright._impl._api_structures.NameValue]
```

WebStorage.items

Returns all items in the storage as name/value pairs.

#### Returns
List[{name: str, value: str}]


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


## remove_item

### 同步

```python
def remove_item(self, name: str) -> None
```

WebStorage.remove_item

Removes the item with the given `name`. No-op if the item is absent.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | Name of the item to remove. |

### 异步

```python
async def remove_item(self, name: str) -> None
```

WebStorage.remove_item

Removes the item with the given `name`. No-op if the item is absent.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | Name of the item to remove. |

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


## set_item

### 同步

```python
def set_item(self, name: str, value: str) -> None
```

WebStorage.set_item

Sets the value for the given `name`. Overwrites any existing value for that name.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | Name of the item to set. |
| `value` | str | New value for the item. |

### 异步

```python
async def set_item(self, name: str, value: str) -> None
```

WebStorage.set_item

Sets the value for the given `name`. Overwrites any existing value for that name.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | Name of the item to set. |
| `value` | str | New value for the item. |
