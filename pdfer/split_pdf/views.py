from django.shortcuts import render

from .forms import SplitForm
from .services import split_pdf_service


def split_pdf(request):
    if request.method == 'POST':
        form = SplitForm(request.POST, request.FILES)
        if form.is_valid():
            merged_file_response = split_pdf_service(form.cleaned_data)
            return merged_file_response
    else:
        form = SplitForm()
    context = {
        'title': 'Разделение документа',
        'form': form
    }
    return render(request, 'split_pdf/split.html', context)
