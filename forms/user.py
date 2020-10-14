from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from flask_babel import _, lazy_gettext as _l
from flask import current_app
from flask_login import current_user
# Internal packages
from models import User


class RegistrationForm(FlaskForm):
    username = StringField(_l('Username'),
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    confirm_password = PasswordField(_l('Confirm Password'),
                                     validators=[DataRequired(), EqualTo('password')])
    control = PasswordField(_l('Admin Control'), validators=[DataRequired()])
    submit = SubmitField(_l('Sign Up'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(_l('That username is taken. Please choose a different one.'))

    def validate_control(self, control):
        check_control = current_app.config['REGISTER_KEY']
        if control.data != check_control:
            raise ValidationError(_l('Invalid control.'))


class LoginForm(FlaskForm):
    username = StringField(_l('Username'), validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    remember = BooleanField(_l('Remember Me'))
    submit = SubmitField(_l('Login'))


class UpdateAccountForm(FlaskForm):
    username = StringField(_l('Username'),
                           validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField(_l('Update'))

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(_l('That username is taken. Please choose a different one.'))


class ResetPasswordForm(FlaskForm):
    password = PasswordField(_l('Password'), validators=[DataRequired()])
    confirm_password = PasswordField(_l('Confirm Password'),
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(_l('Reset Password'))
