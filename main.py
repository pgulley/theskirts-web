from flask import Flask, current_app, send_from_directory, render_template_string, Response
import random
app = Flask(__name__)

print("this is running")

print(app)

@app.route('/')
def hello_world():
    return current_app.send_static_file('home.html')

@app.route("/hootenanny")
def hoot():
	return current_app.send_static_file("hootenanny.html")

@app.route("/util/<path:filename>")
def serve_util(filename):
	return send_from_directory('static/', filename)

@app.route("/image/<path:filename>")
def serve_image(filename):
	return send_from_directory('images/', filename)

@app.route("/happy_smash_day")
def spash_day():
	return current_app.send_static_file("hause.html")

@app.route("/happy-smash-day")
def smash_day():
	return current_app.send_static_file("hause.html")

#randomly generates num_doods css classes to display the doodl background wallpaper. 
@app.route("/doodl.css")
def serve_doodl():
	num_doods = 40
	#dictionary contains image location and rendering constraints- like aspect ratio and rotation range
	imgs = [{"url":"Su1", "ratio":0.8632, "rot":25},
			{"url":"Su2", "ratio":0.7013, "rot":25}, 
			{"url":"Su3", "ratio":0.6587, "rot":25}, 
			{"url":"Su4", "ratio":0.9099, "rot":25},
			{"url":"Su5", "ratio":0.9162, "rot":25},
			{"url":"Pa1", "ratio":0.9977, "rot":90},
			{"url":"Pa2", "ratio":0.5214, "rot":45},
			{"url":"Pa3", "ratio":0.5214, "rot":25},
			{"url":"Pa4", "ratio":0.8866, "rot":180},
			{"url":"Ji1", "ratio":0.9790, "rot":25},
			{"url":"Ji2", "ratio":0.9790, "rot":90},
			{"url":"Ji3", "ratio":0.4820, "rot":180},
			{"url":"Jo1", "ratio":0.7863, "rot":180},
			{"url":"Jo2", "ratio":1.2310, "rot":45},
			{"url":"Jo3", "ratio":1.0000, "rot":100},
			{"url":"Jo4", "ratio":1.0212, "rot":100},
			{"url":"Jo5", "ratio":0.8060, "rot":45}
			]
	colors = ["#fd9ac8", "purple", "#8cce90","#94b4bb","#E880F7", "#82a4c7"]
	# color distribution should be harmonized with page colors, and generally desaturated. 

	doodls = []
	for i in range(num_doods):
		if random.randint(0,30) < 29:
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