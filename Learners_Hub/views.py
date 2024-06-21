from django.shortcuts import render
from courses.models import Course
from django.contrib.auth.decorators import login_required


def home(request):
    courses = Course.objects.all()
    return render(request, 'home.html', {'courses': courses})
