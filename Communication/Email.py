import sys
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText


class Email:
    def __init__(self, sender_email, password, receiver_list, subject, message):
        self.sender_email = sender_email
        self.password = password
        self.receiver_list = receiver_list
        self.subject = subject
        self.message = message

    def SendEmail(self):
        try:
            message = MIMEMultipart()
            message['From'] = self.sender_email
            message['Subject'] = self.subject
            message.attach(MIMEText(self.message, 'html'))
            session = smtplib.SMTP('smtp.gmail.com', 587)
            session.starttls()
            session.login(self.sender_email, self.password)
            text = message.as_string()
            for receiver in self.receiver_list:
                message['To'] = receiver
                session.sendmail(self.sender_email, receiver, text)
            session.quit()
            return True
        except:
            raise(sys.exc_info()[0])
