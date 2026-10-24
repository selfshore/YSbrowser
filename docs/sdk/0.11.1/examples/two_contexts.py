"""python examples/two_contexts.py --executable ./browser/chrome.exe"""
import argparse
import asyncio

from ysbrowser_sdk import Direct, FingerprintProfile, ProxyConfig, YSBrowser


async def main(executable: str, hold_seconds: int):
    import os
    # Optional proxy credentials come from environment variables, never commit them.
    proxy = ProxyConfig(os.environ["YS_PROXY_SERVER"], username=os.getenv("YS_PROXY_USER"),
                        password=os.getenv("YS_PROXY_PASSWORD")) if os.getenv("YS_PROXY_SERVER") else Direct()
    async with YSBrowser(executable) as browser:
        a = await browser.new_context(name="a", fingerprint=FingerprintProfile(fpseed="example-a", server_gpu_profile="rtx3060"), proxy=proxy)
        b = await browser.new_context(name="b", fingerprint=FingerprintProfile(fpseed="example-b", server_gpu_profile="rtx4070super"), proxy=Direct())
        page_a, page_b = await asyncio.gather(a.new_page(), b.new_page())
        await asyncio.gather(page_a.goto("https://www.baidu.com/"), page_b.goto("https://www.ip138.com/"))
        print("A:", a.context_id, (await a.proxy_status()).to_dict())
        print("B:", b.context_id, (await b.proxy_status()).to_dict())
        await asyncio.sleep(hold_seconds)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--executable", required=True)
    parser.add_argument("--hold-seconds", type=int, default=600)
    args = parser.parse_args()
    asyncio.run(main(args.executable, args.hold_seconds))
