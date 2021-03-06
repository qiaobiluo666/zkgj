# Generated by Django 3.2.9 on 2021-12-10 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_alter_teacher_image_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course_time',
            name='end_time',
            field=models.CharField(help_text='课程结束时间', max_length=64, verbose_name='end_time'),
        ),
        migrations.AlterField(
            model_name='course_time',
            name='start_time',
            field=models.CharField(help_text='课程开始时间', max_length=64, verbose_name='start_time'),
        ),
    ]
