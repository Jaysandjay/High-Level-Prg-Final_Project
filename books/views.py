from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Book
from .forms import BookForm

def home(request):
    books = Book.objects.all()
    return render(request, "books/home.html", {'books': books})


def details(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, "books/details.html", {'book': book})

@login_required
def add(request):
    form = BookForm(request.POST)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            form = BookForm()
    return render(request, 'books/add.html', {'form': form})


@login_required
def edit(request, book_id):
    book = Book.objects.get(id=book_id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'books/add.html', {'form': form})

@login_required
def delete(request, book_id):
    book = Book.objects.get(id=book_id)

    if request.method == 'POST':
        book.delete()
        messages.success(request, "Book deleted successfully!")
        return redirect('home') 
    return render(request, "books/delete.html", {'book': book})


