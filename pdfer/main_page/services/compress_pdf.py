import os
from shutil import rmtree
from pathlib import PosixPath
import tempfile
from PIL import Image
from datetime import datetime

from PyPDF2 import PdfReader, PdfWriter
from pdf2image.pdf2image import convert_from_path


def compress_file(path: PosixPath) -> PosixPath:
    '''Reduces file size converting a pdf pages to 
    jpg images, reducing their quality and then merging into one pdf file'''

    tmp_dir = path.parent / \
        f'pages_{datetime.now().time().isoformat("seconds")}'
    file_path = path

    os.mkdir(tmp_dir)
    os.mkdir(tmp_dir / 'pdf')
    os.mkdir(tmp_dir / 'jpg')

    pdf_to_img_compress(file_path, tmp_dir)
    comressed_name = jpg_to_pdf(file_path, tmp_dir)

    rmtree(tmp_dir)
    return comressed_name


def pdf_to_img_compress(file_path: PosixPath, tmp_dir: PosixPath) -> None:
    '''TODO: use split_pdf function to split files'''

    pdf_file = PdfReader(file_path)
    for num, page in enumerate(pdf_file.pages):
        temp_file = tmp_dir / f'pdf/{num}.pdf'
        with open(temp_file, 'wb') as fout:
            writer = PdfWriter()
            writer.add_page(page)
            writer.write(fout)

        with open(tmp_dir / f'jpg/{num}.jpg', 'wb') as jpg_fout:
            with tempfile.TemporaryDirectory() as tmp_path:
                page_image = convert_from_path(
                    temp_file, output_file=tmp_path, dpi=150, grayscale=True, paths_only=True)
                for image in page_image:
                    image.save(jpg_fout, optimize=True, quality=60)


def jpg_to_pdf(file_path: PosixPath, tmp_dir: PosixPath) -> PosixPath:
    pdf_path = file_path.parent / f'{file_path.stem}_compressed.pdf'
    jpgs_dir = tmp_dir / 'jpg'

    jpg_paths = [jpgs_dir / file for file in sorted(os.listdir(jpgs_dir))]
    Image.open(jpg_paths[0]).save(pdf_path, 'PDF', resolution=50.0,
                                  save_all=True, append_images=(Image.open(file)
                                                                for file in jpg_paths[1:]))
    return pdf_path
