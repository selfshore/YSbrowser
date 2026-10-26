# 可运行示例

先在运行脚本的 Python 环境安装 SDK 0.11.2。本目录示例使用本地页面，不需要第三方站点或代理。

| 文件 | 用途 | 输出 |
| --- | --- | --- |
| [sync_basic.py](sync_basic.py) | 同步浏览器与页面基本操作 | 页面内容和代理模式 |
| [async_basic.py](async_basic.py) | 异步页面与模型移动 | 轨迹引擎和位置 |
| [mouse_between.py](mouse_between.py) | A→B、相对移动、元素点击；支持 --async | 模型与来源 |
| [drag_element.py](drag_element.py) | 本地可拖动滑块；支持 --distance 和 --async | 结果结构、实际元素位移 |
| [offline_trajectory.py](offline_trajectory.py) | 不启动浏览器生成计划 | trajectory.json |

```powershell
python .\sync_basic.py
python .\async_basic.py
python .\mouse_between.py
python .\mouse_between.py --async
python .\drag_element.py --distance 250
python .\drag_element.py --distance 136 --async
python .\offline_trajectory.py --output trajectory.json
```

浏览器示例默认显示窗口。drag_element 的 --keep-open 控制操作后保留窗口的秒数；关闭浏览器前会打印结果。执行 API 使用同一 Python 环境，不要把同步 Page 交给异步鼠标。
