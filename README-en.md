<div align="center">

# ✨ 𝕐𝕊𝕓𝕣𝕠𝕨𝕤𝕖𝕣 ✨  
**Next-Generation Privacy Browser Solution**

</div>

[English](README-en.md) | [中文](README.md)

## 🔍 Fingerprint Detection Pass List
| Detection Platform                                                  | Status          | Notes         |
|--------------------------------------------------------------------|-----------------|---------------|
| [browserscan](https://browserscan.net)                             | ✅ Perfect Pass  | -             |
| [creepjs](https://abrahamjuliot.github.io/creepjs/)                | ✅ 62.5%+        | Continuously optimizing |
| [iphey](https://iphey.com)                                         | ✅ Perfect Pass  | -             |
| [pixelscan](https://pixelscan.net)                                 | ✅ Perfect Pass  | -             |
| [cloudflare](https://www.cloudflare.com/zh-cn/)                    | ✅ Perfect Pass  | -             |
| [datadome](https://datadome.co/products/bot-protection/)           | ✅ Perfect Pass  | -             |
| [brotector](https://kaliiiiiiiiii.github.io/brotector/)            | ✅ Perfect Pass  | -             |
| [sannysoft](https://bot.sannysoft.com/)                            | ✅ Perfect Pass  | -             |
| [fingerprint](https://fingerprint.com/products/bot-detection/)     | ✅ Perfect Pass  | -             |

---

## ⚙️ Core Parameter Configuration

| Parameter | Value | Description |
| :--- | :--- | :--- |
| `--timezone` | `Asia/Tokyo` | Set browser timezone |
| `--fpseed` | `12lfisffwfaTYa` | General fingerprint generation seed |
| `--webgl-seed` | `12lfisffwfaTYa` | WebGL drawing fingerprint seed |
| `--canvas-seed` | `12lfisffwfaTYa` | Canvas drawing fingerprint seed |
| `--quota-seed` | `12lfisffwfaTYa` | Storage quota fingerprint seed |
| `--css-seed` | `12lfisffwfaTYa` | CSS fingerprint seed |
| `--font-seed` | `12lfisffwfaTYa` | Font list fingerprint seed |
| `--audio-seed` | `12lfisffwfaTYa` | Audio context fingerprint seed |
| `--svg-seed` | `12lfisffwfaTYa` | SVG fingerprint seed |
| `--speech-seed` | `12lfisffwfaTYa` | SpeechVoices fingerprint seed |
| `--rect-seed` | `12lfisffwfaTYa` | DOMRect fingerprint seed |
| `--webrtc-ip-policy` | `disabled` or `proxy` | Disable WebRTC or use custom IP (v5.2+) |
| `--webrtc-proxy-ip` | `127.0.0.1` | Exposed WebRTC IP address |
| `--chrome-version` | `130.0.7151.70` | Chrome browser version |
| `--nocrash` | - | Fix automation tool crash issues |
| `--lang` | `zh-CN` | Set browser UI language |
| `--accept-lang` | `zh-CN` | Set HTTP Request-Language header |
| `--proxy-server` | `socks5://ip:port` | Set proxy server address |
| `--proxy-auth` | `username:password` | Set proxy authentication credentials |
| `--cpucores` | `6` | Reported CPU core count |
| `--platformversion` | `15.4.1` | Operating system version |
| `--custom-screen` | `1792x1120,1792x1039` | Screen resolution and usable area |
| `--force-device-scale-factor` | `1` | Ratio of physical pixels to CSS pixels |
| `--custom-geolocation` | `110,220,70` | Set Lat, Long, and Accuracy |
| `--block-geolocation` | - | Block location access (v5.2+) |
| `--use-fake-device-for-media-stream` | - | Use virtual media devices (camera/mic) |
| `--custom-brand` | `"Microsoft Edge"` | Browser brand identity |
| `--close-portscan` | - | Block local port scanning attempts |
| `--iconumber` | `1` | Browser instance index number |
| `--gpu-fingerprint` | `ANGLE (NVIDIA, NVIDIA GeForce RTX 4060 Direct3D11 vs_5_0 ps_5_0, D3D11)` | Specific GPU renderer string (v5.2+) |


---

## 📝 Parameter Details
### **`timezone`**  
- **Function**: Set browser timezone
- **Recommendation**: Keep consistent with proxy IP location timezone
- **Example**: `--timezone=America/New_York`

### **`fpseed`**  
- **Function**: Fingerprint generation seed
- **Scope**: canvas, webgl, audio, speech, DOMRect, fonts and other fingerprints
- **Importance**: Keeping the same seed ensures consistent browser fingerprint generation

### **`chrome-version`**  
- **Function**: Specify Chrome browser version
- **Notes**:
  - Version number is closely tied to browser APIs; arbitrary changes may cause detection risks
  - Auto-adapts TLS fingerprint (limited version support)
  - Only recommended when target website has strict version control
- **Recommendation**: Use officially released Chrome version numbers

### **`nocrash`**  
- **Function**: Fix iframe-related crash issues in Playwright/Puppeteer
- **Fixes**: Crashes caused by `contentWindow.open`

### **`lang` and `accept-lang`**
- **Function**: Control browser language and HTTP request headers
- **Affects**: Speech recognition, localization-related fingerprints
- **Recommendation**: Keep both consistent

### **`proxy-server`**  
- **Function**: Set network proxy server
- **Format**: `--proxy-server=[protocol]://[address]:[port]`
- **Protocol Support**:
  - `http`: HTTP/HTTPS proxy
  - `socks4`: SOCKS4 proxy
  - `socks5`: SOCKS5 proxy
- **Example**:
  - `--proxy-server=http://127.0.0.1:8080`

### **`proxy-auth`**  
- **Function**: Set network proxy authentication
- **Example**:
  - `--proxy-auth=username:password`

### **`cpucores`**  
- **Function**: CPU core count (e.g., i7 has 6 cores, corresponds to navigator.hardwareConcurrency)
- **Recommendation**: Use common CPU core counts (6, 8, 10, 12)

### **`platformversion`**  
- **Function**: System version
- **Recommendations**:
  - `macOS`: System version, like 15.4.1, 15.5, etc.
  - `Windows`:
    | Windows Version | Build Number | Platform-Version | Status |
    | :--- | :--- | :--- | :--- |
    | **Windows 11 (24H2)** | 26100+ | `"19.0.0"` | Latest/Preview |
    | **Windows 11 (23H2)** | 22631 | `"17.0.0"` | Mainstream Recommended |
    | **Windows 11 (22H2)** | 22621 | `"15.0.0"` | Stable |
    | **Windows 11 (21H2)** | 22000 | `"13.0.0"` | Initial |
    | **Windows 10 (22H2)** | 19045 | `"10.0.0"` | Win10 Most Common |
    | **Windows 10 (21H2)** | 19044 | `"10.0.0"` | Stable |
    | **Windows 8.1** | 9600 | `"6.3.0"` | Outdated |
    | **Windows 8** | 9200 | `"6.2.0"` | Outdated |
    | **Windows 7** | 7601 | `"6.1.0"` | Outdated |

### **`custom-screen`**  
- **Function**: Screen width/height and available width/height, corresponds to width, height, availWidth, availHeight in JavaScript's screen object.
- **Recommendation**: If setting this, width and height are required. availWidth and availHeight can be omitted if unknown; the browser will auto-adjust. Try to use real resolutions.
- **Examples**:
  - `1792x1120,1792x1039`
  - `1792x1120`

### **`force-device-scale-factor`**  
- **Function**: Physical to CSS pixel ratio, i.e., devicePixelRatio
- **Examples**:
  - `1`
  - `2`

### **`custom-geolocation` and `block-geolocation`** 
- **Function**: custom-geolocation sets latitude/longitude (navigator.geolocation.getCurrentPosition), block-geolocation blocks location functionality
- **Example**:
  - `--custom-geolocation=110,220,70` (latitude, longitude, accuracy)

### **`use-fake-device-for-media-stream`**
- **Function**: Fake media devices (navigator.mediaDevices.enumerateDevices)

### **`custom-brand`**
- **Function**: Spoof browser brand
- **Recommendation**: If spoofing as a real browser brand, include the user-agent parameter. If using a fictional non-existent brand, user-agent is not needed.
- **Examples**:
  - `--custom-brand="Microsoft Edge"
--user-agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/137.0.0.0 Safari/537.36 Edg/137.0.0.0"`
  - `--custom-brand="fake brand"`

### **`close-portscan`**
- **Function**: Block port scanning

### **`webrtc-ip-policy`**
- **Function**: Prevent WebRTC from leaking real IP
- **Example**:
  - `--webrtc-ip-policy=disabled`

### **`gpu-fingerprint`**
- **Function**: Modify renderer
- **Examples**:
    | # | Full ANGLE Renderer String |
    | :--- | :--- |
    | **0** | `ANGLE (NVIDIA, NVIDIA GeForce RTX 4060 Direct3D11 vs_5_0 ps_5_0, D3D11)` |
    | **1** | `ANGLE (AMD, AMD Radeon RX 6750 GRE 12GB Direct3D11 vs_5_0 ps_5_0, D3D11)` |
    | **2** | `ANGLE (NVIDIA, NVIDIA GeForce RTX 2060 SUPER Direct3D11 vs_5_0 ps_5_0, D3D11)` |
    | **3** | `ANGLE (Intel, Intel(R) Iris(R) Xe Graphics Direct3D11 vs_5_0 ps_5_0, D3D11)` |
    | **4** | `ANGLE (AMD, AMD Radeon(TM) Graphics Direct3D11 vs_5_0 ps_5_0, D3D11)` |
    | **5** | `ANGLE (NVIDIA, NVIDIA GeForce GT 710 Direct3D11 vs_5_0 ps_5_0, D3D11)` |
    | **6** | `ANGLE (Intel, Intel(R) UHD Graphics Direct3D11 vs_5_0 ps_5_0, D3D11)` |
    | **7** | `ANGLE (AMD, AMD Radeon RX 6700 Direct3D11 vs_5_0 ps_5_0, D3D11)` |
    | **8** | `ANGLE (NVIDIA, NVIDIA GeForce GTX 1660 SUPER Direct3D11 vs_5_0 ps_5_0, D3D11)` |
    | **9** | `ANGLE (NVIDIA, NVIDIA GeForce RTX 4090 Direct3D11 vs_5_0 ps_5_0, D3D11)` |
    | **10** | `ANGLE (NVIDIA, NVIDIA GeForce RTX 4060 Laptop GPU Direct3D11 vs_5_0 ps_5_0, D3D11)` |
    | **11** | `ANGLE (NVIDIA, NVIDIA GeForce RTX 3080 Ti Direct3D11 vs_5_0 ps_5_0, D3D11)` |
---

## Basic Usage
- **Warning**: Since it's unsigned, run `xattr -cr YSbrowser.app` on macOS before use.
- **Warning**: Below are basic parameters. To maintain environment isolation, `--user-data-dir` is required.
- **Warning**: To print objects in console, include openConsole, e.g., `console.log("openConsole",{})`.
```bash
chrome --timezone=Asia/Hong_Kong --lang=zh-CN --accept-lang=zh-CN,en --fpseed=121e0opwlltx  --user-data-dir=./my_user_data 
```

## Simulate Brave
```bash
chrome --timezone=Asia/Hong_Kong --lang=zh-CN --accept-lang=zh-CN,en --fpseed=121e0opwlltx  --user-data-dir=./my_user_data --chrome-version=137.0.0.0 --custom-brand=Brave --enable-features=BraveAPI --disable-features=keyboardAPI,NetworkAPI
```

## 🤖 Automation Tool Support
### Eliminated Automation Signatures
- ✅ CDP Detection
- ✅ Selenium Signatures
- ✅ Playwright Signatures (only partial removal, patchright still recommended)
- ✅ DrissionPage Signatures

### Key Technical Improvements
1. **Mouse Event Fix**: Thoroughly resolved CDP's `Input.dispatchMouseEvent` defects
2. **Shadow DOM Access**: Access closed shadow DOM via `opshadowRoot`
3. **Automation Detection Bypass**: Eliminated common automation tool signature markers

---

## 🐞 Debugging Support
- **Renamed Debugger**: `debugger` → `debuging` (bypass detection)
- **Console Inspection**: Bypasses common console property checks

---

## 🚧 Development Roadmap
> **Tip**: Project is continuously updated. Welcome to submit Issues! If you'd like to help collect more fingerprints, please visit [website](https://www.hanyiting.com)

## ⚖️ Disclaimer
> **Note:** This project is strictly prohibited for illegal use.
<details>
<summary>Click to expand detailed legal compliance statement</summary>

1. **Legal Compliance**: Users should use this tool in compliance with local laws. It is strictly prohibited to use this tool for any illegal or non-compliant activities.
2. **Risk Assumption**: All consequences arising from improper use or illegal purposes (including legal liability and economic losses) are the sole responsibility of the user and are unrelated to the developer.
3. **No Warranty**: This tool is provided "as is." The developer is not responsible for any losses resulting from the use of this tool.
4. **Commercial Use Prohibited**: This tool is for learning and communication purposes only. It is strictly prohibited for any illegal profit-making activities.

</details>

## Job Seeking: Welcome referrals for crawler and anti-crawler positions

### Discussion Group
<img src="QQ20250723-104659.png" alt="QQ Group 1043047569" width="400" height="400">
