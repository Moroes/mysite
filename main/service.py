from django.core.mail import send_mail


def send(user_email):
    send_mail(
        'Приветствуем Вас на нашем сайте.',
        'Тут будет описание',
        'mysite.moroes@gmail.com',
        [user_email],
        fail_silently=False,
    )