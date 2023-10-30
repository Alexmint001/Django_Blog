from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    # 카테고리 반영은 보류
    # path('', views.post_main, name = 'post_main'),
    # path('<str:category_name>/', views.post_list, name = 'post_list'),    
    path('', views.post_list, name = 'post_list'),    
    path('new/', views.post_new, name='post_new'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('<str:category_name>/', views.CategoryView, name='category'),
    # path('tag/<str:tag>/', views.posttag, name='posttag'),
]
