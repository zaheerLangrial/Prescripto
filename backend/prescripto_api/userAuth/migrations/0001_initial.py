# Generated by Django 4.2.16 on 2024-11-01 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DemoUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_name', models.CharField(max_length=50, unique=True)),
                ('password', models.CharField(max_length=8)),
                ('email', models.EmailField(max_length=100, unique=True)),
            ],
        ),
    ]
