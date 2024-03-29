
from usuario.apiviews import UsuarioViewSet
from pruebas.apiviews import EmotionStateViewSet
from imc.views import IMCViewSet
from blog.apiviews import CategoriaPostViewSet, PostViewSet, ComentarioPostViewSet, CategoriaPostReadOnlyModelViewSet, \
                          PostReadOnlyModelViewSet, ImagenPostViewSet

from negocio.apiviews import CategoriaProductoReadOnlyModelViewSet, \
                             CategoriaNegocioReadOnlyModelViewSet, NegocioViewSet, \
                             NegocioReadOnlyModelViewSet, ProductoViewSet, ProductoReadOnlyModelViewSet, GaleriaViewSet
from rest_framework.routers import DefaultRouter
from django.urls import path


router = DefaultRouter()
router.register('categoria-post', CategoriaPostReadOnlyModelViewSet, basename='categoria-post')
router.register('categoria-negocio', CategoriaNegocioReadOnlyModelViewSet, basename='categoria-negocio')
router.register('categoria-producto', CategoriaProductoReadOnlyModelViewSet, basename='categoria-producto')

router.register('create-post', PostViewSet, basename='create-post')
router.register('create-negocio', NegocioViewSet, basename='create-negocio')
router.register('create-producto', ProductoViewSet, basename='create-producto')

router.register('read-post', PostReadOnlyModelViewSet, basename='read-post')
router.register('read-negocio', NegocioReadOnlyModelViewSet, basename='read-negocio')
router.register('read-producto', ProductoReadOnlyModelViewSet, basename='read-producto')

router.register('imagen', ImagenPostViewSet, basename='imagen')
router.register('comentario-post', ComentarioPostViewSet, basename='comentario-post')

router.register('galeria', GaleriaViewSet, basename='read-producto')



router.register('usuario', UsuarioViewSet, basename='usuario')
router.register('imc', IMCViewSet, basename='imc')
router.register('emotion-state', EmotionStateViewSet, basename='emotion-state')


urlpatterns=[

]

urlpatterns += router.urls



