from flask import Flask, render_template, request
import os
from uploader import apps

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'  # Directory to store uploaded files
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def get_videos_dir():
    base_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(base_dir)
    files_dir = os.path.join(base_dir, 'uploads')
    print(files_dir)
    return files_dir


@app.route('/')
def index():
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"

    file = request.files['file']
    if file.filename == '':
        return "No selected file"

    if file:
        filename = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filename)
        video_dir = get_videos_dir()
        try:
            mp4_files = [os.path.join(video_dir, f) for f in os.listdir(video_dir) if f.endswith('.mp4')]
            print(mp4_files[0])
            # apps.login(mp4_files[0])
        except Exception as e:
            print(e)
        return f"File '{file.filename}' uploaded successfully!"


if __name__ == '__main__':
    app.run(debug=True)
