"""Local, account-free demonstration of Context options and diagnostic bundles."""
import argparse
import asyncio
from pathlib import Path

from ysbrowser_sdk.sync_api import YSBrowser as SyncBrowser, ContextOptions
from ysbrowser_sdk.async_api import YSBrowser as AsyncBrowser

HTML='''<!doctype html><meta charset="utf-8"><title>SDK diagnostics demo</title>
<body style="background:#152337;color:#edf5ff;font:20px system-ui;padding:40px">
<h1>YSbrowser SDK 0.10.0</h1><p>Context options · screenshot · page events · trace</p>
<button onclick="console.log('Demo button clicked')">Test button</button></body>'''


def options(output):
    return ContextOptions(viewport={'width':1000,'height':700},
        record_har_path=output/'network.har',default_timeout_ms=5000,navigation_timeout_ms=15000)


def run_sync(args):
    output=args.output.resolve();output.mkdir(parents=True,exist_ok=True)
    with SyncBrowser(args.executable,headless=not args.headed,context_gpu=False) as browser:
        context=browser.new_context(options=options(output))
        context.start_diagnostics(trace=True,include_messages=True)
        page=context.new_page();page.set_content(HTML)
        page.get_by_role('button').click()
        page.evaluate("setTimeout(()=>{throw new Error('Intentional demo error')},0)",isolated_context=False)
        page.wait_for_timeout(100)
        result=context.capture_diagnostics(output,page=page)
        context.stop_diagnostics()
        print('Diagnostic report:',result['report_path'])
        print('Screenshot:',Path(result['directory'])/result['pages'][0]['screenshot'])
        print('Trace:',Path(result['directory'])/result['trace'])
        assert any(e['kind']=='page_error' for e in result['page_events'])
        if args.headed:page.wait_for_timeout(10000)


async def run_async(args):
    output=args.output.resolve();output.mkdir(parents=True,exist_ok=True)
    async with AsyncBrowser(args.executable,headless=not args.headed,context_gpu=False) as browser:
        context=await browser.new_context(options=options(output))
        await context.start_diagnostics(trace=True,include_messages=True)
        page=await context.new_page();await page.set_content(HTML)
        await page.get_by_role('button').click()
        await page.evaluate("setTimeout(()=>{throw new Error('Intentional demo error')},0)",isolated_context=False)
        await page.wait_for_timeout(100)
        result=await context.capture_diagnostics(output,page=page)
        await context.stop_diagnostics()
        print('Diagnostic report:',result['report_path'])
        print('Screenshot:',Path(result['directory'])/result['pages'][0]['screenshot'])
        print('Trace:',Path(result['directory'])/result['trace'])
        assert any(e['kind']=='page_error' for e in result['page_events'])
        if args.headed:await page.wait_for_timeout(10000)


if __name__=='__main__':
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--executable',default=None)
    parser.add_argument('--output',type=Path,required=True)
    parser.add_argument('--async',dest='async_mode',action='store_true')
    parser.add_argument('--headed',action='store_true')
    args=parser.parse_args()
    if args.async_mode:asyncio.run(run_async(args))
    else:run_sync(args)
