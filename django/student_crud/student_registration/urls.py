from django.urls import path
from . import views

urlpatterns = [
    path('', views.registration_list, name='list'),
    path('create', views.registration_form, name='form'),
    path('view/', views.view_registration, name='view'),
    path('delete/', views.delete_registration, name='delete'),
]