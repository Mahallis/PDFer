from django.shortcuts import render

# Create your views here.


def merge_pdf(request):
    return render(request, 'merge_pdf/merge.html')
