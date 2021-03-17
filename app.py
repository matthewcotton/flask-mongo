# """Application entry point."""
# from TasksApp import init_app

# app = init_app()

# if __name__ == "__main__":
#     app.run(host="0.0.0.0")

from app import create_app, db, cli
from app.models import Users, Tasks

app = create_app()
cli.register(app)


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Users': Users, 'Tasks': Tasks}