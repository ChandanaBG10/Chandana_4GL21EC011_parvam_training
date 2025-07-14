from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Quiz, Question, User, Role, Answer
from .forms import UserForm, LoginForm, QuizForm, QuestionForm, EditProfileForm

# -------------------- Home --------------------
def home(request):
    return render(request, 'quiz/home.html')

# -------------------- Registration --------------------
def register_view(request):
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()
            return redirect('login')
    else:
        form = UserForm()
    return render(request, 'quiz/register.html', {'form': form})

# -------------------- Login --------------------
def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)

            if user:
                login(request, user)
                if user.role.role_name == 'Teacher':
                    return redirect('dashboard_teacher')
                elif user.role.role_name == 'Student':
                    return redirect('dashboard_student')
                else:
                    return redirect('home')
            else:
                form.add_error(None, "Invalid email or password")
    else:
        form = LoginForm()
    return render(request, 'quiz/login.html', {'form': form})

# -------------------- Logout --------------------
@login_required
def logout_view(request):
    logout(request)
    return redirect('home')

# -------------------- Teacher Dashboard --------------------
@login_required
def dashboard_teacher(request):
    if request.user.role.role_name != 'Teacher':
        return HttpResponseForbidden()
    quizzes = Quiz.objects.filter(created_by=request.user)
    return render(request, 'quiz/dashboard_teacher.html', {'quizzes': quizzes})

# -------------------- Student Dashboard --------------------
@login_required
def dashboard_student(request):
    if request.user.role.role_name != 'Student':
        return HttpResponseForbidden()
    quizzes = Quiz.objects.all()
    return render(request, 'quiz/dashboard_student.html', {'quizzes': quizzes})

# -------------------- Create Quiz --------------------
@login_required
def create_quiz(request):
    if request.user.role.role_name != 'Teacher':
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = QuizForm(request.POST)
        if form.is_valid():
            quiz = form.save(commit=False)
            quiz.created_by = request.user
            quiz.save()
            return redirect('dashboard_teacher')
    else:
        form = QuizForm()
    return render(request, 'quiz/quiz_create.html', {'form': form})

# -------------------- Add Question --------------------
@login_required
def add_question(request):
    if request.user.role.role_name != 'Teacher':
        return HttpResponseForbidden()

    if request.method == 'POST':
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('add_question')
    else:
        form = QuestionForm()

    questions = Question.objects.all()
    return render(request, 'quiz/question_add.html', {'form': form, 'questions': questions})

# -------------------- Edit Question --------------------
@login_required
def edit_question(request, question_id):
    if request.user.role.role_name != 'Teacher':
        return HttpResponseForbidden()

    question = get_object_or_404(Question, id=question_id)

    if request.method == 'POST':
        form = QuestionForm(request.POST, instance=question)
        if form.is_valid():
            form.save()
            return redirect('add_question')
    else:
        form = QuestionForm(instance=question)

    return render(request, 'quiz/question_edit.html', {'form': form, 'question': question})

# -------------------- Delete Question --------------------
@login_required
def delete_question(request, question_id):
    if request.user.role.role_name != 'Teacher':
        return HttpResponseForbidden()

    question = get_object_or_404(Question, id=question_id)
    question.delete()
    return redirect('add_question')

# -------------------- Attempt Quiz --------------------
@login_required
def attempt_quiz(request, quiz_id):
    quiz = get_object_or_404(Quiz, id=quiz_id)
    questions = quiz.questions.all()

    if request.method == 'POST':
        score = 0
        for question in questions:
            user_answer = request.POST.get(f'question_{question.id}')
            if user_answer and user_answer == question.correct_option:
                score += 1
        return render(request, 'quiz/quiz_result.html', {
            'quiz': quiz,
            'score': score,
            'total': questions.count()
        })

    return render(request, 'quiz/quiz_attempt.html', {
        'quiz': quiz,
        'questions': questions
    })

# -------------------- Edit Profile --------------------@login_required

@login_required
def edit_profile(request):
    user = request.user

    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=user)
        if form.is_valid():
            updated_user = form.save(commit=False)
            new_password = form.cleaned_data.get('password')
            if new_password:
                updated_user.set_password(new_password)  # ✅ securely hash the new password
            updated_user.save()

            # ✅ Re-login the user after password change
            from django.contrib.auth import update_session_auth_hash
            update_session_auth_hash(request, updated_user)

            if user.role.role_name == 'Teacher':
                return redirect('dashboard_teacher')
            else:
                return redirect('dashboard_student')
    else:
        form = EditProfileForm(instance=user)

    return render(request, 'quiz/edit_profile.html', {'form': form})
