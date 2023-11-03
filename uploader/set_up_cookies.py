import zipfile
import os


def get_main_dir():

    """Get main directory"""

    base_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(base_dir)
    return parent_dir


def unzip_cookies(file):

    """Unzip cookies archive"""

    main_dir = get_main_dir()
    extracted_dir = f'{main_dir}\\uploader\\cookies_tik_tok'
    with zipfile.ZipFile(file, 'r') as zip_ref:
        zip_ref.extractall(extracted_dir)

    print(f"Unzipped zip to {extracted_dir}")


def get_cookies():

    """Get all cookies files"""

    main_dir = get_main_dir()
    extracted_dir = f'{main_dir}\\uploader\\cookies_tik_tok'
    files = os.listdir(extracted_dir)
    txt_files = [file for file in files if file.endswith('.txt')]
    return txt_files


if __name__ == '__main__':
    res = get_cookies()
    print(res)
