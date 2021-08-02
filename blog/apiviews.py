from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics, viewsets, filters, views, permissions
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
# from dj_rest_auth.jwt_auth import JWTAuthentication
from rest_framework_simplejwt.authentication import JWTAuthentication

from blog.models import Post,CategoriaPost, Comentario, Imagen

from usuario.permission import IsOwnerOrReadOnly
from blog.serializers import PostNestedSerializer, CategoriaPostNestedSerializer, ComentarioSerializers,\
    CategoriaPostSerializers, PostSerializers, ImagenSerializers, LikePostSerializers

from djserver.utils import ResizeImageMixin


class ExtendedPagination(PageNumberPagination):
    page_size = 10

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



class PostViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.filter(aprobado=True)
    serializer_class = PostSerializers


class PostReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    permission_classes = [IsOwnerOrReadOnly]
    queryset = Post.objects.filter(aprobado=True).order_by('-creado','-actualizado')
    serializer_class = PostNestedSerializer

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]

    search_fields = ['titulo','mensaje','creado','owner']
    ordering_fields =['creado', 'titulo']
    filterset_fields = {
        'creado': ['lte', 'gte'],  # Año menor o igual, mayor o igual que
        'titulo': ['exact'],  # Género exacto
        'categoria': ['exact'],  # Género exacto
        'owner':['exact']
    }
    pagination_class = ExtendedPagination
    pagination_class.page_size = 10


class CategoriaPostViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = CategoriaPost.objects.filter().order_by("-nombre","-id")
    serializer_class = CategoriaPostNestedSerializer

class CategoriaPostReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = CategoriaPost.objects.filter().order_by("-nombre","-id")
    serializer_class = CategoriaPostNestedSerializer

class ComentarioPostViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Comentario.objects.filter(aprobado=True).order_by("-creado","-id")
    serializer_class = ComentarioSerializers

class ImagenPostViewSet(viewsets.ModelViewSet):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [IsOwnerOrReadOnly]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    queryset = Imagen.objects.all()
    serializer_class = ImagenSerializers





#
# class ComentarioPostViewSet(viewsets.ModelViewSet):
#     authentication_classes = ()
#     # authentication_classes = [JWTAuthentication]
#     # permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
#     permission_classes = ()
#     queryset = Comentario.objects.filter(aprobado=True).order_by("-creado","-id")
#     serializer_class = ComentarioPostNestedSerializer

from django.shortcuts import get_object_or_404

class PostLikeAPIToggle(views.APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get("id")
        obj  = get_object_or_404(Post, id=id)
        # url_ = obj.get_absolute_url()
        user = self.request.user
        updated = False
        liked   = False
        count   = 0
        if user.is_authenticated:
            if user in obj.likes.all():
                liked = False
                obj.likes.remove(user)
                count = obj.likes.count()
            else:
                liked = True
                obj.likes.add(user)
                count = obj.likes.count()
            updated = True
        data = {
            "updated" : updated,
            "liked"   : liked,
            "count"   : count
        }

        return Response(data)


class VistoPostAPIView(views.APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get("id")
        obj  = get_object_or_404(Post, id=id)
        # url_ = obj.get_absolute_url()
        user = self.request.user
        visto = obj.vistas
        suma = 0
        if user.is_authenticated:
            suma = visto + 1
            obj.vistas = suma
            obj.save()
        data = {
            "visto" : suma
        }

        return Response(data)



class AlcancePostAPIView(views.APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        id = self.kwargs.get("id")
        obj  = get_object_or_404(Post, id=id)
        user = self.request.user
        updated = False
        alcance   = False
        if user.is_authenticated:
            if not user in obj.alcance.all():
                alcance = True
                obj.alcance.add(user)
            updated = True
        data = {
            "updated" : updated,
            "alcance" : alcance
        }
        return Response(data)



class PostReportAPIToggle(views.APIView):
    # authentication_classes = [JWTAuthentication]
    # permission_classes = [permissions.IsAuthenticated]
# FUNCTION FOR UPDATE POST (reports)
    def get(self, request, *args, **kwargs):
        id = self.kwargs.get("id")
        obj  = get_object_or_404(Post, id=id)
        # url_ = obj.get_absolute_url()
        user = self.request.user
        updated = False
        reported   = False
        count   = 0
        if user.is_authenticated:
            if not user in obj.reports.all():
                reported = True
                obj.reports.add(user)
                count = obj.reports.count()
                updated = True
        data = {
            "updated" : updated,
            "reported"   : reported,
            "count"   : count
        }

        return Response(data)