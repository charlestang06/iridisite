# Generated by Django 5.0.2 on 2024-02-29 22:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutoring_student', '0002_alter_student_additionalcomments_alter_student_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tutoringsession',
            name='duration',
            field=models.DecimalField(decimal_places=1, max_digits=2, validators=[django.core.validators.MaxValueValidator(1.5)], verbose_name='Duration of Session (Hours)'),
        ),
    ]
