# Generated by Django 2.2.8 on 2019-12-04 12:18

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Astronaut',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=30, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=30, verbose_name='Last Name')),
                ('date_of_birth', models.DateField(blank=True, default=None, null=True, verbose_name='Date of Birth')),
            ],
            options={
                'verbose_name': 'Astronaut',
                'verbose_name_plural': 'Astronauts',
            },
        ),
    ]
