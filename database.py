import os
from peewee import PostgresqlDatabase, Model, CharField
from playhouse.db_url import connect

DATABASE_URL = os.environ.get("postgres://ujbaykmdqeqpux:bcc0efd6ab9b799a34d100d512f4d67a667d7ad7c73015544e34d3cf02bcc592@ec2-79-125-13-42.eu-west-1.compute.amazonaws.com:5432/dep90au2ofgb0")
if DATABASE_URL:
	db = connect(DATABASE_URL)
else:
	DATABASE = "Salladr"
	db = PostgresqlDatabase(DATABASE, threadlocals=True)

class BaseModel(Model):
	class Meta:
		database = db

class Contact(BaseModel):
	email = CharField()
	message = CharField()

