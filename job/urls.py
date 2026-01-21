from django.urls import path
from . import views

urlpatterns = [
    path("", views.job_views, name="job_views"),
    path("job_details", views.job_detail_views, name="job_detail_views"),
]
