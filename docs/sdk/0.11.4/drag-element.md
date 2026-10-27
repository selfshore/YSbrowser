# drag_element：拖动元素一定距离

指定滑块手柄等元素，由 SDK 完成定位、按下、轨迹移动和释放。

```python
result = mouse.drag_element(slider, dx=250, dy=0)
```

这里表示从元素上的起点**向右拖动 250 CSS 像素**，不是把鼠标拖到 x=250。

## 完整签名

```python signature
drag_element(
    locator, dx, dy=0, *, start_offset=None,
    duration_s=None, seed=None, target_size=None,
    trajectory="model", button="left",
    press_delay_ms=40, release_delay_ms=40, timeout_ms=30000,
) -> MotionExecution
```

同步 `mouse.drag_element(...)`；异步 `await mouse.drag_element(...)`。无需先 synchronize，也不要预先 down。

## 每个参数

| 参数 | 类型 | 默认值 | 含义与限制 |
| --- | --- | --- | --- |
| `locator` | Locator 或 str | 必填 | 当前 Page 内唯一的元素；建议传滑块手柄，而不是整条滑轨 |
| `dx` | int / float | 必填 | 相对起点的水平距离，正向右、负向左；有限数 |
| `dy` | int / float | 0 | 相对起点的垂直距离，正向下、负向上；与 dx 不能同时为 0 |
| `start_offset` | tuple[float,float] 或 None | None | 相对元素边界框左上角的偏移；None 为中心；坐标必须位于框内 |
| `duration_s` | float 或 None | None | 运动总时长；None 自动预测；显式值必须在 (0,30] 秒内 |
| `seed` | int 或 None | None | 随机种子。固定值复现计划，不能保证实际事件派发完全一致 |
| `target_size` | tuple[float,float] 或 None | None | 默认使用元素边界框宽高；当前仅验证，网络未学习尺寸条件 |
| `trajectory` | str | model | 仅接受 model；旧 minimum_jerk 已移除 |
| `button` | str | left | left/right/middle；普通滑块通常使用 left |
| `press_delay_ms` | float | 40 | 按下后开始运动前的等待，0–5000 毫秒 |
| `release_delay_ms` | float | 40 | 运动结束后释放前的等待，0–5000 毫秒 |
| `timeout_ms` | float | 30000 | 元素检查、边界框等步骤的原生超时；0 表示不设置超时，不是整个拖动的总预算 |

坐标是主 Frame 视口 CSS 像素，不是屏幕物理像素。`start_offset=(12,12)` 的含义是边界框左上角向右 12、向下 12。

## 常见调用方式

```python
# 自动预测运动时间。
result = mouse.drag_element(slider, dx=250)

# 指定元素内起点与固定运动时间。
result = mouse.drag_element(
    slider, dx=250, dy=3,
    start_offset=(12, 12), duration_s=0.8,
    seed=42, timeout_ms=10000,
)

# 向左拖动；元素必须有足够的可用拖动范围。
result = mouse.drag_element(slider, dx=-120)

# 用 CSS 选择器定位元素。
result = mouse.drag_element("#slider-handle", dx=136)
```

默认 `drag_source="auto"`：136px 向右等覆盖范围内请求优先使用个人拖动条件；250px 等请求通常选择公共拖动条件。两者都来自同一个 Transformer。查看 `result.plan.data_source` 确认。

## 返回结构与字段含义

```python
print(result.plan.source)              # 生成引擎
print(result.plan.model_id)            # 模型 ID
print(result.plan.data_source)         # 数据来源条件
print(result.plan.task)                # drag
print(result.plan.points[0])           # [起点绝对 x, 起点绝对 y, 0]
print(result.plan.points[-1])          # [终点绝对 x, 终点绝对 y, 计划总秒数]
print(result.dispatched_points)        # 实际派发点数
print(result.skipped_points)           # 调度延迟跳过的点数
print(result.elapsed_s)                # 实际移动派发耗时
print(result.max_lateness_s)           # 最大调度迟到秒数
```

| 层级 / 字段 | 类型 | 含义 |
| --- | --- | --- |
| `result` | MotionExecution | 这一次操作的移动执行结果，不是元素是否移动成功的布尔值 |
| `plan.points` | list[list[float]] | 绝对坐标的 [x,y,累计秒数]；第三列不是间隔或毫秒 |
| `plan.source` | str | conditional_flow_matching_transformer |
| `plan.model_id` | str | 随包或指定模型标识 |
| `plan.data_source` | str | user_mousedata / bogazici / sapimouse |
| `plan.task` | str | drag |
| `plan.predicted_cadence_s` | float | 典型采样间隔，不等于浏览器实际事件间隔 |
| `plan.attempts` | int | 有效路径采样尝试次数 |
| `plan.warnings` | list[str] | 像素标定、未学习条件等提示 |
| `dispatched_points` | int | 实际发送的移动点数；起点定位不计在内 |
| `skipped_points` | int | 计划里因迟到而跳过的点数 |
| `elapsed_s` | float | 移动派发耗时，不包含推理、起点定位、按键前后等待 |
| `max_lateness_s` | float | 最大调度迟到秒数 |

转换为字典保存：

```python
from dataclasses import asdict
import json

data = asdict(result)
with open("drag-result.json", "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=2)
```

不要写 `result["plan"]`：它是数据类，先 `.plan` 或 `asdict(result)`。

## iframe 与 ShadowRoot

```python
slider = page.frame_locator("iframe#panel").get_by_role("slider")
result = mouse.drag_element(slider, dx=136)

# 配套 Patchright 支持的 Shadow DOM 定位路径。
slider = page.locator("slider-panel").get_by_role("slider")
result = mouse.drag_element(slider, dx=136)
```

iframe 的 Locator 提供的边界框会用于主 Frame 坐标，不要手动再叠加一次 iframe 偏移。闭合根访问依赖配套浏览器/Patchright，不保证 XPath 能穿过 ShadowRoot；页面脚本读取 `host.shadowRoot` 也不等价。

## 如何检查页面真的响应了

完成派发不等于业务一定成功。网页可能把滑块限制在轨道内，或者需要特定拖放协议。对于移动的 DOM 元素，可比较边界框；对于值型滑块，应读取值或 ARIA 状态。

```python
before = slider.bounding_box()
result = mouse.drag_element(slider, dx=136)
after = slider.bounding_box()
if before is not None and after is not None:
    print("元素实际水平变化：", after["x"] - before["x"])
print("滑块值：", slider.get_attribute("aria-valuenow"))
```

对于手柄本身不移动、仅更新值的控件，边界框变化可能为 0，应检查应用实际状态。不要仅用 `if result:` 判断成功。

## 容易遇到的问题

| 表现 | 原因与处理 |
| --- | --- |
| 调用后没有动作，只打印 coroutine | 异步接口忘了 await；同步代码用 sync_api |
| offset 报错 | 偏移超过元素宽高；先 bounding_box，或省略以使用中心 |
| 拖到了错误位置 | dx/dy 是距离；拖到绝对坐标用 drag_to，元素间拖动用 drag_element_to |
| 只能移动一小段 | 页面轨道限制、目标选择错，或 CSS/设备像素混用；查看页面值/边界框 |
| Outside observed domain | 显式来源覆盖不到该请求；使用 auto 或覆盖范围合适的公共来源；允许外推不代表效果可靠 |
| Position / Endpoint outside viewport | 计划起终点超出视口；先调整页面/目标，API 不会中途自动滚动 |
| skipped_points 大于 0 | 调度迟到会跳过中间点；看实际事件与页面结果，不把计划视为完整浏览器事件记录 |
| 按钮已按住的错误 | 不要先 down 再 drag_element；手动 down 配 move_by，最后 finally up |
| 同一元素有多个匹配 | 使用明确 Locator、过滤器或 nth，避免原生 strict-mode 错误 |
| 看起来有回摆或曲线不合预期 | 当前模型仍有细小回摆；API 整合不代表模型质量已经提高 |

这个函数会执行 trial hover 与滚动、读取边界框、生成路径，再即时定位到起点并按下。页面在读取坐标后继续移动布局时，仍可能错过目标；调用期间避免其他任务同时操作同一 Page。

## 可运行的同步与异步程序

打开[本地滑块示例](examples/drag_element.py)。它只加载本地内存页面，默认有界面：

```powershell
python .\examples\drag_element.py --distance 250
python .\examples\drag_element.py --distance 136 --async
```

也可查看 [TrajectoryMouse 每个方法的参数表](reference/TrajectoryMouse.md)。
