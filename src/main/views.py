from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Sentence
from django.core import serializers
from pprint import pp
from django.shortcuts import redirect
from .forms import FileForm
from django.conf import settings
from .services.recording_file_service import save_file
from .services.session_service import SessionService
from .services.assessment_service import AssessmentService
from .services.whisper_service import set_answers


# Create your views here.
def index(request):

    return render(request, "main/index.html")


def test(request):
    # get sentence
    assessment_service = AssessmentService(request.session)

    form = FileForm()


    # show one question
    return render(
        request,
        "main/test.html",
        {
            "sentence": assessment_service.get_current_sentence(),
            "current_index": assessment_service.get_current_index(),
            "sentence_count": Sentence.objects.TEST_SENTENCES_COUNT,
            "form": form,
        },
    )


def next(request):
    is_success = save_recording(request)

    return redirect("main:test")


def finish_test(request):
    is_success = save_recording(request)

    return redirect("main:result")


def save_recording(request):
    form = FileForm(request.POST, request.FILES)

    if not form.is_valid():
        # TODO: validation handling
        return False

    assessment_service = AssessmentService(request.session)
    session_key = request.session.session_key
    file_path = save_file(
        request.FILES["recording"], session_key, assessment_service.get_current_index()
    )

    assessment_service.add_file_path(file_path)
    return True


def result(request):
    assessment_service = AssessmentService(request.session)
    sentences = assessment_service.assessment.get_sentences()

    set_answers(sentences)

    assessment_service.finish_assessment()
    return render(
        request,
        "main/result.html",
        {"results": sentences},
    )


