from django.http import HttpResponseRedirect
from django.urls import reverse, reverse_lazy
from django.views import generic

from todo.models import Task, Tag


class TaskListView(generic.ListView):
    model = Task


class TaskCreateView(generic.CreateView):
    model = Task
    fields = "__all__"
    success_url = "/"


class TaskUpdateView(generic.UpdateView):
    model = Task
    fields = "__all__"
    success_url = "/"


class TaskDeleteView(generic.DeleteView):
    model = Task
    success_url = "/"


class TagListView(generic.ListView):
    model = Tag


class TagCreateView(generic.CreateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagUpdateView(generic.UpdateView):
    model = Tag
    fields = "__all__"
    success_url = reverse_lazy("todo:tag-list")


class TagDeleteView(generic.DeleteView):
    model = Tag
    success_url = reverse_lazy("todo:tag-list")


def changer_status_task(request, pk):
    task = Task.objects.get(pk=pk)
    task.done = not task.done
    task.save()
    return HttpResponseRedirect(reverse_lazy("todo:task-list"))
