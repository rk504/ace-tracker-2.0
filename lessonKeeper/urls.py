from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name = 'student_list'),
    path('students/<int:pk>', views.student_detail, name = 'student_detail'),
    path('students/new', views.student_create, name = 'student_create'),
    path('contacts/', views.contact_list, name = 'contact_list'),
    path('contacts/<int:pk>', views.contact_detail, name = 'contact_detail'),
    path('contacts/new', views.contact_create, name = 'contact_create'),

]
