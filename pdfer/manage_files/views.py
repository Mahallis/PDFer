from django.shortcuts import render


def main_page(request):
    context = {
        'title': 'PDFer',
        'pages': [('Сжать', 'compress_pdf', 'assets/manage_files/compress.svg', 'Уменьшение размера документов (возможна потеря качества)'), 
                  ('Объединить', 'merge_pdf', 'assets/manage_files/merge.svg', 'Объединение документов в порядке загрузки'), 
                  ('Разделить', 'split_pdf', 'assets/manage_files/split.svg', 'Разделение докумена по страницам'),
                  ('Организовать', 'organize_pdf', 'assets/manage_files/organize.svg', 'Изменение порядка документа и ориентации страниц')
                  ]
    }
    return render(request, 'manage_files/apps.html', context=context)
