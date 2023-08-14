from django.http import HttpResponse
from django.shortcuts import render
from django.conf import settings
from .forms import UploadFileForm
from .services import pdf_modify as pdf
from .services import files

# Figure out how to embed servises here

# Create your views here.


def index(request) -> HttpResponse:
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            files.save_file(request.FILES.get('file'),
                            settings.MEDIA_ROOT / 'pdfs/')
            # pdf.compress_pdf('some_filename')
    else:
        form = UploadFileForm()
    context = {'form': form,
               'name': 'Main Janos'}
    return render(request, 'main_page/main_page.html', context)


def names(request, name) -> HttpResponse:
    context = {'name': name}
    return render(request, 'main_page/main_page.html', context)
