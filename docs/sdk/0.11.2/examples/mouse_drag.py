"""Drag a local element with learned mouse paths. Add --async for async API."""
import argparse
import asyncio

from patchright.sync_api import Error as SyncError
from patchright.async_api import Error as AsyncError
from ysbrowser_sdk.sync_api import YSBrowser as SyncBrowser
from ysbrowser_sdk.async_api import YSBrowser as AsyncBrowser

HTML='''<!doctype html><meta charset="utf-8"><title>YSbrowser element drag</title>
<style>body{margin:0;background:#111e30;color:#ebf5ff;font:18px system-ui}
h2,p{margin:24px}#box{position:absolute;left:100px;top:200px;width:80px;height:80px;
background:#2baf8b;border-radius:12px;display:grid;place-items:center;touch-action:none;user-select:none}
#status{position:absolute;left:24px;top:520px}</style>
<h2>Element drag · 模型轨迹</h2><p>按住元素 → 向右 300 / 向下 60 CSS 像素 → 松开</p>
<div id="box">拖动我</div><p id="status">等待开始…</p>
<script>
const box=document.querySelector('#box'),data=document.documentElement.dataset;
data.events='[]';data.releases='0';let origin=null;
for(const type of ['pointerdown','pointermove','pointerup'])box.addEventListener(type,e=>{
 const events=JSON.parse(data.events);events.push({type,x:e.clientX,y:e.clientY,buttons:e.buttons});
 data.events=JSON.stringify(events);
 if(type==='pointerdown'){
  origin={x:e.clientX,y:e.clientY,left:parseFloat(box.style.left||'100'),top:parseFloat(box.style.top||'200')};
  box.setPointerCapture(e.pointerId);
 }else if(type==='pointermove' && origin && (e.buttons&1)){
  box.style.left=origin.left+e.clientX-origin.x+'px';box.style.top=origin.top+e.clientY-origin.y+'px';
 }else if(type==='pointerup'){
  origin=null;data.releases=String(Number(data.releases)+1);
  document.querySelector('#status').textContent='已松开，元素位置：'+box.style.left+', '+box.style.top;
 }
});
</script>'''


def check_events(events):
    down=next(i for i,e in enumerate(events) if e['type']=='pointerdown')
    up=next(i for i,e in enumerate(events) if e['type']=='pointerup')
    moves=[e for e in events[down+1:up] if e['type']=='pointermove']
    assert moves and all(e['buttons']==1 for e in moves)
    assert events[up]['buttons']==0
    assert abs(events[up]['x']-events[down]['x']-300)<=1
    assert abs(events[up]['y']-events[down]['y']-60)<=1


def run_sync(args):
    with SyncBrowser(args.executable,headless=args.headless,context_gpu=False) as browser:
        context=browser.new_context();page=context.new_page()
        page.set_viewport_size({'width':1100,'height':750});page.set_content(HTML)
        mouse=context.mouse(page)
        result=mouse.drag_element('#box',dx=300,dy=60,duration_s=.8,seed=21)
        check_events(page.evaluate('JSON.parse(document.documentElement.dataset.events)'))
        box=page.locator('#box').bounding_box()
        assert abs(box['x']-400)<=1 and abs(box['y']-260)<=1
        print('PASS:',result.plan.source,mouse.position,flush=True)
        if not args.headless:
            try:page.wait_for_timeout(args.keep_open*1000)
            except SyncError:
                if not page.is_closed():raise


async def run_async(args):
    async with AsyncBrowser(args.executable,headless=args.headless,context_gpu=False) as browser:
        context=await browser.new_context();page=await context.new_page()
        await page.set_viewport_size({'width':1100,'height':750});await page.set_content(HTML)
        mouse=context.mouse(page)
        result=await mouse.drag_element(page.locator('#box'),dx=300,dy=60,duration_s=.8,seed=21)
        check_events(await page.evaluate('JSON.parse(document.documentElement.dataset.events)'))
        box=await page.locator('#box').bounding_box()
        assert abs(box['x']-400)<=1 and abs(box['y']-260)<=1
        print('PASS:',result.plan.source,mouse.position,flush=True)
        if not args.headless:
            try:await page.wait_for_timeout(args.keep_open*1000)
            except AsyncError:
                if not page.is_closed():raise


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--executable',default=None)
    parser.add_argument('--headless',action='store_true')
    parser.add_argument('--async',dest='async_mode',action='store_true')
    parser.add_argument('--keep-open',type=float,default=60)
    args=parser.parse_args()
    if args.async_mode:asyncio.run(run_async(args))
    else:run_sync(args)
