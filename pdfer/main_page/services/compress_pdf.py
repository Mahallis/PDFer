import os
from pathlib import Path
from tempfile import TemporaryDirectory
from PIL import Image

from PyPDF2 import PdfReader, PdfWriter
from pdf2image.pdf2image import convert_from_path


def compress_pdf(form: dict, tmp_storage: Path) -> Path:
    '''Reduces file size converting a pdf pages to 
    jpg images, reducing their quality and then merging into one pdf file'''

    for file in form['file_field']:
        upload_file_path = tmp_storage / 'uploaded_files' / file.name
        with open(upload_file_path, 'wb+') as f:
            for chunk in file.chunks():
                f.write(chunk)
        pdf_to_img_compress(upload_file_path, form)
        jpg_to_pdf(upload_file_path, form)

    return tmp_storage / 'compressed_files'


def pdf_to_img_compress(file_path: Path, form: dict) -> None:
    '''TODO: use split_pdf function to split files'''

    pdf_dir = file_path.parent.parent / 'pdf'
    jpg_dir = file_path.parent.parent / 'jpg'

    pdf_file = PdfReader(file_path)
    for num, page in enumerate(pdf_file.pages):
        temp_pdf_file = pdf_dir / f'{num}.pdf'
        with open(temp_pdf_file, 'wb') as fout:
            writer = PdfWriter()
            writer.add_page(page)
            writer.write(fout)

        with open(jpg_dir / f'{num}.jpg', 'wb') as jpg_fout:
            with TemporaryDirectory() as tmp_path:
                page_image = convert_from_path(
                    temp_pdf_file,
                    output_file=tmp_path,
                    dpi=form['dpi'],
                    grayscale=form['is_grayscale'],
                    paths_only=True)
                for image in page_image:
                    image.save(
                        jpg_fout,
                        optimize=True,
                        quality=form['quality'])


def jpg_to_pdf(file_path: Path, form: dict) -> None:
    pdf_name = f'{file_path.stem}_compressed.pdf'
    pdf_path = file_path.parent.parent / 'compressed_files' / pdf_name
    jpgs_dir = file_path.parent.parent / 'jpg'

    jpg_paths = [jpgs_dir / file for file in sorted(os.listdir(jpgs_dir))]
    Image.open(jpg_paths[0]).save(pdf_path, 'PDF', resolution=form['resolution'],
                                  save_all=True, append_images=(Image.open(file)
                                                                for file in jpg_paths[1:]))
