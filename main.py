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
	#dictionary contains image location and rendering constraints- like aspect ratio and rotation range
	imgs = [{"url":"Su1", "ratio":0.8632, "rot":25},
			{"url":"Su2", "ratio":0.7013, "rot":25}, 
			{"url":"Su3", "ratio":0.6587, "rot":25}, 
			{"url":"Su4", "ratio":0.9099, "rot":25},
			{"url":"Su5", "ratio":0.9162, "rot":25}]
	colors = ["pink", "purple", "#8cce90","#94b4bb","#E880F7"]
	#eventually also generate random positions
	# maybe with some kinda perlin noise thing, so they don't stack on top of each other all ugly. 
	# color distribution should be harmonized with page colors- with a slightly biased chance of a saturation outlier. 
	doodls = []
	for i in range(num_doods):
		img = random.choice(imgs)
		size = random.randint(80,250)
		rot = img["rot"]
		dood = {
				"id":i, 
				"url":"/image/{}.png".format(img["url"]), 
				"color": random.choice(colors),
				"x_size":size,
				"y_size":size*img["ratio"],
				"rot": random.randint(-rot,rot)
		}
		doodls.append(dood)


	with open("templates/doodl.css") as css:
		template = css.read()


	doodl_out = render_template_string(template, doodls = doodls)


	return Response(doodl_out, mimetype="text/css")



