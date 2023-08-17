import os
from pathlib import Path
import tempfile
from PIL import Image

from PyPDF2 import PdfReader, PdfWriter
from pdf2image.pdf2image import convert_from_path


def compress_file(file_path: Path, comp_params: dict) -> Path:
    '''Reduces file size converting a pdf pages to 
    jpg images, reducing their quality and then merging into one pdf file'''

    pdf_to_img_compress(file_path, comp_params)
    comressed_name = jpg_to_pdf(file_path, comp_params)

    return comressed_name


def pdf_to_img_compress(file_path: Path, comp_params: dict) -> None:
    '''TODO: use split_pdf function to split files'''

    pdf_file = PdfReader(file_path)
    for num, page in enumerate(pdf_file.pages):
        temp_pdf_file = file_path.parent.parent / f'pdf/{num}.pdf'
        with open(temp_pdf_file, 'wb') as fout:
            writer = PdfWriter()
            writer.add_page(page)
            writer.write(fout)

        with open(file_path.parent.parent / f'jpg/{num}.jpg', 'wb') as jpg_fout:
            with tempfile.TemporaryDirectory() as tmp_path:
                page_image = convert_from_path(
                    temp_pdf_file,
                    output_file=tmp_path,
                    dpi=comp_params['dpi'],
                    grayscale=comp_params['is_grayscale'],
                    paths_only=True)
                for image in page_image:
                    image.save(
                        jpg_fout,
                        optimize=True,
                        quality=comp_params['quality'])


def jpg_to_pdf(file_path: Path, comp_params: dict) -> Path:
    pdf_path = file_path.parent.parent / 'compressed_files' / \
        f'{file_path.stem}_compressed.pdf'
    jpgs_dir = file_path.parent.parent / 'jpg'

    jpg_paths = [jpgs_dir / file for file in sorted(os.listdir(jpgs_dir))]
    Image.open(jpg_paths[0]).save(pdf_path, 'PDF', resolution=comp_params['resolution'],
                                  save_all=True, append_images=(Image.open(file)
                                                                for file in jpg_paths[1:]))
    return pdf_path
