from django.shortcuts import render
from .models import Cinema, Movie, Screening

def project_info(request):
    Cinema = Cinema.objects.all()
    Movie = Movie.objects.all()
    Screening = Screening.objects.all()

    # Передаем данные в шаблон
    return render(request, 'project_info.html', {
        'project_name': 'Лабораторна робота №8',  
        'student_name': 'Павлов Владислав Юрійович',
        'student_group': 'КБ21015Б',
        'Cinema': Cinema,
        'Movie': Movie,
        'Screening': Screening,
    })
