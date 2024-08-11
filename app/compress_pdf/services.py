from zipfile import ZipFile
from pathlib import Path
from tempfile import TemporaryDirectory

from django.core.files.base import File
from django.http import FileResponse
from pdf2image.pdf2image import convert_from_bytes


def compress_pdf(form: dict) -> FileResponse:
    '''Reduces file size converting a pdf pages to
    jpg images, reducing their quality and then merging into one pdf file'''

    with TemporaryDirectory(dir='/media/') as tmp_dir:
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

    pdf_path = file_path / f'{file.name[0:-4]}_compressed.pdf'
    page_image = convert_from_bytes(file.read(),
                                    dpi=form['dpi'],
                                    grayscale=form['is_grayscale'])
    page_image[0].save(pdf_path, 'PDF', quality=form['quality'],
                       save_all=True, append_images=page_image[1:])


def generate_result_file(result_path: Path, name: str) -> Path:
    '''Return a path to a compressed file if single file was
    uploaded or to an archive if multiple'''

    compressed_files = [file for file in result_path.glob('*.pdf')]
    if len(compressed_files) > 1:
        result_file_path = result_path / f'{name}.zip'
        with ZipFile(result_file_path, 'w') as archive:
            for file in compressed_files:
                archive.write(file, arcname=file.name)
    else:
        result_file_path = compressed_files[0]
    return result_file_path
