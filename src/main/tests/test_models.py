from django.test import TestCase

from main.models import Sentence


# Create your tests here.
class SentenceTest(TestCase):
    def setUp(self) -> None:
        sentence_count = Sentence.objects.TEST_SENTENCES_COUNT

        for i in range(sentence_count + 1):
            Sentence.objects.create(
                sentence=f"test {i+1}",
                pronunciation_sound_url=f"url{i+1}",
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
