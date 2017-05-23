from flask_wtf import FlaskForm
from wtforms import StringField, validators, TextAreaField, PasswordField


class MyForm(FlaskForm):
	"""docstring for MyForms"""
	name = StringField("Your name", [validators.InputRequired()])
	message = TextAreaField("Messages")

class Password(FlaskForm):
	password = PasswordField("Password", [validators.InputRequired()])


class Register():
	pass