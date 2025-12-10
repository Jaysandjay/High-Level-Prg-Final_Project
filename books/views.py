# books/views.pys
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Book
from .forms import BookForm, SearchBookForm


def home(request):
    # SHOW ALL THE BOOKS
    books = Book.objects.all()
    return render(request, "books/home.html", {'books': books})


def details(request, book_id):
    # GET DETAILS OF A BOOK BY ID
    book = Book.objects.get(id=book_id)
    return render(request, "books/details.html", {'book': book})


def search_book(request):
    # SEARCH FOR A BOOK BASED ON VALS IN REQUEST

    # DEFAULT VARS
    book = None
    id = None

    # GET THE FORM
    form = SearchBookForm(request.GET or None)

    # PERFORM SEARCH IF FORM VALID
    if form.is_valid():
        id = form.cleaned_data['book_id']
        try:
            book = Book.objects.get(id=id)
        except Book.DoesNotExist:
            book = None

    # RETURN THE VIEW WITH FORM, ID, AND/OR BOOK IF FOUND
    return render(request, 'books/search.html', {
        'form': form,
        'book': book,
        'id': id
    })


# ===========================================================================
# BOOK CREATE, UPDATE, DELETE LOGIC REQUIRE LOGIN

@login_required(login_url='/login/')
def add(request):

    # HANDLE IF POST
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            book = form.save(commit=False)
            book.created_by = request.user
            book.save()
            return redirect('home')
    else:
        form = BookForm()

    return render(request, 'books/add.html', {'form': form})


@login_required(login_url='/login/')
def edit(request, book_id):

    book = Book.objects.get(id=book_id)

    # CHECK IF USER IS THE OWNER
    if book.created_by != request.user:
        messages.error(request, "You are not authorized to edit this book.")
        return redirect('home')

    form = BookForm(request.POST or None, instance=book)
    if form.is_valid():
        form.save()
        return redirect('home')
    return render(request, 'books/add.html', {'form': form, 'is_edit': True})


@login_required(login_url='/login/')
def delete(request, book_id):

    book = Book.objects.get(id=book_id)

    # CHECK IF USER IS THE OWNER
    if book.created_by != request.user:
        messages.error(request, "You are not authorized to delete this book.")
        return redirect('home')

    if request.method == 'POST':
        book.delete()
        messages.success(request, "Book deleted successfully!")
        return redirect('home')
    return render(request, "books/delete.html", {'book': book})
