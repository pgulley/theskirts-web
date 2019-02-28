from flask import Flask, current_app
app = Flask(__name__)


@app.route('/')
def hello_world():
    return current_app.send_static_file('home.html')

@app.route('/style.csvv')
def serve_style():
	return current_app.send_static_file('style.css')