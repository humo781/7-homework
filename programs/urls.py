from django.urls import path
from .views import program_list, add_prog_lang

app_name = 'programs'
urlpatterns = [
    path('program_list/', program_list, name='prog_list'),
    path('add_prog_lang/', add_prog_lang, name='add_prog_lang')
]
