from __future__ import unicode_literals
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, reverse
from django.contrib.auth import authenticate, login, logout
from users.forms import LoginForm
from django.http import HttpResponseRedirect
from users.admin import MyUserCreationForm


def handle_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, username=email, password=password)

            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('users:profile'))
    else:
        form = LoginForm()

    return render(request, 'users/login.html', {
        'form' : form
    })


def handle_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('users:login'))


@login_required
def profile(request):
    return render(request, 'users/profile.html')


def register(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)

        if form.is_valid():
            form.save()

            return HttpResponseRedirect(reverse('users:login'))
    else :
        form = MyUserCreationForm()

    return render(request, 'users/register.html', {
        'form' : form
    })
