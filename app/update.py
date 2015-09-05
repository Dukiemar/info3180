from . import db, models
import time
from form import login
def update():

form=login()  db.session.query(models.SignUp).filter(models.SignUp.firstname)=form.firstname.data
db.session.commit