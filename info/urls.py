from django.urls import path
from .import views


urlpatterns = [
    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('', views.home, name='home'),
    path('profile/<str:pk>/', views.studentProfile , name="stud-profile"),
    path('add/', views.add, name ="add"),
    path('update/<str:pk>/', views.update , name = 'update'),
    path('delete/<str:pk>', views.delete , name ='delete'),
]



