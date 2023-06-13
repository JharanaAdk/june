from django.shortcuts import render
from . models import Books, Author
# Create your views here.
def index(request):
    return render(request, "index.html")

def author(request):
    author = Author.objects.all()
    context={
        "author": author
    }
    return render(request, "author.html", context)

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, "about.html")

def book(request):
    book = Books.objects.all()
    context= {'book':book}
    return render(request, 'book.html', context)