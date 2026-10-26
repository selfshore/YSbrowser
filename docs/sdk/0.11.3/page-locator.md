# 页面与定位器

[返回目录](README.md)

`context.new_page()` 返回当前入口对应的 Patchright `Page`，`context.raw` 返回原生 `BrowserContext`，`browser.raw` 返回原生 `Browser`。以下片段使用已创建的同步 `page` / `context`。完整可运行启动代码见[快速开始](installation.md)。所有原生对象的详细参数与返回类型见[原生 API 参考](native-reference/README.md)。

## 导航与页面内容

```python
response = page.goto("https://app.example.com", wait_until="domcontentloaded", timeout=30000)
print(page.url)
print(page.title())
html = page.content()
page.screenshot(path="page.png", full_page=True)
```

示例 URL 需替换。`goto()` 返回 `Response | None`；`response.status` 是 HTTP 状态码。HTTP 404/500 通常返回响应而非触发导航异常。`wait_until` 可为 `commit`、`domcontentloaded`、`load`、`networkidle`；业务准备状态通常通过元素或明确响应判断。`timeout` 使用毫秒，0 禁用超时。

`page.set_content(html)` 用字符串设置页面；`content()` 返回 HTML 字符串；`title()` 返回标题；`screenshot()` 返回图片字节，传 `path=` 时同时保存文件。`reload()`、`go_back()`、`go_forward()` 用于刷新与历史导航。

## 定位、读取与输入

```python
button = page.get_by_role("button", name="提交", exact=True)
username = page.get_by_label("用户名")
username.fill("alice")
page.get_by_placeholder("请输入密码").fill("example-password")
page.get_by_text("记住我", exact=True).click()
button.click(timeout=10000)

text = page.locator("#result").inner_text()
value = username.input_value()
href = page.locator("a.details").get_attribute("href")
count = page.locator(".item").count()
```

| 接口 | 返回 / 用途 |
| --- | --- |
| `locator(selector)` | Locator，支持 CSS 等原生选择器 |
| `get_by_role(role, name=..., exact=...)` | 按可访问角色和名称定位 |
| `get_by_label(text)` / `get_by_placeholder(text)` | 定位表单控件 |
| `get_by_text(text)` / `get_by_test_id(test_id)` | 按文本或测试属性定位 |
| `locator.filter(has_text=...)` | 缩小元素集合 |
| `locator.nth(index)` / `.first` / `.last` | 选择集合中的元素；nth 从 0 开始 |
| `inner_text()` / `text_content()` | 返回可见文本 `str` / DOM 文本 `str \| None` |
| `input_value()` | 输入框值 `str` |
| `get_attribute(name)` | 属性值 `str \| None` |
| `count()` | 当前匹配元素数量 `int` |
| `bounding_box()` | `{"x", "y", "width", "height"}` 或 `None`，坐标相对主页面视口 |
| `fill(value)` | 替换输入框文字，返回 `None` |
| `press(key)` | 发送键盘组合，例如 `"Control+A"`、`"Enter"` |
| `press_sequentially(text, delay=...)` | 逐字符输入，delay 为字符间毫秒 |
| `check()` / `uncheck()` / `set_checked(bool)` | 操作复选框 |
| `select_option(value=...)` | 选择 select，返回选中项值的字符串列表 |

Locator 是延迟定位对象，构造时不等于元素已存在。要求单个元素的操作匹配到多个元素时会抛严格模式错误；优先改进定位条件。

## 等待与断言

```python
from patchright.sync_api import expect

page.locator("#result").wait_for(state="visible", timeout=10000)
expect(page.locator("#result")).to_have_text("完成", timeout=10000)
expect(page.get_by_role("button", name="提交")).to_be_enabled()
```

`wait_for(state=...)` 的状态为 `attached`、`detached`、`visible`、`hidden`。`expect(...)` 断言按条件重试；异步入口从 `patchright.async_api` 导入 expect，并使用 `await expect(locator).to_have_text(...)`。

`is_visible()`、`count()` 等即时查询不能替代等待断言。`page.wait_for_timeout(ms)` 是固定等待，返回 `None`；通常优先等待可观察的页面状态。

## iframe、嵌套 iframe 和 Shadow DOM

```python
frame = page.frame_locator("iframe#login")
frame.get_by_label("用户名").fill("alice")
frame.get_by_role("button", name="登录").click()

nested = page.frame_locator("iframe#outer").frame_locator("iframe#inner")
nested.locator("#submit").click()

page.locator("user-panel").get_by_role("button", name="保存").click()
```

Page 的定位器不自动跨越 iframe；使用 `frame_locator` 或 `page.frame(...)`。Shadow DOM 使用配套浏览器/Patchright 支持的 CSS/role 定位路径；不要依赖 XPath 跨越 shadow root，也不要把页面 JavaScript 读取 closed `shadowRoot` 当作通用方法。轨迹拖动直接接受这些 Locator，详见[鼠标](mouse.md)。

## 新页面、弹窗与对话框

```python
with page.expect_popup() as popup_info:
    page.get_by_role("link", name="打开详情").click()
popup = popup_info.value
popup.wait_for_load_state("domcontentloaded")

page.on("dialog", lambda dialog: dialog.accept())
print([item.url for item in context.raw.pages])
popup.close()
```

`expect_popup()` 返回事件上下文管理器，`.value` 得到新 Page；必须先开始等待再触发动作。无原页面可关联时使用 `context.raw.expect_page()`。注册 dialog 监听后，需要调用 `accept(prompt_text=...)` 或 `dismiss()` 处理，否则触发该对话框的操作可能等待不结束。

异步模式使用 `async with page.expect_popup() as info:`，随后 `popup = await info.value`；页面属性如 `.url`、`.context`、`.mouse` 不加 `await`。

## 下载与上传

```python
with page.expect_download() as download_info:
    page.get_by_role("link", name="下载").click()
download = download_info.value
download.save_as("downloads/" + download.suggested_filename)
print(download.failure())  # 成功通常为 None

page.locator('input[type="file"]').set_input_files(r"./files/sample.pdf")
```

创建 Context 时可设置 `accept_downloads=True`。下载临时文件随 Context 生命周期清理，需要长期保存时在关闭前 `save_as(path)`。上传可传一个路径、路径列表或原生文件内容对象；清空选择用空列表。

自定义上传按钮可用 `page.expect_file_chooser()`，触发按钮后对 `info.value` 调用 `set_files(...)`。异步版本同样使用 `async with` 和 `await info.value`。

## 网络请求与路由

```python
page.route("**/api/profile", lambda route: route.fulfill(
    status=200,
    content_type="application/json",
    body='{"name":"Alice"}',
))

with page.expect_response("**/api/items") as response_info:
    page.get_by_role("button", name="刷新").click()
response = response_info.value
print(response.status, response.json())

page.on("requestfailed", lambda request: print(request.url, request.failure))
```

`route.fulfill()` 返回模拟响应，`route.continue_()` 放行或覆盖请求参数，`route.abort()` 中止请求。可以使用 `context.raw.route(...)` 覆盖多个页面。Service Worker 接管的请求可能不经过普通路由拦截；按用途设置 `ContextOptions(service_workers="block")`。

`requestfailed` 关注网络失败；HTTP 4xx/5xx 应通过 `response.status` 判断。`page.request`、`context.raw.request` 属于原生 APIRequestContext，不能假设跟随 SDK 自定义 CDP 代理及运行时切换；需要确认页面出口时使用 `context.check_proxy()`。

## JavaScript、Cookie 与权限

```python
value = page.evaluate("([a, b]) => a + b", [2, 3])
print(value)  # 5
text = page.locator("h1").evaluate("element => element.textContent")

cookies = context.raw.cookies()
context.raw.add_cookies([{
    "name": "theme", "value": "light", "url": "https://app.example.com",
}])
context.raw.clear_cookies()
context.raw.grant_permissions(["geolocation"], origin="https://app.example.com")
```

`evaluate(expression, arg=None)` 接受一个可序列化参数，多个值可封装成列表/字典。返回可序列化的 JS 值；需要对象句柄使用 `evaluate_handle()` 并在结束后 `dispose()`。Cookie 与权限的完整参数见原生 BrowserContext 参考。

## 原生鼠标、键盘及底层协议

```python
page.keyboard.press("Control+A")
page.keyboard.insert_text("Hello")
page.mouse.wheel(0, 500)

session = context.raw.new_cdp_session(page)
try:
    metrics = session.send("Page.getLayoutMetrics")
finally:
    session.detach()
```

原生 `page.mouse.move/click/down/up/wheel` 仍可用，路径不自动经过 SDK 模型。原生操作后再使用坐标轨迹时重新 `synchronize()`。CDP 的可用方法由浏览器版本决定；直接修改 SDK 管理的配置会影响配置导出的可靠性。
