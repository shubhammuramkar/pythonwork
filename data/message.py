import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

host = "smtp.gmail.com"
port = 587
username = "abcdef18032015@gmail.com"
password = "Shubham96"
from_ = username
to_list =  "abcdef18032015@gmail.com"

class MessageUser():
    user_details = []
    messages = []
    email_messages = []
    base_message = """Hi {name}!

Thank you for the purchase on {date}.
We hope you are exicted about using it. Just as a
reminder the purcase total was ${total}.
Have a great one!

Team CFE
"""
    def add_user(self, name, amount, email=None):
        name = name[0].upper() + name[1:].lower()
        amount = "%.2f" %(amount)
        today = datetime.date.today()
        dates = "{today.day}/{today.month}/{today.year}".format(today = today)
        detail = {
            "name": name,
            "amount": amount,
            "date":dates
        }
        if email is not None: # if email != None
            detail["email"] = email
        self.user_details.append(detail)
    def get_details(self):
        return self.user_details
    def make_messages(self):
        if len(self.user_details) > 0:
            for detail in self.get_details():
                name = detail["name"]
                amount = detail["amount"]
                date = detail["date"]
                mess = self.base_message
                new_message = mess.format(
                    name=name,
                    date=date,
                    total=amount
                )
                user_email = detail.get("email")
                if user_email:
                	user_data = {
                	"email":user_email,
                	"message" : new_message
                	}
                	self.email_messages.append(user_data)
                else:
                	self.messages.append(new_message)
            return self.messages
            return []
    def send_email(self):
    	self.make_messages()
    	if len(self.email_messages) > 0:
    		for detail in self.email_messages:
    			user_email = detail["email"]
    			user_message = detail["message"]
    			try:
    				email = smtplib.SMTP(host,port)
    				email.ehlo()
    				email.starttls()
    				email.login(username,password)
    				message = MIMEMultipart("alternative")
    				message["Subject"] = "Billing Update"
    				message["From"] = from_
    				message["To"] = user_email
    				m1 = MIMEText(user_message,"plain")
    				message.attach(m1)
    				email.sendmail(from_, [user_email], message.as_string())
    				email.quit()
    			except smtplib.SMTPException:
    				print("Unable to connect")
    		return True
    	return False

obj = MessageUser()
obj.add_user("Justin", 123.32, email='abcdef18032015@gmail.com')
obj.add_user("jOhn", 94.23, email='abcdef18032015@gmail.com')
obj.add_user("Sean", 93.23, email='abcdef18032015@gmail.com')
obj.add_user("Emilee", 193.23, email='abcdef18032015@gmail.com')
obj.add_user("Marie", 13.23, email='abcdef18032015@gmail.com')
obj.get_details()
obj.send_email()





