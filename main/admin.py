from django.contrib import admin

# Register your models here.
from .models import Student, Course, Session, Enrollment

admin.site.register(Student)
admin.site.register(Course)
admin.site.register(Session)
admin.site.register(Enrollment)