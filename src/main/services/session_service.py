"""
This is a class to deal with session used in test.
"""


from main.services.assessment.assessment import Assessment


class SessionService:
    SENTENCES_KEY = "sentences"
    CURRENT_INDEX_KEY = "current_index"
    ASSESSMENT_KEY = "assessment"

    def __init__(self, session):
        self.session = session

    def set_assessment(self, assessment: Assessment):
        dict_assessment = assessment.to_dict()
        self.session[self.ASSESSMENT_KEY] = dict_assessment

    def get_assessment(self) -> Assessment:
        dict_assessment = self.session[self.ASSESSMENT_KEY]
        return Assessment.from_dict(dict_assessment)

    def has_assessment(self) -> Assessment:
        return self.session.get(self.ASSESSMENT_KEY) != None

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

    def get_index(self) -> int:
        return self.session[self.CURRENT_INDEX_KEY]

    def set_index(self, index: int):
        self.session[self.CURRENT_INDEX_KEY] = index

    def set_sentence(self, index, sentence):
        self.session[self.SENTENCES_KEY][index] = sentence
        self.session.modified = True

    def get_sentence_info(self):
        index = self.session[self.CURRENT_INDEX_KEY]
        sentence = self.session[self.SENTENCES_KEY][index]
        return (index, sentence)

    def get_sentences(self):
        return self.session[self.SENTENCES_KEY]

    def get_session_key(self):
        return self.session.session_key
