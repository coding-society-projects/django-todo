from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Task
import json
from django.core.serializers.json import DjangoJSONEncoder

def index(request):
    tasks = Task.objects.filter(user_id=2).order_by('date_posted')
    context = {'tasks': tasks}
    return render(request, 'tasks/index.html', context)

def api_tasks(request):
    tasks = Task.objects.filter(user_id=2).values('id', 'content', 'completed')
    data = list(tasks)
    return HttpResponse(json.dumps(data), content_type="application/json")

def complete(request, id):
    task = Task.objects.filter(pk=id).update(completed=1)
    return redirect(index)

def about(request):
    return HttpResponse("About")
