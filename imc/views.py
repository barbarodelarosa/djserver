from django.shortcuts import render
from rest_framework import permissions, viewsets, filters, views
from rest_framework.response import Response
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.shortcuts import get_object_or_404
from imc.models import IMC
from usuario.permission import IsOwnerOrReadOnly
from imc.serializers import IMCSerializers
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.pagination import PageNumberPagination

# from rest_framework import generics, viewsets, 
# Create your views here.


class ExtendedPagination(PageNumberPagination):
    page_size = 20

    def get_paginated_response(self, data):

        return Response({
            'count': self.page.paginator.count,
            'num_pages': self.page.paginator.num_pages,
            'page_number': self.page.number,
            'page_size': self.page_size,
            'next_link': self.get_next_link(),
            'previous_link': self.get_previous_link(),
            'results': data
        })

class IMCViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = IMC.objects.filter().order_by("-created","-imc", "-id")
    serializer_class = IMCSerializers


    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]


    search_fields = ['talla','peso','created','imc','calification']
    ordering_fields =['created', 'owner', 'imc', 'calification','talla','peso']
    filterset_fields = {
        'owner': ['exact'],
        'created': ['lte', 'gte'],  # Año menor o igual, mayor o igual que
        'imc': ['exact'],  # Género exacto
        'talla': ['exact'],  # Género exacto
        'peso': ['exact']  # Género exacto
    }
    pagination_class = ExtendedPagination
    pagination_class.page_size = 20


class PrivateTestAPIToggle(views.APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsOwnerOrReadOnly]
# FUNCTION FOR UPDATE POST (reports)
    def get(self, request, *args, **kwargs):
        id = self.kwargs.get("id")
        obj  = get_object_or_404(IMC, id=id)
        # url_ = obj.get_absolute_url()
        user = self.request.user
        updated = False
        # private   = obj.private
        # count   = 0
        
        if user.is_authenticated:
            if obj.private == False:
                obj.private = True
                updated = True
                obj.save()
            else:
                obj.private = False
                updated = True
                obj.save()
        # if obj.private == False:
        #     obj.private = True
        #     updated = True
        # obj.private = True

        data = {
            "updated" : updated,
            "private"   : obj.private,
            "talla"   : obj.talla,
        }
        return Response(data)


