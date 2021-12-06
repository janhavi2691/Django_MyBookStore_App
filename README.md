# Django_MyBookStore_App
This is a small book store app which can be used to perform some basic logical things as a book store might be involved in like create books, and search books by author. 
I will give a walkthrough the application.

## Scope:
Create a Book Store App
  <li>Must be able to create book</li>
  <li>Create Author and relate Author with Books</li>
  <li>List Books for given author</li>
  <li>Must use Python, Django</li>
  <li>Can use Javascript</li>
  <li>You can save data however you want</li>
  
### I tried to fulfill all the requirements (Basically Backend Part) to the best of my knowledge. 
### More variations are possible like fancy frontend and even more clarity on backend as well.     


# Urls to get started with the App: 
    http://localhost/home/       - Home Page to search books by author names
    http://localhost/admin/      - Admin page allows to add, delete, update records


#For simplicity used default sqlite database   


## Directory Structure 
 <li><b>Models.py</b> : Used to define and create Book schema, its fields</li>
 <li><b>Views.py</b> : Contains a function to process request for admin page, a class to process search query request, another class to process a request for home page</li>
 <li><b>urls.py</b> : Used to create url paths for webpages of the application</li>
 <li><b>Templates Directory</b> : Created html templates for different webpages of the application</li>
 <li><b>static Directory</b> : Created to contain default style sheet used by all web pages and other multimedia displayed on them</li>

