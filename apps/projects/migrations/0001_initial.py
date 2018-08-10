# Generated by Django 2.1 on 2018-08-10 07:25

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Projects',
            fields=[
                ('projects_id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='projects的唯一id，pk', primary_key=True, serialize=False, verbose_name='一个projects的id')),
                ('projects_name', models.TextField(help_text='一个项目的项目名', verbose_name='项目名')),
                ('projects_info', models.TextField(help_text='一个项目的介绍信息', verbose_name='介绍')),
                ('projects_complete', models.BooleanField(default=False, help_text='projects是否被标记为完成', verbose_name='是否完成')),
                ('projects_create_at', models.DateTimeField(auto_now_add=True, help_text='projects创建的时间戳', verbose_name='创建时间戳')),
                ('projects_update_at', models.DateTimeField(auto_now=True, help_text='每次数据修改的时间戳', verbose_name='更新时间戳')),
                ('projects_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.Users')),
            ],
        ),
    ]
