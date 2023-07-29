from unittest import TestCase
from main.models import Sentence
from main.services.session_service import SessionService
from pprint import pp


# run test: python manage.py test main.tests.test_session_service
class SessionServiceTest(TestCase):
    # def setUp(self) -> None:
    #     return super().setUp()

    def test_set_sentence(self) -> None:
        mockQset = [
            Sentence(sentence="test 1", pronunciation_sound_url="url1"),
            Sentence(sentence="test 2", pronunciation_sound_url="url2"),
            Sentence(sentence="test 3", pronunciation_sound_url="url3"),
            Sentence(sentence="test 4", pronunciation_sound_url="url4"),
            Sentence(sentence="test 5", pronunciation_sound_url="url5"),
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

    def get_mocked_session_service(self) -> SessionService:
        # give dictionary instead of real session
        mockedSession = SessionService({})
        return mockedSession
