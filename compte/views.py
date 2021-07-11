from django.shortcuts import render
from .models import *

# Create your views here.
def accueil(request): 
    return render(request,'compte/base.html')

def dashboard(request): 
    enf=Enfant.objects.all()
    total=enf.count()

    context={
        'enf':enf,
        'total': total,
    }
    return render(request,'compte/dashboard.html',context)

def cantine(request): 
    enf=Cantine.objects.all()
    total4J=enf.filter(type_cantine='4j').count()
    total5J=enf.filter(type_cantine='5j').count()
    context={
        'enf':enf,
        'total4J' : total4J,
        'total5J' : total5J,
    }
    return render(request,'compte/cantine.html', context)

def assurance(request): 
    enf=Assurance.objects.all()
    ASSURE=enf.filter(assure='OUI').count()
    NON_ASSURE=enf.filter(assure='NON').count()
    context={
        'enf':enf,
        'ASSURE' : ASSURE,
        'NON_ASSURE' : NON_ASSURE,
    }
    return render(request,'compte/assurance.html', context)