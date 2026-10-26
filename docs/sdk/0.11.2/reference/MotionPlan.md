# MotionPlan

[SDK API 目录](../api-reference.md) · [使用章节](../mouse.md)

## 导入与准备

```python
from ysbrowser_sdk.sync_api import MotionPlan
```

结果对象通常由 SDK 返回。下面的构造字段也可用于理解返回对象的结构。

## 构造参数

```python signature
MotionPlan(points: 'list[list[float]]', source: 'str', attempts: 'int', model_id: 'str', warnings: 'list[str]', data_source: 'str' = '', task: 'str' = '', predicted_cadence_s: 'float | None' = None) -> None
```

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `points` | list[list[float]] | `必填` | 绝对主 Frame 视口坐标 [x,y,累计秒数] 列表；时间从 0 起严格递增。 |
| `source` | str | `必填` | 引擎名 conditional_flow_matching_transformer；零位移普通移动为 stationary。 |
| `attempts` | int | `必填` | 有限重采样中累计的模型采样次数。 |
| `model_id` | str | `必填` | 本次使用的模型标识。 |
| `warnings` | list[str] | `必填` | 生成提示字符串列表。 |
| `data_source` | str | `''` | 实际来源条件：user_mousedata / bogazici / sapimouse。 |
| `task` | str | `''` | 实际任务：move / approach_click / drag。 |
| `predicted_cadence_s` | float \| None | `None` | 预测的典型采样间隔（秒），不是实际事件间隔。 |


## 字段与返回结构

直接用 `对象.字段` 读取；需要普通字典时用 `dataclasses.asdict(对象)`，或使用本类型提供的 to_dict。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `points` | list[list[float]] | 绝对主 Frame 视口坐标 [x,y,累计秒数] 列表；时间从 0 起严格递增。 |
| `source` | str | 引擎名 conditional_flow_matching_transformer；零位移普通移动为 stationary。 |
| `attempts` | int | 有限重采样中累计的模型采样次数。 |
| `model_id` | str | 本次使用的模型标识。 |
| `warnings` | list[str] | 生成提示字符串列表。 |
| `data_source` | str | 实际来源条件：user_mousedata / bogazici / sapimouse。 |
| `task` | str | 实际任务：move / approach_click / drag。 |
| `predicted_cadence_s` | float \| None | 预测的典型采样间隔（秒），不是实际事件间隔。 |
