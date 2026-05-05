from django.shortcuts import render, redirect
from django.views.generic import View
from .forms import BookForm
from .models import Book

class BookView(View):
    def get(self, request):
        form = BookForm()
        books = Book.objects.all()
        return render(request, 'book_page.html', {
            'form': form,
            'books': books,
        })

    def post(self, request):
        form = BookForm(request.POST)
        if form.is_valid():
            Book.objects.create(
                title=form.cleaned_data['title'],
                author=form.cleaned_data['author']
            )
            return redirect('book_page')
        books = Book.objects.all()
        return render(request, 'book_page.html', {
            'form': form,
            'books': books,
        })

