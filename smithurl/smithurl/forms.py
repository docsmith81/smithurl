from django import forms

class UrlForm(forms.Form):
    long_url = forms.CharField(label='Please enter your URL', max_length=1000)