from django.shortcuts import redirect, render
from .models import Property
from django.db.models import Q

# Create your views here.
def home(request):
    return render(request, 'properties/home.html')

def search(request):
    compound_name = request.GET.get('compound-name')
    compounds = Property.objects.filter(Q(Name__contains=compound_name) | Q(Formula__contains=compound_name))
    print(compounds)
    context = {
        'compounds' : compounds
    }
    return render(request, 'properties/search.html', context)
    # print(compound)
    # return redirect('properties:detail', compound.pk)

def detail(request, pk):
    compound = Property.objects.get(pk=pk)
    context = {
        'compound' : compound,
    }
    return render(request, 'properties/detail.html', context)
