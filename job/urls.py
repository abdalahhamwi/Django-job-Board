from django.urls import path
from . import views
from . import api


urlpatterns = [
    path("", views.jobs_views, name="jobs"),
    path("job_detail/<str:slug>", views.job_detail_views, name="job_detail"),
    # api
    path("api/list", api.job_list_api, name="job_list_api"),
    
    
]
