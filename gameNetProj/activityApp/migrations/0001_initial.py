# Generated by Django 4.2.3 on 2023-08-14 10:57

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Chat',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('avatar', models.CharField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='GroupPostComment',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('text', models.CharField(default=None)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='GroupPosts',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('text', models.CharField(default=None)),
                ('published', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(verbose_name=datetime.datetime.now)),
                ('text', models.CharField()),
                ('is_viewed', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='UserPostComment',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('text', models.CharField(default=None)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='UserPosts',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('date', models.DateTimeField(default=datetime.datetime.now)),
                ('text', models.CharField(default=None)),
                ('published', models.BooleanField(default=False)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
