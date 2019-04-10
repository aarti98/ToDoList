from django.urls import path
from . import views


urlpatterns = [
    path('list/', views.task_list, name='list'),
    path('detail/<int:id>/', views.task_detail, name='detail'),
    path('add/', views.task_new, name='add'),
    path('delete/<int:id>/', views.task_delete, name='delete'),
    path('update/<int:id>', views.task_update, name='update')
]