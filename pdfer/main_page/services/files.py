def save_file(file, path):
    with open(path / file.name, 'wb+') as f:
        for chunk in file.chunks():
            f.write(chunk)
