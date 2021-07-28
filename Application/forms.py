from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Email, EqualTo, DataRequired, ValidationError
from Application.models import User


class Login(FlaskForm):
    username = StringField(label='Username:', validators=[DataRequired()])
    password = PasswordField(label='Password:', validators=[DataRequired()])
    sign_in = SubmitField(label='Sign In')


class Register(FlaskForm):

    def validate_username(self, username_to_check):
        user = User.query.filter_by(username=username_to_check.data).first()
        if user:
            raise ValidationError("Username Already Exist")

    def validate_email(self, email_to_check):
        user = User.query.filter_by(email=email_to_check.data).first()
        if user:
            raise ValidationError("Email-Id Already Exist")

    username = StringField(label='Username:', validators=[DataRequired()])
    name = StringField(label='Full Name:', validators=[DataRequired()])
    email = StringField(label='Email:', validators=[DataRequired(), Email()])
    password1 = PasswordField(label='Password:', validators=[DataRequired()])
    password2 = PasswordField(label='Confirm Password:', validators=[DataRequired(), EqualTo('password1')])
    sign_up = SubmitField(label='Register')

