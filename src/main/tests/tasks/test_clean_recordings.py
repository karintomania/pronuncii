from pathlib import Path
from unittest import TestCase

from main.tasks.clean_recordings import get_directories_in_path


# Create your tests here.
class CleanRecordingsTest(TestCase):
    def test_clean_recordings(self) -> None:

        dirs = get_directories_in_path("/app/static/recordings/")
        print(dirs)
