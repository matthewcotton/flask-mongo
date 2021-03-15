from flask import Flask, jsonify, render_template
from mongoengine import *

app = Flask(__name__)

# Connect to MongoDB
connect(host="mongodb+srv://flask_user:VeFWloeju0dVbhdF@cluster0.3e1h8.mongodb.net/tasksdb?retryWrites=true&w=majority")

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


@app.route('/tasks')
def get_tasks():
    taskList = []
    for task in Tasks.objects:
        taskList.append(task)
    print(taskList)
    return render_template('index.html', taskList = taskList)

# add get one task by id route


@app.route('/add')
def add_task():
    # get data from form
    # newTask = Tasks(title="",
    #          description="",
    #          completed=False, assigned_to="").save()
    return "add route"


app.run()
