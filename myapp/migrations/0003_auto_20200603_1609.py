# Generated by Django 2.0 on 2020-06-03 10:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0002_remove_student_rank'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Student',
            new_name='Students',
        ),
    ]