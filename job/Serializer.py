from rest_framework import serializers
from home.models import Post_Job

class Post_JobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post_Job
        fields = '__all__'