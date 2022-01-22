from django.shortcuts import render
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages

from .forms import ContactForm
from .models import Contact


def contact(request):
    """
    Function allows to send email to website administrator.
    """
    def contact(request):
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')
        email = request.POST.get('email', '')
        if subject and message and email:
            try:
                send_mail(subject, message, email, ['deluxecoffeeshop@example.com'])
            except BadHeaderError:
                return HttpResponse('Invalid header found.')
            return HttpResponseRedirect('/contact/thanks/')
        else:
            # In reality we'd use a form class
            # to get proper validation errors.
            return HttpResponse('Make sure all fields are entered and valid.')
    
    return render(request, 'contact/contact.html')
