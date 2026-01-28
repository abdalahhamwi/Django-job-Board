from django.shortcuts import render
from .models import Job_Detail


# Create your views here.


def jobs_views(request):
    job_detail = Job_Detail.objects.all()
    Jobs_Available = Job_Detail.objects.count()

    return render(request, "jobs.html", {"job_detail": job_detail ,"Jobs_Available":Jobs_Available })


def job_detail_views(request, id):
    job_id = Job_Detail.objects.get(id=id)
    job_detail = Job_Detail.objects.all()

    return render(request, "job_details.html", {"job_detail": job_detail})
