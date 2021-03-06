from flask import Flask
# Internal packages
from configurations import BaseConfig
from flask_base import db, bcrypt, log_mgr
from .admin import admin
from .api import api
from .errors import errors
from .main import main
from .posts import posts
from .user import users


def create_app(*args, **kwargs) -> Flask:
    """Creates a Flask app instance"""
    # Config app
    config_class = kwargs.pop('config_class', BaseConfig)
    app = Flask(__name__, static_folder=config_class.STATIC_DIR_PATH,
                template_folder=config_class.TEMPLATE_DIR_PATH)
    app.config.from_object(config_class)
    # Initialize things that supports app
    db.init_app(app)
    bcrypt.init_app(app)
    log_mgr.init_app(app)
    # Register routes
    for rt in [admin, api, main, users, posts, errors]:
        app.register_blueprint(rt)

    return app
