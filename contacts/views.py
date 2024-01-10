from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Contact

# Create your views here.
def contact(request):
    if request.method == 'POST':
       listing_id = request.POST['listing_id']
       realtor_email = request.POST['realtor_email']
       listing = request.POST['listing']
       name = request.POST['name']
       email = request.POST['email']
       phone = request.POST['phone']
       message = request.POST['message']
       user_id = request.POST['user_id']

       contact = Contact(listing=listing, listing_id=listing_id, user_id=user_id,
                         name=name, phone=phone, message=message, email=email)
       
       contact.save()
       messages.success(request, 'Your request has been submitted, a realtor\n'
                       'will get back to you soon')
       return redirect('/listings/'+listing_id)
        