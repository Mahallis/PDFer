from os import remove
from pathlib import PosixPath
from django.conf import settings
from django.core.files import File


def save_file(file: File) -> PosixPath:
    '''Saves the given file and returns PosixPath'''
    file_path = settings.MEDIA_ROOT / 'pdfs' / file.name
    with open(file_path, 'wb+') as f:
        for chunk in file.chunks():
            f.write(chunk)
    return file_path


def delete_file(file_path: PosixPath) -> None:
    remove(file_path)
