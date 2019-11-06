from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name = 'student_list'),
    path('students/<int:pk>', views.student_detail, name = 'student_detail'),

]
