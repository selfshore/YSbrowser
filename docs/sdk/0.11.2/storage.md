# 配置与登录状态

[返回目录](README.md)

配置保存指纹、代理和 Context 选项；登录状态保存 Cookie、LocalStorage 和可选 IndexedDB。两类文件分别保存、分别恢复。

## ContextConfig

```python
from ysbrowser_sdk.sync_api import (
    ContextConfig, ContextOptions, FingerprintProfile, Direct,
)

config = ContextConfig(
    fingerprint=FingerprintProfile(fpseed="account-001"),
    proxy=Direct(),
    no_viewport=False,
    options=ContextOptions(viewport={"width": 1280, "height": 720}),
)
config.save("config/account-001.json")
loaded = ContextConfig.load("config/account-001.json")
# browser 为已启动的 YSBrowser。
context = browser.new_context(config=loaded)
```

| 构造字段 | 类型 / 默认值 | 用法 |
| --- | --- | --- |
| `fingerprint` | `FingerprintProfile = FingerprintProfile()` | 指纹配置 |
| `proxy` | `ProxyConfig \| Direct = Direct()` | 显式保存代理策略 |
| `no_viewport` | `bool = True` | 是否不固定视口；有 `options.viewport` 时必须为 `False` |
| `options` | `ContextOptions = ContextOptions()` | Context 选项 |

### 保存与加载方法

| 调用 | 返回值 | 参数 |
| --- | --- | --- |
| `config.to_dict(include_proxy_credentials=False, include_sensitive_options=False)` | `dict` | 两个开关均默认 `False` |
| `config.save(path, include_proxy_credentials=False, include_sensitive_options=False)` | `None` | `path: str \| Path`；自动创建父目录并写入 JSON |
| `ContextConfig.from_dict(data, proxy_username=None, proxy_password=None, options=None)` | `ContextConfig` | 字典输入；认证信息和选项可在加载时补齐 |
| `ContextConfig.load(path, proxy_username=None, proxy_password=None, options=None)` | `ContextConfig` | 从 JSON 文件读取，补齐规则同 `from_dict` |

除第一个位置参数外，以上可选参数都只能用关键字传入。它们是本地同步操作，异步程序中也不使用 `await`。

### 从已有 Context 导出

```python
config_data = context.export_config("config/current.json")
```

签名：`context.export_config(path=None, *, include_proxy_credentials=False, include_sensitive_options=False) -> dict`。异步入口使用 `await`。不传路径只返回字典；传路径后同时保存并返回字典。

如果代理或指纹被 SDK 以外的客户端修改，SDK 无法确认可复用配置时抛 `CONFIG_CHANGED_EXTERNALLY`。需要在合适的 Context 中重新成功应用明确配置；指纹已锁定时新建 Context。通过原生对象修改的其他选项不一定能反映在导出文件中。

### JSON 格式

无额外选项时使用 schema 1；包含选项值或待补齐字段时使用 schema 2：

```json
{
  "schema_version": 2,
  "fingerprint": {"fpseed": "account-001", "cpu_cores": 8},
  "proxy": {"mode": "direct"},
  "no_viewport": false,
  "options": {
    "values": {"viewport": {"width": 1280, "height": 720}},
    "requires": []
  }
}
```

| JSON 字段 | 含义 |
| --- | --- |
| `schema_version` | `1` 或 `2`；版本 1 不含 `options`，版本 2 必须包含 |
| `fingerprint` | Python snake_case 字段，只包含已指定值 |
| `proxy.mode` | `direct` 或 `fixed_servers` |
| `proxy.server` | 固定代理的 URL |
| `proxy.bypass_list` | 固定代理绕过规则，可为 `null` |
| `proxy.requires_auth` | 固定代理是否需要认证，布尔值 |
| `proxy.username/password` | 仅显式包含凭据时出现 |
| `no_viewport` | 布尔值 |
| `options.values` | 已保存的 ContextOptions 值 |
| `options.requires` | 默认被省略且加载时需要补齐的选项字段名 |

不要把 `profile.to_cdp()` 的 camelCase 字典直接用作配置中的 `fingerprint`。

### 补齐认证与敏感选项

```python
import os
from ysbrowser_sdk.sync_api import ContextConfig, ContextOptions

config = ContextConfig.load(
    "config/account-with-proxy.json",
    proxy_username=os.environ["PROXY_USERNAME"],
    proxy_password=os.environ["PROXY_PASSWORD"],
    options=ContextOptions(extra_http_headers={
        "Authorization": "Bearer " + os.environ["SITE_TOKEN"],
    }),
)
```

此例要求文件声明了需要代理认证及附加请求头。代理用户名和密码必须成对补齐；直连配置不接受代理凭据。`options` 中非 `None` 字段覆盖或补充文件值。默认不保存认证信息，但指纹 seed 仍保存在配置中。

## 保存登录状态

```python
state = context.save_storage_state("state/account-001.json", indexed_db=True)
```

签名：`save_storage_state(path=None, *, indexed_db=True) -> dict`。异步入口使用 `await`。`path` 为 `str | Path | None`；省略时只返回字典。`indexed_db` 默认为 `True`，用于包含 IndexedDB 中的登录数据。

返回原生存储状态结构：

```json
{
  "cookies": [],
  "origins": [
    {
      "origin": "https://app.example.com",
      "localStorage": [{"name": "theme", "value": "light"}]
    }
  ]
}
```

Cookie 项通常包括 `name`、`value`、`domain`、`path`、`expires`、`httpOnly`、`secure`、`sameSite`，以及原生版本支持的可选分区字段；`expires` 为 Unix 秒。启用 IndexedDB 时相应 origin 可以带 `indexedDB` 数据。使用原样返回的结构恢复，避免自行改写 IndexedDB 的内部表示。

不包含 SessionStorage、内存中的页面状态、打开的标签页、缓存或完整用户目录。需要站点专用 SessionStorage 时自行读取并在目标页面导航前恢复。

## 恢复登录状态

优先在创建时恢复：

```python
from ysbrowser_sdk.sync_api import ContextConfig

config = ContextConfig.load("config/account-001.json")
context = browser.new_context(
    config=config,
    storage_state="state/account-001.json",
)
page = context.new_page()
page.goto("https://app.example.com")  # 替换为实际站点
```

也可在尚未打开页面的 Context 中调用：

```python
context = browser.new_context(config=config)
context.restore_storage_state("state/account-001.json")
page = context.new_page()
```

`restore_storage_state(state: dict | str | Path) -> None`，异步入口使用 `await`。若已有页面，抛 `STORAGE_RESTORE_REQUIRES_EMPTY_CONTEXT`。状态文件含登录凭据，应放在应用自己的受控目录，不上传公共仓库。
