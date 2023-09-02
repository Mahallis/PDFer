from django.shortcuts import render


def main_page(request):
    context = {
        'title': 'PDFer',
        'pages': [('Сжать', 'compress_pdf', 'assets/manage_files/compress.svg', 'Уменьшение размера документов'),
                  ('Объединить', 'merge_pdf', 'assets/manage_files/merge.svg',
                   'Объединение документов в порядке загрузки'),
                  ]
    }
    return render(request, 'manage_files/apps.html', context=context)
