from flask_wtf import FlaskForm
from wtforms import *
from wtforms.validators import DataRequired

class Register(FlaskForm):
	username = StringField('username', validators=[DataRequired()])
	email = StringField('email', validators=[DataRequired()])
	name = StringField('name', validators=[DataRequired()])
	password = PasswordField('password', validators=[DataRequired()])
	submit = SubmitField('submit', validators=[DataRequired()])

class Login(FlaskForm):
	username = StringField('username', validators=[DataRequired()])
	password = PasswordField('password', validators=[DataRequired()])
	submit = SubmitField('submit', validators=[DataRequired()])
