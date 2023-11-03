from tiktok_uploader.upload import upload_video, upload_videos
from tiktok_uploader.auth import AuthBackend
import os


def get_accounts_dir():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(base_dir)
    return parent_dir


def tiktok_uploader(file, caption):
    main_dir = get_accounts_dir()
    upload_video(file,
                 description=caption,
                 cookies=f'{main_dir}\\uploader\\cookies_tik_tok\\cookies_2.txt')


if __name__ == '__main__':
    res = get_accounts_dir()
    print(res)