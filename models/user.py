from dataclasses import dataclass
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask import current_app
from flask_login import UserMixin
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import deferred
# Internal packages
from flask_base import db, log_mgr


@log_mgr.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@dataclass
class User(db.Model, UserMixin):
    id: int
    username: str
    password: str

    id = Column(Integer, primary_key=True)
    username = Column(String(20), unique=True, nullable=False)
    # Making a column deferred will only render it when called directly
    password = deferred(Column(String(60), nullable=False))
    user_posts = db.relationship('Posts', backref='author', lazy='dynamic')

    def get_reset_token(self, expires_sec=1800):
        s = Serializer(current_app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(current_app.config['SECRET_KEY'])
        try:
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    def __repr__(self):
        return f"User('{self.username}')"
