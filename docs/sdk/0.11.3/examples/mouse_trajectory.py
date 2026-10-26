"""Local visual demo. No training directory, external website or account needed."""
import argparse
import asyncio
import json
from dataclasses import asdict

from patchright.sync_api import Error as SyncError
from patchright.async_api import Error as AsyncError
from ysbrowser_sdk.sync_api import YSBrowser as SyncBrowser
from ysbrowser_sdk.async_api import YSBrowser as AsyncBrowser

HTML = '''<!doctype html><meta charset="utf-8"><title>YSbrowser trajectory demo</title>
<style>
body{margin:0;background:#101b2b;color:#e8f1fc;font:16px system-ui}
header{position:absolute;left:24px;top:16px;pointer-events:none}
h1{font-size:22px;margin:0 0 6px}p{margin:4px 0;color:#a8c1d9}
canvas{position:absolute;inset:0;pointer-events:none}
button{position:absolute;width:70px;height:70px;border:2px solid #70ebbe;
border-radius:50%;background:#1e594e;color:white;font:16px system-ui}
#stats{position:absolute;bottom:12px;left:24px;white-space:pre;font:13px monospace}
#cursor{position:absolute;width:8px;height:8px;border-radius:50%;background:#fff;
transform:translate(-50%,-50%);pointer-events:none}
</style>
<canvas width="1050" height="700"></canvas>
<header><h1>YSbrowser · Mouse trajectory</h1><p>实际浏览器 mousemove 轨迹 · 白点为事件坐标</p>
<p id="count">点击成功：0</p></header>
<button id="target">目标</button><div id="cursor"></div><div id="stats"></div>
<script>
const canvas=document.querySelector('canvas'),ctx=canvas.getContext('2d');
const data=document.documentElement.dataset;data.clicks='0';data.reset='1';let previous=null;
document.addEventListener('mousemove', e=>{
 if(data.reset==='1'){ctx.clearRect(0,0,canvas.width,canvas.height);previous=null;data.reset='0'}
 if(previous){ctx.beginPath();ctx.moveTo(...previous);ctx.lineTo(e.clientX,e.clientY);
 ctx.strokeStyle='#70ebbe';ctx.lineWidth=2;ctx.stroke()}
 previous=[e.clientX,e.clientY];
 const cursor=document.querySelector('#cursor');cursor.style.left=e.clientX+'px';cursor.style.top=e.clientY+'px';
});
document.querySelector('#target').onclick=()=>{data.clicks=String(Number(data.clicks)+1);
document.querySelector('#count').textContent='点击成功：'+data.clicks};
</script>'''

TARGETS = [(650, 350), (250, 450), (800, 150), (150, 150), (800, 550), (300, 350)]
PLACE = '''([x,y])=>{const t=document.querySelector('#target');t.style.left=(x-35)+'px';
t.style.top=(y-35)+'px';document.documentElement.dataset.reset='1'}'''
SHOW = "text=>document.querySelector('#stats').textContent=text"


def describe(result):
    stats = asdict(result)
    stats['plan'] = {k: v for k, v in stats['plan'].items() if k != 'points'}
    print(json.dumps(stats, ensure_ascii=False), flush=True)
    return (f"source: {result.plan.source}  |  model: {result.plan.model_id}\n"
            f"dispatched: {result.dispatched_points}  skipped: {result.skipped_points}  "
            f"movement: {result.elapsed_s:.3f}s  max lateness: {result.max_lateness_s*1000:.1f}ms")


def run_sync(args):
    with SyncBrowser(args.executable, headless=args.headless, context_gpu=False) as browser:
        context = browser.new_context(name='mouse-demo')
        page = context.new_page()
        page.set_viewport_size({'width': 1050, 'height': 700})
        page.set_content(HTML)
        mouse = context.mouse(page)
        mouse.synchronize(100, 150)
        for i, (x, y) in enumerate(TARGETS):
            page.evaluate(PLACE, [x, y])
            page.wait_for_timeout(350)
            result = mouse.click(x, y, target_size=(70, 70), duration_s=.65, seed=21+i)
            page.evaluate(SHOW, describe(result))
        assert page.evaluate('Number(document.documentElement.dataset.clicks)') == len(TARGETS)
        print('PASS: all targets clicked', flush=True)
        if not args.headless and args.keep_open:
            try:
                page.wait_for_timeout(args.keep_open * 1000)
            except SyncError:
                if not page.is_closed():
                    raise


async def run_async(args):
    async with AsyncBrowser(args.executable, headless=args.headless, context_gpu=False) as browser:
        context = await browser.new_context(name='mouse-demo')
        page = await context.new_page()
        await page.set_viewport_size({'width': 1050, 'height': 700})
        await page.set_content(HTML)
        mouse = context.mouse(page)
        await mouse.synchronize(100, 150)
        for i, (x, y) in enumerate(TARGETS):
            await page.evaluate(PLACE, [x, y])
            await page.wait_for_timeout(350)
            result = await mouse.click(x, y, target_size=(70, 70), duration_s=.65, seed=21+i)
            await page.evaluate(SHOW, describe(result))
        assert await page.evaluate('Number(document.documentElement.dataset.clicks)') == len(TARGETS)
        print('PASS: all targets clicked', flush=True)
        if not args.headless and args.keep_open:
            try:
                await page.wait_for_timeout(args.keep_open * 1000)
            except AsyncError:
                if not page.is_closed():
                    raise


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--executable', default=None)
    parser.add_argument('--async', dest='async_mode', action='store_true')
    parser.add_argument('--headless', action='store_true')
    parser.add_argument('--keep-open', type=float, default=60, help='Visible window retention in seconds')
    args = parser.parse_args()
    if args.async_mode:
        asyncio.run(run_async(args))
    else:
        run_sync(args)
