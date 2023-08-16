from shutil import rmtree

from django.http import HttpResponse, FileResponse
from django.shortcuts import render

from .forms import UploadFileForm
from .services import compress_pdf, file_manage


def index(request) -> FileResponse | HttpResponse:
    '''Add validation to a form (to check for a type)'''
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES.get('file')
            upload_file_path = file_manage.store_file(file)
            compressed_file_path = compress_pdf.compress_file(
                upload_file_path, form.cleaned_data)

            file_response = FileResponse(
                open(compressed_file_path, 'rb'),
                as_attachment=True,
                filename=compressed_file_path.name)
            rmtree(upload_file_path.parent)
            return file_response
    else:
        form = UploadFileForm()
    context = {'form': form,
               'title': 'Сжатие документа'}
    return render(request, 'main_page/main_page.html', context)


def names(request, name) -> HttpResponse:
    context = {'name': name}
    return render(request, 'main_page/main_page.html', context)
