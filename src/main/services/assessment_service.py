from main.models import Sentence as SentenceModel
from main.services.assessment.assessment import Assessment
from main.services.session_service import SessionService


class AssessmentService():

    def __init__(self, session):
        self.session_service = SessionService(session)

        if self.session_service.has_assessment():
            self.assessment = self.session_service.get_assessment()
        else:
            qset = SentenceModel.objects.get_sentences_for_test()
            self.assessment = Assessment.from_qset(qset)
            self.session_service.set_assessment(self.assessment)


