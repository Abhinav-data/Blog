# Generated by Django 3.0.2 on 2020-01-30 13:21

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0005_auto_20200130_1645'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogpost',
            name='publish_date',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='timestamp',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='blogpost',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
