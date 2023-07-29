from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Sentence
from .services import test_service
from django.core import serializers
from pprint import pp
from django.shortcuts import redirect
from .forms import NameForm
from django.conf import settings
from .services.session_service import SessionService

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def start_test(request):
    qset = Sentence.objects.get_sentences_for_test()

    sessionService = SessionService(request.session)
    sessionService.set_sentences(qset)

    return redirect("main:test")

def test(request):

    # get sentence
    current_index = request.session[Config.SESSION_CURRENT_INDEX]
    sentence = request.session[Config.SESSION_SENTENCES][current_index]

    form = NameForm()

    # show one question
    return render(request, 'main/test.html', {
        "sentence": sentence,
        "current_index": current_index,
        "form": form,
    })

def next(request):

    form = NameForm(request.POST, request.FILES)

    if form.is_valid():
        handle_uploaded_file(request.FILES["recording"])
        # get sentence
        current_index = request.session[Config.SESSION_CURRENT_INDEX]
        sentence = request.session[Config.SESSION_SENTENCES][current_index]

        # update session
        sentence["sound_path"] = form.cleaned_data['your_name']
        request.session[Config.SESSION_SENTENCES][request.session[Config.SESSION_CURRENT_INDEX]] = sentence
        request.session[Config.SESSION_CURRENT_INDEX] += 1
        request.session.modified = True

    return redirect("main:test")

def result(request):
    results = request.session[Config.SESSION_SENTENCES]
    return render(request, 'main/result.html', {"results": results})

class Config():
    SESSION_CURRENT_INDEX = "current_sentence_index"
    SESSION_SENTENCES = "sentences"

def handle_uploaded_file(f):
    path =  f"{settings.BASE_DIR}/main/static/sound.wav"
    with open(path, "wb+") as destination:
        for chunk in f.chunks():
            destination.write(chunk)


