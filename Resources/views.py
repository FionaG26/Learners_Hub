from django.shortcuts import render
from .models import Book, Blog

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    return render(request, 'resources/books.html', {'books': books})

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'resources/blog.html', {'blogs': blogs})
