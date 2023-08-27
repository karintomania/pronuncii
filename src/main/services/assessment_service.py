from main.models import Sentence as SentenceModel
from main.services.assessment.assessment import Assessment
from main.services.assessment.sentence import Sentence
from main.services.session_service import SessionService


class AssessmentService:
    def __init__(self, session):
        self.session_service = SessionService(session)

        if self.session_service.has_assessment():
            self.assessment = self.session_service.get_assessment()
            self.index = self.session_service.get_index()

        else:
            qset = SentenceModel.objects.get_sentences_for_test()
            self.assessment = Assessment.from_qset(qset)
            self.session_service.set_assessment(self.assessment)

            self.index = 0
            self.session_service.set_index(self.index)

    def get_current_index(self):
        return self.index

    def get_current_sentence(self) -> Sentence:
        sentences = self.assessment.get_sentences()
        sentence = sentences[self.index]
        return sentence

    def add_file_path(self, file_path):
        sentence = self.get_current_sentence()
        sentence.file_path = file_path
        sentence.is_answered = True

        self.session_service.set_assessment(self.assessment)
        index = self.session_service.get_index() + 1
        self.session_service.set_index(index)

    def finish_assessment(self):
        self.session_service.reset_session()
