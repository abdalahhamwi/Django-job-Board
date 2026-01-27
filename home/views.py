from django.shortcuts import render, redirect
from .models import Popolar_Categories, Job_Listing

# Create your views here.


def home_view(request):
    category = Popolar_Categories.objects.all()
    Jobs = Job_Listing.objects.all()

    return render(request, "home.html", {"category": category, "Jobs": Jobs})


def post_job(request):

    return render(request, "post_job.html")
