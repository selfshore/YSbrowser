# 原生 APIRequest

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [new_context](#new_context)
- [on](#on)
- [once](#once)
- [remove_listener](#remove_listener)

## new_context

### 同步

```python signature
def new_context(self, *, base_url: Optional[str] = None, client_certificates: Optional[Sequence[patchright._impl._api_structures.ClientCertificate]] = None, extra_http_headers: Optional[Dict[str, str]] = None, fail_on_status_code: Optional[bool] = None, http_credentials: Union[patchright._impl._api_structures.HttpCredentials, Sequence[patchright._impl._api_structures.HttpCredentials], NoneType] = None, ignore_https_errors: Optional[bool] = None, max_redirects: Optional[int] = None, proxy: Optional[patchright._impl._api_structures.ProxySettings] = None, storage_state: Union[str, pathlib.Path, patchright._impl._api_structures.StorageState, NoneType] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, user_agent: Optional[str] = None) -> 'APIRequestContext'
```

APIRequest.new_context

Creates new instances of `APIRequestContext`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `base_url` | Union[str, None] | Methods like `api_request_context.get()` take the base URL into consideration by using the [`URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) constructor for building the corresponding URL. Examples: - baseURL: `http://localhost:3000` and sending request to `/bar.html` results in `http://localhost:3000/bar.html` - baseURL: `http://localhost:3000/foo/` and sending request to `./bar.html` results in `http://localhost:3000/foo/bar.html` - baseURL: `http://localhost:3000/foo` (without trailing slash) and navigating to `./bar.html` results in `http://localhost:3000/bar.html` |
| `client_certificates` | Union[Sequence[{origin: str, certPath: Union[pathlib.Path, str, None], cert: Union[bytes, None], keyPath: Union[pathlib.Path, str, None], key: Union[bytes, None], pfxPath: Union[pathlib.Path, str, None], pfx: Union[bytes, None], passphrase: Union[str, None]}], None] | TLS Client Authentication allows the server to request a client certificate and verify it.  **Details**  An array of client certificates to be used. Each certificate object must have either both `certPath` and `keyPath`, a single `pfxPath`, or their corresponding direct value equivalents (`cert` and `key`, or `pfx`). Optionally, `passphrase` property should be provided if the certificate is encrypted. The `origin` property should be provided with an exact match to the request origin that the certificate is valid for.  Client certificate authentication is only active when at least one client certificate is provided. If you want to reject all client certificates sent by the server, you need to provide a client certificate with an `origin` that does not match any of the domains you plan to visit.  **NOTE** When using WebKit on macOS, accessing `localhost` will not pick up client certificates. You can make it work by replacing `localhost` with `local.playwright`. |
| `extra_http_headers` | Union[Dict[str, str], None] | An object containing additional HTTP headers to be sent with every request. Defaults to none. |
| `fail_on_status_code` | Union[bool, None] | Whether to throw on response codes other than 2xx and 3xx. By default response object is returned for all status codes. |
| `http_credentials` | Union[Sequence[{username: str, password: str, origin: Union[str, None], send: Union["always", "unauthorized", None]}], {username: str, password: str, origin: Union[str, None], send: Union["always", "unauthorized", None]}, None] | Credentials for [HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication). If no origin is specified, the username and password are sent to any servers upon unauthorized responses.  Pass an array to use different credentials for different origins. The first entry that matches the request origin is used, and entries with no origin match any request. |
| `ignore_https_errors` | Union[bool, None] | Whether to ignore HTTPS errors when sending network requests. Defaults to `false`. |
| `max_redirects` | Union[int, None] | Maximum number of request redirects that will be followed automatically. An error will be thrown if the number is exceeded. Defaults to `20`. Pass `0` to not follow redirects. This can be overwritten for each request individually. |
| `proxy` | Union[{server: str, bypass: Union[str, None], username: Union[str, None], password: Union[str, None]}, None] | Network proxy settings. |
| `storage_state` | Union[pathlib.Path, str, {cookies: Sequence[{name: str, value: str, domain: str, path: str, expires: float, httpOnly: bool, secure: bool, sameSite: Union["Lax", "None", "Strict"]}], origins: Sequence[{origin: str, localStorage: Sequence[{name: str, value: str}]}]}, None] | Populates context with given storage state. This option can be used to initialize context with logged-in information obtained via `browser_context.storage_state()` or `api_request_context.storage_state()`. Either a path to the file with saved storage, or the value returned by one of `browser_context.storage_state()` or `api_request_context.storage_state()` methods. |
| `timeout` | Union[float, None] | Maximum time in milliseconds to wait for the response. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. |
| `user_agent` | Union[str, None] | Specific user agent to use in this context. |

#### Returns
APIRequestContext

### 异步

```python signature
async def new_context(self, *, base_url: Optional[str] = None, client_certificates: Optional[Sequence[patchright._impl._api_structures.ClientCertificate]] = None, extra_http_headers: Optional[Dict[str, str]] = None, fail_on_status_code: Optional[bool] = None, http_credentials: Union[patchright._impl._api_structures.HttpCredentials, Sequence[patchright._impl._api_structures.HttpCredentials], NoneType] = None, ignore_https_errors: Optional[bool] = None, max_redirects: Optional[int] = None, proxy: Optional[patchright._impl._api_structures.ProxySettings] = None, storage_state: Union[str, pathlib.Path, patchright._impl._api_structures.StorageState, NoneType] = None, timeout: Union[float, datetime.timedelta, NoneType] = None, user_agent: Optional[str] = None) -> 'APIRequestContext'
```

APIRequest.new_context

Creates new instances of `APIRequestContext`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `base_url` | Union[str, None] | Methods like `api_request_context.get()` take the base URL into consideration by using the [`URL()`](https://developer.mozilla.org/en-US/docs/Web/API/URL/URL) constructor for building the corresponding URL. Examples: - baseURL: `http://localhost:3000` and sending request to `/bar.html` results in `http://localhost:3000/bar.html` - baseURL: `http://localhost:3000/foo/` and sending request to `./bar.html` results in `http://localhost:3000/foo/bar.html` - baseURL: `http://localhost:3000/foo` (without trailing slash) and navigating to `./bar.html` results in `http://localhost:3000/bar.html` |
| `client_certificates` | Union[Sequence[{origin: str, certPath: Union[pathlib.Path, str, None], cert: Union[bytes, None], keyPath: Union[pathlib.Path, str, None], key: Union[bytes, None], pfxPath: Union[pathlib.Path, str, None], pfx: Union[bytes, None], passphrase: Union[str, None]}], None] | TLS Client Authentication allows the server to request a client certificate and verify it.  **Details**  An array of client certificates to be used. Each certificate object must have either both `certPath` and `keyPath`, a single `pfxPath`, or their corresponding direct value equivalents (`cert` and `key`, or `pfx`). Optionally, `passphrase` property should be provided if the certificate is encrypted. The `origin` property should be provided with an exact match to the request origin that the certificate is valid for.  Client certificate authentication is only active when at least one client certificate is provided. If you want to reject all client certificates sent by the server, you need to provide a client certificate with an `origin` that does not match any of the domains you plan to visit.  **NOTE** When using WebKit on macOS, accessing `localhost` will not pick up client certificates. You can make it work by replacing `localhost` with `local.playwright`. |
| `extra_http_headers` | Union[Dict[str, str], None] | An object containing additional HTTP headers to be sent with every request. Defaults to none. |
| `fail_on_status_code` | Union[bool, None] | Whether to throw on response codes other than 2xx and 3xx. By default response object is returned for all status codes. |
| `http_credentials` | Union[Sequence[{username: str, password: str, origin: Union[str, None], send: Union["always", "unauthorized", None]}], {username: str, password: str, origin: Union[str, None], send: Union["always", "unauthorized", None]}, None] | Credentials for [HTTP authentication](https://developer.mozilla.org/en-US/docs/Web/HTTP/Authentication). If no origin is specified, the username and password are sent to any servers upon unauthorized responses.  Pass an array to use different credentials for different origins. The first entry that matches the request origin is used, and entries with no origin match any request. |
| `ignore_https_errors` | Union[bool, None] | Whether to ignore HTTPS errors when sending network requests. Defaults to `false`. |
| `max_redirects` | Union[int, None] | Maximum number of request redirects that will be followed automatically. An error will be thrown if the number is exceeded. Defaults to `20`. Pass `0` to not follow redirects. This can be overwritten for each request individually. |
| `proxy` | Union[{server: str, bypass: Union[str, None], username: Union[str, None], password: Union[str, None]}, None] | Network proxy settings. |
| `storage_state` | Union[pathlib.Path, str, {cookies: Sequence[{name: str, value: str, domain: str, path: str, expires: float, httpOnly: bool, secure: bool, sameSite: Union["Lax", "None", "Strict"]}], origins: Sequence[{origin: str, localStorage: Sequence[{name: str, value: str}]}]}, None] | Populates context with given storage state. This option can be used to initialize context with logged-in information obtained via `browser_context.storage_state()` or `api_request_context.storage_state()`. Either a path to the file with saved storage, or the value returned by one of `browser_context.storage_state()` or `api_request_context.storage_state()` methods. |
| `timeout` | Union[float, None] | Maximum time in milliseconds to wait for the response. Defaults to `30000` (30 seconds). Pass `0` to disable timeout. |
| `user_agent` | Union[str, None] | Specific user agent to use in this context. |

#### Returns
APIRequestContext


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
