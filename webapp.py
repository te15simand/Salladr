from flask import Flask, render_template, request

app = Flask("salladr")

visits = 0

@app.route("/")
def home():
	global visits
	visits += 1
	return render_template("index.html", visits = visits,
		username = "Simon")



@app.route("/profile/")
def profile():
	return render_template("profile.html")

@app.route("/help/")
def help():
	return render_template("help.html")

@app.route("/contact", methods=["GET", "POST"])
def contact():
	if request.method == "POST":
		page = "You are {} with email {} and your message was {}".format(
			request.form["name"],
			request.form["email"],
			request.form["message"]
		)
		return page
	else:
		return render_template("contact.html")


if __name__ == "__main__":
	app.run("0.0.0.0", debug=True)
