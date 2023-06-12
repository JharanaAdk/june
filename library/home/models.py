from django.db import models

# Create your models here.
class Author(models.Model):
    name = models.CharField(max_length=200)
    age = models.PositiveIntegerField()
    pen_name = models.CharField(max_length=200)
    journal = models.CharField(max_length=200)
    active_date = models.DateField()
    
    def __str__(self):
        return str(self.name)
    

class Books(models.Model):
   name = models.CharField(max_length=200, blank=False, null=False)
   price = models.PositiveIntegerField(blank=False, null=False)
   author = models.ForeignKey(Author, on_delete=models.CASCADE)
   published_date = models.DateField(blank=False, null=False)
   edition = models.CharField(max_length =200, blank=True, null=True)
   description = models.TextField(max_length=500, blank=True, null = True)
   
   def __str__(self):
       return str(self.name)
   
    