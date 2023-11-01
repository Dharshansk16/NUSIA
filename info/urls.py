from django.urls import path
from .import views


urlpatterns = [
    path('', views.home, name='home'),
    path('profile/<str:pk>/', views.studentProfile , name="stud-profile"),
    path('add/', views.add, name ="add")


]



