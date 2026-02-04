from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from django.core.mail import send_mail
from .tasks import send_email


# Create your views here.


def contact_view(request):

    if request.method == "POST":
        add_contact = ContactForm(request.POST)
        if add_contact.is_valid():
            add_contact.save()
            
            # call celery task
            send_email.delay()
            
            return redirect("home")
        
    else:
        add_contact = ContactForm()

    return render(request, "contact.html", {"add_contact": ContactForm})
