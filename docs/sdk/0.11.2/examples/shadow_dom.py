"""Run only against a page you control; selectors are examples."""
import argparse
import asyncio

from ysbrowser_sdk import YSBrowser


async def main(executable, url):
    async with YSBrowser(executable) as browser:
        context = await browser.new_context()
        page = await context.new_page()
        await page.goto(url)
        # Ordinary locators traverse open and (in pinned Patchright) closed roots.
        await page.locator("#host").get_by_role("button", name="Submit", exact=True).click()
        # For an iframe: page.frame_locator('#frame').get_by_role(...)
        # page.evaluate('host.shadowRoot') is not a closed-root access API.


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--executable", required=True)
    parser.add_argument("--url", required=True)
    args = parser.parse_args()
    asyncio.run(main(args.executable, args.url))
