from django.core.mail import send_mail
from django.dispatch import receiver
from django.db.models.signals import post_save

from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):

    if created:
        send_mail(
            "Добро пожаловать в наш NewsWatch сайт!",
            f"Привет, {instance.username}. Добро пожаловать в наш NewsWatch сайт!. Наслаждайтесь новостями и обзорами",
            "AdaptaMail@gmail.com",
            [instance.email]
        )