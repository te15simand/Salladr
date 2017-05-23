import os
from peewee import PostgresqlDatabase, Model, CharField, BooleanField, ForeignKeyField
from playhouse.db_url import connect
from flask_security import UserMixin, RoleMixin

DATABASE_URL = os.environ.get("DATABASE_URL")
if DATABASE_URL:
	db = connect(DATABASE_URL)
else:
	DATABASE = "salladr"
	db = PostgresqlDatabase(DATABASE, threadlocals=True)

class BaseModel(Model):
	class Meta:
		database = db

class Contact(BaseModel):
	email = CharField()
	message = CharField()

class User(BaseModel, UserMixin):
	email = CharField(unique=True)
	password = CharField()
	active = BooleanField(default=True)

class Role(BaseModel, RoleMixin):
	name = CharField(unique=True)
	description = CharField(null=True)

class UserRoles(BaseModel):
	user = ForeignKeyField(User, related_name="roles")
	role = ForeignKeyField(User, related_name="users")
	name = property(lambda self: self.role.name)
	description = property(lambda self: self.role.description)

