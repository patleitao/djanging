# Generated by Django 3.2.15 on 2022-09-26 16:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0007_course_sub_heading'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='course_type',
            field=models.CharField(choices=[('CORE', 'Core'), ('CR', 'Close Reading'), ('SMR', 'Seminar')], default='CORE', max_length=200),
        ),
    ]
