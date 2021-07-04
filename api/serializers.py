from rest_framework import serializers
from django.contrib.auth.tokens import PasswordResetTokenGenerator
from django.utils.encoding import smart_str, force_str, smart_bytes, DjangoUnicodeDecodeError
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from usuario.models import User
from django.contrib import auth
from rest_framework.exceptions import AuthenticationFailed

from dj_rest_auth.registration.serializers import RegisterSerializer
from dj_rest_auth.serializers import PasswordResetSerializer

from allauth.account.adapter import get_adapter


class MyPasswordResetConfirmSerializer(serializers.Serializer):
    password=serializers.CharField(min_length=6, max_length=68, write_only=True)
    token=serializers.CharField(min_length=1, max_length=68, write_only=True)
    uidb64=serializers.CharField(min_length=1, write_only=True)

    # redirect_url = serializers.CharField(max_length=500, required=False)

    class Meta:
        fields =['password','token','uidb64']


    def validate(self, attrs):

        try:
            password=attrs.get('password')
            token=attrs.get('token')
            uidb64=attrs.get('uidb64')
            id=force_str(urlsafe_base64_decode(uidb64))
            user=User.objects.get(id=id)

            if not PasswordResetTokenGenerator().check_token(user, token):
                raise AuthenticationFailed('El enlace no es válido', 401)

            user.set_password(password)
            user.save()
        except Exception as e:
            raise AuthenticationFailed('El enlace no es válido', 401)

        return super().validate(attrs)




class CustomRegistrationSerializer(RegisterSerializer):

    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        # setup_user_email(request, user, [])
        return user




class CustomPasswordResetSerializer(PasswordResetSerializer):
  def get_email_options(self):
      return {
          'email_template_name': 'usuario/email/password_reset_email.html'
      }

#
# class CustomRegisterSerializer(RegisterSerializer):
#   def get_email_options(self):
#       return {
#           'email_template_name': 'usuario/email/password_reset_email.html'
#       }

class CustomRegisterSerializer(serializers.Serializer):
    email=serializers.EmailField(max_length=68, min_length=1, write_only=True)
    username=serializers.CharField(max_length=68, min_length=1, write_only=True)
    password=serializers.CharField(max_length=68, min_length=6, write_only=True)
    avatar=serializers.CharField(max_length=68, min_length=6, write_only=True)

    class Meta:
        model=User
        fields=['email','username','password', 'avatar']

    def validate(self, attrs):
        email = attrs.get('email','')
        username = attrs.get('username','')

        if not username.isalnum():
            raise serializers.ValidationError(
                'The username should only contain alphanumeric characters'
            )
        return attrs

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)


class MyCustomRegisterSerializer(RegisterSerializer):
    # def save(self, request):
    #     pass
    # avatar = serializers.CharField(write_only=True, required=True, max_length=100)
    # first_name = serializers.CharField(write_only=True, required=True, max_length=100)
    # last_name = serializers.CharField(
    #     write_only=True, required=True, max_length=100)
    #
    # birthday = serializers.DateField(required=True, write_only=True)
    # phone = serializers.CharField(max_length=20, write_only=True,
    #                               validators=[
    #                                   UniqueValidator(
    #                                       User.objects.all(),
    #                                       message=_('A user with this phone number already exists.')
    #                                   )
    #                               ])
    #
    # gender = serializers.ChoiceField(
    #     write_only=True,
    #     choices=[
    #         ('NO-OP', 'Rather not tell'),
    #         ('M', 'Male'),
    #         ('F', 'Female'),
    #     ],
    #     default='NO-OP'
    # )
    #
    # def get_cleaned_data(self):
    #     cleaned_data = super().get_cleaned_data()
    #     cleaned_data['avatar'] = self.validated_data.get('avatar', '')
    #     # cleaned_data['first_name'] = self.validated_data.get('first_name', '')
    #     # cleaned_data['last_name'] = self.validated_data.get('last_name', '')
    #     # cleaned_data['phone'] = self.validated_data.get('phone', '')
    #     # cleaned_data['birthday'] = self.validated_data.get('birthday', '')
    #     # cleaned_data['gender'] = self.validated_data.get('gender', '')
    #     print(cleaned_data)
    #     return cleaned_data
    def save(self, request):
        adapter = get_adapter()
        user = adapter.new_user(request)
        self.cleaned_data = self.get_cleaned_data()
        adapter.save_user(request, user, self)
        self.custom_signup(request, user)
        # setup_user_email(request, user, [])
        return user