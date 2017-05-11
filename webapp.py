from flask import Flask, render_template, request, make_response, session, redirect, url_for
from forms import MyForm, Password
from database import db
import os

app = Flask("salladr")
app.config["WTF_CSRF_ENABLED"] = False
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "insecure dev key")

@app.before_request
def before_requrst():
	db.connect()

@app.after_request
def after_request(response):
	db.close()
	return response


@app.route("/track/cookie") 
def track_cookie():
	visits = int(request.cookies.get("number_of_visits", 0))
	if visits == 0:
		text = "Welcome! This is your first visit!"
		visits += 1
	elif visits >= 1:
		visits += 1
		text = "Welcome back!"

	resp = make_response(text)
	resp.set_cookie("number_of_visits", str(visits))
	return resp

@app.route("/login", methods=["GET", "POST"])
def log_in():
	form = Password()
	if form.validate_on_submit():

		if form.data["password"] == "sallad":
			print("XD")
			session["logged_in"] = True
			return redirect(url_for("rem"))
		else:
			print(form.data["password"])
			return render_template("login.html", form=form)
	else:
		return render_template("login.html", form=form)

	


@app.route("/")
def home():
	return render_template("index.html")




@app.route("/rem")
def rem():
	logged_in = int(session.get("logged_in", 0))
	if logged_in:
		return render_template("rem.html")
	else:
		return redirect(url_for("log_in"))

@app.route("/profile/")
def profile():
	return render_template("profile.html")

@app.route("/contact/", methods=["GET", "POST"])
def contact():
	form = MyForm()
	if form.validate_on_submit():
		return "Hey there, {}".format(form.name.data)
	else:
		return render_template("contact.html", form=form)



if __name__ == "__main__":
	app.run("0.0.0.0", debug=True)
