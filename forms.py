
from django import forms
from .models import Book
class BookForm(forms.ModelForm):
    class Meta:
        Model = Book
        fields = ['title', 'author', 'publication_date']