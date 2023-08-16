from os import mkdir, remove
from pathlib import PosixPath
from datetime import datetime
from django.conf import settings
from django.core.files import File


def store_file(file: File) -> PosixPath:
    '''Saves the given file, creates directories and returns PosixPath'''

    tmp_dir_path = settings.MEDIA_ROOT / 'pdfs' / \
        f'pages_{datetime.now().time().isoformat("seconds")}'

    mkdir(tmp_dir_path)
    mkdir(tmp_dir_path / 'pdf')
    mkdir(tmp_dir_path / 'jpg')

    upload_file_path = tmp_dir_path / file.name
    with open(upload_file_path, 'wb+') as f:
        for chunk in file.chunks():
            f.write(chunk)
    return upload_file_path
