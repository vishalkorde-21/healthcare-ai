from django.contrib import admin
from django.urls import path
from api import views   # ✅ FIX

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Healthcare AI API",
        default_version='v1',
        description="AI based diagnosis system",
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.get_patients),
    path('create/', views.create_patient),

    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0)),
]