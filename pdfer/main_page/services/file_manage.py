from os import mkdir
from pathlib import Path
from datetime import datetime
from django.conf import settings


def store_files(files: dict) -> Path:
    '''Saves the given file, creates directories and returns PosixPath'''

    tmp_dir_path = settings.MEDIA_ROOT / 'pdfs' / \
        f'pages_{datetime.now().time().isoformat("seconds")}'

    mkdir(tmp_dir_path)
    mkdir(tmp_dir_path / 'uploaded_files')
    mkdir(tmp_dir_path / 'compressed_files')
    mkdir(tmp_dir_path / 'pdf')
    mkdir(tmp_dir_path / 'jpg')

    for file in files:
        upload_file_path = tmp_dir_path / 'uploaded_files' / file.name
        with open(upload_file_path, 'wb+') as f:
            for chunk in file.chunks():
                f.write(chunk)
    return tmp_dir_path
