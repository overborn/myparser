from django import forms


class FileForm(forms.Form):
    source = forms.FileField()


class ChartForm(forms.Form):
    def __init__(self, choices, *args, **kwargs):
        super(ChartForm, self).__init__(*args, **kwargs)
        self.fields['region'].choices = choices
    region = forms.ChoiceField(choices=[])
