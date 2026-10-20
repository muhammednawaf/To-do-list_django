from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse
from tasks.models import Tasks
from django.views.decorators.http import require_POST

# Create your views here.
def home(req):
    if(req.method == 'POST'):
        Tasks.objects.create(title = req.POST.get('title'))
        return redirect('home')
    else:
        data = Tasks.objects.all()
        return render(req,"tasks/index.html",{"tasks":data})

@require_POST
def update(req,task_id):
    task = get_object_or_404(Tasks,id=task_id)
    task.completed = True
    task.save()
    return redirect('home')

@require_POST
def delete(req,task_id):
    task = get_object_or_404(Tasks,id=task_id)
    task.delete()
    return redirect('home')