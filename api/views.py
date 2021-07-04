from django.shortcuts import render
from rest_framework import generics, status, views
from usuario.models import User
from django.utils.http import urlsafe_base64_decode
from django.utils.encoding import *
from rest_framework.response import Response
from django.urls import reverse
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from api.serializers import MyPasswordResetConfirmSerializer, CustomRegisterSerializer
from rest_framework_simplejwt.tokens import RefreshToken

from dj_rest_auth.registration.serializers import RegisterSerializer

import string
import random

from dj_rest_auth.app_settings import PasswordResetConfirmSerializer
    # JWTSerializer, JWTSerializerWithExpiration, LoginSerializer,
    # PasswordChangeSerializer, ,
class MyPasswordTokenCheckAPI(generics.GenericAPIView):
    serializer_class = MyPasswordResetConfirmSerializer

    def get(self, request, uidb64, token):
        try:
            id=smart_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                return Response({'error': 'El token utilizado no es válido'}, status=status.HTTP_401_UNAUTHORIZED)

            return Response({'success':True, 'message':'Credencial Valid','uidb64':uidb64,'token':token}, status=status.HTTP_200_OK)


        except DjangoUnicodeDecodeError as identifier:
            if not PasswordResetTokenGenerator().check_token(user):
                return Response({'error':'El token utilizado no es válido'},status=status.HTTP_401_UNAUTHORIZED)

    def put(self, request, uidb64, token):
        serializer=self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response({
            'success': True,
            'message':'La contraseña ha sido modificada'
        }, status=status.HTTP_200_OK)

#
# class MySetNewPasswordAPIView(generics.GenericAPIView):
#     serializer_class = MyPasswordResetConfirmSerializer
#
#     def patch(self, request):
#         serializer=self.serializer_class(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         return Response({
#             'success': True,
#             'message':'La contraseña ha sido modificada'
#         }, status=status.HTTP_200_OK)

class CustomResgisterView(generics.GenericAPIView):
    serializer_class = RegisterSerializer
    def post(self, request):
        user = request.data
        serializer = self.serializer_class(data= user)
        serializer.is_valid(raise_exception=True)
        serializer.save(user)


        user_data = serializer.data
        token = RefreshToken.for_user(user_data)
        return Response(user_data, status.HTTP_201_CREATED)



        # user = self.perform_create(serializer)
        # headers = self.get_success_headers(serializer.data)


    #
    # def perform_create(self, serializer):
    #     user = serializer.save(self.request)
    #     if allauth_settings.EMAIL_VERIFICATION != \
    #             allauth_settings.EmailVerificationMethod.MANDATORY:
    #         if getattr(settings, 'REST_USE_JWT', False):
    #             self.access_token, self.refresh_token = jwt_encode(user)
    #         else:
    #             create_token(self.token_model, user, serializer)
    #
    #     complete_signup(
    #         self.request._request, user,
    #         allauth_settings.EMAIL_VERIFICATION,
    #         None,
    #     )
    #     return user


#
# def Prueba(number=1,length=10):
#
#     number_of_strings = number
#     length_of_string = length
#     for x in range(number_of_strings):
#         code = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length_of_string))
#         print(code)
#     return code
#
#
# class CustomRegister():
#     pass