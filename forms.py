from flask_wtf import FlaskForm
from wtforms import StringField, validators, TextAreaField, PasswordField
from wtforms.fields.html5 import EmailField


class MyForm(FlaskForm):
	"""docstring for MyForms"""
	name = StringField("Your name", [validators.InputRequired()])
	message = TextAreaField("Messages")

class LoginForm(FlaskForm):
	email = EmailField("Email", [validators.DataRequired(), validators.Email()])
	password = PasswordField("Password", [validators.InputRequired()])


class RegisterForm(FlaskForm):
	email = EmailField("Email", [validators.DataRequired(), validators.Email()])
	password = PasswordField("Password", [validators.InputRequired()])
