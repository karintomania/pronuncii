from django.test import TestCase

from main.models import Sentence


# Create your tests here.
class SentenceTest(TestCase):
    def setUp(self) -> None:
        Sentence.objects.create(
            sentence="test 1",
            pronunciation_sound_url="url1",
        )
        Sentence.objects.create(
            sentence="test 2",
            pronunciation_sound_url="url2",
        )
        Sentence.objects.create(
            sentence="test 3",
            pronunciation_sound_url="url3",
        )
        Sentence.objects.create(
            sentence="test 4",
            pronunciation_sound_url="url4",
        )
        Sentence.objects.create(
            sentence="test 5",
            pronunciation_sound_url="url5",
        )
        Sentence.objects.create(
            sentence="test 6",
            pronunciation_sound_url="url6",
        )
        return super().setUp()

    def test_get_sentence_for_test(self) -> None:
        sentences = Sentence.objects.get_sentences_for_test()

        expectedSentencesCount = Sentence.objects.TEST_SENTENCES_COUNT
        # test if it retrieves 5 records
        self.assertEquals(expectedSentencesCount, len(sentences))
        idSet = set()
        for sentence in sentences:
            idSet.add(sentence.id)
        # test if the result doesn't contain duplicated records
        self.assertEquals(expectedSentencesCount, len(idSet))
