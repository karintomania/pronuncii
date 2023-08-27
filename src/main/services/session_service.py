from typing import Union
from main.services.assessment.assessment import Assessment


class SessionService:
    CURRENT_INDEX_KEY = "current_index"
    ASSESSMENT_KEY = "assessment"

    def __init__(self, session):
        self.session = session

    def set_assessment(self, assessment: Assessment):
        dict_assessment = assessment.to_dict()
        self.session[self.ASSESSMENT_KEY] = dict_assessment

    def get_assessment(self) -> Union[Assessment, None]:
        dict_assessment = self.session[self.ASSESSMENT_KEY]
        if dict_assessment == None:
            return None
        return Assessment.from_dict(dict_assessment)

    def has_assessment(self) -> Assessment:
        return self.session.get(self.ASSESSMENT_KEY) != None

    def get_index(self) -> int:
        return self.session[self.CURRENT_INDEX_KEY]

    def set_index(self, index: int):
        self.session[self.CURRENT_INDEX_KEY] = index

    def reset_session(self) -> None:
        self.session[self.CURRENT_INDEX_KEY] = 0
        self.session[self.ASSESSMENT_KEY] = None
