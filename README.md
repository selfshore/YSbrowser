<div align="center">

# ✨ 𝕐𝕊𝕓𝕣𝕠𝕨𝕤𝕖𝕣 ✨  
**下一代隐私浏览器解决方案**

</div>

[English](README-en.md) | [中文](README.md)

## 🔍 检测通过列表
| 检测平台                                                             | 状态            | 备注    |
|--------------------------------------------------------------------|---------------|-------|
| [browserscan](https://browserscan.net)                             | ✅ 完美通过        | -     |
| [creepjs](https://abrahamjuliot.github.io/creepjs/)                | ✅ 62.5%+      | 持续优化中 |
| [iphey](https://iphey.com)                                         | ✅ 完美通过        | -     |
| [pixelscan](https://pixelscan.net)                                 | ✅ 完美通过        | -     |
| [cloudflare](https://www.cloudflare.com/zh-cn/)                    | ✅ 完美通过        | -     |
| [datadome](https://datadome.co/products/bot-protection/)           | ✅ 完美通过        | -     |
| [brotector](https://kaliiiiiiiiii.github.io/brotector/)            | ✅ 完美通过        | -     |
| [sannysoft](https://bot.sannysoft.com/)                            | ✅ 完美通过        | -     |
| [fingerprint](https://fingerprint.com/products/bot-detection/)     | ✅ 完美通过        | -     |

---

## ⚙️ 核心参数配置
| 参数名                                  | 值                     | 功能描述         |
|--------------------------------------|-----------------------|--------------|
| `--timezone`                         | `Asia/Tokyo`          | 设置浏览器时区      |
| `--fpseed`                           | `12lfisffwfaTYa`      | 指纹生成种子       |
| `--chrome-version`                   | `130.0.7151.70`       | Chrome 浏览器版本 |
| `--nocrash`                          | -                     | 修复自动化工具崩溃问题  |
| `--lang`                             | `zh-CN`               | 设置浏览器语言      |
| `--accept-lang`                      | `zh-CN`               | 设置 HTTP 请求语言 |
| `--proxy-server`                     | `socks5://ip:port`    | 设置代理服务器      |
| `--proxy-auth`                       | `username:password`   | 设置代理认证       |
| `--cpucores`                         | `6`                   | cpu核心数       |
| `--platformversion`                  | `15.4.1`              | 系统版本         |
| `--custom-screen`                    | `1792x1120,1792x1039` | 屏幕宽高         |
| `--force-device-scale-factor`        | `1`                   | 物理像素和css像素比值 |
| `--custom-geolocation`               | `110,220,70`          | 设置纬度和经度，精确距离 |
| `--block-geolocation`               | -          | 屏蔽位置 |
| `--use-fake-device-for-media-stream` | -                     | 设置虚拟媒体设备     |
| `--custom-brand`                     | `"Microsoft Edge"`    | 浏览器品牌        |
| `--close-portscan`                   | -                     | 屏蔽端口扫描       |
| `--iconumber`                        | 1                     | 浏览器编号        |
| `--webrtc-ip-policy`                | `disabled`            | 关闭webtrc的ip泄露（5.2版本以上可用）        |
| `--gpu-fingerprint`                  |    `ANGLE (NVIDIA, NVIDIA GeForce RTX 4060 Direct3D11 vs_5_0 ps_5_0, D3D11)`                | 渲染器        |


---

## 📝 参数详解
### **`timezone`**  
- **功能**：设置浏览器时区
- **建议**：与代理 IP 所在地区时区保持一致
- **示例**：`--timezone=America/New_York`

### **`fpseed`**  
- **功能**：指纹生成种子
- **影响范围**：canvas, webgl, audio, speech, DOMRect, 字体等指纹
- **重要性**：保持相同种子可确保生成一致的浏览器指纹

### **`chrome-version`**  
- **功能**：指定 Chrome 浏览器版本
- **注意**：
  - 版本号与浏览器 API 紧密相关，随意修改可能导致检测风险
  - 自动适配 TLS 指纹（支持版本有限）
  - 仅建议在目标网站有严格版本控制时使用
- **推荐**：使用官方发布的 Chrome 版本号

### **`nocrash`**  
- **功能**：修复 Playwright/Puppeteer 中 iframe 相关的崩溃问题
- **修复问题**：`contentWindow.open` 导致的崩溃

### **`lang` 与 `accept-lang`**
- **功能**：控制浏览器语言和 HTTP 请求头
- **影响**：语音识别(speech)、本地化相关指纹
- **建议**：保持两者一致

### **`proxy-server`**  
- **功能**：设置网络代理服务器
- **格式**：`--proxy-server=[协议]://[地址]:[端口]`
- **协议支持**：
  - `http`：HTTP/HTTPS 代理
  - `socks4`：SOCKS4 代理
  - `socks5`：SOCKS5 代理
- **示例**：
  - `--proxy-server=http://127.0.0.1:8080`

### **`proxy-auth`**  
- **功能**：设置网络代理认证
- **示例**：
  - `--proxy-auth=username:password`

### **`cpucores`**  
- **功能**：cpu的核心数（比如i7是6核，对应navigator.hardwareConcurrency）
- **建议**：使用常见的cpu核心数（6，8，10，12）

### **`platformversion`**  
- **功能**：系统的版本
- **建议**：
  - `macOS`：系统的版本,像15.4.1，15.5等
  - `Windows`：
    | Windows 版本 | 内部版本号 (Build) | Platform-Version | 状态 |
    | :--- | :--- | :--- | :--- |
    | **Windows 11 (24H2)** | 26100+ | `"19.0.0"` | 最新/预览 |
    | **Windows 11 (23H2)** | 22631 | `"17.0.0"` | 主流推荐 |
    | **Windows 11 (22H2)** | 22621 | `"15.0.0"` | 稳定版 |
    | **Windows 11 (21H2)** | 22000 | `"13.0.0"` | 初始版 |
    | **Windows 10 (22H2)** | 19045 | `"10.0.0"` | Win10 最常见 |
    | **Windows 10 (21H2)** | 19044 | `"10.0.0"` | 稳定版 |
    | **Windows 8.1** | 9600 | `"6.3.0"` | 已过时 |
    | **Windows 8** | 9200 | `"6.2.0"` | 已过时 |
    | **Windows 7** | 7601 | `"6.1.0"` | 已过时 |

### **`custom-screen`**  
- **功能**：屏幕的宽高和可用宽高，对应javascript里的screen中width,height,availwidth,availheight。
- **建议**：如果设置它，width和height是必须的，availwidth和availheight如果不知道怎么设置可不加，浏览器会自动更改，尽量使用真实的分辨率。
- **示例**：
  - `1792x1120,1792x1039`
  - `1792x1120`

### **`force-device-scale-factor`**  
- **功能**：物理像素和css像素比值，也就是devicePixelRatio
- **示例**：
  - `1`
  - `2`

### **`custom-geolocation`和`block-geolocation`** 
- **功能**：custom-geolocation设置经纬度（navigator.geolocation.getCurrentPosition）,block-geolocation屏蔽位置功能
- **示例**：
  - `--custom-geolocation=110,220,70`(纬度,经度,精度)

### **`use-fake-device-for-media-stream`**
- **功能**：伪造媒体设备（navigator.mediaDevices.enumerateDevices）

### **`custom-brand`**
- **功能**：伪装浏览器品牌
- **建议**：如果伪装成真实的浏览器品牌，请携带user-agent这个参数，如果虚构不存在的品牌就不用携带user-agent。
- **示例**：
  - `--custom-brand="Microsoft Edge"
--user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0"`
  - `--custom-brand="fake brand"`

### **`close-portscan`**
- **功能**：屏蔽端口扫描

### **`webrtc-ip-policy`**
- **功能**：防止webrtc泄露真实IP
- **示例**：
  - `--webrtc-ip-policy=disabled`

### **`gpu-fingerprint`**
- **功能**：修改渲染器
- **示例**：
    | 序号 | 完整 ANGLE 渲染器字符串 |
    | :--- | :--- |
    | **0** | `ANGLE (NVIDIA, NVIDIA GeForce GTX 960 Direct3D11 vs_5_0 ps_5_0, D3D11)` |
    | **1** | `ANGLE (AMD, AMD Radeon R9 200 Series Direct3D11 vs_5_0 ps_5_0, D3D11)` |
    | **2** | `ANGLE (NVIDIA, NVIDIA GeForce GTX 770 Direct3D11 vs_5_0 ps_5_0, D3D11)` |
    | **3** | `ANGLE (Intel, Intel(R) HD Graphics 4600 Direct3D11 vs_5_0 ps_5_0, D3D11)` |
    | **4** | `ANGLE (AMD, AMD Radeon HD 8800 Series Direct3D11 vs_5_0 ps_5_0, D3D11)` |
    | **5** | `ANGLE (NVIDIA, NVIDIA GeForce GT 730 Direct3D11 vs_5_0 ps_5_0, D3D11)` |
    | **6** | `ANGLE (Intel, Intel(R) HD Graphics 4400 Direct3D11 vs_5_0 ps_5_0, D3D11)` |
    | **7** | `ANGLE (AMD, AMD Radeon R7 200 Series Direct3D11 vs_5_0 ps_5_0, D3D11)` |
    | **8** | `ANGLE (NVIDIA, NVIDIA GeForce GTX 1050 Direct3D11 vs_5_0 ps_5_0, D3D11)` |
    | **9** | `ANGLE (NVIDIA, NVIDIA GeForce GTX 980 Ti Direct3D11 vs_5_0 ps_5_0, D3D11)` |
    | **10** | `ANGLE (NVIDIA, NVIDIA GeForce GTX 970M Direct3D11 vs_5_0 ps_5_0, D3D11)` |
    | **11** | `ANGLE (NVIDIA, NVIDIA GeForce GTX 1080 Direct3D11 vs_5_0 ps_5_0, D3D11)` |
---

## 基本用法
- **警告**：由于没签名，mac上要执行xattr -cr YSbrowser.app才能使用。
- **警告**：下面是基本参数，保持环境隔离必须携带--user-data-dir。
- **警告**：如果需要console打印对象请携带openConsole，例如console.log("openConsole",{})。
```bash
chrome --timezone=Asia/Hong_Kong --lang=zh-CN --accept-lang=zh-CN,en --fpseed=121e0opwlltx  --user-data-dir=./my_user_data 
```

## 模拟brave
```bash
chrome --timezone=Asia/Hong_Kong --lang=zh-CN --accept-lang=zh-CN,en --fpseed=121e0opwlltx  --user-data-dir=./my_user_data --chrome-version=137.0.0.0 --custom-brand=Brave --enable-features=BraveAPI --disable-features=keyboardAPI,NetworkAPI
```

## 🤖 自动化工具支持
### 已消除的自动化特征
- ✅ CDP 检测
- ✅ Selenium 特征
- ✅ Playwright 特征(仅去掉部分，仍建议使用patchright)
- ✅ DrissionPage 特征

### 关键技术改进
1. **鼠标事件修复**：彻底解决 CDP 的 `Input.dispatchMouseEvent` 缺陷
2. **Shadow DOM 访问**：通过 `opshadowRoot` 访问封闭式 shadow DOM
3. **自动化检测绕过**：消除常见自动化工具特征标记

---

## 🐞 调试支持
- **重命名调试器**：`debugger` → `debuging`（绕过检测）
- **控制台检查**：绕过常见的控制台属性检查

---

## 🚧 开发路线图
| 功能                     | 状态   | 说明                                                                 |
|--------------------------|--------|----------------------------------------------------------------------|
| GPU 指纹伪造             | ⚙️ 开发中 | 增强图形指纹的伪装能力                                               |
> **提示**：项目持续更新中，欢迎提交 Issue！如果想帮助我收集更多指纹，请点击[网址](https://www.hanyiting.com)

## ⚖️ 免责声明
> **注意：** 本项目严禁用于非法用途。
<details>
<summary>点击展开详细法律合规声明</summary>

1. **法律合规性**：使用者应在遵守当地法律的前提下使用，严禁将本工具用于任何违法违规行为。
2. **风险自担**：由于使用不当或用于非法目的所产生的一切后果（包括法律责任和经济损失），均由使用者本人承担，与开发者无关。
3. **无担保性**：本工具按“原样”提供，开发者不对因使用本工具导致的任何损失负责。
4. **禁止商用**：本工具仅供学习交流，严禁用于任何非法盈利活动。

</details>

## 求职：有合适的爬虫和反爬岗位欢迎内推

### 交流群
<img src="QQ20250723-104659.png" alt="Q群1043047569" width="400" height="400">
