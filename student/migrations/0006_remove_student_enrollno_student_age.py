# Generated by Django 4.1.10 on 2023-11-01 08:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0005_marks'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='enrollNo',
        ),
        migrations.AddField(
            model_name='student',
            name='age',
            field=models.IntegerField(default=0, verbose_name='Age'),
            preserve_default=False,
        ),
    ]
