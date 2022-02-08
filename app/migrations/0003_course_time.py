# Generated by Django 3.2.9 on 2021-12-08 09:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20211129_1253'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course_time',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('create_time', models.DateTimeField(auto_now_add=True, help_text='创建时间', verbose_name='create_time')),
                ('last_time', models.DateTimeField(auto_now=True, help_text='上次登录时间', verbose_name='last_time')),
                ('token', models.CharField(help_text='uuid', max_length=36, verbose_name='token')),
                ('is_delete', models.BooleanField(help_text='是否删除', verbose_name='is_delete')),
                ('czy', models.CharField(help_text='操作人员', max_length=32, verbose_name='czy')),
                ('start_time', models.DateTimeField(help_text='课程开始时间', verbose_name='start_time')),
                ('end_time', models.DateTimeField(help_text='课程结束时间', verbose_name='end_time')),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.course')),
                ('teacher', models.ManyToManyField(to='app.teacher')),
            ],
        ),
    ]
