from django.shortcuts import render

# Create your views here.


def split_pdf(request):
    return render(request, 'split_pdf/split.html')
