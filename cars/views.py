from django.shortcuts import render, redirect
from .models import Car


def car_list(request):
    cars = Car.objects.all()
    ctx = {'cars': cars}
    return render(request, 'car/car_list.html', ctx)

def add_car(request):
    car_name = request.POST.get('car_name')
    model = request.POST.get('model')
    year = request.POST.get('year')
    if car_name and model and year:
        Car.objects.create(
            car_name=car_name,
            model=model,
            year=year
        )
        return redirect('cars:car_list')
    else:
        return render(request, 'car/add_car.html')

def main_page(request):
    return render(request, 'main_page.html')
