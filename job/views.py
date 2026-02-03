from django.shortcuts import render , redirect
from home.models import Post_Job
from .forms import JobApplicationForm


# Create your views here.


def jobs_views(request):

    job_detail = Post_Job.objects.all()
    job_number = Post_Job.objects.count()
    
    return render(request, "jobs.html", {"job_detail": job_detail , "job_number":job_number})

def job_detail_views(request, slug):
    
    if request.method == "POST" :
        apply_job = JobApplicationForm(request.POST , request.FILES)
        if apply_job.is_valid():
            apply_job.save()
        return redirect('jobs')
    else:
        apply_job = JobApplicationForm()

    job_detail = Post_Job.objects.get(slug=slug)

    return render(request, "job_detail.html", {"job_detail": job_detail ,"apply_job": apply_job})
