from django import forms
from .models import Post_Job

class PostJobForm(forms.ModelForm):
    class Meta :
        model = Post_Job
        fields = "__all__"
        exclude = ["slug"]