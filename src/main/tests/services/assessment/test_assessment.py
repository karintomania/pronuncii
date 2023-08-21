from unittest import TestCase
from main.services.assessment.sentence import Sentence
from main.services.assessment.assessment import Assessment
from pprint import pp


class AssessmentTest(TestCase):

    def test_get_sentences(self):
        assessment = Assessment()
        sentence1 = Sentence(
            "sentence1", "http://example.com/test1.mp3", "some/path/test1.mp3", True
        )
        sentence2 = Sentence(
            "sentence2", "http://example.com/test2.mp3", "some/path/test2.mp3", False
        )

        assessment.add_sentence(sentence1)
        assessment.add_sentence(sentence2)
        res = assessment.get_sentences()

        self.assertEqual(2, len(res))
        self.assertEqual(sentence1, res[0])
        self.assertEqual(sentence2, res[1])

    def test_add_sentences(self):
        assessment = Assessment()
        sentence = Sentence(
            "sentence", "http://example.com/test.mp3", "some/path/test.mp3", False
        )

        assessment.add_sentence(sentence)
        res = assessment.get_sentences()

        self.assertEqual(sentence, res[0])

    def test_to_dict(self):
        assessment = Assessment()
        sentence = Sentence(
            "sentence", "http://example.com/test.mp3", "some/path/test.mp3", False
        )
        assessment.add_sentence(sentence)
        assessment_dic = assessment.to_dict()

        expected = [
            {
                "sentence": "sentence",
                "pronunciation_sound_url": "http://example.com/test.mp3",
                "file_path": "some/path/test.mp3",
                "is_answered": False,
            }
        ]

        self.assertEqual(expected, assessment_dic)

    def test_from_dict(self):
        assessment_dic = [
            {
                "sentence": "sentence",
                "pronunciation_sound_url": "http://example.com/test.mp3",
                "file_path": "some/path/test.mp3",
                "is_answered": False,
            }
        ]
        res = Assessment.from_dict(assessment_dic)
        res_sentence = res.get_sentences()[0]
        expected_sentence = Sentence(
            "sentence", "http://example.com/test.mp3", "some/path/test.mp3", False
        )
        self.assertEqual(expected_sentence.sentence, res_sentence.sentence)
        self.assertEqual(
            expected_sentence.pronunciation_sound_url,
            res_sentence.pronunciation_sound_url,
        )
        self.assertEqual(expected_sentence.file_path, res_sentence.file_path)
        self.assertEqual(expected_sentence.is_answered, res_sentence.is_answered)
