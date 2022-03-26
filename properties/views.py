from django.shortcuts import redirect, render
from .models import Property
import numpy as np
import matplotlib.pyplot as plt

# Create your views here.
def home(request):
    return render(request, 'properties/home.html')

def search(request):
    compound_name = request.GET.get('compound-name')
    compound = Property.objects.get(Name=compound_name)
    print(compound)
    return redirect('properties:detail', compound.pk)

def detail(request, pk):
    compound = Property.objects.get(pk=pk)
    context = {
        'compound' : compound,
    }
    return render(request, 'properties/detail.html', context)
