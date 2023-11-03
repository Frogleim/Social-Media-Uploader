from flask import Flask, render_template, request
import os
from uploader import instagram_uploader, tik_tok_uploader, set_up_cookies
import shutil

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'  # Directory to store uploaded files
COOKIES_UPLOAD_FOLDER = 'uploads'  # Directory to store uploaded files

app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def get_main_dir():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(base_dir)
    return parent_dir


def get_uploads_dir():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    files_dir = os.path.join(base_dir, 'uploads')
    return files_dir


def get_accounts_dir():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    files_dir = os.path.join(base_dir, 'uploader\\instagram_accounts')
    return files_dir


@app.route('/instagram')
def index():
    return render_template('upload.html')


@app.route('/tiktok')
def tiktok():
    return render_template('tiktok.html')


@app.route('/upload', methods=['POST'])
def instagram_upload_file():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    caption = request.form['caption']  # Get the caption from the form data

    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        video_dir = get_uploads_dir()
        try:
            mp4_files = [os.path.join(video_dir, f) for f in os.listdir(video_dir) if f.endswith('.mp4')]
            print(mp4_files[0])
            instagram_uploader.login(mp4_files[0], caption)  # Pass the caption to your login method
        except Exception as e:
            print(e)
        return f"File '{file.filename}' uploaded successfully with caption: {caption}!"


@app.route('/tiktok_upload', methods=['POST'])
def tiktok_upload_file():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    caption = request.form['caption']  # Get the caption from the form data

    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        video_dir = get_uploads_dir()
        try:
            mp4_files = [os.path.join(video_dir, f) for f in os.listdir(video_dir) if f.endswith('.mp4')]
            print(mp4_files[0])
            tik_tok_uploader.tiktok_uploader(mp4_files[0], caption)
        except Exception as e:
            print(e)
        return f"File '{file.filename}' uploaded successfully with caption: {caption}!"


@app.route('/unzip_cookies', methods=['POST'])
def unzip_upload_file():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        zip_dir = get_uploads_dir()
        try:
            zip_files = [os.path.join(zip_dir, f) for f in os.listdir(zip_dir) if f.endswith('.zip')]
            set_up_cookies.unzip_cookies(zip_files[0])
        except Exception as e:
            print(e)
        return render_template('success.html')


@app.route('/save_accounts', methods=['POST'])
def save_accounts_file():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        accounts_dir = get_accounts_dir()
        uploads_dir = get_uploads_dir()
        try:
            accounts_file = [os.path.join(uploads_dir, f) for f in os.listdir(uploads_dir) if f.endswith('.txt')]
            shutil.move(accounts_file[0], accounts_dir)
        except Exception as e:
            print(e)
        return render_template('success.html')


if __name__ == '__main__':
    app.run(debug=True)
