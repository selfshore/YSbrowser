# 原生输入输出结构

[原生 API 目录](README.md)

下列类型用于原生方法的字典参数或返回值。是否必须传入某个字段还受具体方法及字段组合约束；例如 Cookie 可使用 URL 或 domain/path 组合。请同时参照调用方法的正文。

## BrowserBindResult

| 字段 | 类型 | TypedDict 必填 |
| --- | --- | --- |
| `endpoint` | `<class 'str'>` | 是 |

## ClientCertificate

| 字段 | 类型 | TypedDict 必填 |
| --- | --- | --- |
| `origin` | `<class 'str'>` | 否 |
| `certPath` | `typing.Union[str, pathlib.Path, NoneType]` | 否 |
| `cert` | `typing.Optional[bytes]` | 否 |
| `keyPath` | `typing.Union[str, pathlib.Path, NoneType]` | 否 |
| `key` | `typing.Optional[bytes]` | 否 |
| `pfxPath` | `typing.Union[str, pathlib.Path, NoneType]` | 否 |
| `pfx` | `typing.Optional[bytes]` | 否 |
| `passphrase` | `typing.Optional[str]` | 否 |

## Cookie

| 字段 | 类型 | TypedDict 必填 |
| --- | --- | --- |
| `name` | `<class 'str'>` | 否 |
| `value` | `<class 'str'>` | 否 |
| `domain` | `<class 'str'>` | 否 |
| `path` | `<class 'str'>` | 否 |
| `expires` | `<class 'float'>` | 否 |
| `httpOnly` | `<class 'bool'>` | 否 |
| `secure` | `<class 'bool'>` | 否 |
| `sameSite` | `typing.Literal['Lax', 'None', 'Strict']` | 否 |
| `partitionKey` | `typing.Optional[str]` | 否 |

## DebuggerLocation

| 字段 | 类型 | TypedDict 必填 |
| --- | --- | --- |
| `file` | `<class 'str'>` | 是 |
| `line` | `typing.Optional[int]` | 是 |
| `column` | `typing.Optional[int]` | 是 |

## DebuggerPausedDetails

| 字段 | 类型 | TypedDict 必填 |
| --- | --- | --- |
| `location` | `<class 'patchright._impl._api_structures.DebuggerLocation'>` | 是 |
| `title` | `<class 'str'>` | 是 |

## DropPayload

| 字段 | 类型 | TypedDict 必填 |
| --- | --- | --- |
| `files` | `typing.Union[str, pathlib.Path, typing.Sequence[typing.Union[str, pathlib.Path]], patchright._impl._api_structures.FilePayload, typing.Sequence[patchright._impl._api_structures.FilePayload], NoneType]` | 否 |
| `data` | `typing.Optional[typing.Dict[str, str]]` | 否 |

## FilePayload

| 字段 | 类型 | TypedDict 必填 |
| --- | --- | --- |
| `name` | `<class 'str'>` | 是 |
| `mimeType` | `<class 'str'>` | 是 |
| `buffer` | `<class 'bytes'>` | 是 |

## FloatRect

| 字段 | 类型 | TypedDict 必填 |
| --- | --- | --- |
| `x` | `<class 'float'>` | 是 |
| `y` | `<class 'float'>` | 是 |
| `width` | `<class 'float'>` | 是 |
| `height` | `<class 'float'>` | 是 |

## Geolocation

| 字段 | 类型 | TypedDict 必填 |
| --- | --- | --- |
| `latitude` | `<class 'float'>` | 否 |
| `longitude` | `<class 'float'>` | 否 |
| `accuracy` | `typing.Optional[float]` | 否 |

## HttpCredentials

| 字段 | 类型 | TypedDict 必填 |
| --- | --- | --- |
| `username` | `<class 'str'>` | 否 |
| `password` | `<class 'str'>` | 否 |
| `origin` | `typing.Optional[str]` | 否 |
| `send` | `typing.Optional[typing.Literal['always', 'unauthorized']]` | 否 |

## LocalStorageEntry

| 字段 | 类型 | TypedDict 必填 |
| --- | --- | --- |
| `name` | `<class 'str'>` | 是 |
| `value` | `<class 'str'>` | 是 |

## NameValue

| 字段 | 类型 | TypedDict 必填 |
| --- | --- | --- |
| `name` | `<class 'str'>` | 是 |
| `value` | `<class 'str'>` | 是 |

## OriginState

| 字段 | 类型 | TypedDict 必填 |
| --- | --- | --- |
| `origin` | `<class 'str'>` | 是 |
| `localStorage` | `typing.List[patchright._impl._api_structures.LocalStorageEntry]` | 是 |

## PdfMargins

| 字段 | 类型 | TypedDict 必填 |
| --- | --- | --- |
| `top` | `typing.Union[str, float, NoneType]` | 否 |
| `right` | `typing.Union[str, float, NoneType]` | 否 |
| `bottom` | `typing.Union[str, float, NoneType]` | 否 |
| `left` | `typing.Union[str, float, NoneType]` | 否 |

## Position

| 字段 | 类型 | TypedDict 必填 |
| --- | --- | --- |
| `x` | `<class 'float'>` | 是 |
| `y` | `<class 'float'>` | 是 |

## ProxySettings

| 字段 | 类型 | TypedDict 必填 |
| --- | --- | --- |
| `server` | `<class 'str'>` | 否 |
| `bypass` | `typing.Optional[str]` | 否 |
| `username` | `typing.Optional[str]` | 否 |
| `password` | `typing.Optional[str]` | 否 |

## RemoteAddr

| 字段 | 类型 | TypedDict 必填 |
| --- | --- | --- |
| `ipAddress` | `<class 'str'>` | 是 |
| `port` | `<class 'int'>` | 是 |

## RequestSizes

| 字段 | 类型 | TypedDict 必填 |
| --- | --- | --- |
| `requestBodySize` | `<class 'int'>` | 是 |
| `requestHeadersSize` | `<class 'int'>` | 是 |
| `responseBodySize` | `<class 'int'>` | 是 |
| `responseHeadersSize` | `<class 'int'>` | 是 |

## ResourceTiming

| 字段 | 类型 | TypedDict 必填 |
| --- | --- | --- |
| `startTime` | `<class 'float'>` | 是 |
| `domainLookupStart` | `<class 'float'>` | 是 |
| `domainLookupEnd` | `<class 'float'>` | 是 |
| `connectStart` | `<class 'float'>` | 是 |
| `secureConnectionStart` | `<class 'float'>` | 是 |
| `connectEnd` | `<class 'float'>` | 是 |
| `requestStart` | `<class 'float'>` | 是 |
| `responseStart` | `<class 'float'>` | 是 |
| `responseEnd` | `<class 'float'>` | 是 |

## ScreencastActionStyle

| 字段 | 类型 | TypedDict 必填 |
| --- | --- | --- |
| `point` | `typing.Optional[str]` | 否 |
| `highlight` | `typing.Optional[str]` | 否 |
| `title` | `typing.Optional[str]` | 否 |

## ScreencastFrame

| 字段 | 类型 | TypedDict 必填 |
| --- | --- | --- |
| `data` | `<class 'bytes'>` | 是 |
| `timestamp` | `<class 'float'>` | 是 |
| `viewportWidth` | `<class 'int'>` | 是 |
| `viewportHeight` | `<class 'int'>` | 是 |

## ScreencastSize

| 字段 | 类型 | TypedDict 必填 |
| --- | --- | --- |
| `width` | `<class 'int'>` | 是 |
| `height` | `<class 'int'>` | 是 |

## SecurityDetails

| 字段 | 类型 | TypedDict 必填 |
| --- | --- | --- |
| `issuer` | `typing.Optional[str]` | 是 |
| `protocol` | `typing.Optional[str]` | 是 |
| `subjectName` | `typing.Optional[str]` | 是 |
| `validFrom` | `typing.Optional[float]` | 是 |
| `validTo` | `typing.Optional[float]` | 是 |

## SetCookieParam

| 字段 | 类型 | TypedDict 必填 |
| --- | --- | --- |
| `name` | `<class 'str'>` | 否 |
| `value` | `<class 'str'>` | 否 |
| `url` | `typing.Optional[str]` | 否 |
| `domain` | `typing.Optional[str]` | 否 |
| `path` | `typing.Optional[str]` | 否 |
| `expires` | `typing.Optional[float]` | 否 |
| `httpOnly` | `typing.Optional[bool]` | 否 |
| `secure` | `typing.Optional[bool]` | 否 |
| `sameSite` | `typing.Optional[typing.Literal['Lax', 'None', 'Strict']]` | 否 |
| `partitionKey` | `typing.Optional[str]` | 否 |

## SourceLocation

| 字段 | 类型 | TypedDict 必填 |
| --- | --- | --- |
| `url` | `<class 'str'>` | 是 |
| `line` | `<class 'int'>` | 是 |
| `column` | `<class 'int'>` | 是 |
| `lineNumber` | `<class 'int'>` | 是 |
| `columnNumber` | `<class 'int'>` | 是 |

## StorageState

| 字段 | 类型 | TypedDict 必填 |
| --- | --- | --- |
| `cookies` | `typing.List[patchright._impl._api_structures.StorageStateCookie]` | 否 |
| `origins` | `typing.List[patchright._impl._api_structures.OriginState]` | 否 |

## StorageStateCookie

| 字段 | 类型 | TypedDict 必填 |
| --- | --- | --- |
| `name` | `<class 'str'>` | 否 |
| `value` | `<class 'str'>` | 否 |
| `domain` | `<class 'str'>` | 否 |
| `path` | `<class 'str'>` | 否 |
| `expires` | `<class 'float'>` | 否 |
| `httpOnly` | `<class 'bool'>` | 否 |
| `secure` | `<class 'bool'>` | 否 |
| `sameSite` | `typing.Literal['Lax', 'None', 'Strict']` | 否 |

## TracingGroupLocation

| 字段 | 类型 | TypedDict 必填 |
| --- | --- | --- |
| `file` | `<class 'str'>` | 是 |
| `line` | `typing.Optional[int]` | 是 |
| `column` | `typing.Optional[int]` | 是 |

## ViewportSize

| 字段 | 类型 | TypedDict 必填 |
| --- | --- | --- |
| `width` | `<class 'int'>` | 是 |
| `height` | `<class 'int'>` | 是 |

## VirtualCredential

| 字段 | 类型 | TypedDict 必填 |
| --- | --- | --- |
| `id` | `<class 'str'>` | 是 |
| `rpId` | `<class 'str'>` | 是 |
| `userHandle` | `<class 'str'>` | 是 |
| `privateKey` | `<class 'str'>` | 是 |
| `publicKey` | `<class 'str'>` | 是 |
| `signCount` | `<class 'int'>` | 是 |

## WebErrorLocation

| 字段 | 类型 | TypedDict 必填 |
| --- | --- | --- |
| `url` | `<class 'str'>` | 是 |
| `line` | `<class 'int'>` | 是 |
| `column` | `<class 'int'>` | 是 |

## WebMCPTool

| 字段 | 类型 | TypedDict 必填 |
| --- | --- | --- |
| `name` | `<class 'str'>` | 否 |
| `description` | `<class 'str'>` | 否 |
| `inputSchema` | `typing.Optional[typing.Any]` | 否 |
| `annotations` | `typing.Optional[patchright._impl._api_structures.WebMCPToolAnnotations]` | 否 |

## WebMCPToolAnnotations

| 字段 | 类型 | TypedDict 必填 |
| --- | --- | --- |
| `readOnly` | `typing.Optional[bool]` | 否 |
| `untrustedContent` | `typing.Optional[bool]` | 否 |
| `consequential` | `typing.Optional[bool]` | 否 |
