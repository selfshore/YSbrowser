# 代理与出口检查

[返回目录](README.md)

## 配置代理

```python
import os
from ysbrowser_sdk.sync_api import YSBrowser, ProxyConfig, ProxyCheck

proxy = ProxyConfig(
    server=os.environ["PROXY_SERVER"],  # 例如 http://proxy.example.com:8000
    username=os.environ["PROXY_USERNAME"],
    password=os.environ["PROXY_PASSWORD"],
)
with YSBrowser() as browser:
    context = browser.new_context(
        proxy=proxy,
        check=ProxyCheck(check_url=os.environ["IP_CHECK_URL"]),
    )
    print(context.proxy_status().to_dict())
```

无认证代理省略 `username` 和 `password`；不要把账号密码拼在 `server` URL 内。`IP_CHECK_URL` 应为自己可访问、返回请求出口 IP 的检查服务，格式见下文。

### ProxyConfig

`ProxyConfig(server, username=None, password=None, bypass_list=None)` 为不可重新赋值字段的数据类。

| 字段 | 类型 / 默认值 | 用法 |
| --- | --- | --- |
| `server` | `str`，必填 | `http://host:port`、`https://host:port` 或 `socks5://host:port`；端口 1–65535，不能带路径、查询、fragment、空白或内嵌账号密码 |
| `username` | `str \| None = None` | 代理用户名，与密码同时提供或同时省略 |
| `password` | `str \| None = None` | 代理密码 |
| `bypass_list` | `str \| None = None` | Chromium 代理绕过规则，例如 `"localhost;127.0.0.1;*.internal.example"` |

需要让本机回环请求也经过代理时，按用途使用 `bypass_list="<-loopback>"` 关闭隐式回环绕过规则。具体主机能否通过代理访问取决于代理服务。

`proxy.to_cdp() -> dict` 返回原生字段 `proxyServer`、可选 `username`、`password`、`bypassList`；此结果含实际凭据。该方法只转换数据，不连接代理。

### Direct

`Direct()` 显式直连，无构造字段。`Direct().to_cdp()` 返回 `{"proxyServer": "direct://"}`。

```python
from ysbrowser_sdk.sync_api import Direct
context = browser.new_context(proxy=Direct())
context.set_proxy(Direct())
```

`YSBrowser(default_proxy=...)` 设置新 Context 的默认代理；`new_context(proxy=...)` 可覆盖。SDK 不会自动提取供应商代理、轮换代理或切回直连。

## 创建或切换时检查：ProxyCheck

`ProxyCheck(check_url, expected_exit_ip=None, timeout_ms=10000, rollback_on_failure=True)`。

| 字段 | 类型 / 默认值 | 用法 |
| --- | --- | --- |
| `check_url` | `str`，必填 | 可匿名 GET 的 HTTP(S) 出口检查 URL，不含内嵌认证或 fragment |
| `expected_exit_ip` | `str \| None = None` | 预期的合法 IPv4/IPv6；省略则只验证返回有效 IP，不固定出口 |
| `timeout_ms` | `int = 10000` | 整数，1000–60000 毫秒 |
| `rollback_on_failure` | `bool = True` | 切换检查失败后是否恢复旧代理配置 |

`to_cdp() -> dict` 转为 `checkUrl`、`checkTimeoutMs`、`rollbackOnFailure` 和可选 `expectedExitIp`。创建和切换时使用 `check=ProxyCheck(...)`；检查失败通常抛 `ProxyCheckError`。滚动出口代理不宜固定 `expected_exit_ip`。

### 检查服务响应

最终响应需为 HTTP 2xx，正文不超过 65536 字节，并能解析合法 IP。推荐返回：

```json
{"ip":"203.0.113.10"}
```

这里的 IP 仅是格式示例；服务应返回它实际观察到的请求来源 IP。也接受顶层 `query` / `origin` 字符串、JSON 字符串、纯文本 IP 和 IPv6。不能只放在 `data.ip` 中，也不能返回 HTML 登录页或空正文。

原生检查使用当前 Context 网络配置，绕过缓存，不附带站点 Cookie；检查服务不应要求站点登录。代理认证由 `ProxyConfig` 提供。

## 运行期间切换

```python
context.set_proxy(
    new_proxy,
    check=ProxyCheck(check_url=check_url),
    mode="drain",
    drain_timeout_ms=15000,
)
```

`set_proxy(proxy, *, check=None, mode=None, drain_timeout_ms=None) -> ProxyStatus`；异步入口使用 `await`。

| 参数 | 类型 / 默认值 | 用法 |
| --- | --- | --- |
| `proxy` | `ProxyConfig \| Direct`，必填 | 目标网络配置 |
| `check` | `ProxyCheck \| None` | 可选出口检查，失败按配置回滚 |
| `mode` | `str \| None = None` | `None`、`drain` 或 `immediate`，区别如下 |
| `drain_timeout_ms` | `int \| None = None` | `drain` 模式的旧请求等待时间，1–60000，省略使用 10000；不包含出口检查耗时 |

| 模式 | 行为 | 使用条件 |
| --- | --- | --- |
| `None` | 原有设置行为，不提供新请求暂停屏障 | 调用方自行安排空闲时机 |
| `drain` | 暂停新请求，等待旧请求结束，再切换和检查 | 适合允许等待在途请求的业务 |
| `immediate` | 暂停新请求，取消旧请求/连接，然后切换和检查 | 允许当前请求失败的业务 |

`drain` / `immediate` 需要浏览器支持 `proxySwitchBarrier`。`drain` 超时抛 `PROXY_DRAIN_TIMEOUT`，保留旧配置并恢复暂停请求；长连接可能使等待一直无法结束。

切换成功或检查回滚完成后再放行新请求。已取消请求不会自动重发；取消不能证明服务端没有处理提交。调用期间页面定时器与自动化超时继续计时。取消 Python `await` 不等于撤回浏览器已收到的切换命令。

切换范围针对浏览器 Context 默认分区的原生网络请求。独立 Python `requests/httpx`、原生 `APIRequestContext`、WebRTC 等不能据此认定共用同一切换机制。

## 只检查当前代理

```python
result = context.check_proxy(check_url, timeout_ms=10000)
if result.ok and not result.stale:
    print("当前出口：", result.exit_ip)
else:
    print(result.kind, result.network_error)
```

`check_proxy(check_url, *, expected_exit_ip=None, timeout_ms=10000) -> ProxyHealthResult`；异步入口使用 `await`。参数格式与 `ProxyCheck` 相同，但没有回滚开关：它不重新设置代理，也不主动关闭连接。

正常的网络/HTTP 检查失败以 `ok=False` 返回；协议调用或生命周期错误仍会抛异常。结果更新 `proxy_status().health`，不会覆盖配置时的历史 `check_state`。

### ProxyHealthResult 全部字段

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `ok` | `bool` | 本次检查是否成功 |
| `kind` | `str` | 结果分类，如 `success`、`network_error`、`timeout`、`http_error`、`invalid_ip`、`exit_ip_mismatch`；还可能有取消或被新操作替代的分类 |
| `check_id` | `str` | 本次检查标识 |
| `generation` | `str` | 检查关联的代理配置版本，按不透明标识比较 |
| `stale` | `bool` | 返回时是否已被更新的配置/检查替代；`True` 不应用于判定当前代理 |
| `checked_at` | `float` | 检查时间，Unix 毫秒 |
| `elapsed_ms` | `float` | 本次检查耗时，毫秒 |
| `exit_ip` | `str \| None` | 解析到的出口 IP |
| `http_status` | `int \| None` | HTTP 状态码，没有响应时可为 `None` |
| `network_error` | `str \| None` | 浏览器网络错误码或说明 |

调用 `result.to_dict()` 返回全部字段字典。`ProxyHealthResult.from_cdp(value)` 可将原生 camelCase 结果转换为对象，不执行检查。

## 查询状态：ProxyStatus

`context.proxy_status() -> ProxyStatus`；异步入口使用 `await`。查询配置及已有检查记录，本身不会请求出口服务。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `mode` | `str` | `direct`、`fixed_servers`、`system`，未知原生值可显示 `unknown`；表示路由配置 |
| `check_state` | `str` | 配置/切换时的检查记录，见下表 |
| `context_id` | `str` | 浏览器 Context ID |
| `auth_configured` | `bool` | 是否配置代理认证 |
| `runtime_override` | `bool` | 是否存在运行时代理覆盖 |
| `last_exit_ip` | `str \| None` | 最近配置检查解析到的出口 |
| `last_http_status` | `int \| None` | 最近配置检查的 HTTP 状态 |
| `last_rollback` | `bool \| None` | 最近配置检查失败后是否回滚 |
| `proxy_server` | `str` | 已去除凭据等信息的代理地址，直连为 `direct://` |
| `check_url` | `str \| None` | 已去除路径/query 等信息的检查来源地址 |
| `generation` | `str \| None` | 当前配置版本标识 |
| `health_check_in_progress` | `bool` | 是否有独立健康检查正在执行 |
| `health` | `ProxyHealthResult \| None` | 最近独立健康检查结果 |
| `last_error_kind` | `str \| None` | 最近配置检查错误分类，如 `proxy_auth_error`、`http_error`、`network_error`、`timeout`、`invalid_ip`、`exit_ip_mismatch`、`cancelled`、`unknown` |
| `last_network_error` | `str \| None` | 最近配置检查提取的 `net::ERR_...` 错误码 |
| `switch_in_progress` | `bool` | 是否处于有屏障的代理切换过程 |

| `check_state` | 含义 |
| --- | --- |
| `unchecked` | 没有配置检查记录 |
| `checking` | 配置检查进行中 |
| `success` | 最近一次配置检查成功 |
| `failed_rolled_back` | 最近配置检查失败，已回滚 |
| `failed_no_rollback` | 最近配置检查失败，未回滚 |

`status.to_dict()` 返回全部字段，`health` 转成嵌套字典。`ProxyStatus.from_cdp(status)` 接收原生状态字典，转换字段、计算 `check_state` 并对地址做裁剪，不访问网络。

`check_state="success"` 只说明历史检查成功。代理随后失效或页面导航失败时，该字段仍可能保持成功；需要调用 `check_proxy()` 获取新结果。回滚后的 `last_exit_ip` 等字段可能描述失败尝试，不保证是回滚后的当前出口。SDK 没有后台心跳、自动到期通知或自动切换代理。
