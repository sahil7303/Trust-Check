# checker/forms.py
from django import forms

class URLForm(forms.Form):
    url = forms.URLField(label='Enter URL', required=True)
