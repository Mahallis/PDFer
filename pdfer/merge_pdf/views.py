from django.shortcuts import render
from .forms import MergeForm
from .services import merge_pdf_service


def merge_pdf(request):
    if request.method == 'POST':
        form = MergeForm(request.POST, request.FILES)
        if form.is_valid():
            merged_file_path = merge_pdf_service(form.cleaned_data)
            return merged_file_path
    else:
        form = MergeForm()
    context = {'form': form,
               'title': 'Разделение документа'}
    return render(request, 'merge_pdf/merge.html', context=context)
