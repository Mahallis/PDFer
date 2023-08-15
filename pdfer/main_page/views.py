from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings

from .forms import UploadFileForm
from .services import compress_pdf, file_manage


def index(request) -> HttpResponse:
    '''Add validation to a form (to check for a type)'''
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES.get('file')
            file_path = file_manage.save_file(
                file, settings.MEDIA_ROOT / 'pdfs/')
            compressed_file_path = compress_pdf.compress_file(file_path)
            file_manage.delete_file(file_path)
            with open(compressed_file_path, 'rb') as compressed_file:
                file_manage.delete_file(compressed_file_path)
                return HttpResponse(compressed_file.read(), headers={
                    'Content-Type': 'application:pdf',
                    'Content-Disposition': f'attachment; filename="{request.FILES.get("file").name}"'
                })
    else:
        form = UploadFileForm()
    context = {'form': form,
               'name': 'Main Janos'}
    return render(request, 'main_page/main_page.html', context)


def names(request, name) -> HttpResponse:
    context = {'name': name}
    return render(request, 'main_page/main_page.html', context)
