from flask import Blueprint, render_template, flash, redirect, url_for
# from mongoengine import * #???
from flask-mongo.models import Tasks, Users
from addForm import AddForm

tasks_bp = Blueprint('tasks_bp', __name__,
                     template_folder='templates')


# Define routes
@tasks_bp.route('/')
@tasks_bp.route('/tasks')
def get_tasks():
    taskList = []
    for task in Tasks.objects:
        taskList.append(task)
    print(taskList)
    return render_template('index.html', taskList=taskList)


@tasks_bp.route('/add', methods=['GET', 'POST'])
def add_task():
    form = AddForm()
    if form.validate_on_submit():
        newTask = Tasks(title=form.title.data,
                        description=form.description.data, completed=form.completed.data)
        newTask.save()
        flash('Task "' + newTask.title + '" Added')
        return redirect(url_for('get_tasks'))
    return render_template('add.html', title="Add Task", form=form)

