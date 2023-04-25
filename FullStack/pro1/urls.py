from django.urls import path 

from pro1 import views

urlpatterns = [
    path('home/', views.home , name='home'),
]
