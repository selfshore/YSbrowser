# 原生 FrameLocator

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [first](#first)
- [frame_locator](#frame_locator)
- [get_by_alt_text](#get_by_alt_text)
- [get_by_label](#get_by_label)
- [get_by_placeholder](#get_by_placeholder)
- [get_by_role](#get_by_role)
- [get_by_test_id](#get_by_test_id)
- [get_by_text](#get_by_text)
- [get_by_title](#get_by_title)
- [last](#last)
- [locator](#locator)
- [nth](#nth)
- [on](#on)
- [once](#once)
- [owner](#owner)
- [remove_listener](#remove_listener)

## first

属性，直接读取；异步入口也不加 await。

```python signature
FrameLocator.first: FrameLocator
```

FrameLocator.first

Returns locator to the first matching frame.

#### Returns
FrameLocator


## frame_locator

### 同步

```python
def frame_locator(self, selector: str) -> 'FrameLocator'
```

FrameLocator.frame_locator

When working with iframes, you can create a frame locator that will enter the iframe and allow selecting elements
in that iframe.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to use when resolving DOM element. |

#### Returns
FrameLocator

### 异步

```python
def frame_locator(self, selector: str) -> 'FrameLocator'
```

FrameLocator.frame_locator

When working with iframes, you can create a frame locator that will enter the iframe and allow selecting elements
in that iframe.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector` | str | A selector to use when resolving DOM element. |

#### Returns
FrameLocator


## get_by_alt_text

### 同步

```python signature
def get_by_alt_text(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'
```

FrameLocator.get_by_alt_text

Allows locating elements by their alt text.

**Usage**

For example, this method will find the image by alt text "Playwright logo":

```html
<img alt='Playwright logo'>
```

```py
page.get_by_alt_text("Playwright logo").click()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `text` | Union[Pattern[str], str] | Text to locate the element for. |
| `exact` | Union[bool, None] | Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace. |

#### Returns
Locator

### 异步

```python signature
def get_by_alt_text(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'
```

FrameLocator.get_by_alt_text

Allows locating elements by their alt text.

**Usage**

For example, this method will find the image by alt text "Playwright logo":

```html
<img alt='Playwright logo'>
```

```py
await page.get_by_alt_text("Playwright logo").click()
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `text` | Union[Pattern[str], str] | Text to locate the element for. |
| `exact` | Union[bool, None] | Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace. |

#### Returns
Locator


## get_by_label

### 同步

```python signature
def get_by_label(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'
```

FrameLocator.get_by_label

Allows locating input elements by the text of the associated `<label>` or `aria-labelledby` element, or by the
`aria-label` attribute.

**Usage**

For example, this method will find inputs by label "Username" and "Password" in the following DOM:

```html
<input aria-label="Username">
<label for="password-input">Password:</label>
<input id="password-input">
```

```py
page.get_by_label("Username").fill("john")
page.get_by_label("Password").fill("secret")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `text` | Union[Pattern[str], str] | Text to locate the element for. |
| `exact` | Union[bool, None] | Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace. |

#### Returns
Locator

### 异步

```python signature
def get_by_label(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'
```

FrameLocator.get_by_label

Allows locating input elements by the text of the associated `<label>` or `aria-labelledby` element, or by the
`aria-label` attribute.

**Usage**

For example, this method will find inputs by label "Username" and "Password" in the following DOM:

```html
<input aria-label="Username">
<label for="password-input">Password:</label>
<input id="password-input">
```

```py
await page.get_by_label("Username").fill("john")
await page.get_by_label("Password").fill("secret")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `text` | Union[Pattern[str], str] | Text to locate the element for. |
| `exact` | Union[bool, None] | Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace. |

#### Returns
Locator


## get_by_placeholder

### 同步

```python signature
def get_by_placeholder(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'
```

FrameLocator.get_by_placeholder

Allows locating input elements by the placeholder text.

**Usage**

For example, consider the following DOM structure.

```html
<input type="email" placeholder="name@example.com" />
```

You can fill the input after locating it by the placeholder text:

```py
page.get_by_placeholder("name@example.com").fill("playwright@microsoft.com")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `text` | Union[Pattern[str], str] | Text to locate the element for. |
| `exact` | Union[bool, None] | Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace. |

#### Returns
Locator

### 异步

```python signature
def get_by_placeholder(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'
```

FrameLocator.get_by_placeholder

Allows locating input elements by the placeholder text.

**Usage**

For example, consider the following DOM structure.

```html
<input type="email" placeholder="name@example.com" />
```

You can fill the input after locating it by the placeholder text:

```py
await page.get_by_placeholder("name@example.com").fill("playwright@microsoft.com")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `text` | Union[Pattern[str], str] | Text to locate the element for. |
| `exact` | Union[bool, None] | Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace. |

#### Returns
Locator


## get_by_role

### 同步

```python signature
def get_by_role(self, role: Literal['alert', 'alertdialog', 'application', 'article', 'banner', 'blockquote', 'button', 'caption', 'cell', 'checkbox', 'code', 'columnheader', 'combobox', 'complementary', 'contentinfo', 'definition', 'deletion', 'dialog', 'directory', 'document', 'emphasis', 'feed', 'figure', 'form', 'generic', 'grid', 'gridcell', 'group', 'heading', 'img', 'insertion', 'link', 'list', 'listbox', 'listitem', 'log', 'main', 'marquee', 'math', 'menu', 'menubar', 'menuitem', 'menuitemcheckbox', 'menuitemradio', 'meter', 'navigation', 'none', 'note', 'option', 'paragraph', 'presentation', 'progressbar', 'radio', 'radiogroup', 'region', 'row', 'rowgroup', 'rowheader', 'scrollbar', 'search', 'searchbox', 'separator', 'slider', 'spinbutton', 'status', 'strong', 'subscript', 'superscript', 'switch', 'tab', 'table', 'tablist', 'tabpanel', 'term', 'textbox', 'time', 'timer', 'toolbar', 'tooltip', 'tree', 'treegrid', 'treeitem'], *, checked: Optional[bool] = None, description: Union[str, Pattern[str], NoneType] = None, disabled: Optional[bool] = None, exact: Optional[bool] = None, expanded: Optional[bool] = None, include_hidden: Optional[bool] = None, level: Optional[int] = None, name: Union[str, Pattern[str], NoneType] = None, pressed: Optional[bool] = None, selected: Optional[bool] = None) -> 'Locator'
```

FrameLocator.get_by_role

Allows locating elements by their [ARIA role](https://www.w3.org/TR/wai-aria-1.2/#roles),
[ARIA attributes](https://www.w3.org/TR/wai-aria-1.2/#aria-attributes) and
[accessible name](https://w3c.github.io/accname/#dfn-accessible-name).

**Usage**

Consider the following DOM structure.

```html
<h3>Sign up</h3>
<label>
  <input type="checkbox" /> Subscribe
</label>
<br/>
<button>Submit</button>
```

You can locate each element by its implicit role:

```py
expect(page.get_by_role("heading", name="Sign up")).to_be_visible()

page.get_by_role("checkbox", name="Subscribe").check()

page.get_by_role("button", name=re.compile("submit", re.IGNORECASE)).click()
```

**Details**

Role selector **does not replace** accessibility audits and conformance tests, but rather gives early feedback
about the ARIA guidelines.

Many html elements have an implicitly [defined role](https://w3c.github.io/html-aam/#html-element-role-mappings)
that is recognized by the role selector. You can find all the
[supported roles here](https://www.w3.org/TR/wai-aria-1.2/#role_definitions). ARIA guidelines **do not recommend**
duplicating implicit roles and attributes by setting `role` and/or `aria-*` attributes to default values.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `role` | Union["alert", "alertdialog", "application", "article", "banner", "blockquote", "button", "caption", "cell", "checkbox", "code", "columnheader", "combobox", "complementary", "contentinfo", "definition", "deletion", "dialog", "directory", "document", "emphasis", "feed", "figure", "form", "generic", "grid", "gridcell", "group", "heading", "img", "insertion", "link", "list", "listbox", "listitem", "log", "main", "marquee", "math", "menu", "menubar", "menuitem", "menuitemcheckbox", "menuitemradio", "meter", "navigation", "none", "note", "option", "paragraph", "presentation", "progressbar", "radio", "radiogroup", "region", "row", "rowgroup", "rowheader", "scrollbar", "search", "searchbox", "separator", "slider", "spinbutton", "status", "strong", "subscript", "superscript", "switch", "tab", "table", "tablist", "tabpanel", "term", "textbox", "time", "timer", "toolbar", "tooltip", "tree", "treegrid", "treeitem"] | Required aria role. |
| `checked` | Union[bool, None] | An attribute that is usually set by `aria-checked` or native `<input type=checkbox>` controls.  Learn more about [`aria-checked`](https://www.w3.org/TR/wai-aria-1.2/#aria-checked). |
| `description` | Union[Pattern[str], str, None] | Option to match the [accessible description](https://w3c.github.io/accname/#dfn-accessible-description). By default, matching is case-insensitive and searches for a substring, use `exact` to control this behavior.  Learn more about [accessible description](https://w3c.github.io/accname/#dfn-accessible-description). |
| `disabled` | Union[bool, None] | An attribute that is usually set by `aria-disabled` or `disabled`.  **NOTE** Unlike most other attributes, `disabled` is inherited through the DOM hierarchy. Learn more about [`aria-disabled`](https://www.w3.org/TR/wai-aria-1.2/#aria-disabled). |
| `exact` | Union[bool, None] | Whether `name` and `description` are matched exactly: case-sensitive and whole-string. Defaults to false. Ignored when the value is a regular expression. Note that exact match still trims whitespace. |
| `expanded` | Union[bool, None] | An attribute that is usually set by `aria-expanded`.  Learn more about [`aria-expanded`](https://www.w3.org/TR/wai-aria-1.2/#aria-expanded). |
| `include_hidden` | Union[bool, None] | Option that controls whether hidden elements are matched. By default, only non-hidden elements, as [defined by ARIA](https://www.w3.org/TR/wai-aria-1.2/#tree_exclusion), are matched by role selector.  Learn more about [`aria-hidden`](https://www.w3.org/TR/wai-aria-1.2/#aria-hidden). |
| `level` | Union[int, None] | A number attribute that is usually present for roles `heading`, `listitem`, `row`, `treeitem`, with default values for `<h1>-<h6>` elements.  Learn more about [`aria-level`](https://www.w3.org/TR/wai-aria-1.2/#aria-level). |
| `name` | Union[Pattern[str], str, None] | Option to match the [accessible name](https://w3c.github.io/accname/#dfn-accessible-name). By default, matching is case-insensitive and searches for a substring, use `exact` to control this behavior.  Learn more about [accessible name](https://w3c.github.io/accname/#dfn-accessible-name). |
| `pressed` | Union[bool, None] | An attribute that is usually set by `aria-pressed`.  Learn more about [`aria-pressed`](https://www.w3.org/TR/wai-aria-1.2/#aria-pressed). |
| `selected` | Union[bool, None] | An attribute that is usually set by `aria-selected`.  Learn more about [`aria-selected`](https://www.w3.org/TR/wai-aria-1.2/#aria-selected). |

#### Returns
Locator

### 异步

```python signature
def get_by_role(self, role: Literal['alert', 'alertdialog', 'application', 'article', 'banner', 'blockquote', 'button', 'caption', 'cell', 'checkbox', 'code', 'columnheader', 'combobox', 'complementary', 'contentinfo', 'definition', 'deletion', 'dialog', 'directory', 'document', 'emphasis', 'feed', 'figure', 'form', 'generic', 'grid', 'gridcell', 'group', 'heading', 'img', 'insertion', 'link', 'list', 'listbox', 'listitem', 'log', 'main', 'marquee', 'math', 'menu', 'menubar', 'menuitem', 'menuitemcheckbox', 'menuitemradio', 'meter', 'navigation', 'none', 'note', 'option', 'paragraph', 'presentation', 'progressbar', 'radio', 'radiogroup', 'region', 'row', 'rowgroup', 'rowheader', 'scrollbar', 'search', 'searchbox', 'separator', 'slider', 'spinbutton', 'status', 'strong', 'subscript', 'superscript', 'switch', 'tab', 'table', 'tablist', 'tabpanel', 'term', 'textbox', 'time', 'timer', 'toolbar', 'tooltip', 'tree', 'treegrid', 'treeitem'], *, checked: Optional[bool] = None, description: Union[str, Pattern[str], NoneType] = None, disabled: Optional[bool] = None, exact: Optional[bool] = None, expanded: Optional[bool] = None, include_hidden: Optional[bool] = None, level: Optional[int] = None, name: Union[str, Pattern[str], NoneType] = None, pressed: Optional[bool] = None, selected: Optional[bool] = None) -> 'Locator'
```

FrameLocator.get_by_role

Allows locating elements by their [ARIA role](https://www.w3.org/TR/wai-aria-1.2/#roles),
[ARIA attributes](https://www.w3.org/TR/wai-aria-1.2/#aria-attributes) and
[accessible name](https://w3c.github.io/accname/#dfn-accessible-name).

**Usage**

Consider the following DOM structure.

```html
<h3>Sign up</h3>
<label>
  <input type="checkbox" /> Subscribe
</label>
<br/>
<button>Submit</button>
```

You can locate each element by its implicit role:

```py
await expect(page.get_by_role("heading", name="Sign up")).to_be_visible()

await page.get_by_role("checkbox", name="Subscribe").check()

await page.get_by_role("button", name=re.compile("submit", re.IGNORECASE)).click()
```

**Details**

Role selector **does not replace** accessibility audits and conformance tests, but rather gives early feedback
about the ARIA guidelines.

Many html elements have an implicitly [defined role](https://w3c.github.io/html-aam/#html-element-role-mappings)
that is recognized by the role selector. You can find all the
[supported roles here](https://www.w3.org/TR/wai-aria-1.2/#role_definitions). ARIA guidelines **do not recommend**
duplicating implicit roles and attributes by setting `role` and/or `aria-*` attributes to default values.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `role` | Union["alert", "alertdialog", "application", "article", "banner", "blockquote", "button", "caption", "cell", "checkbox", "code", "columnheader", "combobox", "complementary", "contentinfo", "definition", "deletion", "dialog", "directory", "document", "emphasis", "feed", "figure", "form", "generic", "grid", "gridcell", "group", "heading", "img", "insertion", "link", "list", "listbox", "listitem", "log", "main", "marquee", "math", "menu", "menubar", "menuitem", "menuitemcheckbox", "menuitemradio", "meter", "navigation", "none", "note", "option", "paragraph", "presentation", "progressbar", "radio", "radiogroup", "region", "row", "rowgroup", "rowheader", "scrollbar", "search", "searchbox", "separator", "slider", "spinbutton", "status", "strong", "subscript", "superscript", "switch", "tab", "table", "tablist", "tabpanel", "term", "textbox", "time", "timer", "toolbar", "tooltip", "tree", "treegrid", "treeitem"] | Required aria role. |
| `checked` | Union[bool, None] | An attribute that is usually set by `aria-checked` or native `<input type=checkbox>` controls.  Learn more about [`aria-checked`](https://www.w3.org/TR/wai-aria-1.2/#aria-checked). |
| `description` | Union[Pattern[str], str, None] | Option to match the [accessible description](https://w3c.github.io/accname/#dfn-accessible-description). By default, matching is case-insensitive and searches for a substring, use `exact` to control this behavior.  Learn more about [accessible description](https://w3c.github.io/accname/#dfn-accessible-description). |
| `disabled` | Union[bool, None] | An attribute that is usually set by `aria-disabled` or `disabled`.  **NOTE** Unlike most other attributes, `disabled` is inherited through the DOM hierarchy. Learn more about [`aria-disabled`](https://www.w3.org/TR/wai-aria-1.2/#aria-disabled). |
| `exact` | Union[bool, None] | Whether `name` and `description` are matched exactly: case-sensitive and whole-string. Defaults to false. Ignored when the value is a regular expression. Note that exact match still trims whitespace. |
| `expanded` | Union[bool, None] | An attribute that is usually set by `aria-expanded`.  Learn more about [`aria-expanded`](https://www.w3.org/TR/wai-aria-1.2/#aria-expanded). |
| `include_hidden` | Union[bool, None] | Option that controls whether hidden elements are matched. By default, only non-hidden elements, as [defined by ARIA](https://www.w3.org/TR/wai-aria-1.2/#tree_exclusion), are matched by role selector.  Learn more about [`aria-hidden`](https://www.w3.org/TR/wai-aria-1.2/#aria-hidden). |
| `level` | Union[int, None] | A number attribute that is usually present for roles `heading`, `listitem`, `row`, `treeitem`, with default values for `<h1>-<h6>` elements.  Learn more about [`aria-level`](https://www.w3.org/TR/wai-aria-1.2/#aria-level). |
| `name` | Union[Pattern[str], str, None] | Option to match the [accessible name](https://w3c.github.io/accname/#dfn-accessible-name). By default, matching is case-insensitive and searches for a substring, use `exact` to control this behavior.  Learn more about [accessible name](https://w3c.github.io/accname/#dfn-accessible-name). |
| `pressed` | Union[bool, None] | An attribute that is usually set by `aria-pressed`.  Learn more about [`aria-pressed`](https://www.w3.org/TR/wai-aria-1.2/#aria-pressed). |
| `selected` | Union[bool, None] | An attribute that is usually set by `aria-selected`.  Learn more about [`aria-selected`](https://www.w3.org/TR/wai-aria-1.2/#aria-selected). |

#### Returns
Locator


## get_by_test_id

### 同步

```python
def get_by_test_id(self, test_id: Union[str, Pattern[str]]) -> 'Locator'
```

FrameLocator.get_by_test_id

Locate element by the test id.

**Usage**

Consider the following DOM structure.

```html
<button data-testid="directions">Itinéraire</button>
```

You can locate the element by its test id:

```py
page.get_by_test_id("directions").click()
```

**Details**

By default, the `data-testid` attribute is used as a test id. Use `selectors.set_test_id_attribute()` to configure
a different test id attribute if necessary.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `test_id` | Union[Pattern[str], str] | Id to locate the element by. |

#### Returns
Locator

### 异步

```python
def get_by_test_id(self, test_id: Union[str, Pattern[str]]) -> 'Locator'
```

FrameLocator.get_by_test_id

Locate element by the test id.

**Usage**

Consider the following DOM structure.

```html
<button data-testid="directions">Itinéraire</button>
```

You can locate the element by its test id:

```py
await page.get_by_test_id("directions").click()
```

**Details**

By default, the `data-testid` attribute is used as a test id. Use `selectors.set_test_id_attribute()` to configure
a different test id attribute if necessary.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `test_id` | Union[Pattern[str], str] | Id to locate the element by. |

#### Returns
Locator


## get_by_text

### 同步

```python signature
def get_by_text(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'
```

FrameLocator.get_by_text

Allows locating elements that contain given text.

See also `locator.filter()` that allows to match by another criteria, like an accessible role, and then filter by
the text content.

**Usage**

Consider the following DOM structure:

```html
<div>Hello <span>world</span></div>
<div>Hello</div>
```

You can locate by text substring, exact string, or a regular expression:

```py
# Matches <span>
page.get_by_text("world")

# Matches first <div>
page.get_by_text("Hello world")

# Matches second <div>
page.get_by_text("Hello", exact=True)

# Matches both <div>s
page.get_by_text(re.compile("Hello"))

# Matches second <div>
page.get_by_text(re.compile("^hello$", re.IGNORECASE))
```

**Details**

Matching by text always normalizes whitespace, even with exact match. For example, it turns multiple spaces into
one, turns line breaks into spaces and ignores leading and trailing whitespace.

Input elements of the type `button` and `submit` are matched by their `value` instead of the text content. For
example, locating by text `"Log in"` matches `<input type=button value="Log in">`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `text` | Union[Pattern[str], str] | Text to locate the element for. |
| `exact` | Union[bool, None] | Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace. |

#### Returns
Locator

### 异步

```python signature
def get_by_text(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'
```

FrameLocator.get_by_text

Allows locating elements that contain given text.

See also `locator.filter()` that allows to match by another criteria, like an accessible role, and then filter by
the text content.

**Usage**

Consider the following DOM structure:

```html
<div>Hello <span>world</span></div>
<div>Hello</div>
```

You can locate by text substring, exact string, or a regular expression:

```py
# Matches <span>
page.get_by_text("world")

# Matches first <div>
page.get_by_text("Hello world")

# Matches second <div>
page.get_by_text("Hello", exact=True)

# Matches both <div>s
page.get_by_text(re.compile("Hello"))

# Matches second <div>
page.get_by_text(re.compile("^hello$", re.IGNORECASE))
```

**Details**

Matching by text always normalizes whitespace, even with exact match. For example, it turns multiple spaces into
one, turns line breaks into spaces and ignores leading and trailing whitespace.

Input elements of the type `button` and `submit` are matched by their `value` instead of the text content. For
example, locating by text `"Log in"` matches `<input type=button value="Log in">`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `text` | Union[Pattern[str], str] | Text to locate the element for. |
| `exact` | Union[bool, None] | Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace. |

#### Returns
Locator


## get_by_title

### 同步

```python signature
def get_by_title(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'
```

FrameLocator.get_by_title

Allows locating elements by their title attribute.

**Usage**

Consider the following DOM structure.

```html
<span title='Issues count'>25 issues</span>
```

You can check the issues count after locating it by the title text:

```py
expect(page.get_by_title("Issues count")).to_have_text("25 issues")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `text` | Union[Pattern[str], str] | Text to locate the element for. |
| `exact` | Union[bool, None] | Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace. |

#### Returns
Locator

### 异步

```python signature
def get_by_title(self, text: Union[str, Pattern[str]], *, exact: Optional[bool] = None) -> 'Locator'
```

FrameLocator.get_by_title

Allows locating elements by their title attribute.

**Usage**

Consider the following DOM structure.

```html
<span title='Issues count'>25 issues</span>
```

You can check the issues count after locating it by the title text:

```py
await expect(page.get_by_title("Issues count")).to_have_text("25 issues")
```

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `text` | Union[Pattern[str], str] | Text to locate the element for. |
| `exact` | Union[bool, None] | Whether to find an exact match: case-sensitive and whole-string. Default to false. Ignored when locating by a regular expression. Note that exact match still trims whitespace. |

#### Returns
Locator


## last

属性，直接读取；异步入口也不加 await。

```python signature
FrameLocator.last: FrameLocator
```

FrameLocator.last

Returns locator to the last matching frame.

#### Returns
FrameLocator


## locator

### 同步

```python signature
def locator(self, selector_or_locator: Union[str, ForwardRef('Locator')], *, has: Optional[ForwardRef('Locator')] = None, has_not: Optional[ForwardRef('Locator')] = None, has_not_text: Union[str, Pattern[str], NoneType] = None, has_text: Union[str, Pattern[str], NoneType] = None) -> 'Locator'
```

FrameLocator.locator

The method finds an element matching the specified selector in the locator's subtree. It also accepts filter
options, similar to `locator.filter()` method.

[Learn more about locators](https://playwright.dev/python/docs/locators).

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector_or_locator` | Union[Locator, str] | A selector or locator to use when resolving DOM element. |
| `has` | Union[Locator, None] | Narrows down the results of the method to those which contain elements matching this relative locator. For example, `article` that has `text=Playwright` matches `<article><div>Playwright</div></article>`.  Inner locator **must be relative** to the outer locator and is queried starting with the outer locator match, not the document root. For example, you can find `content` that has `div` in `<article><content><div>Playwright</div></content></article>`. However, looking for `content` that has `article div` will fail, because the inner locator must be relative and should not use any elements outside the `content`.  Note that outer and inner locators must belong to the same frame. Inner locator must not contain `FrameLocator`s. |
| `has_not` | Union[Locator, None] | Matches elements that do not contain an element that matches an inner locator. Inner locator is queried against the outer one. For example, `article` that does not have `div` matches `<article><span>Playwright</span></article>`.  Note that outer and inner locators must belong to the same frame. Inner locator must not contain `FrameLocator`s. |
| `has_not_text` | Union[Pattern[str], str, None] | Matches elements that do not contain specified text somewhere inside, possibly in a child or a descendant element. When passed a [string], matching is case-insensitive and searches for a substring. |
| `has_text` | Union[Pattern[str], str, None] | Matches elements containing specified text somewhere inside, possibly in a child or a descendant element. When passed a [string], matching is case-insensitive and searches for a substring. For example, `"Playwright"` matches `<article><div>Playwright</div></article>`. |

#### Returns
Locator

### 异步

```python signature
def locator(self, selector_or_locator: Union[str, ForwardRef('Locator')], *, has: Optional[ForwardRef('Locator')] = None, has_not: Optional[ForwardRef('Locator')] = None, has_not_text: Union[str, Pattern[str], NoneType] = None, has_text: Union[str, Pattern[str], NoneType] = None) -> 'Locator'
```

FrameLocator.locator

The method finds an element matching the specified selector in the locator's subtree. It also accepts filter
options, similar to `locator.filter()` method.

[Learn more about locators](https://playwright.dev/python/docs/locators).

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `selector_or_locator` | Union[Locator, str] | A selector or locator to use when resolving DOM element. |
| `has` | Union[Locator, None] | Narrows down the results of the method to those which contain elements matching this relative locator. For example, `article` that has `text=Playwright` matches `<article><div>Playwright</div></article>`.  Inner locator **must be relative** to the outer locator and is queried starting with the outer locator match, not the document root. For example, you can find `content` that has `div` in `<article><content><div>Playwright</div></content></article>`. However, looking for `content` that has `article div` will fail, because the inner locator must be relative and should not use any elements outside the `content`.  Note that outer and inner locators must belong to the same frame. Inner locator must not contain `FrameLocator`s. |
| `has_not` | Union[Locator, None] | Matches elements that do not contain an element that matches an inner locator. Inner locator is queried against the outer one. For example, `article` that does not have `div` matches `<article><span>Playwright</span></article>`.  Note that outer and inner locators must belong to the same frame. Inner locator must not contain `FrameLocator`s. |
| `has_not_text` | Union[Pattern[str], str, None] | Matches elements that do not contain specified text somewhere inside, possibly in a child or a descendant element. When passed a [string], matching is case-insensitive and searches for a substring. |
| `has_text` | Union[Pattern[str], str, None] | Matches elements containing specified text somewhere inside, possibly in a child or a descendant element. When passed a [string], matching is case-insensitive and searches for a substring. For example, `"Playwright"` matches `<article><div>Playwright</div></article>`. |

#### Returns
Locator


## nth

### 同步

```python
def nth(self, index: int) -> 'FrameLocator'
```

FrameLocator.nth

Returns locator to the n-th matching frame. It's zero based, `nth(0)` selects the first frame.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `index` | int |  |

#### Returns
FrameLocator

### 异步

```python
def nth(self, index: int) -> 'FrameLocator'
```

FrameLocator.nth

Returns locator to the n-th matching frame. It's zero based, `nth(0)` selects the first frame.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `index` | int |  |

#### Returns
FrameLocator


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


## owner

属性，直接读取；异步入口也不加 await。

```python signature
FrameLocator.owner: Locator
```

FrameLocator.owner

Returns a `Locator` object pointing to the same `iframe` as this frame locator.

Useful when you have a `FrameLocator` object obtained somewhere, and later on would like to interact with the
`iframe` element.

For a reverse operation, use `locator.content_frame`.

**Usage**

```py
frame_locator = page.locator("iframe[name=\"embedded\"]").content_frame
# ...
locator = frame_locator.owner
expect(locator).to_be_visible()
```

#### Returns
Locator


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
