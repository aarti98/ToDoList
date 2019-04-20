from django.shortcuts import render
from .forms import UserSignUpForm, UserLoginForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))


def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserSignUpForm(request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            registered = True
        else:
            print(user_form.errors)
    else:
        user_form = UserSignUpForm()
    return render(request, 'Account/registration.html',
                  {'user_form':user_form,
                           'registered':registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('list'))
            else:
                return HttpResponse("Your registration was inactive.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details given")
    else:
        return render(request, 'Account/login.html', {})