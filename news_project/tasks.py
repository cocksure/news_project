from django.core.mail import send_mail
from news_project.celery import app


@app.task()
def send_email(subject, message, recipient_list):
    send_mail(
                subject,
                message,
                "AdaptaMail@gmail.com",
                recipient_list
            )
