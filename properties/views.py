from django.shortcuts import render
from .models import Property
from django.shortcuts import get_object_or_404
from .models import Developer
from .models import Subdivision

def property_detail(request, pk):
    property = get_object_or_404(Property, pk=pk)
    return render(request, 'properties/property_detail.html', {
        'property': property,
        'subdivision': property.subdivision
    })
def home(request):
    return render(request, 'properties/home.html')

def developer_list(request):
    developers = Developer.objects.all()
    return render(request, 'properties/developer_list.html', {
        'developers': developers
    })

def subdivision_properties(request, subdiv_id):
    subdivision = get_object_or_404(Subdivision, pk=subdiv_id)
    properties = Property.objects.filter(subdivision=subdivision)
    return render(request, 'properties/subdivision_properties.html', {
        'subdivision': subdivision,
        'properties': properties
    })