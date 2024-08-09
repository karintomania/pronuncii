import os
from pathlib import Path
from typing import List

class RecordingCleaner():

    def __init__(self) -> None:
        pass

    def is_expired_recording(self, key: str) -> bool:

        return False

    def get_directories_in_path(self, path: str) -> List[str]:
        try:
            return [d for d in os.listdir(str(path)) if os.path.isdir(os.path.join(path, d))]
        except OSError as e:
            print(f"An error occurred: {e}")
            return []
