from django import forms


class FileForm(forms.Form):
    source = forms.FileField()
