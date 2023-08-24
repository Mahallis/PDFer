from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter
from tempfile import TemporaryDirectory
from re import match, split

from django.http import FileResponse
from manage_files.services import generate_result_file


def split_pdf_service(form: dict) -> FileResponse:
    '''Splits given file by range'''

    with TemporaryDirectory(dir='media/') as tmp_dir:

        file = form['file_field'][0]
        file_path = Path(tmp_dir, file.name)
        reader = PdfReader(file)
        intervals = prep_pages(form['intervals'], len(reader.pages))

        for num, interval in enumerate(intervals):
            writer = PdfWriter()
            with open(file_path.parent / f'{file_path.stem}_{str(num)}.pdf', 'wb') as fout:
                for page in interval:
                    writer.add_page(reader.pages[page])
                    writer.write(fout)
        splitted_file_path = generate_result_file(Path(tmp_dir), 'splitted')

        file_response = FileResponse(
            open(splitted_file_path, 'rb'),
            as_attachment=True,
            filename=splitted_file_path.name)
        return file_response


def prep_pages(intervals: str, pages: int) -> list:
    '''Prepares intervals for processing'''
    '''TODO: check in frontside for staying in ranges'''

    prepared = []
    for interval in split(r'[, ]', intervals):
        interval = interval.strip()
        if len(interval) == 1:
            if 0 < (interval := int(interval) - 1) < pages:
                prepared.append([interval])
        elif match(r'^\d+-\d+$', interval):
            min, max = [int(num) for num in interval.split('-')]
            prepared.append(range(min-1, max))
    return prepared
