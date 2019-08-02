import os
from flask import Flask, render_template, request, jsonify, make_response
import werkzeug
from werkzeug.utils import secure_filename
import json
import docker
client = docker.from_env()

app = Flask(__name__, instance_relative_config=True)
app.config.from_object('config.TestingConfig')

# try:
#    from json.decoder import JSONDecodeError
# except ImportError:
#    JSONDecodeError = ValueError


@app.errorhandler(werkzeug.exceptions.BadRequest)
def handle_bad_request(e):
    return 'bad request!', 400


def index():
    return render_template("public/index.html")


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


class Models(object):
    """Models"""

    def __init__(self, model_id):
        self.model_id = model_id
        self.model_type = ['docker', 'binary', 's3']
        self.current_data_state = ''
        self.model_state = ''

    def execute(self, current_data_state, model_state):
        pass

    def get_id(self):
        return self.model_id


class Registry(object):
    """Registry"""

    def __init__(self):
        self.models_registry = ['vizml', 'vizrec', 'data2vis', 'draco']

    def get(self):
        return self.models_registry[Models(self.model_id).get_id()]


@app.route("/upload_file", methods=["POST"])
def uploadfile():
    if request.method == 'POST':
        if "filesize" in request.cookies:
            if not allowed_filesize(request.cookies["filesize"]):
                return handle_bad_request('e')
        f1 = request.files["file"]
        if allowed_file(f1.filename):
            full_filename = os.path.join(
                app.config['UPLOAD_FOLDER'],
                secure_filename(
                    f1.filename))
            # f1.save(full_filename)
            with open(full_filename) as json_file:
                json_data = json.load(json_file)
                app.config["VIZREC"].insert(json_data)
            return make_response(jsonify(f1.filename), 200)
        else:
            return handle_bad_request('e')


@app.route("/infered", methods=["POST"])
def infered(inpt):
    choices = inpt
    return make_response(jsonify(choices), 200)


@app.route("/recommender", methods=["POST"])
def recommender():
    if not request.json:
        return handle_bad_request('e')
    else:
        inference_request = []
        inference_request.append(json.dumps(request.json))
        for i in inference_request:
            try:
                a, b, c = eval(i)['model_id'], eval(
                    i)['current_data_state'], eval(i)['model_state']
                print(type(eval(i)['model_id']))
                if eval(i)['model_id'] in ['1', '2', '3', '4']:
                    d = Models(a, b, c).run(eval(i)['model_id'])
                    infered(d)
                else:
                    return handle_bad_request('e')
            except KeyError:
                return handle_bad_request('e')
        return ''.join(inference_request)
