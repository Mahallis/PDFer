from PyPDF2 import PdfReader, PdfWriter


def show_pages(filename: str) -> None:
    '''Scaling pages to place them on a web page to proceed modification'''
    'TODO: get files one by one'

    file = PdfReader(filename)
    pages = file.pages
    with open('Page_scaled_1', 'wb') as fout:
        writer = PdfWriter()
        for page in pages:
            page.scale(0.05, 0.05)
            writer.add_page(page)
            writer.write(fout)


def split_pdf(filename: str, ranges: list) -> None:
    '''Splits file'''
    '''On frontend I should create an array of ranges'''

    file = PdfReader(filename)
    for num, page_range in enumerate(ranges):
        with open(f'{filename[0:-4]}_{num}.pdf', 'wb') as fout:
            writer = PdfWriter()
            for page in page_range:
                try:
                    writer.add_page(file.pages[page - 1])
                except IndexError:
                    print('Out of range.')
                writer.write(fout)


def merge_pdf(filenames: list) -> None:
    '''Merges given files'''
    '''TODO: figure out how to merge several files. Maybe it is possible by handling files as list of pages'''

    with open('Merged_files.pdf', 'wb') as fout:
        writer = PdfWriter()
        for filename in filenames:
            file = PdfReader(filename)
            writer.append(file)
        writer.write(fout)


def organize_pdf() -> None:
    pass
