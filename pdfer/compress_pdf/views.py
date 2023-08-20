from shutil import rmtree

from django.http import HttpResponse, FileResponse
from django.shortcuts import render

from .forms import UploadFileForm
from .services.compress_pdf import compress_pdf
from manage_files.services.manage_files import tmp_storage_init, generate_result_file


def compress(request) -> FileResponse | HttpResponse:
    '''Add validation to a form (to check for a type)'''
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            form = form.cleaned_data
            tmp_storage = tmp_storage_init()
            compressed_files = compress_pdf(form, tmp_storage)
            result_file_path = generate_result_file(compressed_files)
            file_response = FileResponse(
                open(result_file_path, 'rb'),
                as_attachment=True,
                filename=result_file_path.name)
            rmtree(tmp_storage)
            return file_response
    else:
        form = UploadFileForm()
    context = {'form': form,
               'title': 'Сжатие документа'}
    return render(request, 'compress_pdf/compress_pdf.html', context)
