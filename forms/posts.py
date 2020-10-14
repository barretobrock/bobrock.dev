from flask_wtf import FlaskForm
from flask_babel import lazy_gettext as _l
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired
# Internal packages
from flask import current_app


class PostForm(FlaskForm):
    lang = SelectField(_l('Language'), validators=[DataRequired()], choices=['en', 'et'])
    title = StringField(_l('Title'), validators=[DataRequired()])
    content = TextAreaField(_l('Content'), validators=[DataRequired()])
    submit = SubmitField(_l('Post'))
