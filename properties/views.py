from django.shortcuts import get_object_or_404, render
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

def propertyDetail(request, property_id):
    property = get_object_or_404(Property, pk=property_id)
    loop_times = range(0,property.number_of_layouts)
    return render(request, 'properties/detail.html', {'property': property, 'loop_times': loop_times})