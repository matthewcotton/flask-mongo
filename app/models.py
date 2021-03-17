# Define Users schema
class Users(Document):
    username = StringField(required=True)
    password = StringField(required=True)

# Define Tasks schema
class Tasks(Document):
    title = StringField(required=True)
    description = StringField(required=True)
    completed = BooleanField(required=True)
    assigned_to = ReferenceField(Users)