from django.shortcuts import render, redirect
from .models import Program


def program_list(request):
    programs = Program.objects.all()
    ctx = {'programs': programs}
    return render(request, 'program/prog_lang_list.html', ctx)

def add_prog_lang(request):
    language_name = request.POST.get('language_name')
    description = request.POST.get('description')
    if language_name and description:
        Program.objects.create(
            language_name=language_name,
            description=description
        )
        return redirect('programs:prog_list')
    else:
        return render(request, 'program/add_prog_lang.html')
