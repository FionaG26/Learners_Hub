from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),path('login/', views.login_view, name='login'),
    path('subscribe/', views.subscribe, name='subscribe'),
    path('profile/update/', views.update_profile, name='update_profile'),
]
