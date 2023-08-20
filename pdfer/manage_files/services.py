from os import listdir
from pathlib import Path
from zipfile import ZipFile


def generate_result_file(result_path: Path) -> Path:
    compressed_files = listdir(result_path)
    if len(compressed_files) > 1:
        result_file_path = result_path / 'compressed.zip'
        with ZipFile(result_file_path, 'w') as archive:
            for file in compressed_files:
                archive.write(result_path / file, arcname=file)
    else:
        result_file_path = result_path / compressed_files[0]
    return result_file_path
