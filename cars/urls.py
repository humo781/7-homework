from django.urls import path
from .views import car_list, add_car, main_page

app_name = 'cars'
urlpatterns = [
    path('', main_page, name='main'),
    path('car_list/', car_list, name='car_list'),
    path('add_car/', add_car, name='add_car')
]
