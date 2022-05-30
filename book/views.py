from django.shortcuts import render
from django.views import generic

from book.models import Book

class BookListView(generic.ListView):
    model=Book
    template_name='/book/book_list.html'
    context_object_name='books'