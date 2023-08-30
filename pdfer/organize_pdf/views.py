from django.shortcuts import render

from .forms import OrganizeForm
from .services import organize_pdf_service

def organize_pdf(request):
    if request.method == 'POST':
        form = OrganizeForm(request.POST, request.FILES)
        if form.is_valid():
            merged_file_response = organize_pdf_service(form.cleaned_data)
            return merged_file_response
    else:
        form = OrganizeForm()
    context = {
        'title': 'Организация документа',
        'form': form
    }
    return render(request, 'organize_pdf/organize.html', context)
