from django import forms
from .models import Job, Category


class JobForm(forms.ModelForm):
    class Meta:
        model = Job
        fields = ['title', 'location', 'job_type', 'description', 'vacancy', 'salary', 'category', 'experience' , 'published_at' ]
        
        widgets = {
            "title": forms.TextInput(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "job_type": forms.Select(attrs={"class": "form-control"}),
            "description": forms.Textarea(attrs={"class": "form-control"}),
            "vacancy": forms.NumberInput(attrs={"class": "form-control"}),
            "salary": forms.NumberInput(attrs={"class": "form-control"}),
            "category": forms.Select(attrs={"class": "form-control"}),
            "experience": forms.TextInput(attrs={"class": "form-control"}),
            "published_at": forms.DateTimeInput(attrs={"class": "form-control"}),
        }

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ['name']
        
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
        }