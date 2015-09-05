from flask.ext.wtf import Form
from wtforms import StringField, TextField, FileField,PasswordField
from wtforms.validators import DataRequired, Required
from flask_wtf.file import FileField, FileRequired

class signUp(Form):
  image=FileField('image', validators=[Required()])
  firstname = TextField('firstname', validators=[Required()])
  lastname = TextField('lastname', validators=[Required()])
  age = TextField('age', validators=[Required()])
  sex = TextField('sex', validators=[Required()])
  username = TextField('username', validators=[Required()])
  email = TextField('email', validators=[Required()])
  password = PasswordField('password', validators=[Required()])
  
class update(Form):
  image=FileField('image', validators=[Required()])
  firstname = TextField('firstname', validators=[Required()])
  lastname = TextField('lastname', validators=[Required()])
  age = TextField('age', validators=[Required()])
  username = TextField('username', validators=[Required()])
  email = TextField('email', validators=[Required()])
  
  
# class sign_up(Form):
#   email = TextField('email',validator=[Required()])
#   password = PasswordField('Password',validator=[Required()])
  
class loginForm(Form):
  username = TextField('Username',validators=[Required()])
  password = PasswordField('Password',validators=[Required()])
  