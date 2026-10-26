"""Run: python async_basic.py [--executable ./browser/chrome.exe] [--headless]"""
import argparse
import asyncio
from ysbrowser_sdk.async_api import YSBrowser, FingerprintProfile, ContextOptions

async def run(args):
    async with YSBrowser(args.executable, headless=args.headless) as browser:
        context = await browser.new_context(
            fingerprint=FingerprintProfile(fpseed='async-demo'),
            options=ContextOptions(viewport={'width': 1280, 'height': 720}),
        )
        page = await context.new_page()
        await page.set_content('<h1>Hello</h1>')
        print(await page.locator('h1').inner_text())
        mouse = context.mouse(page)
        await mouse.synchronize(100, 100)
        result = await mouse.move(500, 300, duration_s=0.3, seed=42)
        print(result.plan.source, mouse.position)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--executable', default=None, help='Optional relative browser path; otherwise use the installed browser')
    parser.add_argument('--headless', action='store_true')
    asyncio.run(run(parser.parse_args()))

if __name__ == '__main__':
    main()
