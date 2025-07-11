from django import forms
from .models import User, Role, RolePermission, Question, Quiz, QuizQuestion, AttendQuiz, Answer, QuestionType

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)
    
    class Meta:
        model = User
        fields = ['name', 'email', 'phone', 'password', 'role_name']


class RoleForm(forms.ModelForm):
    class Meta:
        model = Role
        fields = ['role_name']


class RolePermissionForm(forms.ModelForm):
    class Meta:
        model = RolePermission
        fields = ['role_id', 'Permission_id']


class QuestionTypeForm(forms.ModelForm):
    class Meta:
        model = QuestionType
        fields = ['type']


class QuestionForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = ['qt_id', 'question', 'options', 'key_answer', 'marks']


class QuizForm(forms.ModelForm):
    class Meta:
        model = Quiz
        fields = ['title', 'points', 'duration', 'total_marks']


class QuizQuestionForm(forms.ModelForm):
    class Meta:
        model = QuizQuestion
        fields = ['quiz_id', 'question_id', 'marks']


class AttendQuizForm(forms.ModelForm):
    class Meta:
        model = AttendQuiz
        fields = [
            'user_id', 'quiz_id', 'time_taken', 'final_score',
            'quiz_completed', 'number_of_question', 'Attend_number',
            'started_at', 'submitted_at'
        ]


class AnswerForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['attend_quiz_id', 'question_id', 'selected_option', 'is_correct']
