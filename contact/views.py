from django.shortcuts import render, redirect
from .models import Contact
from .forms import ContactForm

# Create your views here.


def contact_view(request):

    if request.method == "POST":
        add_contact = ContactForm(request.POST)
        if add_contact.is_valid():
            add_contact.save()
            return redirect("home")
    else:
        add_contact = ContactForm()

    return render(request, "contact.html", {"add_contact": ContactForm})
