from app import app
from flask import render_template,request,redirect,jsonify,
from werkzeug.utils import secure_filename
import os


@app.route("/")
def index():
    return render_template("public/index.html")


APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(APP_ROOT, 'static', 'file')
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["ALLOWED_EXTENSIONS"] = ["JSON"]
app.config["MAX_CONTENT_LENGTH"] = 16 * 1024 * 100024


def allowed_file(filename):
    if "." not in filename:
        return False
    ext = filename.rsplit(".", 1)[1]
    if ext.upper() in app.config["ALLOWED_EXTENSIONS"]:
        return True
    else:
        return False


def allowed_filesize(filesize):
    if int(filesize) <= app.config["MAX_CONTENT_LENGTH"]:
        return True
    else:
        return False


@app.route("/upload_file", methods=["GET", "POST"])
def upload_file():
    if request.method == 'POST':
        if request.files:
            if "filesize" in request.cookies:
                if not allowed_filesize(request.cookies["filesize"]):
                    app.logger.info('not saved')
                    return jsonify({'message': 'Too large size,400'})
            else:
                file = request.files["file"]
                if allowed_file(file.filename):
                    full_filename = os.path.join(
                        app.config['UPLOAD_FOLDER'],
                        secure_filename(
                            file.filename))
                    file.save(full_filename)
                    app.logger.info('saved')
                    return jsonify({'message': 'Json received,200'})
                else:
                    app.logger.info('not saved')
                    return jsonify(
                        {'message': 'File extension not allowed,400'})
    return render_template("public/upload_file.html")
