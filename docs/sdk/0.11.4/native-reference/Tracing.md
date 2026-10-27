# 原生 Tracing

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [group](#group)
- [group_end](#group_end)
- [on](#on)
- [once](#once)
- [remove_listener](#remove_listener)
- [start](#start)
- [start_chunk](#start_chunk)
- [start_har](#start_har)
- [stop](#stop)
- [stop_chunk](#stop_chunk)
- [stop_har](#stop_har)

## group

### 同步

```python signature
def group(self, name: str, *, location: Optional[patchright._impl._api_structures.TracingGroupLocation] = None) -> 'SyncContextManager'
```

Tracing.group

**NOTE** Use `test.step` instead when available.

Creates a new group within the trace, assigning any subsequent API calls to this group, until `tracing.group_end()`
is called. Groups can be nested and will be visible in the trace viewer.

**Usage**

```py
# All actions between group and group_end
# will be shown in the trace viewer as a group.
page.context.tracing.group("Open Playwright.dev > API")
page.goto("https://playwright.dev/")
page.get_by_role("link", name="API").click()
page.context.tracing.group_end()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | Group name shown in the trace viewer. |
| `location` | Union[{file: str, line: Union[int, None], column: Union[int, None]}, None] | Specifies a custom location for the group to be shown in the trace viewer. Defaults to the location of the `tracing.group()` call. |

#### Returns
SyncContextManager

### 异步

```python signature
async def group(self, name: str, *, location: Optional[patchright._impl._api_structures.TracingGroupLocation] = None) -> 'AsyncContextManager'
```

Tracing.group

**NOTE** Use `test.step` instead when available.

Creates a new group within the trace, assigning any subsequent API calls to this group, until `tracing.group_end()`
is called. Groups can be nested and will be visible in the trace viewer.

**Usage**

```py
# All actions between group and group_end
# will be shown in the trace viewer as a group.
await page.context.tracing.group("Open Playwright.dev > API")
await page.goto("https://playwright.dev/")
await page.get_by_role("link", name="API").click()
await page.context.tracing.group_end()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | str | Group name shown in the trace viewer. |
| `location` | Union[{file: str, line: Union[int, None], column: Union[int, None]}, None] | Specifies a custom location for the group to be shown in the trace viewer. Defaults to the location of the `tracing.group()` call. |

#### Returns
AsyncContextManager


## group_end

### 同步

```python
def group_end(self) -> None
```

Tracing.group_end

Closes the last group created by `tracing.group()`.

### 异步

```python
async def group_end(self) -> None
```

Tracing.group_end

Closes the last group created by `tracing.group()`.


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


## start

### 同步

```python signature
def start(self, *, aria_snapshots: Optional[bool] = None, live: Optional[bool] = None, name: Optional[str] = None, screen_snapshots: Optional[bool] = None, screenshots: Optional[bool] = None, snapshots: Optional[bool] = None, sources: Optional[bool] = None, title: Optional[str] = None) -> 'SyncContextManager'
```

Tracing.start

Start tracing. Disposing the returned `Disposable` stops tracing without saving the trace, similarly to calling
`tracing.stop()` without a path.

**NOTE** You probably want to
[enable tracing in your config file](https://playwright.dev/docs/api/class-testoptions#test-options-trace) instead
of using `Tracing.start`.

The `context.tracing` API captures browser operations and network activity, but it doesn't record test assertions
(like `expect` calls). We recommend
[enabling tracing through Playwright Test configuration](https://playwright.dev/docs/api/class-testoptions#test-options-trace),
which includes those assertions and provides a more complete trace for debugging test failures.

**Usage**

```py
context.tracing.start(screenshots=True, snapshots=True)
page = context.new_page()
page.goto("https://playwright.dev")
context.tracing.stop(path = "trace.zip")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `aria_snapshots` | Union[bool, None] | Whether to capture aria snapshot of the page on every action. |
| `live` | Union[bool, None] | When enabled, the trace is written to an unarchived file that is updated in real time as actions occur, instead of caching changes and archiving them into a zip file at the end. This is useful for live trace viewing during test execution. |
| `name` | Union[str, None] | If specified, intermediate trace files are going to be saved into the files with the given name prefix inside the `traces_dir` directory specified in `browser_type.launch()`. To specify the final trace zip file name, you need to pass `path` option to `tracing.stop()` instead. |
| `screen_snapshots` | Union[bool, None] | Whether to capture a screenshot of the page on every action. |
| `screenshots` | Union[bool, None] | Whether to capture screenshots during tracing. Screenshots are used to build a timeline preview. |
| `snapshots` | Union[bool, None] | Whether to capture DOM snapshot and record network activity on every action. |
| `sources` | Union[bool, None] | Whether to include source files for trace actions. |
| `title` | Union[str, None] | Trace name to be shown in the Trace Viewer. |

#### Returns
SyncContextManager

### 异步

```python signature
async def start(self, *, aria_snapshots: Optional[bool] = None, live: Optional[bool] = None, name: Optional[str] = None, screen_snapshots: Optional[bool] = None, screenshots: Optional[bool] = None, snapshots: Optional[bool] = None, sources: Optional[bool] = None, title: Optional[str] = None) -> 'AsyncContextManager'
```

Tracing.start

Start tracing. Disposing the returned `Disposable` stops tracing without saving the trace, similarly to calling
`tracing.stop()` without a path.

**NOTE** You probably want to
[enable tracing in your config file](https://playwright.dev/docs/api/class-testoptions#test-options-trace) instead
of using `Tracing.start`.

The `context.tracing` API captures browser operations and network activity, but it doesn't record test assertions
(like `expect` calls). We recommend
[enabling tracing through Playwright Test configuration](https://playwright.dev/docs/api/class-testoptions#test-options-trace),
which includes those assertions and provides a more complete trace for debugging test failures.

**Usage**

```py
await context.tracing.start(screenshots=True, snapshots=True)
page = await context.new_page()
await page.goto("https://playwright.dev")
await context.tracing.stop(path = "trace.zip")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `aria_snapshots` | Union[bool, None] | Whether to capture aria snapshot of the page on every action. |
| `live` | Union[bool, None] | When enabled, the trace is written to an unarchived file that is updated in real time as actions occur, instead of caching changes and archiving them into a zip file at the end. This is useful for live trace viewing during test execution. |
| `name` | Union[str, None] | If specified, intermediate trace files are going to be saved into the files with the given name prefix inside the `traces_dir` directory specified in `browser_type.launch()`. To specify the final trace zip file name, you need to pass `path` option to `tracing.stop()` instead. |
| `screen_snapshots` | Union[bool, None] | Whether to capture a screenshot of the page on every action. |
| `screenshots` | Union[bool, None] | Whether to capture screenshots during tracing. Screenshots are used to build a timeline preview. |
| `snapshots` | Union[bool, None] | Whether to capture DOM snapshot and record network activity on every action. |
| `sources` | Union[bool, None] | Whether to include source files for trace actions. |
| `title` | Union[str, None] | Trace name to be shown in the Trace Viewer. |

#### Returns
AsyncContextManager


## start_chunk

### 同步

```python signature
def start_chunk(self, *, name: Optional[str] = None, title: Optional[str] = None) -> 'SyncContextManager'
```

Tracing.start_chunk

Start a new trace chunk. Disposing the returned `Disposable` stops the chunk without saving it, similarly to
calling `tracing.stop_chunk()` without a path. If you'd like to record multiple traces on the same
`BrowserContext`, use `tracing.start()` once, and then create multiple trace chunks with `tracing.start_chunk()`
and `tracing.stop_chunk()`.

**Usage**

```py
context.tracing.start(screenshots=True, snapshots=True)
page = context.new_page()
page.goto("https://playwright.dev")

context.tracing.start_chunk()
page.get_by_text("Get Started").click()
# Everything between start_chunk and stop_chunk will be recorded in the trace.
context.tracing.stop_chunk(path = "trace1.zip")

context.tracing.start_chunk()
page.goto("http://example.com")
# Save a second trace file with different actions.
context.tracing.stop_chunk(path = "trace2.zip")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | Union[str, None] | If specified, intermediate trace files are going to be saved into the files with the given name prefix inside the `traces_dir` directory specified in `browser_type.launch()`. To specify the final trace zip file name, you need to pass `path` option to `tracing.stop_chunk()` instead. |
| `title` | Union[str, None] | Trace name to be shown in the Trace Viewer. |

#### Returns
SyncContextManager

### 异步

```python signature
async def start_chunk(self, *, name: Optional[str] = None, title: Optional[str] = None) -> 'AsyncContextManager'
```

Tracing.start_chunk

Start a new trace chunk. Disposing the returned `Disposable` stops the chunk without saving it, similarly to
calling `tracing.stop_chunk()` without a path. If you'd like to record multiple traces on the same
`BrowserContext`, use `tracing.start()` once, and then create multiple trace chunks with `tracing.start_chunk()`
and `tracing.stop_chunk()`.

**Usage**

```py
await context.tracing.start(screenshots=True, snapshots=True)
page = await context.new_page()
await page.goto("https://playwright.dev")

await context.tracing.start_chunk()
await page.get_by_text("Get Started").click()
# Everything between start_chunk and stop_chunk will be recorded in the trace.
await context.tracing.stop_chunk(path = "trace1.zip")

await context.tracing.start_chunk()
await page.goto("http://example.com")
# Save a second trace file with different actions.
await context.tracing.stop_chunk(path = "trace2.zip")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `name` | Union[str, None] | If specified, intermediate trace files are going to be saved into the files with the given name prefix inside the `traces_dir` directory specified in `browser_type.launch()`. To specify the final trace zip file name, you need to pass `path` option to `tracing.stop_chunk()` instead. |
| `title` | Union[str, None] | Trace name to be shown in the Trace Viewer. |

#### Returns
AsyncContextManager


## start_har

### 同步

```python signature
def start_har(self, path: Union[str, pathlib.Path], *, content: Optional[Literal['attach', 'embed', 'omit']] = None, mode: Optional[Literal['full', 'minimal']] = None, url_filter: Union[str, Pattern[str], NoneType] = None) -> 'SyncContextManager'
```

Tracing.start_har

Start recording a HAR (HTTP Archive) of network activity in this context. The HAR file is written to disk when
`tracing.stop_har()` is called, or when the returned `Disposable` is disposed.

Only one HAR recording can be active at a time per `Tracing` instance.

**Usage**

```py
context.tracing.start_har("trace.har")
page = context.new_page()
page.goto("https://playwright.dev")
context.tracing.stop_har()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `path` | Union[pathlib.Path, str] | Path on the filesystem to write the HAR file to. If the file name ends with `.zip`, the HAR is saved as a zip archive with response bodies attached as separate files. |
| `content` | Union["attach", "embed", "omit", None] | Optional setting to control resource content management. If `omit` is specified, content is not persisted. If `attach` is specified, resources are persisted as separate files or entries in the ZIP archive. If `embed` is specified, content is stored inline the HAR file as per HAR specification. Defaults to `attach` for `.zip` output files and to `embed` for all other file extensions. |
| `mode` | Union["full", "minimal", None] | When set to `minimal`, only record information necessary for routing from HAR. This omits sizes, timing, page, cookies, security and other types of HAR information that are not used when replaying from HAR. Defaults to `full`. |
| `url_filter` | Union[Pattern[str], str, None] | A glob or regex pattern to filter requests that are stored in the HAR. Defaults to none. |

#### Returns
SyncContextManager

### 异步

```python signature
async def start_har(self, path: Union[str, pathlib.Path], *, content: Optional[Literal['attach', 'embed', 'omit']] = None, mode: Optional[Literal['full', 'minimal']] = None, url_filter: Union[str, Pattern[str], NoneType] = None) -> 'AsyncContextManager'
```

Tracing.start_har

Start recording a HAR (HTTP Archive) of network activity in this context. The HAR file is written to disk when
`tracing.stop_har()` is called, or when the returned `Disposable` is disposed.

Only one HAR recording can be active at a time per `Tracing` instance.

**Usage**

```py
await context.tracing.start_har("trace.har")
page = await context.new_page()
await page.goto("https://playwright.dev")
await context.tracing.stop_har()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `path` | Union[pathlib.Path, str] | Path on the filesystem to write the HAR file to. If the file name ends with `.zip`, the HAR is saved as a zip archive with response bodies attached as separate files. |
| `content` | Union["attach", "embed", "omit", None] | Optional setting to control resource content management. If `omit` is specified, content is not persisted. If `attach` is specified, resources are persisted as separate files or entries in the ZIP archive. If `embed` is specified, content is stored inline the HAR file as per HAR specification. Defaults to `attach` for `.zip` output files and to `embed` for all other file extensions. |
| `mode` | Union["full", "minimal", None] | When set to `minimal`, only record information necessary for routing from HAR. This omits sizes, timing, page, cookies, security and other types of HAR information that are not used when replaying from HAR. Defaults to `full`. |
| `url_filter` | Union[Pattern[str], str, None] | A glob or regex pattern to filter requests that are stored in the HAR. Defaults to none. |

#### Returns
AsyncContextManager


## stop

### 同步

```python signature
def stop(self, *, path: Union[pathlib.Path, str, NoneType] = None) -> None
```

Tracing.stop

Stop tracing.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `path` | Union[pathlib.Path, str, None] | Export trace into the file with the given path. |

### 异步

```python signature
async def stop(self, *, path: Union[pathlib.Path, str, NoneType] = None) -> None
```

Tracing.stop

Stop tracing.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `path` | Union[pathlib.Path, str, None] | Export trace into the file with the given path. |

## stop_chunk

### 同步

```python signature
def stop_chunk(self, *, path: Union[pathlib.Path, str, NoneType] = None) -> None
```

Tracing.stop_chunk

Stop the trace chunk. See `tracing.start_chunk()` for more details about multiple trace chunks.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `path` | Union[pathlib.Path, str, None] | Export trace collected since the last `tracing.start_chunk()` call into the file with the given path. |

### 异步

```python signature
async def stop_chunk(self, *, path: Union[pathlib.Path, str, NoneType] = None) -> None
```

Tracing.stop_chunk

Stop the trace chunk. See `tracing.start_chunk()` for more details about multiple trace chunks.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `path` | Union[pathlib.Path, str, None] | Export trace collected since the last `tracing.start_chunk()` call into the file with the given path. |

## stop_har

### 同步

```python
def stop_har(self) -> None
```

Tracing.stop_har

Stop HAR recording and save the HAR file to the path given to `tracing.start_har()`.

### 异步

```python
async def stop_har(self) -> None
```

Tracing.stop_har

Stop HAR recording and save the HAR file to the path given to `tracing.start_har()`.
