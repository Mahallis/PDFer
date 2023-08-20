from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter


def split_pdf(filename: Path, ranges: list) -> None:
    '''Splits file'''

    file = PdfReader(filename)
    for num, page_range in enumerate(ranges):
        with open(f'{filename.stem}_{num}.pdf', 'wb') as fout:
            writer = PdfWriter()
            for page in page_range:
                try:
                    writer.add_page(file.pages[page - 1])
                except IndexError:
                    print('Out of range.')
                writer.write(fout)
