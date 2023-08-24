from django.contrib.sessions.backends.db import SessionStore
from pronuncii import settings
import tempfile
import os


def save_file(file, session_key, index):
    name = "recording{:02}.jpg".format(index)
    path = f"{settings.BASE_DIR}/{session_key}/main/static/{name}.wav"

    temp_dir = os.path.join(tempfile.gettempdir(), session_key)

    if not os.path.exists(temp_dir):
        os.makedirs(temp_dir)

    file_path = os.path.join(temp_dir, name)
    with open(file_path, "wb+") as destination:
        for chunk in file.chunks():
            destination.write(chunk)

    return path


def remove_folder(sessionId):
    print(sessionId)
