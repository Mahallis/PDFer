from pathlib import Path
from PyPDF2 import PdfWriter, PdfReader
from tempfile import TemporaryDirectory

from django.http import FileResponse


def merge_pdf_service(files: dict) -> FileResponse:
    '''Merges given files'''

    with TemporaryDirectory(dir='media/') as tmp_dir:
        result_path = Path(tmp_dir, 'merged_file.pdf')
        writer = PdfWriter()
        with open(result_path, 'wb') as fout:
            for file in files['file_field']:
                pdf_file = PdfReader(file)
                writer.append(pdf_file)
            writer.write(fout)

        file_response = FileResponse(
            open(result_path, 'rb'),
            as_attachment=True,
            filename=result_path.name)
        return file_response
