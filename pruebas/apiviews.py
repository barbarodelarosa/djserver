from rest_framework import viewsets, filters
from rest_framework_simplejwt.authentication import JWTAuthentication
from usuario.permission import IsOwnerOrReadOnly
from pruebas.models import EmotionState
from pruebas.serializers import EmotionStateSerializers
from django_filters.rest_framework import DjangoFilterBackend

class EmotionStateViewSet(viewsets.ModelViewSet):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsOwnerOrReadOnly]
    queryset = EmotionState.objects.filter()
    serializer_class = EmotionStateSerializers

    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    ordering = ('-id', '-created_at')
    search_fields = ['emotion_name','emotion_value','created_at','owner','public']
    ordering_fields =['id', 'created_at', 'emotion_name','owner']
    filterset_fields = {
        'created_at': ['lte', 'gte'],  # Año menor o igual, mayor o igual que
        'emotion_name': ['exact'],
        'emotion_value': ['exact'],
        'owner':['exact']
    }
