# TrajectoryPrediction

[SDK API 目录](../api-reference.md) · [使用章节](../mouse.md)

## 导入与准备

```python
from ysbrowser_sdk.motion import TrajectoryPrediction
```

结果对象通常由 SDK 返回。下面的构造字段也可用于理解返回对象的结构。

## 构造参数

```python signature
TrajectoryPrediction(trajectory: list, model_id: str, task: str, source: str, duration_s: float, predicted_cadence_s: float, warnings: list, attempts: int, engine: str = 'conditional_flow_matching_transformer') -> None
```

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `trajectory` | list | `必填` | 相对起点的 [x,y,累计秒数] 列表。 |
| `model_id` | str | `必填` | 模型标识。 |
| `task` | str | `必填` | 实际生成任务。 |
| `source` | str | `必填` | 实际数据来源条件；不是引擎名。 |
| `duration_s` | float | `必填` | 返回轨迹的总秒数。 |
| `predicted_cadence_s` | float | `必填` | 预测的典型采样间隔（秒）。 |
| `warnings` | list | `必填` | 生成提示字符串列表。 |
| `attempts` | int | `必填` | 采样次数。 |
| `engine` | str | `'conditional_flow_matching_transformer'` | conditional_flow_matching_transformer；零位移普通移动为 stationary。 |


## 字段与返回结构

直接用 `对象.字段` 读取；需要普通字典时用 `dataclasses.asdict(对象)`，或使用本类型提供的 to_dict。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `trajectory` | list | 相对起点的 [x,y,累计秒数] 列表。 |
| `model_id` | str | 模型标识。 |
| `task` | str | 实际生成任务。 |
| `source` | str | 实际数据来源条件；不是引擎名。 |
| `duration_s` | float | 返回轨迹的总秒数。 |
| `predicted_cadence_s` | float | 预测的典型采样间隔（秒）。 |
| `warnings` | list | 生成提示字符串列表。 |
| `attempts` | int | 采样次数。 |
| `engine` | str | conditional_flow_matching_transformer；零位移普通移动为 stationary。 |
