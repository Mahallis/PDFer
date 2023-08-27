from django.shortcuts import render


def main_page(request):
    context = {
        'title': 'PDFer проект',
        'pages': [('Сжать', 'compress_pdf', 'assets/manage_files/compress.svg'), 
                  ('Объединить', 'merge_pdf', 'assets/manage_files/merge.svg'), 
                  ('Разделить', 'split_pdf', 'assets/manage_files/split.svg'),
                  ('Организовать', 'organize_pdf', 'assets/manage_files/organize.svg')
                  ]
    }
    return render(request, 'manage_files/apps.html', context=context)
