from django.contrib import admin
from .models import Blog

#this line of code adds this model inside of the admin online. Registers the model(s)
admin.site.register(Blog)
