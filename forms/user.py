from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, ValidationError
from flask_babel import lazy_gettext as LBBL
from flask import current_app
from flask_login import current_user
# Internal packages
from models import User


class RegistrationForm(FlaskForm):
    username = StringField(LBBL('Username'),
                           validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField(LBBL('Password'), validators=[DataRequired()])
    confirm_password = PasswordField(LBBL('Confirm Password'),
                                     validators=[DataRequired(), EqualTo('password')])
    control = PasswordField(LBBL('Admin Control'), validators=[DataRequired()])
    submit = SubmitField(LBBL('Sign Up'))

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError(LBBL('That username is taken. Please choose a different one.'))

    def validate_control(self, control):
        check_control = current_app.config['REGISTER_KEY']
        if control.data != check_control:
            raise ValidationError(LBBL('Invalid control.'))


class LoginForm(FlaskForm):
    username = StringField(LBBL('Username'), validators=[DataRequired(), Length(min=2, max=20)])
    password = PasswordField(LBBL('Password'), validators=[DataRequired()])
    remember = BooleanField(LBBL('Remember Me'))
    submit = SubmitField(LBBL('Login'))


class UpdateAccountForm(FlaskForm):
    username = StringField(LBBL('Username'),
                           validators=[DataRequired(), Length(min=2, max=20)])
    submit = SubmitField(LBBL('Update'))

    def validate_username(self, username):
        if username.data != current_user.username:
            user = User.query.filter_by(username=username.data).first()
            if user:
                raise ValidationError(LBBL('That username is taken. Please choose a different one.'))


class ResetPasswordForm(FlaskForm):
    password = PasswordField(LBBL('Password'), validators=[DataRequired()])
    confirm_password = PasswordField(LBBL('Confirm Password'),
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField(LBBL('Reset Password'))
