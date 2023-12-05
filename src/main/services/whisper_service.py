from typing import List
from main.services.assessment.sentence import Sentence

def set_answers(sentences: List[Sentence]) -> None:

    for sentence in sentences:
        sentence.answer = "hello world 1"

