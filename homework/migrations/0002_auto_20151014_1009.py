# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('homework', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=100)),
                ('type1', models.CharField(blank=True, null=True, choices=[('1', '本科生'), ('2', '研究生'), ('3', '教师'), ('4', '访客')], max_length=20)),
                ('stu_num', models.CharField(max_length=20)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='auth_type',
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='groups',
        ),
        migrations.RemoveField(
            model_name='newuser',
            name='user_permissions',
        ),
        migrations.DeleteModel(
            name='NewUser',
        ),
        migrations.DeleteModel(
            name='user_type',
        ),
    ]
