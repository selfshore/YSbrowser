# 原生 APIResponse

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [body](#body)
- [dispose](#dispose)
- [headers](#headers)
- [headers_array](#headers_array)
- [json](#json)
- [ok](#ok)
- [on](#on)
- [once](#once)
- [remove_listener](#remove_listener)
- [security_details](#security_details)
- [server_addr](#server_addr)
- [status](#status)
- [status_text](#status_text)
- [text](#text)
- [timing](#timing)
- [url](#url)

## body

### 同步

```python
def body(self) -> bytes
```

APIResponse.body

Returns the buffer with response body.

#### Returns
bytes

### 异步

```python
async def body(self) -> bytes
```

APIResponse.body

Returns the buffer with response body.

#### Returns
bytes


## dispose

### 同步

```python
def dispose(self) -> None
```

APIResponse.dispose

Disposes the body of this response. If not called then the body will stay in memory until the context closes.

### 异步

```python
async def dispose(self) -> None
```

APIResponse.dispose

Disposes the body of this response. If not called then the body will stay in memory until the context closes.


## headers

属性，直接读取；异步入口也不加 await。

```python signature
APIResponse.headers: typing.Dict[str, str]
```

APIResponse.headers

An object with all the response HTTP headers associated with this response.

#### Returns
Dict[str, str]


## headers_array

属性，直接读取；异步入口也不加 await。

```python signature
APIResponse.headers_array: typing.List[patchright._impl._api_structures.NameValue]
```

APIResponse.headers_array

An array with all the response HTTP headers associated with this response. Header names are not lower-cased.
Headers with multiple entries, such as `Set-Cookie`, appear in the array multiple times.

#### Returns
List[{name: str, value: str}]


## json

### 同步

```python
def json(self) -> Any
```

APIResponse.json

Returns the JSON representation of response body.

This method will throw if the response body is not parsable via `JSON.parse`.

#### Returns
Any

### 异步

```python
async def json(self) -> Any
```

APIResponse.json

Returns the JSON representation of response body.

This method will throw if the response body is not parsable via `JSON.parse`.

#### Returns
Any


## ok

属性，直接读取；异步入口也不加 await。

```python signature
APIResponse.ok: <class 'bool'>
```

APIResponse.ok

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


## security_details

### 同步

```python
def security_details(self) -> Optional[patchright._impl._api_structures.SecurityDetails]
```

APIResponse.security_details

Returns SSL and other security information. Resolves to `null` for non-HTTPS responses. For redirected requests,
returns the information for the last request in the redirect chain.

#### Returns
Union[{issuer: Union[str, None], protocol: Union[str, None], subjectName: Union[str, None], validFrom: Union[float, None], validTo: Union[float, None]}, None]

### 异步

```python
async def security_details(self) -> Optional[patchright._impl._api_structures.SecurityDetails]
```

APIResponse.security_details

Returns SSL and other security information. Resolves to `null` for non-HTTPS responses. For redirected requests,
returns the information for the last request in the redirect chain.

#### Returns
Union[{issuer: Union[str, None], protocol: Union[str, None], subjectName: Union[str, None], validFrom: Union[float, None], validTo: Union[float, None]}, None]


## server_addr

### 同步

```python
def server_addr(self) -> Optional[patchright._impl._api_structures.RemoteAddr]
```

APIResponse.server_addr

Returns the IP address and port of the server. Resolves to `null` if the server address is not available. For
redirected requests, returns the information for the last request in the redirect chain.

#### Returns
Union[{ipAddress: str, port: int}, None]

### 异步

```python
async def server_addr(self) -> Optional[patchright._impl._api_structures.RemoteAddr]
```

APIResponse.server_addr

Returns the IP address and port of the server. Resolves to `null` if the server address is not available. For
redirected requests, returns the information for the last request in the redirect chain.

#### Returns
Union[{ipAddress: str, port: int}, None]


## status

属性，直接读取；异步入口也不加 await。

```python signature
APIResponse.status: <class 'int'>
```

APIResponse.status

Contains the status code of the response (e.g., 200 for a success).

#### Returns
int


## status_text

属性，直接读取；异步入口也不加 await。

```python signature
APIResponse.status_text: <class 'str'>
```

APIResponse.status_text

Contains the status text of the response (e.g. usually an "OK" for a success).

#### Returns
str


## text

### 同步

```python
def text(self) -> str
```

APIResponse.text

Returns the text representation of response body.

#### Returns
str

### 异步

```python
async def text(self) -> str
```

APIResponse.text

Returns the text representation of response body.

#### Returns
str


## timing

属性，直接读取；异步入口也不加 await。

```python signature
APIResponse.timing: <class 'patchright._impl._api_structures.ResourceTiming'>
```

APIResponse.timing

Returns resource timing information for given response. For redirected requests, returns the information for the
last request in the redirect chain. When the response is served [from the HAR file](https://playwright.dev/python/docs/mock#replaying-from-har),
timing information is not available and all the values are -1. Find more information at
[Resource Timing API](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceResourceTiming).

#### Returns
{startTime: float, domainLookupStart: float, domainLookupEnd: float, connectStart: float, secureConnectionStart: float, connectEnd: float, requestStart: float, responseStart: float, responseEnd: float}


## url

属性，直接读取；异步入口也不加 await。

```python signature
APIResponse.url: <class 'str'>
```

APIResponse.url

Contains the URL of the response.

#### Returns
str
