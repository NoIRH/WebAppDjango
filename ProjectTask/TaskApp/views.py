from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from TaskApp.models import Task

def index(request):
   return render(request, 'index.html')

def listTasks(request):
   tasks = Task.objects.all()
   template = loader.get_template('taskList.html')
   context = {
      'listTasks' : tasks
   }
   return HttpResponse(template.render(context, request))

def addTask(request):
   if request.method == "POST":
      task = request.POST.get("task", "ничего!")
      Task.objects.create(task=task)
   return HttpResponse(render(request, 'addTask.html'))

def task(request, id_task):
   task = Task.objects.all()[id_task]
   return HttpResponse(f"<h2>Список дел</h2> {task}")

def delete(request, task_id):
   try:
      Task.objects.filter(id=task_id).delete()
      return HttpResponseRedirect("../list")
   except:
      return HttpResponseNotFound()

def update(request, task_id):
   return HttpResponse(render(request, 'addTask.html'))