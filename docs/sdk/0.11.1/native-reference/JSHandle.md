# 原生 JSHandle

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [as_element](#as_element)
- [dispose](#dispose)
- [evaluate](#evaluate)
- [evaluate_handle](#evaluate_handle)
- [get_properties](#get_properties)
- [get_property](#get_property)
- [json_value](#json_value)
- [on](#on)
- [once](#once)
- [remove_listener](#remove_listener)

## as_element

### 同步

```python
def as_element(self) -> Optional[ForwardRef('ElementHandle')]
```

JSHandle.as_element

Returns either `null` or the object handle itself, if the object handle is an instance of `ElementHandle`.

#### Returns
Union[ElementHandle, None]

### 异步

```python
def as_element(self) -> Optional[ForwardRef('ElementHandle')]
```

JSHandle.as_element

Returns either `null` or the object handle itself, if the object handle is an instance of `ElementHandle`.

#### Returns
Union[ElementHandle, None]


## dispose

### 同步

```python
def dispose(self) -> None
```

JSHandle.dispose

The `jsHandle.dispose` method stops referencing the element handle.

### 异步

```python
async def dispose(self) -> None
```

JSHandle.dispose

The `jsHandle.dispose` method stops referencing the element handle.


## evaluate

### 同步

```python signature
def evaluate(self, expression: str, arg: Optional[Any] = None, *, isolated_context: Optional[bool] = True) -> Any
```

JSHandle.evaluate

Returns the return value of `expression`.

This method passes this handle as the first argument to `expression`.

If `expression` returns a [Promise], then `handle.evaluate` would wait for the promise to resolve and return its
value.

**Usage**

```py
tweet_handle = page.query_selector(".tweet .retweets")
assert tweet_handle.evaluate("node => node.innerText") == "10 retweets"
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expression` | str | JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked. |
| `arg` | Union[Any, None] | Optional argument to pass to `expression`. |

#### Returns
Any

### 异步

```python signature
async def evaluate(self, expression: str, arg: Optional[Any] = None, *, isolated_context: Optional[bool] = True) -> Any
```

JSHandle.evaluate

Returns the return value of `expression`.

This method passes this handle as the first argument to `expression`.

If `expression` returns a [Promise], then `handle.evaluate` would wait for the promise to resolve and return its
value.

**Usage**

```py
tweet_handle = await page.query_selector(".tweet .retweets")
assert await tweet_handle.evaluate("node => node.innerText") == "10 retweets"
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expression` | str | JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked. |
| `arg` | Union[Any, None] | Optional argument to pass to `expression`. |

#### Returns
Any


## evaluate_handle

### 同步

```python signature
def evaluate_handle(self, expression: str, arg: Optional[Any] = None, *, isolated_context: Optional[bool] = True) -> 'JSHandle'
```

JSHandle.evaluate_handle

Returns the return value of `expression` as a `JSHandle`.

This method passes this handle as the first argument to `expression`.

The only difference between `jsHandle.evaluate` and `jsHandle.evaluateHandle` is that `jsHandle.evaluateHandle`
returns `JSHandle`.

If the function passed to the `jsHandle.evaluateHandle` returns a [Promise], then `jsHandle.evaluateHandle` would
wait for the promise to resolve and return its value.

See `page.evaluate_handle()` for more details.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expression` | str | JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked. |
| `arg` | Union[Any, None] | Optional argument to pass to `expression`. |

#### Returns
JSHandle

### 异步

```python signature
async def evaluate_handle(self, expression: str, arg: Optional[Any] = None, *, isolated_context: Optional[bool] = True) -> 'JSHandle'
```

JSHandle.evaluate_handle

Returns the return value of `expression` as a `JSHandle`.

This method passes this handle as the first argument to `expression`.

The only difference between `jsHandle.evaluate` and `jsHandle.evaluateHandle` is that `jsHandle.evaluateHandle`
returns `JSHandle`.

If the function passed to the `jsHandle.evaluateHandle` returns a [Promise], then `jsHandle.evaluateHandle` would
wait for the promise to resolve and return its value.

See `page.evaluate_handle()` for more details.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `expression` | str | JavaScript expression to be evaluated in the browser context. If the expression evaluates to a function, the function is automatically invoked. |
| `arg` | Union[Any, None] | Optional argument to pass to `expression`. |

#### Returns
JSHandle


## get_properties

### 同步

```python
def get_properties(self) -> Dict[str, ForwardRef('JSHandle')]
```

JSHandle.get_properties

The method returns a map with **own property names** as keys and JSHandle instances for the property values.

**Usage**

```py
handle = page.evaluate_handle("({ window, document })")
properties = handle.get_properties()
window_handle = properties.get("window")
document_handle = properties.get("document")
handle.dispose()
```

#### Returns
Dict[str, JSHandle]

### 异步

```python
async def get_properties(self) -> Dict[str, ForwardRef('JSHandle')]
```

JSHandle.get_properties

The method returns a map with **own property names** as keys and JSHandle instances for the property values.

**Usage**

```py
handle = await page.evaluate_handle("({ window, document })")
properties = await handle.get_properties()
window_handle = properties.get("window")
document_handle = properties.get("document")
await handle.dispose()
```

#### Returns
Dict[str, JSHandle]


## get_property

### 同步

```python
def get_property(self, property_name: str) -> 'JSHandle'
```

JSHandle.get_property

Fetches a single property from the referenced object.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `property_name` | str | property to get |

#### Returns
JSHandle

### 异步

```python
async def get_property(self, property_name: str) -> 'JSHandle'
```

JSHandle.get_property

Fetches a single property from the referenced object.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `property_name` | str | property to get |

#### Returns
JSHandle


## json_value

### 同步

```python
def json_value(self) -> Any
```

JSHandle.json_value

Returns a JSON representation of the object. If the object has a `toJSON` function, it **will not be called**.

**NOTE** The method will return an empty JSON object if the referenced object is not stringifiable. It will throw
an error if the object has circular references.

#### Returns
Any

### 异步

```python
async def json_value(self) -> Any
```

JSHandle.json_value

Returns a JSON representation of the object. If the object has a `toJSON` function, it **will not be called**.

**NOTE** The method will return an empty JSON object if the referenced object is not stringifiable. It will throw
an error if the object has circular references.

#### Returns
Any


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
