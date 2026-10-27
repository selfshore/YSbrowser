# TrajectoryMouse

[SDK API 目录](../api-reference.md) · [使用章节](../mouse.md)

## 导入与准备

```python
from ysbrowser_sdk.sync_api import TrajectoryMouse

# page 为已有同步 Page。
mouse = TrajectoryMouse(page)
mouse.synchronize(100, 200)
```

## 构造参数

```python signature
TrajectoryMouse(page, model: 'TrajectoryModel | str | Path | None' = None, *, fallback='error', viewport=None, **model_options)
```

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `page` | Page \| None | `必填` | 当前 Context 的原生页面；context.mouse 和鼠标构造必须提供；截图采集省略时选择 Context 页面。 |
| `model` | TrajectoryModel \| str \| Path \| None | `None` | 模型实例或含 model.json、vector_field.onnx 的目录；None 使用随包模型。 |
| `fallback` | str | `'error'` | 只接受 error。范围/采样错误会抛异常，不替换为其他算法。 |
| `viewport` | tuple[float,float] \| None | `None` | 轨迹边界 (width,height)，均为正数；鼠标省略时读取 Page.viewport_size，离线生成省略则不裁定视口。 |
| `model_options` | 关键字参数 | `展开字段见下表` | steps、threads、drag_source、move_source、click_source、allow_extrapolation；model 为实例时须在实例构造时配置。 |
| `steps`（展开） | int | `24` | ODE 积分步数，4–128；值增大通常增加耗时，不保证效果提高。 |
| `threads`（展开） | int | `2` | ONNX CPU 线程数，1–16。 |
| `drag_source`（展开） | str | `'auto'` | auto 按范围选择 user_mousedata/bogazici/sapimouse，或显式指定其中一个来源。 |
| `move_source`（展开） | str | `'bogazici'` | 普通移动条件来源：bogazici 或 sapimouse。 |
| `click_source`（展开） | str | `'bogazici'` | 接近点击和按住时长条件来源：bogazici 或 sapimouse。 |
| `allow_extrapolation`（展开） | bool | `False` | 允许距离/方向超出已观察范围；True 不代表范围外质量已验证。 |


## 实例状态

`page` 为绑定页面，`model` 为模型，`viewport` 为显式边界，`fallback` 只能为 error。`last_click_hold` 为自动预测的点击时长元数据，显式指定 hold_ms 时为 None。只读 position/pressed_buttons 见下文。

## 方法与属性索引

- [TrajectoryMouse.click](#trajectorymouse-click)
- [TrajectoryMouse.click_element](#trajectorymouse-click-element)
- [TrajectoryMouse.dblclick](#trajectorymouse-dblclick)
- [TrajectoryMouse.down](#trajectorymouse-down)
- [TrajectoryMouse.drag_between](#trajectorymouse-drag-between)
- [TrajectoryMouse.drag_by](#trajectorymouse-drag-by)
- [TrajectoryMouse.drag_element](#trajectorymouse-drag-element)
- [TrajectoryMouse.drag_element_to](#trajectorymouse-drag-element-to)
- [TrajectoryMouse.drag_to](#trajectorymouse-drag-to)
- [TrajectoryMouse.hover](#trajectorymouse-hover)
- [TrajectoryMouse.hover_element](#trajectorymouse-hover-element)
- [TrajectoryMouse.move](#trajectorymouse-move)
- [TrajectoryMouse.move_between](#trajectorymouse-move-between)
- [TrajectoryMouse.move_by](#trajectorymouse-move-by)
- [TrajectoryMouse.move_to](#trajectorymouse-move-to)
- [TrajectoryMouse.move_to_element](#trajectorymouse-move-to-element)
- [TrajectoryMouse.position](#trajectorymouse-position)
- [TrajectoryMouse.pressed_buttons](#trajectorymouse-pressed-buttons)
- [TrajectoryMouse.synchronize](#trajectorymouse-synchronize)
- [TrajectoryMouse.up](#trajectorymouse-up)
- [TrajectoryMouse.wheel](#trajectorymouse-wheel)

## TrajectoryMouse.click

按接近点击任务移动，然后按下、等待并释放。

```python signature
async click(x, y, *, seed=None, duration_s=None, target_size=None, button='left', hold_ms=None)
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `x` | float | `必填` | 终点横坐标，主 Frame 视口 CSS 像素；synchronize 中为即时定位坐标。 |
| `y` | float | `必填` | 终点纵坐标，主 Frame 视口 CSS 像素，向下为正。 |
| `seed` | int \| None | `None` | 随机种子；None 每次采样。相同模型、参数、种子可复现计划，不保证浏览器派发时序相同。 |
| `duration_s` | float \| None | `None` | 运动总时长（秒）。None 由模型预测；显式值为 (0,30]，不含推理和按键前后等待。 |
| `target_size` | tuple[float,float] \| None | `None` | 目标宽、高，均为正数；仅验证并保留兼容，本模型未学习目标尺寸条件。 |
| `button` | str | `'left'` | left/right/middle；预测按住时长仅支持 left/right，中键点击须显式传 hold_ms。 |
| `hold_ms` | float \| None | `None` | 按下至释放时间，毫秒，显式值 0–5000；None 预测左/右键时长。 |


### 返回值

返回 [MotionExecution](MotionExecution.md)，嵌套 [MotionPlan](MotionPlan.md)；[逐字段用法](../result-structures.md)。不是业务成功布尔值。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
result = mouse.click(600, 300, button="left")
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
result = await mouse.click(600, 300, button="left")
```

### 注意事项

坐标点击不进行元素命中检查；中键必须显式 hold_ms。自动时长可从 last_click_hold 读取。

[更多示例和完整业务规则](../mouse.md)

## TrajectoryMouse.click_element

检查元素、生成接近路径并完成点击。

```python signature
async click_element(locator, *, offset=None, seed=None, duration_s=None, target_size=None, button='left', hold_ms=None, timeout_ms=30000)
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `locator` | Locator \| str | `必填` | 属于当前 Page 的唯一 Locator 或选择器字符串。iframe 使用 frame_locator 得到的 Locator。 |
| `offset` | tuple[float,float] \| None | `None` | 相对元素边界框左上角的偏移，必须在框内；None 为中心。 |
| `seed` | int \| None | `None` | 随机种子；None 每次采样。相同模型、参数、种子可复现计划，不保证浏览器派发时序相同。 |
| `duration_s` | float \| None | `None` | 运动总时长（秒）。None 由模型预测；显式值为 (0,30]，不含推理和按键前后等待。 |
| `target_size` | tuple[float,float] \| None | `None` | 目标宽、高，均为正数；仅验证并保留兼容，本模型未学习目标尺寸条件。 |
| `button` | str | `'left'` | left/right/middle；预测按住时长仅支持 left/right，中键点击须显式传 hold_ms。 |
| `hold_ms` | float \| None | `None` | 按下至释放时间，毫秒，显式值 0–5000；None 预测左/右键时长。 |
| `timeout_ms` | 见说明 | `30000` | 元素检查/边界框步骤的毫秒超时，非负有限数；0 为不设超时，不是整个交互总预算。 |


### 返回值

返回 [MotionExecution](MotionExecution.md)，嵌套 [MotionPlan](MotionPlan.md)；[逐字段用法](../result-structures.md)。不是业务成功布尔值。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
result = mouse.click_element(page.get_by_role("button", name="保存"))
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
result = await mouse.click_element(page.get_by_role("button", name="保存"))
```

### 注意事项

需已知起点。trial hover 后页面仍可能布局变化；它不是原生 Locator.click 的完整重试流程。

[更多示例和完整业务规则](../mouse.md)

## TrajectoryMouse.dblclick

接近目标后连续点击两次，设置正确的 click_count。

```python signature
async dblclick(x, y, *, seed=None, duration_s=None, target_size=None, button='left', hold_ms=None, interval_ms=80)
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `x` | float | `必填` | 终点横坐标，主 Frame 视口 CSS 像素；synchronize 中为即时定位坐标。 |
| `y` | float | `必填` | 终点纵坐标，主 Frame 视口 CSS 像素，向下为正。 |
| `seed` | int \| None | `None` | 随机种子；None 每次采样。相同模型、参数、种子可复现计划，不保证浏览器派发时序相同。 |
| `duration_s` | float \| None | `None` | 运动总时长（秒）。None 由模型预测；显式值为 (0,30]，不含推理和按键前后等待。 |
| `target_size` | tuple[float,float] \| None | `None` | 目标宽、高，均为正数；仅验证并保留兼容，本模型未学习目标尺寸条件。 |
| `button` | str | `'left'` | left/right/middle；预测按住时长仅支持 left/right，中键点击须显式传 hold_ms。 |
| `hold_ms` | float \| None | `None` | 按下至释放时间，毫秒，显式值 0–5000；None 预测左/右键时长。 |
| `interval_ms` | float | `80` | 双击两次点击之间的等待，0–5000 毫秒；固定调用参数，不由模型预测。 |


### 返回值

返回 [MotionExecution](MotionExecution.md)，嵌套 [MotionPlan](MotionPlan.md)；[逐字段用法](../result-structures.md)。不是业务成功布尔值。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
result = mouse.dblclick(600, 300, interval_ms=80)
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
result = await mouse.dblclick(600, 300, interval_ms=80)
```

### 注意事项

两次按住使用本次采样的同一 hold_ms；双击间隔没有学习模型。

[更多示例和完整业务规则](../mouse.md)

## TrajectoryMouse.down

按住一个鼠标按钮。

```python signature
async down(*, button='left')
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `button` | str | `'left'` | left/right/middle；预测按住时长仅支持 left/right，中键点击须显式传 hold_ms。 |


### 返回值

返回 None，不返回轨迹执行对象。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
mouse.down(button="left")
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
await mouse.down(button="left")
```

### 注意事项

调用前需已知位置。成功后由调用者负责 finally 中 up；不要重复按下同一按钮。

[更多示例和完整业务规则](../mouse.md)

## TrajectoryMouse.drag_between

即时定位 A，按下后由模型拖至 B，再释放。

```python signature
async drag_between(x1, y1, x2, y2, *, duration_s=None, seed=None, target_size=None, trajectory='model', button='left', press_delay_ms=40, release_delay_ms=40)
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `x1` | float | `必填` | A 点横坐标；先即时定位到 A，再执行轨迹。 |
| `y1` | float | `必填` | A 点纵坐标。 |
| `x2` | float | `必填` | B 点横坐标。 |
| `y2` | float | `必填` | B 点纵坐标。 |
| `duration_s` | float \| None | `None` | 运动总时长（秒）。None 由模型预测；显式值为 (0,30]，不含推理和按键前后等待。 |
| `seed` | int \| None | `None` | 随机种子；None 每次采样。相同模型、参数、种子可复现计划，不保证浏览器派发时序相同。 |
| `target_size` | tuple[float,float] \| None | `None` | 目标宽、高，均为正数；仅验证并保留兼容，本模型未学习目标尺寸条件。 |
| `trajectory` | str | `'model'` | 只接受 model。旧 minimum_jerk 选项已移除。 |
| `button` | str | `'left'` | left/right/middle；预测按住时长仅支持 left/right，中键点击须显式传 hold_ms。 |
| `press_delay_ms` | float | `40` | 按下后、开始移动前的等待，0–5000 毫秒。 |
| `release_delay_ms` | float | `40` | 移动结束后、释放前的等待，0–5000 毫秒。 |


### 返回值

返回 [MotionExecution](MotionExecution.md)，嵌套 [MotionPlan](MotionPlan.md)；[逐字段用法](../result-structures.md)。不是业务成功布尔值。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
result = mouse.drag_between(100, 300, 500, 350)
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
result = await mouse.drag_between(100, 300, 500, 350)
```

### 注意事项

无需预先 synchronize；起终点必须不同，定位 A 的动作不是模型轨迹。

[更多示例和完整业务规则](../mouse.md)

## TrajectoryMouse.drag_by

从当前位置按下，按相对距离拖动，再释放。

```python signature
async drag_by(dx, dy=0, *, duration_s=None, seed=None, target_size=None, trajectory='model', button='left', press_delay_ms=40, release_delay_ms=40)
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `dx` | float | `必填` | 相对起点的水平位移，正数向右、负数向左。拖动时与 dy 不能同时为 0。 |
| `dy` | float | `0` | 相对起点的垂直位移，正数向下、负数向上。 |
| `duration_s` | float \| None | `None` | 运动总时长（秒）。None 由模型预测；显式值为 (0,30]，不含推理和按键前后等待。 |
| `seed` | int \| None | `None` | 随机种子；None 每次采样。相同模型、参数、种子可复现计划，不保证浏览器派发时序相同。 |
| `target_size` | tuple[float,float] \| None | `None` | 目标宽、高，均为正数；仅验证并保留兼容，本模型未学习目标尺寸条件。 |
| `trajectory` | str | `'model'` | 只接受 model。旧 minimum_jerk 选项已移除。 |
| `button` | str | `'left'` | left/right/middle；预测按住时长仅支持 left/right，中键点击须显式传 hold_ms。 |
| `press_delay_ms` | float | `40` | 按下后、开始移动前的等待，0–5000 毫秒。 |
| `release_delay_ms` | float | `40` | 移动结束后、释放前的等待，0–5000 毫秒。 |


### 返回值

返回 [MotionExecution](MotionExecution.md)，嵌套 [MotionPlan](MotionPlan.md)；[逐字段用法](../result-structures.md)。不是业务成功布尔值。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
result = mouse.drag_by(250, 0)
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
result = await mouse.drag_by(250, 0)
```

### 注意事项

必须已知位置且位移非零；不要预先手动 down。

[更多示例和完整业务规则](../mouse.md)

## TrajectoryMouse.drag_element

定位元素内起点，按下后拖动指定距离并释放。

```python signature
async drag_element(locator, dx, dy=0, *, start_offset=None, duration_s=None, seed=None, target_size=None, trajectory='model', button='left', press_delay_ms=40, release_delay_ms=40, timeout_ms=30000)
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `locator` | Locator \| str | `必填` | 属于当前 Page 的唯一 Locator 或选择器字符串。iframe 使用 frame_locator 得到的 Locator。 |
| `dx` | float | `必填` | 相对起点的水平位移，正数向右、负数向左。拖动时与 dy 不能同时为 0。 |
| `dy` | float | `0` | 相对起点的垂直位移，正数向下、负数向上。 |
| `start_offset` | tuple[float,float] \| None | `None` | 拖动起点相对源元素边界框左上角的偏移；None 为中心，必须在框内。 |
| `duration_s` | float \| None | `None` | 运动总时长（秒）。None 由模型预测；显式值为 (0,30]，不含推理和按键前后等待。 |
| `seed` | int \| None | `None` | 随机种子；None 每次采样。相同模型、参数、种子可复现计划，不保证浏览器派发时序相同。 |
| `target_size` | tuple[float,float] \| None | `None` | 目标宽、高，均为正数；仅验证并保留兼容，本模型未学习目标尺寸条件。 |
| `trajectory` | str | `'model'` | 只接受 model。旧 minimum_jerk 选项已移除。 |
| `button` | str | `'left'` | left/right/middle；预测按住时长仅支持 left/right，中键点击须显式传 hold_ms。 |
| `press_delay_ms` | float | `40` | 按下后、开始移动前的等待，0–5000 毫秒。 |
| `release_delay_ms` | float | `40` | 移动结束后、释放前的等待，0–5000 毫秒。 |
| `timeout_ms` | 见说明 | `30000` | 元素检查/边界框步骤的毫秒超时，非负有限数；0 为不设超时，不是整个交互总预算。 |


### 返回值

返回 [MotionExecution](MotionExecution.md)，嵌套 [MotionPlan](MotionPlan.md)；[逐字段用法](../result-structures.md)。不是业务成功布尔值。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
result = mouse.drag_element(page.get_by_role("slider"), dx=250, dy=0, start_offset=(12, 12), seed=42, timeout_ms=10000)
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
result = await mouse.drag_element(page.get_by_role("slider"), dx=250, dy=0, start_offset=(12, 12), seed=42, timeout_ms=10000)
```

### 注意事项

API 保留。dx/dy 是距离。无需先同步或手动 down；不会在拖动途中自动滚动页面。

[更多示例和完整业务规则](../mouse.md)

## TrajectoryMouse.drag_element_to

从源元素拖到目标元素内的指定点。

```python signature
async drag_element_to(locator, target, *, start_offset=None, target_offset=None, duration_s=None, seed=None, target_size=None, button='left', press_delay_ms=40, release_delay_ms=40, timeout_ms=30000)
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `locator` | Locator \| str | `必填` | 属于当前 Page 的唯一 Locator 或选择器字符串。iframe 使用 frame_locator 得到的 Locator。 |
| `target` | Locator \| str | `必填` | 拖动目标元素，须属于同一 Page；可以是另一个 frame 内可定位的元素。 |
| `start_offset` | tuple[float,float] \| None | `None` | 拖动起点相对源元素边界框左上角的偏移；None 为中心，必须在框内。 |
| `target_offset` | tuple[float,float] \| None | `None` | 终点相对目标元素边界框左上角的偏移；None 为中心，必须在框内。 |
| `duration_s` | float \| None | `None` | 运动总时长（秒）。None 由模型预测；显式值为 (0,30]，不含推理和按键前后等待。 |
| `seed` | int \| None | `None` | 随机种子；None 每次采样。相同模型、参数、种子可复现计划，不保证浏览器派发时序相同。 |
| `target_size` | tuple[float,float] \| None | `None` | 目标宽、高，均为正数；仅验证并保留兼容，本模型未学习目标尺寸条件。 |
| `button` | str | `'left'` | left/right/middle；预测按住时长仅支持 left/right，中键点击须显式传 hold_ms。 |
| `press_delay_ms` | float | `40` | 按下后、开始移动前的等待，0–5000 毫秒。 |
| `release_delay_ms` | float | `40` | 移动结束后、释放前的等待，0–5000 毫秒。 |
| `timeout_ms` | 见说明 | `30000` | 元素检查/边界框步骤的毫秒超时，非负有限数；0 为不设超时，不是整个交互总预算。 |


### 返回值

返回 [MotionExecution](MotionExecution.md)，嵌套 [MotionPlan](MotionPlan.md)；[逐字段用法](../result-structures.md)。不是业务成功布尔值。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
result = mouse.drag_element_to("#item", "#drop-zone")
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
result = await mouse.drag_element_to("#item", "#drop-zone")
```

### 注意事项

滚动后重新读取两端坐标，须同时可见；鼠标事件不保证实现网站的 HTML5 DataTransfer 拖放协议。

[更多示例和完整业务规则](../mouse.md)

## TrajectoryMouse.drag_to

从当前位置拖动到绝对坐标。

```python signature
async drag_to(x, y, *, duration_s=None, seed=None, target_size=None, trajectory='model', button='left', press_delay_ms=40, release_delay_ms=40)
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `x` | float | `必填` | 终点横坐标，主 Frame 视口 CSS 像素；synchronize 中为即时定位坐标。 |
| `y` | float | `必填` | 终点纵坐标，主 Frame 视口 CSS 像素，向下为正。 |
| `duration_s` | float \| None | `None` | 运动总时长（秒）。None 由模型预测；显式值为 (0,30]，不含推理和按键前后等待。 |
| `seed` | int \| None | `None` | 随机种子；None 每次采样。相同模型、参数、种子可复现计划，不保证浏览器派发时序相同。 |
| `target_size` | tuple[float,float] \| None | `None` | 目标宽、高，均为正数；仅验证并保留兼容，本模型未学习目标尺寸条件。 |
| `trajectory` | str | `'model'` | 只接受 model。旧 minimum_jerk 选项已移除。 |
| `button` | str | `'left'` | left/right/middle；预测按住时长仅支持 left/right，中键点击须显式传 hold_ms。 |
| `press_delay_ms` | float | `40` | 按下后、开始移动前的等待，0–5000 毫秒。 |
| `release_delay_ms` | float | `40` | 移动结束后、释放前的等待，0–5000 毫秒。 |


### 返回值

返回 [MotionExecution](MotionExecution.md)，嵌套 [MotionPlan](MotionPlan.md)；[逐字段用法](../result-structures.md)。不是业务成功布尔值。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
result = mouse.drag_to(700, 400)
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
result = await mouse.drag_to(700, 400)
```

### 注意事项

x/y 为终点，不是距离；不要预先手动 down。

[更多示例和完整业务规则](../mouse.md)

## TrajectoryMouse.hover

move 的同义接口，用于坐标悬停。

```python signature
async hover(x, y, **kwargs)
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `x` | float | `必填` | 终点横坐标，主 Frame 视口 CSS 像素；synchronize 中为即时定位坐标。 |
| `y` | float | `必填` | 终点纵坐标，主 Frame 视口 CSS 像素，向下为正。 |
| `kwargs` | 关键字参数 | `展开字段见下表` | 转发参数；本页下方展开支持的字段，不接受任意未知字段。 |
| `seed`（展开） | int \| None | `None` | 随机种子；None 每次采样。相同模型、参数、种子可复现计划，不保证浏览器派发时序相同。 |
| `duration_s`（展开） | float \| None | `None` | 运动总时长（秒）。None 由模型预测；显式值为 (0,30]，不含推理和按键前后等待。 |
| `target_size`（展开） | tuple[float,float] \| None | `None` | 目标宽、高，均为正数；仅验证并保留兼容，本模型未学习目标尺寸条件。 |


### 返回值

返回 [MotionExecution](MotionExecution.md)，嵌套 [MotionPlan](MotionPlan.md)；[逐字段用法](../result-structures.md)。不是业务成功布尔值。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
result = mouse.hover(600, 300)
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
result = await mouse.hover(600, 300)
```

### 注意事项

不会等待某个 CSS 悬停效果完成；需要时另加页面条件等待。

[更多示例和完整业务规则](../mouse.md)

## TrajectoryMouse.hover_element

move_to_element 的同义接口。

```python signature
async hover_element(locator, **kwargs)
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `locator` | Locator \| str | `必填` | 属于当前 Page 的唯一 Locator 或选择器字符串。iframe 使用 frame_locator 得到的 Locator。 |
| `kwargs` | 关键字参数 | `展开字段见下表` | 转发参数；本页下方展开支持的字段，不接受任意未知字段。 |
| `offset`（展开） | tuple[float,float] \| None | `None` | 相对元素边界框左上角的偏移，必须在框内；None 为中心。 |
| `seed`（展开） | int \| None | `None` | 随机种子；None 每次采样。相同模型、参数、种子可复现计划，不保证浏览器派发时序相同。 |
| `duration_s`（展开） | float \| None | `None` | 运动总时长（秒）。None 由模型预测；显式值为 (0,30]，不含推理和按键前后等待。 |
| `target_size`（展开） | tuple[float,float] \| None | `None` | 目标宽、高，均为正数；仅验证并保留兼容，本模型未学习目标尺寸条件。 |
| `timeout_ms`（展开） | float | `30000` | 元素检查/边界框步骤的毫秒超时，非负有限数；0 为不设超时，不是整个交互总预算。 |


### 返回值

返回 [MotionExecution](MotionExecution.md)，嵌套 [MotionPlan](MotionPlan.md)；[逐字段用法](../result-structures.md)。不是业务成功布尔值。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
result = mouse.hover_element("#target")
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
result = await mouse.hover_element("#target")
```

### 注意事项

kwargs 与 move_to_element 一致；不能把其他 Page 的 Locator 传入。

[更多示例和完整业务规则](../mouse.md)

## TrajectoryMouse.move

从已知位置移动到绝对视口坐标。

```python signature
async move(x, y, *, seed=None, duration_s=None, target_size=None)
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `x` | float | `必填` | 终点横坐标，主 Frame 视口 CSS 像素；synchronize 中为即时定位坐标。 |
| `y` | float | `必填` | 终点纵坐标，主 Frame 视口 CSS 像素，向下为正。 |
| `seed` | int \| None | `None` | 随机种子；None 每次采样。相同模型、参数、种子可复现计划，不保证浏览器派发时序相同。 |
| `duration_s` | float \| None | `None` | 运动总时长（秒）。None 由模型预测；显式值为 (0,30]，不含推理和按键前后等待。 |
| `target_size` | tuple[float,float] \| None | `None` | 目标宽、高，均为正数；仅验证并保留兼容，本模型未学习目标尺寸条件。 |


### 返回值

返回 [MotionExecution](MotionExecution.md)，嵌套 [MotionPlan](MotionPlan.md)；[逐字段用法](../result-structures.md)。不是业务成功布尔值。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
result = mouse.move(600, 300)
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
result = await mouse.move(600, 300)
```

### 注意事项

首次使用需同步位置；move 的参数不是相对距离。

[更多示例和完整业务规则](../mouse.md)

## TrajectoryMouse.move_between

即时定位 A，然后由模型完成 A→B 移动。

```python signature
async move_between(x1, y1, x2, y2, *, seed=None, duration_s=None, target_size=None)
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `x1` | float | `必填` | A 点横坐标；先即时定位到 A，再执行轨迹。 |
| `y1` | float | `必填` | A 点纵坐标。 |
| `x2` | float | `必填` | B 点横坐标。 |
| `y2` | float | `必填` | B 点纵坐标。 |
| `seed` | int \| None | `None` | 随机种子；None 每次采样。相同模型、参数、种子可复现计划，不保证浏览器派发时序相同。 |
| `duration_s` | float \| None | `None` | 运动总时长（秒）。None 由模型预测；显式值为 (0,30]，不含推理和按键前后等待。 |
| `target_size` | tuple[float,float] \| None | `None` | 目标宽、高，均为正数；仅验证并保留兼容，本模型未学习目标尺寸条件。 |


### 返回值

返回 [MotionExecution](MotionExecution.md)，嵌套 [MotionPlan](MotionPlan.md)；[逐字段用法](../result-structures.md)。不是业务成功布尔值。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
result = mouse.move_between(100, 200, 800, 400)
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
result = await mouse.move_between(100, 200, 800, 400)
```

### 注意事项

先验证计划才定位 A；当前已有按住的按钮时拒绝执行。

[更多示例和完整业务规则](../mouse.md)

## TrajectoryMouse.move_by

从已知位置按相对距离移动。

```python signature
async move_by(dx, dy=0, *, seed=None, duration_s=None, target_size=None)
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `dx` | float | `必填` | 相对起点的水平位移，正数向右、负数向左。拖动时与 dy 不能同时为 0。 |
| `dy` | float | `0` | 相对起点的垂直位移，正数向下、负数向上。 |
| `seed` | int \| None | `None` | 随机种子；None 每次采样。相同模型、参数、种子可复现计划，不保证浏览器派发时序相同。 |
| `duration_s` | float \| None | `None` | 运动总时长（秒）。None 由模型预测；显式值为 (0,30]，不含推理和按键前后等待。 |
| `target_size` | tuple[float,float] \| None | `None` | 目标宽、高，均为正数；仅验证并保留兼容，本模型未学习目标尺寸条件。 |


### 返回值

返回 [MotionExecution](MotionExecution.md)，嵌套 [MotionPlan](MotionPlan.md)；[逐字段用法](../result-structures.md)。不是业务成功布尔值。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
result = mouse.move_by(120, -30)
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
result = await mouse.move_by(120, -30)
```

### 注意事项

先建立位置；手动按住按钮时采用 drag 任务，结束不会自动释放。

[更多示例和完整业务规则](../mouse.md)

## TrajectoryMouse.move_to

move 的同义接口，移到绝对坐标。

```python signature
async move_to(x, y, **kwargs)
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `x` | float | `必填` | 终点横坐标，主 Frame 视口 CSS 像素；synchronize 中为即时定位坐标。 |
| `y` | float | `必填` | 终点纵坐标，主 Frame 视口 CSS 像素，向下为正。 |
| `kwargs` | 关键字参数 | `展开字段见下表` | 转发参数；本页下方展开支持的字段，不接受任意未知字段。 |
| `seed`（展开） | int \| None | `None` | 随机种子；None 每次采样。相同模型、参数、种子可复现计划，不保证浏览器派发时序相同。 |
| `duration_s`（展开） | float \| None | `None` | 运动总时长（秒）。None 由模型预测；显式值为 (0,30]，不含推理和按键前后等待。 |
| `target_size`（展开） | tuple[float,float] \| None | `None` | 目标宽、高，均为正数；仅验证并保留兼容，本模型未学习目标尺寸条件。 |


### 返回值

返回 [MotionExecution](MotionExecution.md)，嵌套 [MotionPlan](MotionPlan.md)；[逐字段用法](../result-structures.md)。不是业务成功布尔值。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
result = mouse.move_to(600, 300)
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
result = await mouse.move_to(600, 300)
```

### 注意事项

kwargs 与 move 完全一致。

[更多示例和完整业务规则](../mouse.md)

## TrajectoryMouse.move_to_element

检查并滚动元素后，沿模型轨迹移到元素内的目标点。

```python signature
async move_to_element(locator, *, offset=None, seed=None, duration_s=None, target_size=None, timeout_ms=30000)
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `locator` | Locator \| str | `必填` | 属于当前 Page 的唯一 Locator 或选择器字符串。iframe 使用 frame_locator 得到的 Locator。 |
| `offset` | tuple[float,float] \| None | `None` | 相对元素边界框左上角的偏移，必须在框内；None 为中心。 |
| `seed` | int \| None | `None` | 随机种子；None 每次采样。相同模型、参数、种子可复现计划，不保证浏览器派发时序相同。 |
| `duration_s` | float \| None | `None` | 运动总时长（秒）。None 由模型预测；显式值为 (0,30]，不含推理和按键前后等待。 |
| `target_size` | tuple[float,float] \| None | `None` | 目标宽、高，均为正数；仅验证并保留兼容，本模型未学习目标尺寸条件。 |
| `timeout_ms` | 见说明 | `30000` | 元素检查/边界框步骤的毫秒超时，非负有限数；0 为不设超时，不是整个交互总预算。 |


### 返回值

返回 [MotionExecution](MotionExecution.md)，嵌套 [MotionPlan](MotionPlan.md)；[逐字段用法](../result-structures.md)。不是业务成功布尔值。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
result = mouse.move_to_element(page.get_by_role("button", name="保存"), offset=(12, 12))
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
result = await mouse.move_to_element(page.get_by_role("button", name="保存"), offset=(12, 12))
```

### 注意事项

起点必须已知。offset 相对边界框左上角，不是元素中心。

[更多示例和完整业务规则](../mouse.md)

## TrajectoryMouse.position

最后确认的 (x,y) CSS 坐标；未知位置为 None。只读。

**只读属性；异步程序也直接读取，不加 await。**

```python
print(mouse.position)
```

## TrajectoryMouse.pressed_buttons

当前 Page 由此 API 记录的按住按钮集合 frozenset[str]；多个适配器共享状态。只读。

**只读属性；异步程序也直接读取，不加 await。**

```python
print(mouse.pressed_buttons)
```

## TrajectoryMouse.synchronize

即时移动到指定位置并记录状态。

```python signature
async synchronize(x, y)
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `x` | float | `必填` | 终点横坐标，主 Frame 视口 CSS 像素；synchronize 中为即时定位坐标。 |
| `y` | float | `必填` | 终点纵坐标，主 Frame 视口 CSS 像素，向下为正。 |


### 返回值

返回 None，不返回轨迹执行对象。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
mouse.synchronize(100, 200)
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
await mouse.synchronize(100, 200)
```

### 注意事项

不会生成模型轨迹；外部原生鼠标动作后重新同步。

[更多示例和完整业务规则](../mouse.md)

## TrajectoryMouse.up

释放指定按钮。

```python signature
async up(*, button='left')
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `button` | str | `'left'` | left/right/middle；预测按住时长仅支持 left/right，中键点击须显式传 hold_ms。 |


### 返回值

返回 None，不返回轨迹执行对象。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
mouse.up(button="left")
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
await mouse.up(button="left")
```

### 注意事项

释放失败会抛原生异常；页面关闭时清理已记录的按键状态。

[更多示例和完整业务规则](../mouse.md)

## TrajectoryMouse.wheel

派发原生滚轮事件。

```python signature
async wheel(delta_x=0, delta_y=0)
```

**异步入口：需要 await。同步入口：直接调用。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `delta_x` | float | `0` | 原生滚轮水平滚动像素；有限数。 |
| `delta_y` | float | `0` | 原生滚轮垂直滚动像素；正数通常向下。 |


### 返回值

返回 None，不返回轨迹执行对象。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
mouse.wheel(delta_x=0, delta_y=400)
```

异步调用（在 async def 内，使用异步入口创建的对象）：

```python
await mouse.wheel(delta_x=0, delta_y=400)
```

### 注意事项

没有滚轮轨迹模型；返回不表示滚动动画已结束。

[更多示例和完整业务规则](../mouse.md)
