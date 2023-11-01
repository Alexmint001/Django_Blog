from blog.models import Category, Tag, Comment

def categories(request):
    return {
        'categories': Category.objects.all(),
            }

def tags(request):
    return {
        'tags': Tag.objects.all(),
            }
