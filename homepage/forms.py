from django import forms


class InputForm(forms.Form):
    body = forms.CharField(max_length=100)