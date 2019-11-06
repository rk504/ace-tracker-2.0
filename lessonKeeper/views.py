from django.shortcuts import render
from .models import Student, Contact

# Create your views here.
def student_list(request):
    students = Student.objects.all()
    return render(request, 'student_list.html', {'students': students})

def student_detail(request, pk):
    student = Student.objects.get(id = pk)
    return render(request, 'student_detail.html', {'student': student})

def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            student = form.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm()
    return render(request, 'student_form.html', {'form': form})

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})

def contact_detail(request, pk):
    contact = Contact.objects.get(id = pk)
    return render(request, 'contact_detail.html', {'contact': contact})

