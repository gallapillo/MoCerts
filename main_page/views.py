from datetime import datetime
import time
import random

from django.contrib.auth.models import User
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Account
from blog.models import Certificate_1
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.forms import UserCreationForm

from django.contrib import messages

from .forms import certificateForm, certificateForm2, RegistrationForm, LoginForm
from .names.names_generator import false_user


def main_page(request, *args, **kwargs):
    form_user = RegistrationForm(request.POST or None)
    if request.method == 'POST' and 'btn-register' in request.POST:#btn-register
        new_user = form_user.save(commit=False)
        new_user.username = form_user.cleaned_data['username']
        new_user.email = form_user.cleaned_data['email']
        new_user.save()
        new_user.set_password(form_user.cleaned_data['password'])
        new_user.save()
        Account.objects.create(
            user=new_user,
            phone=form_user.cleaned_data['phone'],
            full_name=form_user.cleaned_data['full_name'],
        )
        user = authenticate(username=form_user.cleaned_data['username'], password=form_user.cleaned_data['password'])
        login(request, user)
        return HttpResponseRedirect('new_cert/')

    form_login = LoginForm(request.POST or None)
    if request.method == 'POST' and 'btn-login' in request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('main_page')
        else:
            messages.info(request, 'Username OR password is incorrect')
    context = {'form_user': form_user,'form_login': form_login}
    return render(request, 'index.html', context)


def contacts(request):
    return HttpResponse('<h2>Страница с контактами</h2>')



def certificates(request, *args, **kwargs):
    cert = Certificate_1()
    cert_num, url, nominal, user1, user2, user3, published_date = cert.new_cert()
    context = {'cert_num': cert_num, 'url': url, 'nominal': nominal,
                                                                      'user1': user1, 'user2': user2, 'user3': user3, 'data': published_date}

    return render(request, 'My-Certificates.html', context)


def new_cert(request, *args, **kwargs):
    cert = Certificate_1()
    cert_num = cert.new_cert()
    context = {'cert_num': cert_num}
    return render(request, 'sertificates.html',  context)


def blog(request):
    return HttpResponse('<h2>blog</h2>')


class About(TemplateView):
    def get_context_data(self, *args, **kwargs):
        context = super().get_context_data(*args, **kwargs)
        cert = Certificate_1()
        cert_num, url, nominal, user1, user2, user3, published_date = cert.new_cert()
        context['cert_num'] = cert_num
        return context


def SignupPage(request):

        context = {}
        return render(request, 'signup.html', context)


def logoutUser(request):
    logout(request)
    return HttpResponseRedirect('/')


def BalanceAdd(request):
    context = {}
    return render(request, 'balanceAdd.html', context)


@login_required
def CreateCertificate(request):
    form = certificateForm(request.POST or None)
    certificate = Certificate_1()

    time.sleep(1)

    certificate1 = Certificate_1()
    certificate1.user1 = false_user()
    certificate1.user1_id = random.randint(1000, 10000000)
    certificate1.user2 = false_user()
    certificate1.user2_id = random.randint(1000, 10000000)
    certificate1.user3 = false_user()
    certificate1.user3_id = random.randint(1000, 10000000)
    date_cert4 = datetime.today()
    cert_num = date_cert4.strftime("%d%m%y%H%M%f")
    certificate1.number = cert_num

    time.sleep(2)

    certificate2 = Certificate_1()
    certificate2.user1 = false_user()
    certificate2.user1_id = random.randint(1000, 10000000)
    certificate2.user2 = false_user()
    certificate2.user2_id = random.randint(1000, 10000000)
    certificate2.user3 = false_user()
    certificate2.user3_id = random.randint(1000, 10000000)
    date_cert = datetime.today()
    cert_num2 = date_cert.strftime("%d%m%y%H%M%f")
    certificate2.number = cert_num2

    time.sleep(4)

    certificate3 = Certificate_1()
    certificate3.user1 = false_user()
    certificate3.user1_id = random.randint(1000, 10000000)
    certificate3.user2 = false_user()
    certificate3.user2_id = random.randint(1000, 10000000)
    certificate3.user3 = false_user()
    certificate3.user3_id = random.randint(1000, 10000000)
    date_cert2 = datetime.today()
    cert_num3 = date_cert2.strftime("%d%m%y%H%M%f")
    certificate3.number = cert_num3

    time.sleep(2)

    certificate4 = Certificate_1()
    certificate4.user1 = false_user()
    certificate4.user1_id = random.randint(1000, 10000000)
    certificate4.user2 = false_user()
    certificate4.user2_id = random.randint(1000, 10000000)
    certificate4.user3 = false_user()
    certificate4.user3_id = random.randint(1000, 10000000)
    date_cert3 = datetime.today()
    cert_num4 = date_cert3.strftime("%d%m%y%H%M%f")
    certificate4.number = cert_num4

    time.sleep(4)

    certificate5 = Certificate_1()
    certificate5.user1 = false_user()
    certificate5.user1_id = random.randint(1000, 10000000)
    certificate5.user2 = false_user()
    certificate5.user2_id = random.randint(1000, 10000000)
    certificate5.user3 = false_user()
    certificate5.user3_id = random.randint(1000, 10000000)
    date_cert4 = datetime.today()
    cert_num5 = date_cert4.strftime("%d%m%y%H%M%f")
    certificate5.number = cert_num5

    time.sleep(6)

    owner = Account.objects.get(user=request.user)
    owner_id = Account.objects.get(user=request.user.id)

    certificate1.owner = request.user
    certificate1.status = 'val3'

    certificate2.owner = request.user
    certificate2.status = 'val3'

    certificate3.owner = request.user
    certificate3.status = 'val3'

    certificate4.owner = request.user
    certificate4.status = 'val3'

    certificate5.owner = request.user
    certificate5.status = 'val3'

    context = {'form': form, 'certificate': certificate}
    if request.method == 'POST':
        if form.is_valid():
            new_certificate = form.save(commit=False)
            new_certificate.owner = request.user


            if owner_id.balance > 0:
                owner_id.balance -= new_certificate.nominal
                owner_id.save()


                new_certificate.status = 'val3'


                certificate1.save()
                certificate2.save()
                certificate3.save()
                certificate4.save()
                certificate5.save()
                owner_id.certificate_quantity += 5

                owner_id.cert_1.add(certificate1)
                owner_id.cert_1.add(certificate2)
                owner_id.cert_1.add(certificate3)
                owner_id.cert_1.add(certificate4)
                owner_id.cert_1.add(certificate5)
                owner.save()
                owner_id.save()



            return HttpResponseRedirect('/mycertificates/')
    return render(request, 'CreateCert.html', context)


@login_required
def CreateCertificate2(request):
    form = certificateForm2(request.POST or None)
    certificate = Certificate_1()
    owner = Account.objects.get(user=request.user)

    if request.method == 'POST':
        if form.is_valid():
            new_certificate = form.save(commit=False)
            new_certificate.owner = owner
            new_certificate.save()
            return HttpResponseRedirect('/')

    context = {'form': form, 'certificate': certificate}
    return render(request, 'CreateCert.html', context)


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


@login_required
def MyCertificate(request):
    context = {}
    return render(request, 'Myserticates.html', context)

def Instruction(request):
    context = {}
    return render(request, 'instructions.html',context)

class RegistrationView(View):

    def get(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        context = {'form': form}
        return render(request, 'registraion.html', context)

    def post(self, request, *args, **kwargs):
        form = RegistrationForm(request.POST or None)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.username = form.cleaned_data['username']
            new_user.email = form.cleaned_data['email']
            new_user.save()
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            Account.objects.create(
                user=new_user,
                phone=form.cleaned_data['phone'],
                full_name=form.cleaned_data['full_name'],
            )
            user = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            login(request, user)
            return HttpResponseRedirect('/')
        context = {'form': form}
        return render(request, 'registraion.html', context)
