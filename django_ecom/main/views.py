from django.shortcuts import render, redirect
from django.http import HttpResponse

from .forms import NewUserForm
from .models import Tutorials, TutorialCategory, TutorialSeries
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages


def single_slug(request, single_slug_view):
    categories = [c.category_slug for c in TutorialCategory.objects.all()]
    if single_slug_view in categories:
        matching_series = TutorialSeries.objects.filter(tutorial_category__category_slug=single_slug_view)
        series_urls = {}
        for m in matching_series.all():
            part_one = Tutorials.objects.filter(tutorial_series__tutorial_series=m.tutorial_series).earliest('tutorial_published')
            series_urls[m] = part_one.tutorial_slug
        return render(request,
                      "category.html",
                      {'part_ones':series_urls})

    tutorials = [t.tutorial_slug for t in Tutorials.objects.all()]
    if single_slug_view in tutorials:
        this_tutorial = Tutorials.objects.filter(tutorial_slug=single_slug_view)
        # this_tutorial = Tutorials.objects.get(tutorial_slug=single_slug_view)
        tutorials_from_series = Tutorials.objects.filter(tutorial_series__tutorial_series=this_tutorial.tutorial_series).order_by('tutorial_published')
        this_tutorial_idx = list(tutorials_from_series).index(this_tutorial)
        return render(request=request,
                      template_name='tutorial.html',
                      context={"tutorial": this_tutorial,
                               "sidebar": tutorials_from_series,
                               "this_tut_idx": this_tutorial_idx})

    return HttpResponse(f"No match for {single_slug_view}")


def homepage(request):
    return render(request=request,
                  template_name="index.html",
                  context={"tutorials": TutorialCategory.objects.all()})


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
