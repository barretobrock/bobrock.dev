from flask import Flask, request, g
# Internal packages
from configurations import BaseConfig
from flask_base import db, bcrypt, log_mgr, babel
from .admin import admin
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
    babel.init_app(app)
    # Register routes
    for rt in [admin, main, users, posts, errors]:
        app.register_blueprint(rt)

    @babel.localeselector
    def get_locale():
        if not g.get('lang_code', None):
            g.lang_code = request.accept_languages.best_match(app.config['LANGUAGES'])
        return g.lang_code
    return app
