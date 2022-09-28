from django.db import models
from django.contrib.auth.models import User
from datetime import date


class Course(models.Model):
    COURSE_TYPE = [
        ('CORE', 'Core'),
        ('CR', 'Close Reading'),
        ('SMR', 'Seminar'),
    ]
    name = models.CharField(max_length=200)
    sub_heading = models.CharField(max_length=200, blank=True, null=True)
    course_type = models.CharField(max_length=200, choices=COURSE_TYPE, default='CORE')
    description = models.TextField()
    instructor = models.CharField(max_length=20, default='To be Announced')
    start_date = models.DateField('start date')
    end_date = models.DateField('end date')
    price = models.IntegerField(default=0)
    rebate_per_session = models.IntegerField(default=0)

    @property
    def has_started(self):
        return date.today() > self.start_date

    @property
    def has_finished(self):
        return date.today() > self.end_date

    def __str__(self):
        return self.name

class Student(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    student = models.OneToOneField(User, on_delete=models.CASCADE)
    # Many-to-Many relationship with Courses.
    courses = models.ManyToManyField(Course, through='Enrollment')

    def __str__(self):
        return self.student.username

class Session(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    date = models.DateTimeField()
    link = models.CharField(max_length=200, blank=True, null=True)
    readings = models.TextField(blank=True, null=True)
    session_number = models.IntegerField(default=0)

    def __str__(self):
        return 'session' + str(self.session_number)

class Enrollment(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    date_joined = models.DateField()
    finished = models.BooleanField(default=False)


    def __str__(self):
        return self.student.username + '-' + self.course.name
