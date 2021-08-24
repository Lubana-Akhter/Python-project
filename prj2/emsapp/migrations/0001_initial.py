# Generated by Django 3.2.5 on 2021-08-09 01:06

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(blank=True, max_length=254, unique=True)),
                ('dob', models.DateField(blank=True, default=datetime.datetime.now)),
                ('gender', models.CharField(choices=[('Male', 'Male'), ('Female', 'Female')], default='Male', max_length=6)),
                ('salary', models.DecimalField(blank=True, decimal_places=2, max_digits=8, null=True)),
                ('photo', models.FileField(blank=True, default='empimage/blank.jpg', upload_to='empimage')),
                ('Department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='emsapp.department')),
            ],
        ),
    ]
