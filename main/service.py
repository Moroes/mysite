from django.core.mail import send_mail
from django.conf import settings


def send(user_email):
    print(send_mail(
        'asdss',
        '21sscs',
        settings.EMAIL_HOST_USER,
        [user_email],
        fail_silently=True,
    ))