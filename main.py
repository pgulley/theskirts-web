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
    
	num_doods = 20
	#dictionary contains image location and rendering constraints- like aspect ratio and rotation range
	imgs = [{"url":"Su1", "ratio":0.8632, "rot":25},
			{"url":"Su2", "ratio":0.7013, "rot":25}, 
			{"url":"Su3", "ratio":0.6587, "rot":25}, 
			{"url":"Su4", "ratio":0.9099, "rot":25},
			{"url":"Su5", "ratio":0.9162, "rot":25}]
	colors = ["pink", "purple", "#8cce90","#94b4bb","#E880F7"]
	# color distribution should be harmonized with page colors, and generally desaturated. 

	doodls = []
	for i in range(num_doods):
		if random.randint(0,20) < 19:
			img = random.choice(imgs)
			size = random.randint(30,100)
			rot = img["rot"]
			margin = random.randint(10,40)
			margin_bottom = random.randint(-40,40)
			dood = {
					"id":i, 
					"url":"/image/{}.png".format(img["url"]), 
					"color": random.choice(colors),
					"x_size":size,
					"y_size":size*img["ratio"],
					"rot": random.randint(-rot,rot), 
					"margin":margin, 
					"margin_bottom":margin_bottom
			}

		else:
			#give an empty  tile
			size = random.randint(50,150)
			dood = {
					"id":i, 
					"url": "None",
					"color": "None",
					"x_size": size,
					"y_size": size,
					"rot":0,
					"margin": 20, 
					"margin_bottom":0
			}

		doodls.append(dood)

		


	with open("templates/doodl.css") as css:
		template = css.read()


	doodl_out = render_template_string(template, doodls = doodls)


	return Response(doodl_out, mimetype="text/css")



