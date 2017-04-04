from flask_wtf import FlaskForm
from wtforms import StringField, validators, TextAreaField

class MyForm(FlaskForm):
	"""docstring for MyForms"""
	name = StringField("Your name", [validators.InputRequired()])
	message = TextAreaField("Messages")