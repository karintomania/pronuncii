from unittest import TestCase
from main.models import Sentence as SentenceModel
from main.services.assessment.sentence import Sentence
from main.services.session_service import SessionService
from main.services.assessment.assessment import Assessment
from main.services.assessment.sentence import Sentence
from pprint import pp


# run test: python manage.py test main.tests.test_session_service
class SessionServiceTest(TestCase):
    def test_set_sentence(self) -> None:
        mockQset = [
            SentenceModel(sentence="test 1", pronunciation_sound_url="url1"),
            SentenceModel(sentence="test 2", pronunciation_sound_url="url2"),
            SentenceModel(sentence="test 3", pronunciation_sound_url="url3"),
            SentenceModel(sentence="test 4", pronunciation_sound_url="url4"),
            SentenceModel(sentence="test 5", pronunciation_sound_url="url5"),
        ]
        ss = self.get_mocked_session_service()
        ss.set_sentences(mockQset)

        for i in range(5):
            index, sentence = ss.get_sentence_info()
            self.assertEquals(i, index)
            self.assertEquals(mockQset[i].sentence, sentence["sentence"])
            self.assertEquals(
                mockQset[i].pronunciation_sound_url, sentence["pronunciation_sound_url"]
            )
            ss.set_index(i + 1)

    def test_get_set_assessment(self) -> None:
        ss = self.get_mocked_session_service()

        assessment = Assessment()
        sentence1 = Sentence(
            "sentence1", "http://example.com/test1.mp3", "some/path/test1.mp3", True
        )
        sentence2 = Sentence(
            "sentence2", "http://example.com/test2.mp3", "some/path/test2.mp3", False
        )

        assessment.add_sentence(sentence1)
        assessment.add_sentence(sentence2)

        ss.set_assessment(assessment)
        result_assessment = ss.get_assessment()
        res = result_assessment.get_sentences()

        self.assertEquals(sentence1.__dict__(), res[0].__dict__())
        self.assertEquals(sentence2.__dict__(), res[1].__dict__())

    def test_has_assessment(self) -> None:
        ss = self.get_mocked_session_service()

        self.assertFalse(ss.has_assessment())
        assessment = Assessment()
        ss.set_assessment(assessment)

        self.assertTrue(ss.has_assessment())

    def test_get_set_index(self) -> None:
        ss = self.get_mocked_session_service()

        index = 5
        ss.set_index(index)

        self.assertEquals(index, ss.get_index())

    def get_mocked_session_service(self) -> SessionService:
        # give dictionary instead of real session
        mockedSession = SessionService({})
        return mockedSession
