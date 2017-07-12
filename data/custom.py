import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
to_list = "abcdef18032015@gmail.com"
from_ = "abcdef18032015@gmail.com"
def send_email(from_ ,to_list ):
	try:
		host = "smtp.gmail.com"
		port = 587
		username = "abcdef18032015@gmail.com"
		password = "Shubham96"
		from_ = from_
		to_list =  to_list  #shubhammuramkar96@gmail.com"
		message = MIMEMultipart("alternative")
		message["Subject"] = "pdf"
		message["To"] = to_list
		message["From"] = from_
		text  = "Hello! how are you"
		html = """\
		<html>
		   <head></head>
		   <body>
		      <p>Hey!<br>
		          Testing this email <b>message</b>. Made by <a href='http://joincfe.com'>Team CFE</a>.
		      </p>
		   </body>
		</html>
		    """
		m1 = MIMEText(text,"plain")
		m2 = MIMEText(html,"html")
		message.attach(m1)
		message.attach(m2)
		email = smtplib.SMTP(host,port)
		email.ehlo()
		email.starttls()
		email.login(username,password)
		email.sendmail(from_,to_list,message.as_string())
		email.quit()
	except smtplib.SMTPException:
		print("Unable to connect")
		return False
	else:
		return True

print(send_email("abcdef18032015@gmail.com","abcdef18032015@gmail.com"))



















