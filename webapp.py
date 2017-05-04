from flask import Flask, render_template, request, make_response, session
from forms import MyForm
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

@app.route("/track/session")
def track_session():
	visits = int(session.get("number_of_visits", 0))
	visits += 1
	session["number_of_visits"] = visits
	text = "Welcome! This is visit number: {}".format(visits)
	return text

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
		return render_template("contact.html", form=form)



if __name__ == "__main__":
	app.run("0.0.0.0", debug=True)
