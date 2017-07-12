import csv
import datetime
import shutil,os
from tempfile import NamedTemporaryFile
from zintergating.templates import get_template,changing_context
import datetime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
file_get_path = os.path.join(os.getcwd(),"data.csv")

host = "smtp.gmail.com"
port = 587
username = "abcdef18032015@gmail.com"
password = "Shubham96"
from_ = username
to_list =  "abcdef18032015@gmail.com"

class UserManager():
    def change_read_data(self,user_data):
        file = "/Users/cool/Desktop/data/templates/email_message.txt"
        file_html = "/Users/cool/Desktop/data/templates/test.html"

        change = user_data
        if isinstance(user_data,dict):
            message = get_template(file)
            message_html = get_template(file_html)
            plain_ = changing_context(message,change)
            html_ = changing_context(message_html,change)
            return (plain_ , html_)
        return (None , None)


    def UserMessage(self, user_id=None, email= None):
        user = self.read_data(user_id = user_id, email = email)
        if user:
            plain_ , html_ = self.change_read_data(user)
            print(plain_ , html_)
            user_email = user.get("email","shubhammuramkar96@gmail.com")
            to_list.append(user_email)
            email = smtplib.SMTP(host,port)
            email.ehlo()
            email.starttls()
            email.login(username,password)
            message = MIMEMultipart("alternative")
            message["Subject"] = "Billing Update"
            message["From"] = from_
            message["To"] = user_email
            m1 = MIMEText(plain_,"plain")
            m2 = MIMEText(html_,"html")
            message.attach(m1)
            message.attach(m2)
            email.sendmail(from_, to_list, message.as_string())
            email.quit()
        return None

    def read_data(self,user_id=None, email=None):
        filename = file_get_path
        with open(filename, "r") as csvfile:
            reader = csv.DictReader(csvfile)
            items = []
            unknown_user_id = None
            unknown_email = None
            for row in reader:
                if user_id is not None:
                    if int(user_id) == int(row.get("id")):
                        return row
                    else:
                        unknown_user_id = user_id
                if email is not None:
                    if email == row.get("email"):
                        return row
                    else:
                        unknown_email = email
            if unknown_user_id is not None:
                print("User id {user_id} not found".format(user_id=unknown_user_id))
            if unknown_email is not None:
                print("Email {email} not found".format(email=unknown_email))
        return None
