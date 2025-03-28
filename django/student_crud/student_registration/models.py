from django.db import models

# Create your models here.
class Registration(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Others'),
    ]

    BRANCH_CHOICES = [
        ('CS', 'Computer Science'),
        ('EC', 'Electronics & Communication'),
        ('ME', 'Mechanical'),
        ('CS', 'Civil'),
    ]

    name = models.CharField(max_length=100)
    age = models.IntegerField()
    usn = models.CharField(max_length=10, unique=True)
    branch = models.CharField(max_length=50, choices=BRANCH_CHOICES)
    sem = models.IntegerField()
    course = models.CharField(max_length=50)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    email_id = models.EmailField()
    hobbies = models.JSONField(default=list)
    address = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='images/', blank=True, null=True)
    resume_pdf = models.FileField(upload_to='pdfs/', blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

