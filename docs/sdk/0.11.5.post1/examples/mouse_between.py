"""Visible local example: explicit A to B, relative movement, and element click."""
import argparse
import asyncio
from ysbrowser_sdk.sync_api import YSBrowser
from ysbrowser_sdk.async_api import YSBrowser as AsyncBrowser

HTML = """<body style="margin:0"><button style="position:absolute;left:700px;top:300px;width:100px;height:50px" onclick="this.textContent='已点击'">目标</button></body>"""

def run_sync(executable):
    with YSBrowser(executable, headless=False, context_gpu=False) as browser:
        context = browser.new_context()
        page = context.new_page()
        page.set_viewport_size({"width": 1100, "height": 750})
        page.set_content(HTML)
        mouse = context.mouse(page)
        result = mouse.move_between(100, 200, 500, 300)
        print(result.plan.source, result.plan.data_source, result.elapsed_s)
        mouse.move_by(100, 50)
        mouse.click_element(page.get_by_role("button", name="目标"))
        page.wait_for_timeout(3000)

async def run_async(executable):
    async with AsyncBrowser(executable, headless=False, context_gpu=False) as browser:
        context = await browser.new_context()
        page = await context.new_page()
        await page.set_viewport_size({"width": 1100, "height": 750})
        await page.set_content(HTML)
        mouse = context.mouse(page)
        result = await mouse.move_between(100, 200, 500, 300)
        print(result.plan.source, result.plan.data_source, result.elapsed_s)
        await mouse.move_by(100, 50)
        await mouse.click_element(page.get_by_role("button", name="目标"))
        await page.wait_for_timeout(3000)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--executable', default=None)
    parser.add_argument('--async', dest='async_mode', action='store_true')
    args = parser.parse_args()
    if args.async_mode:
        asyncio.run(run_async(args.executable))
    else:
        run_sync(args.executable)
