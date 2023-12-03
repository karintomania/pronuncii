from pathlib import Path
import os
from django.core.files.uploadedfile import UploadedFile
from django.conf import settings


def save_file(file: UploadedFile, file_path: Path) -> Path:
    folder_path = file_path.parent

    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    with open(file_path, "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return file_path


def generate_file_path(session_key: str, index: int) -> Path:
    str_path = (
        f"{settings.RECORDING_FILE_DIR_PATH}{session_key}/recording{index:02}.ogg"
    )

    print(str_path)
    path = Path(str_path)

    return path


def remove_folder(session_id):
    print(session_id)
