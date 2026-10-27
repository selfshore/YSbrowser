# 安装与快速开始

[返回目录](README.md)

## 环境要求

| 项目 | 要求 |
| --- | --- |
| 操作系统 | Windows、Linux；macOS 尚未验证 |
| Python | 3.10+ |
| Python 包 | `ysbrowser-sdk` 0.11.4，导入名称 `ysbrowser_sdk` |
| 配套依赖 | Patchright Python 1.64.2，内置 driver 1.64.1；不要单独升级 |
| 浏览器 | 提供 Context 指纹、代理、能力查询和代理检查扩展的 YSbrowser |
| 浏览器文件 | 通过安装命令下载，或手动提供浏览器文件；同时保留目录内的依赖文件 |

## 安装 Python 包

```powershell
pip install ysbrowser-sdk
```

更新时使用 `pip install --upgrade ysbrowser-sdk`。如果电脑上有多个 Python，请在运行脚本的同一环境里安装，也可使用 `python -m pip install ysbrowser-sdk`。

## Linux 浏览器准备

Linux 使用原生 `chrome` 和对应资源。可以将本平台压缩包直链设置为
`YSBROWSER_LINUX_BROWSER_URL`，或在命令中显式传入发布者提供的地址：

```bash
python -m ysbrowser_sdk install --url "$YSBROWSER_LINUX_BROWSER_URL"
```

也可直接传 `YSBrowser("./browser/chrome")`。SDK 不会在 Linux 默认下载 Windows
浏览器。首次运行需要 Chromium 的共享库、字体和沙箱依赖；WSL 中显示界面及
播放系统语音需要可用的 WSLg 桌面/音频连接。下面的目录图和未指定地址的下载
命令展示 Windows 安装；注册完成后，两端都可用 `YSBrowser()` 查找当前入口。

## 自动下载浏览器

以下未指定 --url 的命令适用于 Windows。在项目工作目录执行，默认下载本包内置的 [YSBrowser 6.3](https://github.com/selfshore/YSbrowser/releases/download/6.3/chrome.7z)：

```powershell
python -m ysbrowser_sdk install
```

等价的控制台命令：

```powershell
ysbrowser-sdk install
```

可选的 `--url` 用于覆盖内置地址，支持 `.7z` 和 `.zip`，包括 GitHub Release 的资产下载地址和 HTTP 跳转。传入的是压缩包直链，不是 Release 网页。压缩包内可以有外层目录，但必须包含当前平台唯一的入口（Windows 为 `chrome.exe`，Linux 为 `chrome`）。

默认目录结构如下，`<安装标识>` 由安装器生成：

```text
你的项目/
├─ main.py
└─ browsers/
   ├─ installed.json
   ├─ .install.lock
   └─ <安装标识>/
      └─ Chrome-bin/
         ├─ chrome.exe
         └─ 其他浏览器文件
```

安装成功后，标准输出为 JSON：

```json
{
  "executable_path": "<安装得到的 chrome.exe 绝对路径>"
}
```

`executable_path` 是字符串，可以直接传给 `YSBrowser`。返回绝对路径便于程序确定同一个文件；调用示例不依赖个人电脑路径。下载进度写入标准错误，不混入 JSON。

安装结束会删除下载压缩包及临时解压目录。浏览器文件、`installed.json` 和用于并发控制的 `.install.lock` 会保留。安装目录不是用户数据目录；登录状态的保存和恢复见[配置与登录状态](storage.md)。

安装命令只负责下载、校验、解压和记录入口，不会启动浏览器。下载成功不代表浏览器版本兼容，扩展接口可用性用后面的 `doctor` 检查。

### 安装命令全部参数

| 参数 | 默认值 | 含义 |
| --- | --- | --- |
| `--url` | 内置的 YSBrowser 6.3 下载地址 | HTTP(S) 压缩包直链，支持查询参数；不接受 URL 内嵌用户名和密码。 |
| `--directory` | 环境变量或 `./browsers` | 安装目录；显式传入优先，相对路径以当前工作目录为基准。 |
| `--sha256` | 不指定 | 压缩包 SHA256，64 位十六进制字符串，不区分大小写；不匹配则失败。 |
| `--timeout` | `60` | 网络 socket 超时，单位秒，必须大于 0；不是整个任务的总时限。 |
| `--quiet` | 不启用 | 隐藏进度，仍输出成功结果或错误 JSON。 |

```powershell
python -m ysbrowser_sdk install --directory ./runtime/browsers --timeout 120
```

相同 URL 已安装、入口文件存在，且指定的 SHA256 与记录一致时会复用，并设为当前版本。未指定 SHA256 时，同 URL 也会复用，不再联网检查远端是否变化。因此发布新版应使用新版本 URL；同 URL 内容变化时，应提供新的 SHA256。

切换新版本不会删除旧版已解压的浏览器，也不会改变正在运行的浏览器。新的 `YSBrowser()` 实例才读取当前安装；下载、校验或解压失败时原有有效安装不变。缓存复用检查入口存在和记录的压缩包校验值，不会逐个重新校验已解压文件。

## 自定义目录和相对路径

`YSBrowser()` 的查找顺序为：显式 `executable_path` → `YSBROWSER_BROWSERS_PATH` 下的清单 → 当前工作目录 `./browsers` 下的清单。未找到时抛 `BROWSER_NOT_INSTALLED`，构造函数不会联网下载。

`--directory` 不会永久修改环境变量。使用自定义目录时，可在当前 PowerShell 会话中设置：

```powershell
$env:YSBROWSER_BROWSERS_PATH = "./runtime/browsers"
python -m ysbrowser_sdk install
python main.py
```

也可在代码中显式获取路径：

```python
from ysbrowser_sdk.installer import get_browser_path
from ysbrowser_sdk.sync_api import YSBrowser

with YSBrowser(get_browser_path("./runtime/browsers")) as browser:
    context = browser.new_context()
```

手动解压浏览器时，直接传相对路径，不需要安装清单：

```python
from ysbrowser_sdk.sync_api import YSBrowser

with YSBrowser("./browser/chrome.exe", headless=False) as browser:
    context = browser.new_context()
```

相对路径按**进程工作目录**解释，不是按脚本所在目录解释。IDE 和定时任务需保持工作目录一致；也可固定到脚本所在项目目录：

```python
from pathlib import Path
from ysbrowser_sdk.installer import get_browser_path
from ysbrowser_sdk.sync_api import YSBrowser

project = Path(__file__).resolve().parent
with YSBrowser(get_browser_path(project / "browsers")) as browser:
    context = browser.new_context()
```

## Python 安装 API

```python
from ysbrowser_sdk.installer import install_browser, get_browser_path
```

### install_browser

```python signature
install_browser(url: str | None = None, *, directory: str | Path | None = None,
                sha256: str | None = None, timeout_s: float = 60,
                progress: bool = False) -> Path
```

| 参数 | 类型 / 默认值 | 含义 |
| --- | --- | --- |
| `url` | `str \| None = None` | Windows 省略时使用内置 YSBrowser 6.3 地址；Linux 省略时读取 YSBROWSER_LINUX_BROWSER_URL，未配置则报 LINUX_BROWSER_URL_REQUIRED。也可显式提供本平台原生压缩包直链。 |
| `directory` | `str \| Path \| None = None` | 安装目录；`None` 先读取 `YSBROWSER_BROWSERS_PATH`，未设置时使用 `./browsers`。 |
| `sha256` | `str \| None = None` | 预期压缩包 SHA256；64 位十六进制字符串。用于校验本次下载或匹配现有安装记录。 |
| `timeout_s` | `float = 60` | 网络 socket 超时秒数，有限且大于 0。 |
| `progress` | `bool = False` | 为 `True` 时向标准错误打印下载和解压进度。 |

返回 `pathlib.Path`，指向安装成功后的本平台入口绝对路径（Windows chrome.exe / Linux chrome）；缓存命中时同样返回 Path。失败抛 `SDKError`，非法参数抛其子类 `ConfigurationError`，不会返回 `None`。

```python
from ysbrowser_sdk.installer import install_browser
from ysbrowser_sdk.sync_api import YSBrowser

executable = install_browser(
    directory="./browsers",
    timeout_s=120,
    progress=True,
)
with YSBrowser(executable) as browser:
    context = browser.new_context()
```

这是同步函数，通常在业务启动前调用。已有异步事件循环中需要安装时，用线程调用以免阻塞其他任务：

```python
import asyncio
from ysbrowser_sdk.installer import install_browser
from ysbrowser_sdk.async_api import YSBrowser

async def main():
    executable = await asyncio.to_thread(
        install_browser,
        directory="./browsers",
    )
    async with YSBrowser(executable) as browser:
        context = await browser.new_context()

if __name__ == "__main__":
    asyncio.run(main())
```

### get_browser_path

```python signature
get_browser_path(directory: str | Path | None = None) -> Path
```

唯一参数 `directory` 与 `install_browser` 的同名参数含义相同，可按位置传入。返回当前有效安装的本平台入口绝对 Path；只读取清单和检查入口存在，不联网、不启动浏览器。无有效安装时抛 `BROWSER_NOT_INSTALLED`，清单损坏时抛 `BROWSER_INSTALL_INVALID`。

```python
from ysbrowser_sdk.installer import get_browser_path

executable = get_browser_path()
print(executable.name)  # chrome.exe
```

## 安装常见问题

| 错误码 | 处理方式 |
| --- | --- |
| `LINUX_BROWSER_URL_REQUIRED` | 提供本平台原生压缩包 --url、配置 YSBROWSER_LINUX_BROWSER_URL，或直接指定已有 Linux 浏览器路径。 |
| `BROWSER_NOT_INSTALLED` | 执行安装命令；核对工作目录和 `YSBROWSER_BROWSERS_PATH`。 |
| `BROWSER_DOWNLOAD_FAILED` | 检查直链、网络、HTTP 状态、代理、权限及空间；失败可重试，重新下载，不支持断点续传。 |
| `BROWSER_CHECKSUM_MISMATCH` | 核对发布者提供的 SHA256 与版本地址；旧安装仍有效。 |
| `BROWSER_ARCHIVE_INVALID` | 需要包含当前平台唯一原生入口的压缩包（Windows chrome.exe / Linux chrome），不能是网页或安装器。 |
| `BROWSER_ARCHIVE_UNSAFE` | 不支持加密包、链接、特殊文件、越界或冲突路径，请重新生成常规发行包。 |
| `BROWSER_EXTRACT_FAILED` | 压缩包损坏、编码不支持或文件写入失败；推荐常规 LZMA/LZMA2 的 7z 或 zip，不支持 7z BCJ2 编码。 |
| `BROWSER_INSTALL_DISK_FULL` | 释放安装盘空间，下载和解压需要同时占用空间。 |
| `BROWSER_INSTALL_BUSY` | 等待同目录的安装任务结束，不要删除正在使用的锁文件。 |
| `BROWSER_INSTALL_INVALID` | 恢复安装清单，或选择新的目录重新安装。 |
| `BROWSER_INSTALL_FAILED` | 激活失败，检查目录权限、文件占用和空间；上一次有效安装不变。 |
| `BROWSER_CAPABILITIES_UNAVAILABLE` | 安装包含 SDK 配套扩展接口的浏览器版本。 |

下载使用 Python 的网络配置，可通过 `HTTP_PROXY` / `HTTPS_PROXY` 环境变量配置代理；不使用尚未启动的 Context 的 `ProxyConfig`。

正常成功、异常或取消时会清理临时目录。断电或强制结束进程可能残留 `.download-*`，确认没有安装任务运行后可删除；不要删除当前安装清单和浏览器文件。

录制视频还需要 Patchright 对应的 FFmpeg；仅在使用录屏且未安装该资源时执行：

```powershell
python -m patchright install ffmpeg
```

接下来保存同步或异步示例为 `main.py`，在安装浏览器的同一工作目录执行 `python main.py`。默认显示浏览器，程序结束关闭会话，但安装文件保留。


## 同步程序

```python
from ysbrowser_sdk.sync_api import (
    YSBrowser, FingerprintProfile, ContextOptions, Direct,
)

def main():
    with YSBrowser(headless=False) as browser:
        context = browser.new_context(
            name="demo",
            fingerprint=FingerprintProfile(fpseed="demo", cpu_cores=8, device_memory=8),
            proxy=Direct(),
            options=ContextOptions(viewport={"width": 1280, "height": 720}),
        )
        page = context.new_page()
        page.set_content('<input aria-label="姓名"><button>提交</button>')
        page.get_by_label("姓名").fill("张三")
        page.get_by_role("button", name="提交").click()
        print(page.get_by_label("姓名").input_value())
        context.save_storage_state("state/demo.json")

if __name__ == "__main__":
    main()
```

同步对象必须在创建它的线程使用。已有正在运行的 asyncio 事件循环时，使用异步入口。

## 异步程序

```python
import asyncio
from ysbrowser_sdk.async_api import YSBrowser, FingerprintProfile, ContextOptions

async def main():
    async with YSBrowser(headless=False) as browser:
        context = await browser.new_context(
            fingerprint=FingerprintProfile(fpseed="async-demo"),
            options=ContextOptions(viewport={"width": 1280, "height": 720}),
        )
        page = await context.new_page()
        await page.set_content('<button onclick="this.textContent=\'完成\'">开始</button>')
        await page.get_by_role("button", name="开始").click()
        print(await page.get_by_role("button").inner_text())
        print(browser.diagnostics())  # 此方法不加 await
        mouse = context.mouse(page)  # 工厂不加 await
        await mouse.synchronize(100, 100)
        result = await mouse.move(400, 250, duration_s=0.6, seed=10)
        print(result.plan.source, result.elapsed_s)

if __name__ == "__main__":
    asyncio.run(main())
```

## 命令行

安装后提供 `ysbrowser-sdk` 命令，也可使用 `python -m ysbrowser_sdk`。

### info

```powershell
python -m ysbrowser_sdk info
```

不启动浏览器。成功时向标准输出写入 JSON：

```json
{
  "sdk_version": "0.11.4",
  "patchright_version": "1.64.2",
  "driver_version": "1.64.1",
  "adapter_id": "patchright-python-1.64.2-driver-1.64.1",
  "validated_platform": "Windows",
  "browser_bundled": false
}
```

### doctor

```powershell
python -m ysbrowser_sdk doctor
```

| 参数 | 必填 | 含义 |
| --- | --- | --- |
| `--executable` | 否 | 配套浏览器可执行文件路径，如 `./browser/chrome.exe`；省略时读取安装清单 |
| `--headless` | 否 | 无界面启动；省略时显示浏览器 |

临时启动浏览器和 Context，查询能力、指纹锁定状态、代理状态，然后关闭。输出包含 `info` 字段及 `capabilities`、`browser`、`context_gpu`、`server_gpu_backend`、`media_router`、`server_gpu_profile`、`context_count`、`connected`、`contexts`、`custom_cdp`、`fingerprint_locked`、`proxy_status`。各结构见[浏览器与 Context](browser-context.md)和[代理](proxy.md)。命令不验证某个代理供应商是否可用。

成功退出码为 `0`；捕获到 SDK 异常时输出异常 JSON 并以 `1` 退出；命令行参数错误由参数解析器报告并以 `2` 退出。

