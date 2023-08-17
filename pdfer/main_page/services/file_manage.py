from os import mkdir, listdir
from pathlib import Path
from zipfile import ZipFile
from datetime import datetime
from django.conf import settings


def tmp_storage_init() -> Path:
    '''Saves the given file, creates directories and returns PosixPath'''

    tmp_dir_path = settings.MEDIA_ROOT / 'pdfs' / \
        f'pages_{datetime.now().time().isoformat("seconds")}'

    mkdir(tmp_dir_path)
    mkdir(tmp_dir_path / 'uploaded_files')
    mkdir(tmp_dir_path / 'compressed_files')
    mkdir(tmp_dir_path / 'pdf')
    mkdir(tmp_dir_path / 'jpg')

    return tmp_dir_path


def generate_result_file(files_cnt: int, result_files: Path):
    compressed_files = listdir(result_files)
    if files_cnt > 1:
        result_file_path = result_files.parent / 'compressed.zip'
        with ZipFile(result_file_path, 'w') as archive:
            for file in compressed_files:
                archive.write(result_files / file, arcname=file)
    else:
        result_file_path = result_files / compressed_files[0]
    return result_file_path
