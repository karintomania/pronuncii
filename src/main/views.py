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


# Create your views here.
def index(request):
    return render(request, "main/index.html")


def start_test(request):
    qset = Sentence.objects.get_sentences_for_test()

    sessionService = SessionService(request.session)
    sessionService.set_sentences(qset)

    return redirect("main:test")


def test(request):
    # get sentence
    sessionService = SessionService(request.session)
    current_index, sentence = sessionService.get_sentence_info()

    form = FileForm()

    # show one question
    return render(
        request,
        "main/test.html",
        {
            "sentence": sentence,
            "current_index": current_index,
            "sentence_count": Sentence.objects.TEST_SENTENCES_COUNT,
            "form": form,
        },
    )


def next(request):
    sessionService = SessionService(request.session)
    # get sentence
    currentIndex, sentence = sessionService.get_sentence_info()
    succeed = save_recording(request, sessionService.get_session_key(), currentIndex)
    if succeed:
        # update session
        sentence["sound_path"] = "file path"
        sessionService.set_sentence(currentIndex, sentence)
        sessionService.set_index(currentIndex + 1)

        return redirect("main:test")


def finish_test(request):
    return redirect("main:result")


def result(request):
    sessionService = SessionService(request.session)
    # currentIndex, sentence = sessionService.get_sentence_info()

    results = sessionService.get_sentences()

    return render(request, "main/result.html", {"results": results})


def handle_uploaded_file(f):
    path = f"{settings.BASE_DIR}/main/static/sound.wav"
    with open(path, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


def save_recording(request, sessionKey, currentIndex) -> bool:
    form = FileForm(request.POST, request.FILES)

    if not form.is_valid():
        return False

    # save the recording
    save_file(request.FILES["recording"], sessionKey, currentIndex)
    return True
