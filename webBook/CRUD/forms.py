from django import forms
from django.forms import ModelForm
from .models import Books

class BookForm(forms.ModelForm):
    class Meta:
        model = Books
        fields = [
            'title',
            'author',
            'pages',
            'types',
            'pub_date',
        ]