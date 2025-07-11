from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .forms import (
    UserForm, RoleForm, RolePermissionForm, QuestionForm, QuestionTypeForm,
    QuizForm, QuizQuestionForm, AttendQuizForm, AnswerForm
)
from .models import Quiz, Question, Answer


# Register new user
def register_user(request):
    form = UserForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "User registered successfully.")
        return redirect('quiz_list')
    return render(request, 'register_user.html', {'form': form})


# Create Role
def create_role(request):
    form = RoleForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Role created.")
        return redirect('quiz_list')
    return render(request, 'create_role.html', {'form': form})


# Create RolePermission
def assign_role_permission(request):
    form = RolePermissionForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Permission assigned to role.")
        return redirect('quiz_list')
    return render(request, 'assign_permission.html', {'form': form})


# Create Question Type
def create_question_type(request):
    form = QuestionTypeForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Question type added.")
        return redirect('quiz_list')
    return render(request, 'create_question_type.html', {'form': form})


# Create Question
def create_question(request):
    form = QuestionForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Question added.")
        return redirect('quiz_list')
    return render(request, 'create_question.html', {'form': form})


# Create Quiz
def create_quiz(request):
    form = QuizForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Quiz created.")
        return redirect('quiz_list')
    return render(request, 'create_quiz.html', {'form': form})


# Assign Question to Quiz
def assign_question_to_quiz(request):
    form = QuizQuestionForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Question assigned to quiz.")
        return redirect('quiz_list')
    return render(request, 'assign_question.html', {'form': form})


# Submit an answer
def submit_answer(request):
    form = AnswerForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        answer = form.save(commit=False)
        # Validate answer correctness
        correct = answer.question_id.key_answer.strip().lower() == answer.selected_option.strip().lower()
        answer.is_correct = correct
        answer.save()
        messages.success(request, "Answer submitted.")
        return redirect('quiz_list')
    return render(request, 'submit_answer.html', {'form': form})


# Record quiz attempt
def attend_quiz(request):
    form = AttendQuizForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        form.save()
        messages.success(request, "Quiz attempt recorded.")
        return redirect('quiz_list')
    return render(request, 'attend_quiz.html', {'form': form})


# List available quizzes
def quiz_list(request):
    quizzes = Quiz.objects.all()
    return render(request, 'quiz_list.html', {'quizzes': quizzes})


# View quiz questions (Optional view)
def quiz_detail(request, quiz_id):
    quiz = get_object_or_404(Quiz, pk=quiz_id)
    questions = quiz.quizquestion_set.all()
    return render(request, 'quiz_detail.html', {'quiz': quiz, 'questions': questions})
