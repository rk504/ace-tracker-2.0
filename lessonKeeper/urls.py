from django.urls import path
from . import views

urlpatterns = [
    path('', views.student_list, name = 'student_list'),
    path('students/<int:pk>', views.student_detail, name = 'student_detail'),
    path('students/new', views.student_create, name = 'student_create'),
    path('students/<int:pk>/edit', views.student_edit, name = 'student_edit'),
    path('students/<int:pk>/delete', views.student_delete, name = 'student_delete'),
    path('contacts/', views.contact_list, name = 'contact_list'),
    path('contacts/<int:pk>', views.contact_detail, name = 'contact_detail'),
    path('contacts/new', views.contact_create, name = 'contact_create'),
    path('contacts/<int:pk>/edit', views.contact_edit, name = 'contact_edit'),
    path('contacts/<int:pk>/delete', views.contact_delete, name = 'contact_delete'),
]
