from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

# Swagger imports
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# Media handling
from django.conf import settings
from django.conf.urls.static import static

# Swagger schema setup
schema_view = get_schema_view(
    openapi.Info(
        title="Ecommerce API",
        default_version='v1',
        description="API for Users, Products, Bookings",
        contact=openapi.Contact(email="admin@example.com"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    # Admin
    path("admin/", admin.site.urls),

    # App APIs
    path("api/", include("UsersApp.urls")),
    path("api/", include("ProductApp.urls")),
    path("api/", include("BookingApp.urls")),

    # Swagger & ReDoc
    path("swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("swagger.json/", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
]

# Media file support (optional for development)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
