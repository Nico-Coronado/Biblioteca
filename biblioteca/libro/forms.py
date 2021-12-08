from django import forms
from django.forms import widgets

from . models import Book
from autor.models import Author

class FilterForm(forms.ModelForm):
    authors = forms.ModelMultipleChoiceField(
        queryset=Author.objects.all(),
        widget = forms.CheckboxSelectMultiple,
        label = "Filtrar por autores"
    )        
    class Meta:
        model = Book
        fields = ('authors',)
