from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .view import hello_world, update

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("xuitter.urls")),
    path("update_server/", update, name="update"),
    path("hello/", hello_world, name="hello_world"),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
