from pathlib import Path
from tempfile import TemporaryDirectory

from django.core.files.base import File
from django.http import FileResponse

from pdf2image.pdf2image import convert_from_bytes
from manage_files.services import generate_result_file


def compress_pdf(form: dict) -> FileResponse:
    '''Reduces file size converting a pdf pages to 
    jpg images, reducing their quality and then merging into one pdf file'''

    with TemporaryDirectory(dir='media/') as tmp_dir:
        for file in form['file_field']:
            pdf_to_img_compress(Path(tmp_dir), form, file)

        compressed_file_path = generate_result_file(
            Path(tmp_dir), 'compressed')
        file_response = FileResponse(
            open(compressed_file_path, 'rb'),
            as_attachment=True,
            filename=compressed_file_path.name)
        return file_response


def pdf_to_img_compress(file_path: Path, form: dict, file: File) -> None:
    '''Converts pdf to jpg, compresses it and converts it back'''

    # Did this to remove file extension
    pdf_path = file_path / f'{file.name[0:-4]}_compressed.pdf'
    page_image = convert_from_bytes(file.read(),
                                    dpi=form['dpi'],
                                    grayscale=form['is_grayscale'])
    page_image[0].save(pdf_path, 'PDF', quality=form['quality'],
                       save_all=True, append_images=page_image[1:])
