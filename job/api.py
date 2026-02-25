from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Post_Job
from . Serializer import Post_JobSerializer
from rest_framework import generics

@api_view(['GET'])
def job_list_api (request):
    jobs = Post_Job.objects.all()
    data = Post_JobSerializer(jobs, many=True).data
    return Response({"data":data})

@api_view(['GET'])
def job_detail_api (request, id):
    job_detail = Post_Job.objects.get(id=id)
    data = Post_JobSerializer(job_detail).data
    return Response({"data":data})


class JobListApi(generics.ListAPIView):
    queryset = Post_Job.objects.all()
    serializer_class = Post_JobSerializer
    
class JobListCreateApi(generics.ListCreateAPIView):
    queryset = Post_Job.objects.all()
    serializer_class = Post_JobSerializer
    
class JobDetailApi(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post_Job.objects.all()
    serializer_class = Post_JobSerializer
    lookup_field = 'id'