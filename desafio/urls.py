from django.contrib import admin
from django.urls import path, include

from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.mini_twitter.views import PostagemViewSet, ComentarioViewSet

router = routers.DefaultRouter()
router.register('postagens', PostagemViewSet,'Postagens')
router.register('comentarios', ComentarioViewSet,'Comentarios')


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)), 
]