from django.contrib import admin
from .models import User as MyUser
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from usuario.tasks import send_emails_user
from django.contrib import admin
from django.core.mail import send_mail
from djserver import settings


def activar_cuenta(self, request, queryset):
    asunto = 'Cuenta Activada'
    mensaje = 'Se ha activado su cuenta de usuario'
    queryset.update(is_active=True)
    users = queryset.all()
    for user in users:
        send_mail(asunto, mensaje, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
    return True

def desactivar_cuenta(self, request, queryset):
    asunto = 'Cuenta Desactivada'
    mensaje = 'Se ha desactivado su cuenta de usuario'
    queryset.update(is_active=False)
    users = queryset.all()

    for user in users:
        send_mail(asunto, mensaje, settings.EMAIL_HOST_USER, [user.email], fail_silently=False)
    return True

@admin.register(User)
class MyUserAdmin(admin.ModelAdmin):
    model=MyUser
    list_display = ('tipo_usuario', 'username', 'email', 'first_name', 'last_name', 'is_active', 'date_joined','is_staff')
    list_display_links = ('username', 'email',)
    search_fields = ['username', 'email', 'first_name', 'last_name']
    filter_horizontal = ['seguidores','groups','amigos']
    list_filter = ['tipo_usuario','is_active', 'date_joined', 'is_staff']
    readonly_fields = ['password']

    actions=[activar_cuenta,desactivar_cuenta]

    # def send_emails_action(self, request, queryset):
    #     send_emails_user.delay()
    #     queryset.update(is_staff=True)
    #
    #     return True




# admin.site.unregister(User)
admin.site.register(MyUser, MyUserAdmin)
# admin.site.register(User)
# Register your models here.
