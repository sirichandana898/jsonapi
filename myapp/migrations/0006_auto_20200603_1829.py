# Generated by Django 2.0 on 2020-06-03 12:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20200603_1826'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=100)),
                ('Marks', models.CharField(max_length=4)),
            ],
        ),
        migrations.DeleteModel(
            name='Students',
        ),
    ]