# 原生 APIRequestContext

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [add_cookies](#add_cookies)
- [clear_cookies](#clear_cookies)
- [cookies](#cookies)
- [delete](#delete)
- [dispose](#dispose)
- [fetch](#fetch)
- [get](#get)
- [head](#head)
- [on](#on)
- [once](#once)
- [patch](#patch)
- [post](#post)
- [put](#put)
- [remove_listener](#remove_listener)
- [storage_state](#storage_state)
- [tracing](#tracing)

## add_cookies

### 同步

```python
def add_cookies(self, cookies: Sequence[patchright._impl._api_structures.SetCookieParam]) -> None
```

APIRequestContext.add_cookies

Adds cookies into this request context. They will be sent with matching subsequent requests. For
`browser_context.request` and `page.request`, this is equivalent to calling `browser_context.add_cookies()` on the
corresponding browser context.

**Usage**

```py
request.add_cookies([cookie_object1, cookie_object2])
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `cookies` | Sequence[{name: str, value: str, url: Union[str, None], domain: Union[str, None], path: Union[str, None], expires: Union[float, None], httpOnly: Union[bool, None], secure: Union[bool, None], sameSite: Union["Lax", "None", "Strict", None], partitionKey: Union[str, None]}] |  |

### 异步

```python
async def add_cookies(self, cookies: Sequence[patchright._impl._api_structures.SetCookieParam]) -> None
```

APIRequestContext.add_cookies

Adds cookies into this request context. They will be sent with matching subsequent requests. For
`browser_context.request` and `page.request`, this is equivalent to calling `browser_context.add_cookies()` on the
corresponding browser context.

**Usage**

```py
await request.add_cookies([cookie_object1, cookie_object2])
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `cookies` | Sequence[{name: str, value: str, url: Union[str, None], domain: Union[str, None], path: Union[str, None], expires: Union[float, None], httpOnly: Union[bool, None], secure: Union[bool, None], sameSite: Union["Lax", "None", "Strict", None], partitionKey: Union[str, None]}] |  |

## clear_cookies

### 同步

```python signature
def clear_cookies(self, *, domain: Union[str, Pattern[str], NoneType] = None, name: Union[str, Pattern[str], NoneType] = None, path: Union[str, Pattern[str], NoneType] = None) -> None
```

APIRequestContext.clear_cookies

Removes cookies from this request context. Accepts optional filter. For `browser_context.request` and
`page.request`, this is equivalent to calling `browser_context.clear_cookies()` on the corresponding browser
context.

**Usage**

```py
request.clear_cookies()
request.clear_cookies(name="session-id")
request.clear_cookies(domain="my-origin.com")
request.clear_cookies(path="/api/v1")
request.clear_cookies(name="session-id", domain="my-origin.com")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `domain` | Union[Pattern[str], str, None] | Only removes cookies with the given domain. |
| `name` | Union[Pattern[str], str, None] | Only removes cookies with the given name. |
| `path` | Union[Pattern[str], str, None] | Only removes cookies with the given path. |

### 异步

```python signature
async def clear_cookies(self, *, domain: Union[str, Pattern[str], NoneType] = None, name: Union[str, Pattern[str], NoneType] = None, path: Union[str, Pattern[str], NoneType] = None) -> None
```

APIRequestContext.clear_cookies

Removes cookies from this request context. Accepts optional filter. For `browser_context.request` and
`page.request`, this is equivalent to calling `browser_context.clear_cookies()` on the corresponding browser
context.

**Usage**

```py
await request.clear_cookies()
await request.clear_cookies(name="session-id")
await request.clear_cookies(domain="my-origin.com")
await request.clear_cookies(path="/api/v1")
await request.clear_cookies(name="session-id", domain="my-origin.com")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `domain` | Union[Pattern[str], str, None] | Only removes cookies with the given domain. |
| `name` | Union[Pattern[str], str, None] | Only removes cookies with the given name. |
| `path` | Union[Pattern[str], str, None] | Only removes cookies with the given path. |

## cookies

### 同步

```python
def cookies(self, urls: Union[str, Sequence[str], NoneType] = None) -> List[patchright._impl._api_structures.Cookie]
```

APIRequestContext.cookies

If no URLs are specified, this method returns all cookies. If URLs are specified, only cookies that affect those
URLs are returned. For `browser_context.request` and `page.request`, this is equivalent to calling
`browser_context.cookies()` on the corresponding browser context.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `urls` | Union[Sequence[str], str, None] | Optional list of URLs. |

#### Returns
List[{name: str, value: str, domain: str, path: str, expires: float, httpOnly: bool, secure: bool, sameSite: Union["Lax", "None", "Strict"], partitionKey: Union[str, None]}]

### 异步

```python
async def cookies(self, urls: Union[str, Sequence[str], NoneType] = None) -> List[patchright._impl._api_structures.Cookie]
```

APIRequestContext.cookies

If no URLs are specified, this method returns all cookies. If URLs are specified, only cookies that affect those
URLs are returned. For `browser_context.request` and `page.request`, this is equivalent to calling
`browser_context.cookies()` on the corresponding browser context.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `urls` | Union[Sequence[str], str, None] | Optional list of URLs. |

#### Returns
List[{name: str, value: str, domain: str, path: str, expires: float, httpOnly: bool, secure: bool, sameSite: Union["Lax", "None", "Strict"], partitionKey: Union[str, None]}]


## delete

### 同步

```python signature
def delete(self, url: str, *, data: Union[str, bytes, Any, NoneType] = None, fail_on_status_code: Optional[bool] = None, form: Union[Dict[str, Union[str, float, bool]], ForwardRef('FormData'), NoneType] = None, headers: Optional[Dict[str, str]] = None, ignore_https_errors: Optional[bool] = None, max_redirects: Optional[int] = None, max_retries: Optional[int] = None, multipart: Union[Dict[str, Union[bytes, bool, float, str, patchright._impl._api_structures.FilePayload]], ForwardRef('FormData'), NoneType] = None, params: Union[Dict[str, Union[str, float, bool]], str, NoneType] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'APIResponse'
```

APIRequestContext.delete

Sends HTTP(S) [DELETE](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/DELETE) request and returns its
response. The method will populate request cookies from the context and update context cookies from the response.
The method will automatically follow redirects.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url` | str | Target URL. |
| `data` | Union[Any, bytes, str, None] | Allows to set post data of the request. If the data parameter is an object, it will be serialized to json string and `content-type` header will be set to `application/json` if not explicitly set. Otherwise the `content-type` header will be set to `application/octet-stream` if not explicitly set. |
| `fail_on_status_code` | Union[bool, None] | Whether to throw on response codes other than 2xx and 3xx. By default response object is returned for all status codes. |
| `form` | Union[Dict[str, Union[bool, float, str]], FormData, None] | Provides an object that will be serialized as html form using `application/x-www-form-urlencoded` encoding and sent as this request body. If this parameter is specified `content-type` header will be set to `application/x-www-form-urlencoded` unless explicitly provided. Use `FormData` to send multiple values for the same field. |
| `headers` | Union[Dict[str, str], None] | Allows to set HTTP headers. These headers will apply to the fetched request as well as any redirects initiated by it. |
| `ignore_https_errors` | Union[bool, None] | Whether to ignore HTTPS errors when sending network requests. Defaults to `false`. |
| `max_redirects` | Union[int, None] | Maximum number of request redirects that will be followed automatically. An error will be thrown if the number is exceeded. Defaults to `20`. Pass `0` to not follow redirects. |
| `max_retries` | Union[int, None] | Maximum number of times network errors should be retried. Currently only `ECONNRESET` error is retried. Does not retry based on HTTP response codes. An error will be thrown if the limit is exceeded. Defaults to `0` - no retries. |
| `multipart` | Union[Dict[str, Union[bool, bytes, float, str, {name: str, mimeType: str, buffer: bytes}]], FormData, None] | Provides an object that will be serialized as html form using `multipart/form-data` encoding and sent as this request body. If this parameter is specified `content-type` header will be set to `multipart/form-data` unless explicitly provided. File values can be passed as file-like object containing file name, mime-type and its content. Use `FormData` to send multiple files in the same field. |
| `params` | Union[Dict[str, Union[bool, float, str]], str, None] | Query parameters to be sent with the URL. |
| `timeout` | Union[float, None] | Request timeout in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. |

#### Returns
APIResponse

### 异步

```python signature
async def delete(self, url: str, *, data: Union[str, bytes, Any, NoneType] = None, fail_on_status_code: Optional[bool] = None, form: Union[Dict[str, Union[str, float, bool]], ForwardRef('FormData'), NoneType] = None, headers: Optional[Dict[str, str]] = None, ignore_https_errors: Optional[bool] = None, max_redirects: Optional[int] = None, max_retries: Optional[int] = None, multipart: Union[Dict[str, Union[bytes, bool, float, str, patchright._impl._api_structures.FilePayload]], ForwardRef('FormData'), NoneType] = None, params: Union[Dict[str, Union[str, float, bool]], str, NoneType] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'APIResponse'
```

APIRequestContext.delete

Sends HTTP(S) [DELETE](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/DELETE) request and returns its
response. The method will populate request cookies from the context and update context cookies from the response.
The method will automatically follow redirects.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url` | str | Target URL. |
| `data` | Union[Any, bytes, str, None] | Allows to set post data of the request. If the data parameter is an object, it will be serialized to json string and `content-type` header will be set to `application/json` if not explicitly set. Otherwise the `content-type` header will be set to `application/octet-stream` if not explicitly set. |
| `fail_on_status_code` | Union[bool, None] | Whether to throw on response codes other than 2xx and 3xx. By default response object is returned for all status codes. |
| `form` | Union[Dict[str, Union[bool, float, str]], FormData, None] | Provides an object that will be serialized as html form using `application/x-www-form-urlencoded` encoding and sent as this request body. If this parameter is specified `content-type` header will be set to `application/x-www-form-urlencoded` unless explicitly provided. Use `FormData` to send multiple values for the same field. |
| `headers` | Union[Dict[str, str], None] | Allows to set HTTP headers. These headers will apply to the fetched request as well as any redirects initiated by it. |
| `ignore_https_errors` | Union[bool, None] | Whether to ignore HTTPS errors when sending network requests. Defaults to `false`. |
| `max_redirects` | Union[int, None] | Maximum number of request redirects that will be followed automatically. An error will be thrown if the number is exceeded. Defaults to `20`. Pass `0` to not follow redirects. |
| `max_retries` | Union[int, None] | Maximum number of times network errors should be retried. Currently only `ECONNRESET` error is retried. Does not retry based on HTTP response codes. An error will be thrown if the limit is exceeded. Defaults to `0` - no retries. |
| `multipart` | Union[Dict[str, Union[bool, bytes, float, str, {name: str, mimeType: str, buffer: bytes}]], FormData, None] | Provides an object that will be serialized as html form using `multipart/form-data` encoding and sent as this request body. If this parameter is specified `content-type` header will be set to `multipart/form-data` unless explicitly provided. File values can be passed as file-like object containing file name, mime-type and its content. Use `FormData` to send multiple files in the same field. |
| `params` | Union[Dict[str, Union[bool, float, str]], str, None] | Query parameters to be sent with the URL. |
| `timeout` | Union[float, None] | Request timeout in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. |

#### Returns
APIResponse


## dispose

### 同步

```python signature
def dispose(self, *, reason: Optional[str] = None) -> None
```

APIRequestContext.dispose

All responses returned by `api_request_context.get()` and similar methods are stored in the memory, so that you can
later call `api_response.body()`.This method discards all its resources, calling any method on disposed
`APIRequestContext` will throw an exception.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `reason` | Union[str, None] | The reason to be reported to the operations interrupted by the context disposal. |

### 异步

```python signature
async def dispose(self, *, reason: Optional[str] = None) -> None
```

APIRequestContext.dispose

All responses returned by `api_request_context.get()` and similar methods are stored in the memory, so that you can
later call `api_response.body()`.This method discards all its resources, calling any method on disposed
`APIRequestContext` will throw an exception.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `reason` | Union[str, None] | The reason to be reported to the operations interrupted by the context disposal. |

## fetch

### 同步

```python signature
def fetch(self, url_or_request: Union[str, ForwardRef('Request')], *, data: Union[str, bytes, Any, NoneType] = None, fail_on_status_code: Optional[bool] = None, form: Union[Dict[str, Union[str, float, bool]], ForwardRef('FormData'), NoneType] = None, headers: Optional[Dict[str, str]] = None, ignore_https_errors: Optional[bool] = None, max_redirects: Optional[int] = None, max_retries: Optional[int] = None, method: Optional[str] = None, multipart: Union[Dict[str, Union[bytes, bool, float, str, patchright._impl._api_structures.FilePayload]], ForwardRef('FormData'), NoneType] = None, params: Union[Dict[str, Union[str, float, bool]], str, NoneType] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'APIResponse'
```

APIRequestContext.fetch

Sends HTTP(S) request and returns its response. The method will populate request cookies from the context and
update context cookies from the response. The method will automatically follow redirects.

**Usage**

JSON objects can be passed directly to the request:

```python
data = {
    "title": "Book Title",
    "body": "John Doe",
}
api_request_context.fetch("https://example.com/api/createBook", method="post", data=data)
```

The common way to send file(s) in the body of a request is to upload them as form fields with `multipart/form-data`
encoding, by specifiying the `multipart` parameter:

```python
api_request_context.fetch(
  "https://example.com/api/uploadScript",  method="post",
  multipart={
    "fileField": {
      "name": "f.js",
      "mimeType": "text/javascript",
      "buffer": b"console.log(2022);",
    },
  })
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url_or_request` | Union[Request, str] | Target URL or Request to get all parameters from. |
| `data` | Union[Any, bytes, str, None] | Allows to set post data of the request. If the data parameter is an object, it will be serialized to json string and `content-type` header will be set to `application/json` if not explicitly set. Otherwise the `content-type` header will be set to `application/octet-stream` if not explicitly set. |
| `fail_on_status_code` | Union[bool, None] | Whether to throw on response codes other than 2xx and 3xx. By default response object is returned for all status codes. |
| `form` | Union[Dict[str, Union[bool, float, str]], FormData, None] | Provides an object that will be serialized as html form using `application/x-www-form-urlencoded` encoding and sent as this request body. If this parameter is specified `content-type` header will be set to `application/x-www-form-urlencoded` unless explicitly provided. Use `FormData` to send multiple values for the same field. |
| `headers` | Union[Dict[str, str], None] | Allows to set HTTP headers. These headers will apply to the fetched request as well as any redirects initiated by it. |
| `ignore_https_errors` | Union[bool, None] | Whether to ignore HTTPS errors when sending network requests. Defaults to `false`. |
| `max_redirects` | Union[int, None] | Maximum number of request redirects that will be followed automatically. An error will be thrown if the number is exceeded. Defaults to `20`. Pass `0` to not follow redirects. |
| `max_retries` | Union[int, None] | Maximum number of times network errors should be retried. Currently only `ECONNRESET` error is retried. Does not retry based on HTTP response codes. An error will be thrown if the limit is exceeded. Defaults to `0` - no retries. |
| `method` | Union[str, None] | If set changes the fetch method (e.g. [PUT](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT) or [POST](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST)). If not specified, GET method is used. |
| `multipart` | Union[Dict[str, Union[bool, bytes, float, str, {name: str, mimeType: str, buffer: bytes}]], FormData, None] | Provides an object that will be serialized as html form using `multipart/form-data` encoding and sent as this request body. If this parameter is specified `content-type` header will be set to `multipart/form-data` unless explicitly provided. File values can be passed as file-like object containing file name, mime-type and its content. Use `FormData` to send multiple files in the same field. |
| `params` | Union[Dict[str, Union[bool, float, str]], str, None] | Query parameters to be sent with the URL. |
| `timeout` | Union[float, None] | Request timeout in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. |

#### Returns
APIResponse

### 异步

```python signature
async def fetch(self, url_or_request: Union[str, ForwardRef('Request')], *, data: Union[str, bytes, Any, NoneType] = None, fail_on_status_code: Optional[bool] = None, form: Union[Dict[str, Union[str, float, bool]], ForwardRef('FormData'), NoneType] = None, headers: Optional[Dict[str, str]] = None, ignore_https_errors: Optional[bool] = None, max_redirects: Optional[int] = None, max_retries: Optional[int] = None, method: Optional[str] = None, multipart: Union[Dict[str, Union[bytes, bool, float, str, patchright._impl._api_structures.FilePayload]], ForwardRef('FormData'), NoneType] = None, params: Union[Dict[str, Union[str, float, bool]], str, NoneType] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'APIResponse'
```

APIRequestContext.fetch

Sends HTTP(S) request and returns its response. The method will populate request cookies from the context and
update context cookies from the response. The method will automatically follow redirects.

**Usage**

JSON objects can be passed directly to the request:

```python
data = {
    "title": "Book Title",
    "body": "John Doe",
}
api_request_context.fetch("https://example.com/api/createBook", method="post", data=data)
```

The common way to send file(s) in the body of a request is to upload them as form fields with `multipart/form-data`
encoding, by specifiying the `multipart` parameter:

```python
api_request_context.fetch(
  "https://example.com/api/uploadScript",  method="post",
  multipart={
    "fileField": {
      "name": "f.js",
      "mimeType": "text/javascript",
      "buffer": b"console.log(2022);",
    },
  })
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url_or_request` | Union[Request, str] | Target URL or Request to get all parameters from. |
| `data` | Union[Any, bytes, str, None] | Allows to set post data of the request. If the data parameter is an object, it will be serialized to json string and `content-type` header will be set to `application/json` if not explicitly set. Otherwise the `content-type` header will be set to `application/octet-stream` if not explicitly set. |
| `fail_on_status_code` | Union[bool, None] | Whether to throw on response codes other than 2xx and 3xx. By default response object is returned for all status codes. |
| `form` | Union[Dict[str, Union[bool, float, str]], FormData, None] | Provides an object that will be serialized as html form using `application/x-www-form-urlencoded` encoding and sent as this request body. If this parameter is specified `content-type` header will be set to `application/x-www-form-urlencoded` unless explicitly provided. Use `FormData` to send multiple values for the same field. |
| `headers` | Union[Dict[str, str], None] | Allows to set HTTP headers. These headers will apply to the fetched request as well as any redirects initiated by it. |
| `ignore_https_errors` | Union[bool, None] | Whether to ignore HTTPS errors when sending network requests. Defaults to `false`. |
| `max_redirects` | Union[int, None] | Maximum number of request redirects that will be followed automatically. An error will be thrown if the number is exceeded. Defaults to `20`. Pass `0` to not follow redirects. |
| `max_retries` | Union[int, None] | Maximum number of times network errors should be retried. Currently only `ECONNRESET` error is retried. Does not retry based on HTTP response codes. An error will be thrown if the limit is exceeded. Defaults to `0` - no retries. |
| `method` | Union[str, None] | If set changes the fetch method (e.g. [PUT](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT) or [POST](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST)). If not specified, GET method is used. |
| `multipart` | Union[Dict[str, Union[bool, bytes, float, str, {name: str, mimeType: str, buffer: bytes}]], FormData, None] | Provides an object that will be serialized as html form using `multipart/form-data` encoding and sent as this request body. If this parameter is specified `content-type` header will be set to `multipart/form-data` unless explicitly provided. File values can be passed as file-like object containing file name, mime-type and its content. Use `FormData` to send multiple files in the same field. |
| `params` | Union[Dict[str, Union[bool, float, str]], str, None] | Query parameters to be sent with the URL. |
| `timeout` | Union[float, None] | Request timeout in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. |

#### Returns
APIResponse


## get

### 同步

```python signature
def get(self, url: str, *, data: Union[str, bytes, Any, NoneType] = None, fail_on_status_code: Optional[bool] = None, form: Union[Dict[str, Union[str, float, bool]], ForwardRef('FormData'), NoneType] = None, headers: Optional[Dict[str, str]] = None, ignore_https_errors: Optional[bool] = None, max_redirects: Optional[int] = None, max_retries: Optional[int] = None, multipart: Union[Dict[str, Union[bytes, bool, float, str, patchright._impl._api_structures.FilePayload]], ForwardRef('FormData'), NoneType] = None, params: Union[Dict[str, Union[str, float, bool]], str, NoneType] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'APIResponse'
```

APIRequestContext.get

Sends HTTP(S) [GET](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET) request and returns its
response. The method will populate request cookies from the context and update context cookies from the response.
The method will automatically follow redirects.

**Usage**

Request parameters can be configured with `params` option, they will be serialized into the URL search parameters:

```python
query_params = {
  "isbn": "1234",
  "page": "23"
}
api_request_context.get("https://example.com/api/getText", params=query_params)
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url` | str | Target URL. |
| `data` | Union[Any, bytes, str, None] | Allows to set post data of the request. If the data parameter is an object, it will be serialized to json string and `content-type` header will be set to `application/json` if not explicitly set. Otherwise the `content-type` header will be set to `application/octet-stream` if not explicitly set. |
| `fail_on_status_code` | Union[bool, None] | Whether to throw on response codes other than 2xx and 3xx. By default response object is returned for all status codes. |
| `form` | Union[Dict[str, Union[bool, float, str]], FormData, None] | Provides an object that will be serialized as html form using `application/x-www-form-urlencoded` encoding and sent as this request body. If this parameter is specified `content-type` header will be set to `application/x-www-form-urlencoded` unless explicitly provided. Use `FormData` to send multiple values for the same field. |
| `headers` | Union[Dict[str, str], None] | Allows to set HTTP headers. These headers will apply to the fetched request as well as any redirects initiated by it. |
| `ignore_https_errors` | Union[bool, None] | Whether to ignore HTTPS errors when sending network requests. Defaults to `false`. |
| `max_redirects` | Union[int, None] | Maximum number of request redirects that will be followed automatically. An error will be thrown if the number is exceeded. Defaults to `20`. Pass `0` to not follow redirects. |
| `max_retries` | Union[int, None] | Maximum number of times network errors should be retried. Currently only `ECONNRESET` error is retried. Does not retry based on HTTP response codes. An error will be thrown if the limit is exceeded. Defaults to `0` - no retries. |
| `multipart` | Union[Dict[str, Union[bool, bytes, float, str, {name: str, mimeType: str, buffer: bytes}]], FormData, None] | Provides an object that will be serialized as html form using `multipart/form-data` encoding and sent as this request body. If this parameter is specified `content-type` header will be set to `multipart/form-data` unless explicitly provided. File values can be passed as file-like object containing file name, mime-type and its content. Use `FormData` to send multiple files in the same field. |
| `params` | Union[Dict[str, Union[bool, float, str]], str, None] | Query parameters to be sent with the URL. |
| `timeout` | Union[float, None] | Request timeout in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. |

#### Returns
APIResponse

### 异步

```python signature
async def get(self, url: str, *, data: Union[str, bytes, Any, NoneType] = None, fail_on_status_code: Optional[bool] = None, form: Union[Dict[str, Union[str, float, bool]], ForwardRef('FormData'), NoneType] = None, headers: Optional[Dict[str, str]] = None, ignore_https_errors: Optional[bool] = None, max_redirects: Optional[int] = None, max_retries: Optional[int] = None, multipart: Union[Dict[str, Union[bytes, bool, float, str, patchright._impl._api_structures.FilePayload]], ForwardRef('FormData'), NoneType] = None, params: Union[Dict[str, Union[str, float, bool]], str, NoneType] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'APIResponse'
```

APIRequestContext.get

Sends HTTP(S) [GET](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/GET) request and returns its
response. The method will populate request cookies from the context and update context cookies from the response.
The method will automatically follow redirects.

**Usage**

Request parameters can be configured with `params` option, they will be serialized into the URL search parameters:

```python
query_params = {
  "isbn": "1234",
  "page": "23"
}
api_request_context.get("https://example.com/api/getText", params=query_params)
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url` | str | Target URL. |
| `data` | Union[Any, bytes, str, None] | Allows to set post data of the request. If the data parameter is an object, it will be serialized to json string and `content-type` header will be set to `application/json` if not explicitly set. Otherwise the `content-type` header will be set to `application/octet-stream` if not explicitly set. |
| `fail_on_status_code` | Union[bool, None] | Whether to throw on response codes other than 2xx and 3xx. By default response object is returned for all status codes. |
| `form` | Union[Dict[str, Union[bool, float, str]], FormData, None] | Provides an object that will be serialized as html form using `application/x-www-form-urlencoded` encoding and sent as this request body. If this parameter is specified `content-type` header will be set to `application/x-www-form-urlencoded` unless explicitly provided. Use `FormData` to send multiple values for the same field. |
| `headers` | Union[Dict[str, str], None] | Allows to set HTTP headers. These headers will apply to the fetched request as well as any redirects initiated by it. |
| `ignore_https_errors` | Union[bool, None] | Whether to ignore HTTPS errors when sending network requests. Defaults to `false`. |
| `max_redirects` | Union[int, None] | Maximum number of request redirects that will be followed automatically. An error will be thrown if the number is exceeded. Defaults to `20`. Pass `0` to not follow redirects. |
| `max_retries` | Union[int, None] | Maximum number of times network errors should be retried. Currently only `ECONNRESET` error is retried. Does not retry based on HTTP response codes. An error will be thrown if the limit is exceeded. Defaults to `0` - no retries. |
| `multipart` | Union[Dict[str, Union[bool, bytes, float, str, {name: str, mimeType: str, buffer: bytes}]], FormData, None] | Provides an object that will be serialized as html form using `multipart/form-data` encoding and sent as this request body. If this parameter is specified `content-type` header will be set to `multipart/form-data` unless explicitly provided. File values can be passed as file-like object containing file name, mime-type and its content. Use `FormData` to send multiple files in the same field. |
| `params` | Union[Dict[str, Union[bool, float, str]], str, None] | Query parameters to be sent with the URL. |
| `timeout` | Union[float, None] | Request timeout in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. |

#### Returns
APIResponse


## head

### 同步

```python signature
def head(self, url: str, *, data: Union[str, bytes, Any, NoneType] = None, fail_on_status_code: Optional[bool] = None, form: Union[Dict[str, Union[str, float, bool]], ForwardRef('FormData'), NoneType] = None, headers: Optional[Dict[str, str]] = None, ignore_https_errors: Optional[bool] = None, max_redirects: Optional[int] = None, max_retries: Optional[int] = None, multipart: Union[Dict[str, Union[bytes, bool, float, str, patchright._impl._api_structures.FilePayload]], ForwardRef('FormData'), NoneType] = None, params: Union[Dict[str, Union[str, float, bool]], str, NoneType] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'APIResponse'
```

APIRequestContext.head

Sends HTTP(S) [HEAD](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/HEAD) request and returns its
response. The method will populate request cookies from the context and update context cookies from the response.
The method will automatically follow redirects.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url` | str | Target URL. |
| `data` | Union[Any, bytes, str, None] | Allows to set post data of the request. If the data parameter is an object, it will be serialized to json string and `content-type` header will be set to `application/json` if not explicitly set. Otherwise the `content-type` header will be set to `application/octet-stream` if not explicitly set. |
| `fail_on_status_code` | Union[bool, None] | Whether to throw on response codes other than 2xx and 3xx. By default response object is returned for all status codes. |
| `form` | Union[Dict[str, Union[bool, float, str]], FormData, None] | Provides an object that will be serialized as html form using `application/x-www-form-urlencoded` encoding and sent as this request body. If this parameter is specified `content-type` header will be set to `application/x-www-form-urlencoded` unless explicitly provided. Use `FormData` to send multiple values for the same field. |
| `headers` | Union[Dict[str, str], None] | Allows to set HTTP headers. These headers will apply to the fetched request as well as any redirects initiated by it. |
| `ignore_https_errors` | Union[bool, None] | Whether to ignore HTTPS errors when sending network requests. Defaults to `false`. |
| `max_redirects` | Union[int, None] | Maximum number of request redirects that will be followed automatically. An error will be thrown if the number is exceeded. Defaults to `20`. Pass `0` to not follow redirects. |
| `max_retries` | Union[int, None] | Maximum number of times network errors should be retried. Currently only `ECONNRESET` error is retried. Does not retry based on HTTP response codes. An error will be thrown if the limit is exceeded. Defaults to `0` - no retries. |
| `multipart` | Union[Dict[str, Union[bool, bytes, float, str, {name: str, mimeType: str, buffer: bytes}]], FormData, None] | Provides an object that will be serialized as html form using `multipart/form-data` encoding and sent as this request body. If this parameter is specified `content-type` header will be set to `multipart/form-data` unless explicitly provided. File values can be passed as file-like object containing file name, mime-type and its content. Use `FormData` to send multiple files in the same field. |
| `params` | Union[Dict[str, Union[bool, float, str]], str, None] | Query parameters to be sent with the URL. |
| `timeout` | Union[float, None] | Request timeout in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. |

#### Returns
APIResponse

### 异步

```python signature
async def head(self, url: str, *, data: Union[str, bytes, Any, NoneType] = None, fail_on_status_code: Optional[bool] = None, form: Union[Dict[str, Union[str, float, bool]], ForwardRef('FormData'), NoneType] = None, headers: Optional[Dict[str, str]] = None, ignore_https_errors: Optional[bool] = None, max_redirects: Optional[int] = None, max_retries: Optional[int] = None, multipart: Union[Dict[str, Union[bytes, bool, float, str, patchright._impl._api_structures.FilePayload]], ForwardRef('FormData'), NoneType] = None, params: Union[Dict[str, Union[str, float, bool]], str, NoneType] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'APIResponse'
```

APIRequestContext.head

Sends HTTP(S) [HEAD](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/HEAD) request and returns its
response. The method will populate request cookies from the context and update context cookies from the response.
The method will automatically follow redirects.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url` | str | Target URL. |
| `data` | Union[Any, bytes, str, None] | Allows to set post data of the request. If the data parameter is an object, it will be serialized to json string and `content-type` header will be set to `application/json` if not explicitly set. Otherwise the `content-type` header will be set to `application/octet-stream` if not explicitly set. |
| `fail_on_status_code` | Union[bool, None] | Whether to throw on response codes other than 2xx and 3xx. By default response object is returned for all status codes. |
| `form` | Union[Dict[str, Union[bool, float, str]], FormData, None] | Provides an object that will be serialized as html form using `application/x-www-form-urlencoded` encoding and sent as this request body. If this parameter is specified `content-type` header will be set to `application/x-www-form-urlencoded` unless explicitly provided. Use `FormData` to send multiple values for the same field. |
| `headers` | Union[Dict[str, str], None] | Allows to set HTTP headers. These headers will apply to the fetched request as well as any redirects initiated by it. |
| `ignore_https_errors` | Union[bool, None] | Whether to ignore HTTPS errors when sending network requests. Defaults to `false`. |
| `max_redirects` | Union[int, None] | Maximum number of request redirects that will be followed automatically. An error will be thrown if the number is exceeded. Defaults to `20`. Pass `0` to not follow redirects. |
| `max_retries` | Union[int, None] | Maximum number of times network errors should be retried. Currently only `ECONNRESET` error is retried. Does not retry based on HTTP response codes. An error will be thrown if the limit is exceeded. Defaults to `0` - no retries. |
| `multipart` | Union[Dict[str, Union[bool, bytes, float, str, {name: str, mimeType: str, buffer: bytes}]], FormData, None] | Provides an object that will be serialized as html form using `multipart/form-data` encoding and sent as this request body. If this parameter is specified `content-type` header will be set to `multipart/form-data` unless explicitly provided. File values can be passed as file-like object containing file name, mime-type and its content. Use `FormData` to send multiple files in the same field. |
| `params` | Union[Dict[str, Union[bool, float, str]], str, None] | Query parameters to be sent with the URL. |
| `timeout` | Union[float, None] | Request timeout in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. |

#### Returns
APIResponse


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


## patch

### 同步

```python signature
def patch(self, url: str, *, data: Union[str, bytes, Any, NoneType] = None, fail_on_status_code: Optional[bool] = None, form: Union[Dict[str, Union[str, float, bool]], ForwardRef('FormData'), NoneType] = None, headers: Optional[Dict[str, str]] = None, ignore_https_errors: Optional[bool] = None, max_redirects: Optional[int] = None, max_retries: Optional[int] = None, multipart: Union[Dict[str, Union[bytes, bool, float, str, patchright._impl._api_structures.FilePayload]], ForwardRef('FormData'), NoneType] = None, params: Union[Dict[str, Union[str, float, bool]], str, NoneType] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'APIResponse'
```

APIRequestContext.patch

Sends HTTP(S) [PATCH](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PATCH) request and returns its
response. The method will populate request cookies from the context and update context cookies from the response.
The method will automatically follow redirects.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url` | str | Target URL. |
| `data` | Union[Any, bytes, str, None] | Allows to set post data of the request. If the data parameter is an object, it will be serialized to json string and `content-type` header will be set to `application/json` if not explicitly set. Otherwise the `content-type` header will be set to `application/octet-stream` if not explicitly set. |
| `fail_on_status_code` | Union[bool, None] | Whether to throw on response codes other than 2xx and 3xx. By default response object is returned for all status codes. |
| `form` | Union[Dict[str, Union[bool, float, str]], FormData, None] | Provides an object that will be serialized as html form using `application/x-www-form-urlencoded` encoding and sent as this request body. If this parameter is specified `content-type` header will be set to `application/x-www-form-urlencoded` unless explicitly provided. Use `FormData` to send multiple values for the same field. |
| `headers` | Union[Dict[str, str], None] | Allows to set HTTP headers. These headers will apply to the fetched request as well as any redirects initiated by it. |
| `ignore_https_errors` | Union[bool, None] | Whether to ignore HTTPS errors when sending network requests. Defaults to `false`. |
| `max_redirects` | Union[int, None] | Maximum number of request redirects that will be followed automatically. An error will be thrown if the number is exceeded. Defaults to `20`. Pass `0` to not follow redirects. |
| `max_retries` | Union[int, None] | Maximum number of times network errors should be retried. Currently only `ECONNRESET` error is retried. Does not retry based on HTTP response codes. An error will be thrown if the limit is exceeded. Defaults to `0` - no retries. |
| `multipart` | Union[Dict[str, Union[bool, bytes, float, str, {name: str, mimeType: str, buffer: bytes}]], FormData, None] | Provides an object that will be serialized as html form using `multipart/form-data` encoding and sent as this request body. If this parameter is specified `content-type` header will be set to `multipart/form-data` unless explicitly provided. File values can be passed as file-like object containing file name, mime-type and its content. Use `FormData` to send multiple files in the same field. |
| `params` | Union[Dict[str, Union[bool, float, str]], str, None] | Query parameters to be sent with the URL. |
| `timeout` | Union[float, None] | Request timeout in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. |

#### Returns
APIResponse

### 异步

```python signature
async def patch(self, url: str, *, data: Union[str, bytes, Any, NoneType] = None, fail_on_status_code: Optional[bool] = None, form: Union[Dict[str, Union[str, float, bool]], ForwardRef('FormData'), NoneType] = None, headers: Optional[Dict[str, str]] = None, ignore_https_errors: Optional[bool] = None, max_redirects: Optional[int] = None, max_retries: Optional[int] = None, multipart: Union[Dict[str, Union[bytes, bool, float, str, patchright._impl._api_structures.FilePayload]], ForwardRef('FormData'), NoneType] = None, params: Union[Dict[str, Union[str, float, bool]], str, NoneType] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'APIResponse'
```

APIRequestContext.patch

Sends HTTP(S) [PATCH](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PATCH) request and returns its
response. The method will populate request cookies from the context and update context cookies from the response.
The method will automatically follow redirects.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url` | str | Target URL. |
| `data` | Union[Any, bytes, str, None] | Allows to set post data of the request. If the data parameter is an object, it will be serialized to json string and `content-type` header will be set to `application/json` if not explicitly set. Otherwise the `content-type` header will be set to `application/octet-stream` if not explicitly set. |
| `fail_on_status_code` | Union[bool, None] | Whether to throw on response codes other than 2xx and 3xx. By default response object is returned for all status codes. |
| `form` | Union[Dict[str, Union[bool, float, str]], FormData, None] | Provides an object that will be serialized as html form using `application/x-www-form-urlencoded` encoding and sent as this request body. If this parameter is specified `content-type` header will be set to `application/x-www-form-urlencoded` unless explicitly provided. Use `FormData` to send multiple values for the same field. |
| `headers` | Union[Dict[str, str], None] | Allows to set HTTP headers. These headers will apply to the fetched request as well as any redirects initiated by it. |
| `ignore_https_errors` | Union[bool, None] | Whether to ignore HTTPS errors when sending network requests. Defaults to `false`. |
| `max_redirects` | Union[int, None] | Maximum number of request redirects that will be followed automatically. An error will be thrown if the number is exceeded. Defaults to `20`. Pass `0` to not follow redirects. |
| `max_retries` | Union[int, None] | Maximum number of times network errors should be retried. Currently only `ECONNRESET` error is retried. Does not retry based on HTTP response codes. An error will be thrown if the limit is exceeded. Defaults to `0` - no retries. |
| `multipart` | Union[Dict[str, Union[bool, bytes, float, str, {name: str, mimeType: str, buffer: bytes}]], FormData, None] | Provides an object that will be serialized as html form using `multipart/form-data` encoding and sent as this request body. If this parameter is specified `content-type` header will be set to `multipart/form-data` unless explicitly provided. File values can be passed as file-like object containing file name, mime-type and its content. Use `FormData` to send multiple files in the same field. |
| `params` | Union[Dict[str, Union[bool, float, str]], str, None] | Query parameters to be sent with the URL. |
| `timeout` | Union[float, None] | Request timeout in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. |

#### Returns
APIResponse


## post

### 同步

```python signature
def post(self, url: str, *, data: Union[str, bytes, Any, NoneType] = None, fail_on_status_code: Optional[bool] = None, form: Union[Dict[str, Union[str, float, bool]], ForwardRef('FormData'), NoneType] = None, headers: Optional[Dict[str, str]] = None, ignore_https_errors: Optional[bool] = None, max_redirects: Optional[int] = None, max_retries: Optional[int] = None, multipart: Union[Dict[str, Union[bytes, bool, float, str, patchright._impl._api_structures.FilePayload]], ForwardRef('FormData'), NoneType] = None, params: Union[Dict[str, Union[str, float, bool]], str, NoneType] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'APIResponse'
```

APIRequestContext.post

Sends HTTP(S) [POST](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST) request and returns its
response. The method will populate request cookies from the context and update context cookies from the response.
The method will automatically follow redirects.

**Usage**

JSON objects can be passed directly to the request:

```python
data = {
    "title": "Book Title",
    "body": "John Doe",
}
api_request_context.post("https://example.com/api/createBook", data=data)
```

To send form data to the server use `form` option. Its value will be encoded into the request body with
`application/x-www-form-urlencoded` encoding (see below how to use `multipart/form-data` form encoding to send
files):

```python
formData = {
    "title": "Book Title",
    "body": "John Doe",
}
api_request_context.post("https://example.com/api/findBook", form=formData)
```

The common way to send file(s) in the body of a request is to upload them as form fields with `multipart/form-data`
encoding. Use `FormData` to construct request body and pass it to the request as `multipart` parameter:

```python
api_request_context.post(
  "https://example.com/api/uploadScript'",
  multipart={
    "fileField": {
      "name": "f.js",
      "mimeType": "text/javascript",
      "buffer": b"console.log(2022);",
    },
  })
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url` | str | Target URL. |
| `data` | Union[Any, bytes, str, None] | Allows to set post data of the request. If the data parameter is an object, it will be serialized to json string and `content-type` header will be set to `application/json` if not explicitly set. Otherwise the `content-type` header will be set to `application/octet-stream` if not explicitly set. |
| `fail_on_status_code` | Union[bool, None] | Whether to throw on response codes other than 2xx and 3xx. By default response object is returned for all status codes. |
| `form` | Union[Dict[str, Union[bool, float, str]], FormData, None] | Provides an object that will be serialized as html form using `application/x-www-form-urlencoded` encoding and sent as this request body. If this parameter is specified `content-type` header will be set to `application/x-www-form-urlencoded` unless explicitly provided. Use `FormData` to send multiple values for the same field. |
| `headers` | Union[Dict[str, str], None] | Allows to set HTTP headers. These headers will apply to the fetched request as well as any redirects initiated by it. |
| `ignore_https_errors` | Union[bool, None] | Whether to ignore HTTPS errors when sending network requests. Defaults to `false`. |
| `max_redirects` | Union[int, None] | Maximum number of request redirects that will be followed automatically. An error will be thrown if the number is exceeded. Defaults to `20`. Pass `0` to not follow redirects. |
| `max_retries` | Union[int, None] | Maximum number of times network errors should be retried. Currently only `ECONNRESET` error is retried. Does not retry based on HTTP response codes. An error will be thrown if the limit is exceeded. Defaults to `0` - no retries. |
| `multipart` | Union[Dict[str, Union[bool, bytes, float, str, {name: str, mimeType: str, buffer: bytes}]], FormData, None] | Provides an object that will be serialized as html form using `multipart/form-data` encoding and sent as this request body. If this parameter is specified `content-type` header will be set to `multipart/form-data` unless explicitly provided. File values can be passed as file-like object containing file name, mime-type and its content. Use `FormData` to send multiple files in the same field. |
| `params` | Union[Dict[str, Union[bool, float, str]], str, None] | Query parameters to be sent with the URL. |
| `timeout` | Union[float, None] | Request timeout in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. |

#### Returns
APIResponse

### 异步

```python signature
async def post(self, url: str, *, data: Union[str, bytes, Any, NoneType] = None, fail_on_status_code: Optional[bool] = None, form: Union[Dict[str, Union[str, float, bool]], ForwardRef('FormData'), NoneType] = None, headers: Optional[Dict[str, str]] = None, ignore_https_errors: Optional[bool] = None, max_redirects: Optional[int] = None, max_retries: Optional[int] = None, multipart: Union[Dict[str, Union[bytes, bool, float, str, patchright._impl._api_structures.FilePayload]], ForwardRef('FormData'), NoneType] = None, params: Union[Dict[str, Union[str, float, bool]], str, NoneType] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'APIResponse'
```

APIRequestContext.post

Sends HTTP(S) [POST](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/POST) request and returns its
response. The method will populate request cookies from the context and update context cookies from the response.
The method will automatically follow redirects.

**Usage**

JSON objects can be passed directly to the request:

```python
data = {
    "title": "Book Title",
    "body": "John Doe",
}
api_request_context.post("https://example.com/api/createBook", data=data)
```

To send form data to the server use `form` option. Its value will be encoded into the request body with
`application/x-www-form-urlencoded` encoding (see below how to use `multipart/form-data` form encoding to send
files):

```python
formData = {
    "title": "Book Title",
    "body": "John Doe",
}
api_request_context.post("https://example.com/api/findBook", form=formData)
```

The common way to send file(s) in the body of a request is to upload them as form fields with `multipart/form-data`
encoding. Use `FormData` to construct request body and pass it to the request as `multipart` parameter:

```python
api_request_context.post(
  "https://example.com/api/uploadScript'",
  multipart={
    "fileField": {
      "name": "f.js",
      "mimeType": "text/javascript",
      "buffer": b"console.log(2022);",
    },
  })
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url` | str | Target URL. |
| `data` | Union[Any, bytes, str, None] | Allows to set post data of the request. If the data parameter is an object, it will be serialized to json string and `content-type` header will be set to `application/json` if not explicitly set. Otherwise the `content-type` header will be set to `application/octet-stream` if not explicitly set. |
| `fail_on_status_code` | Union[bool, None] | Whether to throw on response codes other than 2xx and 3xx. By default response object is returned for all status codes. |
| `form` | Union[Dict[str, Union[bool, float, str]], FormData, None] | Provides an object that will be serialized as html form using `application/x-www-form-urlencoded` encoding and sent as this request body. If this parameter is specified `content-type` header will be set to `application/x-www-form-urlencoded` unless explicitly provided. Use `FormData` to send multiple values for the same field. |
| `headers` | Union[Dict[str, str], None] | Allows to set HTTP headers. These headers will apply to the fetched request as well as any redirects initiated by it. |
| `ignore_https_errors` | Union[bool, None] | Whether to ignore HTTPS errors when sending network requests. Defaults to `false`. |
| `max_redirects` | Union[int, None] | Maximum number of request redirects that will be followed automatically. An error will be thrown if the number is exceeded. Defaults to `20`. Pass `0` to not follow redirects. |
| `max_retries` | Union[int, None] | Maximum number of times network errors should be retried. Currently only `ECONNRESET` error is retried. Does not retry based on HTTP response codes. An error will be thrown if the limit is exceeded. Defaults to `0` - no retries. |
| `multipart` | Union[Dict[str, Union[bool, bytes, float, str, {name: str, mimeType: str, buffer: bytes}]], FormData, None] | Provides an object that will be serialized as html form using `multipart/form-data` encoding and sent as this request body. If this parameter is specified `content-type` header will be set to `multipart/form-data` unless explicitly provided. File values can be passed as file-like object containing file name, mime-type and its content. Use `FormData` to send multiple files in the same field. |
| `params` | Union[Dict[str, Union[bool, float, str]], str, None] | Query parameters to be sent with the URL. |
| `timeout` | Union[float, None] | Request timeout in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. |

#### Returns
APIResponse


## put

### 同步

```python signature
def put(self, url: str, *, data: Union[str, bytes, Any, NoneType] = None, fail_on_status_code: Optional[bool] = None, form: Union[Dict[str, Union[str, float, bool]], ForwardRef('FormData'), NoneType] = None, headers: Optional[Dict[str, str]] = None, ignore_https_errors: Optional[bool] = None, max_redirects: Optional[int] = None, max_retries: Optional[int] = None, multipart: Union[Dict[str, Union[bytes, bool, float, str, patchright._impl._api_structures.FilePayload]], ForwardRef('FormData'), NoneType] = None, params: Union[Dict[str, Union[str, float, bool]], str, NoneType] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'APIResponse'
```

APIRequestContext.put

Sends HTTP(S) [PUT](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT) request and returns its
response. The method will populate request cookies from the context and update context cookies from the response.
The method will automatically follow redirects.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url` | str | Target URL. |
| `data` | Union[Any, bytes, str, None] | Allows to set post data of the request. If the data parameter is an object, it will be serialized to json string and `content-type` header will be set to `application/json` if not explicitly set. Otherwise the `content-type` header will be set to `application/octet-stream` if not explicitly set. |
| `fail_on_status_code` | Union[bool, None] | Whether to throw on response codes other than 2xx and 3xx. By default response object is returned for all status codes. |
| `form` | Union[Dict[str, Union[bool, float, str]], FormData, None] | Provides an object that will be serialized as html form using `application/x-www-form-urlencoded` encoding and sent as this request body. If this parameter is specified `content-type` header will be set to `application/x-www-form-urlencoded` unless explicitly provided. Use `FormData` to send multiple values for the same field. |
| `headers` | Union[Dict[str, str], None] | Allows to set HTTP headers. These headers will apply to the fetched request as well as any redirects initiated by it. |
| `ignore_https_errors` | Union[bool, None] | Whether to ignore HTTPS errors when sending network requests. Defaults to `false`. |
| `max_redirects` | Union[int, None] | Maximum number of request redirects that will be followed automatically. An error will be thrown if the number is exceeded. Defaults to `20`. Pass `0` to not follow redirects. |
| `max_retries` | Union[int, None] | Maximum number of times network errors should be retried. Currently only `ECONNRESET` error is retried. Does not retry based on HTTP response codes. An error will be thrown if the limit is exceeded. Defaults to `0` - no retries. |
| `multipart` | Union[Dict[str, Union[bool, bytes, float, str, {name: str, mimeType: str, buffer: bytes}]], FormData, None] | Provides an object that will be serialized as html form using `multipart/form-data` encoding and sent as this request body. If this parameter is specified `content-type` header will be set to `multipart/form-data` unless explicitly provided. File values can be passed as file-like object containing file name, mime-type and its content. Use `FormData` to send multiple files in the same field. |
| `params` | Union[Dict[str, Union[bool, float, str]], str, None] | Query parameters to be sent with the URL. |
| `timeout` | Union[float, None] | Request timeout in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. |

#### Returns
APIResponse

### 异步

```python signature
async def put(self, url: str, *, data: Union[str, bytes, Any, NoneType] = None, fail_on_status_code: Optional[bool] = None, form: Union[Dict[str, Union[str, float, bool]], ForwardRef('FormData'), NoneType] = None, headers: Optional[Dict[str, str]] = None, ignore_https_errors: Optional[bool] = None, max_redirects: Optional[int] = None, max_retries: Optional[int] = None, multipart: Union[Dict[str, Union[bytes, bool, float, str, patchright._impl._api_structures.FilePayload]], ForwardRef('FormData'), NoneType] = None, params: Union[Dict[str, Union[str, float, bool]], str, NoneType] = None, timeout: Union[float, datetime.timedelta, NoneType] = None) -> 'APIResponse'
```

APIRequestContext.put

Sends HTTP(S) [PUT](https://developer.mozilla.org/en-US/docs/Web/HTTP/Methods/PUT) request and returns its
response. The method will populate request cookies from the context and update context cookies from the response.
The method will automatically follow redirects.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `url` | str | Target URL. |
| `data` | Union[Any, bytes, str, None] | Allows to set post data of the request. If the data parameter is an object, it will be serialized to json string and `content-type` header will be set to `application/json` if not explicitly set. Otherwise the `content-type` header will be set to `application/octet-stream` if not explicitly set. |
| `fail_on_status_code` | Union[bool, None] | Whether to throw on response codes other than 2xx and 3xx. By default response object is returned for all status codes. |
| `form` | Union[Dict[str, Union[bool, float, str]], FormData, None] | Provides an object that will be serialized as html form using `application/x-www-form-urlencoded` encoding and sent as this request body. If this parameter is specified `content-type` header will be set to `application/x-www-form-urlencoded` unless explicitly provided. Use `FormData` to send multiple values for the same field. |
| `headers` | Union[Dict[str, str], None] | Allows to set HTTP headers. These headers will apply to the fetched request as well as any redirects initiated by it. |
| `ignore_https_errors` | Union[bool, None] | Whether to ignore HTTPS errors when sending network requests. Defaults to `false`. |
| `max_redirects` | Union[int, None] | Maximum number of request redirects that will be followed automatically. An error will be thrown if the number is exceeded. Defaults to `20`. Pass `0` to not follow redirects. |
| `max_retries` | Union[int, None] | Maximum number of times network errors should be retried. Currently only `ECONNRESET` error is retried. Does not retry based on HTTP response codes. An error will be thrown if the limit is exceeded. Defaults to `0` - no retries. |
| `multipart` | Union[Dict[str, Union[bool, bytes, float, str, {name: str, mimeType: str, buffer: bytes}]], FormData, None] | Provides an object that will be serialized as html form using `multipart/form-data` encoding and sent as this request body. If this parameter is specified `content-type` header will be set to `multipart/form-data` unless explicitly provided. File values can be passed as file-like object containing file name, mime-type and its content. Use `FormData` to send multiple files in the same field. |
| `params` | Union[Dict[str, Union[bool, float, str]], str, None] | Query parameters to be sent with the URL. |
| `timeout` | Union[float, None] | Request timeout in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. |

#### Returns
APIResponse


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


## storage_state

### 同步

```python signature
def storage_state(self, *, indexed_db: Optional[bool] = None, opfs: Optional[bool] = None, path: Union[pathlib.Path, str, NoneType] = None) -> patchright._impl._api_structures.StorageState
```

APIRequestContext.storage_state

Returns storage state for this request context, contains current cookies and local storage snapshot if it was
passed to the constructor.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `indexed_db` | Union[bool, None] | Set to `true` to include IndexedDB in the storage state snapshot. |
| `opfs` | Union[bool, None] | Set to `true` to include the origin private file system in the storage state snapshot. |
| `path` | Union[pathlib.Path, str, None] | The file path to save the storage state to. If `path` is a relative path, then it is resolved relative to current working directory. If no path is provided, storage state is still returned, but won't be saved to the disk. |

#### Returns
{cookies: List[{name: str, value: str, domain: str, path: str, expires: float, httpOnly: bool, secure: bool, sameSite: Union["Lax", "None", "Strict"]}], origins: List[{origin: str, localStorage: List[{name: str, value: str}]}]}

### 异步

```python signature
async def storage_state(self, *, indexed_db: Optional[bool] = None, opfs: Optional[bool] = None, path: Union[pathlib.Path, str, NoneType] = None) -> patchright._impl._api_structures.StorageState
```

APIRequestContext.storage_state

Returns storage state for this request context, contains current cookies and local storage snapshot if it was
passed to the constructor.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `indexed_db` | Union[bool, None] | Set to `true` to include IndexedDB in the storage state snapshot. |
| `opfs` | Union[bool, None] | Set to `true` to include the origin private file system in the storage state snapshot. |
| `path` | Union[pathlib.Path, str, None] | The file path to save the storage state to. If `path` is a relative path, then it is resolved relative to current working directory. If no path is provided, storage state is still returned, but won't be saved to the disk. |

#### Returns
{cookies: List[{name: str, value: str, domain: str, path: str, expires: float, httpOnly: bool, secure: bool, sameSite: Union["Lax", "None", "Strict"]}], origins: List[{origin: str, localStorage: List[{name: str, value: str}]}]}


## tracing

属性，直接读取；异步入口也不加 await。

```python signature
APIRequestContext.tracing: Tracing
```

APIRequestContext.tracing

Tracing recorder for requests made through this API request context.

#### Returns
Tracing
