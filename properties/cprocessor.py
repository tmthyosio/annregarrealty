from .models import Developer

def developer_nav(request):
    return {
        'all_developers': Developer.objects.prefetch_related('subdivision_set').all()
    }
