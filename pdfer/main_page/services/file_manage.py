from os import remove


def save_file(file, media_path):
    file_path = media_path / file.name
    with open(file_path, 'wb+') as f:
        for chunk in file.chunks():
            f.write(chunk)
    return file_path


def delete_file(file_path):
    remove(file_path)
