from tempfile import TemporaryDirectory

from django.http import HttpResponse, FileResponse
from django.conf import settings
from django.shortcuts import render

from .forms import CompressForm
from .services import compress_pdf


def compress(request) -> FileResponse | HttpResponse:
    '''Shows the form and sendf the POSTed data to a compress service'''
    if request.method == 'POST':
        form = CompressForm(request.POST, request.FILES)
        if form.is_valid():
            with TemporaryDirectory(dir=settings.MEDIA_ROOT) as tmp_dir:
                compressed_file_path = compress_pdf(
                    form.cleaned_data,
                    tmp_dir
                )
                return FileResponse(
                    open(compressed_file_path, 'rb'),
                    as_attachment=True,
                    filename=compressed_file_path.name
                )
    else:
        form = CompressForm()
    context = {'form': form,
               'title': 'Сжатие документа'}
    return render(request, 'compress_pdf/compress_pdf.html', context)
