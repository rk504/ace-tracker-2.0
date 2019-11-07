from django.shortcuts import render, redirect
from .models import Student, Contact
from .forms import StudentForm, ContactForm

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

def student_edit(request, pk):
    student = Student.objects.get(pk=pk)
    if request.method == "POST":
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            student = form.save()
            return redirect('student_detail', pk=student.pk)
    else:
        form = StudentForm(instance=student)
    return render(request, 'student_form.html', {'form': form})

def student_delete(request, pk):
    Student.objects.get(id=pk).delete()
    return redirect('student_list')

def contact_list(request):
    contacts = Contact.objects.all()
    return render(request, 'contact_list.html', {'contacts': contacts})

def contact_detail(request, pk):
    contact = Contact.objects.get(id = pk)
    return render(request, 'contact_detail.html', {'contact': contact})

def contact_create(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            contact = form.save()
            return redirect('contact_detail', pk=contact.pk)
    else:
        form = ContactForm()
    return render(request, 'contact_form.html', {'form': form})

def contact_edit(request, pk):
    contact = Contact.objects.get(pk=pk)
    if request.method == "POST":
        form = ContactForm(request.POST, instance=contact)
        if form.is_valid():
            contact = form.save()
            return redirect('contact_detail', pk=contact.pk)
    else:
        form = ContactForm(instance=contact)
    return render(request, 'contact_form.html', {'form': form})

def contact_delete(request, pk):
    Contact.objects.get(id=pk).delete()
    return redirect('contact_list')
