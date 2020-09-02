from django.shortcuts import render
from .models import Project #to get the objects from the database so we can pass them to the html template(s)

def home(request):
    projects = Project.objects.all() #grabs all of the objects from the database, turns them into Python objects, and puts them into a list (or QuerySet, same thing)
    return render(request, 'portfolio/home.html', {'Projects': projects})
