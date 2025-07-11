from django.urls import path
from . import views

urlpatterns = [
    path('', views.quiz_list, name='quiz_list'),

    # User and Role Management
    path('register/', views.register_user, name='register_user'),
    path('create-role/', views.create_role, name='create_role'),
    path('assign-permission/', views.assign_role_permission, name='assign_permission'),

    # Question & Quiz Creation
    path('question-type/', views.create_question_type, name='create_question_type'),
    path('create-question/', views.create_question, name='create_question'),
    path('create-quiz/', views.create_quiz, name='create_quiz'),
    path('assign-question/', views.assign_question_to_quiz, name='assign_question_to_quiz'),

    # Quiz Participation
    path('attend-quiz/', views.attend_quiz, name='attend_quiz'),
    path('submit-answer/', views.submit_answer, name='submit_answer'),

    # View Quiz Details
    path('quiz/<int:quiz_id>/', views.quiz_detail, name='quiz_detail'),
]
