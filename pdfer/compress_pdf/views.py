from django.http import HttpResponse, FileResponse
from django.shortcuts import render

from .forms import CompressForm
from .services import compress_pdf


def compress(request) -> FileResponse | HttpResponse:
    '''Shows the form and sendf the POSTed data to a compress service'''
    if request.method == 'POST':
        form = CompressForm(request.POST, request.FILES)
        if form.is_valid():
            compressed_file_response = compress_pdf(
                form.cleaned_data)  # TODO: check mem usage
            return compressed_file_response
    else:
        form = CompressForm()
    context = {'form': form,
               'title': 'Сжатие документа'}
    return render(request, 'compress_pdf/compress_pdf.html', context)
