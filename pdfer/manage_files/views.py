from django.shortcuts import render


def main_page(request):
    pages = ['compress_pdf', 'merge_pdf', 'split_pdf']
    return render(request, 'manage_files/index.html', context={'pages': pages})
