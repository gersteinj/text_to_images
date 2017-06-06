from django import forms
from django.core.exceptions import ValidationError

class TTIForm(forms.Form):
	your_word = forms.CharField(label='give me a word', max_length=100)