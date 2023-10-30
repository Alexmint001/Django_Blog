from django.urls import path
from . import views
# from django.conf import settings
# from django.conf.urls.static import static

app_name = 'accounts'

urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('profile/', views.profile, name='profile'),
    path('change_password/', views.change_password, name="re_password"),
    path('profile_update/', views.profile_update, name='profile_update')
]

# urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)