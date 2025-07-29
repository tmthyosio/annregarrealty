from .models import Developer
from django.db.utils import ProgrammingError, OperationalError

def developer_nav(request):
    try:
        developers = Developer.objects.all()
    except (ProgrammingError, OperationalError):
        developers = []
    return {
        'all_developers': developers
    }
