from django.shortcuts import render
from django.http import HttpResponse
import json
from .models import Sentence
from .services import test_service
from django.core import serializers
from pprint import pp
from django.shortcuts import redirect

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def start_test(request):

    # get sentences
    qset = Sentence.objects.get_sentences_for_test()
    sentences = [{
        "id": sentence.id,
        "sentence": sentence.sentence,
        "pronunciation_sound_url": sentence.pronunciation_sound_url,
        "sound_path": ""
        } for sentence in qset]

    # save ids in session
    request.session[Config.SESSION_SENTENCES] = sentences
    request.session[Config.SESSION_CURRENT_INDEX] = 0

    # redirect to test page
    return redirect("main:test")

def test(request):

    # get sentence
    current_index = request.session[Config.SESSION_CURRENT_INDEX]
    sentence = request.session[Config.SESSION_SENTENCES][current_index]

    # show one question
    return render(request, 'main/test.html', {
        "sentence": sentence,
        "current_index": current_index,
    })

def next(request):

    # get sentence
    current_index = request.session[Config.SESSION_CURRENT_INDEX]
    sentence = request.session[Config.SESSION_SENTENCES][current_index]

    # update session
    sentence["sound_path"] = "sound_path"
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
