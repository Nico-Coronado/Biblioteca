from django.http import response
from django.views.generic import (
    TemplateView, ListView, 
    DetailView
    )

from prestamo.views import LoanFormView
from . models import Book
from . forms import FilterForm
from prestamo.models import Loan

class Index(TemplateView):
    template_name = "base/index.html"
   
class BookListView(ListView):
    model = Book
    template_name = "book/book_list.html"
    context_object_name = 'list'

    def get_queryset(self):
        author = self.request.GET.get('authors')
        querysetAuthor = Book.objects.getAuthors(author)
        kword = self.request.GET.get('kword', '')
        querysetKword = Book.objects.getKword(kword)

        if querysetAuthor:
            return querysetAuthor
        elif querysetKword:
            return querysetKword

    
    def get_context_data(self, **kwargs):
        context = super(BookListView, self).get_context_data(**kwargs)
        context['form'] = FilterForm()
        return context
    


class BookDetailView(LoanFormView, DetailView):
    model = Book
    template_name = "book/book_detail.html"
    context_object_name = "book"

    

    
   
    
