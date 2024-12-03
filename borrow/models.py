from django.db import models
from readers.models import Reader
from books.models import Books
from readers.models import Reader
# Create your models here.

class BorrowBook(models.Model):
    books=models.ForeignKey(Books,on_delete=models.CASCADE)
    reader=models.ForeignKey(Reader,on_delete=models.CASCADE)
    borrowDate=models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return self.books.title
    