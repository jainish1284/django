from django.shortcuts import render
from django.http import HttpResponse
from .models import MainModel


def homepage(request):
    return HttpResponse("<strong>Innnnn</strong>");


