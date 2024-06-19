from django.urls import path
from . import views

urlpatterns = [
    path('', views.course_list, name='course_list'),
    path('<int:pk>/', views.course_detail, name='course_detail'),
    path('create/', views.course_create, name='course_create'),
    path('resources/online-courses/', views.online_courses, name='online_courses'),
    path('resources/books/', views.books, name='books'),
    path('resources/blogs/', views.blogs, name='blogs'),
]
