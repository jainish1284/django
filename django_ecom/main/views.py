from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import NewUserForm
from .models import Tutorials
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


def homepage(request):
    return render(request=request,
                  template_name="index.html",
                  context={"tutorials": Tutorials.objects.all()})


# def register(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             user = form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f"New Account Created : {username}")
#             login(request, user)
#             messages.info(request, f"User Logged In  : {username}")
#             return redirect("main:homepage")
#         else:
#             for msg in form.errors:
#                 messages.error(request, f"{msg}:{form.errors[msg]}")
#     form = UserCreationForm
#     return render(request=request,
#                   template_name="register.html",
#                   context={"form":form})


def register(request):
    if request.method == 'POST':
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created : {username}")
            login(request, user)
            messages.info(request, f"User Logged In  : {username}")
            return redirect("main:homepage")
        else:
            for msg in form.errors:
                messages.error(request, f"{msg}:{form.errors[msg]}")
    form = NewUserForm
    return render(request=request,
                  template_name="register.html",
                  context={"form":form})



def logout_request(request):
    logout(request)
    messages.info(request, "Logged Out Successfully")
    return redirect('main:homepage')


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, f"Welcome {username}")
            return redirect('main:homepage')
        else:
            for msg in form.errors:
                messages.error(request, f"{msg}:{form.errors[msg]}")
    form = AuthenticationForm()
    return render(request=request,
                  template_name='login.html',
                  context={"form": form})
