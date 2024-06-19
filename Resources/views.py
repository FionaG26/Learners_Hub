from django.shortcuts import render
from .models import Book, Blog

# Create your views here.
def book_list(request):
    books = Book.objects.all()
    return render(request, 'Resources/book.html', {'books': books})

def blog_list(request):
    blogs = Blog.objects.all()
    return render(request, 'Resources/blog.html', {'blogs': blogs})
