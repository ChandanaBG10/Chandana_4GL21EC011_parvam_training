from django.urls import path
from . import views

urlpatterns = [
    path('', views.teacher_list, name="teacher-list"),
    path('create', views.create_teacher, name="create-teacher"),
    path('<int:pk>', views.view_teacher, name="view-teacher"),
    path('<int:pk>/edit/', views.edit_teacher, name="edit-teacher"),
    path('<int:pk>/delete/', views.delete_teacher, name="delete-teacher"),
    

]