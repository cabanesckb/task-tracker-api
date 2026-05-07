from django.urls import path

from . import views

app_name = 'tasks'
urlpatterns = [
    path("", views.index, name="index"),
    path("update/<int:task_id>/", views.update_task, name="update_task"),
    path("delete/<int:task_id>/", views.delete_task, name="delete_task"),
    path("add/", views.add_task, name="add_task"),
    
]