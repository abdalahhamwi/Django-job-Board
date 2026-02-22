from django.shortcuts import render, redirect
from home.models import Post_Job
from .forms import JobApplicationForm
from django.contrib import messages
from django.core.mail import send_mail
from django.core.paginator import Paginator

# Create your views here.

def jobs_views(request):
    
    job_detail = Post_Job.objects.all()
    job_number = Post_Job.objects.count()
    
    paginator = Paginator(job_detail, 1)
    page_number = request.GET.get("page")
    page_obj = paginator.get_page(page_number)
    return render(
        request, "jobs.html", {"job_detail": page_obj, "job_number": job_number ,}
    )


def job_detail_views(request, slug):

    if request.method == "POST":
        apply_job = JobApplicationForm(request.POST, request.FILES)
        if apply_job.is_valid():
            apply_job.save()
            
            user_email = apply_job.cleaned_data["email"]
            
            # رسالة للمستخدم
            send_mail(
                subject="Thanks for applying!",
                message="Hello! We received your application and will reply soon.",
                from_email="abdalah09941@gmail.com",
                recipient_list=[user_email],
            )
            
            messages.add_message(request, messages.INFO, "Your job application has been submitted.") 
            return redirect("jobs")

    else:
        apply_job = JobApplicationForm()
        job_detail = Post_Job.objects.get(slug=slug)

    return render(
        request, "job_detail.html", {"job_detail": job_detail, "apply_job": apply_job}
    )
