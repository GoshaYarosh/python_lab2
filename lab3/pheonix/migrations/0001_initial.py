# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-08 20:49
from __future__ import unicode_literals

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0007_alter_validators_add_error_messages'),
    ]

    operations = [
        migrations.CreateModel(
            name='Channel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('description', models.CharField(blank=True, max_length=400, null=True)),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'channel',
                'verbose_name_plural': 'channels',
                'default_related_name': 'channels',
            },
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'ordering': ['name'],
                'verbose_name': 'member',
                'verbose_name_plural': 'members',
                'default_related_name': 'members',
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('send_at', models.DateTimeField(auto_now=True)),
            ],
            options={
                'ordering': ['-send_at'],
                'verbose_name': 'message',
                'verbose_name_plural': 'messages',
                'default_related_name': 'messages',
            },
        ),
        migrations.CreateModel(
            name='Notification',
            fields=[
                ('message_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pheonix.Message')),
                ('title', models.CharField(max_length=100)),
                ('view', models.CharField(choices=[('info', 'Information'), ('alert', 'Alert'), ('warning', 'Warning'), ('success', 'Success')], default='info', max_length=6)),
            ],
            options={
                'ordering': ['view', 'title'],
                'verbose_name': 'Notification message',
                'verbose_name_plural': 'Notification messages',
            },
            bases=('pheonix.message',),
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('message_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='pheonix.Message')),
                ('title', models.CharField(max_length=100)),
                ('description', models.CharField(max_length=400, null=True)),
            ],
            options={
                'ordering': ['title'],
                'verbose_name': 'Post',
                'verbose_name_plural': 'Posts',
            },
            bases=('pheonix.message',),
        ),
        migrations.AddField(
            model_name='message',
            name='channel',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='pheonix.Channel'),
        ),
        migrations.AddField(
            model_name='message',
            name='send_by',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='pheonix.Member'),
        ),
    ]