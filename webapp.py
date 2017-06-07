from flask import Flask, render_template, request, make_response, session, redirect, url_for
from flask_security import Security, PeeweeUserDatastore, login_required
from forms import MyForm, RegisterForm
from database import db, User, Role, UserRoles, Contact
import os

app = Flask("salladr")
app.config["SECRET_KEY"] = os.environ.get("SECRET_KEY", "insecure dev key")
app.config["SECURITY_USER_IDENTITY_ATTRIBUTES"] = "email"
app.config["SECURITY_PASSWORD_HASH"] = "pbkdf2_sha512"
app.config["SECURITY_PASSWORD_SALT"] = app.config["SECRET_KEY"]

user_datastore = PeeweeUserDatastore(db, User, Role, UserRoles)
security = Security(app, user_datastore)




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




@app.route("/")
@login_required
def home():
	return render_template("index.html")

@app.route("/profile/")
@login_required
def profile():
	user = User.email
	return render_template("profile.html", user=user)

@app.route("/contact/", methods=["GET", "POST"])
@login_required
def contact():
	form = MyForm()
	if form.validate_on_submit():

		return "Hey there, {}".format(form.name.data)
	else:
		return render_template("contact.html", form=form)



if __name__ == "__main__":
	app.run("0.0.0.0", debug=True)
