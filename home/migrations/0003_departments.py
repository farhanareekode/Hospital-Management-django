# Generated by Django 3.2.12 on 2024-07-31 03:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_patientprofile_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Departments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dep_name', models.CharField(max_length=100)),
                ('dep_description', models.TextField()),
            ],
        ),
    ]
