import os

from flask import Flask, request, render_template, send_from_directory

__author__ = 'denghaowen'

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def index():
    return render_template('upload.html')


@app.route('/upload', methods=['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'files/')
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)
    else:
        print("Couldn't create upload directory: {}",format(target))
    print(request.files.getlist("file"))
    for upload in request.files.getlist('file'):
        print(upload)
        print('{} is the file name'.format(upload.filename))
        filename = upload.filename
        destination = '/'.join([target, filename])
        print('Accept incoming file:', filename)
        print('Save it to:', destination)
        upload.save(destination)

    # return send_from_directory('files', filename, as_attachment=True)
    return render_template('complete.html', file_name=filename)


@app.route('/upload/<filename>')
def send_file(filename):
    return send_from_directory('files', filename)


@app.route('/gallery')
def get_gallery():
    file_names = os.listdir('./files')
    print(file_names)
    return render_template('gallery.html', file_names=file_names)


if __name__ == '__main__':
    app.run(port=5000, debug=True)