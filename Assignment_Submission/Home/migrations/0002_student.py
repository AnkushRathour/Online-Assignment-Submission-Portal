# Generated by Django 3.2.1 on 2021-05-09 15:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Name', models.CharField(max_length=200)),
                ('Email', models.CharField(max_length=200)),
                ('Password', models.CharField(max_length=200)),
                ('Gender', models.CharField(max_length=200)),
                ('Mobile', models.CharField(max_length=200)),
                ('DOB', models.CharField(max_length=200)),
                ('Course', models.CharField(max_length=200)),
                ('Image', models.CharField(max_length=200)),
            ],
        ),
    ]
