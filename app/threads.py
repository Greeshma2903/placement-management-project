import threading
from django.conf import settings
from django.core.mail import send_mail


class send_applied_mail(threading.Thread):
    def __init__(self, email, company, position):
        self.email = email
        self.company = company
        self.position = position
        threading.Thread.__init__(self)
    def run(self):
        try:
            subject = "You Applied to a Company"
            message = f"You successfully applied for {self.position} at {self.company}.\nContact TPO for further details."
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject , message ,email_from ,[self.email])
        except Exception as e:
            print(e)


class send_result(threading.Thread):
    def __init__(self, email, job, res):
        self.email = email
        self.job = job
        self.res = res
        threading.Thread.__init__(self)
    def run(self):
        try:
            subject = "Regarding Job Application"
            message = f"Your application for {self.job} job post was {self.res}.\nContact TPO for further details."
            email_from = settings.EMAIL_HOST_USER
            send_mail(subject , message ,email_from ,[self.email])
        except Exception as e:
            print(e)