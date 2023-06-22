from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('', views.index, name="index"),
    path('about/', views.about, name="about"),
    path('book/', views.book, name="book"),
    path('contact/', views.contact, name="contact"),
    path('author/', views.author, name="author"),
    path('createauthor/', views.createauthor, name="createauthor"),
    path('readauthor/<int:author_id>/', views.readauthor, name="readauthor"),
    path('editauthor/<int:author_id>/', views.editauthor, name="editauthor"),
    path('deleteauthor/<int:author_id>/', views.deleteauthor, name="deleteauthor"),
    
    
    # authntication and authorization urls
    path('register', views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name='auth/login.html'), name="login"),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name="auth/password_reset.html"), name="password_reset"),
    path('password_reset_done/', auth_views.PasswordResetDoneView.as_view(template_name='auth/password_reset_done.html'), name="password_reset_done"),
    path('password_reset_confirm/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset_confirm.html"), name="password_reset_confirm"),
    path('password_reset_complete/', auth_views.PasswordResetCompleteView.as_view(template_name="password_reset_complete"), name="password_reset_complete"),
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, documnet_root=settings.MEDIA_ROOT)
