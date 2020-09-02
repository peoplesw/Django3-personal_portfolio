from django.shortcuts import render, get_object_or_404 # this function to selects an individual object or row from the database
from .models import Blog # the class/table we created in models

def all_blogs(request):
    #all_blogs = Blog.objects.all() #grabs all of the objects from the database, turns them into Python objects, and puts them into a list (or QuerySet, same thing)
    all_blogs = Blog.objects.order_by('-date')
    return render(request, 'blog/all_blogs.html', {"All_blogs": all_blogs})

def detail(request, blog_id):
    blog = get_object_or_404(Blog, pk=blog_id) # matches the int typed in with the id in the database
    return render(request, 'blog/detail.html', {'blog': blog})
