from django import forms

class DniForm(forms.Form):
    dni = forms.CharField(label='DNI', max_length=10)