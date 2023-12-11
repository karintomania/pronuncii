from pathlib import Path
from typing import Optional
from django.conf import settings

class Sentence:
    def __init__(
        self, sentence: str,
        sound_url: str,
        file_path: Optional[Path]=None,
        is_answered: bool=False,
        answer: str=""
    ):
        self.sentence = sentence
        self.sound_url = sound_url
        self.file_path = file_path
        self.is_answered = is_answered
        self.answer = answer

    def to_dict(self) -> dict:
        return {
            "sentence": self.sentence,
            "sound_url": self.sound_url,
            "file_path": str(self.file_path),
            "is_answered": self.is_answered,
            "answer": self.answer,
        }

    def get_uri(self) -> str:
        base_path = Path(settings.BASE_DIR)
        file_path = self.file_path
        relative_path = file_path.relative_to(base_path)
        return str(relative_path)

    uri = property(get_uri)

    @classmethod
    def from_dict(cls, q_dict):
        return cls(
            sentence=q_dict["sentence"],
            sound_url=q_dict["sound_url"],
            file_path=Path(q_dict["file_path"]),
            is_answered=q_dict["is_answered"],
            answer=q_dict["answer"],
        )

    def __str__(self):
        return f"{{ sentence: {self.sentence}, sound_url: {self.sound_url}, file_path: {self.file_path}, is_answered: {self.is_answered}, answer: {self.answer}}}"
