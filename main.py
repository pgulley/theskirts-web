from flask import Flask
app = Flask(__name__)

print("we got here")

@app.route('/')
def hello_world():
    return 'Hello, World!'