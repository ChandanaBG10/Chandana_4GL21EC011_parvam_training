from django.urls import path
from . import views


urlpatterns = [
    path('', views.library_list, name="library-list"),
    path('create', views.create_library, name="create-library"),
    path('<int:pk>/', views.view_library, name="view-library"),
    path('<int:pk>/edit/', views.edit_library, name="edit-library"),
    path('<int:pk>/delete/', views.delete_library, name="delete-library"),
    

]