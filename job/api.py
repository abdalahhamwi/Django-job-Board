from rest_framework.decorators import api_view
from rest_framework.response import Response
from home.models import Post_Job
from . Serializer import Post_JobSerializer

@api_view(['GET'])
def job_list_api (request):
    jobs = Post_Job.objects.all()
    data = Post_JobSerializer(jobs, many=True).data
    return Response({"data":data})