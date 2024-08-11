from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from compress_pdf import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.compress, name='compress_pdf'),
]

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
