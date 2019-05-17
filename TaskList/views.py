from django.shortcuts import render,redirect,reverse
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import ToDoList
from .forms import AddTaskForm, UpdateTaskForm


# Function to list the tasks and completed tasks
@login_required
def task_list(request):
    tasks = ToDoList.objects.filter(user=request.user)
    completed_tasks = ToDoList.objects.filter(user=request.user).filter(completed__exact='True')

    context = {
        'tasks': tasks,
        'Completed_tasks': completed_tasks
    }

    return render(request, 'TaskList/list.html', context=context)


# Detail of a specific task
def task_detail(request, id):
    task = get_object_or_404(ToDoList, id=id)

    context = {
        'task':task,
    }

    return render(request, 'TaskList/detail.html', context=context)


# Adding a new task
def task_new(request):

    form = AddTaskForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect(reverse('list'))

    return render(request, 'TaskList/add.html', {'form': form})
    # if request.method == "POST":
    #     title = request.POST['title']
    #     description = request.POST['description']
    #     completed = request.POST['completed']
    #     if 'created_date' in request.POST:
    #         created_date = request.POST['created_date']
    #     else:
    #         created_date = False
    #     if 'due_date' in request.POST:
    #         due_date = request.POST['due_date']
    #     else:
    #         due_date = False
    #     task = ToDoList(title=title,
    #                     description=description,
    #                     created_date=created_date,
    #                     due_date=due_date,
    #                     completed=completed)
    #     task.save()
    #     return redirect(reverse('list'))
    # else:
    #     return render(request, 'TaskList/add.html')
    #


def task_delete(request,id):
    task = get_object_or_404(ToDoList, id=id)

    task.delete()
    return redirect(reverse('list'))


def task_update(request,id):
    task = get_object_or_404(ToDoList, id=id)

    if request.method == "POST":
        form = UpdateTaskForm(request.POST, instance=task)
        if form.is_valid():
            task.description = form.cleaned_data['description']
            print(task)
            task.save()
            form.save()
            print(task)
            return redirect(reverse('list'))

    else:
        form = UpdateTaskForm(instance=task)

    context = {
        'form':form,
        'task':task,
    }

    return render(request, 'TaskList/update.html', context)
