from django.shortcuts import render

# Create your views here.
import string, math
from usuario.models import User
from blog.models import Post

from django.utils.crypto import get_random_string

"""
************ SCRIPT PARA CREAR USUARIOS ALEATORIAMENTE *************
"""
def create_user_random(cantidad):
    for x in range(cantidad):
        username = 'usuario_{}'.format(get_random_string(6, string.ascii_letters))
        email = '{}@prueba.com'.format(username)
        password = get_random_string(50)
        User.objects.create_user(username=username, email=email, password=password)
    return print('{} Usuario creados correctamente...'.format(x))

