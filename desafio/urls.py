from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from apps.mini_twitter.views import UserViewSet, PostagemViewSet, ComentarioViewSet, CurtidaViewSet
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Documentação da API mini Twitter",
      default_version='v1',
      description="A presente documentação tem como finalidade detalhar o funcionamento das endpoints de uma API que simula um mini twitter.",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

router = routers.DefaultRouter()
router.register('users', UserViewSet, 'Users')
router.register('postagens', PostagemViewSet,'Posts')
router.register('comentarios', ComentarioViewSet,'Comentarios')
router.register('curtidas', CurtidaViewSet,'Curtidas')

urlpatterns = [
    path('admin-login/', admin.site.urls),
    path('token/', TokenObtainPairView.as_view()),
    path('token/refresh/', TokenRefreshView.as_view()),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('', include(router.urls)), 
]