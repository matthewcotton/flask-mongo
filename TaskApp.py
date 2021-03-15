from flask import Flask, jsonify, render_template, flash, redirect, url_for
from mongoengine import *
from addForm import AddForm

app = Flask(__name__)

app.config['SECRET_KEY'] = 'fourjaw'

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

# Define routes
@app.route('/')
@app.route('/tasks')
def get_tasks():
    taskList = []
    for task in Tasks.objects:
        taskList.append(task)
    print(taskList)
    return render_template('index.html', taskList=taskList)


@app.route('/add', methods=['GET', 'POST'])
def add_task():
    form = AddForm()
    if form.validate_on_submit():
        newTask = Tasks(title=form.title.data,
                        description=form.description.data, completed=form.completed.data).save()
        flash('Task Added')
        return redirect(url_for('get_tasks'))
    return render_template('add.html', title="Add Task", form=form)


app.run()
