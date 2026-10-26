# MotionRequest

[SDK API 目录](../api-reference.md) · [使用章节](../mouse.md)

## 导入与准备

```python
from ysbrowser_sdk.sync_api import MotionRequest
```

结果对象通常由 SDK 返回。下面的构造字段也可用于理解返回对象的结构。

## 构造参数

```python signature
MotionRequest(start: tuple[float, float], end: tuple[float, float], action: str = 'move', duration_s: float | None = None, target_size: tuple[float, float] | None = None, seed: int | None = None) -> None
```

| 参数 | 类型 | 默认值 | 含义 / 单位 / 限制 |
| --- | --- | --- | --- |
| `start` | tuple[float, float] | `必填` | 起点绝对 CSS 坐标 (x,y)。 |
| `end` | tuple[float, float] | `必填` | 终点绝对 CSS 坐标 (x,y)。 |
| `action` | str | `'move'` | move / click / drag。 |
| `duration_s` | float \| None | `None` | 运动总时长（秒）。None 由模型预测；显式值为 (0,30]，不含推理和按键前后等待。 |
| `target_size` | tuple[float, float] \| None | `None` | 目标宽、高，均为正数；仅验证并保留兼容，本模型未学习目标尺寸条件。 |
| `seed` | int \| None | `None` | 随机种子；None 每次采样。相同模型、参数、种子可复现计划，不保证浏览器派发时序相同。 |


## 字段与返回结构

直接用 `对象.字段` 读取；需要普通字典时用 `dataclasses.asdict(对象)`，或使用本类型提供的 to_dict。

| 字段 | 类型 | 含义 |
| --- | --- | --- |
| `start` | tuple[float, float] | 起点绝对 CSS 坐标 (x,y)。 |
| `end` | tuple[float, float] | 终点绝对 CSS 坐标 (x,y)。 |
| `action` | str | move / click / drag。 |
| `duration_s` | float \| None | 运动总时长（秒）。None 由模型预测；显式值为 (0,30]，不含推理和按键前后等待。 |
| `target_size` | tuple[float, float] \| None | 目标宽、高，均为正数；仅验证并保留兼容，本模型未学习目标尺寸条件。 |
| `seed` | int \| None | 随机种子；None 每次采样。相同模型、参数、种子可复现计划，不保证浏览器派发时序相同。 |
