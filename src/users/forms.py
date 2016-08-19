from wtforms import SubmitField, StringField, PasswordField, validators
from flask_wtf import Form


class SignupForm(Form):

    first_name = StringField(label='First Name', validators=[validators.DataRequired("Please enter your first name.")])
    last_name = StringField(label='Last Name', validators=[validators.DataRequired("Please enter your last name.")])
    email = StringField(label='Email', validators=[validators.DataRequired("Please enter your email address."),
                                                   validators.Email("Please enter your email address.")])
    password = PasswordField(label='Password', validators=[validators.DataRequired("Please enter a password."),
                                                           validators.Length(min=6,
                                                                             message="Password must be 6 characters or more.")])
    submit = SubmitField(label='Sign up')


class LoginForm(Form):
    email = StringField(label='Email',
                        validators=[validators.DataRequired("Please enter your email address."),
                                    validators.Email("Please enter your email address.")])
    password = PasswordField(label='Password',
                             validators=[validators.DataRequired("Please enter a password.")])
    submit = SubmitField(label='Sign in')
