from pathlib import Path
from zipfile import ZipFile


def generate_result_file(result_path: Path, name: str) -> Path:
    compressed_files = [file for file in result_path.glob('*.pdf')]
    if len(compressed_files) > 1:
        result_file_path = result_path / f'{name}.zip'
        with ZipFile(result_file_path, 'w') as archive:
            for file in compressed_files:
                archive.write(file, arcname=file.name)
    else:
        result_file_path = compressed_files[0]
    return result_file_path
