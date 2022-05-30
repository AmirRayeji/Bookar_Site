from django.shortcuts import render
from django.views import generic

from book.models import Book

class BookListView(generic.ListView):
    model=Book
    paginate_by = 4
    template_name='/book/book_list.html'
    context_object_name='books'


class BookDetailView(generic.DetailView):
    model=Book
    template_name='book/book_detail.html'


class BookCreateView(generic.CreateView):
    model=Book
    fields=['user', 'title', 'author', 'description', 'cover']
    template_name='book/book_create.html'
    
