from flask import Flask, current_app, send_from_directory
app = Flask(__name__)


@app.route('/')
def hello_world():
    return current_app.send_static_file('home.html')

@app.route('/style.css')
def serve_style():
	return current_app.send_static_file('style.css')

@app.route('/favicon.ico')
def serve_fav():
	return current_app.send_static_file('favicon.jpg')

@app.route("/image/<path:filename>")
def serve_image(filename):
	return send_from_directory('static/', filename)

