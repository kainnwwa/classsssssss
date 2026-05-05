from django import forms 
from .models import Book

class BookForm(forms.Form):
    title = forms.CharField(label='Название книги', max_length=100)
    author = forms.CharField(label='Автор', max_length=100)
    
