from django.urls import path
from . import views

urlpatterns = [
    path('contacts/', views.contacts, name='contacts-home'),
    path('certificates/', views.certificates, name='certificates-home'),
    path('new_cert/', views.new_cert, name='create-certificate'),
    path('', views.main_page, name='main_page'),

    path('about/', views.About, name='about'),
    path('signup/', views.SignupPage, name='signup'),
    path('login/', views.LoginPage, name='login'),
path('logout/', views.logoutUser, name='logout'),
    path('balance/', views.BalanceAdd, name='balance')
]
