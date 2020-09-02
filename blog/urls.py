from django.urls import path
from . import views

app_name = "blog"

urlpatterns = [
    path('', views.all_blogs, name='all_blogs'),
    path('<int:blog_id>/', views.detail, name='detail'), # it saves the integer in the variable "blog_id" and passes it to the detail function in views
]
