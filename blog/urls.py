from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    
    path('post/<int:pk>/', views.blog_detail, name='blog_detail'),
    
    path('category/<str:category_name>/', views.blog_category, name='blog_category'),
]