from django.db import models
from django.db.models.query import QuerySet


class SentenceManager(models.Manager):
    def get_sentences_for_test(self) -> models.QuerySet:
        return self.all().only('id').order_by("?")[:5]

class Sentence(models.Model):
    sentence = models.CharField(max_length=200)
    pronunciation_sound_url = models.CharField(max_length=1000)
    objects = SentenceManager()

    def __str__(self):
        return self.sentence

