# Generated by Django 2.0 on 2020-06-04 14:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0007_auto_20200604_1927'),
    ]

    operations = [
        migrations.CreateModel(
            name='Students',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Marks', models.CharField(max_length=4)),
            ],
        ),
        migrations.DeleteModel(
            name='Student',
        ),
    ]
