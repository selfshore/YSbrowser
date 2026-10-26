# 原生 Keyboard

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [down](#down)
- [insert_text](#insert_text)
- [on](#on)
- [once](#once)
- [press](#press)
- [remove_listener](#remove_listener)
- [type](#type)
- [up](#up)

## down

### 同步

```python
def down(self, key: str) -> None
```

Keyboard.down

Dispatches a `keydown` event.

`key` can specify the intended
[keyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key) value or a single character
to generate the text for. A superset of the `key` values can be found
[here](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values). Examples of the keys are:

`F1` - `F12`, `Digit0`- `Digit9`, `KeyA`- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`,
`Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp`,
etc.

Following modification shortcuts are also supported: `Shift`, `Control`, `Alt`, `Meta`, `ShiftLeft`,
`ControlOrMeta`. `ControlOrMeta` resolves to `Control` on Windows and Linux and to `Meta` on macOS.

Holding down `Shift` will type the text that corresponds to the `key` in the upper case.

If `key` is a single character, it is case-sensitive, so the values `a` and `A` will generate different respective
texts.

If `key` is a modifier key, `Shift`, `Meta`, `Control`, or `Alt`, subsequent key presses will be sent with that
modifier active. To release the modifier key, use `keyboard.up()`.

After the key is pressed once, subsequent calls to `keyboard.down()` will have
[repeat](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/repeat) set to true. To release the key,
use `keyboard.up()`.

**NOTE** Modifier keys DO influence `keyboard.down`. Holding down `Shift` will type the text in upper case.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | str | Name of the key to press or a character to generate, such as `ArrowLeft` or `a`. |

### 异步

```python
async def down(self, key: str) -> None
```

Keyboard.down

Dispatches a `keydown` event.

`key` can specify the intended
[keyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key) value or a single character
to generate the text for. A superset of the `key` values can be found
[here](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values). Examples of the keys are:

`F1` - `F12`, `Digit0`- `Digit9`, `KeyA`- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`,
`Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp`,
etc.

Following modification shortcuts are also supported: `Shift`, `Control`, `Alt`, `Meta`, `ShiftLeft`,
`ControlOrMeta`. `ControlOrMeta` resolves to `Control` on Windows and Linux and to `Meta` on macOS.

Holding down `Shift` will type the text that corresponds to the `key` in the upper case.

If `key` is a single character, it is case-sensitive, so the values `a` and `A` will generate different respective
texts.

If `key` is a modifier key, `Shift`, `Meta`, `Control`, or `Alt`, subsequent key presses will be sent with that
modifier active. To release the modifier key, use `keyboard.up()`.

After the key is pressed once, subsequent calls to `keyboard.down()` will have
[repeat](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/repeat) set to true. To release the key,
use `keyboard.up()`.

**NOTE** Modifier keys DO influence `keyboard.down`. Holding down `Shift` will type the text in upper case.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | str | Name of the key to press or a character to generate, such as `ArrowLeft` or `a`. |

## insert_text

### 同步

```python
def insert_text(self, text: str) -> None
```

Keyboard.insert_text

Dispatches only `input` event, does not emit the `keydown`, `keyup` or `keypress` events.

**Usage**

```py
page.keyboard.insert_text("嗨")
```

**NOTE** Modifier keys DO NOT effect `keyboard.insertText`. Holding down `Shift` will not type the text in upper
case.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `text` | str | Sets input to the specified text value. |

### 异步

```python
async def insert_text(self, text: str) -> None
```

Keyboard.insert_text

Dispatches only `input` event, does not emit the `keydown`, `keyup` or `keypress` events.

**Usage**

```py
await page.keyboard.insert_text("嗨")
```

**NOTE** Modifier keys DO NOT effect `keyboard.insertText`. Holding down `Shift` will not type the text in upper
case.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `text` | str | Sets input to the specified text value. |

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


## press

### 同步

```python signature
def press(self, key: str, *, delay: Optional[float] = None) -> None
```

Keyboard.press

**NOTE** In most cases, you should use `locator.press()` instead.

`key` can specify the intended
[keyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key) value or a single character
to generate the text for. A superset of the `key` values can be found
[here](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values). Examples of the keys are:

`F1` - `F12`, `Digit0`- `Digit9`, `KeyA`- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`,
`Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp`,
etc.

Following modification shortcuts are also supported: `Shift`, `Control`, `Alt`, `Meta`, `ShiftLeft`,
`ControlOrMeta`. `ControlOrMeta` resolves to `Control` on Windows and Linux and to `Meta` on macOS.

Holding down `Shift` will type the text that corresponds to the `key` in the upper case.

If `key` is a single character, it is case-sensitive, so the values `a` and `A` will generate different respective
texts.

Shortcuts such as `key: "Control+o"`, `key: "Control++` or `key: "Control+Shift+T"` are supported as well. When
specified with the modifier, modifier is pressed and being held while the subsequent key is being pressed.

**Usage**

```py
page = browser.new_page()
page.goto("https://keycode.info")
page.keyboard.press("a")
page.screenshot(path="a.png")
page.keyboard.press("ArrowLeft")
page.screenshot(path="arrow_left.png")
page.keyboard.press("Shift+O")
page.screenshot(path="o.png")
browser.close()
```

Shortcut for `keyboard.down()` and `keyboard.up()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | str | Name of the key to press or a character to generate, such as `ArrowLeft` or `a`. |
| `delay` | Union[float, None] | Time to wait between `keydown` and `keyup` in milliseconds. Defaults to 0. |

### 异步

```python signature
async def press(self, key: str, *, delay: Optional[float] = None) -> None
```

Keyboard.press

**NOTE** In most cases, you should use `locator.press()` instead.

`key` can specify the intended
[keyboardEvent.key](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key) value or a single character
to generate the text for. A superset of the `key` values can be found
[here](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent/key/Key_Values). Examples of the keys are:

`F1` - `F12`, `Digit0`- `Digit9`, `KeyA`- `KeyZ`, `Backquote`, `Minus`, `Equal`, `Backslash`, `Backspace`, `Tab`,
`Delete`, `Escape`, `ArrowDown`, `End`, `Enter`, `Home`, `Insert`, `PageDown`, `PageUp`, `ArrowRight`, `ArrowUp`,
etc.

Following modification shortcuts are also supported: `Shift`, `Control`, `Alt`, `Meta`, `ShiftLeft`,
`ControlOrMeta`. `ControlOrMeta` resolves to `Control` on Windows and Linux and to `Meta` on macOS.

Holding down `Shift` will type the text that corresponds to the `key` in the upper case.

If `key` is a single character, it is case-sensitive, so the values `a` and `A` will generate different respective
texts.

Shortcuts such as `key: "Control+o"`, `key: "Control++` or `key: "Control+Shift+T"` are supported as well. When
specified with the modifier, modifier is pressed and being held while the subsequent key is being pressed.

**Usage**

```py
page = await browser.new_page()
await page.goto("https://keycode.info")
await page.keyboard.press("a")
await page.screenshot(path="a.png")
await page.keyboard.press("ArrowLeft")
await page.screenshot(path="arrow_left.png")
await page.keyboard.press("Shift+O")
await page.screenshot(path="o.png")
await browser.close()
```

Shortcut for `keyboard.down()` and `keyboard.up()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | str | Name of the key to press or a character to generate, such as `ArrowLeft` or `a`. |
| `delay` | Union[float, None] | Time to wait between `keydown` and `keyup` in milliseconds. Defaults to 0. |

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


## type

### 同步

```python signature
def type(self, text: str, *, delay: Optional[float] = None) -> None
```

Keyboard.type

**NOTE** In most cases, you should use `locator.fill()` instead. You only need to press keys one by one if there is
special keyboard handling on the page - in this case use `locator.press_sequentially()`.

Sends a `keydown`, `keypress`/`input`, and `keyup` event for each character in the text.

To press a special key, like `Control` or `ArrowDown`, use `keyboard.press()`.

**Usage**

```py
page.keyboard.type("Hello") # types instantly
page.keyboard.type("World", delay=100) # types slower, like a user
```

**NOTE** Modifier keys DO NOT effect `keyboard.type`. Holding down `Shift` will not type the text in upper case.

**NOTE** For characters that are not on a US keyboard, only an `input` event will be sent.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `text` | str | A text to type into a focused element. |
| `delay` | Union[float, None] | Time to wait between key presses in milliseconds. Defaults to 0. |

### 异步

```python signature
async def type(self, text: str, *, delay: Optional[float] = None) -> None
```

Keyboard.type

**NOTE** In most cases, you should use `locator.fill()` instead. You only need to press keys one by one if there is
special keyboard handling on the page - in this case use `locator.press_sequentially()`.

Sends a `keydown`, `keypress`/`input`, and `keyup` event for each character in the text.

To press a special key, like `Control` or `ArrowDown`, use `keyboard.press()`.

**Usage**

```py
await page.keyboard.type("Hello") # types instantly
await page.keyboard.type("World", delay=100) # types slower, like a user
```

**NOTE** Modifier keys DO NOT effect `keyboard.type`. Holding down `Shift` will not type the text in upper case.

**NOTE** For characters that are not on a US keyboard, only an `input` event will be sent.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `text` | str | A text to type into a focused element. |
| `delay` | Union[float, None] | Time to wait between key presses in milliseconds. Defaults to 0. |

## up

### 同步

```python
def up(self, key: str) -> None
```

Keyboard.up

Dispatches a `keyup` event.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | str | Name of the key to press or a character to generate, such as `ArrowLeft` or `a`. |

### 异步

```python
async def up(self, key: str) -> None
```

Keyboard.up

Dispatches a `keyup` event.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `key` | str | Name of the key to press or a character to generate, such as `ArrowLeft` or `a`. |
