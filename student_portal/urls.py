from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    
    
    path('', views.home, name='home'),
    
    path('student/login/', views.student_login, name='student_login'),
    path('student/register/', views.student_register, name='student_register'),
    path('student/dashboard/', views.student_dashboard, name='student_dashboard'),

    path('admin/login/', views.admin_login, name='admin_login'),
    path('admin/dashboard/', views.admin_dashboard, name='admin_dashboard'),

    path('logout/', views.user_logout, name='logout'),
]
