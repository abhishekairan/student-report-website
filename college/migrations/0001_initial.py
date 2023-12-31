# Generated by Django 4.1.10 on 2023-10-30 14:14

from django.db import migrations, models
import django.db.models.deletion
import student.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Course')),
                ('duration', models.CharField(choices=[(1, '1 Year'), (2, '2 Year'), (3, '3 Year'), (4, '4 Year'), (5, '5 Year'), (6, '6 Year'), (7, '7 Year'), (8, '8 Year')], max_length=10, verbose_name='Duration')),
                ('sems', models.CharField(choices=[(1, '1 Sem'), (2, '2 Sem'), (3, '3 Sem'), (4, '4 Sem'), (5, '5 Sem'), (6, '6 Sem'), (7, '7 Sem'), (8, '8 Sem'), (9, '9 Sem'), (10, '10 Sem'), (11, '11 Sem'), (12, '12 Sem'), (13, '13 Sem'), (14, '14 Sem'), (15, '15 Sem'), (16, '16 Sem')], max_length=10, verbose_name='Semisters')),
                ('course_type', models.CharField(choices=[('UG', 'UG'), ('PG', 'PG'), ('PHD', 'PHD')], max_length=50, verbose_name='Course Type')),
                ('fees', models.IntegerField(verbose_name='Fees')),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('facultyID', models.CharField(max_length=15, verbose_name='Faculty ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('phone_no', models.CharField(max_length=15, validators=[student.models.only_int], verbose_name='Phone Number')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='Email')),
                ('address', models.TextField(verbose_name='Address')),
                ('image', models.ImageField(null=True, upload_to='college/image/', verbose_name='Image')),
                ('department', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='college.department')),
            ],
        ),
        migrations.AddField(
            model_name='department',
            name='dean',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='departmentDean', to='college.faculty'),
        ),
        migrations.AddField(
            model_name='department',
            name='hod',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='departmentHOD', to='college.faculty'),
        ),
    ]
