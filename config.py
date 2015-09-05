import os

import psycopg2#added
import urlparse#added

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["DATABASE_URL"])

#conn = psycopg2.connect(
  #  database=url.path[1:],
  #  user=url.username,
  #  password=url.password,
  #  host=url.hostname,
 #   port=url.port
#)

SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']#added



WTF_CSRF_ENABLED = True
SECRET_KEY = 'javanddukes'

#the updates databases are below
#SQLALCHEMY_DATABASE_URI='postgresql://dukiemar:rameik@localhost/mydatabase'
#SQLALCHEMY_DATABASE_URI="postgresql://vipywuddzcwghu:TD-iEfkQMgBDcthqFpwlV7MjBD@ec2-54-197-245-93.compute-1.amazonaws.com:5432/ddjb4h7m7opmpk"