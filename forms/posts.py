from flask_wtf import FlaskForm
from flask_babel import lazy_gettext as LBBL
from wtforms import StringField, SubmitField, TextAreaField, SelectField
from wtforms.validators import DataRequired


class PostForm(FlaskForm):
    lang = SelectField(LBBL('Language'), validators=[DataRequired()], choices=['en', 'et'])
    title = StringField(LBBL('Title'), validators=[DataRequired()])
    content = TextAreaField(LBBL('Content'), validators=[DataRequired()])
    submit = SubmitField(LBBL('Post'))
