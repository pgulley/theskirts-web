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
    
	num_doods = 10
	urls = ["/image/Su2.png", "/image/Su1.png", "/image/Su3.png", "/image/Su4.png"]
	colors = ["pink", "purple", "#8cce90"]
	#eventually also generate random positions, sizes, and rotations
	# maybe with some kinda perlin noise thing, so they don't stack on top of each other all ugly. 
	# also certain doodls should probably have direction biases- don't want to generate flowers upsidedown. probably. 

	# color distribution should be harmonized with page colors- with a slightly biased chance of a saturation outlier. 

	doodls = [{
				"id":i, 
				"url":random.choice(urls), 
				"color": random.choice(colors),
				"size":str(random.randint(80,200))} 
			for i in range(num_doods)]

	print doodls 
	with open("templates/doodl.css") as css:
		template = css.read()


	doodl_out = render_template_string(template, doodls = doodls)


	return Response(doodl_out, mimetype="text/css")



