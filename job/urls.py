from django.urls import path
from . import views
from . import api

urlpatterns = [
    path("", views.jobs_views, name="jobs"),
    path("job_detail/<str:slug>", views.job_detail_views, name="job_detail"),
    
    # api
    path("api/list", api.job_list_api, name="job_list_api"),
    path("api/jobs/<int:id>", api.job_detail_api, name="job_detail_api"),
    
    
    #class based view
    path("api/v2/list", api.JobListApi.as_view(), name="JobListApi"),
    path("api/v2/jobs/<int:id>", api.JobDetailApi.as_view(), name="job_detail_api"),
    path("api/v2/ListCreate/", api.JobListCreateApi.as_view(), name="JobListCreateApi"),
]
