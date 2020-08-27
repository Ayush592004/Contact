from django.shortcuts import render, redirect
from .models import Contact
from django.contrib import messages

# Create your views here.
def contact(request):
    if request.method == 'POST':
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        content = request.POST['content']
        # Adding Basic Checks to Contact
        if len(content)<10:
            messages.error(request, "Your Message should contain atleast 10 characters")
            return redirect('/')
        # Contact Information
        else:
            allcontacts = Contact(fname=fname, lname=lname, email=email, content=content)
            allcontacts.save()
            messages.success(request, "Your Contact Form has been Submitted to us.")
        return redirect('/')
    return render(request, 'contact.html')
