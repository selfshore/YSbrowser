# TrajectoryModel

[SDK API 目录](../api-reference.md) · [使用章节](../mouse.md)

## 导入与准备

```python
from ysbrowser_sdk.motion import TrajectoryModel, MotionRequest

model = TrajectoryModel()
```

## 构造参数

```python signature
TrajectoryModel(path: 'str | Path | None' = None, *, steps: 'int' = 24, threads: 'int' = 2, drag_source: 'str' = 'auto', move_source: 'str' = 'bogazici', click_source: 'str' = 'bogazici', allow_extrapolation: 'bool' = False)
```

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `path` | str \| Path \| None | `None` | 模型目录，含 model.json 与 vector_field.onnx；None 使用随包模型，不接受旧模型 JSON。 |
| `steps` | int | `24` | ODE 积分步数，4–128；值增大通常增加耗时，不保证效果提高。 |
| `threads` | int | `2` | ONNX CPU 线程数，1–16。 |
| `drag_source` | str | `'auto'` | auto 按范围选择 user_mousedata/bogazici/sapimouse，或显式指定其中一个来源。 |
| `move_source` | str | `'bogazici'` | 普通移动条件来源：bogazici 或 sapimouse。 |
| `click_source` | str | `'bogazici'` | 接近点击和按住时长条件来源：bogazici 或 sapimouse。 |
| `allow_extrapolation` | bool | `False` | 允许距离/方向超出已观察范围；True 不代表范围外质量已验证。 |


## 实例状态

`core` 是 MultitaskMouseModel；`routes` 为 drag/move/click 的来源配置；建议通过构造参数设置，不直接修改运行中实例。

## 方法与属性索引

- [TrajectoryModel.domain](#trajectorymodel-domain)
- [TrajectoryModel.generate](#trajectorymodel-generate)
- [TrajectoryModel.generate_single_trajectory](#trajectorymodel-generate-single-trajectory)
- [TrajectoryModel.model_id](#trajectorymodel-model-id)
- [TrajectoryModel.sample_click_hold](#trajectorymodel-sample-click-hold)

## TrajectoryModel.domain

各来源/任务的已观察训练范围独立副本；包括 distance、direction_low/high、duration。不是精确联合支持区域。

**只读属性；异步程序也直接读取，不加 await。**

```python
print(model.domain)
```

## TrajectoryModel.generate

验证 MotionRequest，按任务与来源选择同一个网络的条件，生成绝对坐标的 MotionPlan。

```python signature
generate(request: 'MotionRequest', *, viewport=None, fallback='error') -> 'MotionPlan'
```

**同步计算/工厂方法；异步程序中也不加 await。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `request` | MotionRequest | `必填` | 包含 start/end/action/duration_s/target_size/seed 的模型请求。 |
| `viewport` | tuple[float,float] \| None | `None` | 轨迹边界 (width,height)，均为正数；鼠标省略时读取 Page.viewport_size，离线生成省略则不裁定视口。 |
| `fallback` | str | `'error'` | 只接受 error。范围/采样错误会抛异常，不替换为其他算法。 |


### 返回值

返回 [MotionPlan](MotionPlan.md)，绝对坐标 points 及来源、时间等字段见类型表。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
plan = model.generate(MotionRequest((100, 200), (800, 400), action="move", seed=42))
print(plan.source, plan.data_source, plan.points[-1])
```

### 注意事项

只有一种网络。自动选源不等于范围外质量保证；target_size 尚未作为模型条件学习。

[更多示例和完整业务规则](../mouse.md)

## TrajectoryModel.generate_single_trajectory

按相对位移生成轨迹字典；默认使用 drag 任务与本模型的自动来源路由。

```python signature
generate_single_trajectory(end_x, **kwargs) -> 'dict'
```

**同步计算/工厂方法；异步程序中也不加 await。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `end_x` | float | `必填` | 相对起点的水平位移；返回相对坐标轨迹，不操作浏览器。 |
| `kwargs` | 关键字参数 | `展开字段见下表` | 转发参数；本页下方展开支持的字段，不接受任意未知字段。 |
| `dy`（展开） | float | `0` | 相对起点的垂直位移，正数向下、负数向上。 |
| `task`（展开） | str | `'drag'` | 轨迹任务：drag、move/hover、click/approach_click。 |
| `source`（展开） | str \| None | `None` | 明确的数据来源条件：user_mousedata、bogazici、sapimouse；须存在对应训练任务。 不传时 TrajectoryModel 采用路由配置，低层模型采用固定默认来源。 |
| `duration_s`（展开） | float \| None | `None` | 运动总时长（秒）。None 由模型预测；显式值为 (0,30]，不含推理和按键前后等待。 |
| `seed`（展开） | int \| None | `None` | 随机种子；None 每次采样。相同模型、参数、种子可复现计划，不保证浏览器派发时序相同。 |
| `allow_extrapolation`（展开） | bool | `沿用实例` | 允许距离/方向超出已观察范围；True 不代表范围外质量已验证。 不传时 TrajectoryModel 沿用实例配置，低层模型默认 False；这里不要传 None。 |
| `n_points`（展开） | int \| None | `None` | 输出点数，显式整数 2–4096；None 按预测典型间隔选择 8–2049 个点。 |


### 返回值

返回 [相对轨迹字典](../result-structures.md#相对轨迹字典)。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
data = model.generate_single_trajectory(250, seed=42)
print(data["engine"], data["source"], data["trajectory"][-1])
```

### 注意事项

只有一种网络。自动选源不等于范围外质量保证；target_size 尚未作为模型条件学习。

[更多示例和完整业务规则](../mouse.md)

## TrajectoryModel.model_id

当前模型标识字符串。

**只读属性；异步程序也直接读取，不加 await。**

```python
print(model.model_id)
```

## TrajectoryModel.sample_click_hold

采样左/右键按住至释放的时长；使用 click_source 指定来源。

```python signature
sample_click_hold(*, button='left', seed=None)
```

**同步计算/工厂方法；异步程序中也不加 await。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `button` | str | `'left'` | 仅接受 left / right；该预测方法没有中键时长分支。 |
| `seed` | int \| None | `None` | 随机种子；None 每次采样。相同模型、参数、种子可复现计划，不保证浏览器派发时序相同。 |


### 返回值

返回 [点击时长字典](../result-structures.md#点击时长字典)。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
hold = model.sample_click_hold(button="left", seed=42)
print(hold["hold_ms"])
```

### 注意事项

只有一种网络。自动选源不等于范围外质量保证；target_size 尚未作为模型条件学习。

[更多示例和完整业务规则](../mouse.md)
