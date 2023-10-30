from django.conf import settings
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView as AuthPasswordChangeView
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import CreateView
from django.views.generic.detail import DetailView
from django.contrib import messages
from .models import Profile
from django.http import HttpResponse, HttpResponseForbidden
from django.views import View
from .forms import UserForm, ProfileForm, CustomUserCreationForm
from django.contrib.auth.models import User

class ProfileUpdateView(View):
    def get(self, request):
        user = get_object_or_404(User, pk=request.user.pk)
        user_form = UserForm(initial = {
            'first_name': user.first_name,
            'last_name': user.last_name,
        })
        
        if hasattr(user, 'profile'):
            profile = user.profile
            profile_form = ProfileForm(initial={
                'nickname': profile.nickname,
                'profile_image': profile.profile_image,
            })
        else:
            profile_form = ProfileForm()
            
        return render(request, 'accounts/profile_update.html', {"user_form": user_form, "profile_form": profile_form})
    
    def post(self, request):
        u = User.objects.get(id=request.user.pk)        # 로그인중인 사용자 객체를 얻어옴
        user_form = UserForm(request.POST, instance=u)  # 기존의 것의 업데이트하는 것 이므로 기존의 인스턴스를 넘겨줘야한다. 기존의 것을 가져와 수정하는 것

        # User 폼
        if user_form.is_valid():
            user_form.save()

        if hasattr(u, 'profile'):
            profile = u.profile
            profile_form = ProfileForm(request.POST, request.FILES, instance=profile) # 기존의 것 가져와 수정하는 것
        else:
            profile_form = ProfileForm(request.POST, request.FILES) # 새로 만드는 것

        # Profile 폼
        if profile_form.is_valid():
            profile = profile_form.save(commit=False) # 기존의 것을 가져와 수정하는 경우가 아닌 새로 만든 경우 user를 지정해줘야 하므로
            profile.user = u
            profile.save()

        return redirect('accounts:profile') # 수정된 화면 보여주기

profile_update = ProfileUpdateView.as_view()



signup = CreateView.as_view(
    form_class = CustomUserCreationForm,
    template_name = 'accounts/form.html',
    success_url = '/accounts/login/'
)

login = LoginView.as_view(
    template_name = 'accounts/form.html',
)

logout = LogoutView.as_view(
    next_page = '/accounts/login/'
)

@login_required
def profile(request):
    return render(request, 'accounts/profile.html')

@login_required
def change_password(request):
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Password successfully changed')
            return redirect('accounts:profile')
        else:
            messages.error(request, 'Password not changed')
    else:
        form = PasswordChangeForm(request.user)
        return render(request, 'accounts/change_password.html',{'form':form})