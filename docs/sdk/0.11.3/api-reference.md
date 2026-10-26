# SDK API 参考

按类型阅读。每个方法包含签名、参数默认值与单位、返回结构、调用片段和注意事项。两个入口语义相同；异步操作标为 await。

| 类型 | 使用章节 |
| --- | --- |
| [YSBrowser](reference/YSBrowser.md) | [browser-context](browser-context.md) |
| [YSContext](reference/YSContext.md) | [browser-context](browser-context.md) |
| [ContextConfig](reference/ContextConfig.md) | [storage](storage.md) |
| [BrowserCapabilities](reference/BrowserCapabilities.md) | [browser-context](browser-context.md) |
| [ProxyHealthResult](reference/ProxyHealthResult.md) | [proxy](proxy.md) |
| [Direct](reference/Direct.md) | [proxy](proxy.md) |
| [FingerprintProfile](reference/FingerprintProfile.md) | [fingerprint](fingerprint.md) |
| [ProxyCheck](reference/ProxyCheck.md) | [proxy](proxy.md) |
| [ProxyConfig](reference/ProxyConfig.md) | [proxy](proxy.md) |
| [ProxyStatus](reference/ProxyStatus.md) | [proxy](proxy.md) |
| [SDKError](reference/SDKError.md) | [diagnostics-errors](diagnostics-errors.md) |
| [ConfigurationError](reference/ConfigurationError.md) | [diagnostics-errors](diagnostics-errors.md) |
| [CompatibilityError](reference/CompatibilityError.md) | [diagnostics-errors](diagnostics-errors.md) |
| [FingerprintLockedError](reference/FingerprintLockedError.md) | [diagnostics-errors](diagnostics-errors.md) |
| [ProxyCheckError](reference/ProxyCheckError.md) | [diagnostics-errors](diagnostics-errors.md) |
| [TrajectoryMouse](reference/TrajectoryMouse.md) | [mouse](mouse.md) |
| [TrajectoryModel](reference/TrajectoryModel.md) | [mouse](mouse.md) |
| [MotionPlan](reference/MotionPlan.md) | [mouse](mouse.md) |
| [MotionRequest](reference/MotionRequest.md) | [mouse](mouse.md) |
| [MotionExecution](reference/MotionExecution.md) | [mouse](mouse.md) |
| [ContextOptions](reference/ContextOptions.md) | [context-options](context-options.md) |
| [MultitaskMouseModel](reference/MultitaskMouseModel.md) | [mouse](mouse.md) |
| [TrajectoryPrediction](reference/TrajectoryPrediction.md) | [mouse](mouse.md) |

## 浏览器安装函数

从 `ysbrowser_sdk.installer` 导入，均为同步函数：

| 函数 | 返回 | 用途 |
| --- | --- | --- |
| [install_browser](installation.md#install_browser) | `Path` | 下载、解压或复用配套浏览器 |
| [get_browser_path](installation.md#get_browser_path) | `Path` | 取得当前安装的浏览器入口 |

参数、默认值、返回值和示例见[安装指南](installation.md#python-安装-api)。
