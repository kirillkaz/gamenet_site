# Generated by Django 4.2.3 on 2023-08-14 10:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('platforms', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='platform_link',
            name='user_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='platform',
            name='users',
            field=models.ManyToManyField(blank=True, related_name='platform2users', to=settings.AUTH_USER_MODEL),
        ),
    ]
