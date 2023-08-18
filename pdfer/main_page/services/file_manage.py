from os import mkdir, listdir
from pathlib import Path
from zipfile import ZipFile
from datetime import datetime
from django.conf import settings


def tmp_storage_init() -> Path:
    '''Saves the given file, creates directories and returns PosixPath'''

    tmp_dir_name = f'pages_{datetime.now().time().isoformat("seconds")}'
    tmp_dir_path = settings.MEDIA_ROOT / tmp_dir_name
    folder_names = ['', 'uploaded_files', 'compressed_files', 'pdf', 'jpg']
    [mkdir(tmp_dir_path / path) for path in folder_names]

    return tmp_dir_path


def generate_result_file(result_files: Path):
    compressed_files = listdir(result_files)
    if len(compressed_files) > 1:
        result_file_path = result_files.parent / 'compressed.zip'
        with ZipFile(result_file_path, 'w') as archive:
            for file in compressed_files:
                archive.write(result_files / file, arcname=file)
    else:
        result_file_path = result_files / compressed_files[0]
    return result_file_path
