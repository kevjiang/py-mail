#!/usr/bin/env

'''
import smtplib
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login("andoverace10@gmail.com", "gobigblue")
 
msg = "YOUR MESSAGE!"
server.sendmail("barackobama@gmail.com", "kevjiang1@gmail.com", msg)
server.quit()
'''

import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
 
 
fromaddr = "andoverace10@gmail.com"
fakefromaddr = 'bo@gmail.com'
toaddr = "kevjiang1@gmail.com"
msg = MIMEMultipart()
msg['From'] = fakefromaddr
msg['To'] = toaddr
msg['Subject'] = "Very Important"
 
body = "Please contact imemdiately"
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "gobigblue")
text = msg.as_string()
server.sendmail(fakefromaddr, toaddr, text)
server.quit()