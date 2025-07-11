
from django.db import models

# Create your models here.

class Role(models.Model):
    role_name = models.CharField(max_length=100)

    def __str__(self):
        return self.role_name
      
class User(models.Model):
    
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.CharField(max_length=50)
    role_name= models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.name



class RolePermission(models.Model):

    role_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    Permission_id = models.ForeignKey(Role, on_delete=models.CASCADE)

    def __str__(self):
        return self.name

class QuestionType(models.Model):
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Question(models.Model):
    qt_id = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    question = models.TextField()
    options = models.TextField()
    key_answer = models.CharField(max_length=100)
    marks = models.IntegerField()

    def __str__(self):
        return self.name

class Quiz(models.Model):
    title = models.CharField(max_length=100)
    points = models.IntegerField()
    duration = models.IntegerField()
    total_marks = models.IntegerField()

    def __str__(self):
        return self.name

class QuizQuestion(models.Model):
    quiz_id = models.ForeignKey(Quiz, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    marks =models.IntegerField()

    def __str__(self):
        return self.name

class AttendQuiz(models.Model):
    user_id = models.ForeignKey(Role, on_delete=models.CASCADE)
    quiz_id = models.IntegerField(QuizQuestion, on_delete=models.CASCADE)
    time_taken = models.IntegerField()
    final_score = models.IntegerField()
    quiz_completed = models.BooleanField()
    number_of_question = models.IntegerField()
    Attend_number = models.IntegerField()
    started_at = models.DateField()
    submitted_at = models.DateField()


    def __str__(self):
        return self.name

class Answer(models.Model):
    
    attend_quiz_id = models.ForeignKey(AttendQuiz, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Question, on_delete=models.CASCADE)
    selected_option = models.CharField()
    is_correct = models.BooleanField()

    def __str__(self):
        return self.name


        





