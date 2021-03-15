from flask import render_template
from app import app
from mongoengine import *
from models import Tasks


@app.route('/')
@app.route('/index')
def index():
  taskList = []
  for task in Tasks.objects:
    taskList.append(task)
  return str(taskList)
