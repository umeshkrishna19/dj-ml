from django import forms


class NewPredictionForm(forms.Form):
    Title = forms.CharField(max_length=128)
    Description = forms.CharField(max_length=1024)


    def __init__(self, *args, **kwargs):
        super(NewPredictionForm,  self).__init__(*args, **kwargs)
