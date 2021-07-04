from celery import shared_task

from django.core.mail import send_mail
from djserver import settings
from usuario.models import User


# @shared_task
def send_emails_user():
    asunto = 'Mensaje de prueba'
    mensaje = 'Bienvenido al nuevo mensaje de PRUEBA'
    users = User.objects.all()
    for user in users:
        send_mail(asunto, mensaje, settings.EMAIL_HOST_USER,[user.email], fail_silently=False)

    return 'Se envio correctamente el correo al usuario: {}'.format(user.username)