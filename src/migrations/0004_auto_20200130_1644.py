# Generated by Django 3.0.2 on 2020-01-30 11:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('src', '0003_auto_20200130_1530'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='content',
            field=models.TextField(default='Hello'),
        ),
    ]
