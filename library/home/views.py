from django.shortcuts import render, redirect
from . models import Books, Author
from . forms import AuthorForm, UserCreationForm
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

def createauthor(request):
    if request.method =="GET":
        author_form = AuthorForm
        return render(request, 'create_author.html', context={'form': author_form})
    else:
        author_form = AuthorForm(request.POST)
        if author_form.is_valid():
            author_form.save()
            return redirect('author')
    return render(request, 'create_author.html', context={'form': author_form})


def readauthor(request, author_id):
    author = Author.objects.get(id=author_id)
    context ={'author':author}
    return render(request, 'readauthor.html', context)


def editauthor(request, author_id):
    author = Author.objects.get(id=author_id)
    if request.method == 'POST':
        form = AuthorForm(instance=author)
        form = AuthorForm(request.POST, instance=author)
        if form.is_valid():
            form.save()
            return redirect('author')
    else:
        form = AuthorForm(instance=author)
    return  render(request, 'edit_author.html', {'form':form})
    
def deleteauthor(request, author_id):
    author = Author.objects.get(id=author_id)
    if request.method =="POST":
        author.delete()
        return redirect('author')
    else:
        return render(request, 'delete.html', {'author':author})
def register(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)  
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'auth/register.html', context={'form':form})