from django.shortcuts import render
from rest_framework import permissions, viewsets
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from imc.models import IMC
from usuario.permission import IsOwnerOrReadOnly
from imc.serializers import IMCSerializers
# Create your views here.
class IMCViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = IMC.objects.filter().order_by("-created","-imc", "-id")
    serializer_class = IMCSerializers