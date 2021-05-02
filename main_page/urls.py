from django.urls import path
from . import views

urlpatterns = [
    path('contacts/', views.contacts, name='contacts-home'),
    path('certificates/', views.certificates, name='certificates-home'),
    path('new_cert/', views.new_cert, name='create-certificate'),
    path('', views.main_page, name='main_page'),

    path('about/', views.About, name='about'),
    path('signup/', views.RegistrationView.as_view(), name='signup'),
    path('login/', views.LoginPage, name='login'),
path('logout/', views.logoutUser, name='logout'),
    path('balance/', views.BalanceAdd, name='balance'),
    path('mycertificates/', views.MyCertificate, name='my-certificates'),
    path('instructions/', views.Instruction, name='instruction'),
    path('create-certificate/', views.CreateCertificate, name='create-cert'),
    path('create-certificate2/', views.CreateCertificate2, name='create-cert2'),
]
