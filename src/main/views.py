from django.shortcuts import render
from django.http import HttpResponse
from .models import Sentence

# Create your views here.
def index(request):
    return render(request, 'main/index.html')

def test(request):
    sentences = Sentence.objects.get_sentences_for_test()
    return render(request, 'main/test.html', {"sentences": sentences})

def result(request):
    return render(request, 'main/result.html')
