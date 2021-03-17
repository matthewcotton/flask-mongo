from flask import Blueprint

tasks_blueprint = Blueprint('tasks_blueprint', __name__)

@tasks_blueprint.route('/')
def index():
    return "This is an task app"