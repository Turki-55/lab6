from django.urls import path
from . import views


urlpatterns = [
    path('students/', views.students, name='students'),
    path('courses/', views.courses, name='courses'),
    path('students/', views.students, name='students'),
    path('students/<int:student_id>/', views.details, name='details'),
    path('courses/', views.courses, name='courses'),
]
