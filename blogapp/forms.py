from flask_wtf import FlaskForm
from wtforms import StringField, EmailField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, Length, EqualTo, ValidationError
from models import User


class RegistrationForm(FlaskForm):
    username = StringField(
        "username", validators=[DataRequired(), Length(min=4, max=8)]
    )
    email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=4, max=16)]
    )
    confirm_password = PasswordField(
        "Confirm password",
        validators=[DataRequired(), EqualTo("password")],
    )
    submit = SubmitField("Sign Up")
    
    def custom_email_validator(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError("Email already exists")

    def custom_username_validator(self, username):
        user = User.query.filter_by(email=username.data).first()
        if user:
            raise ValidationError("Username already exists")


class LoginForm(FlaskForm):
    username = StringField(
        "username", validators=[DataRequired(), Length(min=4, max=8)]
    )
    # email = EmailField("Email", validators=[DataRequired(), Email()])
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(min=4, max=16)]
    )
    # confirm_password = PasswordField(
    #     "Confirm password",
    #     validators=[DataRequired(), EqualTo("password")],
    # )
    remember = BooleanField("Remember me")
    submit = SubmitField("Login")
