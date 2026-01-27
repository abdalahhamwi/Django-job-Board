from django.shortcuts import render, redirect
from .models import Popolar_Categories

# Create your views here.


def home_view(request):
    category = Popolar_Categories.objects.all()

    return render(request, "home.html", {"category": category})


def post_job(request):

    return render(request, "post_job.html")
