from django.shortcuts import render
from django.http import HttpResponse
from .models import Course

def index(request):
    return HttpResponse("Rango says hey there world!")

def course_list(request):
 #	  name = models.CharField(max_length=200)
 #    description = models.TextField()
 #    instructor = models.CharField(max_length=20, default='To be Announced')
 #    start_date = models.DateField('start date')
 #    end_date = models.DateField('end date')
 #    price = models.IntegerField(default=0)
 #    rebate_per_session = models.IntegerField(default=0)

	course_list = Course.objects.order_by('start_date')

	past_courses, current_courses, upcoming_courses = [], [], []
	for course in course_list:
		if not course.has_started:
			upcoming_courses.append(course)
		elif not course.has_finished:
			current_courses.append(course)
		else:
			past_courses.append(course)

	context = {'past_courses': past_courses, 'current_courses': current_courses, 'upcoming_courses': upcoming_courses}
	return render(request, 'main/courses.html', context)

def menu(request):
	course_list = Course.objects.order_by('start_date')
	context = {'course_list': course_list}
	return render(request, 'main/menu.html', context)

