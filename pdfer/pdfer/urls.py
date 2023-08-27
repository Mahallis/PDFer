from django.contrib import admin
from django.urls import path, include
from compress_pdf.views import compress
from merge_pdf.views import merge_pdf
from split_pdf.views import split_pdf
from organize_pdf.views import organize_pdf


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('manage_files.urls')),
    path('compress_pdf/', compress, name='compress_pdf'),
    path('merge_pdf/', merge_pdf, name='merge_pdf'),
    path('split_pdf/', split_pdf, name='split_pdf'),
    path('organize_pdf/', organize_pdf, name='organize_pdf'),
]

