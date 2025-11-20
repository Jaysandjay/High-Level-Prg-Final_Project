from django.shortcuts import render, redirect
from .models import Book, User

def home(request):
    books = Book.objects.all()
    return render(request, "books/home.html", {'books': books})


def details(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, "books/details.html", {'book': book})


def add(request):
    if request.method == 'POST':
        book = Book(
            title=request.POST['title'],
            author=request.POST['author'],
            year=request.POST['year'],
            rating=request.POST['rating'],
            description=request.POST['description'],
            )
        book.save()
        
    return render(request, "books/add.html")


def edit(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, "books/edit.html", {'book': book})


def login(request):
    if request.method == "POST":
        user = User.objects.get(
            email = request.POST.email,
            password = request.POST.password
            )
        if user:
            return redirect("home", user=user.email)
        else:
            return render(request, "books/login.html", {'error': True })

    return render(request, "books/login.html")


def register(request):
    if request.method == "POST":
        user = User(
            email = request.POST.email,
            password = request.POST.password
            )
        is_user = User.objects.get(
            email = request.POST.email,
            password = request.POST.password
            )
        
        if is_user:
            return render(request, "books/register.html", {'error': True } )
        
        else:
            return redirect("home", {'user':user.email})
        
    return render(request, "books/register.html")

def delete(request, book_id):
    book = Book.objects.get(id=book_id)
    return render(request, "books/delete.html", {'book': book})