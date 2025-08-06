from django.contrib.auth import get_user_model

User = get_user_model()

# List of superusers to create (add as many as needed)
superusers = [
    {
        'username': 'annregar',
        'email': 'annregar@email.com',
        'password': 'annregar'
    },
    {
        'username': 'lester',
        'email': 'annregar@email.com',
        'password': 'annregar'
    },
    {
        'username': 'pat',
        'email': 'annregar@email.com',
        'password': 'annregar'
    }
]

for user_data in superusers:
    if not User.objects.filter(username=user_data['username']).exists():
        User.objects.create_superuser(
            username=user_data['username'],
            email=user_data['email'],
            password=user_data['password']
        )
        print(f"✅ Superuser '{user_data['username']}' created.")
    else:
        print(f"ℹ️ Superuser '{user_data['username']}' already exists.")
