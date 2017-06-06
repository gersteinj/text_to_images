from django import forms
from django.core.exceptions import ValidationError

class TTIForm(forms.Form):
	your_word = forms.CharField(label='Word: ', max_length=100)
	lots_of_words = forms.CharField(widget=forms.Textarea)