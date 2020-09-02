from django.contrib import admin
from .models import Project

#this line of code adds this model inside of the admin online
admin.site.register(Project)
