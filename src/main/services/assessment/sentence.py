class Sentence:
    def __init__(
        self, sentence, sound_url, file_path=None, is_answered=False, answer=""
    ):
        self.sentence = sentence
        self.sound_url = sound_url
        self.file_path = file_path
        self.is_answered = is_answered
        self.answer = answer

    def __dict__(self) -> dict:
        return {
            "sentence": self.sentence,
            "sound_url": self.sound_url,
            "file_path": self.file_path,
            "is_answered": self.is_answered,
            "answer": self.is_answered,
        }

    @classmethod
    def from_dict(cls, q_dict):
        return cls(
            sentence=q_dict["sentence"],
            sound_url=q_dict["sound_url"],
            file_path=q_dict["file_path"],
            is_answered=q_dict["is_answered"],
            answer=q_dict["answer"],
        )
