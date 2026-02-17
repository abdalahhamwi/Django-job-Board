from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
from .tasks import send_message_task
from django.contrib import messages


# Create your views here.


def contact_view(request):
    if request.method == "POST":
        add_contact = ContactForm(request.POST)
        if add_contact.is_valid():
             contact_instance = add_contact.save() 
             
        send_message_task.delay(contact_instance.email)
        
        messages.add_message(request, messages.INFO, "Your message has been sent successfully.") 
        return redirect("contact")
        
        
    else:
        add_contact = ContactForm()
        
    return render(request, "contact.html", {"add_contact": ContactForm})