import smtplib
fromname='Dukes'
toname='User'
subject='Confirmation'
fromaddr = 'dukiemarshaw@gmail.com'
msg='Please confirm your email'
toaddr = 'dukiemarshaw@yahoo.com'
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
password = 'private-hehehe'

# The actual mail send
server = smtplib.SMTP('smtp.gmail.com:587')
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddr, messagetosend)
server.quit()
