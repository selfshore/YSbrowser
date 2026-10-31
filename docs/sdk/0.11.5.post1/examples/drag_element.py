"""Local visible slider demo. Run with --distance 250, optionally --async."""
import argparse
import asyncio
from dataclasses import asdict
import json
from ysbrowser_sdk.sync_api import YSBrowser
from ysbrowser_sdk.async_api import YSBrowser as AsyncBrowser

HTML = """<!doctype html><meta charset="utf-8"><style>body{font:18px system-ui;margin:32px;background:#f2f6fc}#handle{position:absolute;left:100px;top:220px;width:36px;height:36px;background:#2563eb;border-radius:8px;cursor:grab}#track{position:absolute;left:100px;top:232px;width:700px;height:12px;background:#cbd5e1}</style><h1>本地拖动示例</h1><p>鼠标按下后，手柄跟随指针移动。</p><div id="track"></div><div id="handle" role="slider" aria-label="测试滑块" aria-valuenow="0"></div><script>const h=document.querySelector('#handle');let held=false,ox=0,oy=0;h.onpointerdown=e=>{held=true;ox=e.clientX-h.offsetLeft;oy=e.clientY-h.offsetTop;h.setPointerCapture(e.pointerId)};h.onpointermove=e=>{if(held){h.style.left=(e.clientX-ox)+'px';h.style.top=(e.clientY-oy)+'px';h.setAttribute('aria-valuenow',String(e.clientX-ox-100))}};h.onpointerup=()=>held=false;</script>"""

def report(result, before, after):
    print('模型:',result.plan.model_id,'来源:',result.plan.data_source)
    print('派发:',result.dispatched_points,'跳点:',result.skipped_points)
    print('元素实际 dx:',after['x']-before['x'])
    print(json.dumps(asdict(result),ensure_ascii=False,indent=2))

def run_sync(args):
    with YSBrowser(args.executable,headless=False,context_gpu=False) as browser:
        context=browser.new_context();page=context.new_page()
        page.set_viewport_size({'width':1100,'height':750});page.set_content(HTML)
        slider=page.get_by_role('slider',name='测试滑块')
        before=slider.bounding_box()
        mouse=context.mouse(page)
        result=mouse.drag_element(slider,dx=args.distance,start_offset=(12,12),seed=42)
        after=slider.bounding_box()
        assert before is not None and after is not None
        assert abs(after['x']-before['x']-args.distance)<1
        report(result,before,after)
        page.wait_for_timeout(args.keep_open*1000)

async def run_async(args):
    async with AsyncBrowser(args.executable,headless=False,context_gpu=False) as browser:
        context=await browser.new_context();page=await context.new_page()
        await page.set_viewport_size({'width':1100,'height':750});await page.set_content(HTML)
        slider=page.get_by_role('slider',name='测试滑块')
        before=await slider.bounding_box()
        mouse=context.mouse(page)
        result=await mouse.drag_element(slider,dx=args.distance,start_offset=(12,12),seed=42)
        after=await slider.bounding_box()
        assert before is not None and after is not None
        assert abs(after['x']-before['x']-args.distance)<1
        report(result,before,after)
        await page.wait_for_timeout(args.keep_open*1000)

if __name__=='__main__':
    parser=argparse.ArgumentParser()
    parser.add_argument('--executable',default=None)
    parser.add_argument('--distance',type=float,default=250)
    parser.add_argument('--keep-open',type=float,default=3)
    parser.add_argument('--async',dest='async_mode',action='store_true')
    args=parser.parse_args()
    if args.async_mode:asyncio.run(run_async(args))
    else:run_sync(args)
