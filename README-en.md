<div align="center">

# ✨ 𝕐𝕊𝕓𝕣𝕠𝕨𝕤𝕖𝕣 ✨  
**Next-Generation Privacy Browser Solution**

</div>

[English](README-en.md) | [中文](README.md)

## 🔍 Tested & Passed
| Detection Platform                                                  | Status       | Notes                |
|---------------------------------------------------------------------|--------------|----------------------|
| [browserscan](https://browserscan.net)                              | ✅ Perfect    | -                    |
| [creepjs](https://abrahamjuliot.github.io/creepjs/)                 | ✅ 62.5%+     | Continuous improvement |
| [iphey](https://iphey.com)                                          | ✅ Perfect    | -                    |
| [pixelscan](https://pixelscan.net)                                  | ✅ Perfect    | -                    |
| [cloudflare](https://www.cloudflare.com/zh-cn/)                     | ✅ Perfect    | Requires image loading |
| [datadome](https://datadome.co/products/bot-protection/)            | ✅ Perfect    | -                    |
| [brotector](https://kaliiiiiiiiii.github.io/brotector/)             | ✅ Perfect    | -                    |
| [sannysoft](https://bot.sannysoft.com/)                             | ✅ Perfect    | -                    |
| [fingerprint](https://fingerprint.com/products/bot-detection/)      | ✅ Perfect    | -                    |

---

## ⚙️ Core Parameters
| Parameter          | Value            | Description                 |
|--------------------|------------------|-----------------------------|
| `--timezone`       | `Asia/Tokyo`     | Set browser timezone        |
| `--fpseed`         | `12lfisffwfaTYa` | Fingerprint generation seed |
| `--chrome-version` | `130.0.7151.70`  | Chrome browser version      |
| `--noimage`        | -                | Disable image loading       |
| `--nocrash`        | -                | Fix automation tool crashes |
| `--lang`           | `zh-CN`          | Set browser language        |
| `--accept-lang`    | `zh-CN`          | Set HTTP request language   |
| `--proxy-server`   | `-`              | Set proxy server            |
| `--cpucores`        | `6`              | Number of CPU cores         |
| `--platformversion` | `15.4.1`         | Operating system version    |

---

## 📝 Parameter Details
### **`timezone`**  
- **Function**: Sets browser timezone
- **Recommendation**: Match your proxy IP location's timezone
- **Example**: `--timezone=America/New_York`

### **`fpseed`**  
- **Function**: Fingerprint generation seed
- **Impact**: Canvas, WebGL, audio, speech, DOMRect, fonts, and other fingerprints
- **Importance**: Consistent seed ensures reproducible browser fingerprints

### **`chrome-version`**  
- **Function**: Specify Chrome browser version
- **Important Notes**:
  - Version tightly coupled with browser APIs - arbitrary changes may increase detection risk
  - Automatically adapts TLS fingerprints (limited version support)
  - Recommended only for sites with strict version controls
- **Best Practice**: Use officially released Chrome versions

### **`noimage`**  
- **Function**: Disable all image loading
- **Use Case**: Improve page loading speed
- **Warning**: May trigger security systems like Cloudflare (not recommended for regular use)

### **`nocrash`**  
- **Function**: Fixes iframe-related crashes in Playwright/Puppeteer
- **Solves**: Crashes caused by `contentWindow.open`

### **`lang` & `accept-lang`**
- **Function**: Control browser language and HTTP headers
- **Impact**: Speech recognition and localization-related fingerprints
- **Recommendation**: Keep both values consistent

### **`proxy-server`**  
- **Function**: Configure network proxy server
- **Format**: `--proxy-server=[protocol]://[address]:[port]`
- **Supported Protocols**:
  - `http`: HTTP/HTTPS proxy
  - `socks4`: SOCKS4 proxy
  - `socks5`: SOCKS5 proxy (authentication not supported)
- **Examples**:
  - `--proxy-server=http://127.0.0.1:8080`

### **`cpucores`**  
- **Function**：Number of CPU cores (e.g., an i7 typically has 6 cores, corresponding to navigator.hardwareConcurrency).
- **Recommendation**：Use common CPU core counts (6, 8, 10, 12).

### **`platformversion`**  
- **Function**：Operating system version.
- **Recommendation**：
  - `macOS`:  Use versions like 15.4.1, 15.5, etc.
  - `Windows`: Use versions like 10.0.0, etc.

---

## 🤖 Automation Tool Support
### Eliminated Automation Signatures
- ✅ CDP detection
- ✅ Selenium signatures
- ✅ Playwright signatures
- ✅ DrissionPage signatures

### Recommended Tool
**[DrissionPage](https://github.com/g1879/DrissionPage)** - Low-profile, high-performance automation solution  
**Advantages**:
- Minimal browser fingerprint footprint
- Perfect mouse event simulation
- Crash-free content interaction

### Key Technical Improvements
1. **Mouse Event Fix**: Permanently resolves CDP's `Input.dispatchMouseEvent` defect
2. **Shadow DOM Access**: Access closed shadow DOM via `opshadowRoot`
3. **Automation Detection Bypass**: Eliminates common automation tool markers

---

## 🐞 Debugging Support
- **Renamed Debugger**: `debugger` → `debugging` (bypasses detection)
- **Console Checks**: Bypasses common console property checks

---

## 🚧 Development Roadmap
| Feature                  | Status     | Description                                                      |
|--------------------------|------------|------------------------------------------------------------------|
| Linux Support            | ❌ Pending  | Adapting for Linux platform                                      |
| macOS Signing            | ❌ Pending  | Requires Apple Developer account for security warnings           |
| GPU Fingerprint Spoofing | ⚙️ In Progress | Enhancing graphics fingerprint camouflage                        |
| Multi-version TLS Support| ⚙️ In Progress | Expanding TLS fingerprint library for more Chrome versions       |

> **Tip**: Project continuously updated - welcome to submit Issues! If you'd like to help me collect more fingerprints, please click [here](https://www.hanyiting.com)
