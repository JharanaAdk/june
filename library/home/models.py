from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
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
   
    
class Contact(models.Model):
    full_name = models.CharField(max_length=200)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=350)
    
    def __str__(self):
        return str(self.full_name)
    
    
    
    
class Blog(models.Model):
    slug = models.CharField(max_length=200)
    title = models.CharField(max_length=200)
    description = RichTextField(max_length=2000)
    image = models.ImageField(upload_to = 'img/')
    status = models.BooleanField(default=False, help_text="0=default, 1-Hidden")
    trending = models.BooleanField(default=False, help_text="0=default, 1-Trending")
    meta_keyword = models.CharField(max_length=200)
    meta_title = models.CharField(max_length=200)
    meta_description = models.TextField(max_length=500)
    created_at = models.DateTimeField(auto_now_add=True)
    written_by = models.CharField(max_length=200)
    
    def __str__(self):
        return self.title