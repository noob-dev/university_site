from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('faculties/', views.faculty, name='faculties'),
    path('departments/', views.department, name='departments'),
    path('groups/', views.group, name='groups'),
    path('subjects/', views.subject, name='subjects'),
    path('teachers/', views.teacher, name='teachers'),
    path('students/', views.student, name='students'),
]