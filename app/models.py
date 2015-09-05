from . import db


class SignUp(db.Model):
  id = db.Column(db.Integer, primary_key=True)
  image=db.Column(db.String(120))
  firstname = db.Column(db.String(80), unique=True)
  lastname = db.Column(db.String(120), unique=True)
  age=db.Column(db.String(64))
  sex=db.Column(db.String(64))
  highscore_P=db.Column(db.Integer)
  highscore_SI=db.Column(db.Integer)
  tdollars=db.Column(db.Integer)
  password = db.Column(db.String(80))
  username=db.Column(db.String(80),unique=True)
  email = db.Column(db.String(80), unique = True)
  confirmed = db.Column(db.String(64), default=False)
  
    
  def __init__(self,firstname,lastname,age,sex,image,password,email,username,confirmed):
    self.image=image
    self.firstname = firstname
    self.lastname = lastname
    self.age=age
    self.sex=sex
    self.password=email
    self.highscore_P=0
    self.highscore_SI=0
    self.tdollars=0
    self.email=password
    self.username=username
    self.confirmed=confirmed
  
  def is_authenticated(self):
    return True

  def is_active(self):
    return True

  def is_anonymous(self):
    return False

  def get_id(self):
    try:
      return unicode(self.id) # python 2 support
    except NameError:
      return str(self.id) # python 3 support
    
  def __repr__(self):
      return '<SignUp %r>' % self.firstname
    
  

