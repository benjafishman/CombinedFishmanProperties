from django.shortcuts import render
from django.http import HttpResponse

from .models import Property
# Create your views here.

def index(request):
    properties = Property.objects.all()
    context = {'properties': properties, 'title':'cfp' }
    return render(request, 'properties/home.html', context)

def contact(request):
    context = {'title':'Contact' }
    return render(request,'properties/contact.html', context)

def about(request):
    context = {'title':'About Us' }
    return render(request,'properties/about.html', context)