from django.urls import path
from . import views

app_name = 'blog'

urlpatterns = [
    path('', views.post_list, name = 'post_list'),    
    path('new/', views.post_new, name='post_new'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('<int:pk>/delete/', views.post_delete, name='post_delete'),
    path('<str:category_name>/', views.categoryview, name='category'),
    path('tag/<str:tag_name>/', views.tagview, name='tagview'),
    path('<int:pk>/comment/new/', views.comment_new, name='comment_new'),
    path('<int:pk>/comment/edit/', views.comment_edit, name='comment_edit'),
    path('<int:pk>/comment/delete/', views.comment_delete, name='comment_delete'),
    path('<int:pk>/comment/<int:c_pk>/recomment', views.create_recomment, name='create_recomment'),
]
