# Generated by Django 4.2.3 on 2023-08-14 10:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(choices=[('Steam', 'Steam'), ('Origin', 'Origin'), ('Blizard', 'Blizard')], default='Steam', max_length=100)),
                ('image', models.CharField(blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='Platform_Link',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('link', models.CharField(blank=True)),
                ('platform_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='platforms.platform')),
            ],
        ),
    ]
