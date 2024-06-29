from django.db import models

# Create your models here.

class BookDetails(models.Model):
    pdf = models.FileField(upload_to='pdfs/' , blank = True , null= True)
    no_of_borrow = models.BigIntegerField(default = 0)
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    isbn10 = models.CharField(max_length=10 , default='N/A')
    isbn13 = models.CharField(max_length=13 ,  default='N/A')
    overview1 = models.TextField()
    overview2 = models.TextField()
    image_url = models.ImageField(upload_to='photos') 
    authorImage_url = models.ImageField(upload_to='photos')
    category = models.CharField(max_length=50, default ='')
    available=models.BooleanField(default=True)
    btn = models.CharField(max_length=100,default='Borrow')
  
def __str__(self):
        return self.title


class register3(models.Model):
    username = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    password2 = models.CharField(max_length=50)
    type = models.CharField(max_length=50)


class BorrowedBook(models.Model):
    book = models.ForeignKey(BookDetails, on_delete= models.CASCADE)
    user = models.ForeignKey(register3 , on_delete= models.CASCADE , default=1)
def __str__(self):
    return f"{self.book.title} borrowed by {self.user.username}"