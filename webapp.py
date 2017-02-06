from flask import Flask, render_template

app = Flask("salladr")

visits = 0

@app.route("/")
def home():
	global visits
	visits += 1
	return render_template("index.html", visits = visits,
		username = "Simon")



@app.route("/about/")
def about():
	return render_template("about.html")


if __name__ == "__main__":
	app.run(debug=True)
