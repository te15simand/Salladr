from peewee import PostgresqlDatabase, Model, CharField

DATABASE = "Salladr"

db = PostgresqlDatabase(DATABASE, threadlocals=True)

class BaseModel(Model):
	class Meta:
		database = db

class Contact(BaseModel):
	email = CharField()
	message = CharField()

