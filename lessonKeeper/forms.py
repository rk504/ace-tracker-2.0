from django import forms
from .models import Student, Contact

class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        fields = ('name', 'lesson_location', 'lesson_day', 'lesson_time', 'lesson_length',)


class ContactForm(forms.ModelForm):

    class Meta:
        model = Contact
        fields = ('student', 'contact_name', 'relationship', 'email', 'phone',)



