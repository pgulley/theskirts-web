from flask import Flask, current_app, send_from_directory, render_template_string, Response
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
    return current_app.send_static_file('home.html')

@app.route("/util/<path:filename>")
def serve_util(filename):
	return send_from_directory('static/', filename)

@app.route("/image/<path:filename>")
def serve_image(filename):
	return send_from_directory('images/', filename)

@app.route("/doodl.css")
def serve_doodl():

	num_doods = 5
	urls = ["/image/Su2.png", "/image/Su1.png"]
	colors = ["pink", "purple", "#8cce90", "#a38cce"]

	doodls = [{"id":i, "url":random.choice(urls), "color": random.choice(colors)} for i in range(0,num_doods)]

	with open("templates/doodl.css") as css:
		template = css.read()


	doodl_out = render_template_string(template, doodls = doodls)


	return Response(doodl_out, mimetype="text/css")




app.run(debug=True)