# 指纹与 GPU

[返回目录](README.md)

## 创建指纹配置

```python
from ysbrowser_sdk.sync_api import YSBrowser, FingerprintProfile

profile = FingerprintProfile(
    fpseed="account-001",
    cpu_cores=8,
    device_memory=8,
    timezone="Asia/Shanghai",
    language="zh-CN",
    accept_language="zh-CN,zh;q=0.9,en;q=0.8",
    server_gpu_profile="rtx3060",
)

with YSBrowser() as browser:
    context = browser.new_context(fingerprint=profile)
    print(context.fingerprint_status())
    page = context.new_page()
```

`FingerprintProfile` 是不可重新赋值字段的数据类。所有字段默认 `None`，表示不在本次 profile 中显式指定。所有 seed 使用非空字符串；数字形式的 seed 也应写成字符串，如 `"12345"`。

## 全部字段

| 字段 | 类型 | 含义与传入方式 |
| --- | --- | --- |
| `fpseed` | `str \| None` | 总 seed，例如 `"account-001"`；作为未单独指定模块 seed 的来源 |
| `audio_seed` | `str \| None` | Audio 指纹模块 seed |
| `canvas_seed` | `str \| None` | Canvas 指纹模块 seed；实际适用的绘制路径取决于配套浏览器与 GPU 后端 |
| `webgl_seed` | `str \| None` | WebGL 模块 seed；与显式 GPU profile 分别配置 |
| `webgl_profile` | `str \| None` | 普通 WebGL profile ID，受实际后端兼容条件约束 |
| `server_gpu_profile` | `str \| None` | 当前 Context 的服务端 GPU 呈现型号，例如 `"rtx3060"`；从 `browser.capabilities.gpu_profiles` 选择 |
| `font_seed` | `str \| None` | 字体模块 seed |
| `speech_seed` | `str \| None` | 浏览器语音列表选择 seed；固定 seed 用于保持选择稳定 |
| `screen_seed` | `str \| None` | 屏幕指标选择 seed；不是指定视口宽高的接口 |
| `rect_seed` | `str \| None` | Rect 模块的通用 seed |
| `dom_rect_seed` | `str \| None` | DOM Rect 专用 seed |
| `svg_rect_seed` | `str \| None` | SVG Rect 专用 seed |
| `cpu_cores` | `int \| None` | 逻辑处理器数量，整数 1–256 |
| `device_memory` | `float \| None` | 设备内存数值，通常按 GB 配置；有限数且大于 0、不超过 1024，可传整数 |
| `timezone` | `str \| None` | IANA 时区，如 `"Asia/Shanghai"`、`"Europe/London"` |
| `language` | `str \| None` | 浏览器语言，如 `"zh-CN"` |
| `accept_language` | `str \| None` | Accept-Language，如 `"zh-CN,zh;q=0.9"` |
| `platform_version` | `str \| None` | 平台版本呈现值，如 `"15.0.0"`；不是安装操作系统版本 |
| `chrome_version` | `str \| None` | Chrome 版本呈现字符串，如 `"154.0.0.0"`；不会改变实际内核 |
| `geolocation` | `str \| None` | `"纬度,经度[,精度]"`，如 `"31.2304,121.4737,50"`；站点仍需地理位置权限 |
| `web_rtc_ip_policy` | `str \| None` | 使用 `"disabled"` 或 `"proxy"` 限制非代理 UDP；不会关闭整个 WebRTC API |
| `web_rtc_proxy_ip` | `str \| None` | 合法 IPv4/IPv6 地址，用于指定 ICE/SDP 地址呈现；不设置实际代理路由，也不自动检测出口 |

数值和非空字符串由 SDK 验证；时区、型号和具体值还需配套浏览器支持。布尔值不能代替 CPU/内存数值。

### seed 的使用

同一账户可长期使用相同的 `fpseed`；需要固定某个模块时显式设置对应的模块 seed。Context 指定 `fpseed` 后，未显式提供的模块 seed 使用该 Context 的总 seed，而不是继续沿用进程级专用 seed。未覆盖的其他字段遵循浏览器的继承规则。

`screen_seed` 不保证每次更换都得到不同屏幕尺寸。需要控制自动化页面工作区域时，使用 `ContextOptions(viewport={"width": 1280, "height": 720})`。语言、时区、位置、CPU、内存与 GPU 均为独立字段，需要调用方按用途配置。

## set_fingerprint 与 fingerprint_status

```python
context.set_fingerprint(FingerprintProfile(fpseed="another-account"))
status = context.fingerprint_status()
print(status["locked"])
print(status["profile"])
```

以上片段要求 Context 尚未创建 renderer。异步入口分别使用 `await`。

- `set_fingerprint(profile: FingerprintProfile) -> None`：设置一份 profile，按完整配置传入需要保留的字段；不要将多次调用当成字段增量合并。
- `fingerprint_status() -> dict`：返回浏览器原生状态。其中 `locked: bool` 表示是否已经锁定；`profile: dict` 为配置字段，键使用 `fpseed`、`cpuCores`、`serverGpuProfile` 等原生名称。原生协议可附带其他字段。
- 一旦 Context 启动 renderer，修改会抛 `FingerprintLockedError`。应新建 Context，再应用指纹和登录状态。关闭页面不应当作解除锁定的手段。
- 创建 Context 时通过 `fingerprint=` 传入最方便，可避免在打开页面后才设置。

`profile.to_cdp() -> dict` 仅转换并验证字段，不应用到浏览器；省略 `None`，例如 `cpu_cores` 转成 `cpuCores`，`web_rtc_ip_policy` 转成 `webRtcIpPolicy`。

## GPU 配置

```python
from ysbrowser_sdk.sync_api import YSBrowser, FingerprintProfile

with YSBrowser(
    context_gpu=True,
    server_gpu_backend=None,
) as browser:
    print(browser.capabilities.gpu_profiles)
    a = browser.new_context(fingerprint=FingerprintProfile(server_gpu_profile="rtx3060"))
    b = browser.new_context(fingerprint=FingerprintProfile(server_gpu_profile="uhdgraphics770"))
```

`context_gpu=True` 是默认值。不同 Context 可以选择不同呈现型号，实际执行后端仍由浏览器进程共享。省略/None 时 Windows 选择 `warp`，Linux 选择 `llvmpipe`。Linux 还可显式使用 `native`、`software` 或 `swiftshader`；Windows 可选 `warp` 或 `swiftshader`。能力与输出取决于实际后端。

需要浏览器原生 GPU 路径时使用 `context_gpu=False`，并省略启动级 `server_gpu_profile`。该情况下不能再直接请求 Context 服务端 GPU profile。

显式有效的 `server_gpu_profile` 优先于普通 `webgl_profile` 的 GPU 身份选择；不会使软件后端变成对应实体显卡。Canvas、WebGL 和 WebGPU 的执行效果仍受后端与绘制方式影响。

配套浏览器提供的简写型号包括：

```text
gt610 gt710 gt730 gtx750ti gtx1050ti gtx1660super
rtx2060super rtx2070 rtx2080ti rtx3060 rtx3060ti
rtx3070 rtx3070ti rtx3080ti rtx4060 rtx4070 rtx4070super rtx4090 rtx5080
rx6500xt rx6700 rx6750gre12gb
hdgraphics630 uhdgraphics630 uhdgraphics730 uhdgraphics770
```

完整 ID 列表以运行时 `browser.capabilities.gpu_profiles` 为准，包括精确设备 ID 的长名称。不可用或未获浏览器确认的配置会报错。
