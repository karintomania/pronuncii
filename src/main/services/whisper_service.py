import whisper
from typing import List
from main.services.assessment.sentence import Sentence
from pathlib import Path
from django.conf import settings

def set_answers(sentences: List[Sentence]) -> None:
    model = whisper.load_model("tiny.en")
    for sentence in sentences:
        result = model.transcribe(str(sentence.file_path))
        sentence.answer = str(result['text'])

