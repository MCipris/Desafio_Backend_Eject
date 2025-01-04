from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from apps.mini_twitter.views import UserViewSet, PostagemViewSet, ComentarioViewSet, CurtidaViewSet

router = routers.DefaultRouter()
router.register('users', UserViewSet, 'Users')
router.register('postagens', PostagemViewSet,'Posts')
router.register('comentarios', ComentarioViewSet,'Comentarios')
router.register('curtidas', CurtidaViewSet,'Curtidas')

urlpatterns = [
    path('admin-login/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('', include(router.urls)), 
]