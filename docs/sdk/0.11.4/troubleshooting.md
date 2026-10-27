# 常见问题

## drag_element 还在吗？

在。`mouse.drag_element(locator, dx=250, dy=0)` 仍是“拖动元素一定距离”，同步直接调用、异步 await。完整参数和返回值见[专门章节](drag-element.md)。

## 脚本没有反应，只返回 coroutine

同步脚本使用 `ysbrowser_sdk.sync_api`；异步脚本使用 async_api，并等待异步方法。

```python
# 同步，已有同步 page。
from ysbrowser_sdk.sync_api import TrajectoryMouse
mouse = TrajectoryMouse(page)
result = mouse.drag_element(slider, dx=250)
```

```python
# 在 async def 中，page 和 slider 均来自异步 API。
from ysbrowser_sdk.async_api import TrajectoryMouse
mouse = TrajectoryMouse(page)
result = await mouse.drag_element(slider, dx=250)
```

`context.mouse(page)` 是工厂方法，异步代码也不加 await；后续 move/click/drag 等操作才加 await。

## ImportError 或找不到新 API

```powershell
python -c "import sys, ysbrowser_sdk; print(sys.executable); print(ysbrowser_sdk.__version__); print(ysbrowser_sdk.__file__)"
```


## 如何让模型自己决定时间

省略 duration_s，或显式传 None。0 不代表自动，负值也无效。点击 hold_ms=None 自动预测左右键按住时间；拖动前后等待、双击间隔是独立参数。

## 如何确认使用的模型与来源

```python
print(result.plan.model_id)
print(result.plan.source)
print(result.plan.data_source)
print(result.plan.task)
print(result.plan.warnings)
```

source 是引擎名，data_source 才是数据来源。零位移普通移动的 source 为 stationary。SDK 没有旧算法回退。

## mouse.position 是 None

位置尚未建立，或某次移动被取消/失败后无法确认。调用 synchronize(x,y)，或使用自带起点的 move_between/drag_between/drag_element。不要猜测原生鼠标位置。

## 设了 seed，为什么实际事件还是不同

seed 控制模型采样；操作系统调度、浏览器负载、布局变化和跳点不由 seed 控制。比较 plan.points 判断计划是否一致，比较 dispatched_points/skipped_points 判断执行情况。

## 中键点击为什么报错

当前没有中键按住时长的训练数据。显式指定 `hold_ms=40` 可使用中键原生按键事件；移动部分仍由模型生成。左右键可省略 hold_ms。

## 代理检查成功但页面依然失败

历史 check_state=success 不等于当前在线。check_proxy 是新的显式检查，还需看 stale/ok/kind。检查服务可用不等于目标网站可用；HTTP 4xx/5xx 与网络失败的判断不同。详见[代理](proxy.md)。

## 客户端证书为什么不能同时配代理

当前 SDK 明确只允许含客户端证书的 Context 直连。创建、继承默认代理或随后切换代理都会验证此限制。不能通过额外参数绕开这条支持边界；见[Context 选项](context-options.md)。

## 关闭浏览器后登录状态没了

普通 Context 不等于持久 user-data-dir。关闭前显式保存 storage_state，需要时保存 ContextConfig；下次创建时恢复。SessionStorage、页面运行现场、打开的标签页不会因此保存。见[配置与登录状态](storage.md)。

## 文档离线使用

解压完整手册后打开 README.html；不要只复制一个 HTML 文件。高亮样式、搜索索引与复制脚本都在 assets 中，不需要联网。浏览器禁止 clipboard API 时会尝试旧式复制，仍失败时可手动选中代码。
