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

# Function to request admin page of the application: url is "http://localhost/admin/MyBookStore/" 
def  Create_Book(request):
    return render(request,'/MyBookStore/')


# It will be used to request home page for the application: url is "http://localhost/home/"
class home_bookstore(TemplateView):
    template_name = 'home.html'
    
    
#Used to search book by author name and lists book names for the particular author. Makes use of http GET method to extract user query from html form
class search_book_by_author(ListView):
    model = Book
    template_name = 'searchresults.html'
    #queryset = Book.objects.all()
    def get_queryset(self):
        query = self.request.GET.get('q')
        object_list =Book.objects.filter(Q(author__icontains=query))
        return object_list

    
#class home_view(TemplateView):
 #   template_name = 'remhome.html'




