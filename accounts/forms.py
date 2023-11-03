from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, PasswordChangeForm as AuthPasswordChangeForm
from .models import Profile

class PasswordChangeForm(AuthPasswordChangeForm):
    def clean_new_password1(self):
        old_password = self.cleaned_data.get('old_password')
        new_password1 = self.cleaned_data.get('new_password1')
        
        if old_password and new_password1:
            if old_password == new_password1:
                raise forms.ValidationError('새로운 암호는 기존 암호와 다르게 입력해주세요.')
        return new_password1
    
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['first_name','last_name']
        widgets = {
                'first_name': forms.TextInput(
                    attrs={
                        'class': 'form-control'
                    }
                ),
                'last_name': forms.TextInput(
                    attrs={
                        'class': 'form-control'
                    }
                )
            }

class ProfileForm(forms.ModelForm):
    profile_image = forms.ImageField(required=False) # 선택적으로 입력할 수 있음.
    class Meta:
        model = Profile
        fields = ['nickname','profile_image']
        widgets = {
                'nickname': forms.TextInput(
                    attrs={
                        'class': 'form-control'
                    }
                ),
                'profile_image': forms.ClearableFileInput(
                    attrs={
                        'class': 'profile_image'
                    }
                )
            }
    
        
class CustomUserCreationForm(UserCreationForm):
    nickname = forms.CharField(max_length=64)
    profile_image = forms.ImageField(required=False)
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'nickname', 'profile_image']
        
    def save(self, commit=True):
        user = super().save(commit=False)
        if commit:
            user.save()
        profile = Profile(user=user, nickname=self.cleaned_data['nickname'])
        if 'profile_image' in self.cleaned_data:
            profile.profile_image = self.cleaned_data['profile_image']
        profile.save()
        return user