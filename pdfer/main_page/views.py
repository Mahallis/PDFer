from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from .forms import UploadFileForm
from .services import pdf_modify as pdf
from .services import files


def index(request) -> HttpResponse:
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            files.save_file(request.FILES.get('file'),
                            settings.MEDIA_ROOT / 'pdfs/')
            compressed_path = pdf.compress_pdf(request.FILES.get('file').name,
                                               settings.MEDIA_ROOT / 'pdfs/')
            with open(compressed_path, 'rb') as file:
                return HttpResponse(file, headers={
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
