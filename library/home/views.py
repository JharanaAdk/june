from django.shortcuts import render
from . models import Books
# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def book(request):
    book = Books.objects.all()
    context= {'book':book}
    return render(request, 'book.html', context)