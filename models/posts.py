from dataclasses import dataclass
from datetime import datetime
# Internal packages
from flask_base import db


@dataclass
class Posts(db.Model):
    id: int
    lang: str
    title: str
    date_posted: datetime
    content: str
    user_id: int

    id = db.Column(db.Integer, primary_key=True)
    lang = db.Column(db.String(2), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    date_posted = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    content = db.Column(db.Text, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __repr__(self):
        return f"Posts('{self.title}', '{self.date_posted}')"
