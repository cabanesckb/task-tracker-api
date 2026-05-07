from django.urls import path
from . import api_views

app_name = 'api'
urlpatterns = [
    path("", api_views.TaskList.as_view(), name="task_list"),
    path("<int:task_id>/", api_views.TaskDetail.as_view(), name="task_detail"),
]