# Generated by Django 3.2.15 on 2022-09-21 22:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0002_auto_20220920_2137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='instructor',
            field=models.CharField(default='To be Announced', max_length=20),
        ),
        migrations.DeleteModel(
            name='Instructor',
        ),
    ]
