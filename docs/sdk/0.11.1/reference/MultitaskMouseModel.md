# MultitaskMouseModel

[SDK API 目录](../api-reference.md) · [使用章节](../mouse.md)

## 导入与准备

```python
from ysbrowser_sdk.motion import MultitaskMouseModel

model = MultitaskMouseModel()
```

## 构造参数

```python signature
MultitaskMouseModel(path=None, *, steps=24, threads=2)
```

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `path` | str \| Path \| None | `None` | 模型目录，含 model.json 与 vector_field.onnx；None 使用随包模型，不接受旧模型 JSON。 |
| `steps` | int | `24` | ODE 积分步数，4–128；值增大通常增加耗时，不保证效果提高。 |
| `threads` | int | `2` | ONNX CPU 线程数，1–16。 |


## 实例状态

`info` 为配置字典，含 groups/default_routes；`path` 是模型目录，`steps` 是推理步数。`session` 为内部 ONNX 会话，普通使用不需要操作它。

## 方法与属性索引

- [MultitaskMouseModel.generate](#multitaskmousemodel-generate)
- [MultitaskMouseModel.generate_single_trajectory](#multitaskmousemodel-generate-single-trajectory)
- [MultitaskMouseModel.model_id](#multitaskmousemodel-model-id)
- [MultitaskMouseModel.sample_click_hold](#multitaskmousemodel-sample-click-hold)

## MultitaskMouseModel.generate

低层相对坐标轨迹生成，不自动选择个人/公共拖动来源。

```python signature
generate(dx, dy=0, *, task='drag', source=None, duration_s=None, seed=None, allow_extrapolation=False, n_points=None)
```

**同步计算/工厂方法；异步程序中也不加 await。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `dx` | float | `必填` | 相对起点的水平位移，正数向右、负数向左。拖动时与 dy 不能同时为 0。 |
| `dy` | float | `0` | 相对起点的垂直位移，正数向下、负数向上。 |
| `task` | str | `'drag'` | 轨迹任务：drag、move/hover、click/approach_click。 |
| `source` | str \| None | `None` | 明确的数据来源条件：user_mousedata、bogazici、sapimouse；须存在对应训练任务。 |
| `duration_s` | float \| None | `None` | 运动总时长（秒）。None 由模型预测；显式值为 (0,30]，不含推理和按键前后等待。 |
| `seed` | int \| None | `None` | 随机种子；None 每次采样。相同模型、参数、种子可复现计划，不保证浏览器派发时序相同。 |
| `allow_extrapolation` | bool | `False` | 允许距离/方向超出已观察范围；True 不代表范围外质量已验证。 |
| `n_points` | int \| None | `None` | 输出点数，显式整数 2–4096；None 按预测典型间隔选择 8–2049 个点。 |


### 返回值

返回 [TrajectoryPrediction](TrajectoryPrediction.md)，trajectory 是相对坐标。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
prediction = model.generate(136, task="drag", source="user_mousedata", seed=42)
print(prediction.trajectory[-1], prediction.duration_s)
```

### 注意事项

这是低层生成器，默认 drag 固定使用 user_mousedata，默认不会像 TrajectoryModel 一样自动选来源。

[更多示例和完整业务规则](../mouse.md)

## MultitaskMouseModel.generate_single_trajectory

将低层 generate 的结果转为兼容字典。

```python signature
generate_single_trajectory(end_x, **kwargs)
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
| `allow_extrapolation`（展开） | bool | `False` | 允许距离/方向超出已观察范围；True 不代表范围外质量已验证。 不传时 TrajectoryModel 沿用实例配置，低层模型默认 False；这里不要传 None。 |
| `n_points`（展开） | int \| None | `None` | 输出点数，显式整数 2–4096；None 按预测典型间隔选择 8–2049 个点。 |


### 返回值

返回 [相对轨迹字典](../result-structures.md#相对轨迹字典)。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
data = model.generate_single_trajectory(136, seed=42)
print(data["trajectory"][-1])
```

### 注意事项

这是低层生成器，默认 drag 固定使用 user_mousedata，默认不会像 TrajectoryModel 一样自动选来源。

[更多示例和完整业务规则](../mouse.md)

## MultitaskMouseModel.model_id

当前低层模型标识字符串。

**只读属性；异步程序也直接读取，不加 await。**

```python
print(model.model_id)
```

## MultitaskMouseModel.sample_click_hold

按明确来源条件采样左右键按住时长。

```python signature
sample_click_hold(*, button='left', source='bogazici', seed=None)
```

**同步计算/工厂方法；异步程序中也不加 await。**

### 参数

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `button` | str | `'left'` | 仅 left / right；其他值抛 ValueError。 |
| `source` | str \| None | `'bogazici'` | 明确的数据来源条件：user_mousedata、bogazici、sapimouse；须存在对应训练任务。 |
| `seed` | int \| None | `None` | 随机种子；None 每次采样。相同模型、参数、种子可复现计划，不保证浏览器派发时序相同。 |


### 返回值

返回 [点击时长字典](../result-structures.md#点击时长字典)。

### 示例

以下为同步调用片段，沿用本页准备的对象。

```python
hold = model.sample_click_hold(button="right", source="bogazici", seed=42)
print(hold["hold_ms"])
```

### 注意事项

这是低层生成器，默认 drag 固定使用 user_mousedata，默认不会像 TrajectoryModel 一样自动选来源。

[更多示例和完整业务规则](../mouse.md)
