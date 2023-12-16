from unittest import TestCase
from pathlib import Path
from main.models import Sentence as SentenceModel
from main.services.assessment.sentence import Sentence
from main.services import whisper_service
from pprint import pp
from django.conf import settings


# run test: python manage.py test main.tests.test_session_service
class WhisperServiceTest(TestCase):

    def test_set_answer_sets_answer(self) -> None:

        # overwrite setting for testing purpose
        current_folder = Path(__file__).resolve().parent
        settings.RECORDING_FILE_DIR_PATH = str(current_folder) + "/"

        sentence = Sentence(
            sentence = "sentence",
            sound_url = "url",
            file_path = "Hello.ogg",
            is_answered = True,
            answer = "",
        )

        whisper_service.set_answers([sentence])
        self.assertEquals("Hello", sentence.answer)
