# Generated by Django 2.0 on 2020-06-03 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('marks', models.CharField(max_length=4)),
                ('rank', models.CharField(max_length=3)),
            ],
        ),
    ]
