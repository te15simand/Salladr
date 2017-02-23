from flask import Flask, render_template, request

app = Flask("salladr")

visits = 0

@app.route("/")
def home():
	return render_template("index.html")



@app.route("/profile/")
def profile():
	return render_template("profile.html")

@app.route("/contact/")
def contact():
	return render_template("contact.html")

@app.route("/help", methods=["GET", "POST"])
def help():
	if request.method == "POST":
		page = "You are {} with email {} and your message was {}".format(
			request.form["name"],
			request.form["email"],
			request.form["message"]
		)
		return page
	else:
		return render_template("help.html")

@app.route("/math", methods=["GET", "POST"])
def math():
	if request.method == "POST":
		page = "{} + {} = {}".format(
			request.form["x"],
			request.form["y"],
			int(request.form["y"]) + int(request.form["x"])
		)
		return page
	else:
		return render_template("math.html")

if __name__ == "__main__":
	app.run("0.0.0.0", debug=True)
