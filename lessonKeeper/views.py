from django.shortcuts import render
from .models import Student, Contact

# Create your views here.
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_detail(request, pk):
    student = Student.objects.get(id = pk)
    return render(request, 'student_detail.html', {'student': student})

