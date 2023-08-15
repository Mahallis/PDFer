import os
from shutil import rmtree
from pathlib import PosixPath
import tempfile
from PIL import Image
from datetime import datetime

from PyPDF2 import PdfReader, PdfWriter
from pdf2image.pdf2image import convert_from_path


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


def compress_pdf(filename: str, path: PosixPath) -> str:
    '''Reduces file size converting a pdf pages to 
    jpg images, reducing their quality and then merging into one pdf file'''

    tmp_dir = path / f'pages_{datetime.now().time().isoformat("seconds")}'
    file_path = path / filename

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


def jpg_to_pdf(file_path: PosixPath, tmp_dir: PosixPath) -> str:
    pdf_name = f'{file_path.name}_compressed.pdf'
    jpgs_dir = tmp_dir / 'jpg'

    jpg_paths = [jpgs_dir / file for file in sorted(os.listdir(jpgs_dir))]
    Image.open(jpg_paths[0]).save(pdf_name, 'PDF', resolution=50.0,
                                  save_all=True, append_images=(Image.open(file)
                                                                for file in jpg_paths[1:]))
    return pdf_name


def organize_pdf() -> None:
    pass
