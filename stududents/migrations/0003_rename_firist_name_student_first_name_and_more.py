# Generated by Django 4.2.3 on 2023-07-24 16:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('stududents', '0002_rename_students_student'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='firist_name',
            new_name='first_name',
        ),
        migrations.RenameField(
            model_name='student',
            old_name='gta',
            new_name='gpa',
        ),
    ]
