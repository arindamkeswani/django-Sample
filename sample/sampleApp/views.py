from django.shortcuts import render
from .models import Book
# Create your views here.

from django.http import HttpResponse

def index(request):
    return HttpResponse("Hello world")

def book_by_id(request, book_id):
    book = Book.objects.get(pk=book_id)
    # return HttpResponse(f"Book: {book.title}, published on {book.pub_date}")
    return render(request, 'book_details.html', {'book':book})