from django.db import models
from django.test import TestCase

from main.models import Sentence as SentenceModel
from main.models import SentenceManager

from main.services.assessment.sentence import Sentence
from main.services.assessment_service import AssessmentService
from pprint import pp

from main.services.session_service import SessionService


# Create your tests here.
class AssessmentServiceTest(TestCase):
    def setUp(self) -> None:
        # Overwrite the sentences count
        SentenceModel.objects.TEST_SENTENCES_COUNT = 2

        # Create mock function as random qset is hard to test
        def fake_get_sentences_for_test() -> models.QuerySet:
            return (
                SentenceModel.objects.all()
                .only("id")
                .order_by("id")[: SentenceModel.objects.TEST_SENTENCES_COUNT]
            )

        SentenceModel.objects.get_sentences_for_test = fake_get_sentences_for_test

        self.sentence_count = SentenceModel.objects.TEST_SENTENCES_COUNT
        sentence_count = self.sentence_count

        for i in range(sentence_count + 1):
            SentenceModel.objects.create(
                sentence=f"test {i+1}",
                pronunciation_sound_url=f"url{i+1}",
            )

        return super().setUp()

    def test_init_sets_assessment_from_db(self) -> None:
        qset = SentenceModel.objects.get_sentences_for_test()
        session_mock = {}
        assessment_service = AssessmentService(session_mock)

        assessment = assessment_service.assessment
        sentences = assessment.get_sentences()
        self.assertEqual(qset[0].sentence, sentences[0].sentence)
        self.assertEqual(
            qset[0].pronunciation_sound_url, sentences[0].pronunciation_sound_url
        )
        self.assertEqual("", sentences[0].file_path)
        self.assertEqual(False, sentences[0].is_answered)

        self.assertEqual(qset[1].sentence, sentences[1].sentence)
        self.assertEqual(
            qset[1].pronunciation_sound_url, sentences[1].pronunciation_sound_url
        )
        self.assertEqual("", sentences[1].file_path)
        self.assertEqual(False, sentences[1].is_answered)

    def test_init_sets_assessment_from_session(self) -> None:
        sentence1 = Sentence(
            "sentence1", "http://example.com/test1.mp3", "some/path/test1.mp3", True
        )
        sentence2 = Sentence(
            "sentence2", "http://example.com/test2.mp3", "some/path/test2.mp3", True
        )
        # set sentence to session
        session_mock = {
            SessionService.ASSESSMENT_KEY: [sentence1.__dict__(), sentence2.__dict__()]
        }
        assessment_service = AssessmentService(session_mock)

        assessment = assessment_service.assessment
        sentences = assessment.get_sentences()

        self.assertEqual(sentence1.sentence, sentences[0].sentence)
        self.assertEqual(
            sentence1.pronunciation_sound_url, sentences[0].pronunciation_sound_url
        )
        self.assertEqual(sentence1.file_path, sentences[0].file_path)
        self.assertEqual(sentence1.is_answered, sentences[0].is_answered)

        self.assertEqual(sentence2.sentence, sentences[1].sentence)
        self.assertEqual(
            sentence2.pronunciation_sound_url, sentences[1].pronunciation_sound_url
        )
        self.assertEqual(sentence2.file_path, sentences[1].file_path)
        self.assertEqual(sentence2.is_answered, sentences[1].is_answered)
