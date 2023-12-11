from unittest import TestCase
from main.services.assessment.sentence import Sentence
from django.conf import settings

class SentenceTest(TestCase):

    def test_to_dict(self):
        sentence = Sentence(
            "Hello world!",
            "https://example.com/pronunciation.mp3",
            settings.BASE_DIR / "some/path/example.txt",
            True,
            "test answer",
        )
        expected = {
            "sentence": "Hello world!",
            "sound_url": "https://example.com/pronunciation.mp3",
            "file_path": str(settings.BASE_DIR / "some/path/example.txt"),
            "is_answered": True,
            "answer": "test answer",
        }

        self.assertEqual(expected, sentence.to_dict())

    def test_from_dict(self):
        relative_path = "some/path/example.txt"
        sentence_dict = {
            "sentence": "Hello world!",
            "sound_url": "https://example.com/pronunciation.mp3",
            "file_path": settings.BASE_DIR / relative_path,
            "is_answered": True,
            "answer": "test answer",
        }

        result = Sentence.from_dict(sentence_dict)

        self.assertEqual(sentence_dict["sentence"], result.sentence)
        self.assertEqual(sentence_dict["sound_url"], result.sound_url)
        self.assertEqual(sentence_dict["file_path"], result.file_path)
        self.assertEqual(sentence_dict["is_answered"], result.is_answered)
        self.assertEqual(sentence_dict["answer"], result.answer)
        self.assertEqual(relative_path, result.uri)
