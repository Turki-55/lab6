from django.shortcuts import render, redirect
from .models import Student, Course
from .forms import StudentForm, CourseForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Student, Course
from .forms import StudentForm, CourseForm, RegistrationForm


def students(request):
    students_list = Student.objects.all()
    form = StudentForm()
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('students')
    return render(request, 'students.html', {'students_list': students_list, 'form': form})

def courses(request):
    courses_list = Course.objects.all()
    form = CourseForm()
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('courses')
    return render(request, 'courses.html', {'courses_list': courses_list, 'form': form})


def details(request, student_id):
    student = get_object_or_404(Student, pk=student_id)
    available_courses = Course.objects.exclude(students=student)
    form = RegistrationForm()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            course_id = form.cleaned_data['course'].id
            student.courses.add(course_id)
            return redirect('details', student_id=student_id)
    return render(request, 'details.html', {'student': student, 'available_courses': available_courses, 'form': form})