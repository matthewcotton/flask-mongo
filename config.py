from mongoengine import *

class Config():
    # Connect to MongoDB
    connect(host="mongodb+srv://flask_user:VeFWloeju0dVbhdF@cluster0.3e1h8.mongodb.net/tasksdb?retryWrites=true&w=majority")
