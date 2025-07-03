from django.db import models

# Create your models here.
class User(models.Model):
    id = models.IntegerField()
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.IntegerField()
    password = models.PasswordField(max_length=50)
    role_id = models.IntegerField(FK)

    def __str__(self):
        return self.name

class Role(models.Model):
    id = models.IntegerField()
    role_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Permission_list(models.Model):
    id = models.IntegerField()
    name = models.CharField()

    def __str__(self):
        return self.name

class Role_permission(models.Model):
    id = models.IntegerField()
    role_id = models.IntegerField(FK)
    Permission_id = models.IntegerField(FK)

    def __str__(self):
        return self.name

class Question_type(models.Model):
    id = models.IntegerField()
    type = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Question(models.Model):
    id = models.IntegerField()
    qt_id = models.IntegerField(FK)
    question = models.TextField()
    options = models.TextField()
    key_answer = models.CharField()
    marks = models.IntegerField()
    explaination = models.TextField()
    difficulty_level = models.CharField
    created_by = models.IntegerField(FK)

    def __str__(self):
        return self.name

class Quiz(models.Model):
    id = models.IntegerField()
    title = models.CharField()
    points = models.IntegerField()
    duration = models.IntegerField()
    total_marks = models.IntegerField()
    created_by = models.IntegerField()
    publish_date = models.DateField()
    is_active = models.j()

    def __str__(self):
        return self.name

class Quiz_question(models.Model):
    id = models.IntegerField()
    quiz_id = models.IntegerField()
    question_id = models.IntegerField()
    order = models.IntegerField()
    marks =models.IntegerField()

     def __str__(self):
        return self.name

class Attend_quiz(models.Model):
    id = models.IntegerField()
    user_id = models.IntegerField()
    quiz_id = models.IntegerField()
    time_taken = models.IntegerField()
    final_score = models.IntegerField()
    quiz_completed = models.BooleanField()
    number_of_question = models.IntegerField()
    Attend_number = models.IntegerField()
    started_at = models.DateField()
    submitted_at = models.DateField()
    status = models.CharField() 

     def __str__(self):
        return self.name

class Answer(models.Model):
    id = models.IntegerField()
    attend_quiz_id = models.IntegerField()
    question_id = models.IntegerField()
    selected_option = models.CharField()
    is_correct = models.BooleanField()

    def __str__(self):
        return self.name


        





