from django.urls import reverse_lazy
from django.views import generic

from .models import Book


class BookListView(generic.ListView):
    model = Book
    template_name = 'books/book_list.html'
    context_object_name = 'books'


class BookDetailView(generic.DetailView):
    model = Book
    template_name = 'books/book_detail.html'


class BookCreateView(generic.CreateView):
    model = Book
    fields = ['title', 'author', 'description', 'price', 'translator', 'publisher', 'year_of_publication', 'language']
    template_name = 'books/book_create.html'


class BookUpdateView(generic.UpdateView):
    model = Book
    fields = ['title', 'author', 'price', 'translator', 'publisher', 'year_of_publication', 'language',
              'number_of_pages']
    template_name = 'books/book_update.html'


class BookDeleteView(generic.DetailView):
    model = Book
    template_name = 'books/book_delete.html'
    success_url = reverse_lazy('book_list')
