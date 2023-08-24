from main.services.assessment.assessment import Assessment


class SessionService:
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


    def get_index(self) -> int:
        return self.session[self.CURRENT_INDEX_KEY]

    def set_index(self, index: int):
        self.session[self.CURRENT_INDEX_KEY] = index

