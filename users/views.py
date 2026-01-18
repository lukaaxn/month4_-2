from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required 

from .forms import LoginForm, RegisterForm

# Create your views here.

def register_view(request):
    if request.method == 'GET':
        forms_obj = RegisterForm()
        return render(request, 'users/register.html', context={'form': forms_obj})
    elif request.method == 'POST':
        forms_obj = RegisterForm(request.POST)
        if forms_obj.is_valid():
            forms_obj.cleaned_data.__delitem__('confirm_password')
            User.objects.create_user(**forms_obj.cleaned_data)
            return HttpResponse('User created')
        return HttpResponse('Invalid')


def login_view(request):
    if request.method == 'GET':
        forms_obj = LoginForm()
        return render(request, 'users/login.html', context={'form': forms_obj})
    elif request.method == 'POST':
        forms_obj = LoginForm(request.POST)
        if forms_obj.is_valid():
            user = authenticate(**forms_obj.cleaned_data)
            login(request, user)
            return HttpResponse('User logged in')
        
@login_required(login_url='/login/')
def logout_view(request):
    if request.method == 'GET':
        logout(request)
        return HttpResponse('User logged out')