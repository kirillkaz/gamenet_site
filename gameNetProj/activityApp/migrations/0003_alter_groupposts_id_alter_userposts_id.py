# Generated by Django 4.2.3 on 2023-09-13 14:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('activityApp', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='groupposts',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='userposts',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
