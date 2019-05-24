from app import app
from flask import render_template,request,redirect,jsonify,make_response
from flask import request, redirect
from werkzeug.utils import secure_filename
import os

@app.route("/")
def index():
	return render_template("public/index.html")

@app.route("/json_check", methods=["POST"])
def json_check():
    if request.is_json:
        req = request.get_json()
        response = {
        	"message": "JSON received !",
        	"name": req.get("name")
        }
        res=make_response(jsonify(response),200)
        app.logger.info('200')
    else:
    	res=make_response(jsonify({'message':'No Json received'}),400)
    	app.logger.info('400')
    return res

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
app.config["FILE_UPLOADS"] = "/static/img/"
app.config["ALLOWED_FILE_EXTENSIONS"] = ["JPEG", "JPG", "PNG", "GIF"]
app.config["MAX_FILE_FILESIZE"] = 0.5 * 1024 * 100000000024

def allowed_file(filename):
    if not "." in filename:
        return False
    ext = filename.rsplit(".", 1)[1]
    if ext.upper() in app.config["allowed_file_EXTENSIONS"]:
        return True
    else:
        return False

def allowed_file_filesize(filesize):
    if int(filesize) <= app.config["MAX_IMAGE_FILESIZE"]:
        return True
    else:
        return False

@app.route("/upload_file", methods=["GET", "POST"])
def upload_file():
    if request.method == "POST":
        if request.files:
            if "filesize" in request.cookies:
                if not allowed_file_filesize(request.cookies["filesize"]):
                    app.logger.info("Filesize exceeded maximum limit")
                    return redirect(request.url)
                file = request.files["file"]
                if allowed_file(file.filename):
                    filename = secure_filename(file.filename)
                    file.save(os.path.join(app.config["IMAGE_UPLOADS"], filename))
                    app.logger.info("Image saved")
                    return redirect(request.url)
                else:
                    app.logger.info("That file extension is not allowed")
                    return redirect(request.url)

    return render_template("public/upload_file.html")