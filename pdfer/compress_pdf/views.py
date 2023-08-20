from django.http import HttpResponse, FileResponse
from django.shortcuts import render

from .forms import CompressForm
from .services.compress_pdf import compress_pdf


def compress(request) -> FileResponse | HttpResponse:
    '''Add validation to a form (to check for a type)'''
    if request.method == 'POST':
        form = CompressForm(request.POST, request.FILES)
        if form.is_valid():
            file_response = compress_pdf(form.cleaned_data)
            return file_response
    else:
        form = CompressForm()
    context = {'form': form,
               'title': 'Сжатие документа'}
    return render(request, 'compress_pdf/compress_pdf.html', context)
