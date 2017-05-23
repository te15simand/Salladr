from database import db, Contact, User, Role, UserRoles


db.connect()
db.create_tables([Contact, User, Role, UserRoles], safe=True)

