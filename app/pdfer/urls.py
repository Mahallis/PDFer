from django.contrib import admin
from django.urls import path
from compress_pdf.views import compress


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', compress, name='compress_pdf'),
]
