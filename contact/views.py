from django.shortcuts import render


def contact(request):
    """
    View to about company page.
    """

    return render(request, 'contact/contact.html')
