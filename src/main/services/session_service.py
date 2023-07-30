"""
This is a class to deal with session used in test.
"""


class SessionService:
    SENTENCES_KEY = "sentences"
    CURRENT_INDEX_KEY = "current_index"

    def __init__(self, session):
        self.session = session

    def set_sentences(self, qset):
        sentences = [
            {
                "id": sentence.id,
                "sentence": sentence.sentence,
                "pronunciation_sound_url": sentence.pronunciation_sound_url,
                "sound_path": "",
            }
            for sentence in qset
        ]

        # save ids in session
        self.session[self.SENTENCES_KEY] = sentences
        self.session[self.CURRENT_INDEX_KEY] = 0

    def set_index(self, index):
        self.session[self.CURRENT_INDEX_KEY] = index

    def set_sentence(self, index, sentence):
        self.session[self.SENTENCES_KEY][index] = sentence
        self.session.modified = True

    def get_sentence_info(self):
        index = self.session[self.CURRENT_INDEX_KEY]
        sentence = self.session[self.SENTENCES_KEY][index]
        return (index, sentence)
