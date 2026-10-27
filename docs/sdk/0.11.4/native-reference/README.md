# Patchright 原生 API 参考

[返回手册目录](../README.md)

本附录对应 SDK 固定依赖 Patchright Python 1.64.2。常用操作的中文说明见[页面与定位器](../page-locator.md)。下列各页包含该对象所有公开方法/属性的同步及异步签名，并保留随包提供的英文参数、返回值及示例说明，便于核对每个可选字段。

这些接口通过 `Page`、`Locator`、`context.raw` 等原生对象调用，不是 YSContext 的新增方法。BrowserType/Playwright 的原生启动接口仅作参考；使用本 SDK 管理指纹和代理时从 YSBrowser 启动。原生 APIRequestContext 不能据此假设跟随自定义 Context 代理。

异步 API 的普通工厂和属性仍直接使用；声明为 `async def` 的操作使用 await，事件等待上下文管理器使用 async with。参数超时通常以毫秒计，详细默认行为见各方法正文。

原生说明保留上游命名和示例（可能使用 `playwright` 变量名称），本 SDK 返回的对象属于 `patchright`。上游对于平台、Shadow DOM 等通用行为的说明不扩大本 SDK 的 Windows 支持范围；配套浏览器的差异按中文手册说明使用。

第三方 API 说明源自已安装依赖，版权与许可见 [第三方声明](../THIRD_PARTY_NOTICES.md)。

## 对象

- [APIRequest](APIRequest.md)
- [APIRequestContext](APIRequestContext.md)
- [APIResponse](APIResponse.md)
- [APIResponseAssertions](APIResponseAssertions.md)
- [Browser](Browser.md)
- [BrowserContext](BrowserContext.md)
- [BrowserType](BrowserType.md)
- [CDPSession](CDPSession.md)
- [Clock](Clock.md)
- [ConsoleMessage](ConsoleMessage.md)
- [Credentials](Credentials.md)
- [Debugger](Debugger.md)
- [Dialog](Dialog.md)
- [Disposable](Disposable.md)
- [Download](Download.md)
- [ElementHandle](ElementHandle.md)
- [Expect](Expect.md)
- [FileChooser](FileChooser.md)
- [FormData](FormData.md)
- [Frame](Frame.md)
- [FrameLocator](FrameLocator.md)
- [JSHandle](JSHandle.md)
- [Keyboard](Keyboard.md)
- [Locator](Locator.md)
- [LocatorAssertions](LocatorAssertions.md)
- [Mouse](Mouse.md)
- [Page](Page.md)
- [PageAssertions](PageAssertions.md)
- [Playwright](Playwright.md)
- [Request](Request.md)
- [Response](Response.md)
- [Route](Route.md)
- [Screencast](Screencast.md)
- [Selectors](Selectors.md)
- [Touchscreen](Touchscreen.md)
- [Tracing](Tracing.md)
- [Video](Video.md)
- [WebError](WebError.md)
- [WebMCP](WebMCP.md)
- [WebSocket](WebSocket.md)
- [WebSocketRoute](WebSocketRoute.md)
- [WebStorage](WebStorage.md)
- [Worker](Worker.md)

`ChromiumBrowserContext` 是该版本的 BrowserContext 类型别名，参照 [BrowserContext](BrowserContext.md)。

[字典输入输出结构](types.md)

原生异常为 `patchright.sync_api.Error` / `TimeoutError`（异步入口同名）；TimeoutError 继承 Error。使用 SDK 时同时处理这些原生异常和 [SDK 异常](../diagnostics-errors.md)。
