# Generated by Django 4.2.3 on 2023-08-17 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('groups', '0003_alter_group_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='group',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]