from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutorials


def homepage(request):
    return render(request=request,
                  template_name="index.html",
                  context={"tutorials": Tutorials.objects.all()})


