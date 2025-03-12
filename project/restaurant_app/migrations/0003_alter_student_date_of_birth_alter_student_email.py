# Generated by Django 5.1.6 on 2025-03-11 21:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant_app', '0002_student_delete_restaurant'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='date_of_birth',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='student',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
    ]
