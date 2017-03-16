from flask import Flask, render_template, request
from forms import MyForm

app = Flask("salladr")
app.config["WTF_CSRF_ENABLED"] = False



@app.route("/")
def home():
	return render_template("index.html")

@app.route("/rem")
def rem():
	return render_template("rem.html")

@app.route("/profile/")
def profile():
	return render_template("profile.html")

@app.route("/contact/", methods=["GET", "POST"])
def contact():
	form = MyForm()
	if form.validate_on_submit():
		return "Hey there, {}".format(form.name.data)
	else:
		return render_template("help.html", form=form)



if __name__ == "__main__":
	app.run("0.0.0.0", debug=True)
