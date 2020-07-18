from django.shortcuts import render, HttpResponse, redirect
from .models import Book, Author

def index(request):
    context = {
        'all_books':Book.objects.all(),
        'all_authors': Author.objects.all()
    }
    return render(request, "index.html", context)

def addbook(request):
    Book.objects.create(
        title=request.POST['title'],
        desc = request.POST['description']
    )
    return redirect ('/')

def assignauthor(request,author_id):
    book = Book.objects.get(id=id)
    author = Author.objects.get(id=request.POST['author_id'])
    book.authors.add(author)
    return redirect(f'/books/{id}')

def viewbook(request,id):
    book = Book.objects.get(id=id)
    context = {
        'book': book,
        'authors': Author.objects.exclude(books__id=id),      
    }
    return render(request, "bookdetails.html", context)


def author(request):
    context = {
        'all_books':Book.objects.all(),
        'all_authors': Author.objects.all()
    }
    return render(request, "authors.html", context)


def viewauthor(request, author_id):
    author = Author.objects.get(id=author_id)
    context = {
        "author": author,
        "books": Book.objects.filter(author__id=author_id),
    }
    return render(request, "authordetails.html", context)

def addauthor(request):
    Author.objects.create(
        first_name=request.POST['fname'],
        last_name=request.POST['fname'],
        notes=request.POST['notes'],
    )
    return redirect ('/authors.html')