from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm
# from .tasks import send_message_task
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.

def contact_view(request):
    if request.method == "POST":
        add_contact = ContactForm(request.POST)
        if add_contact.is_valid():
            add_contact.save() 
            
            user_subject  = add_contact.cleaned_data["subject"]
            user_email = add_contact.cleaned_data["email"]
            user_msg   = add_contact.cleaned_data["message"]
            
            # رسالة للمستخدم
            send_mail(
                subject="Thanks for contacting us!",
                message="Hello! We received your message and will reply soon.",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[user_email],
            )

            # رسالة لشركتي
            send_mail(
                subject="New contact message",
                message=f"New message from ({user_email}):\n\n{user_msg}",
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],
            )
        
        messages.add_message(request, messages.INFO, "Your message has been sent successfully.") 
        return redirect("contact")
        
    else:
        add_contact = ContactForm()
        
    return render(request, "contact.html", {"add_contact": ContactForm})