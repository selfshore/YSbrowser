# 原生 Clock

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [fast_forward](#fast_forward)
- [install](#install)
- [on](#on)
- [once](#once)
- [pause_at](#pause_at)
- [remove_listener](#remove_listener)
- [resume](#resume)
- [run_for](#run_for)
- [set_fixed_time](#set_fixed_time)
- [set_system_time](#set_system_time)

## fast_forward

### 同步

```python
def fast_forward(self, ticks: Union[int, str]) -> None
```

Clock.fast_forward

Advance the clock by jumping forward in time. Only fires due timers at most once. This is equivalent to user
closing the laptop lid for a while and reopening it later, after given time.

**Usage**

```py
page.clock.fast_forward(1000)
page.clock.fast_forward("30:00")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `ticks` | Union[int, str] | Time may be the number of milliseconds to advance the clock by or a human-readable string. Valid string formats are "08" for eight seconds, "01:00" for one minute and "02:34:10" for two hours, 34 minutes and ten seconds. |

### 异步

```python
async def fast_forward(self, ticks: Union[int, str]) -> None
```

Clock.fast_forward

Advance the clock by jumping forward in time. Only fires due timers at most once. This is equivalent to user
closing the laptop lid for a while and reopening it later, after given time.

**Usage**

```py
await page.clock.fast_forward(1000)
await page.clock.fast_forward("30:00")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `ticks` | Union[int, str] | Time may be the number of milliseconds to advance the clock by or a human-readable string. Valid string formats are "08" for eight seconds, "01:00" for one minute and "02:34:10" for two hours, 34 minutes and ten seconds. |

## install

### 同步

```python signature
def install(self, *, time: Union[float, str, datetime.datetime, NoneType] = None) -> None
```

Clock.install

Install fake implementations for the following time-related functions:
- `Date`
- `Temporal.Now`
- `setTimeout`
- `clearTimeout`
- `setInterval`
- `clearInterval`
- `requestAnimationFrame`
- `cancelAnimationFrame`
- `requestIdleCallback`
- `cancelIdleCallback`
- `performance`

Fake timers are used to manually control the flow of time in tests. They allow you to advance time, fire timers,
and control the behavior of time-dependent functions. See `clock.run_for()` and `clock.fast_forward()` for more
information.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `time` | Union[datetime.datetime, float, str, None] | Time to initialize with, current system time by default. Numeric values are Unix time in seconds. |

### 异步

```python signature
async def install(self, *, time: Union[float, str, datetime.datetime, NoneType] = None) -> None
```

Clock.install

Install fake implementations for the following time-related functions:
- `Date`
- `Temporal.Now`
- `setTimeout`
- `clearTimeout`
- `setInterval`
- `clearInterval`
- `requestAnimationFrame`
- `cancelAnimationFrame`
- `requestIdleCallback`
- `cancelIdleCallback`
- `performance`

Fake timers are used to manually control the flow of time in tests. They allow you to advance time, fire timers,
and control the behavior of time-dependent functions. See `clock.run_for()` and `clock.fast_forward()` for more
information.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `time` | Union[datetime.datetime, float, str, None] | Time to initialize with, current system time by default. Numeric values are Unix time in seconds. |

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


## pause_at

### 同步

```python
def pause_at(self, time: Union[float, str, datetime.datetime]) -> None
```

Clock.pause_at

Advance the clock by jumping forward in time and pause the time. Once this method is called, no timers are fired
unless `clock.run_for()`, `clock.fast_forward()`, `clock.pause_at()` or `clock.resume()` is called.

Only fires due timers at most once. This is equivalent to user closing the laptop lid for a while and reopening it
at the specified time and pausing.

**Usage**

```py
page.clock.pause_at(datetime.datetime(2020, 2, 2))
page.clock.pause_at("2020-02-02")
```

For best results, install the clock before navigating the page and set it to a time slightly before the intended
test time. This ensures that all timers run normally during page loading, preventing the page from getting stuck.
Once the page has fully loaded, you can safely use `clock.pause_at()` to pause the clock.

```py
# Initialize clock with some time before the test time and let the page load
# naturally. `Date.now` will progress as the timers fire.
page.clock.install(time=datetime.datetime(2024, 12, 10, 8, 0, 0))
page.goto("http://localhost:3333")
page.clock.pause_at(datetime.datetime(2024, 12, 10, 10, 0, 0))
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `time` | Union[datetime.datetime, float, str] | Time to pause at. Numeric values are Unix time in seconds. |

### 异步

```python
async def pause_at(self, time: Union[float, str, datetime.datetime]) -> None
```

Clock.pause_at

Advance the clock by jumping forward in time and pause the time. Once this method is called, no timers are fired
unless `clock.run_for()`, `clock.fast_forward()`, `clock.pause_at()` or `clock.resume()` is called.

Only fires due timers at most once. This is equivalent to user closing the laptop lid for a while and reopening it
at the specified time and pausing.

**Usage**

```py
await page.clock.pause_at(datetime.datetime(2020, 2, 2))
await page.clock.pause_at("2020-02-02")
```

For best results, install the clock before navigating the page and set it to a time slightly before the intended
test time. This ensures that all timers run normally during page loading, preventing the page from getting stuck.
Once the page has fully loaded, you can safely use `clock.pause_at()` to pause the clock.

```py
# Initialize clock with some time before the test time and let the page load
# naturally. `Date.now` will progress as the timers fire.
await page.clock.install(time=datetime.datetime(2024, 12, 10, 8, 0, 0))
await page.goto("http://localhost:3333")
await page.clock.pause_at(datetime.datetime(2024, 12, 10, 10, 0, 0))
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `time` | Union[datetime.datetime, float, str] | Time to pause at. Numeric values are Unix time in seconds. |

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


## resume

### 同步

```python
def resume(self) -> None
```

Clock.resume

Resumes timers. Once this method is called, time resumes flowing, timers are fired as usual.

### 异步

```python
async def resume(self) -> None
```

Clock.resume

Resumes timers. Once this method is called, time resumes flowing, timers are fired as usual.


## run_for

### 同步

```python
def run_for(self, ticks: Union[int, str]) -> None
```

Clock.run_for

Advance the clock, firing all the time-related callbacks.

**Usage**

```py
page.clock.run_for(1000);
page.clock.run_for("30:00")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `ticks` | Union[int, str] | Time may be the number of milliseconds to advance the clock by or a human-readable string. Valid string formats are "08" for eight seconds, "01:00" for one minute and "02:34:10" for two hours, 34 minutes and ten seconds. |

### 异步

```python
async def run_for(self, ticks: Union[int, str]) -> None
```

Clock.run_for

Advance the clock, firing all the time-related callbacks.

**Usage**

```py
await page.clock.run_for(1000);
await page.clock.run_for("30:00")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `ticks` | Union[int, str] | Time may be the number of milliseconds to advance the clock by or a human-readable string. Valid string formats are "08" for eight seconds, "01:00" for one minute and "02:34:10" for two hours, 34 minutes and ten seconds. |

## set_fixed_time

### 同步

```python
def set_fixed_time(self, time: Union[float, str, datetime.datetime]) -> None
```

Clock.set_fixed_time

Makes `Date.now` and `new Date()` return fixed fake time at all times, keeps all the timers running.

Use this method for simple scenarios where you only need to test with a predefined time. For more advanced
scenarios, use `clock.install()` instead. Read docs on [clock emulation](https://playwright.dev/python/docs/clock) to learn more.

**Usage**

```py
page.clock.set_fixed_time(datetime.datetime.now())
page.clock.set_fixed_time(datetime.datetime(2020, 2, 2))
page.clock.set_fixed_time("2020-02-02")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `time` | Union[datetime.datetime, float, str] | Time to be set. Numeric values are Unix time in seconds. |

### 异步

```python
async def set_fixed_time(self, time: Union[float, str, datetime.datetime]) -> None
```

Clock.set_fixed_time

Makes `Date.now` and `new Date()` return fixed fake time at all times, keeps all the timers running.

Use this method for simple scenarios where you only need to test with a predefined time. For more advanced
scenarios, use `clock.install()` instead. Read docs on [clock emulation](https://playwright.dev/python/docs/clock) to learn more.

**Usage**

```py
await page.clock.set_fixed_time(datetime.datetime.now())
await page.clock.set_fixed_time(datetime.datetime(2020, 2, 2))
await page.clock.set_fixed_time("2020-02-02")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `time` | Union[datetime.datetime, float, str] | Time to be set. Numeric values are Unix time in seconds. |

## set_system_time

### 同步

```python
def set_system_time(self, time: Union[float, str, datetime.datetime]) -> None
```

Clock.set_system_time

Sets system time, but does not trigger any timers. Use this to test how the web page reacts to a time shift, for
example switching from summer to winter time, or changing time zones.

**Usage**

```py
page.clock.set_system_time(datetime.datetime.now())
page.clock.set_system_time(datetime.datetime(2020, 2, 2))
page.clock.set_system_time("2020-02-02")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `time` | Union[datetime.datetime, float, str] | Time to be set. Numeric values are Unix time in seconds. |

### 异步

```python
async def set_system_time(self, time: Union[float, str, datetime.datetime]) -> None
```

Clock.set_system_time

Sets system time, but does not trigger any timers. Use this to test how the web page reacts to a time shift, for
example switching from summer to winter time, or changing time zones.

**Usage**

```py
await page.clock.set_system_time(datetime.datetime.now())
await page.clock.set_system_time(datetime.datetime(2020, 2, 2))
await page.clock.set_system_time("2020-02-02")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `time` | Union[datetime.datetime, float, str] | Time to be set. Numeric values are Unix time in seconds. |
