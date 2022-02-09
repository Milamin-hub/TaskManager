from django.shortcuts import render, redirect

from .forms import TaskForm
from .models import Task


# Create your views here.
def index(request):
    tasks = Task.objects.order_by('-pk')
    return render(request, 'main/index.html', {'title': 'Главная страница', 'tasks': tasks})


def about(request):
    return render(request, 'main/about.html', {'title': 'О нас'})


def edit(request, id):
    try:
        task = Task.objects.get(id=id)
        if request.method == "POST":
            task.title = request.POST.get("title")
            task.content = request.POST.get("content")
            task.save()
            return redirect('home')
        else:
            return render(request, "main/edit.html", {"task": task})
    except Task.DoesNotExist:
        return render('home')


def delete(request, id):
    try:
        if request.method == "GET":
            task = Task.objects.get(id=id)
            task.delete()
            return redirect('home')
    except Exception as e:
        print(e)
        return redirect('home')

def create(request):
    error = ''
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма заполнена неверно'
    form = TaskForm()
    return render(request, 'main/create.html', {'title': 'Cоздать Задание', 'form': form})