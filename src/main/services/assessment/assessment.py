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
