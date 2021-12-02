from django import forms

class SearchForm(forms.Form):
    author_name = forms.CharField(label='Enter Author Name', max_length=50)