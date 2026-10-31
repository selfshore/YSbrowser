# 原生 Request

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [all_headers](#all_headers)
- [existing_response](#existing_response)
- [failure](#failure)
- [frame](#frame)
- [header_value](#header_value)
- [headers](#headers)
- [headers_array](#headers_array)
- [is_navigation_request](#is_navigation_request)
- [method](#method)
- [on](#on)
- [once](#once)
- [post_data](#post_data)
- [post_data_buffer](#post_data_buffer)
- [post_data_json](#post_data_json)
- [redirected_from](#redirected_from)
- [redirected_to](#redirected_to)
- [remove_listener](#remove_listener)
- [resource_type](#resource_type)
- [response](#response)
- [service_worker](#service_worker)
- [sizes](#sizes)
- [timing](#timing)
- [url](#url)

## all_headers

### 同步

```python
def all_headers(self) -> Dict[str, str]
```

Request.all_headers

An object with all the request HTTP headers associated with this request. The header names are lower-cased.

#### Returns
Dict[str, str]

### 异步

```python
async def all_headers(self) -> Dict[str, str]
```

Request.all_headers

An object with all the request HTTP headers associated with this request. The header names are lower-cased.

#### Returns
Dict[str, str]


## existing_response

属性，直接读取；异步入口也不加 await。

```python signature
Request.existing_response: typing.Optional[ForwardRef('Response')]
```

Request.existing_response

Returns the `Response` object if the response has already been received, `null` otherwise.

Unlike `request.response()`, this method does not wait for the response to arrive. It returns immediately with the
response object if the response has been received, or `null` if the response has not been received yet.

#### Returns
Union[Response, None]


## failure

属性，直接读取；异步入口也不加 await。

```python signature
Request.failure: typing.Optional[str]
```

Request.failure

The method returns `null` unless this request has failed, as reported by `requestfailed` event.

**Usage**

Example of logging of all the failed requests:

```py
page.on("requestfailed", lambda request: print(request.url + " " + request.failure))
```

#### Returns
Union[str, None]


## frame

属性，直接读取；异步入口也不加 await。

```python signature
Request.frame: Frame
```

Request.frame

Returns the `Frame` that initiated this request.

**Usage**

```py
frame_url = request.frame.url
```

**Details**

Note that in some cases the frame is not available, and this method will throw.
- When request originates in the Service Worker. You can use `request.serviceWorker()` to check that.
- When navigation request is issued before the corresponding frame is created. You can use
  `request.is_navigation_request()` to check that.

Here is an example that handles all the cases:

#### Returns
Frame


## header_value

### 同步

```python
def header_value(self, name: str) -> Optional[str]
```

Request.header_value

Returns the value of the header matching the name. The name is case-insensitive.

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

Request.header_value

Returns the value of the header matching the name. The name is case-insensitive.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | Name of the header. |

#### Returns
Union[str, None]


## headers

属性，直接读取；异步入口也不加 await。

```python signature
Request.headers: typing.Dict[str, str]
```

Request.headers

An object with the request HTTP headers. The header names are lower-cased. Note that this method does not return
security-related headers, including cookie-related ones. You can use `request.all_headers()` for complete list of
headers that include `cookie` information.

#### Returns
Dict[str, str]


## headers_array

### 同步

```python
def headers_array(self) -> List[patchright._impl._api_structures.NameValue]
```

Request.headers_array

An array with all the request HTTP headers associated with this request. Unlike `request.all_headers()`, header
names are NOT lower-cased. Headers with multiple entries, such as `Set-Cookie`, appear in the array multiple times.

#### Returns
List[{name: str, value: str}]

### 异步

```python
async def headers_array(self) -> List[patchright._impl._api_structures.NameValue]
```

Request.headers_array

An array with all the request HTTP headers associated with this request. Unlike `request.all_headers()`, header
names are NOT lower-cased. Headers with multiple entries, such as `Set-Cookie`, appear in the array multiple times.

#### Returns
List[{name: str, value: str}]


## is_navigation_request

### 同步

```python
def is_navigation_request(self) -> bool
```

Request.is_navigation_request

Whether this request is driving frame's navigation.

Some navigation requests are issued before the corresponding frame is created, and therefore do not have
`request.frame` available.

#### Returns
bool

### 异步

```python
def is_navigation_request(self) -> bool
```

Request.is_navigation_request

Whether this request is driving frame's navigation.

Some navigation requests are issued before the corresponding frame is created, and therefore do not have
`request.frame` available.

#### Returns
bool


## method

属性，直接读取；异步入口也不加 await。

```python signature
Request.method: <class 'str'>
```

Request.method

Request's method (GET, POST, etc.)

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


## post_data

属性，直接读取；异步入口也不加 await。

```python signature
Request.post_data: typing.Optional[str]
```

Request.post_data

Request's post body, if any.

#### Returns
Union[str, None]


## post_data_buffer

属性，直接读取；异步入口也不加 await。

```python signature
Request.post_data_buffer: typing.Optional[bytes]
```

Request.post_data_buffer

Request's post body in a binary form, if any.

#### Returns
Union[bytes, None]


## post_data_json

属性，直接读取；异步入口也不加 await。

```python signature
Request.post_data_json: typing.Optional[typing.Any]
```

Request.post_data_json

Returns parsed request's body for `form-urlencoded` and JSON as a fallback if any.

When the response is `application/x-www-form-urlencoded` then a key/value object of the values will be returned.
Otherwise it will be parsed as JSON.

#### Returns
Union[Any, None]


## redirected_from

属性，直接读取；异步入口也不加 await。

```python signature
Request.redirected_from: typing.Optional[ForwardRef('Request')]
```

Request.redirected_from

Request that was redirected by the server to this one, if any.

When the server responds with a redirect, Playwright creates a new `Request` object. The two requests are connected
by `redirectedFrom()` and `redirectedTo()` methods. When multiple server redirects has happened, it is possible to
construct the whole redirect chain by repeatedly calling `redirectedFrom()`.

**Usage**

For example, if the website `http://example.com` redirects to `https://example.com`:

```py
response = page.goto("http://example.com")
print(response.request.redirected_from.url) # "http://example.com"
```

If the website `https://google.com` has no redirects:

```py
response = page.goto("https://google.com")
print(response.request.redirected_from) # None
```

#### Returns
Union[Request, None]


## redirected_to

属性，直接读取；异步入口也不加 await。

```python signature
Request.redirected_to: typing.Optional[ForwardRef('Request')]
```

Request.redirected_to

New request issued by the browser if the server responded with redirect.

**Usage**

This method is the opposite of `request.redirected_from`:

```py
assert request.redirected_from.redirected_to == request
```

#### Returns
Union[Request, None]


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


## resource_type

属性，直接读取；异步入口也不加 await。

```python signature
Request.resource_type: <class 'str'>
```

Request.resource_type

Contains the request's resource type as it was perceived by the rendering engine. ResourceType will be one of the
following: `document`, `stylesheet`, `image`, `media`, `font`, `script`, `texttrack`, `xhr`, `fetch`,
`eventsource`, `websocket`, `manifest`, `beacon`, `ping`, `cspreport`, `other`.

#### Returns
str


## response

### 同步

```python
def response(self) -> Optional[ForwardRef('Response')]
```

Request.response

Returns the matching `Response` object, or `null` if the response was not received due to error.

#### Returns
Union[Response, None]

### 异步

```python
async def response(self) -> Optional[ForwardRef('Response')]
```

Request.response

Returns the matching `Response` object, or `null` if the response was not received due to error.

#### Returns
Union[Response, None]


## service_worker

属性，直接读取；异步入口也不加 await。

```python signature
Request.service_worker: typing.Optional[ForwardRef('Worker')]
```

Request.service_worker

The Service `Worker` that is performing the request.

**Details**

This method is Chromium only. It's safe to call when using other browsers, but it will always be `null`.

Requests originated in a Service Worker do not have a `request.frame` available.

#### Returns
Union[Worker, None]


## sizes

### 同步

```python
def sizes(self) -> patchright._impl._api_structures.RequestSizes
```

Request.sizes

Returns resource size information for given request.

#### Returns
{requestBodySize: int, requestHeadersSize: int, responseBodySize: int, responseHeadersSize: int}

### 异步

```python
async def sizes(self) -> patchright._impl._api_structures.RequestSizes
```

Request.sizes

Returns resource size information for given request.

#### Returns
{requestBodySize: int, requestHeadersSize: int, responseBodySize: int, responseHeadersSize: int}


## timing

属性，直接读取；异步入口也不加 await。

```python signature
Request.timing: <class 'patchright._impl._api_structures.ResourceTiming'>
```

Request.timing

Returns resource timing information for given request. Most of the timing values become available upon the
response, `responseEnd` becomes available when request finishes. Find more information at
[Resource Timing API](https://developer.mozilla.org/en-US/docs/Web/API/PerformanceResourceTiming).

**Usage**

```py
with page.expect_event("requestfinished") as request_info:
    page.goto("http://example.com")
request = request_info.value
print(request.timing)
```

#### Returns
{startTime: float, domainLookupStart: float, domainLookupEnd: float, connectStart: float, secureConnectionStart: float, connectEnd: float, requestStart: float, responseStart: float, responseEnd: float}


## url

属性，直接读取；异步入口也不加 await。

```python signature
Request.url: <class 'str'>
```

Request.url

URL of the request.

#### Returns
str
