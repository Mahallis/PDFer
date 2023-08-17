from shutil import rmtree
from os import listdir
from pathlib import Path
import zipfile

from django.http import HttpResponse, FileResponse
from django.shortcuts import render

from .forms import UploadFileForm
from .services import compress_pdf, file_manage


def index(request) -> FileResponse | HttpResponse:
    '''Add validation to a form (to check for a type)'''
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            files = form.cleaned_data['file_field']
            upload_files_path = file_manage.store_files(files)
            for file_path in listdir(upload_files_path / 'uploaded_files'):
                compress_pdf.compress_file(
                    upload_files_path / 'uploaded_files' / Path(file_path), form.cleaned_data)
            archive_path = upload_files_path / 'compressed.zip'
            with zipfile.ZipFile(archive_path, 'w') as archive:
                for file in listdir(upload_files_path / 'compressed_files'):
                    archive.write(
                        upload_files_path / 'compressed_files' / file, arcname=file)
            file_response = FileResponse(
                open(archive_path, 'rb'),
                as_attachment=True,
                filename='compresssed.zip')
            rmtree(upload_files_path)
            return file_response
    else:
        form = UploadFileForm()
    context = {'form': form,
               'title': 'Сжатие документа'}
    return render(request, 'main_page/main_page.html', context)


def names(request, name) -> HttpResponse:
    context = {'name': name}
    return render(request, 'main_page/main_page.html', context)
