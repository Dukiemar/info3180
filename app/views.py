"""
Flask Documentation:     http://flask.pocoo.org/docs/
Jinja2 Documentation:    http://jinja.pocoo.org/2/documentation/
Werkzeug Documentation:  http://werkzeug.pocoo.org/documentation/

This file creates your application.
"""
#from . import db, models
import smtplib
import os
#from flask_wtf.file import FileField
from werkzeug import secure_filename
from app import app
from flask import render_template, request, redirect, url_for,send_file,flash
from app import db
from app.models import SignUp
from flask import jsonify, session
from .form import signUp,loginForm,update
import time
from flask.ext.login import login_user, logout_user, current_user, login_required

###
# Routing for your application.
###
#WTF_CSRF_ENABLED = False
app.config['SECRET_KEY'] = "javanddukes"

@app.route('/home')
def home():
    """Render website's home page."""
    return render_template('home.html')


@app.route('/about/')
def about():
    """Render the website's about page."""
    return render_template('about.html')


###
# The functions below should be applicable to all Flask apps.
###

@app.route('/<file_name>.txt')
def send_text_file(file_name):
    """Send your static text file."""
    file_dot_text = file_name + '.txt'
    return app.send_static_file(file_dot_text)


@app.after_request
def add_header(response):
    """
    Add headers to both force latest IE rendering engine or Chrome Frame,
    and also to cache the rendered page for 10 minutes.
    """
    response.headers['X-UA-Compatible'] = 'IE=Edge,chrome=1'
    response.headers['Cache-Control'] = 'public, max-age=600'
    return response


@app.errorhandler(404)
def page_not_found(error):
    """Custom 404 page."""
    return render_template('404.html'), 404


@app.route("/timeinfo/")
def timeinfo():
  return time.strftime('%a %d %b %Y')


@app.route('/signup', methods=['GET','POST'])
def profile():
    form=signUp(csrf_enabled=False)
    confirmation= request.form.get("username")
    if request.method == 'POST' and form.validate():
      img=form.image.data 
      filename = secure_filename(img.filename)
      form.image.data.save(os.path.join('app/static', filename))
      user=SignUp(form.firstname.data, form.lastname.data, form.age.data, form.sex.data,filename,form.email.data,form.password.data,form.username.data,confirmed=confirmation)
      db.session.add(user)
      db.session.commit()  
      confirm_email(confirmation)
      return "Profile successfully submitted,check your email for confirmation link. Go back to the previous page and refresh if you wish to enter another"
    return render_template('signup.html',form=form)
  
@app.route('/signup/confirm/<confirm>/', methods=['GET'])
def confirm(confirm):
    if (SignUp.query.filter_by(confirmed = confirm).first() is None):
        return "A error has been encountered, please retry"
    else:
        user = SignUp.query.filter_by(confirmed = confirm).first()
        user.active = True
        db.session.commit()
        return  "Thank you...Your profile has been successfully confirmed"
      
  

@app.route('/login',methods=['GET','POST'])
def login():
    form = loginForm()
    if request.method == 'POST':
      user =  SignUp.query.filter_by(username = form.username.data).first()
      if user:
        if user.password == form.password.data:
          return redirect(url_for("games"))
      return "Login failed. Please check to ensure that the username and password that was submitted at the signup route is what you are entering."
    return render_template("loginForm.html", form=form)

  
@app.route('/profiles',methods=['GET','POST'])
def profiles():
  users=db.session.query(SignUp).all()
  if 1>2:
    lst=[]
    for user in users:
      lst.append({'id':user.id, 'image':user.image, 'fname':user.firstname,'lname':user.lastname,'sex':user.sex, 'age':user.age,'highscore_P':user.highscore_P,'highscore_SI':user.highscore_SI,'tdollar':user.tdollars})
      users={'users':lst}
  return render_template('profiles.html', users=users)
  
  
@app.route('/profile/<userid>',methods=['GET','POST'])
def profiles_view(userid):
  prof=SignUp.query.filter_by(id=userid).first()
  user = {'id':prof.id, 'image':prof.image, 'age':prof.age, 'fname':prof.firstname, 'lname':prof.lastname,'username':prof.username, 'sex':prof.sex,'highscore_P':prof.highscore_P,'highscore_SI':prof.highscore_SI,'tdollars':prof.tdollars}
  return render_template('profile.html', user=user,mytime=timeinfo())
  

@app.route('/profile',methods=['GET','POST'])
def profile_view():
  prof=SignUp.query.filter_by(id=2).first()
  user = {'id':prof.id, 'image':prof.image, 'age':prof.age, 'fname':prof.firstname, 'lname':prof.lastname,'username':prof.username, 'sex':prof.sex,'highscore_P':prof.highscore_P,'highscore_SI':prof.highscore_SI,'tdollars':prof.tdollars}
  return render_template('profile.html', user=user,mytime=timeinfo())


@app.route("/profile/update", methods=["GET", "POST"])
def updater():
  form = update()
  #if request.method=="GET":
   #  render_template("update.html")
  if request.method=="POST":
    user = SignUp.query.filter_by(id=1).first()
    user.lastname=form.lastname.data
    user.firstname=form.firstname.data
    user.email=form.email.data
    user.age=form.age.data
    user.image=form.image.data
    db.session.add(user)
    db.session.commit()
  return render_template("update.html", form=form)
 
@app.route('/games/', methods=["GET"])
def games():
   return render_template('games.html')
  
@app.route('/game/<int:id>', methods=["GET"])
def game(id):
  if id == 1:
    return render_template('platformer.html')
  if id == 2:
    return render_template('spaceinvader.html')
 

@app.route('/game/highscore/', methods=['POST','GET'])
#@login_required
def highscore():
  #if request.method=="POST":
    user = SignUp.query.filter_by(id=current_user.get_id()).first()
    return jsonify( {"platformer": 0, "spaceinvader" : 0}) 
     
  


  
#################################################################################################################
def confirm_email(confirmation):
  fromname='Dukiemar (Website Manager)'
  toname='User'
  subject='Confirmation of email'
  fromaddr = 'dukiemarshaw@gmail.com'
  msg='Thank you for signing up. Please confirm your email by clicking the link that follows'+'  '+'http://dukes-info-proj3.herokuapp.com/signup/confirm/'+confirmation
  toaddr = request.form.get("email")
  message = """From: {} <{}>


To: {} <{}>

Subject: {}

{}

"""
  
  messagetosend = message.format(
   fromname,
   fromaddr,
   toname,
   toaddr,
   subject,
   msg)
  
  # Credentials (if needed)
  username = 'dukiemarshaw@gmail.com'
  password = 'private-hahahahaha'

  # The actual mail send
  server = smtplib.SMTP('smtp.gmail.com:587')
  server.starttls()
  server.login(username,password)
  server.sendmail(fromaddr, toaddr, messagetosend)
  server.quit()
  
#################################################################################################
    

  

  
# @app.route('/profile/update', methods=["GET", "POST"])
# def profile_update():
#     return 'profile_update'
  
# @app.route('/game/highscore',method=["POST"])
# def game_highscore():
#   return 'game highscore'
        
    
if __name__ == '__main__':
  app.run(debug=True,host="0.0.0.0",port="8080")


