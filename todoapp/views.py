from django.shortcuts import render, redirect
from . models import *
from . forms import *
# Create your views here.
def index(request):
  todos = Todo.objects.all()
  form = TodoForm()
  if request.method == 'POST':
    form = TodoForm(request.POST)
    if form.is_valid():
      form.save()
      return redirect ('home')
  context = {'todos': todos, 'form': form}
  return render(request, 'todoapp/home.html', context)