from django.contrib import admin
from .models import Post, Comment, Tag, Category, Recomment
admin.site.register(Tag)
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Recomment)
admin.site.register(Category)
