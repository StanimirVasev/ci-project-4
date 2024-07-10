from django.urls import path
from . import views

urlpatterns = [
    path('', views.blog_list, name='blog_list'),
    path('page/<int:page>/', views.blog_list, name='blog_list_paginated'),
    path('post/<int:pk>/', views.blog_detail, name='blog_detail'),
    path('category/<str:category_name>/', views.blog_category, name='blog_category'),
    path('add/', views.add_blog, name='add_blog'),
    path('edit/<int:pk>/', views.edit_blog, name='edit_blog'),
    path('delete/<int:pk>/', views.delete_blog, name='delete_blog'),
]
