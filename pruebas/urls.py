
from pruebas import apiviews
from rest_framework.routers import DefaultRouter
router = DefaultRouter()

router.register('emotion-state', apiviews.EmotionStateViewSet, basename='emotion-state')
urlpatterns=[

]

urlpatterns += router.urls



