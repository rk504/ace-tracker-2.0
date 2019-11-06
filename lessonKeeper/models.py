from django.db import models

# Create your models here.
class Student(models.Model):
    name = models.CharField(max_length=100)
    lesson_day = models.CharField(max_length=10)
    lesson_time = models.CharField(max_length=10)
    lesson_length = models.CharField(max_length=3)
    lesson_location = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Contact(models.Model):
    parent_name = models.CharField(max_length=100)
    email = models.CharField(max_length=180)
    phone = models.CharField(max_length= 15)
    student = models.ForeignKey(Student, on_delete = models.CASCADE, related_name='contact')

    def __str__(self):
        return self.student
