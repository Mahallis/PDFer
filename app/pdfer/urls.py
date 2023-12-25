from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from compress_pdf.views import compress


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', compress, name='compress_pdf'),
]

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
