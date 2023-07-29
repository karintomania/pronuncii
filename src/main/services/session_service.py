from main.models import Sentence

class SessionService:

    SENTENCES_KEY = 'sentences'
    CURRENT_INDEX_KEY = 'current_index'

    def __init__(self, session):
        self.session = session

    def set_sentences(self, qset):

        sentences = [{
            "id": sentence.id,
            "sentence": sentence.sentence,
            "pronunciation_sound_url": sentence.pronunciation_sound_url,
            "sound_path": ""
            } for sentence in qset]

        # save ids in session
        self.session[self.SENTENCES_KEY] = sentences
        self.session[self.CURRENT_INDEX_KEY] = 0

    def set_index(self, index):
        self.session[self.CURRENT_INDEX_KEY] = index

    def get_sentence_info(self):
        index = self.session[self.CURRENT_INDEX_KEY]
        sentence = self.session[self.SENTENCES_KEY][index]
        return (index, sentence)

