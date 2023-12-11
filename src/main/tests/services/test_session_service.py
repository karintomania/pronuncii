from unittest import TestCase
from main.models import Sentence as SentenceModel
from main.services.assessment.sentence import Sentence
from main.services.session_service import SessionService
from main.services.assessment.assessment import Assessment
from pprint import pp


# run test: python manage.py test main.tests.test_session_service
class SessionServiceTest(TestCase):

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

        self.assertEquals(sentence1.to_dict(), res[0].to_dict())
        self.assertEquals(sentence2.to_dict(), res[1].to_dict())

    def test_reset_session(self) -> None:
        ss = self.get_mocked_session_service()

        ss.reset_session()

        assessment = ss.get_assessment()
        index = ss.get_index()

        self.assertEquals(None, assessment)
        self.assertEquals(0, index)

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
