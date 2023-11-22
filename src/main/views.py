from django.shortcuts import render
from .models import Sentence
from django.shortcuts import redirect
from .forms import FileForm
from .services.recording_file_service import save_file, generate_file_path
from .services.assessment_service import AssessmentService
from .services.whisper_service import set_answers


# Create your views here.
def index(request):
    return render(request, "main/index.html")


def assessment(request):
    # get sentence
    assessment_service = AssessmentService(request.session)

    form = FileForm()

    # show one question
    return render(
        request,
        "main/assessment.html",
        {
            "sentence": assessment_service.get_current_sentence(),
            "current_index": assessment_service.get_current_index(),
            "sentence_count": Sentence.objects.ASSESSMENT_SENTENCES_COUNT,
            "form": form,
        },
    )


def next(request):
    is_success = save_recording(request)

    return redirect("main:assessment")


def finish_assessment(request):
    is_success = save_recording(request)

    return redirect("main:result")


def save_recording(request):
    form = FileForm(request.POST, request.FILES)

    if not form.is_valid():
        # TODO: validation handling
        return False

    assessment_service = AssessmentService(request.session)
    session_key = request.session.session_key
    index = assessment_service.get_current_index()
    file_path = generate_file_path(session_key, index)
    file_path = save_file(request.FILES["recording"], file_path)

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
