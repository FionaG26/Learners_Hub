from django.shortcuts import render, get_object_or_404, redirect
from .models import Course
from .forms import CourseForm

def online_courses(request):
    return render(request, 'courses/online_courses.html')

def books(request):
    return render(request, 'courses/books.html')

def blogs(request):
    return render(request, 'courses/blogs.html')

def course_list(request):
    courses = Course.objects.all()
    return render(request, 'courses/course_list.html', {'courses': courses})


def course_detail(request, pk):
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'courses/course_detail.html', {'course': course})


def course_create(request):
    print("Course Create View Called")
    if request.method == 'POST':
        print("POST Request")
        form = CourseForm(request.POST)
        if form.is_valid():
            print("Form is Valid")
            course = form.save()
            return redirect('course_detail', pk=course.pk)
        else:
            print("Form is Invalid")
    else:
        print("GET Request")
        form = CourseForm()

    print("Rendering Form")
    return render(request, 'courses/course_form.html', {'form': form})
