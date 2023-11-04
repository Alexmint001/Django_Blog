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
    
    labels =''
    class Meta:
        model = Comment
        fields = ['content']
        widgets = {
            'content': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }
        labels = {
            'content': '',
        }

class RecommentForm(forms.ModelForm):
    class Meta:
        model = Recomment
        fields = ['content']
        widgets = {
            'content': forms.TextInput(
                attrs={
                    'class': 'form-control'
                }
            )
        }
