from datetime import datetime, timedelta
from pathlib import Path
from typing import List
from unittest.mock import Mock

from unittest import TestCase
from unittest.mock import patch
from django.conf import settings

from main.models import Sentence as SentenceModel

from main.services.assessment.sentence import Sentence
from main.services.assessment_service import AssessmentService

from main.services.session_service import SessionService


class AssessmentServiceTest(TestCase):
    mock_qset: List

    def setUp(self) -> None:
        # Overwrite the sentences count
        sentence_count = 2
        SentenceModel.objects.ASSESSMENT_SENTENCES_COUNT = sentence_count

        def make_mock_sentence(i: int) -> Mock:
            mock = Mock(spec=SentenceModel)
            mock.sentence = f"sentence{str(i)}"
            mock.url = f"http://example.com/{str(i)}"
            return mock

        self.mock_qset = [make_mock_sentence(i) for i in range(1, sentence_count + 1)]

        SentenceModel.objects.get_sentences_for_assessment = lambda: self.mock_qset

        return super().setUp()

    def test_init_sets_assessment_from_db(self) -> None:
        qset = self.mock_qset
        session_mock = {}
        assessment_service = AssessmentService(session_mock)

        assessment = assessment_service.assessment
        sentences = assessment.get_sentences()
        self.assertEqual(qset[0].sentence, sentences[0].sentence)
        self.assertEqual(qset[0].sound_url, sentences[0].sound_url)
        self.assertEqual("", sentences[0].file_path)
        self.assertEqual(False, sentences[0].is_answered)

        self.assertEqual(qset[1].sentence, sentences[1].sentence)
        self.assertEqual(qset[1].sound_url, sentences[1].sound_url)
        self.assertEqual("", sentences[1].file_path)
        self.assertEqual(False, sentences[1].is_answered)

        self.assertEqual(0, assessment_service.index)

    def test_init_sets_assessment_from_session(self) -> None:
        sentence1 = Sentence(
            "sentence1",
            "http://example.com/test1.mp3",
            Path(settings.RECORDING_FILE_DIR_PATH + "some/path/test1.mp3"),
            True,
        )
        sentence2 = Sentence(
            "sentence2",
            "http://example.com/test2.mp3",
            Path(settings.RECORDING_FILE_DIR_PATH + "some/path/test2.mp3"),
            True,
        )
        # set sentence to session
        session_mock = {
            SessionService.ASSESSMENT_KEY: [sentence1.to_dict(), sentence2.to_dict()],
            SessionService.CURRENT_INDEX_KEY: 3,
        }
        assessment_service = AssessmentService(session_mock)

        assessment = assessment_service.assessment
        sentences = assessment.get_sentences()

        self.assertEqual(sentence1.sentence, sentences[0].sentence)
        self.assertEqual(sentence1.sound_url, sentences[0].sound_url)
        self.assertEqual(sentence1.file_path, sentences[0].file_path)
        self.assertEqual(sentence1.is_answered, sentences[0].is_answered)
        self.assertEqual("static/recordings/some/path/test1.mp3", sentences[0].uri)

        self.assertEqual(sentence2.sentence, sentences[1].sentence)
        self.assertEqual(sentence2.sound_url, sentences[1].sound_url)
        self.assertEqual(sentence2.file_path, sentences[1].file_path)
        self.assertEqual(sentence2.is_answered, sentences[1].is_answered)
        self.assertEqual("static/recordings/some/path/test2.mp3", sentences[1].uri)

        self.assertEqual(
            assessment_service.index, session_mock.get(SessionService.CURRENT_INDEX_KEY)
        )

    def test_get_current_index(self):
        current_index = 1
        sentence1 = Sentence(
            "sentence1", "http://example.com/test1.mp3", "some/path/test1.mp3", True
        )
        sentence2 = Sentence(
            "sentence2", "http://example.com/test2.mp3", "some/path/test2.mp3", True
        )
        # set sentence to session
        session_mock = {
            SessionService.ASSESSMENT_KEY: [sentence1.to_dict(), sentence2.to_dict()],
            SessionService.CURRENT_INDEX_KEY: current_index,
        }

        assessment_service = AssessmentService(session_mock)

        result = assessment_service.get_current_index()
        self.assertEqual(current_index, result)

    def test_get_current_sentence(self):
        current_index = 1
        sentence1 = Sentence(
            "sentence1", "http://example.com/test1.mp3", "some/path/test1.mp3", True
        )
        sentence2 = Sentence(
            "sentence2", "http://example.com/test2.mp3", "some/path/test2.mp3", True
        )
        # set sentence to session
        session_mock = {
            SessionService.ASSESSMENT_KEY: [sentence1.to_dict(), sentence2.to_dict()],
            SessionService.CURRENT_INDEX_KEY: current_index,
        }

        assessment_service = AssessmentService(session_mock)

        result = assessment_service.get_current_sentence()
        self.assertEqual(sentence2.sentence, result.sentence)

    def test_add_file_path(self):
        current_index = 1
        sentence1 = Sentence(
            "sentence1", "http://example.com/test1.mp3", "some/path/test1.mp3", True
        )
        sentence2 = Sentence("sentence2", "http://example.com/test2.mp3", "", False)
        session_mock = {
            SessionService.ASSESSMENT_KEY: [sentence1.to_dict(), sentence2.to_dict()],
            SessionService.CURRENT_INDEX_KEY: current_index,
        }

        assessment_service = AssessmentService(session_mock)

        file_path_str = settings.RECORDING_FILE_DIR_PATH + "/tests/test2.mp3"
        file_path = Path(file_path_str)

        assessment_service.add_file_path(file_path)

        sentence = assessment_service.get_current_sentence()

        self.assertEqual(file_path, sentence.file_path)
        self.assertEqual("static/recordings/tests/test2.mp3", sentence.uri)
        self.assertTrue(sentence.is_answered)

    def test_reset_assessment(self):
        current_index = 1
        sentence1 = Sentence(
            "sentence1",
            "http://example.com/test1.mp3",
            Path("some/path/test1.mp3"),
            True,
        )
        # set sentence to session
        session_mock = {
            SessionService.ASSESSMENT_KEY: [sentence1.to_dict()],
            SessionService.CURRENT_INDEX_KEY: current_index,
        }

        assessment_service = AssessmentService(session_mock)

        assessment_service.reset_assessment()
        session_service = assessment_service.session_service
        self.assertEqual(None, session_service.get_assessment())
        self.assertEqual(0, session_service.get_index())

    def test_finish_assessment(self):
        current_index = 1
        sentence1 = Sentence(
            "sentence1",
            "http://example.com/test1.mp3",
            Path("some/path/test1.mp3"),
            True,
        )
        # set sentence to session
        session_mock = {
            SessionService.ASSESSMENT_KEY: [sentence1.to_dict()],
            SessionService.CURRENT_INDEX_KEY: current_index,
        }
        settings.RECORDING_SAVE_MINUTES = 30
        mocked_now = datetime(2023, 2, 1, 0, 10, 20)
        expected_expire_date = mocked_now + timedelta(
            minutes=settings.RECORDING_SAVE_MINUTES
        )
        with patch("main.services.assessment_service.datetime") as mock_datetime:
            mock_datetime.now.return_value = mocked_now
            assessment_service = AssessmentService(session_mock)
            assessment_service.finish_assessment()

        session_service = assessment_service.session_service
        self.assertEqual(None, session_service.get_assessment())
        self.assertEqual(0, session_service.get_index())
        self.assertEqual(
            expected_expire_date, session_service.get_recording_expire_date()
        )
