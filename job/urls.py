from django.urls import path
from . import views

urlpatterns = [
    path("", views.jobs_views, name="jobs"),
    path("job_details", views.job_detail_views, name="job_detail"),
    path("<int:id>", views.job_detail_views, name="id"),
]
