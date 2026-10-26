"""Run with --executable path/to/YSbrowser.exe; closes after --hold-seconds."""
import argparse
import time

from ysbrowser_sdk.sync_api import YSBrowser, FingerprintProfile, Direct


def main(executable, hold_seconds):
    with YSBrowser(executable) as browser:
        a = browser.new_context(name="a", fingerprint=FingerprintProfile(fpseed="example-a", server_gpu_profile="rtx3060"), proxy=Direct())
        b = browser.new_context(name="b", fingerprint=FingerprintProfile(fpseed="example-b", server_gpu_profile="rtx4070super"), proxy=Direct())
        pa, pb = a.new_page(), b.new_page()
        pa.goto("https://www.baidu.com/")
        pb.goto("https://www.ip138.com/")
        print(a.context_id, a.proxy_status().to_dict())
        print(b.context_id, b.proxy_status().to_dict())
        time.sleep(hold_seconds)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--executable", required=True)
    parser.add_argument("--hold-seconds", type=int, default=600)
    args = parser.parse_args()
    main(args.executable, args.hold_seconds)
