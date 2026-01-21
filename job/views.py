from django.shortcuts import render

# Create your views here.


def job_views(request):
    return render(request, "jobs.html")


def job_detail_views(request):
    return render(request, "job_details.html")
