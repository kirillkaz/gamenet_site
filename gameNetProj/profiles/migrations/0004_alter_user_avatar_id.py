# Generated by Django 4.2.3 on 2023-09-09 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profiles', '0003_alter_userimages_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar_id',
            field=models.IntegerField(default=0),
        ),
    ]
