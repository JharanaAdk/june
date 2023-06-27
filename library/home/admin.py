from django.contrib import admin
# from . models import Author , Book
from . models import *
# Register your models here.
admin.site.register(Author)
admin.site.register(Books)
admin.site.register(Contact)
admin.site.register(Blog)