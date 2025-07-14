from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register_view, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),

    path('teacher/dashboard/', views.dashboard_teacher, name='dashboard_teacher'),
    path('student/dashboard/', views.dashboard_student, name='dashboard_student'),

    path('quiz/create/', views.create_quiz, name='create_quiz'),
    path('question/add/', views.add_question, name='add_question'),
    path('quiz/<int:quiz_id>/attempt/', views.attempt_quiz, name='attempt_quiz'),

    
    path('question/edit/<int:question_id>/', views.edit_question, name='edit_question'),
    path('question/delete/<int:question_id>/', views.delete_question, name='delete_question'),

    path('edit-profile/', views.edit_profile, name='edit_profile'),


    


]
