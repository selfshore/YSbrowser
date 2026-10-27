# 原生 Credentials

[原生 API 目录](README.md) · [手册目录](../README.md)

## 方法与属性索引

- [create](#create)
- [delete](#delete)
- [get](#get)
- [install](#install)
- [on](#on)
- [once](#once)
- [remove_listener](#remove_listener)

## create

### 同步

```python signature
def create(self, rp_id: str, *, id: Optional[str] = None, private_key: Optional[str] = None, public_key: Optional[str] = None, sign_count: Optional[int] = None, user_handle: Optional[str] = None) -> patchright._impl._api_structures.VirtualCredential
```

Credentials.create

Seeds a virtual WebAuthn credential and returns it.

With only `rp_id`, generates a fresh **ECDSA P-256** keypair, credential id and user handle. The seeded credential
is discoverable (resident), so the page can resolve it from both username-then-passkey and usernameless passkey
flows. The returned object carries the private and public keys, so it can be persisted to disk and re-seeded in a
later test.

To **import a known credential**, supply all four of `id`, `user_handle`, `private_key` and `public_key` together.
Pass `sign_count` as well to continue from the signature counter the relying party has already seen.

Call `credentials.install()` before navigating to a page that uses WebAuthn.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `rp_id` | str | Relying party id (typically the site's effective domain). |
| `id` | Union[str, None] | Base64url-encoded credential id. Auto-generated if omitted. |
| `private_key` | Union[str, None] | Base64url-encoded PKCS#8 (DER) private key. Auto-generated if omitted. |
| `public_key` | Union[str, None] | Base64url-encoded SPKI (DER) public key. Auto-generated if omitted. |
| `sign_count` | Union[int, None] | Initial value of the [signature counter](https://www.w3.org/TR/webauthn-2/#signature-counter). The counter is incremented by one on every successful `navigator.credentials.get()` assertion, so the first assertion reports `signCount + 1`. Defaults to `0`. |
| `user_handle` | Union[str, None] | Base64url-encoded user handle. Auto-generated if omitted. |

#### Returns
{id: str, rpId: str, userHandle: str, privateKey: str, publicKey: str, signCount: int}

### 异步

```python signature
async def create(self, rp_id: str, *, id: Optional[str] = None, private_key: Optional[str] = None, public_key: Optional[str] = None, sign_count: Optional[int] = None, user_handle: Optional[str] = None) -> patchright._impl._api_structures.VirtualCredential
```

Credentials.create

Seeds a virtual WebAuthn credential and returns it.

With only `rp_id`, generates a fresh **ECDSA P-256** keypair, credential id and user handle. The seeded credential
is discoverable (resident), so the page can resolve it from both username-then-passkey and usernameless passkey
flows. The returned object carries the private and public keys, so it can be persisted to disk and re-seeded in a
later test.

To **import a known credential**, supply all four of `id`, `user_handle`, `private_key` and `public_key` together.
Pass `sign_count` as well to continue from the signature counter the relying party has already seen.

Call `credentials.install()` before navigating to a page that uses WebAuthn.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `rp_id` | str | Relying party id (typically the site's effective domain). |
| `id` | Union[str, None] | Base64url-encoded credential id. Auto-generated if omitted. |
| `private_key` | Union[str, None] | Base64url-encoded PKCS#8 (DER) private key. Auto-generated if omitted. |
| `public_key` | Union[str, None] | Base64url-encoded SPKI (DER) public key. Auto-generated if omitted. |
| `sign_count` | Union[int, None] | Initial value of the [signature counter](https://www.w3.org/TR/webauthn-2/#signature-counter). The counter is incremented by one on every successful `navigator.credentials.get()` assertion, so the first assertion reports `signCount + 1`. Defaults to `0`. |
| `user_handle` | Union[str, None] | Base64url-encoded user handle. Auto-generated if omitted. |

#### Returns
{id: str, rpId: str, userHandle: str, privateKey: str, publicKey: str, signCount: int}


## delete

### 同步

```python
def delete(self, id: str) -> None
```

Credentials.delete

Removes a credential from the authenticator by its id. Works for any credential currently held — both those seeded
with `credentials.create()` and those the page registered itself by calling `navigator.credentials.create()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `id` | str | Base64url-encoded credential id. |

### 异步

```python
async def delete(self, id: str) -> None
```

Credentials.delete

Removes a credential from the authenticator by its id. Works for any credential currently held — both those seeded
with `credentials.create()` and those the page registered itself by calling `navigator.credentials.create()`.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `id` | str | Base64url-encoded credential id. |

## get

### 同步

```python signature
def get(self, *, id: Optional[str] = None, rp_id: Optional[str] = None) -> List[patchright._impl._api_structures.VirtualCredential]
```

Credentials.get

Returns every credential currently held by the authenticator, optionally filtered by `rp_id` or `id`. This includes
both credentials seeded with `credentials.create()` and credentials the page registered itself by calling
`navigator.credentials.create()`.

Each returned credential includes its private and public keys and the current signature counter, so a passkey the
app just registered can be saved and re-seeded into a later test with `credentials.create()` — see the second
example in the class overview.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `id` | Union[str, None] | Only return the credential with this base64url-encoded id. |
| `rp_id` | Union[str, None] | Only return credentials for this relying party id. |

#### Returns
List[{id: str, rpId: str, userHandle: str, privateKey: str, publicKey: str, signCount: int}]

### 异步

```python signature
async def get(self, *, id: Optional[str] = None, rp_id: Optional[str] = None) -> List[patchright._impl._api_structures.VirtualCredential]
```

Credentials.get

Returns every credential currently held by the authenticator, optionally filtered by `rp_id` or `id`. This includes
both credentials seeded with `credentials.create()` and credentials the page registered itself by calling
`navigator.credentials.create()`.

Each returned credential includes its private and public keys and the current signature counter, so a passkey the
app just registered can be saved and re-seeded into a later test with `credentials.create()` — see the second
example in the class overview.

#### Parameters


| Parameter | Type | Meaning |
| --- | --- | --- |
| `id` | Union[str, None] | Only return the credential with this base64url-encoded id. |
| `rp_id` | Union[str, None] | Only return credentials for this relying party id. |

#### Returns
List[{id: str, rpId: str, userHandle: str, privateKey: str, publicKey: str, signCount: int}]


## install

### 同步

```python
def install(self) -> None
```

Credentials.install

Installs the virtual WebAuthn authenticator into the context, overriding `navigator.credentials.create()` and
`navigator.credentials.get()` in all current and future pages. Call this before the page first touches
`navigator.credentials`.

Required: until `credentials.install()` is called, no interception is in place and the page sees the platform's
native (or absent) WebAuthn behaviour. Seeding credentials with `credentials.create()` without installing populates
the authenticator, but the page will never see those credentials.

### 异步

```python
async def install(self) -> None
```

Credentials.install

Installs the virtual WebAuthn authenticator into the context, overriding `navigator.credentials.create()` and
`navigator.credentials.get()` in all current and future pages. Call this before the page first touches
`navigator.credentials`.

Required: until `credentials.install()` is called, no interception is in place and the page sees the platform's
native (or absent) WebAuthn behaviour. Seeding credentials with `credentials.create()` without installing populates
the authenticator, but the page will never see those credentials.


## on

### 同步

```python
def on(self, event: Any, f: Any) -> None
```

Registers the function ``f`` to the event name ``event``.

### 异步

```python
def on(self, event: Any, f: Any) -> None
```

Registers the function ``f`` to the event name ``event``.


## once

### 同步

```python
def once(self, event: Any, f: Any) -> None
```

The same as ``self.on``, except that the listener is automatically
removed after being called.

### 异步

```python
def once(self, event: Any, f: Any) -> None
```

The same as ``self.on``, except that the listener is automatically
removed after being called.


## remove_listener

### 同步

```python
def remove_listener(self, event: Any, f: Any) -> None
```

Removes the function ``f`` from ``event``.

### 异步

```python
def remove_listener(self, event: Any, f: Any) -> None
```

Removes the function ``f`` from ``event``.
