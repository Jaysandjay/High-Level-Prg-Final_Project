# books/views.pys
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Book
from .forms import BookForm, SearchBookForm

def home(request):
    books = Book.objects.all()
    return render(request, "books/home.html", {'books': books})


def details(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, "books/details.html", {'book': book})

def search_book(request):
    book = None
    id = None

    # Use GET instead of POST
    form = SearchBookForm(request.GET or None)

    if form.is_valid():
        id = form.cleaned_data['book_id']
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            book = None

    return render(request, 'books/search.html', {
        'form': form,
        'book': book,
        'id': id    
    })
        

@login_required(login_url='/login/')
def add(request):
    form = BookForm(request.GET)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = BookForm()
    return render(request, 'books/add.html', {'form': form})


@login_required(login_url='/login/')
def edit(request, book_id):

    book = Book.objects.get(id=book_id)
    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'books/add.html', {'form': form})

@login_required(login_url='/login/')
def delete(request, book_id):
    
    book = Book.objects.get(id=book_id)

    if request.method == 'POST':
        book.delete()
        messages.success(request, "Book deleted successfully!")
        return redirect('home') 
    return render(request, "books/delete.html", {'book': book})


