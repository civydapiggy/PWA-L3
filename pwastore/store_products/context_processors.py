from .models import Category

def category_links(request):
    try:
        cats = Category.objects.filter(primaryCategory=True).order_by('title')  # <-- only primary
        if not cats.exists():
            # fallback to all if none marked primary (prevents empty nav during setup)
            cats = Category.objects.all().order_by('title')
    except Exception:
        cats = []
    return {'categories': cats}