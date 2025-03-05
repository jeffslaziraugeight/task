from django.shortcuts import render, get_object_or_404, redirect
from django.http import JsonResponse
from .models import Task
from .forms import TaskForm

def task_list(request):
    query = request.GET.get("q", "")  
    if query:
        tasks = Task.objects.filter(title__icontains=query)  
    else:
        tasks = Task.objects.all()

    form = TaskForm()
    return render(request, "tasks/task_list.html", {"tasks": tasks, "form": form, "query": query})  

def task_create(request):
    if request.method == "POST":
        form = TaskForm(request.POST)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
    return JsonResponse({"success": False, "errors": form.errors})

def task_update(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return JsonResponse({"success": True})
    return JsonResponse({"success": False, "errors": form.errors})

def task_delete(request, id):
    task = get_object_or_404(Task, id=id)
    if request.method == "POST":
        task.delete()
        return JsonResponse({"success": True})
    return JsonResponse({"success": False})
