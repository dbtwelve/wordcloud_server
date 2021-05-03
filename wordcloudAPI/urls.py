from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings
from rest_framework.routers import DefaultRouter
from .views import ImageViewSet, WordCloudViewSet
from rest_framework.urlpatterns import format_suffix_patterns

image_list = ImageViewSet.as_view({
    'post': 'create',
    'get': 'list'
})

image_detail = ImageViewSet.as_view({
    'get': 'list',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})


wc_list = WordCloudViewSet.as_view({
    'post': 'create',
    'get': 'list'
})

wc_detail = WordCloudViewSet.as_view({
    'get': 'list',
    'put': 'update',
    'delete': 'destroy'
})

urlpatterns = [
    path('index', views.index, name='index'),
    path('upload', views.upload_image, name='upload_image'),
    path('list', views.image_list, name='image_list'),
    path('<int:pk>', views.image_detail, name='image_detail'),
    path('<int:pk>/comments/new/', views.comment_new, name='comment_new'),
    path('<int:post_pk>/comments/<int:pk>/edit', views.comment_edit, name='comment_edit'),

]
urlpatterns += format_suffix_patterns([
    path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('image/', image_list, name='image_list'),
    path('image/<int:pk>/', image_detail, name='image_detail'),
    path('wordcloud/', wc_list, name='wc_list'),
    path('wordcloud/<int:pk>', wc_detail, name='wc_detail'),

])
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)