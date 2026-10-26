# 鼠标操作总览

SDK 的移动、接近点击和拖动统一使用随包的条件 Flow Matching Transformer。同步与异步方法名、参数相同；异步操作需要 `await`。

> `drag_element()` 用法详见[拖动元素一定距离](drag-element.md)。每个方法的全部参数见 [TrajectoryMouse 参考](reference/TrajectoryMouse.md)。

## 快速开始：A 点移动到 B 点

```python
from ysbrowser_sdk.sync_api import TrajectoryMouse

# page 为已有的同步 Page，也可以用 mouse = context.mouse(page)。
mouse = TrajectoryMouse(page)
result = mouse.move_between(100, 200, 800, 400)
print(result.plan.source)       # conditional_flow_matching_transformer
print(result.plan.data_source)  # bogazici
print(result.plan.model_id)
```

`move_between(x1, y1, x2, y2)` 先验证整条路径，再即时定位到 A，然后由模型完成 A→B。调用前不需要 `synchronize()`。不传 `duration_s` 时由模型预测运动时长。

```python
from ysbrowser_sdk.async_api import TrajectoryMouse

mouse = TrajectoryMouse(page)  # page 为异步 Page
result = await mouse.move_between(100, 200, 800, 400)
```

## 创建鼠标对象

```python
mouse = context.mouse(page)
# 或：
mouse = TrajectoryMouse(page)
# 调整同一个模型的任务来源与推理配置：
mouse = context.mouse(page, steps=24, drag_source="auto")
```

| 参数 | 默认值 | 用途 |
|---|---|---|
| `page` | 必填 | 所属同步/异步 Page；`context.mouse()` 要求 Page 属于该 Context |
| `model` | `None` | `TrajectoryModel` 实例或模型目录；省略则使用随包模型 |
| `viewport` | `None` | `(width, height)`；省略时读取 Page 的 viewport_size，显式值优先 |
| `fallback` | `'error'` | 仅接受 error；生成失败抛异常 |
| `steps` | `24` | 整数 4–128，ODE 积分步数；增加会增加计算量 |
| `threads` | `2` | ONNX CPU 线程数，整数 1–16 |
| `drag_source` | `'auto'` | 自动选择训练范围覆盖当前请求的拖动来源，或指定一个来源 |
| `move_source` | `'bogazici'` | 普通移动来源：bogazici / sapimouse |
| `click_source` | `'bogazici'` | 接近点击轨迹与按住时长来源：bogazici / sapimouse |
| `allow_extrapolation` | `False` | 是否允许超出已观察距离/方向范围；不保证范围外质量 |

传入 `model` 实例时，将 steps、threads 和来源等选项设在该实例上，不要同时传给鼠标构造器。

```python
from ysbrowser_sdk.sync_api import TrajectoryModel, TrajectoryMouse

model = TrajectoryModel(drag_source="user_mousedata", steps=24)
mouse = TrajectoryMouse(page, model=model)
```

`drag_source='auto'` 按 user_mousedata → bogazici → sapimouse 的顺序，选择距离与方向处于训练范围的来源条件，仍使用同一个网络。个人拖动范围约 111–174 像素、主要向右；范围外一般使用公共拖动条件。返回值 `plan.data_source` 标明实际来源。

## 坐标、状态与公共参数

坐标均为主 Frame 视口左上角为原点的 CSS 像素，x 向右为正，y 向下为正，不是桌面屏幕坐标。iframe 的 Locator 会转换到主 Frame 坐标。操作不会移动操作系统的真实鼠标光标。

| 参数 | 默认值 | 用途 |
|---|---|---|
| `seed` | `None` | 整数随机种子；相同模型、配置和运行环境下用于复现；None 随机采样 |
| `duration_s` | `None` | 运动时长；None 自动预测，显式值须为 `(0,30]` 秒 |
| `target_size` | `None` | `(宽,高)`，须为正数；保留 SDK 参数兼容，本模型未学习目标尺寸条件 |
| `button` | `'left'` | left / right / middle |
| `timeout_ms` | `30000` | 元素定位与动作检查超时，毫秒；0 沿用原生无限超时语义 |

坐标操作从 `mouse.position` 开始。首次使用 `move()` / `click()` / `move_by()` 等方法前，先 `synchronize()` 或 `move_between()`。`drag_element()`、`drag_element_to()` 和 `drag_between()` 自带起点，无需先同步。

```python
mouse.synchronize(100, 200)  # 即时移动并记录起点，返回 None
print(mouse.position)       # (100, 200)，未知时为 None
print(mouse.pressed_buttons) # frozenset()，当前由本 API 按住的键
```

同一 Page 的多个鼠标实例共享位置、按键状态和操作锁。直接调用 `page.mouse` 或原生 Locator 操作后，本 API 无法自动获知位置/按键变化；应先释放外部按住的按键，再用 `synchronize()` 恢复状态。

## 普通移动与悬停

```python signature
move(x, y, *, seed=None, duration_s=None, target_size=None)
move_to(x, y, **kwargs)
hover(x, y, **kwargs)
move_by(dx, dy=0, *, seed=None, duration_s=None, target_size=None)
move_between(x1, y1, x2, y2, *, seed=None, duration_s=None, target_size=None)
```

| 方法 | 起点与终点 |
|---|---|
| `move` / `move_to` / `hover` | 已知当前位置 → 绝对坐标 `(x,y)` |
| `move_by` | 已知当前位置 → 当前坐标加 `(dx,dy)` |
| `move_between` | 显式 `(x1,y1)` → `(x2,y2)` |

以上返回 `MotionExecution`。`move()` 保持旧版绝对坐标语义。显式 `down()` 后调用 move/move_to/move_by/hover 会按拖动任务生成路径，但不会自动释放按键。

```python
mouse.move_between(100, 200, 500, 300)
mouse.move_to(700, 400)
mouse.move_by(-100, 50)
```

### 移到元素

```python signature
move_to_element(locator, *, offset=None, seed=None, duration_s=None,
                target_size=None, timeout_ms=30000)
hover_element(locator, **kwargs)
```

`locator` 为当前 Page 的 Locator 或选择器字符串。`offset=None` 表示元素中心；`offset=(x,y)` 为相对边界框左上角的偏移，必须位于边界框内。会先进行原生 trial hover 检查与滚动，再获取坐标。起点必须已同步，返回 `MotionExecution`。

```python
mouse.synchronize(100, 100)
mouse.hover_element(page.get_by_role("button", name="保存"))
mouse.move_to_element("#target", offset=(10, 12))
```

## 点击、双击与按键

```python signature
click(x, y, *, seed=None, duration_s=None, target_size=None,
      button='left', hold_ms=None)
click_element(locator, *, offset=None, seed=None, duration_s=None,
              target_size=None, button='left', hold_ms=None, timeout_ms=30000)
dblclick(x, y, *, seed=None, duration_s=None, target_size=None,
         button='left', hold_ms=None, interval_ms=80)
down(*, button='left')
up(*, button='left')
```

click/click_element/dblclick 先按接近点击任务移动，再按下和释放，返回 `MotionExecution`。`duration_s` 只控制移动时间。

| 参数 / 属性 | 用途 |
|---|---|
| `hold_ms=None` | 模型预测左/右键按住至释放的毫秒数 |
| `hold_ms=数值` | 显式指定 0–5000 毫秒；中键须显式指定 |
| `interval_ms` | 双击两次点击之间的等待，0–5000 毫秒；该间隔不由模型学习 |
| `last_click_hold` | 自动预测的 hold_ms/button/source/model_id/engine 字典；显式 hold_ms 时为 None |

双击的两次按住使用本次采样的同一 hold_ms，并派发正确的 click_count。`down()` / `up()` 返回 None；down 前需已知位置；它们是原生按键事件，不生成轨迹。显式按住键时不能再调用自动 click/drag，需先 up。

```python
mouse.click(500, 300)                         # 自动预测移动时间和按住时长
mouse.click_element("#submit", button="right")
mouse.dblclick(600, 300, interval_ms=80)

mouse.synchronize(100, 200)
mouse.down()
try:
    mouse.move_by(136, 0)                    # 按住期间自动使用拖动任务
finally:
    mouse.up()
```

## 拖动

```python signature
drag_by(dx, dy=0, *, duration_s=None, seed=None, target_size=None,
        trajectory='model', button='left', press_delay_ms=40, release_delay_ms=40)
drag_to(x, y, *, duration_s=None, seed=None, target_size=None,
        trajectory='model', button='left', press_delay_ms=40, release_delay_ms=40)
drag_between(x1, y1, x2, y2, *, duration_s=None, seed=None, target_size=None,
             trajectory='model', button='left', press_delay_ms=40, release_delay_ms=40)
drag_element(locator, dx, dy=0, *, start_offset=None, duration_s=None, seed=None,
             target_size=None, trajectory='model', button='left',
             press_delay_ms=40, release_delay_ms=40, timeout_ms=30000)
drag_element_to(locator, target, *, start_offset=None, target_offset=None,
                duration_s=None, seed=None, target_size=None, button='left',
                press_delay_ms=40, release_delay_ms=40, timeout_ms=30000)
```

| 方法 | 用途 |
|---|---|
| `drag_by` | 已知当前位置按下，按相对距离拖动，释放 |
| `drag_to` | 已知当前位置按下，拖到绝对坐标，释放 |
| `drag_between` | 即时定位 A，按下，模型拖至 B，释放 |
| `drag_element` | 定位元素起点，按下，按 `(dx,dy)` 拖动，释放 |
| `drag_element_to` | 从元素拖到另一个元素，释放 |

所有拖动返回 `MotionExecution`，位移须非零。`trajectory` 仅接受 model。

`start_offset` / `target_offset` 相对各自元素边界框左上角，None 表示中心。元素间拖动会在滚动后重新读取两端边界框；两点必须同时处于视口内。这里生成鼠标拖动事件，不保证每个网站的 HTML5 DataTransfer 拖放逻辑都能响应。

`press_delay_ms` 为按下后的等待；`release_delay_ms` 为移动结束、释放前的等待，各为 0–5000 毫秒。这些等待由调用参数控制，不包含在模型运动时长内。

```python
result = mouse.drag_element(
    page.get_by_role("slider"),
    dx=136,
    start_offset=(12, 12),
    seed=42,
    timeout_ms=10000,
)
result = mouse.drag_between(100, 300, 500, 350)
result = mouse.drag_element_to("#item", "#drop-zone")
```

在 iframe 中传对应的 Locator：

```python
slider = page.frame_locator("iframe").get_by_role("slider")
result = mouse.drag_element(slider, dx=136)
```

闭合 ShadowRoot 的定位能力来自配套 Patchright/浏览器。已在配套浏览器的本地页面验证闭合根内按钮和 iframe 按钮的点击；模型不自行穿透 DOM。

## 滚轮

```python
mouse.wheel(delta_x=0, delta_y=400)
```

派发原生 wheel 事件，返回 None，不等待滚动动画结束。两个参数为有限像素值。当前没有滚轮学习模型，wheel 不调用轨迹网络。

## MotionExecution 返回值

| 字段 | 类型 | 含义 |
|---|---|---|
| `plan` | MotionPlan | 本次移动计划 |
| `dispatched_points` | int | 实际发送的移动点数 |
| `skipped_points` | int | 因调度延迟跳过的计划点数 |
| `elapsed_s` | float | 移动派发耗时，不含推理、起点即时定位、按键等待 |
| `max_lateness_s` | float | 最大调度迟到秒数 |

### MotionPlan

| 字段 | 含义 |
|---|---|
| `points` | 绝对视口坐标点列表 `[x, y, 从该计划起点开始的累计秒数]` |
| `source` | 引擎名 conditional_flow_matching_transformer；零位移普通移动为 stationary |
| `model_id` | 使用的模型 ID |
| `data_source` | 实际数据来源条件 user_mousedata / bogazici / sapimouse |
| `task` | move / approach_click / drag |
| `predicted_cadence_s` | 模型预测的典型事件间隔 |
| `attempts` | 生成有效路径使用的采样次数 |
| `warnings` | 范围外推、像素标定、未学习条件等提示字符串列表 |

```python
print(result.plan.model_id, result.plan.source, result.plan.data_source)
print(result.plan.points[-1][2])    # 计划运动时长
print(result.elapsed_s)            # 实际移动执行耗时
print(result.skipped_points)
```

时间列是累计秒数，不是毫秒、不是相邻点间隔。起点不计入 dispatched_points，正常完成时 dispatched_points + skipped_points = len(plan.points) - 1。

## 单独生成轨迹

```python
from ysbrowser_sdk.motion import TrajectoryModel, MotionRequest

model = TrajectoryModel()
result = model.generate_single_trajectory(136, seed=42)
print(result["trajectory"])

plan = model.generate(MotionRequest(
    start=(100, 200), end=(500, 300), action="move", seed=42,
))
```

`TrajectoryModel(path=None, *, steps=24, threads=2, drag_source='auto', move_source='bogazici', click_source='bogazici', allow_extrapolation=False)` 创建随包或指定目录的模型。自定义目录需包含 model.json 和 vector_field.onnx。

`generate(request, *, viewport=None, fallback='error')` 返回 MotionPlan，不操作浏览器。MotionRequest 参数为 start、end、action（move/click/drag，默认 move）、duration_s=None、target_size=None、seed=None。

`generate_single_trajectory(end_x, **kwargs)` 返回字典，trajectory 使用相对起点坐标；其他字段为 end_x、end_y、total_points、duration_s、predicted_cadence_s、model_id、source（数据来源）、engine、warnings。

可选 kwargs：dy=0、task='drag'、source=显式来源、duration_s=None、seed=None、allow_extrapolation=False、n_points=None。n_points 整数范围 2–4096；None 由典型采样间隔决定。未指定 source 时使用模型的任务来源配置。

`sample_click_hold(*, button='left', seed=None)` 返回 hold_ms/button/source/model_id/engine 字典，只支持 left/right。

更底层的 `MultitaskMouseModel` 和 `TrajectoryPrediction` 可从 `ysbrowser_sdk.motion` 导入。它的 `generate(dx, dy=0, *, task='drag', source=None, duration_s=None, seed=None, allow_extrapolation=False, n_points=None)` 返回 TrajectoryPrediction，字段为 trajectory、model_id、task、source、duration_s、predicted_cadence_s、warnings、attempts、engine。底层默认 drag 来源固定为 user_mousedata；需要自动选源请使用 TrajectoryModel。

## 错误与迁移

无效输入、超出训练范围、路径越界或有限次数采样失败会抛 ValueError；未知鼠标位置、已按住键却启动另一次完整点击/拖动会抛 RuntimeError。页面/元素错误沿用原生异常。自动点击和拖动在异常或异步取消时尝试释放其按下的按键。

0.11.1 移除了旧 GMM、hurdle-clock、minimum-jerk 的运行代码和权重。DragTrajectoryModel 不再导出；改为 TrajectoryModel。fallback='minimum_jerk' 和 trajectory='minimum_jerk' 不再支持；旧 JSON 模型不能作为新模型目录使用。

独立扩展包 ysbrowser-checkpoint-mouse、ysbrowser-high-order-mouse、ysbrowser-learned-mouse、ysbrowser-motion-dit 不再需要，使用 `ysbrowser_sdk.sync_api` / `async_api` 即可。

`page.mouse`、原生 Locator.click() 等仍是 Patchright 原生入口；要使用模型，调用 `context.mouse(page)` 或 `TrajectoryMouse(page)`，不需要修改浏览器 Page 类。

当前模型预测总时长与典型采样间隔，未预测逐点间隔抖动；公共数据源像素未跨设备统一标定。推理失败不会改用其他算法。异步推理在后台线程进行，所有 Page/Locator 操作在原事件循环执行。

## 其他工具的接口参考

- [Playwright Mouse](https://playwright.dev/python/docs/api/class-mouse)：绝对视口坐标的 move、按键与 wheel。
- [Selenium Mouse actions](https://www.selenium.dev/documentation/webdriver/actions_api/mouse/)：相对偏移、移到元素、元素间拖动。
- [DrissionPage 动作链](https://www.drissionpage.cn/browser_control/actions/)：区分绝对目标与相对位移。

本 SDK 保留 `move(x,y)` 的既有绝对坐标含义，另提供 `move_by(dx,dy)` 表示相对移动；不直接照搬其他库中可能不同的同名语义。
