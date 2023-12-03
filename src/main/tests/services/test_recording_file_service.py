import os
from pathlib import Path
from time import time
from unittest import TestCase
from unittest.mock import Mock

from django.core.files.uploadedfile import UploadedFile
from django.conf import settings
from main.services.recording_file_service import save_file, generate_file_path


class RecordingFileServiceTest(TestCase):
    def test_save_file_saves_file(self) -> None:
        file = Mock(state=UploadedFile)

        # mock the return value as bytes
        content = f"file content: {time()}"
        file.chunks.return_value = [bytes(content, encoding="utf-8")]

        current_folder = Path(__file__).resolve().parent
        path = Path(f"{current_folder}/test.txt")

        save_file(file, path)

        # test if file is created
        self.assertTrue(path.exists())

        with open(path, "r", encoding="utf-8") as file:
            result = file.read()
        # test if the content is correct
        self.assertEqual(content, result)

        try:
            # delete the file after the test
            os.remove(path)
        except OSError as err:
            print(f"Error on deletion of {path}: {err.strerror}.")

    def test_generate_file_path(self) -> None:
        session_key = "session_key"
        index = 1
        result = generate_file_path(session_key, index)

        expected = (
            f"{settings.RECORDING_FILE_DIR_PATH}{session_key}/recording{index:02}.ogg"
        )

        self.assertEqual(expected, result.__str__())
