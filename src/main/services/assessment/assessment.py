from main.models import Sentence as SentenceModel
from .sentence import Sentence


class Assessment:
    def __init__(self):
        self.sentences = []

    def get_sentences(self):
        return self.sentences

    def add_sentence(self, sentence):
        self.sentences.append(sentence)

    def to_dict(self):
        return [sentence.__dict__() for sentence in self.sentences]

    @classmethod
    def from_dict(cls, sentences_dic):
        assessment = cls()
        assessment.sentences = [
            Sentence.from_dict(sentence_dict) for sentence_dict in sentences_dic
        ]
        return assessment

    @classmethod
    def from_qset(cls, qset):
        assessment = cls()

        assessment.sentences = [
            Sentence(
                sentence=sentence_model.sentence,
                pronunciation_sound_url=sentence_model.pronunciation_sound_url,
                file_path="",
                is_answered=False,
            )
            for sentence_model in qset
        ]
        return assessment
