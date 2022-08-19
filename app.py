import os

from flask import Flask, request, render_template, send_from_directory

__author__ = 'denghaowen'

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))


@app.route('/')
def index():
    return render_template("upload.html")


@app.route('/upload', methods=['POST'])
def upload():
    folder_name = request.form['superhero']
    '''
    # this is to verify that folder to upload to exists.
    if os.path.isdir(os.path.join(APP_ROOT, 'files/{}'.format(folder_name))):
        print('folder exist')
    '''
    target = os.path.join(APP_ROOT, 'file/{}'.format(folder_name))
    print(target)
    if not os.path.isdir(target):
        os.mkdir(target)
    print(request.files.getlist('file'))
    for upload in request.files.getlist('file'):
        print(upload)
        print('{} is the file name'.format(upload.filename))
        filename = upload.filename
        # this is to verify files are supported
        ext = os.path.splitext(filename)[1]
        if ext == '.zip' or ext == '.rar':
            print('File supported moving on...')
        else:
            render_template('Error.html', message='File uploaded are not supported...')
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
