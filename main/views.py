from django.shortcuts import render, redirect
from . import models
from .forms import TaskForm


def index(request):
    tasks = models.Task.objects.order_by('-id')#[:1] #<-- выбирает записи. сейчас только одна
     #find() = search   order_by() = filter, можно сотроравать по ид. тайтл. таск
    return render(request, 'index.html', {'title': 'Главная страница сайта', 'tasks': tasks})


def about(request):
    return render(request, 'about.html')


def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма была неверной'

    form = TaskForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'create.html', context )