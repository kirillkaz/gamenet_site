# Generated by Django 4.2.3 on 2023-08-19 02:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0007_alter_group_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='avatar',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]