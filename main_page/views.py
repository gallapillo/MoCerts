from django.contrib.auth import logout, login, authenticate
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Certificate
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages


def main_page(request, *args, **kwargs):
    return render(request, 'index.html', {})


def contacts(request):
    return HttpResponse('<h2>Страница с контактами</h2>')


def certificates(request, *args, **kwargs):
    cert = Certificate()
    cert_num, url, nominal, user1, user2, user3, published_date = cert.new_cert()
    context = {'cert_num': cert_num, 'url': url, 'nominal': nominal,
                                                                      'user1': user1, 'user2': user2, 'user3': user3, 'data': published_date}

    return render(request, 'My-Certificates.html', context)


def new_cert(request, *args, **kwargs):
    cert = Certificate()
    cert_num = cert.new_cert()
    context = {'cert_num': cert_num}
    return render(request, 'sertificates.html',  context)


def blog(request):
    return HttpResponse('<h2>blog</h2>')


class About(TemplateView):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        cert = Certificate()
        cert_num, url, nominal, user1, user2, user3, published_date = cert.new_cert()
        context['cert_num'] = cert_num
        return context


def SignupPage(request):

        context = {}
        return render(request, 'signup.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


def BalanceAdd(request):
    context = {}
    return render(request, 'balanceAdd.html', context)


def LoginPage(request):
    if request.user.is_authenticated:
        return redirect('main_page')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:
                login(request, user)
                return redirect('main_page')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'login.html', context)
