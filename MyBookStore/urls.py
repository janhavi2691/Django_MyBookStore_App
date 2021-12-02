from os import name
from django.urls import path
from . import views
from .views import home_bookstore, search_book_by_author , home_view

app_name = 'MyBookStore'

#URLconfig
urlpatterns = [
    path('', views.Create_Book,name='createbook'),
    path('home/',home_bookstore.as_view(),name='home'),
    path('searchresults/',search_book_by_author.as_view(),name='searchresults'),
]