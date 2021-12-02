from django.db import models
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.generic import ListView , TemplateView
from django.db.models import Q


from .models import Author, Book


# Create your views here.
#request - response
#request handlers

def  Create_Book(request):
    return render(request,'/MyBookStore/')



class home_bookstore(TemplateView):
    template_name = 'home.html'

class search_book_by_author(ListView):
    model = Book
    template_name = 'searchresults.html'
    #queryset = Book.objects.all()
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list =Book.objects.filter(Q(author__icontains=query))
        return object_list

    
class home_view(TemplateView):
    template_name = 'remhome.html'




'''
def search_book(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = SearchForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponseRedirect('/searchbook/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = SearchForm()

    return render(request, 'home.html', {'form': form})
'''