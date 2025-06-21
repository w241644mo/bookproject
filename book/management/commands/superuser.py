import os
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model
from django.conf import settings

User = get_user_model()

class Command(BaseCommand):
    def handle(self, *args, **options):
        username = os.environ.get("SUPERUSER_NAME")
        password = os.environ.get("SUPERUSER_PASS")
        email = os.environ.get("SUPERUSER_EMAIL", "admin@example.com")  # デフォルトメール

        if not username or not password:
            self.stderr.write("SUPERUSER_NAME and SUPERUSER_PASS must be set in environment.")
            return

        if not User.objects.filter(username=username).exists():
            User.objects.create_superuser(
                username=username,
                email=email,
                password=password
            )
            self.stdout.write(self.style.SUCCESS(f"Superuser '{username}' created."))
        else:
            self.stdout.write(f"Superuser '{username}' already exists.")
        #if not User.objects.filter(username='tail').exists():
         #   User.objects.create_superuser(
          #      username = os.environ.get("SUPERUSER_NAME"),
           #     email = os.environ.get("SUPERUSER_EMAIL", "admin@example.com"),
            #    password = os.environ.get("SUPERUSER_PASS"),
            #)
        
