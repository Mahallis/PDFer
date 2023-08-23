from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from compress_pdf.views import compress
from merge_pdf.views import merge_pdf
from split_pdf.views import split_pdf

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('manage_files.urls')),
    path('compress_pdf/', compress, name='compress_pdf'),
    path('merge_pdf/', merge_pdf, name='merge_pdf'),
    path('split_pdf/', split_pdf, name='split_pdf'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
