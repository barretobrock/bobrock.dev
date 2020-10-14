from flask import Flask
# Internal packages
from configurations import BaseConfig
from flask_base import db, bcrypt, log_mgr
from .errors import errors
from .main import main
from .posts import posts
from .user import users


def create_app(config_class=BaseConfig) -> Flask:
    """Creates a Flask app instance"""
    # Config app
    app = Flask(__name__, static_folder='../static', template_folder='../templates')
    app.config.from_object(config_class)
    # Initialize things that supports app
    db.init_app(app)
    bcrypt.init_app(app)
    log_mgr.init_app(app)
    # Register routes
    for rt in [main, users, posts, errors]:
        app.register_blueprint(rt)

    return app