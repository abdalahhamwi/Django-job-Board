from django.urls import path
from . import views

urlpatterns = [
    path("", views.jobs_views, name="jobs"),
    path("job_detail/<int:id>", views.job_detail_views, name="job_detail"),
]
