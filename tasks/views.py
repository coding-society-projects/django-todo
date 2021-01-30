from django.shortcuts import render
from django.http import HttpResponse
from .models import Task

def index(request):
    tasks = Task.objects.filter(user_id=2).order_by('date_posted')
    context = {'tasks': tasks}
    return render(request, 'tasks/index.html', context)

def about(request):
    return HttpResponse("About")
