from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from rest_framework_mongoengine.routers import DefaultRouter
from inventory.views import SettingViewSet
from rest_framework_swagger.views import get_swagger_view


schema_view = get_swagger_view(title='OCSHOP API')

router = DefaultRouter()
router.register(r'setting', SettingViewSet, base_name="setting")

urlpatterns = [
    path('', admin.site.urls),
    path('api/', include(router.urls)),
    path('api/docs/', schema_view, name="schema_view"),

]

if settings.DEBUG:
     urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT, show_indexes=True)
     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)