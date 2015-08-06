from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse

from .models import Property
# Create your views here.

def index(request):
    properties = Property.objects.all().order_by('pk')
    context = {'properties': properties, 'title':'cfp' }
    return render(request, 'properties/home.html', context)

def contact(request):
    properties = Property.objects.all().order_by('pk')
    context = {'properties': properties, 'title':'Contact' }
    return render(request,'properties/contact.html', context)

def about(request):
    properties = Property.objects.all().order_by('pk')
    context = {'properties': properties, 'title':'About Us' }
    return render(request,'properties/about.html', context)

def propertyDetail(request, property_id):
    # Exclude the property being viewed from the drop down list of properties
    properties = Property.objects.all().exclude(pk=property_id).order_by('pk')
    property = get_object_or_404(Property, pk=property_id)
    loop_times = range(0,property.number_of_layouts)
    context = {'properties': properties, 'property': property, 'loop_times': loop_times}
    return render(request, 'properties/detail.html', context)