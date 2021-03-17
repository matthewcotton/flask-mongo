from flask import Flask
# from flask_assets import Environment
# from ddtrace import patch_all


# patch_all()


def init_app():
    """Create Flask application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object("config.Config")
    assets = Environment()
    assets.init_app(app)

    with app.app_context():
        # Import parts of our application
        from .blueprints.tasks_bp.tasks import tasks_bp

        # Register Blueprints
        app.register_blueprint(tasks_bp, url_prefic='/tasks')

        # Compile static assets
        compile_static_assets(assets)

        return app
