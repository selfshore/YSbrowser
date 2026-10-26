# 原生 Route

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [abort](#abort)
- [continue_](#continue_)
- [fallback](#fallback)
- [fetch](#fetch)
- [fulfill](#fulfill)
- [on](#on)
- [once](#once)
- [remove_listener](#remove_listener)
- [request](#request)

## abort

### 同步

```python
def abort(self, error_code: Optional[str] = None) -> None
```

Route.abort

Aborts the route's request.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `error_code` | Union[str, None] | Optional error code. Defaults to `failed`, could be one of the following: - `'aborted'` - An operation was aborted (due to user action) - `'accessdenied'` - Permission to access a resource, other than the network, was denied - `'addressunreachable'` - The IP address is unreachable. This usually means that there is no route to the specified host or network. - `'blockedbyclient'` - The client chose to block the request. - `'blockedbyresponse'` - The request failed because the response was delivered along with requirements which are not met ('X-Frame-Options' and 'Content-Security-Policy' ancestor checks, for instance). - `'connectionaborted'` - A connection timed out as a result of not receiving an ACK for data sent. - `'connectionclosed'` - A connection was closed (corresponding to a TCP FIN). - `'connectionfailed'` - A connection attempt failed. - `'connectionrefused'` - A connection attempt was refused. - `'connectionreset'` - A connection was reset (corresponding to a TCP RST). - `'internetdisconnected'` - The Internet connection has been lost. - `'namenotresolved'` - The host name could not be resolved. - `'timedout'` - An operation timed out. - `'failed'` - A generic failure occurred. |

### 异步

```python
async def abort(self, error_code: Optional[str] = None) -> None
```

Route.abort

Aborts the route's request.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `error_code` | Union[str, None] | Optional error code. Defaults to `failed`, could be one of the following: - `'aborted'` - An operation was aborted (due to user action) - `'accessdenied'` - Permission to access a resource, other than the network, was denied - `'addressunreachable'` - The IP address is unreachable. This usually means that there is no route to the specified host or network. - `'blockedbyclient'` - The client chose to block the request. - `'blockedbyresponse'` - The request failed because the response was delivered along with requirements which are not met ('X-Frame-Options' and 'Content-Security-Policy' ancestor checks, for instance). - `'connectionaborted'` - A connection timed out as a result of not receiving an ACK for data sent. - `'connectionclosed'` - A connection was closed (corresponding to a TCP FIN). - `'connectionfailed'` - A connection attempt failed. - `'connectionrefused'` - A connection attempt was refused. - `'connectionreset'` - A connection was reset (corresponding to a TCP RST). - `'internetdisconnected'` - The Internet connection has been lost. - `'namenotresolved'` - The host name could not be resolved. - `'timedout'` - An operation timed out. - `'failed'` - A generic failure occurred. |

## continue_

### 同步

```python signature
def continue_(self, *, headers: Optional[Dict[str, str]] = None, method: Optional[str] = None, post_data: Union[str, bytes, Any, NoneType] = None, url: Optional[str] = None, patchrightInitScript: Optional[bool] = None) -> None
```

Route.continue_

Sends route's request to the network with optional overrides.

**Usage**

```py
def handle(route, request):
    # override headers
    headers = {
        **request.headers,
        "foo": "foo-value", # set "foo" header
        "bar": None # remove "bar" header
    }
    route.continue_(headers=headers)

page.route("**/*", handle)
```

**Details**

The `headers` option applies to both the routed request and any redirects it initiates. However, `url`, `method`,
and `post_data` only apply to the original request and are not carried over to redirected requests.

`route.continue_()` will immediately send the request to the network, other matching handlers won't be invoked. Use
`route.fallback()` If you want next matching handler in the chain to be invoked.

**NOTE** Some request headers are **forbidden** and cannot be overridden (for example, `Cookie`, `Host`,
`Content-Length` and others, see
[this MDN page](https://developer.mozilla.org/en-US/docs/Glossary/Forbidden_request_header) for full list). If an
override is provided for a forbidden header, it will be ignored and the original request header will be used.

To set custom cookies, use `browser_context.add_cookies()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `headers` | Union[Dict[str, str], None] | If set changes the request HTTP headers. Header values will be converted to a string. |
| `method` | Union[str, None] | If set changes the request method (e.g. GET or POST). |
| `post_data` | Union[Any, bytes, str, None] | If set changes the post data of request. |
| `url` | Union[str, None] | If set changes the request URL. New URL must have same protocol as original one. |

### 异步

```python signature
async def continue_(self, *, headers: Optional[Dict[str, str]] = None, method: Optional[str] = None, post_data: Union[str, bytes, Any, NoneType] = None, url: Optional[str] = None, patchrightInitScript: Optional[bool] = None) -> None
```

Route.continue_

Sends route's request to the network with optional overrides.

**Usage**

```py
async def handle(route, request):
    # override headers
    headers = {
        **request.headers,
        "foo": "foo-value", # set "foo" header
        "bar": None # remove "bar" header
    }
    await route.continue_(headers=headers)

await page.route("**/*", handle)
```

**Details**

The `headers` option applies to both the routed request and any redirects it initiates. However, `url`, `method`,
and `post_data` only apply to the original request and are not carried over to redirected requests.

`route.continue_()` will immediately send the request to the network, other matching handlers won't be invoked. Use
`route.fallback()` If you want next matching handler in the chain to be invoked.

**NOTE** Some request headers are **forbidden** and cannot be overridden (for example, `Cookie`, `Host`,
`Content-Length` and others, see
[this MDN page](https://developer.mozilla.org/en-US/docs/Glossary/Forbidden_request_header) for full list). If an
override is provided for a forbidden header, it will be ignored and the original request header will be used.

To set custom cookies, use `browser_context.add_cookies()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `headers` | Union[Dict[str, str], None] | If set changes the request HTTP headers. Header values will be converted to a string. |
| `method` | Union[str, None] | If set changes the request method (e.g. GET or POST). |
| `post_data` | Union[Any, bytes, str, None] | If set changes the post data of request. |
| `url` | Union[str, None] | If set changes the request URL. New URL must have same protocol as original one. |

## fallback

### 同步

```python signature
def fallback(self, *, headers: Optional[Dict[str, str]] = None, method: Optional[str] = None, post_data: Union[str, bytes, Any, NoneType] = None, url: Optional[str] = None, patchrightInitScript: Optional[bool] = None) -> None
```

Route.fallback

Continues route's request with optional overrides. The method is similar to `route.continue_()` with the difference
that other matching handlers will be invoked before sending the request.

**Usage**

When several routes match the given pattern, they run in the order opposite to their registration. That way the
last registered route can always override all the previous ones. In the example below, request will be handled by
the bottom-most handler first, then it'll fall back to the previous one and in the end will be aborted by the first
registered route.

```py
page.route("**/*", lambda route: route.abort())  # Runs last.
page.route("**/*", lambda route: route.fallback())  # Runs second.
page.route("**/*", lambda route: route.fallback())  # Runs first.
```

Registering multiple routes is useful when you want separate handlers to handle different kinds of requests, for
example API calls vs page resources or GET requests vs POST requests as in the example below.

```py
# Handle GET requests.
def handle_get(route):
    if route.request.method != "GET":
        route.fallback()
        return
  # Handling GET only.
  # ...

# Handle POST requests.
def handle_post(route):
    if route.request.method != "POST":
        route.fallback()
        return
  # Handling POST only.
  # ...

page.route("**/*", handle_get)
page.route("**/*", handle_post)
```

One can also modify request while falling back to the subsequent handler, that way intermediate route handler can
modify url, method, headers and postData of the request.

```py
def handle(route, request):
    # override headers
    headers = {
        **request.headers,
        "foo": "foo-value", # set "foo" header
        "bar": None # remove "bar" header
    }
    route.fallback(headers=headers)

page.route("**/*", handle)
```

Use `route.continue_()` to immediately send the request to the network, other matching handlers won't be invoked in
that case.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `headers` | Union[Dict[str, str], None] | If set changes the request HTTP headers. Header values will be converted to a string. |
| `method` | Union[str, None] | If set changes the request method (e.g. GET or POST). |
| `post_data` | Union[Any, bytes, str, None] | If set changes the post data of request. |
| `url` | Union[str, None] | If set changes the request URL. New URL must have same protocol as original one. Changing the URL won't affect the route matching, all the routes are matched using the original request URL. |

### 异步

```python signature
async def fallback(self, *, headers: Optional[Dict[str, str]] = None, method: Optional[str] = None, post_data: Union[str, bytes, Any, NoneType] = None, url: Optional[str] = None, patchrightInitScript: Optional[bool] = None) -> None
```

Route.fallback

Continues route's request with optional overrides. The method is similar to `route.continue_()` with the difference
that other matching handlers will be invoked before sending the request.

**Usage**

When several routes match the given pattern, they run in the order opposite to their registration. That way the
last registered route can always override all the previous ones. In the example below, request will be handled by
the bottom-most handler first, then it'll fall back to the previous one and in the end will be aborted by the first
registered route.

```py
await page.route("**/*", lambda route: route.abort())  # Runs last.
await page.route("**/*", lambda route: route.fallback())  # Runs second.
await page.route("**/*", lambda route: route.fallback())  # Runs first.
```

Registering multiple routes is useful when you want separate handlers to handle different kinds of requests, for
example API calls vs page resources or GET requests vs POST requests as in the example below.

```py
# Handle GET requests.
async def handle_get(route):
    if route.request.method != "GET":
        await route.fallback()
        return
  # Handling GET only.
  # ...

# Handle POST requests.
async def handle_post(route):
    if route.request.method != "POST":
        await route.fallback()
        return
  # Handling POST only.
  # ...

await page.route("**/*", handle_get)
await page.route("**/*", handle_post)
```

One can also modify request while falling back to the subsequent handler, that way intermediate route handler can
modify url, method, headers and postData of the request.

```py
async def handle(route, request):
    # override headers
    headers = {
        **request.headers,
        "foo": "foo-value", # set "foo" header
        "bar": None # remove "bar" header
    }
    await route.fallback(headers=headers)

await page.route("**/*", handle)
```

Use `route.continue_()` to immediately send the request to the network, other matching handlers won't be invoked in
that case.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `headers` | Union[Dict[str, str], None] | If set changes the request HTTP headers. Header values will be converted to a string. |
| `method` | Union[str, None] | If set changes the request method (e.g. GET or POST). |
| `post_data` | Union[Any, bytes, str, None] | If set changes the post data of request. |
| `url` | Union[str, None] | If set changes the request URL. New URL must have same protocol as original one. Changing the URL won't affect the route matching, all the routes are matched using the original request URL. |

## fetch

### 同步

```python signature
def fetch(self, *, headers: Optional[Dict[str, str]] = None, max_redirects: Optional[int] = None, max_retries: Optional[int] = None, method: Optional[str] = None, post_data: Union[str, bytes, Any, NoneType] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, url: Optional[str] = None) -> 'APIResponse'
```

Route.fetch

Performs the request and fetches result without fulfilling it, so that the response could be modified and then
fulfilled.

**Usage**

```py
def handle(route):
    response = route.fetch()
    json = response.json()
    json["message"]["big_red_dog"] = []
    route.fulfill(response=response, json=json)

page.route("https://dog.ceo/api/breeds/list/all", handle)
```

**Details**

Note that `headers` option will apply to the fetched request as well as any redirects initiated by it. If you want
to only apply `headers` to the original request, but not to redirects, look into `route.continue_()` instead.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `headers` | Union[Dict[str, str], None] | If set changes the request HTTP headers. Header values will be converted to a string. |
| `max_redirects` | Union[int, None] | Maximum number of request redirects that will be followed automatically. An error will be thrown if the number is exceeded. Defaults to `20`. Pass `0` to not follow redirects. |
| `max_retries` | Union[int, None] | Maximum number of times network errors should be retried. Currently only `ECONNRESET` error is retried. Does not retry based on HTTP response codes. An error will be thrown if the limit is exceeded. Defaults to `0` - no retries. |
| `method` | Union[str, None] | If set changes the request method (e.g. GET or POST). |
| `post_data` | Union[Any, bytes, str, None] | Allows to set post data of the request. If the data parameter is an object, it will be serialized to json string and `content-type` header will be set to `application/json` if not explicitly set. Otherwise the `content-type` header will be set to `application/octet-stream` if not explicitly set. |
| `timeout` | Union[float, None] | Request timeout in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. |
| `url` | Union[str, None] | If set changes the request URL. New URL must have same protocol as original one. |

#### Returns
APIResponse

### 异步

```python signature
async def fetch(self, *, headers: Optional[Dict[str, str]] = None, max_redirects: Optional[int] = None, max_retries: Optional[int] = None, method: Optional[str] = None, post_data: Union[str, bytes, Any, NoneType] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, url: Optional[str] = None) -> 'APIResponse'
```

Route.fetch

Performs the request and fetches result without fulfilling it, so that the response could be modified and then
fulfilled.

**Usage**

```py
async def handle(route):
    response = await route.fetch()
    json = await response.json()
    json["message"]["big_red_dog"] = []
    await route.fulfill(response=response, json=json)

await page.route("https://dog.ceo/api/breeds/list/all", handle)
```

**Details**

Note that `headers` option will apply to the fetched request as well as any redirects initiated by it. If you want
to only apply `headers` to the original request, but not to redirects, look into `route.continue_()` instead.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `headers` | Union[Dict[str, str], None] | If set changes the request HTTP headers. Header values will be converted to a string. |
| `max_redirects` | Union[int, None] | Maximum number of request redirects that will be followed automatically. An error will be thrown if the number is exceeded. Defaults to `20`. Pass `0` to not follow redirects. |
| `max_retries` | Union[int, None] | Maximum number of times network errors should be retried. Currently only `ECONNRESET` error is retried. Does not retry based on HTTP response codes. An error will be thrown if the limit is exceeded. Defaults to `0` - no retries. |
| `method` | Union[str, None] | If set changes the request method (e.g. GET or POST). |
| `post_data` | Union[Any, bytes, str, None] | Allows to set post data of the request. If the data parameter is an object, it will be serialized to json string and `content-type` header will be set to `application/json` if not explicitly set. Otherwise the `content-type` header will be set to `application/octet-stream` if not explicitly set. |
| `timeout` | Union[float, None] | Request timeout in milliseconds. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. |
| `url` | Union[str, None] | If set changes the request URL. New URL must have same protocol as original one. |

#### Returns
APIResponse


## fulfill

### 同步

```python signature
def fulfill(self, *, body: Union[str, bytes, NoneType] = None, content_type: Optional[str] = None, headers: Optional[Dict[str, str]] = None, json: Optional[Any] = None, path: Union[pathlib.Path, str, NoneType] = None, response: Optional[ForwardRef('APIResponse')] = None, status: Optional[int] = None) -> None
```

Route.fulfill

Fulfills route's request with given response.

**Usage**

An example of fulfilling all requests with 404 responses:

```py
page.route("**/*", lambda route: route.fulfill(
    status=404,
    content_type="text/plain",
    body="not found!"))
```

An example of serving static file:

```py
page.route("**/xhr_endpoint", lambda route: route.fulfill(path="mock_data.json"))
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `body` | Union[bytes, str, None] | Response body. |
| `content_type` | Union[str, None] | If set, equals to setting `Content-Type` response header. |
| `headers` | Union[Dict[str, str], None] | Response headers. Header values will be converted to a string. |
| `json` | Union[Any, None] | JSON response. This method will set the content type to `application/json` if not set. |
| `path` | Union[pathlib.Path, str, None] | File path to respond with. The content type will be inferred from file extension. If `path` is a relative path, then it is resolved relative to the current working directory. |
| `response` | Union[APIResponse, None] | `APIResponse` to fulfill route's request with. Individual fields of the response (such as headers) can be overridden using fulfill options. |
| `status` | Union[int, None] | Response status code, defaults to `200`. |

### 异步

```python signature
async def fulfill(self, *, body: Union[str, bytes, NoneType] = None, content_type: Optional[str] = None, headers: Optional[Dict[str, str]] = None, json: Optional[Any] = None, path: Union[pathlib.Path, str, NoneType] = None, response: Optional[ForwardRef('APIResponse')] = None, status: Optional[int] = None) -> None
```

Route.fulfill

Fulfills route's request with given response.

**Usage**

An example of fulfilling all requests with 404 responses:

```py
await page.route("**/*", lambda route: route.fulfill(
    status=404,
    content_type="text/plain",
    body="not found!"))
```

An example of serving static file:

```py
await page.route("**/xhr_endpoint", lambda route: route.fulfill(path="mock_data.json"))
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `body` | Union[bytes, str, None] | Response body. |
| `content_type` | Union[str, None] | If set, equals to setting `Content-Type` response header. |
| `headers` | Union[Dict[str, str], None] | Response headers. Header values will be converted to a string. |
| `json` | Union[Any, None] | JSON response. This method will set the content type to `application/json` if not set. |
| `path` | Union[pathlib.Path, str, None] | File path to respond with. The content type will be inferred from file extension. If `path` is a relative path, then it is resolved relative to the current working directory. |
| `response` | Union[APIResponse, None] | `APIResponse` to fulfill route's request with. Individual fields of the response (such as headers) can be overridden using fulfill options. |
| `status` | Union[int, None] | Response status code, defaults to `200`. |

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
Route.request: Request
```

Route.request

A request to be routed.

#### Returns
Request
