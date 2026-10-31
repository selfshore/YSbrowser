# FingerprintProfile

[SDK API 目录](../api-reference.md) · [使用章节](../fingerprint.md)

## 导入与准备

```python
from ysbrowser_sdk.sync_api import FingerprintProfile

profile = FingerprintProfile(fpseed="account-001", cpu_cores=8)
```

## 构造参数

```python signature
FingerprintProfile(fpseed: 'str | None' = None, audio_seed: 'str | None' = None, canvas_seed: 'str | None' = None, webgl_seed: 'str | None' = None, webgl_profile: 'str | None' = None, server_gpu_profile: 'str | None' = None, font_seed: 'str | None' = None, speech_seed: 'str | None' = None, screen_seed: 'str | None' = None, rect_seed: 'str | None' = None, dom_rect_seed: 'str | None' = None, svg_rect_seed: 'str | None' = None, cpu_cores: 'int | None' = None, device_memory: 'float | None' = None, timezone: 'str | None' = None, language: 'str | None' = None, accept_language: 'str | None' = None, platform_version: 'str | None' = None, chrome_version: 'str | None' = None, geolocation: 'str | None' = None, web_rtc_ip_policy: 'str | None' = None, web_rtc_proxy_ip: 'str | None' = None) -> None
```

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `fpseed` | str \| None | `None` | 总 seed，例如 `"account-001"`；作为未单独指定模块 seed 的来源 |
| `audio_seed` | str \| None | `None` | Audio 指纹模块 seed |
| `canvas_seed` | str \| None | `None` | Canvas 指纹模块 seed；实际适用的绘制路径取决于配套浏览器与 GPU 后端 |
| `webgl_seed` | str \| None | `None` | WebGL 模块 seed；与显式 GPU profile 分别配置 |
| `webgl_profile` | str \| None | `None` | 普通 WebGL profile ID，受实际后端兼容条件约束 |
| `server_gpu_profile` | str \| None | `None` | 当前 Context 的服务端 GPU 呈现型号，例如 `"rtx3060"`；从 `browser.capabilities.gpu_profiles` 选择 |
| `font_seed` | str \| None | `None` | 字体模块 seed |
| `speech_seed` | str \| None | `None` | 浏览器语音列表选择 seed；固定 seed 用于保持选择稳定 |
| `screen_seed` | str \| None | `None` | 屏幕指标选择 seed；不是指定视口宽高的接口 |
| `rect_seed` | str \| None | `None` | Rect 模块的通用 seed |
| `dom_rect_seed` | str \| None | `None` | DOM Rect 专用 seed |
| `svg_rect_seed` | str \| None | `None` | SVG Rect 专用 seed |
| `cpu_cores` | int \| None | `None` | 逻辑处理器数量，整数 1–256 |
| `device_memory` | float \| None | `None` | 设备内存数值，通常按 GB 配置；有限数且大于 0、不超过 1024，可传整数 |
| `timezone` | str \| None | `None` | IANA 时区，如 `"Asia/Shanghai"`、`"Europe/London"` |
| `language` | str \| None | `None` | 浏览器语言，如 `"zh-CN"` |
| `accept_language` | str \| None | `None` | Accept-Language，如 `"zh-CN,zh;q=0.9"` |
| `platform_version` | str \| None | `None` | 平台版本呈现值，如 `"15.0.0"`；不是安装操作系统版本 |
| `chrome_version` | str \| None | `None` | Chrome 版本呈现字符串，如 `"154.0.0.0"`；不会改变实际内核 |
| `geolocation` | str \| None | `None` | `"纬度,经度[,精度]"`，如 `"31.2304,121.4737,50"`；站点仍需地理位置权限 |
| `web_rtc_ip_policy` | str \| None | `None` | 使用 `"disabled"` 或 `"proxy"` 限制非代理 UDP；不会关闭整个 WebRTC API |
| `web_rtc_proxy_ip` | str \| None | `None` | 合法 IPv4/IPv6 地址，用于指定 ICE/SDP 地址呈现；不设置实际代理路由，也不自动检测出口 |


## 字段与返回结构

直接用 `对象.字段` 读取；需要普通字典时用 `dataclasses.asdict(对象)`，或使用本类型提供的 to_dict。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `fpseed` | str \| None | 总 seed，例如 `"account-001"`；作为未单独指定模块 seed 的来源 |
| `audio_seed` | str \| None | Audio 指纹模块 seed |
| `canvas_seed` | str \| None | Canvas 指纹模块 seed；实际适用的绘制路径取决于配套浏览器与 GPU 后端 |
| `webgl_seed` | str \| None | WebGL 模块 seed；与显式 GPU profile 分别配置 |
| `webgl_profile` | str \| None | 普通 WebGL profile ID，受实际后端兼容条件约束 |
| `server_gpu_profile` | str \| None | 当前 Context 的服务端 GPU 呈现型号，例如 `"rtx3060"`；从 `browser.capabilities.gpu_profiles` 选择 |
| `font_seed` | str \| None | 字体模块 seed |
| `speech_seed` | str \| None | 浏览器语音列表选择 seed；固定 seed 用于保持选择稳定 |
| `screen_seed` | str \| None | 屏幕指标选择 seed；不是指定视口宽高的接口 |
| `rect_seed` | str \| None | Rect 模块的通用 seed |
| `dom_rect_seed` | str \| None | DOM Rect 专用 seed |
| `svg_rect_seed` | str \| None | SVG Rect 专用 seed |
| `cpu_cores` | int \| None | 逻辑处理器数量，整数 1–256 |
| `device_memory` | float \| None | 设备内存数值，通常按 GB 配置；有限数且大于 0、不超过 1024，可传整数 |
| `timezone` | str \| None | IANA 时区，如 `"Asia/Shanghai"`、`"Europe/London"` |
| `language` | str \| None | 浏览器语言，如 `"zh-CN"` |
| `accept_language` | str \| None | Accept-Language，如 `"zh-CN,zh;q=0.9"` |
| `platform_version` | str \| None | 平台版本呈现值，如 `"15.0.0"`；不是安装操作系统版本 |
| `chrome_version` | str \| None | Chrome 版本呈现字符串，如 `"154.0.0.0"`；不会改变实际内核 |
| `geolocation` | str \| None | `"纬度,经度[,精度]"`，如 `"31.2304,121.4737,50"`；站点仍需地理位置权限 |
| `web_rtc_ip_policy` | str \| None | 使用 `"disabled"` 或 `"proxy"` 限制非代理 UDP；不会关闭整个 WebRTC API |
| `web_rtc_proxy_ip` | str \| None | 合法 IPv4/IPv6 地址，用于指定 ICE/SDP 地址呈现；不设置实际代理路由，也不自动检测出口 |

## 方法与属性索引

- [FingerprintProfile.to_cdp](#fingerprintprofile-to-cdp)

## FingerprintProfile.to_cdp

验证并转换为协议字段字典。

```python signature
to_cdp() -> 'dict[str, Any]'
```

**同步计算/工厂方法；异步程序中也不加 await。**

### 参数

此方法没有调用参数。


### 返回值

返回已指定字段的 camelCase 字典，省略 None。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
data = profile.to_cdp()
# data 用于协议字段转换；包含凭据时不要写入公开日志。
```

### 注意事项

只能在指纹尚未锁定时应用；to_cdp() 只转换字段，不会修改浏览器。

[更多示例和完整业务规则](../fingerprint.md)
