
from blog import apiviews
from rest_framework.routers import DefaultRouter
from rest_framework.urlpatterns import format_suffix_patterns 
from django.urls import path 
router = DefaultRouter()

"""
SOLO SE ESTA UTILIZANDO PARA LOS COMENTARIOS DEL POST
"""
# router.register('categoria', apiviews.CategoriaPostViewSet, basename='categoria-post')
# router.register('post', apiviews.PostNestedSerializer, basename='post')
# router.register('comentario', apiviews.ComentarioPostViewSet, basename='comentario-post')
# router.register('galeria', apiviews.GaleriaViewSet, basename='galeria')


# post_list = apiviews.PostViewSet.as_view({
#     'get': 'list',
#     'post': 'create'
# })

# post_detail = apiviews.PostViewSet.as_view({
#     'get': 'retrieve',
#     'put': 'update',
#     'patch': 'partial_update',
#     'delete': 'destroy'
# })



comment_creation = apiviews.PostCommentViewSet.as_view({
    'post': 'set_comment'
})
urlpatterns=[
    # path('posts/', post_list, name='post_list'), 
    # path('post/(?P<pk>[0-9]+)/', post_detail, name='post_detail'), 
    # path('post/<int:pk>/', post_detail, name='post_detail'), 
    # path('post/(?P<pk>[0-9]+)/comment/', comment_creation, name='comment_creation'),
    path('post/<int:pk>/comment/', comment_creation, name='comment_creation'),
]
# urlpatterns += urlpatterns('blog.apiviews', 
#     path('posts/$', post_list, name='post_list'), 
#     path('post/(?P<pk>[0-9]+)/$', post_detail, name='post_detail'), 
#     path('post/(?P<pk>[0-9]+)/comment/$', comment_creation, name='comment_creation'),
# )

urlpatterns += router.urls



