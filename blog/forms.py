from django import forms
from .models import Post, Comment, Tag, Recomment

class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = ['name']
        
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['category', 'title', 'content', 'image_upload', 'tags'] # counter같은 값은 건들면 안되니까!

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['message']

class RecommentForm(forms.ModelForm):
    class Meta:
        model = Recomment
        fields = ['message', 'comment']