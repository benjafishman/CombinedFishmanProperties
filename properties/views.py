from django.shortcuts import render
from django.http import HttpResponse

from .models import Property
# Create your views here.

def index(request):
    properties = Property.objects.all()
    print(properties)
    context = {'properties': properties }
    return render(request, 'properties/home.html', context)