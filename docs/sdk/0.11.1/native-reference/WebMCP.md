# 原生 WebMCP

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [call_tool](#call_tool)
- [on](#on)
- [once](#once)
- [remove_listener](#remove_listener)
- [tools](#tools)

## call_tool

### 同步

```python signature
def call_tool(self, name: str, input: Optional[Any] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Any
```

WebMCP.call_tool

Calls a tool registered by the frame and returns its result. The result is whatever the tool's `execute` function
resolved to, typically an object with a `content` array. A result with `isError: true` is returned as is. The
method throws when the tool is not registered or its `execute` function throws.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | Name of the tool, as reported by `web_mcp.tools()`. |
| `input` | Union[Any, None] | Input for the tool, matching its `inputSchema`. Defaults to an empty object. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
Any

### 异步

```python signature
async def call_tool(self, name: str, input: Optional[Any] = None, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> Any
```

WebMCP.call_tool

Calls a tool registered by the frame and returns its result. The result is whatever the tool's `execute` function
resolved to, typically an object with a `content` array. A result with `isError: true` is returned as is. The
method throws when the tool is not registered or its `execute` function throws.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | Name of the tool, as reported by `web_mcp.tools()`. |
| `input` | Union[Any, None] | Input for the tool, matching its `inputSchema`. Defaults to an empty object. |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

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


## tools

### 同步

```python signature
def tools(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> List[patchright._impl._api_structures.WebMCPTool]
```

WebMCP.tools

Returns the tools currently registered by the frame. Throws if the browser was launched without WebMCP support, see
the note above for the launch options that enable it.

`page.webmcp` covers the main frame only, child frames list their tools through their own `frame.webmcp`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
List[{name: str, description: str, inputSchema: Union[Any, None], annotations: Union[{readOnly: Union[bool, None], untrustedContent: Union[bool, None], consequential: Union[bool, None]}, None]}]

### 异步

```python signature
async def tools(self, *, timeout: Union[float, datetime.timedelta, NoneType] = None) -> List[patchright._impl._api_structures.WebMCPTool]
```

WebMCP.tools

Returns the tools currently registered by the frame. Throws if the browser was launched without WebMCP support, see
the note above for the launch options that enable it.

`page.webmcp` covers the main frame only, child frames list their tools through their own `frame.webmcp`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `timeout` | Union[float, None] | Maximum time in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. The default value can be changed by using the `browser_context.set_default_timeout()` or `page.set_default_timeout()` methods. |

#### Returns
List[{name: str, description: str, inputSchema: Union[Any, None], annotations: Union[{readOnly: Union[bool, None], untrustedContent: Union[bool, None], consequential: Union[bool, None]}, None]}]
