from django.shortcuts import render, redirect
from django.urls import reverse
from . import models
from cars.forms import ReviewForm


# Create your views here.
def list_car(request):
    all_cars = models.Car.objects.all()
    context = {'all_cars': all_cars}
    return render(request, 'cars/list_car.html', context=context)


def delete_car(request):
    if request.POST:
        pk = request.POST['pk']
        try:
            car = models.Car.objects.filter(pk=pk)
            car.delete()
            return redirect(reverse('cars:list_car'))
        except BaseException as e:
            print(e.args)
            return redirect(reverse('cars:list_car'))
    else:
        return render(request, 'cars/delete_car.html', {})


def add_car(request):
    if request.POST:
        brand = request.POST['brand']
        year = int(request.POST['year'])
        models.Car.objects.create(brand=brand, year=year)

        # if user submitted new car --> List.html
        return redirect(reverse('cars:list_car'))
        # return list_car(request)
    else:
        return render(request, 'cars/add_car.html', {})

def rental_review(request):
    #POST REQUEST --> Form CONTENTS --> Thank you page
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
           # print(form.cleaned_data)
           # {'first_name': 'Adm', 'last_name': 'Petrovich', 'email': 'job8@i.ua', 'review': '55'}
           return redirect(reverse('cars:thank_you', kwargs={}))
    else:
        form = ReviewForm()
        return render(request, 'cars/rental_review.html',context={'form':form})

def thank_you(request):
    return render(request, 'cars/thank_you.html',{})
