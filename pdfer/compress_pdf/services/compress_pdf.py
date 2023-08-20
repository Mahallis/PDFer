from os import mkdir
from pathlib import Path
from tempfile import TemporaryDirectory
from pdf2image.pdf2image import convert_from_path

from django.http import FileResponse
from django.conf import settings

from manage_files.services.manage_files import generate_result_file


def compress_pdf(form: dict) -> FileResponse:
    '''Reduces file size converting a pdf pages to 
    jpg images, reducing their quality and then merging into one pdf file'''

    with TemporaryDirectory(dir=settings.MEDIA_ROOT) as tmp_dir:
        uploaded_files = Path(tmp_dir) / 'uploaded_files'
        result_files = Path(tmp_dir) / 'result_files'
        [mkdir(path) for path in [uploaded_files, result_files]]

        for file in form['file_field']:
            upload_file_path = uploaded_files / file.name
            with open(upload_file_path, 'wb+') as f:
                for chunk in file.chunks():
                    f.write(chunk)
            pdf_to_img_compress(upload_file_path, form)

        result_file_path = generate_result_file(result_files)
        file_response = FileResponse(
            open(result_file_path, 'rb'),
            as_attachment=True,
            filename=result_file_path.name)
        return file_response


def pdf_to_img_compress(file_path: Path, form: dict) -> None:
    '''Converts pdf to jpg, compresses it and converts it back'''

    pdf_name = f'{file_path.stem}_compressed.pdf'
    pdf_path = file_path.parent.parent / 'result_files' / pdf_name
    with TemporaryDirectory() as tmp_path:
        page_image = convert_from_path(
            file_path,
            output_folder=tmp_path,
            dpi=form['dpi'],
            grayscale=form['is_grayscale'])
        page_image[0].save(pdf_path, 'PDF', quality=form['quality'],
                           save_all=True, append_images=page_image[1:])
