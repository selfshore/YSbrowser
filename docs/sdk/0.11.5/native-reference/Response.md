# 原生 Response

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [all_headers](#all_headers)
- [body](#body)
- [finished](#finished)
- [frame](#frame)
- [from_service_worker](#from_service_worker)
- [header_value](#header_value)
- [header_values](#header_values)
- [headers](#headers)
- [headers_array](#headers_array)
- [http_version](#http_version)
- [json](#json)
- [ok](#ok)
- [on](#on)
- [once](#once)
- [remove_listener](#remove_listener)
- [request](#request)
- [security_details](#security_details)
- [server_addr](#server_addr)
- [status](#status)
- [status_text](#status_text)
- [text](#text)
- [url](#url)

## all_headers

### 同步

```python
def all_headers(self) -> Dict[str, str]
```

Response.all_headers

An object with all the response HTTP headers associated with this response.

#### Returns
Dict[str, str]

### 异步

```python
async def all_headers(self) -> Dict[str, str]
```

Response.all_headers

An object with all the response HTTP headers associated with this response.

#### Returns
Dict[str, str]


## body

### 同步

```python
def body(self) -> bytes
```

Response.body

Returns the buffer with response body.

#### Returns
bytes

### 异步

```python
async def body(self) -> bytes
```

Response.body

Returns the buffer with response body.

#### Returns
bytes


## finished

### 同步

```python
def finished(self) -> None
```

Response.finished

Waits for this response to finish, returns always `null`.

### 异步

```python
async def finished(self) -> None
```

Response.finished

Waits for this response to finish, returns always `null`.


## frame

属性，直接读取；异步入口也不加 await。

```python signature
Response.frame: Frame
```

Response.frame

Returns the `Frame` that initiated this response.

#### Returns
Frame


## from_service_worker

属性，直接读取；异步入口也不加 await。

```python signature
Response.from_service_worker: <class 'bool'>
```

Response.from_service_worker

Indicates whether this Response was fulfilled by a Service Worker's Fetch Handler (i.e. via
[FetchEvent.respondWith](https://developer.mozilla.org/en-US/docs/Web/API/FetchEvent/respondWith)).

#### Returns
bool


## header_value

### 同步

```python
def header_value(self, name: str) -> Optional[str]
```

Response.header_value

Returns the value of the header matching the name. The name is case-insensitive. If multiple headers have the same
name (except `set-cookie`), they are returned as a list separated by `, `. For `set-cookie`, the `\n` separator is
used. If no headers are found, `null` is returned.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | Name of the header. |

#### Returns
Union[str, None]

### 异步

```python
async def header_value(self, name: str) -> Optional[str]
```

Response.header_value

Returns the value of the header matching the name. The name is case-insensitive. If multiple headers have the same
name (except `set-cookie`), they are returned as a list separated by `, `. For `set-cookie`, the `\n` separator is
used. If no headers are found, `null` is returned.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | Name of the header. |

#### Returns
Union[str, None]


## header_values

### 同步

```python
def header_values(self, name: str) -> List[str]
```

Response.header_values

Returns all values of the headers matching the name, for example `set-cookie`. The name is case-insensitive.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | Name of the header. |

#### Returns
List[str]

### 异步

```python
async def header_values(self, name: str) -> List[str]
```

Response.header_values

Returns all values of the headers matching the name, for example `set-cookie`. The name is case-insensitive.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | Name of the header. |

#### Returns
List[str]


## headers

属性，直接读取；异步入口也不加 await。

```python signature
Response.headers: typing.Dict[str, str]
```

Response.headers

An object with the response HTTP headers. The header names are lower-cased. Note that this method does not return
security-related headers, including cookie-related ones. You can use `response.all_headers()` for complete list of
headers that include `cookie` information.

#### Returns
Dict[str, str]


## headers_array

### 同步

```python
def headers_array(self) -> List[patchright._impl._api_structures.NameValue]
```

Response.headers_array

An array with all the response HTTP headers associated with this response. Unlike `response.all_headers()`, header
names are NOT lower-cased. Headers with multiple entries, such as `Set-Cookie`, appear in the array multiple times.
Some browser network stacks combine multiple field values before reporting them, so separate entries are not always
available.

#### Returns
List[{name: str, value: str}]

### 异步

```python
async def headers_array(self) -> List[patchright._impl._api_structures.NameValue]
```

Response.headers_array

An array with all the response HTTP headers associated with this response. Unlike `response.all_headers()`, header
names are NOT lower-cased. Headers with multiple entries, such as `Set-Cookie`, appear in the array multiple times.
Some browser network stacks combine multiple field values before reporting them, so separate entries are not always
available.

#### Returns
List[{name: str, value: str}]


## http_version

### 同步

```python
def http_version(self) -> str
```

Response.http_version

Returns the http version used by the response.

#### Returns
str

### 异步

```python
async def http_version(self) -> str
```

Response.http_version

Returns the http version used by the response.

#### Returns
str


## json

### 同步

```python
def json(self) -> Any
```

Response.json

Returns the JSON representation of response body.

This method will throw if the response body is not parsable via `JSON.parse`.

#### Returns
Any

### 异步

```python
async def json(self) -> Any
```

Response.json

Returns the JSON representation of response body.

This method will throw if the response body is not parsable via `JSON.parse`.

#### Returns
Any


## ok

属性，直接读取；异步入口也不加 await。

```python signature
Response.ok: <class 'bool'>
```

Response.ok

Contains a boolean stating whether the response was successful (status in the range 200-299) or not.

#### Returns
bool


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


## request

属性，直接读取；异步入口也不加 await。

```python signature
Response.request: Request
```

Response.request

Returns the matching `Request` object.

#### Returns
Request


## security_details

### 同步

```python
def security_details(self) -> Optional[patchright._impl._api_structures.SecurityDetails]
```

Response.security_details

Returns SSL and other security information.

#### Returns
Union[{issuer: Union[str, None], protocol: Union[str, None], subjectName: Union[str, None], validFrom: Union[float, None], validTo: Union[float, None]}, None]

### 异步

```python
async def security_details(self) -> Optional[patchright._impl._api_structures.SecurityDetails]
```

Response.security_details

Returns SSL and other security information.

#### Returns
Union[{issuer: Union[str, None], protocol: Union[str, None], subjectName: Union[str, None], validFrom: Union[float, None], validTo: Union[float, None]}, None]


## server_addr

### 同步

```python
def server_addr(self) -> Optional[patchright._impl._api_structures.RemoteAddr]
```

Response.server_addr

Returns the IP address and port of the server.

#### Returns
Union[{ipAddress: str, port: int}, None]

### 异步

```python
async def server_addr(self) -> Optional[patchright._impl._api_structures.RemoteAddr]
```

Response.server_addr

Returns the IP address and port of the server.

#### Returns
Union[{ipAddress: str, port: int}, None]


## status

属性，直接读取；异步入口也不加 await。

```python signature
Response.status: <class 'int'>
```

Response.status

Contains the status code of the response (e.g., 200 for a success).

#### Returns
int


## status_text

属性，直接读取；异步入口也不加 await。

```python signature
Response.status_text: <class 'str'>
```

Response.status_text

Contains the status text of the response (e.g. usually an "OK" for a success).

#### Returns
str


## text

### 同步

```python
def text(self) -> str
```

Response.text

Returns the text representation of response body.

#### Returns
str

### 异步

```python
async def text(self) -> str
```

Response.text

Returns the text representation of response body.

#### Returns
str


## url

属性，直接读取；异步入口也不加 await。

```python signature
Response.url: <class 'str'>
```

Response.url

Contains the URL of the response.

#### Returns
str
