class Sentence:
    def __init__(
        self, sentence, pronunciation_sound_url, file_path=None, is_answered=False
    ):
        self.sentence = sentence
        self.pronunciation_sound_url = pronunciation_sound_url
        self.file_path = file_path
        self.is_answered = is_answered

    def __dict__(self) -> dict:
        return {
            "sentence": self.sentence,
            "pronunciation_sound_url": self.pronunciation_sound_url,
            "file_path": self.file_path,
            "is_answered": self.is_answered,
        }

    @classmethod
    def from_dict(cls, q_dict):
        return cls(
            sentence=q_dict["sentence"],
            pronunciation_sound_url=q_dict["pronunciation_sound_url"],
            file_path=q_dict["file_path"],
            is_answered=q_dict["is_answered"],
        )
