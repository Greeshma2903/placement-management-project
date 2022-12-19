import threading
from django.conf import settings
from django.core.mail import send_mail


class send_credentials_mail(threading.Thread):
    def __init__(self, email, pw):
        self.email = email
        self.pw = pw
        threading.Thread.__init__(self)
    def run(self):
        try:
            subject = "Login Credentials"
            message = f"The login credentails toaccess your account are as following.\n Email : {self.email}\n Password : {self.pw}"
            email_from = settings.EMAIL_HOST_USER
            print(self.pw)
            send_mail(subject , message ,email_from ,[self.email])
        except Exception as e:
            print(e)
