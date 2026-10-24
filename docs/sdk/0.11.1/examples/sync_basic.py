"""Run: python sync_basic.py [--executable ./browser/chrome.exe] [--headless]"""
import argparse
from ysbrowser_sdk.sync_api import YSBrowser, FingerprintProfile, ContextOptions

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--executable', default=None, help='Optional relative browser path; otherwise use the installed browser')
    parser.add_argument('--headless', action='store_true')
    args = parser.parse_args()
    with YSBrowser(args.executable, headless=args.headless) as browser:
        context = browser.new_context(
            name='demo', fingerprint=FingerprintProfile(fpseed='demo'),
            options=ContextOptions(viewport={'width': 1280, 'height': 720}),
        )
        page = context.new_page()
        page.set_content('<input aria-label="name"><button onclick="this.textContent=\'done\'">save</button>')
        page.get_by_label('name').fill('Alice')
        page.get_by_role('button', name='save').click()
        print(page.get_by_role('button').inner_text())
        print(context.proxy_status().mode)

if __name__ == '__main__':
    main()
