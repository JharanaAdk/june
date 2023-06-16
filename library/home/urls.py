from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('contact/', views.contact, name="contact"),
    path('author/', views.author, name="author"),
    path('createauthor/', views.createauthor, name="createauthor"),
    path('readauthor/<int:author_id>/', views.readauthor, name="readauthor"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, documnet_root=settings.MEDIA_ROOT)
