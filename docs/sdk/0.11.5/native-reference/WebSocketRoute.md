# 原生 WebSocketRoute

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [close](#close)
- [connect_to_server](#connect_to_server)
- [on](#on)
- [on_close](#on_close)
- [on_message](#on_message)
- [once](#once)
- [protocols](#protocols)
- [remove_listener](#remove_listener)
- [send](#send)
- [url](#url)

## close

### 同步

```python signature
def close(self, *, code: Optional[int] = None, reason: Optional[str] = None) -> None
```

WebSocketRoute.close

Closes one side of the WebSocket connection.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `code` | Union[int, None] | Optional [close code](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket/close#code). |
| `reason` | Union[str, None] | Optional [close reason](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket/close#reason). |

### 异步

```python signature
async def close(self, *, code: Optional[int] = None, reason: Optional[str] = None) -> None
```

WebSocketRoute.close

Closes one side of the WebSocket connection.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `code` | Union[int, None] | Optional [close code](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket/close#code). |
| `reason` | Union[str, None] | Optional [close reason](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket/close#reason). |

## connect_to_server

### 同步

```python
def connect_to_server(self) -> 'WebSocketRoute'
```

WebSocketRoute.connect_to_server

By default, routed WebSocket does not connect to the server, so you can mock entire WebSocket communication. This
method connects to the actual WebSocket server, and returns the server-side `WebSocketRoute` instance, giving the
ability to send and receive messages from the server.

Once connected to the server:
- Messages received from the server will be **automatically forwarded** to the WebSocket in the page, unless
  `web_socket_route.on_message()` is called on the server-side `WebSocketRoute`.
- Messages sent by the [`WebSocket.send()`](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket/send) call
  in the page will be **automatically forwarded** to the server, unless `web_socket_route.on_message()` is called
  on the original `WebSocketRoute`.

See examples at the top for more details.

#### Returns
WebSocketRoute

### 异步

```python
def connect_to_server(self) -> 'WebSocketRoute'
```

WebSocketRoute.connect_to_server

By default, routed WebSocket does not connect to the server, so you can mock entire WebSocket communication. This
method connects to the actual WebSocket server, and returns the server-side `WebSocketRoute` instance, giving the
ability to send and receive messages from the server.

Once connected to the server:
- Messages received from the server will be **automatically forwarded** to the WebSocket in the page, unless
  `web_socket_route.on_message()` is called on the server-side `WebSocketRoute`.
- Messages sent by the [`WebSocket.send()`](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket/send) call
  in the page will be **automatically forwarded** to the server, unless `web_socket_route.on_message()` is called
  on the original `WebSocketRoute`.

See examples at the top for more details.

#### Returns
WebSocketRoute


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


## on_close

### 同步

```python
def on_close(self, handler: Callable[[Optional[int], Optional[str]], Any]) -> None
```

WebSocketRoute.on_close

Allows to handle [`WebSocket.close`](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket/close).

By default, closing one side of the connection, either in the page or on the server, will close the other side.
However, when `web_socket_route.on_close()` handler is set up, the default forwarding of closure is disabled, and
handler should take care of it.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `handler` | Callable[[Union[int, None], Union[str, None]], Any] | Function that will handle WebSocket closure. Received an optional [close code](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket/close#code) and an optional [close reason](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket/close#reason). |

### 异步

```python
def on_close(self, handler: Callable[[Optional[int], Optional[str]], Any]) -> None
```

WebSocketRoute.on_close

Allows to handle [`WebSocket.close`](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket/close).

By default, closing one side of the connection, either in the page or on the server, will close the other side.
However, when `web_socket_route.on_close()` handler is set up, the default forwarding of closure is disabled, and
handler should take care of it.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `handler` | Callable[[Union[int, None], Union[str, None]], Any] | Function that will handle WebSocket closure. Received an optional [close code](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket/close#code) and an optional [close reason](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket/close#reason). |

## on_message

### 同步

```python
def on_message(self, handler: Callable[[Union[str, bytes]], Any]) -> None
```

WebSocketRoute.on_message

This method allows to handle messages that are sent by the WebSocket, either from the page or from the server.

When called on the original WebSocket route, this method handles messages sent from the page. You can handle this
messages by responding to them with `web_socket_route.send()`, forwarding them to the server-side connection
returned by `web_socket_route.connect_to_server()` or do something else.

Once this method is called, messages are not automatically forwarded to the server or to the page - you should do
that manually by calling `web_socket_route.send()`. See examples at the top for more details.

Calling this method again will override the handler with a new one.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `handler` | Callable[[Union[bytes, str]], Any] | Function that will handle messages. |

### 异步

```python
def on_message(self, handler: Callable[[Union[str, bytes]], Any]) -> None
```

WebSocketRoute.on_message

This method allows to handle messages that are sent by the WebSocket, either from the page or from the server.

When called on the original WebSocket route, this method handles messages sent from the page. You can handle this
messages by responding to them with `web_socket_route.send()`, forwarding them to the server-side connection
returned by `web_socket_route.connect_to_server()` or do something else.

Once this method is called, messages are not automatically forwarded to the server or to the page - you should do
that manually by calling `web_socket_route.send()`. See examples at the top for more details.

Calling this method again will override the handler with a new one.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `handler` | Callable[[Union[bytes, str]], Any] | Function that will handle messages. |

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


## protocols

属性，直接读取；异步入口也不加 await。

```python signature
WebSocketRoute.protocols: typing.List[str]
```

WebSocketRoute.protocols

The list of WebSocket subprotocols requested by the page, as passed via the second argument to the
[`WebSocket` constructor](https://developer.mozilla.org/en-US/docs/Web/API/WebSocket/WebSocket). Corresponds to the
`Sec-WebSocket-Protocol` request header.

Returns an empty array if no protocols were specified.

**Usage**

```py
def handler(ws: WebSocketRoute):
  if "chat.v2" in ws.protocols:
    ws.on_message(lambda message: ws.send(f"v2:{message}"))
  else:
    ws.close(code=1002, reason="Unsupported protocol")

page.route_web_socket("wss://example.com/ws", handler)
```

#### Returns
List[str]


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


## send

### 同步

```python
def send(self, message: Union[str, bytes]) -> None
```

WebSocketRoute.send

Sends a message to the WebSocket. When called on the original WebSocket, sends the message to the page. When called
on the result of `web_socket_route.connect_to_server()`, sends the message to the server. See examples at the top
for more details.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `message` | Union[bytes, str] | Message to send. |

### 异步

```python
def send(self, message: Union[str, bytes]) -> None
```

WebSocketRoute.send

Sends a message to the WebSocket. When called on the original WebSocket, sends the message to the page. When called
on the result of `web_socket_route.connect_to_server()`, sends the message to the server. See examples at the top
for more details.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `message` | Union[bytes, str] | Message to send. |

## url

属性，直接读取；异步入口也不加 await。

```python signature
WebSocketRoute.url: <class 'str'>
```

WebSocketRoute.url

URL of the WebSocket created in the page.

#### Returns
str
