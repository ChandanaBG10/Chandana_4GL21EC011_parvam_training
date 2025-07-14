# quiz/apps.py

from django.apps import AppConfig

class QuizConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'quiz'

    def ready(self):
        from django.db.utils import OperationalError
        try:
            from .models import Role
            for role_name in ['Teacher', 'Student']:
                Role.objects.get_or_create(role_name=role_name)
        except OperationalError:
            pass

