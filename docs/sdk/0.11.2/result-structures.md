# 返回结构速查

先区分模型计划、实际派发结果和网页业务状态。生成了有效路径并完成派发，不保证网站已经接受操作。

## MotionExecution

由 SDK 鼠标移动、点击与拖动返回；不是字典，使用属性访问。

```python
result = mouse.drag_element(slider, dx=250)
print(result.plan.model_id)
print(result.dispatched_points, result.skipped_points)
```

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `plan` | MotionPlan | 本次运动计划 |
| `dispatched_points` | int | 已发送的移动点数，不计起点定位 |
| `skipped_points` | int | 因调度迟到跳过的计划点数 |
| `elapsed_s` | float | 移动派发秒数，不含推理、起点定位和按键等待 |
| `max_lateness_s` | float | 最大派发迟到秒数 |

正常完成时 `dispatched_points + skipped_points == len(plan.points) - 1`。

## MotionPlan

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `points` | list[list[float]] | `[绝对x, 绝对y, 累计秒数]` 列表，时间从 0 开始严格递增 |
| `source` | str | 引擎名 conditional_flow_matching_transformer；无位移普通移动为 stationary |
| `model_id` | str | 模型 ID |
| `data_source` | str | 实际来源条件 user_mousedata / bogazici / sapimouse |
| `task` | str | move / approach_click / drag |
| `predicted_cadence_s` | float 或 None | 预测的典型采样间隔；外部自行构造对象时可能为 None |
| `attempts` | int | 模型采样次数 |
| `warnings` | list[str] | 像素标定、未学习的条件等提示 |

```python
from dataclasses import asdict

data = asdict(result)
print(data["plan"]["points"][-1])
print(result.plan.points[-1][2])  # 计划运动总秒数
```

`plan.source` 是引擎名，不是数据集名。坐标是主 Frame 视口 CSS 像素，不是屏幕坐标。

## 相对轨迹字典

由 `generate_single_trajectory()` 返回，可直接按键访问。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `trajectory` | list[list[float]] | `[相对x, 相对y, 累计秒数]`；首点 `[0,0,0]` |
| `end_x` / `end_y` | float | 最终相对位移 |
| `total_points` | int | trajectory 的点数 |
| `duration_s` | float | 轨迹总秒数 |
| `predicted_cadence_s` | float | 典型采样间隔 |
| `model_id` | str | 模型 ID |
| `source` | str | 此字典中 source 是数据来源条件 |
| `engine` | str | 引擎名称 |
| `warnings` | list[str] | 提示列表 |

```python
from ysbrowser_sdk.motion import TrajectoryModel

model = TrajectoryModel()
data = model.generate_single_trajectory(250, seed=42)
print(data["trajectory"][-1])
print(data["engine"], data["source"])
```

该函数不移动浏览器。要实际拖动，应使用鼠标 API；手工播放时别把累计秒数当作每步 sleep，也别把相对坐标当绝对坐标。

## 点击时长字典

由 `sample_click_hold()` 返回；鼠标自动点击采样时也存入 `mouse.last_click_hold`。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `hold_ms` | float | 按下至释放的毫秒数 |
| `button` | str | left / right |
| `source` | str | 数据来源条件 |
| `model_id` | str | 模型 ID |
| `engine` | str | 引擎名称 |

显式传入 hold_ms 的点击将 last_click_hold 设为 None。drag_element 的前后等待不使用此字段。

## 代理与其他结果

| 调用 | 返回类型 | 逐字段说明 |
| --- | --- | --- |
| `context.proxy_status()` / `set_proxy()` | ProxyStatus | [配置、历史状态、health](reference/ProxyStatus.md) |
| `context.check_proxy()` | ProxyHealthResult | [ok/kind/stale/exit_ip 等](reference/ProxyHealthResult.md) |
| `browser.capabilities` | BrowserCapabilities | [功能能力字段](reference/BrowserCapabilities.md) |
| `context.export_config()` | dict | [schema 1/2 配置格式](storage.md#json-格式) |
| `context.save_storage_state()` | dict | [cookies/origins/IndexedDB](storage.md#保存登录状态) |
| `context.capture_diagnostics()` | dict | [文件清单与错误结构](diagnostics-errors.md#返回字段) |
| `SDKError.to_dict()` | dict | [code/stage/message/context_id/details](reference/SDKError.md) |

如果方法写明返回 None，就没有可读取的结果对象。异步方法未 await 时得到的是 coroutine，也不是结果对象。
