import os
from django.contrib.auth import get_user_model

User = get_user_model()

username = os.getenv('DJANGO_SUPERUSER_USERNAME', 'ANNREGAR')
email = os.getenv('DJANGO_SUPERUSER_EMAIL', 'annregar@email.com')
password = os.getenv('DJANGO_SUPERUSER_PASSWORD', 'ANNREGAR123')

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print("Superuser created successfully.")
else:
    print("Superuser already exists.")
