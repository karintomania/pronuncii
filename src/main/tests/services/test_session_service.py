from datetime import datetime
from unittest import TestCase
from main.services.assessment.sentence import Sentence
from main.services.session_service import SessionService
from main.services.assessment.assessment import Assessment


# run test: python manage.py test main.tests.test_session_service
class SessionServiceTest(TestCase):
    def test_get_set_assessment(self) -> None:
        session_service = self.get_mocked_session_service()

        assessment = Assessment()
        sentence1 = Sentence(
            "sentence1", "http://example.com/test1.mp3", "some/path/test1.mp3", True
        )
        sentence2 = Sentence(
            "sentence2", "http://example.com/test2.mp3", "some/path/test2.mp3", False
        )

        assessment.add_sentence(sentence1)
        assessment.add_sentence(sentence2)

        session_service.set_assessment(assessment)
        result_assessment = session_service.get_assessment()
        res = result_assessment.get_sentences()

        self.assertEqual(sentence1.to_dict(), res[0].to_dict())
        self.assertEqual(sentence2.to_dict(), res[1].to_dict())

    def test_reset_session(self) -> None:
        session_service = self.get_mocked_session_service()

        session_service.reset_session()

        assessment = session_service.get_assessment()
        index = session_service.get_index()

        self.assertEqual(None, assessment)
        self.assertEqual(0, index)

    def test_has_assessment(self) -> None:
        session_service = self.get_mocked_session_service()

        self.assertFalse(session_service.has_assessment())
        assessment = Assessment()
        session_service.set_assessment(assessment)

        self.assertTrue(session_service.has_assessment())

    def test_get_set_index(self) -> None:
        session_service = self.get_mocked_session_service()

        index = 5
        session_service.set_index(index)

        self.assertEqual(index, session_service.get_index())

    def get_mocked_session_service(self) -> SessionService:
        # give dictionary instead of real session
        mocked_session = SessionService({})
        return mocked_session

    def test_get_set_recording_expire_date(self) -> None:
        session_service = self.get_mocked_session_service()

        expires_at = datetime.now()
        session_service.set_recording_expire_date(expires_at)

        self.assertEqual(expires_at, session_service.get_recording_expire_date())
