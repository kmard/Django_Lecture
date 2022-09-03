from django.shortcuts import render
from . import models

# Create your views here.
def list_patients(request):
    all_patiets = models.Patient.objects.all()
    context = {'patients':all_patiets}
    return render(request,'office/list.html',context=context)