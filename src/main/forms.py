from django import forms


class FileForm(forms.Form):
    recording = forms.FileField()
