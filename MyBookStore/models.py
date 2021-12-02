from django.db import models
from django.db.models.deletion import CASCADE

# Create your models here.
class Author(models.Model):
    aname = models.CharField(name='Author Name',default='Enter Author Name', max_length=25)
    #booklist = models.TextField(name="List of Books authored by {}\n".format(aname))
    def __str__(self):
        return str(self.aname)



class Book(models.Model):
    title = models.CharField(default='Write book title here',max_length=100)
    author = models.CharField(default='Write author name here',max_length=25)
    language = models.CharField(choices=[('EG','English'),('FR','French'),('GE','German'),('SP','Spanish')],max_length=20)
    isbn = models.IntegerField(name='ISBN', default=0,unique=True, max_length=13,primary_key=True)
    pubyear = models.DateField(name='Publication Year')
    category = models.CharField(choices=[('FICT','Fiction'),('NFICT','Nonfiction'),('CL','Classic'),('BI','Biography'),('TECH','Technology'),('OT','Other')],max_length=20)

    def __str__(self):
        return str(self.title)

    