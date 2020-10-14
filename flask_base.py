from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_babel import Babel

db = SQLAlchemy()
bcrypt = Bcrypt()
babel = Babel()
log_mgr = LoginManager()
log_mgr.login_view = 'users.login'
log_mgr.login_message_category = 'info'
