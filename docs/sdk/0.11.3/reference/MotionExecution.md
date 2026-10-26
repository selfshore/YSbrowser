# MotionExecution

[SDK API 目录](../api-reference.md) · [使用章节](../mouse.md)

## 导入与准备

```python
from ysbrowser_sdk.sync_api import MotionExecution
```

结果对象通常由 SDK 返回。下面的构造字段也可用于理解返回对象的结构。

## 构造参数

```python signature
MotionExecution(plan: 'MotionPlan', dispatched_points: 'int', skipped_points: 'int', elapsed_s: 'float', max_lateness_s: 'float') -> None
```

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `plan` | MotionPlan | `必填` | MotionPlan，描述运动部分；不包含按键事件序列。 |
| `dispatched_points` | int | `必填` | 实际派发的移动点数，不计起点即时定位。 |
| `skipped_points` | int | `必填` | 因调度迟到跳过的计划点数。 |
| `elapsed_s` | float | `必填` | 运动派发耗时，不含推理、起点定位、按键等待。 |
| `max_lateness_s` | float | `必填` | 最大调度迟到秒数。 |


## 字段与返回结构

直接用 `对象.字段` 读取；需要普通字典时用 `dataclasses.asdict(对象)`，或使用本类型提供的 to_dict。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `plan` | MotionPlan | MotionPlan，描述运动部分；不包含按键事件序列。 |
| `dispatched_points` | int | 实际派发的移动点数，不计起点即时定位。 |
| `skipped_points` | int | 因调度迟到跳过的计划点数。 |
| `elapsed_s` | float | 运动派发耗时，不含推理、起点定位、按键等待。 |
| `max_lateness_s` | float | 最大调度迟到秒数。 |
