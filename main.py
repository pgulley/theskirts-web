from flask import Flask, current_app, send_from_directory
app = Flask(__name__)


@app.route('/')
def hello_world():
    return current_app.send_static_file('home.html')

@app.route("/util/<path:filename>")
def serve_util():
	return send_from_directory('static/', filename)

@app.route("/image/<path:filename>")
def serve_image(filename):
	return send_from_directory('images/', filename)

