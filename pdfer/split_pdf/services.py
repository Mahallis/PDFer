from pathlib import Path
from PyPDF2 import PdfReader, PdfWriter
from tempfile import TemporaryDirectory

from django.http import FileResponse
from manage_files.services import generate_result_file


def split_pdf_service(form: dict) -> FileResponse:
    '''Splits given file by range'''

    with TemporaryDirectory(dir='media/') as tmp_dir:

        file = form['file_field'][0]
        file_path = Path(tmp_dir, file.name)
        reader = PdfReader(file)
        pages = parse_pages(form['intervals'], len(reader.pages))

        for num, page in enumerate(pages):
            writer = PdfWriter()
            with open(file_path.parent / f'{file_path.stem}_{str(num)}.pdf', 'wb') as fout:
                writer.add_page(reader.pages[page])
                writer.write(fout)
        splitted_file_path = generate_result_file(Path(tmp_dir), 'splitted')

        file_response = FileResponse(
            open(splitted_file_path, 'rb'),
            as_attachment=True,
            filename=splitted_file_path.name)
        return file_response


def parse_pages(intervals: str, pages: int) -> list:
    result = [int(item.strip()) - 1 for item in intervals.split(',')
              if 0 < int(item.strip()) < pages]
    return result
