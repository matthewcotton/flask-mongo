# from os import path
# from mongoengine import *

# basedir = path.abspath(path.dirname(__file__))


  
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config:
    # Connect to MongoDB
    # db = connect(host="mongodb+srv://flask_user:VeFWloeju0dVbhdF@cluster0.3e1h8.mongodb.net/tasksdb?retryWrites=true&w=majority")

    # Forms secret key
    'SECRET_KEY' = 'fourjaw'
