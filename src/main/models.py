from django.db import models
from django.db.models.query import QuerySet


class SentenceManager(models.Manager):
    # number of the sentences for one assessment
    ASSESSMENT_SENTENCES_COUNT = 2

    def get_sentences_for_assessment(self) -> models.QuerySet:
        return self.all().only("id").order_by("?")[: self.ASSESSMENT_SENTENCES_COUNT]


class Sentence(models.Model):
    sentence = models.CharField(max_length=200)
    sound_url = models.CharField(max_length=1000)
    objects = SentenceManager()

    def __str__(self):
        return self.sentence
