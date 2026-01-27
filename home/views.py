from django.shortcuts import render, redirect
from .models import Popolar_Categories

# Create your views here.


def home_view(request):
    return render(request, "home.html")


def post_job(request):

    return render(request, "post_job.html")
