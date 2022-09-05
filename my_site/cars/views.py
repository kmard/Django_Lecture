from django.shortcuts import render

# Create your views here.
def list_car(request):
    return render(request,'cars/list_car.html',{})

def delete_car(request):
    return render(request,'cars/delete_car.html',{})

def add_car(request):
    return render(request,'cars/add_car.html',{})