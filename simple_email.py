import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText

##############################################
# You fill out the following variables 
# and let Python do the rest...
fromaddr = "andoverace10@gmail.com"
password = "gobigblue"
toaddr = "kjiang@andover.edu"
subject = "Sample Subject"
body = "Sample body"
##############################################

print "Sending email from %s to %s..." % (fromaddr, toaddr)
# the rest of the code
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = subject
 
msg.attach(MIMEText(body, 'plain'))
 
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, password)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()

print "Email sent!"