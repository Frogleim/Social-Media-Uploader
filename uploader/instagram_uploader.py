import random
from instabot import Bot
import time
import os
import json


def get_accounts_dir():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(base_dir)
    return parent_dir


def read_accounts():
    main_dir = get_accounts_dir()
    with open(f'{main_dir}\\accounts.txt', 'r') as file:
        file_contents = file.read()
    return file_contents


def login(file, caption):
    start_time = time.time()
    accounts_list = read_accounts()
    data = accounts_list.split('\n')
    for accounts in data[4:]:
        username = accounts.split(':')[1]
        password = accounts.split(':')[0]
        print(username)
        print(password)
        try:
            bot = Bot()
            bot.login(username=username,
                      password=password, is_threaded=True)
            time.sleep(random.uniform(1.5, 2))
            bot.upload_video(file,
                             caption=caption)
        except Exception as e:
            print(f'Failed\n{e}')
        time.sleep(random.uniform(3.6, 6.958))
    end_time = time.time()
    total_time = end_time - start_time
    print(total_time)
    return total_time


if __name__ == "__main__":
    accounts = read_accounts()
    print(accounts)
