from django.shortcuts import render
from django.views import generic
from .models import Book, BookInstance, Author


# Create your views here.
def index(request):

    num_books = Book.objects.count()
    num_instances = BookInstance.objects.count()
    num_instances_available = BookInstance.objects.filter(status__exact='a').count()
    num_authors = Author.objects.count()

    context = {
        'num_books': num_books,
        'num_instances': num_instances,
        'num_instances_available': num_instances_available,
        'num_authors': num_authors
    }

    return render(request, 'index.html', context=context)


class BookListView(generic.ListView):
    model = Book

    def get_queryset(self):
        return Book.objects.all()[:5]


class BookDetailView(generic.DetailView):
    model = Book
