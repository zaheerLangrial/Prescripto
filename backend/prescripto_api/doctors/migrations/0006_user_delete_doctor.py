# Generated by Django 4.2.16 on 2024-10-31 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('doctors', '0005_doctor_experience'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('image', models.ImageField(blank=True, null=True, upload_to='doctors/')),
                ('experience', models.PositiveIntegerField(default=0)),
                ('is_active', models.BooleanField(default=True)),
                ('role', models.CharField(choices=[('doctor', 'Doctor'), ('patient', 'Patient')], default='patient', max_length=10)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='doctors', to='doctors.category')),
            ],
        ),
        migrations.DeleteModel(
            name='Doctor',
        ),
    ]