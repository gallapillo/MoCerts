from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('contacts/', views.contacts, name='contacts-home')
]