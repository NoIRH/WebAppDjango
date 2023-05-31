from django.urls import path
from . import views

urlpatterns = [
   path('', views.index),
   path('list', views.listTasks),
   path('add', views.addTask),
   path('<int:id_task>/', views.task, name='task'),
   path('updateTask/<int:task_id>', views.update),
   path('deleteTask/<int:task_id>', views.delete),
   path('addTask', views.addTask),
]