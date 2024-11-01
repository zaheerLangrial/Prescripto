# Generated by Django 4.2.16 on 2024-10-31 13:54

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('stu_name', models.CharField(max_length=30)),
                ('roll_number', models.IntegerField(max_length=10)),
                ('level', models.IntegerField(max_length=10)),
                ('father_name', models.CharField(max_length=30)),
                ('section', models.CharField(max_length=10)),
            ],
        ),
    ]
