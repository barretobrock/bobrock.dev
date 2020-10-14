from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
bcrypt = Bcrypt()
log_mgr = LoginManager()
log_mgr.login_view = 'users.login'
log_mgr.login_message_category = 'info'


# def get_db_connection() -> sqlite3.Connection:
#     """Returns sqlite connection object"""
#     conn = sqlite3.connect('database.db')
#     # Set this so we can have name-based access to columns
#     conn.row_factory = sqlite3.Row
#     return conn
#

