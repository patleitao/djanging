from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('courses/', views.course_list, name='courses'),
    path('menu/', views.menu, name='menu')
]