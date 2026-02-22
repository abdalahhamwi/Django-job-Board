import django_filters
from home.models import Post_Job

class Post_JobFilter(django_filters.FilterSet):
    job_title = django_filters.CharFilter(lookup_expr='icontains')
    Job_description = job_title
    location = django_filters.CharFilter(lookup_expr='icontains')
    
    class Meta:
        model = Post_Job
        fields = '__all__'
        exclude = ['photo_company','published_at','salary','Vacancy','slug','Responsibility']
        
        # Bootstrap styling
    def __init__(self, *args, **kwargs):
        super(Post_JobFilter, self).__init__(*args, **kwargs)
        for field in self.form.fields:
            self.form.fields[field].widget.attrs.update({
                'class': 'form-control',
                'placeholder': 'Search here...'
            })