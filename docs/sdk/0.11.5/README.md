# YSbrowser SDK 0.11.5 使用手册

YSbrowser SDK 是配套 YSbrowser 定制浏览器的 Python 自动化库。提供同步与异步接口、独立 Context 指纹与代理、代理出口检查、配置与登录状态保存、轨迹鼠标和诊断文件。页面、定位器、网络拦截等操作使用返回的 Patchright 原生对象。

**支持 Windows 与 Linux；macOS 尚未验证。** Python 要求 3.10 或更高版本。SDK 不附带浏览器。先安装当前操作系统对应的配套原生浏览器，随后 `YSBrowser()` 自动定位；也可手动指定 Windows 的 `./browser/chrome.exe` 或 Linux 的 `./browser/chrome`，普通 Chrome 不提供本 SDK 必需的扩展接口。

## 先找到你要做的操作

- [拖动元素一定距离：drag_element](drag-element.md)
- [从 A 点移动到 B 点、相对移动、点击和拖动](mouse.md)
- [返回值是对象还是字典，各字段代表什么](result-structures.md)
- [没有动作、ImportError、坐标或范围错误](troubleshooting.md)

## 文档目录

| 文档 | 内容 |
| --- | --- |
| [安装与快速开始](installation.md) | pip 安装、浏览器自动下载、同步/异步完整程序、命令行 |
| [浏览器与 Context](browser-context.md) | 启动参数、创建与关闭、命名、能力查询、并发 |
| [指纹与 GPU](fingerprint.md) | 全部指纹字段、seed、GPU 型号、设置时机 |
| [Context 选项](context-options.md) | 视口、超时、HTTP 认证、证书、下载、视频、HAR |
| [代理与出口检查](proxy.md) | HTTP/HTTPS/SOCKS5、认证、动态切换、全部状态字段 |
| [配置与登录状态](storage.md) | JSON 配置、凭据补齐、Cookie/LocalStorage/IndexedDB |
| [drag_element 详解](drag-element.md) | 每个参数、返回值、iframe、示例和常见问题 |
| [返回结构速查](result-structures.md) | MotionExecution、MotionPlan、轨迹字典与其他结果 |
| [鼠标轨迹与拖动](mouse.md) | 坐标移动、点击、指定元素拖动、iframe、模型输入输出 |
| [页面与定位器](page-locator.md) | 导航、输入、等待、下载、上传、网络、Shadow DOM |
| [诊断与异常](diagnostics-errors.md) | 诊断采集、截图、trace、返回结构、异常处理 |
| [完整 SDK API](api-reference.md) | 所有公开类型、构造签名、方法、属性和默认值 |
| [Patchright 原生 API 参考](native-reference/README.md) | 原生对象的同步/异步签名、参数、返回值及使用说明 |
| [可运行示例](examples/README.md) | 同步、异步、拖动、离线生成轨迹 |

先按[安装与快速开始](installation.md)安装包和配套浏览器。

## 最小同步程序

```python
from ysbrowser_sdk.sync_api import YSBrowser, FingerprintProfile

with YSBrowser() as browser:
    context = browser.new_context(
        name="account-001",
        fingerprint=FingerprintProfile(fpseed="account-001"),
    )
    page = context.new_page()
    page.set_content('<button onclick="this.textContent=\'完成\'">开始</button>')
    page.get_by_role("button", name="开始").click()
    print(page.get_by_role("button").inner_text())  # 完成
```

`with` 结束时关闭浏览器及其 Context。业务中需要持久保存的登录状态，应在结束前调用 `context.save_storage_state(...)`。

## 导入与单位约定

- 同步入口：`from ysbrowser_sdk.sync_api import ...`。
- 异步入口：`from ysbrowser_sdk.async_api import ...`。根入口 `ysbrowser_sdk` 也导出异步接口。
- 配置类、模型计算和结果对象在两个入口中的调用方式相同；不需要 `await`。
- 浏览器、Context 和鼠标的异步方法使用 `await`；工厂 `context.mouse(page)`、`browser.diagnostics()`、`browser.get_context()` 等仍为同步方法，完整 API 表逐项标出。
- 鼠标坐标和元素尺寸使用页面视口 CSS 像素；`duration_s` 使用秒，`timeout_ms`、`hold_ms` 等使用毫秒。
- 参数中的 `None` 一般表示不指定；`ContextOptions` 的 `None` 表示交给原生接口处理，不等同于 `False`。
- `ProxyStatus` 等结果可调用 `to_dict()`；轨迹数据类可使用 `dataclasses.asdict()`。

## 从 Patchright 使用方式迁移

用 `YSBrowser` 创建浏览器，用 `browser.new_context()` 设置指纹和代理，再通过 `context.new_page()` 取得原生 Page。已有 `page.locator(...)`、`page.goto(...)`、`page.route(...)` 等代码可以继续使用。轨迹鼠标通过 `context.mouse(page)` 调用；它不会自动替换 `page.mouse` 或 `locator.click()`。

本文面向 SDK 0.11.5、Patchright Python 1.64.2 / driver 1.64.1。其他版本请使用对应版本说明。文中网站域名、账号和环境变量值均为示例，访问实际站点时替换为自己的配置。
