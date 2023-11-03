from tiktok_uploader.upload import upload_video, upload_videos
from tiktok_uploader.auth import AuthBackend
import os
from . import set_up_cookies


def get_accounts_dir():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(base_dir)
    return parent_dir


def tiktok_uploader(file, caption):
    cookies_file = set_up_cookies.get_cookies()
    main_dir = get_accounts_dir()
    for txt_file in cookies_file:
        upload_video(file,
                     description=caption,
                     cookies=f'{main_dir}\\uploader\\cookies_tik_tok\\{txt_file}')


if __name__ == '__main__':
    res = get_accounts_dir()
    print(res)